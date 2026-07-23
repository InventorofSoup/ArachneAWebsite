---
layout: default
title: YouTube
permalink: /youtube/
---

{% assign vids = site.posts | where: "content_type", "youtube" | sort: "date" | reverse %}
{% assign featured = vids.first %}

<header class="page-hero">
  <p class="signal-kicker"><span aria-hidden="true"></span> Arachne on YouTube</p>
  <h1 class="page-title">Watch</h1>
  <p class="page-copy">Battle reports, model previews, campaigns, and tabletop transmissions from the Arachne channel.</p>
</header>

{% if featured %}
  <section class="video-feature">
    <div class="yt-embed">
      <iframe
        src="https://www.youtube.com/embed/{{ featured.youtube_id }}?rel=0&amp;modestbranding=1"
        title="{{ featured.title | escape }}"
        loading="lazy"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
      </iframe>
    </div>
    <div class="video-feature-copy">
      <p class="signal-label">Latest video</p>
      <h2><a href="{{ site.baseurl }}{{ featured.url }}">{{ featured.title }}</a></h2>
      <p>{{ featured.excerpt | default: featured.content | strip_html | truncate: 210 }}</p>
      <div class="transmission-meta">
        <span>{{ featured.date | date: "%b %d, %Y" }}</span>
        {% if featured.duration %}<span>{{ featured.duration }}</span>{% endif %}
      </div>
      <div class="hero-actions">
        <a class="btn btn-primary" href="{{ site.baseurl }}{{ featured.url }}">Video notes</a>
        <a class="btn btn-ghost" href="https://www.youtube.com/@ArachneAGamingYoutubeChannel" target="_blank" rel="noopener noreferrer">Open channel ↗</a>
      </div>
    </div>
  </section>
{% endif %}

<section class="broadcast-section">
  <div class="section-head">
    <div>
      <p class="signal-label">Video archive</p>
      <h2 class="section-title">Recent uploads</h2>
    </div>
    <span class="archive-count">{{ vids.size }} videos</span>
  </div>

  <div class="media-grid">
    {% for post in vids offset:1 %}
      {% assign card_image = post.thumbnail | default: post.video_thumbnail | default: "/assets/images/arachne-no-text.png" %}
      <article class="media-card" data-type="youtube">
        <a class="media-card-image media-card-video" href="{{ site.baseurl }}{{ post.url }}">
          <img src="{{ card_image }}" alt="" loading="lazy">
          <span class="media-card-action">WATCH</span>
        </a>
        <div class="media-card-body">
          <div class="media-card-meta">
            <span>YouTube</span>
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
