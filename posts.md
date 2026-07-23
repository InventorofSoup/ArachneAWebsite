---
layout: default
title: Archive
permalink: /posts/
---

{% assign all = site.posts | sort: "date" | reverse %}

<header class="page-hero">
  <p class="signal-kicker"><span aria-hidden="true"></span> Everything Arachne</p>
  <h1 class="page-title">Archive</h1>
  <p class="page-copy">Filter every podcast episode, video, event, and community update received by Arachne.</p>
</header>

<section class="broadcast-section archive-section">
  <div class="section-head">
    <div>
      <p class="signal-label">Browse by format</p>
      <h2 class="section-title">Latest and past posts</h2>
    </div>
    <span class="archive-count">{{ all.size }} posts</span>
  </div>

  <div class="archive-filter-row">
    <span class="archive-filter-label">Format</span>
    <div class="archive-filters" data-archive-filters data-filter-group="format" aria-label="Filter by format">
      <button class="filter-btn active" type="button" data-filter="all" aria-pressed="true">All</button>
      <button class="filter-btn" type="button" data-filter="episode" aria-pressed="false">Podcasts</button>
      <button class="filter-btn" type="button" data-filter="youtube" aria-pressed="false">Videos</button>
      <button class="filter-btn" type="button" data-filter="event" aria-pressed="false">Events</button>
      <button class="filter-btn" type="button" data-filter="article" aria-pressed="false">Posts</button>
    </div>
  </div>

  <div class="archive-filter-row">
    <span class="archive-filter-label">Series / game</span>
    <div class="archive-filters" data-archive-filters data-filter-group="series" aria-label="Filter by series or game">
      <button class="filter-btn active" type="button" data-filter="all" aria-pressed="true">All games</button>
      <button class="filter-btn" type="button" data-filter="netwatch" aria-pressed="false">Netwatch</button>
      <button class="filter-btn" type="button" data-filter="raise-the-black" aria-pressed="false">Raise the Black</button>
      <button class="filter-btn" type="button" data-filter="arachne" aria-pressed="false">Arachne</button>
      <button class="filter-btn" type="button" data-filter="arachne-specials" aria-pressed="false">Specials</button>
    </div>
  </div>
  <p class="archive-status small" data-archive-status data-item-name="post" aria-live="polite"></p>

  <div class="media-grid archive-grid">
    {% for post in all %}
      {% assign card_image = post.thumbnail | default: post.episode_artwork | default: post.video_thumbnail | default: "/assets/images/arachne-no-text.png" %}
      {% assign card_series = post.series %}
      {% unless card_series %}
        {% assign normalized_title = post.title | downcase %}
        {% if normalized_title contains "netwatch" %}
          {% assign card_series = "Netwatch" %}
        {% elsif normalized_title contains "raise the black" %}
          {% assign card_series = "Raise the Black" %}
        {% else %}
          {% assign card_series = "Arachne" %}
        {% endif %}
      {% endunless %}
      <article class="media-card" data-archive-item data-filter-format="{{ post.content_type | default: 'article' }}" data-filter-series="{{ card_series | slugify }}">
        <a class="media-card-image" href="{{ site.baseurl }}{{ post.url }}">
          <img src="{{ card_image }}" alt="" loading="lazy">
          <span class="media-card-action">{% if post.content_type == "youtube" %}WATCH{% elsif post.content_type == "episode" %}LISTEN{% else %}OPEN{% endif %}</span>
        </a>
        <div class="media-card-body">
          <div class="media-card-meta">
            <span>{{ card_series | default: post.content_type | default: "Post" }}</span>
            <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %d, %Y" }}</time>
          </div>
          <h3><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
          <p>{{ post.excerpt | default: post.content | strip_html | truncate: 135 }}</p>
        </div>
      </article>
    {% endfor %}
  </div>
</section>

<script src="{{ site.baseurl }}/assets/js/archive-filter.js"></script>
