---
title: "Anthropic's AI Exposure Index: Measurement Limitations Worth Knowing"
date: 2026-03-09
tags: ["AI", "labor markets", "measurement", "Anthropic"]
summary: "The new Anthropic radar chart is an interesting construct, but the underlying measurement has limitations worth understanding."
---

A lot of people in my feed are sharing the new [Anthropic radar chart](https://www.anthropic.com/research/labor-market-impacts) — theoretical AI coverage and observed AI coverage by occupation.

![Theoretical capability and observed exposure by occupational category](https://www-cdn.anthropic.com/images/4zrzovbb/website/c1952c81bca02a7c8cc05ef7801e67ca60831c55-4096x4096.png)

Observed AI coverage is an interesting new construct, and I'm thankful Anthropic is continuing to share usage data — but the underlying measurement has limitations worth understanding:

**Observed AI coverage:** Anthropic doesn't actually know your occupation — they infer it from the task you're performing. (OpenAI, by contrast, has merged their usage data with external information about workers' actual occupations.) This matters because AI is expanding the set of tasks workers can perform, and their measurement doesn't account for that.

I remade my website with Claude Code earlier this week. But Anthropic doesn't know I'm a professor and not a web developer — that task would be attributed to a web developer. The observed coverage measure can't capture people performing new tasks as a result of AI, something we know is happening.

**Automation vs. augmentation:** Anthropic is doubling down on this distinction in their exposure measure. Automation is when a task is directive or involves a feedback loop; augmentation is when a task involves validation, iteration, or learning. But because I don't know CSS, I'm automating web development, not augmenting it — and these carry different weights in their index. What counts as automation vs. augmentation is quite opaque to Claude, because it doesn't know the full distribution of activities I (or anyone) am performing, both on and off platform. If I edit in a Word document or iterate with Gemini, that's invisible. The distinction can also be easily muddled just by the way a user phrases a question.

**Validation:** They validate against BLS projected employment growth from 2024–2034. But the BLS's models do not explicitly incorporate AI — so they're validating an AI exposure index against a baseline that is essentially AI-blind. That's not entirely helpful.

And if anything, reading their research should spur your own set of reflections on your tasks. This is something I've advocated for before and I'll advocate for again — the only person who knows your job's exposure is you. Ask a colleague or friend how they've been using AI and set up a work block to watch them. Share with someone a task you've been stuck on, and see if you can both use AI to figure it out.

The jagged frontier continues to be real, and I have found exploration to be quite valuable.
