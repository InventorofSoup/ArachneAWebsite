---
layout: default
title: Listen
permalink: /listen/
---

{% assign eps = site.posts | where: "content_type", "episode" | sort: "date" | reverse %}
{% assign featured = eps.first %}

<header class="page-hero">
  <p class="signal-kicker"><span aria-hidden="true"></span> The Arachne podcast</p>
  <h1 class="page-title">Listen</h1>
  <p class="page-copy">Tune into the latest release or filter the complete archive by program.</p>
</header>

{% if featured %}
  {% assign featured_image = featured.thumbnail | default: featured.episode_artwork | default: "/assets/images/arachne-no-text.png" %}
  <section class="featured-transmission">
    <div class="featured-transmission-art">
      <img src="{{ featured_image }}" alt="{{ featured.title | escape }}">
      <span class="scanlines" aria-hidden="true"></span>
    </div>
    <div class="featured-transmission-copy">
      <p class="signal-label">Latest episode</p>
      <div class="tag">{{ featured.series | default: "Arachne" | upcase }}</div>
      <h2><a href="{{ site.baseurl }}{{ featured.url }}">{{ featured.title }}</a></h2>
      <p>{{ featured.excerpt | default: featured.content | strip_html | truncate: 240 }}</p>
      <div class="transmission-meta">
        <span>{{ featured.date | date: "%b %d, %Y" }}</span>
        {% if featured.duration %}<span>{{ featured.duration }}</span>{% endif %}
      </div>
      {% if featured.audio_url %}
        <audio class="broadcast-player" controls preload="metadata">
          <source src="{{ featured.audio_url }}" type="audio/mpeg">
          Your browser does not support the audio player.
        </audio>
      {% endif %}
      <div class="hero-actions">
        <a class="btn btn-primary" href="{{ site.baseurl }}{{ featured.url }}">Episode notes</a>
        <a class="btn btn-ghost" href="https://open.spotify.com/show/1X2k6XBqV2LJF9Jee0cdE2" target="_blank" rel="noopener noreferrer">Open Spotify ↗</a>
      </div>
    </div>
  </section>
{% endif %}

<section class="broadcast-section archive-section">
  <div class="section-head">
    <div>
      <p class="signal-label">Explore the show</p>
      <h2 class="section-title">Episode archive</h2>
    </div>
    <span class="archive-count">{{ eps.size }} episodes</span>
  </div>

  <div class="archive-filters" data-archive-filters data-filter-group="series" aria-label="Filter podcast archive by series or game">
    <button class="filter-btn active" type="button" data-filter="all" aria-pressed="true">All</button>
    <button class="filter-btn" type="button" data-filter="arachne" aria-pressed="false">Arachne</button>
    <button class="filter-btn" type="button" data-filter="netwatch" aria-pressed="false">Netwatch</button>
    <button class="filter-btn" type="button" data-filter="raise-the-black" aria-pressed="false">Raise the Black</button>
    <button class="filter-btn" type="button" data-filter="arachne-specials" aria-pressed="false">Specials</button>
  </div>
  <p class="archive-status small" data-archive-status data-item-name="episode" aria-live="polite"></p>

  <div class="media-grid archive-grid">
    {% for post in eps %}
      {% assign card_image = post.thumbnail | default: post.episode_artwork | default: "/assets/images/arachne-no-text.png" %}
      {% assign card_series = post.series | default: "Arachne" %}
      <article class="media-card" data-archive-item data-filter-series="{{ card_series | slugify }}">
        <a class="media-card-image" href="{{ site.baseurl }}{{ post.url }}">
          <img src="{{ card_image }}" alt="" loading="lazy">
          <span class="media-card-action">LISTEN</span>
        </a>
        <div class="media-card-body">
          <div class="media-card-meta">
            <span>{{ card_series }}</span>
            {% if post.duration %}<span>{{ post.duration }}</span>{% endif %}
          </div>
          <h3><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
          <p>{{ post.excerpt | default: post.content | strip_html | truncate: 135 }}</p>
          <time class="card-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %d, %Y" }}</time>
        </div>
      </article>
    {% endfor %}
  </div>
</section>

<script src="{{ site.baseurl }}/assets/js/archive-filter.js"></script>
