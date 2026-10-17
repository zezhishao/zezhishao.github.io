#!/usr/bin/env python3
"""Build self-hosted, SIL OFL-licensed fonts for the Chinese pages.

Requires: pip install fonttools brotli
See README-zh-fonts.md for source files and rebuilding instructions.
"""

import argparse
import logging
import shutil
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "assets/fonts/zh"


def unicode_ranges(points):
    ranges = []
    start = end = None
    for point in sorted(points):
        if start is None:
            start = end = point
        elif point == end + 1:
            end = point
        else:
            ranges.append(f"U+{start:X}" + (f"-{end:X}" if end != start else ""))
            start = end = point
    if start is not None:
        ranges.append(f"U+{start:X}" + (f"-{end:X}" if end != start else ""))
    return ", ".join(ranges)


def rename_sans_subset(font):
    # The upstream OFL reserves "Source". Give modified subsets their own
    # primary family name while retaining copyright and license metadata.
    names = {
        1: "Site Sans SC",
        3: "SiteSansSC-Bold-web-subset",
        4: "Site Sans SC Bold",
        6: "SiteSansSC-Bold",
        16: "Site Sans SC",
        17: "Bold",
    }
    for record in font["name"].names:
        if record.nameID in names:
            record.string = names[record.nameID].encode(record.getEncoding())
    if "CFF " in font:
        cff = font["CFF "].cff
        cff.fontNames = ["SiteSansSC-Bold"]
        top = cff.topDictIndex[0]
        top.FamilyName = "Site Sans SC"
        top.FullName = "Site Sans SC Bold"
        if hasattr(top, "FDArray"):
            for index, dictionary in enumerate(top.FDArray):
                dictionary.FontName = f"SiteSansSC-Bold-{index}"


def build_face(source, index, family, slug, weight, core, split=True):
    logging.getLogger("fontTools").setLevel(logging.ERROR)
    original = TTFont(source, fontNumber=index, recalcTimestamp=False)
    points = set(original.getBestCmap())
    groups = {"core": points & core} if split else {"full": points}
    if split:
        for point in sorted(points - core):
            groups.setdefault(f"{point // 1024:03x}", set()).add(point)
    rules = []
    covered = set()
    for group, glyphs in groups.items():
        if not glyphs:
            continue
        font = TTFont(source, fontNumber=index, recalcTimestamp=False)
        options = subset.Options()
        options.flavor = "woff2"
        options.name_IDs = ["*"]  # Keep copyright, family and licensing metadata.
        options.name_languages = ["*"]
        options.name_legacy = True
        options.notdef_glyph = True
        options.notdef_outline = True
        subsetter = subset.Subsetter(options=options)
        subsetter.populate(unicodes=glyphs)
        subsetter.subset(font)
        if family == "Site Sans SC":
            rename_sans_subset(font)
        font.flavor = "woff2"
        filename = f"{slug}-{group}.woff2"
        font.save(DEST / filename)
        assert not (covered & glyphs), "Overlapping Unicode subsets"
        covered.update(glyphs)
        rules.append(
            "@font-face {\n"
            f'  font-family: "{family}";\n'
            f"  src: url(\"{{{{ '/assets/fonts/zh/{filename}' | relative_url }}}}\") format(\"woff2\");\n"
            "  font-style: normal;\n"
            f"  font-weight: {weight};\n"
            "  font-display: swap;\n"
            f"  unicode-range: {unicode_ranges(glyphs)};\n"
            "}\n"
        )
    assert covered == points, "Incomplete font coverage"
    print(f"{family} {weight}: {len(points)} codepoints in {len(groups)} files", flush=True)
    return rules


def build_job(job):
    return build_face(*job)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ["belleza", "zhuque", "source-han-bold"]:
        parser.add_argument(f"--{name}", type=Path, required=True)
        parser.add_argument(f"--{name}-license", type=Path, required=True)
    args = parser.parse_args()
    logging.getLogger("fontTools").setLevel(logging.ERROR)
    DEST.mkdir(parents=True, exist_ok=True)
    # Current page characters share one small download. Other glyphs remain
    # available in Unicode chunks, so future text doesn't need a font rebuild.
    core = set(range(0x250))
    sources = [ROOT / "_pages/about_zh.md", ROOT / "_data/locales/zh.yml"]
    sources += list((ROOT / "_news").glob("*.md"))
    sources += list((ROOT / "_layouts").glob("*.liquid"))
    sources += list((ROOT / "_includes").glob("*.liquid"))
    for source in sources:
        core.update(map(ord, source.read_text()))
    jobs = [
        (args.belleza, 0, "Belleza", "belleza-regular", 400, core, False),
        (args.zhuque, 0, "Zhuque Fangsong", "zhuque-fangsong", 400, core, True),
        (args.source_han_bold, 0, "Site Sans SC", "source-han-sans-bold", 700, core, True),
    ]
    # Families write distinct files and can be compressed independently.
    with ProcessPoolExecutor(max_workers=3) as pool:
        rules = [rule for result in pool.map(build_job, jobs) for rule in result]
    stylesheet = ROOT / "assets/css/chinese-fonts.css"
    stylesheet.write_text(
        "---\n---\n/* Generated by _scripts/build_zh_fonts.py. Loaded only on Chinese pages. */\n\n"
        + "\n".join(rules)
    )
    licenses = DEST / "licenses"
    licenses.mkdir(exist_ok=True)
    for source, filename in [
        (args.belleza_license, "Belleza-OFL.txt"),
        (args.zhuque_license, "Zhuque-Fangsong-OFL.txt"),
        (args.source_han_bold_license, "Source-Han-Sans-OFL.txt"),
    ]:
        shutil.copyfile(source, licenses / filename)
    print(f"Total: {sum(p.stat().st_size for p in DEST.glob('*.woff2')) / 1024:.0f} KiB")


if __name__ == "__main__":
    main()
