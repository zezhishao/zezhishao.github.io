---
layout: page
permalink: /zh/repositories/
language_alternate: /repositories/
lang: zh-CN
title: 开源
description: 时间序列分析与时空数据挖掘相关的开源项目
nav: false
---

<div class="zh-repositories">
  {% for repo in site.data.repositories.github_repos %}
    {% assign project = site.data.repositories_zh[repo] %}
    {% assign repo_name = repo | split: '/' | last %}
    <section class="zh-repository">
      <h2><a href="https://github.com/{{ repo }}">{{ repo_name }}</a></h2>
      <p>{{ project.description }}</p>
      <a class="zh-repository-link" href="https://github.com/{{ repo }}" aria-label="在 GitHub 查看 {{ repo_name }}">查看项目 <i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i></a>
    </section>
  {% endfor %}
</div>
