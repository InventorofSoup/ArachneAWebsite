---
layout: default
title: Support Arachne
permalink: /support/
ads: false
---

<header class="header page-hero">
  <p class="hero-kicker">Support the network</p>
  <h1 class="page-title">Help keep the Website Running</h1>
  <p class="page-copy">
    Arachne's website collects the network's podcasts, videos, events, and community updates in one independent archive.
  </p>
</header>

<section class="panel section">
  <div class="section-head">
    <h2 class="feed-title">Ways to help</h2>
  </div>
  {% if site.support_url and site.support_url != "" %}
    <p>Contributions help cover hosting, web services, equipment, and the time required to maintain the archive.</p>
    <p><a class="btn btn-primary" href="{{ site.support_url }}" target="_blank" rel="noopener noreferrer">Help keep the Website Running</a></p>
    <p class="small">Support is voluntary and does not purchase goods or services.</p>
  {% else %}
    <p>A secure contribution page is being prepared. Until it is ready, watching, listening, subscribing, and sharing Arachne's work are meaningful ways to help.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{{ '/youtube/' | relative_url }}">Watch the latest videos</a>
      <a class="btn btn-ghost" href="{{ '/listen/' | relative_url }}">Listen to the podcast</a>
    </div>
  {% endif %}
</section>
