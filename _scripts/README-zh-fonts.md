# Chinese-page web fonts

`assets/css/chinese-fonts.css` and `assets/fonts/zh/` contain the self-hosted
Belleza regular, Zhuque Fangsong regular, and Source Han Sans SC bold fonts.
All three use the SIL Open Font License 1.1. Copyright and licensing metadata
remain in the fonts, with full license texts in `assets/fonts/zh/licenses/`.

Sources:

- [Belleza](https://github.com/google/fonts/tree/main/ofl/belleza)
- [Zhuque Fangsong v0.212](https://github.com/TrionesType/zhuque/releases/tag/v0.212)
- [Source Han Sans SC bold](https://github.com/adobe-fonts/source-han-sans/tree/release/OTF/SimplifiedChinese)

Only pages with `lang: zh-CN` load this stylesheet. Font declarations
deliberately omit `local()` so the same bundled fonts load on every
computer. `font-display: swap` keeps text readable while loading.

Latin text uses Belleza throughout the Chinese page. Chinese body text uses
Zhuque Fangsong; Chinese headings and navigation use Source Han Sans SC bold.
Belleza is available in regular only, so the browser synthesizes bold Latin
text where the existing layout calls for bold. Code and icon fonts keep their
existing specialized families. English pages keep their original Roboto typeface
and do not load this font stylesheet.
The Source Han subsets use the internal/CSS family name `Site Sans SC` to
respect the upstream reserved font name; their glyph designs remain unchanged.

To rebuild from the upstream font files and their accompanying licenses:

```sh
python -m pip install fonttools brotli
python _scripts/build_zh_fonts.py \
  --belleza /path/Belleza-Regular.ttf --belleza-license /path/Belleza-OFL.txt \
  --zhuque /path/ZhuqueFangsong-Regular.ttf --zhuque-license /path/Zhuque-OFL.txt \
  --source-han-bold /path/SourceHanSansSC-Bold.otf \
  --source-han-bold-license /path/SourceHanSans-LICENSE.txt
```

The Chinese fonts include a small core subset for current content and additional
Unicode subsets for the rest of the source font. Browsers fetch only the subsets
needed for the displayed text. New text can use those remaining glyphs without
rebuilding; rebuilding merely optimizes which characters share the core download.
