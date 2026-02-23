---
layout: default
title: Listen
permalink: /listen/
---

<header class="header">
  <h1 class="logo" style="font-size:40px; color: var(--text);">Listen</h1>
  <p class="tagline">Check out our latest episode or look for a specific episode below!</p>
</header>

<section class="panel section">
  <h2 class="feed-title">Latest Episode</h2>

<p class="small" style="margin-top:6px;">
</p>

  <div style="margin-top:14px; border-radius:14px; overflow:hidden; border:1px solid rgba(255,255,255,0.06);">
    <iframe
      style="width:100%; height:380px; border:0;"
      src="https://open.spotify.com/embed/show/1X2k6XBqV2LJF9Jee0cdE2?utm_source=generator&theme=0"
      allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
      loading="lazy">
    </iframe>
  </div>

  <p class="small" style="margin-top:12px;">
    </p>
</section>

<section class="panel section" style="margin-top:16px;">
  <h2 class="feed-title">Episode Write-ups</h2>

  {% assign eps = site.posts | where: "content_type", "episode" | sort: "date" | reverse %}

  {% if eps.size == 0 %}
    <p class="small">No episode posts yet. Add new episodes in <code>_posts</code> with <code>content_type: episode</code>.</p>
  {% endif %}

  {% for post in eps %}
    <div class="post-row">
      <div class="tag">EPISODE</div>
      <h3 class="hline"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
      <p class="excerpt">{{ post.excerpt | default: post.content | strip_html | truncate: 170 }}</p>
      <div class="meta">{{ post.date | date: "%b %d, %Y" }}</div>
    </div>
    {% unless forloop.last %}<hr class="divider">{% endunless %}
  {% endfor %}
</section>
