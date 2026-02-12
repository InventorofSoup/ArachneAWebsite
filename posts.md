---
layout: default
title: Recent Posts
permalink: /posts/
---

<header class="header">
  <h1 class="logo" style="font-size:40px; color: var(--text);">Recent Posts</h1>
  <p class="tagline">Everything, newest to oldest. No filters.</p>
</header>

<section class="panel section">
  {% assign latest = site.posts | sort: "date" | reverse %}
  {% for post in latest %}
    <div class="post-row">
          <div>
        <div class="tag">{{ post.content_type | default: "post" | upcase }}</div>
        <h3 class="hline"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
        <p class="excerpt">{{ post.excerpt | default: post.content | strip_html | truncate: 140 }}</p>
        <div class="meta">{{ post.date | date: "%b %d, %Y" }}</div>
      </div>
    </div>
    {% unless forloop.last %}<hr class="divider">{% endunless %}
  {% endfor %}
</section>
