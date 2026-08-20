---
layout: default
title: Posts
permalink: /posts/
---

{% assign standard_posts = site.posts | where: "content_type", "post" %}
{% assign announcements = site.posts | where: "content_type", "announcement" %}
{% assign written_posts = standard_posts | concat: announcements | sort: "date" | reverse %}

<header class="page-hero">
  <p class="signal-kicker"><span aria-hidden="true"></span> From the crew</p>
  <h1 class="page-title">Posts</h1>
  <p class="page-copy">News, announcements, community updates, and everything else we want to share beyond the shows.</p>
</header>

<section class="broadcast-section">
  <div class="section-head">
    <div>
      <p class="signal-label">Latest updates</p>
      <h2 class="section-title">From Arachne</h2>
    </div>
    <span class="archive-count">{{ written_posts.size }} {% if written_posts.size == 1 %}post{% else %}posts{% endif %}</span>
  </div>

  <div class="media-grid archive-grid">
    {% for post in written_posts %}
      {% assign card_image = post.thumbnail | default: "/assets/images/arachne-no-text.png" %}
      <article class="media-card">
        <a class="media-card-image" href="{{ site.baseurl }}{{ post.url }}">
          <img src="{{ card_image }}" alt="" loading="lazy">
          <span class="media-card-action">READ</span>
        </a>
        <div class="media-card-body">
          <div class="media-card-meta">
            <span>{{ post.series | default: "Arachne update" }}</span>
            <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %d, %Y" }}</time>
          </div>
          <h3><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
          <p>{{ post.excerpt | default: post.content | strip_html | truncate: 150 }}</p>
        </div>
      </article>
    {% endfor %}
  </div>
</section>
