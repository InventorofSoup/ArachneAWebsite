---
layout: default
title: Events
permalink: /events/
---

<header class="header page-hero">
  <p class="hero-kicker">Calendar and coverage</p>
  <h1 class="page-title">Events</h1>
  <p class="page-copy">
    Upcoming appearances, event coverage, and past highlights from Arachne. Check what is coming up next, then browse older event posts below.
  </p>
</header>

{% assign today = "now" | date: "%s" %}
{% assign upcoming = site.posts | where: "content_type", "event" | sort: "event_date" %}
{% assign past = site.posts | where: "content_type", "event" | sort: "event_date" | reverse %}

<section class="panel section">
  <div class="section-head">
    <h2 class="feed-title">Upcoming Events</h2>
  </div>

  {% assign has_upcoming = false %}
  {% for post in upcoming %}
    {% assign ev = post.event_date | date: "%s" %}
    {% if ev >= today %}
      {% assign has_upcoming = true %}
      <article class="post-row">
        <div class="tag">EVENT</div>
        <h3 class="hline"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
        <p class="excerpt">{{ post.excerpt | default: post.content | strip_html | truncate: 180 }}</p>
        <div class="meta">
          {{ post.event_date | date: "%b %d, %Y" }}
          {% if post.location %} · {{ post.location }}{% endif %}
        </div>
      </article>
      {% unless forloop.last %}<hr class="divider">{% endunless %}
    {% endif %}
  {% endfor %}

  {% unless has_upcoming %}
    <p class="small">No upcoming events yet.</p>
  {% endunless %}
</section>

<section class="panel section" style="margin-top:16px;">
  <div class="section-head">
    <h2 class="feed-title">Past Events</h2>
  </div>

  {% assign has_past = false %}
  {% for post in past %}
    {% assign ev = post.event_date | date: "%s" %}
    {% if ev < today %}
      {% assign has_past = true %}
      <article class="post-row">
        <div class="tag">EVENT</div>
        <h3 class="hline"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
        <p class="excerpt">{{ post.excerpt | default: post.content | strip_html | truncate: 180 }}</p>
        <div class="meta">
          {{ post.event_date | date: "%b %d, %Y" }}
          {% if post.location %} · {{ post.location }}{% endif %}
        </div>
      </article>
      {% unless forloop.last %}<hr class="divider">{% endunless %}
    {% endif %}
  {% endfor %}

  {% unless has_past %}
    <p class="small">No past events yet.</p>
  {% endunless %}
</section>
