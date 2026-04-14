---
layout: default
title: YouTube
permalink: /youtube/
---

<header class="header page-hero">
  <p class="hero-kicker">Video archive</p>
  <h1 class="page-title">YouTube</h1>
  <p class="page-copy">
    Watch the latest Arachne video content, then browse older uploads, coverage, and archive posts below.
  </p>
</header>

{% assign vids = site.posts | where: "content_type", "youtube" | sort: "date" | reverse %}

<section class="panel section">
  <div class="section-head">
    <h2 class="feed-title">Latest Video</h2>
    <a class="section-link" href="https://www.youtube.com/@ArachneAnGamingYoutubeChanne" target="_blank" rel="noopener noreferrer">Open channel ↗</a>
  </div>

  {% if vids.size > 0 %}
    {% assign post = vids.first %}
    <article class="post-row featured-row">
      <div class="tag">YOUTUBE</div>
      <h3 class="hline"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
      <p class="excerpt">{{ post.excerpt | default: post.content | strip_html | truncate: 220 }}</p>
      <div class="meta">{{ post.date | date: "%b %d, %Y" }}</div>
    </article>
  {% else %}
    <p class="small">No YouTube posts yet.</p>
  {% endif %}
</section>

<section class="panel section" style="margin-top:16px;">
  <div class="section-head">
    <h2 class="feed-title">Video Posts</h2>
    {% if vids.size > 0 %}
      <span class="small">{{ vids.size }} video{% if vids.size != 1 %}s{% endif %}</span>
    {% endif %}
  </div>

  {% if vids.size == 0 %}
    <p class="small">No YouTube posts yet.</p>
  {% else %}
    {% for post in vids offset:1 %}
      <article class="post-row">
        <div class="tag">YOUTUBE</div>
        <h3 class="hline"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
        <p class="excerpt">{{ post.excerpt | default: post.content | strip_html | truncate: 180 }}</p>
        <div class="meta">{{ post.date | date: "%b %d, %Y" }}</div>
      </article>
      {% unless forloop.last %}<hr class="divider">{% endunless %}
    {% endfor %}
  {% endif %}
</section>
