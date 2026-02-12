---
layout: default
title: Events
permalink: /events/
---

<header class="header">
  <h1 class="logo" style="font-size:40px; color: var(--text);">Events</h1>
  <p class="tagline">Upcoming and past events.</p>
</header>

<section class="panel section">
  {% assign ev = site.posts | where: "content_type", "event" | sort: "date" | reverse %}

  {% if ev.size == 0 %}
    <p class="small">No events posted yet.</p>
  {% endif %}

  {% for post in ev %}
    <div class="post-row">
      <div class="tag">EVENT</div>
      <h3 class="hline"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
      <p class="excerpt">{{ post.excerpt | default: post.content | strip_html | truncate: 160 }}</p>
      <div class="meta">{{ post.date | date: "%b %d, %Y" }}</div>
    </div>
    {% unless forloop.last %}<hr class="divider">{% endunless %}
  {% endfor %}
</section>
