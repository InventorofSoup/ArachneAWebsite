---
layout: default
title: Listen
permalink: /listen/
---

<header class="header page-hero">
  <p class="hero-kicker">Podcast archive</p>
  <h1 class="page-title">Listen</h1>
  <p class="page-copy">
    Start with the latest episode, then dig through the archive for older write-ups, discussions, and tabletop coverage.
  </p>
</header>

{% assign eps = site.posts | where: "content_type", "episode" | sort: "date" | reverse %}

<section class="panel section">
  <div class="section-head">
    <h2 class="feed-title">Latest Episode</h2>
    <a class="section-link" href="https://open.spotify.com/show/1X2k6XBqV2LJF9Jee0cdE2" target="_blank" rel="noopener noreferrer">Open in Spotify ↗</a>
  </div>

  <p class="small">
    Listen directly from Spotify, then scroll down for episode write-ups and archive entries.
  </p>

  <div class="listen-embed-wrap">
    <iframe
      class="listen-embed"
      src="https://open.spotify.com/embed/show/1X2k6XBqV2LJF9Jee0cdE2?utm_source=generator&theme=0"
      allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
      loading="lazy">
    </iframe>
  </div>
</section>

<section class="panel section" style="margin-top:16px;">
  <div class="section-head">
    <h2 class="feed-title">Episode Write-ups</h2>
    {% if eps.size > 0 %}
      <span class="small">{{ eps.size }} episode{% if eps.size != 1 %}s{% endif %}</span>
    {% endif %}
  </div>

  {% if eps.size == 0 %}
    <p class="small">No episode posts yet. Add new episodes in <code>_posts</code> with <code>content_type: episode</code>.</p>
  {% endif %}

  {% for post in eps %}
    <article class="post-row">
      <div class="tag">EPISODE</div>
      <h3 class="hline"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
      <p class="excerpt">{{ post.excerpt | default: post.content | strip_html | truncate: 190 }}</p>
      <div class="meta">{{ post.date | date: "%b %d, %Y" }}</div>
    </article>
    {% unless forloop.last %}<hr class="divider">{% endunless %}
  {% endfor %}
</section>
