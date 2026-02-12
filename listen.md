---
layout: default
title: Listen
permalink: /listen/
---

<header class="header">
  <h1 class="logo" style="font-size:40px; color: var(--text);">Listen</h1>
  <p class="tagline">Search will come next. This page will list episodes.</p>
</header>

<section class="panel section">
  <h2 class="feed-title">Episodes</h2>

  {% assign eps = site.posts | where: "content_type", "episode" | sort: "date" | reverse %}
  {% if eps.size == 0 %}
    <p class="small">No episodes posted yet.</p>
  {% endif %}

  {% for post in eps %}
    <div class="post-row">
      <div>
        <div class="tag">EPISODE</div>
        <h3 class="hline"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
        <p class="excerpt">{{ post.excerpt | default: post.content | strip_html | truncate: 140 }}</p>
        <div class="meta">{{ post.date | date: "%b %d, %Y" }}</div>
      </div>
    </div>
    {% unless forloop.last %}<hr class="divider">{% endunless %}
  {% endfor %}
</section>
