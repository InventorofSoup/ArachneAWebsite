---
layout: default
title: Tags
permalink: /tags/
---

<header class="header page-hero">
  <p class="hero-kicker">Browse the archive</p>
  <h1 class="page-title">Tags</h1>
  <p class="page-copy">
    Explore Arachne posts by topic, game, event, and category. Select a tag below to jump to that section.
  </p>
</header>

{% assign tags = site.tags | sort %}

<section class="panel section">
  <div class="section-head">
    <h2 class="feed-title">Tag Index</h2>
    {% if tags.size > 0 %}
      <span class="small">{{ tags.size }} tag{% if tags.size != 1 %}s{% endif %}</span>
    {% endif %}
  </div>

  {% if tags.size == 0 %}
    <p class="small">No tags yet. Add tags to your posts to build this page out.</p>
  {% else %}
    <div class="tag-cloud">
      {% for tag in tags %}
        <a class="tag-chip" href="#{{ tag[0] | slugify }}">
          #{{ tag[0] }}
          <span class="tag-count">{{ tag[1].size }}</span>
        </a>
      {% endfor %}
    </div>
  {% endif %}
</section>

{% for tag in tags %}
<section class="panel section tag-section" id="{{ tag[0] | slugify }}">
  <div class="section-head">
    <h2 class="tag-heading">#{{ tag[0] }}</h2>
    <span class="small">{{ tag[1].size }} post{% if tag[1].size != 1 %}s{% endif %}</span>
  </div>

  {% assign tagged_posts = tag[1] | sort: "date" | reverse %}
  {% for post in tagged_posts %}
    <article class="post-row">
      <div class="tag">{{ post.content_type | default: "post" | upcase }}</div>
      <h3 class="hline">
        <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
      </h3>
      <p class="excerpt">{{ post.excerpt | default: post.content | strip_html | truncate: 160 }}</p>
      <div class="meta">{{ post.date | date: "%b %d, %Y" }}</div>
    </article>
    {% unless forloop.last %}<hr class="divider">{% endunless %}
  {% endfor %}
</section>
{% endfor %}
