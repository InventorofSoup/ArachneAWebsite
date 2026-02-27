---
layout: default
title: Tags
permalink: /tags/
---

<header class="header">
  <h1 class="logo" style="font-size:40px; color: var(--text);">Tags</h1>
  <p class="tagline">Browse content by topic.</p>
</header>

<section class="panel section">
  {% assign tags = site.tags | sort %}
  {% for tag in tags %}
    <h2 id="{{ tag[0] | slugify }}" style="margin-top:24px;">#{{ tag[0] }}</h2>

    {% for post in tag[1] %}
      <div class="post-row">
        <div class="tag">{{ post.content_type | default: "post" | upcase }}</div>
        <h3 class="hline">
          <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
        </h3>
        <div class="meta">{{ post.date | date: "%b %d, %Y" }}</div>
      </div>
      {% unless forloop.last %}<hr class="divider">{% endunless %}
    {% endfor %}
  {% endfor %}
</section>
