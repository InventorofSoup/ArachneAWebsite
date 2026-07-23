"""Import public videos from the official Arachne YouTube channel."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    sys.exit("Install the importer first: python -m pip install --upgrade yt-dlp")


CHANNEL_URL = "https://www.youtube.com/@ArachneAGamingYoutubeChannel/videos"
CHANNEL_HOME = "https://www.youtube.com/@ArachneAGamingYoutubeChannel"
ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "_posts"


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


def safe_body(value: str) -> str:
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    value = "\n".join(line.rstrip() for line in value.splitlines()).strip()
    # Podcast/video descriptions are content, not Liquid templates.
    return value.replace("{{", "&#123;&#123;").replace("{%", "&#123;%")


def excerpt_from(value: str) -> str:
    value = re.sub(r"https?://\S+", "", value)
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) > 240:
        value = value[:237].rsplit(" ", 1)[0] + "…"
    return value


def duration_string(seconds: int | float | None) -> str:
    if not seconds:
        return ""
    seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}" if hours else f"{minutes:02d}:{seconds:02d}"


def publication_date(info: dict) -> datetime:
    upload_date = info.get("upload_date")
    if upload_date:
        return datetime.strptime(upload_date, "%Y%m%d").replace(
            hour=12,
            tzinfo=timezone.utc,
        )
    timestamp = info.get("timestamp") or info.get("release_timestamp")
    if timestamp:
        return datetime.fromtimestamp(timestamp, tz=timezone.utc)
    raise ValueError(f"Video {info.get('id')} has no publication date")


def render_post(info: dict) -> tuple[str, str]:
    video_id = str(info["id"])
    title = str(info.get("title") or video_id).strip()
    published = publication_date(info)
    description = safe_body(str(info.get("description") or ""))
    excerpt = excerpt_from(description) or f"Watch {title} from Arachne: A Gaming Channel."
    filename = f"{published.date().isoformat()}-{slugify(title)}.md"
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    thumbnail = f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"

    front_matter = [
        "---",
        "layout: post",
        f"title: {yaml_string(title)}",
        f"date: {published.strftime('%Y-%m-%d %H:%M:%S %z')}",
        "published: true",
        "content_type: youtube",
        f"excerpt: {yaml_string(excerpt)}",
        "tags: [youtube, video]",
        f"youtube_id: {yaml_string(video_id)}",
        f"video_url: {yaml_string(video_url)}",
        f"video_thumbnail: {yaml_string(thumbnail)}",
        f"duration: {yaml_string(duration_string(info.get('duration')))}",
        f"youtube_channel_url: {yaml_string(CHANNEL_HOME)}",
        "youtube_imported: true",
        "---",
        "",
    ]
    return filename, "\n".join(front_matter) + description + "\n"


def main() -> None:
    options = {
        "quiet": True,
        "skip_download": True,
        "ignoreerrors": True,
        "extract_flat": False,
    }
    with yt_dlp.YoutubeDL(options) as downloader:
        channel = downloader.extract_info(CHANNEL_URL, download=False)

    entries = [entry for entry in channel.get("entries", []) if entry]
    created = updated = unchanged = skipped = 0
    for entry in entries:
        filename, content = render_post(entry)
        target = POSTS_DIR / filename

        if target.exists():
            existing = target.read_text(encoding="utf-8")
            if "youtube_imported: true" not in existing:
                print(f"Skipped unmanaged file: {target.name}")
                skipped += 1
                continue
            if existing == content:
                unchanged += 1
                continue
            updated += 1
        else:
            created += 1

        target.write_text(content, encoding="utf-8", newline="\n")

    print(
        "YouTube import complete: "
        f"{created} created, {updated} updated, {unchanged} unchanged, {skipped} skipped."
    )


if __name__ == "__main__":
    main()
