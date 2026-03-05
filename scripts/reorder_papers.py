#!/usr/bin/env python3
"""
View and edit sort weights for all research papers.

Usage:
    python scripts/reorder_papers.py          # Show current order
    python scripts/reorder_papers.py --edit   # Interactive reordering
"""

import os
import re
import sys


RESEARCH_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "content",
    "research",
)


def parse_frontmatter(filepath):
    """Extract frontmatter fields from a markdown file."""
    with open(filepath, "r") as f:
        content = f.read()
    info = {"filepath": filepath}
    for key in ("title", "status", "venue", "sort_weight", "year"):
        match = re.search(rf'^{key}:\s*"?([^"\n]+)"?', content, re.MULTILINE)
        if match:
            val = match.group(1).strip()
            if key in ("sort_weight", "year"):
                try:
                    val = int(val)
                except ValueError:
                    pass
            info[key] = val
    return info


def set_sort_weight(filepath, new_weight):
    """Update the sort_weight in a markdown file."""
    with open(filepath, "r") as f:
        content = f.read()
    content = re.sub(
        r"^sort_weight:\s*\d+",
        f"sort_weight: {new_weight}",
        content,
        count=1,
        flags=re.MULTILINE,
    )
    with open(filepath, "w") as f:
        f.write(content)


def load_papers():
    """Load all research papers grouped by status."""
    papers = []
    for fname in sorted(os.listdir(RESEARCH_DIR)):
        if not fname.endswith(".md") or fname == "_index.md":
            continue
        info = parse_frontmatter(os.path.join(RESEARCH_DIR, fname))
        info["filename"] = fname
        papers.append(info)
    return papers


def show_papers(papers):
    """Display papers grouped by status with sort weights."""
    for status in ("published", "working"):
        group = [p for p in papers if p.get("status") == status]
        group.sort(key=lambda p: p.get("sort_weight", 99))
        label = "PUBLICATIONS" if status == "published" else "WORKING PAPERS"
        print(f"\n{'='*60}")
        print(f"  {label}")
        print(f"{'='*60}")
        for i, p in enumerate(group, 1):
            w = p.get("sort_weight", "?")
            title = p.get("title", "Untitled")
            year = p.get("year", "")
            venue = p.get("venue", "")
            print(f"  [{w}]  {title}")
            print(f"        {venue}, {year}  ({p['filename']})")
        print()


def interactive_edit(papers):
    """Interactive mode: reorder papers within each group."""
    for status in ("published", "working"):
        group = [p for p in papers if p.get("status") == status]
        group.sort(key=lambda p: p.get("sort_weight", 99))
        label = "PUBLICATIONS" if status == "published" else "WORKING PAPERS"

        print(f"\n{'='*60}")
        print(f"  {label} — current order:")
        print(f"{'='*60}")
        for i, p in enumerate(group, 1):
            title = p.get("title", "Untitled")[:70]
            print(f"  {i}. {title}")

        print()
        print("  Enter new order as comma-separated numbers (e.g., 3,1,2,4,5)")
        print("  Or press Enter to keep current order.")
        response = input("  New order: ").strip()

        if not response:
            print("  (kept current order)")
            continue

        try:
            new_order = [int(x.strip()) for x in response.split(",")]
            if sorted(new_order) != list(range(1, len(group) + 1)):
                print("  Error: must use each number exactly once.")
                continue
        except ValueError:
            print("  Error: invalid input.")
            continue

        for new_weight, idx in enumerate(new_order, 1):
            paper = group[idx - 1]
            set_sort_weight(paper["filepath"], new_weight)
            print(f"  Set weight {new_weight}: {paper.get('title', '')[:60]}")

        print("  Done!")

    print("\nAll changes saved. Rebuild the site to see the new order.")


def main():
    papers = load_papers()

    if "--edit" in sys.argv:
        show_papers(papers)
        interactive_edit(papers)
    else:
        show_papers(papers)
        print("Run with --edit to reorder interactively.")


if __name__ == "__main__":
    main()
