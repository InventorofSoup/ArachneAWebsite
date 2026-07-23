# Arachne

The source for the Arachne gaming podcast website, built with Jekyll and hosted on Netlify.

## Run locally

1. Install Ruby 3.2 and Bundler.
2. Run `bundle install`.
3. Run `bundle exec jekyll serve`.
4. Open `http://localhost:4000/`.

Run `bundle exec jekyll build --strict_front_matter` before submitting a change. GitHub Actions runs the same build for every push and pull request.

## Publish content

- Put public posts in `_posts` using the filename format `YYYY-MM-DD-short-title.md`.
- Start from an example in `templates`.
- Keep unfinished posts out of the public site with `published: false`.
- Do not use characters that Windows forbids in filenames, including `:`, `*`, `?`, `"`, `<`, `>`, `|`, or `\`.
- Replace all example URLs and IDs before setting `published: true`.

The `content_type` field controls where an entry appears:

- `episode` appears on Listen.
- `youtube` appears on YouTube.
- `event` appears on Events.
- `article` appears in the general post archive.

## Content manager

The public site is deployed by Netlify. Decap CMS at `/admin/` provides invited editors with forms for podcast episodes, YouTube videos, events, and general posts.

Authentication uses Netlify Identity and Git Gateway connected to this repository.

To activate editor login:

1. Create a free Netlify project connected to this GitHub repository.
2. Enable Netlify Identity and set registration to **Invite only**.
3. Enable Git Gateway for the repository.
4. Configure Identity invitation and recovery links to return users to the public `/admin/` page.
5. Invite each editor by email from the Netlify Identity dashboard.

Editors can then sign in at `https://arachneawebsite.netlify.app/admin/`. Their published changes are written to the repository and trigger a new Netlify deployment.

Git Gateway is deprecated by Netlify. It remains suitable for this small invite-only
site for now, but the editing workflow should be reevaluated if Netlify announces
an end-of-service date.

## Import podcast episodes

Run the following command to create or update episode pages from the official Captivate RSS feed:

```text
python scripts/import_podcast.py
```

The importer only overwrites pages marked with `rss_guid`; hand-written posts are left untouched.

To import or refresh videos from the official YouTube channel:

```text
python -m pip install --upgrade yt-dlp
python scripts/import_youtube.py
```

The video importer only overwrites pages marked with `youtube_imported: true`.
