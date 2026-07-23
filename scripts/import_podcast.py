"""Import published podcast episodes from the official Captivate RSS feed."""

from __future__ import annotations

import html
import json
import re
import unicodedata
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path


RSS_URL = "https://feeds.captivate.fm/arachne/"
ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "_posts"
ITUNES = "{http://www.itunes.com/dtds/podcast-1.0.dtd}"
LEGACY_EPISODE_ONE = "2023-04-22-episode-1-hello-arachne.md"


def text(node: ET.Element, name: str) -> str:
    return (node.findtext(name) or "").strip()


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def slugify(value: str) -> str:
    ascii_value = (
        unicodedata.normalize("NFKD", value)
        .encode("ascii", "ignore")
        .decode("ascii")
        .lower()
    )
    return re.sub(r"[^a-z0-9]+", "-", ascii_value).strip("-")[:90].rstrip("-")


def markdown_from_html(value: str) -> str:
    def replace_link(match: re.Match[str]) -> str:
        attributes, label = match.groups()
        href_match = re.search(r'href=["\']([^"\']+)["\']', attributes, re.I)
        label = re.sub(r"<[^>]+>", "", label)
        label = html.unescape(label).strip()
        return f"[{label}]({href_match.group(1)})" if href_match and label else label

    value = re.sub(r"<a\b([^>]*)>(.*?)</a>", replace_link, value, flags=re.I | re.S)
    value = re.sub(r"<br\s*/?>", "\n", value, flags=re.I)
    value = re.sub(r"</p\s*>", "\n\n", value, flags=re.I)
    value = re.sub(r"<p\b[^>]*>", "", value, flags=re.I)
    value = re.sub(r"<(strong|b)\b[^>]*>", "**", value, flags=re.I)
    value = re.sub(r"</(strong|b)\s*>", "**", value, flags=re.I)
    value = re.sub(r"<(em|i)\b[^>]*>", "*", value, flags=re.I)
    value = re.sub(r"</(em|i)\s*>", "*", value, flags=re.I)
    value = re.sub(r"<[^>]+>", "", value)
    value = html.unescape(value).replace("\r", "")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in value.splitlines()]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def plain_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def series_for(title: str) -> tuple[str, str]:
    lowered = title.lower()
    if lowered.startswith("netwatch"):
        return "Netwatch", "netwatch"
    if lowered.startswith("raise the black"):
        return "Raise the Black", "raise-the-black"
    if re.match(r"^episode\s+\d+", title, re.I):
        return "Arachne", "arachne"
    return "Arachne Specials", "special"


def render_post(item: ET.Element) -> tuple[str, str]:
    title = text(item, "title")
    published = parsedate_to_datetime(text(item, "pubDate"))
    date_value = published.strftime("%Y-%m-%d %H:%M:%S %z")
    filename = f"{published.date().isoformat()}-{slugify(title)}.md"
    description_html = text(item, "description")
    description = markdown_from_html(description_html)
    excerpt = plain_text(description_html)
    if len(excerpt) > 240:
        excerpt = excerpt[:237].rsplit(" ", 1)[0] + "…"

    enclosure = item.find("enclosure")
    audio_url = enclosure.attrib.get("url", "") if enclosure is not None else ""
    artwork_node = item.find(f"{ITUNES}image")
    artwork = artwork_node.attrib.get("href", "") if artwork_node is not None else ""
    duration = text(item, f"{ITUNES}duration")
    series, tag = series_for(title)

    front_matter = [
        "---",
        "layout: post",
        f"title: {yaml_string(title)}",
        f"date: {date_value}",
        "published: true",
        "content_type: episode",
        f"series: {yaml_string(series)}",
        f"excerpt: {yaml_string(excerpt)}",
        f"tags: [podcast, {tag}]",
        f"audio_url: {yaml_string(audio_url)}",
        f"episode_url: {yaml_string(text(item, 'link'))}",
        f"episode_artwork: {yaml_string(artwork)}",
        f"duration: {yaml_string(duration)}",
        f"rss_guid: {yaml_string(text(item, 'guid'))}",
    ]

    if filename == LEGACY_EPISODE_ONE:
        front_matter.extend(
            [
                "redirect_from:",
                '  - "/posts/Episode_1-Hello,Arachne!/"',
            ]
        )

    front_matter.extend(["---", ""])
    return filename, "\n".join(front_matter) + description + "\n"


def main() -> None:
    request = urllib.request.Request(
        RSS_URL,
        headers={"User-Agent": "ArachneWebsite/1.0 podcast importer"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        root = ET.fromstring(response.read())

    created = updated = skipped = 0
    for item in root.findall("./channel/item"):
        filename, content = render_post(item)
        target = POSTS_DIR / filename

        if target.exists():
            existing = target.read_text(encoding="utf-8")
            is_managed = "rss_guid:" in existing or filename == LEGACY_EPISODE_ONE
            if not is_managed:
                print(f"Skipped unmanaged file: {target.name}")
                skipped += 1
                continue
            if existing == content:
                skipped += 1
                continue
            updated += 1
        else:
            created += 1

        target.write_text(content, encoding="utf-8", newline="\n")

    print(f"Podcast import complete: {created} created, {updated} updated, {skipped} unchanged.")


if __name__ == "__main__":
    main()
