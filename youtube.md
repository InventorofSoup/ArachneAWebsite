---
layout: default
title: YouTube
permalink: /youtube/
---

<header class="header">
  <h1 class="logo" style="font-size:40px; color: var(--text);">YouTube</h1>
  <p class="tagline">All video posts, newest to oldest.</p>
</header>

<section class="panel section">
  {% assign vids = site.posts | where: "content_type", "youtube" | sort: "date" | reverse %}

  {% if vids.size == 0 %}
    <p class="small">No YouTube posts yet.</p>
  {% endif %}

  {% for post in vids %}
    <div class="post-row">
      <div class="tag">YOUTUBE</div>
      <h3 class="hline"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
      <p class="excerpt">{{ post.excerpt | default: post.content | strip_html | truncate: 160 }}</p>
      <div class="meta">{{ post.date | date: "%b %d, %Y" }}</div>
    </div>
    {% unless forloop.last %}<hr class="divider">{% endunless %}
  {% endfor %}
</section>
