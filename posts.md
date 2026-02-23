---
layout: default
title: Recent Posts
permalink: /posts/
---

<header class="header">
  <h1 class="logo" style="font-size:40px; color: var(--text);">Recent Posts</h1>
  <p class="tagline">Everything new, in one place. Newest to oldest.</p>
</header>

<section class="panel section">
  {% assign all = site.posts | sort: "date" | reverse %}

  {% if all.size == 0 %}
    <p class="small">No posts yet.</p>
  {% endif %}

  {% for post in all %}
    <div class="post-row">
      <div class="tag">
        {{ post.content_type | default: "post" | upcase }}
      </div>

      <h3 class="hline"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>

      <p class="excerpt">
        {{ post.excerpt | default: post.content | strip_html | truncate: 170 }}
      </p>

      <div class="meta">
        {{ post.date | date: "%b %d, %Y" }}
        {% if post.content_type == "event" and post.event_date %}
          · Event: {{ post.event_date | date: "%b %d, %Y" }}
        {% endif %}
      </div>
    </div>
    {% unless forloop.last %}<hr class="divider">{% endunless %}
  {% endfor %}
</section>
