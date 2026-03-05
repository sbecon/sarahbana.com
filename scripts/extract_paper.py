#!/usr/bin/env python3
"""
Extract metadata from PDFs in static/papers/ and generate Hugo content files.

Scans static/papers/published/ and static/papers/working/ for PDFs that don't
have corresponding .md files in content/research/. For each new PDF, extracts
text from the first few pages, sends it to the Claude API, and generates a
markdown file with proper frontmatter.

Usage:
    python scripts/extract_paper.py
"""

import json
import os
import re
import sys

import anthropic
import fitz  # pymupdf


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:80].rstrip("-")


def get_existing_pdfs() -> dict[str, str]:
    """Map PDF filenames (without extension) already covered by .md files."""
    existing = {}
    research_dir = os.path.join("content", "research")
    if not os.path.isdir(research_dir):
        return existing

    for fname in os.listdir(research_dir):
        if not fname.endswith(".md") or fname == "_index.md":
            continue
        filepath = os.path.join(research_dir, fname)
        with open(filepath, "r") as f:
            content = f.read()
        # Extract the pdf path from frontmatter
        match = re.search(r'^pdf:\s*"([^"]+)"', content, re.MULTILINE)
        if match:
            pdf_path = match.group(1)
            pdf_basename = os.path.splitext(os.path.basename(pdf_path))[0]
            existing[pdf_basename] = fname
    return existing


def extract_text_from_pdf(pdf_path: str, max_pages: int = 3) -> str:
    """Extract text from the first few pages of a PDF."""
    doc = fitz.open(pdf_path)
    text = ""
    for i, page in enumerate(doc):
        if i >= max_pages:
            break
        text += page.get_text()
    doc.close()
    return text[:8000]  # Limit to avoid token overflows


def extract_metadata_with_claude(text: str, status: str) -> dict:
    """Send extracted text to Claude API and get structured metadata."""
    client = anthropic.Anthropic()

    prompt = f"""Analyze the following text extracted from an academic paper PDF and extract the metadata.

Return a JSON object with these fields:
- "title": the paper title (string)
- "authors": list of author names (list of strings), in the order they appear
- "abstract": the paper's abstract (string), or empty string if not found
- "year": publication year (integer), or null if not found
- "venue": journal/conference name (string), or "Working Paper" if not identifiable

The paper's status is: {status}

Text from PDF:
{text}

Return ONLY valid JSON, no other text."""

    message = client.messages.create(
        model="claude-sonnet-4-5-20250514",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )

    response_text = message.content[0].text.strip()
    # Try to extract JSON from the response
    if response_text.startswith("```"):
        response_text = re.sub(r"^```(?:json)?\n?", "", response_text)
        response_text = re.sub(r"\n?```$", "", response_text)

    return json.loads(response_text)


def generate_markdown(metadata: dict, pdf_relative_path: str, status: str) -> str:
    """Generate Hugo-compatible markdown content from metadata."""
    title = metadata.get("title", "Untitled")
    authors = metadata.get("authors", [])
    venue = metadata.get("venue", "Working Paper")
    year = metadata.get("year", "")
    abstract = metadata.get("abstract", "")

    authors_yaml = ", ".join(f'"{a}"' for a in authors)

    # Indent abstract for YAML block scalar
    abstract_lines = abstract.strip().split("\n")
    abstract_yaml = "\n  ".join(abstract_lines)

    md = f"""---
title: "{title}"
authors: [{authors_yaml}]
venue: "{venue}"
status: "{status}"
year: {year}
abstract: |
  {abstract_yaml}
pdf: "{pdf_relative_path}"
links: []
sort_weight: 99
auto_generated: true
---
"""
    return md


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(base_dir)

    existing = get_existing_pdfs()
    research_dir = os.path.join("content", "research")
    os.makedirs(research_dir, exist_ok=True)

    folders = {
        "published": os.path.join("static", "papers", "published"),
        "working": os.path.join("static", "papers", "working"),
    }

    new_count = 0

    for status, folder in folders.items():
        if not os.path.isdir(folder):
            continue

        for fname in sorted(os.listdir(folder)):
            if not fname.lower().endswith(".pdf"):
                continue

            basename = os.path.splitext(fname)[0]

            if basename in existing:
                print(f"  Skipping {fname} (already has .md)")
                continue

            pdf_path = os.path.join(folder, fname)
            pdf_relative = f"/papers/{status}/{fname}"

            print(f"  Extracting: {fname}")
            text = extract_text_from_pdf(pdf_path)

            if not text.strip():
                print(f"    Warning: No text extracted from {fname}, skipping")
                continue

            try:
                metadata = extract_metadata_with_claude(text, status)
            except Exception as e:
                print(f"    Error calling Claude API for {fname}: {e}")
                continue

            title = metadata.get("title", basename)
            slug = slugify(title)
            md_filename = f"{slug}.md"
            md_path = os.path.join(research_dir, md_filename)

            # Avoid overwriting existing files
            if os.path.exists(md_path):
                md_filename = f"{slug}-{basename[:20]}.md"
                md_path = os.path.join(research_dir, md_filename)

            md_content = generate_markdown(metadata, pdf_relative, status)

            with open(md_path, "w") as f:
                f.write(md_content)

            print(f"    Created: {md_path}")
            new_count += 1

    print(f"\nDone. Generated {new_count} new file(s).")


if __name__ == "__main__":
    main()
