# How to Update Your Website

## Adding a New Paper

### Option A: Drop-a-PDF (automatic metadata extraction)

1. **Copy your PDF** into the appropriate folder:
   - Final/accepted papers: `static/papers/published/`
   - Working papers or under review: `static/papers/working/`

2. **Run the extraction script** (requires Python and an Anthropic API key):
   ```bash
   # Install dependencies (first time only)
   pip install pymupdf anthropic

   # Set your API key (or export it in your shell profile)
   export ANTHROPIC_API_KEY="your-key-here"

   # Run the script
   python scripts/extract_paper.py
   ```
   This reads the first few pages of any new PDF, sends the text to Claude, and generates a markdown file in `content/research/` with the title, authors, abstract, venue, and year pre-filled.

3. **Review and edit** the generated `.md` file in `content/research/`. You may want to:
   - Fix any extraction errors
   - Add links (SSRN, DOI, media coverage) to the `links:` section
   - Adjust `sort_weight:` to control ordering within its group (lower = higher on page)

4. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add new paper: Paper Title"
   git push
   ```
   The site auto-deploys within a couple of minutes.

### Option B: If you push PDFs directly to GitHub

If you push a new PDF to `static/papers/` on the `main` branch, the GitHub Action (`.github/workflows/extract-papers.yml`) will automatically:
1. Run the extraction script
2. Commit the generated `.md` file back to the repo
3. Trigger a site deploy

This requires the `ANTHROPIC_API_KEY` secret to be set in your GitHub repo settings (Settings > Secrets and variables > Actions > New repository secret).

### Option C: Write the markdown manually

Create a new file in `content/research/` (e.g., `content/research/my-paper.md`) with this template:

```yaml
---
title: "Your Paper Title"
authors: ["Sarah H. Bana", "Coauthor Name"]
venue: "Journal Name"
status: "published"       # "published" or "working"
year: 2026
abstract: |
  Your abstract text here. This can be multiple
  lines as long as they're indented.
pdf: "/papers/published/your-file.pdf"
links:
  - label: "DOI"
    url: "https://doi.org/..."
  - label: "SSRN"
    url: "https://ssrn.com/..."
sort_weight: 1            # lower number = appears first in its group
---
```

Then push to GitHub.

---

## Adding a Blog Post

Create a new file in `content/blog/` (e.g., `content/blog/my-post.md`):

```yaml
---
title: "Post Title"
date: 2026-03-04
tags: ["AI", "labor markets"]
summary: "A one-line summary shown on the blog list page."
---

Write your post content here in regular markdown.

You can use **bold**, *italics*, [links](https://example.com), images, code blocks, etc.
```

Push to GitHub and it auto-deploys.

---

## Updating Your CV

Replace the PDF at `static/cv/bana_cv.pdf` with the new version, then push:

```bash
cp ~/path/to/new-cv.pdf static/cv/bana_cv.pdf
git add static/cv/bana_cv.pdf
git commit -m "Update CV"
git push
```

---

## Updating Your Bio / Homepage

Edit `content/_index.md` and push.

---

## Updating Contact Info or Social Links

Edit `config.toml` for the social icon links (email, Google Scholar, GitHub, X, LinkedIn). Edit `content/contact.md` for the contact page text.

---

## Previewing Locally

```bash
# Start the local dev server
hugo server -D

# Open the URL it prints (usually http://localhost:1313)
# Changes auto-reload in the browser
```

---

## How Deployment Works

- Every push to `main` triggers the GitHub Action in `.github/workflows/deploy.yml`
- It builds the site with Hugo and deploys to GitHub Pages
- Changes are typically live within 2-3 minutes of pushing

---

## File Locations Quick Reference

| What                  | Where                              |
|-----------------------|------------------------------------|
| Site config           | `config.toml`                      |
| Homepage content      | `content/_index.md`                |
| Research papers       | `content/research/*.md`            |
| Blog posts            | `content/blog/*.md`                |
| CV page               | `content/cv.md`                    |
| Contact page          | `content/contact.md`               |
| CV PDF                | `static/cv/bana_cv.pdf`            |
| Published paper PDFs  | `static/papers/published/`         |
| Working paper PDFs    | `static/papers/working/`           |
| Headshot              | `static/img/headshot.jpg`          |
| CSS styles            | `assets/css/main.css`              |
| Page templates        | `layouts/`                         |
| Extraction script     | `scripts/extract_paper.py`         |
| GitHub Actions        | `.github/workflows/`               |
