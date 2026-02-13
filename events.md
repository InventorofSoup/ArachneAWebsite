---
layout: default
title: Events
permalink: /events/
---

<header class="header">
  <h1 class="logo" style="font-size:40px; color: var(--text);">Events</h1>
  <p class="tagline">Upcoming events and past highlights.</p>
</header>

{% assign today = "now" | date: "%s" %}

<section class="panel section">
  <h2 class="feed-title">Upcoming</h2>

  {% assign upcoming = site.posts | where: "content_type", "event" | sort: "event_date" %}
  {% assign has_upcoming = false %}

  {% for post in upcoming %}
    {% assign ev = post.event_date | date: "%s" %}
    {% if ev >= today %}
      {% assign has_upcoming = true %}
      <div class="post-row">
        <div class="tag">EVENT</div>
        <h3 class="hline"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
        <p class="excerpt">{{ post.excerpt | default: post.content | strip_html | truncate: 160 }}</p>
        <div class="meta">
          {{ post.event_date | date: "%b %d, %Y" }}
          {% if post.location %} · {{ post.location }}{% endif %}
        </div>
      </div>
      {% unless forloop.last %}<hr class="divider">{% endunless %}
    {% endif %}
  {% endfor %}

  {% unless has_upcoming %}
    <p class="small">No upcoming events yet.</p>
  {% endunless %}
</section>

<section class="panel section" style="margin-top:16px;">
  <h2 class="feed-title">Past</h2>

  {% assign past = site.posts | where: "content_type", "event" | sort: "event_date" | reverse %}
  {% assign has_past = false %}

  {% for post in past %}
    {% assign ev = post.event_date | date: "%s" %}
    {% if ev < today %}
      {% assign has_past = true %}
      <div class="post-row">
        <div class="tag">EVENT</div>
        <h3 class="hline"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
        <p class="excerpt">{{ post.excerpt | default: post.content | strip_html | truncate: 160 }}</p>
        <div class="meta">
          {{ post.event_date | date: "%b %d, %Y" }}
          {% if post.location %} · {{ post.location }}{% endif %}
        </div>
      </div>
      {% unless forloop.last %}<hr class="divider">{% endunless %}
    {% endif %}
  {% endfor %}

  {% unless has_past %}
    <p class="small">No past events yet.</p>
  {% endunless %}
</section>
