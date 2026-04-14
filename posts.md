---
layout: default
title: Recent Posts
permalink: /posts/
---

<header class="header page-hero">
  <p class="hero-kicker">Full archive</p>
  <h1 class="page-title">Recent Posts</h1>
  <p class="page-copy">
    Everything new in one place. Browse the latest updates across podcast episodes, videos, events, and other Arachne posts.
  </p>
</header>

{% assign all = site.posts | sort: "date" | reverse %}

<section class="panel section">
  <div class="section-head">
    <h2 class="feed-title">All Updates</h2>
    {% if all.size > 0 %}
      <span class="small">{{ all.size }} post{% if all.size != 1 %}s{% endif %}</span>
    {% endif %}
  </div>

  {% if all.size == 0 %}
    <p class="small">No posts yet.</p>
  {% else %}
    {% for post in all %}
      <article class="post-row">
        <div class="tag">
          {{ post.content_type | default: "post" | upcase }}
        </div>

        <h3 class="hline">
          <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
        </h3>

        <p class="excerpt">
          {{ post.excerpt | default: post.content | strip_html | truncate: 180 }}
        </p>

        <div class="meta">
          {{ post.date | date: "%b %d, %Y" }}
          {% if post.content_type == "event" and post.event_date %}
            · Event: {{ post.event_date | date: "%b %d, %Y" }}
          {% endif %}
        </div>
      </article>
      {% unless forloop.last %}<hr class="divider">{% endunless %}
    {% endfor %}
  {% endif %}
</section>
