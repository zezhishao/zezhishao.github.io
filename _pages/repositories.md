---
layout: page
permalink: /repositories/
language_alternate: /zh/repositories/
title: GitHub repositories
nav: true
nav_order: 4
description: Open-source projects for time series analysis and spatio-temporal data mining.
---

{% if site.data.repositories.github_repos %}

<div class="en-repositories">
  {% for repo in site.data.repositories.github_repos %}
    {% assign project = site.data.repositories_en[repo] %}
    {% assign repo_name = repo | split: '/' | last %}
    <section class="en-repository">
      <h2><a href="https://github.com/{{ repo }}">{{ repo_name }}</a></h2>
      <p>{{ project.description }}</p>
      <a class="repository-link" href="https://github.com/{{ repo }}" aria-label="View {{ repo_name }} on GitHub">View on GitHub <i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i></a>
    </section>
  {% endfor %}
</div>
{% endif %}
