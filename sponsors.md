---
layout: default
title: Sponsors
permalink: /sponsors/
extra_css: /assets/css/sponsors.css
robots: noindex,follow
sitemap: false
---

<header class="header page-hero">
  <p class="hero-kicker">Friends of the network</p>
  <h1 class="page-title">Sponsors and affiliates</h1>
  <p class="page-copy">
    These partners help support Arachne's podcasts, videos, events, and community projects.
    Active partnerships and codes may change over time.
  </p>
</header>

{% assign sorted_sponsors = site.sponsors | sort: "sort_order" %}
{% assign active_count = 0 %}
{% for sponsor in sorted_sponsors %}
  {% if sponsor.active %}
    {% assign active_count = active_count | plus: 1 %}
  {% endif %}
{% endfor %}

<section class="broadcast-section">
  <div class="section-head">
    <div>
      <p class="signal-label">Current partners</p>
      <h2 class="section-title">Supporting the broadcast</h2>
    </div>
  </div>

  {% if active_count > 0 %}
    <div class="sponsor-grid">
      {% for sponsor in sorted_sponsors %}
        {% if sponsor.active %}
          <article class="sponsor-card">
            {% if sponsor.logo %}
              <div class="sponsor-logo">
                <img src="{{ sponsor.logo }}" alt="{{ sponsor.name | escape }} logo" loading="lazy">
              </div>
            {% endif %}
            <div class="sponsor-card-body">
              <div class="sponsor-meta">
                <span>{{ sponsor.level | default: "Partner" }}</span>
                <span>Active</span>
              </div>
              <h3>{{ sponsor.name }}</h3>
              {% if sponsor.summary %}<p>{{ sponsor.summary }}</p>{% endif %}

              {% if sponsor.affiliate_code %}
                <div class="affiliate-code">
                  <span>{{ sponsor.code_label | default: "Affiliate code" }}</span>
                  <strong>{{ sponsor.affiliate_code }}</strong>
                </div>
              {% endif %}

              {% assign sponsor_link = sponsor.affiliate_url | default: sponsor.website_url %}
              {% if sponsor_link %}
                <a class="btn btn-ghost"
                  href="{{ sponsor_link }}"
                  target="_blank"
                  rel="sponsored noopener noreferrer">Visit {{ sponsor.name }} ↗</a>
              {% endif %}

              {% if sponsor.affiliate_url or sponsor.affiliate_code %}
                <p class="affiliate-disclosure">
                  {{ sponsor.disclosure | default: "Arachne may receive a commission or other support when you use this link or code, at no additional cost to you." }}
                </p>
              {% endif %}
            </div>
          </article>
        {% endif %}
      {% endfor %}
    </div>
  {% else %}
    <div class="panel sponsor-empty">
      <p class="signal-label">No active listings</p>
      <h3>Current sponsor details are being confirmed.</h3>
      <p>Confirmed partners and affiliate codes will appear here when available.</p>
    </div>
  {% endif %}
</section>

<section class="signal-cta sponsor-contact">
  <div>
    <p class="signal-label">Work with Arachne</p>
    <h2>Interested in sponsoring the network?</h2>
    <p>Contact the crew to discuss a transparent partnership that fits the audience.</p>
  </div>
  <a class="btn btn-ghost" href="{{ site.baseurl }}/contact/">Contact Arachne</a>
</section>
