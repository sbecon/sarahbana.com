---
title: "Algorithmic Monoculture in Hiring"
date: 2026-05-28
tags: ["AI", "hiring", "algorithmic monoculture", "labor markets"]
summary: "Select thoughts on our new paper, accepted at FAccT '26, which finds both racial bias and applicants who get rejected everywhere at once."
---

*Our paper, **[Algorithmic Monocultures in Hiring](https://arxiv.org/abs/2605.27371)** (with Rishi Bommasani, Kathleen Creel, Dan Jurafsky, and Percy Liang), is now public and accepted at the 2026 ACM Conference on Fairness, Accountability, and Transparency (FAccT '26). This content was written for the Stanford Digital Economy Lab's Q&A — the [full set of comments is here](https://digitaleconomy.stanford.edu/news/qa-algorithmic-monoculture/). These are some select thoughts.*

**What is "algorithmic monoculture?"**

Algorithmic monoculture, to me, is any circumstance in which similar outcomes occur because of algorithms. There are plenty of simple algorithms, like needing a college degree or three years of experience, before getting a job. But the more complex algorithms that are now appearing in the labor market produce similar outcomes through more complicated processes. These machine learning tools, built to characterize opaque elements like "fit," generate similar outcomes across firms with less interpretability.

**What would you say is the main takeaway?**

I think the most significant result of our study is how much bias we find in this algorithmic hiring system. The vendor has published aggregated audits that demonstrate that their tools do not demonstrate measurable bias. In that way, I was surprised because I thought that their algorithms would be an example of best practice. When you read that something you're buying has been audited, you tend to take that finding at face value – and that's likely part of what is going on.

**How do you explain the gap between earlier research that found no significant bias and your findings?**

Earlier research reported aggregate numbers — averaged across all the positions a vendor screens for. We disaggregated and looked at each position separately. That's the major difference.

U.S. employment law evaluates adverse impact one position at a time, because that's how employers actually make hiring decisions. Aggregating can mask the disparity. Imagine a model that over-selects one group for warehouse jobs and under-selects them for finance jobs. The averages would look balanced; the position-by-position picture would show real bias. That's roughly the pattern we found.

**What groups experience the most adverse impact?**

We see many Black and Asian applicants adversely impacted. We don't have any causal evidence here but my guess is that behaviors that are being picked up by the games are functioning as proxies for race – the kind of bias that is hard to remove without explicit adjustments to the trained models.

There's also a structural piece that we don't observe with the data we have access to. The models are trained against each firm's current employees in a given role, and those workforces likely aren't very diverse to begin with.

**What advice would you give to those hiring using current algorithms?**

Figure out what your algorithm is doing – who it is screening in/out for each position you're using it. This means you have to let, ideally, a random subset of applicants through that first stage and see how they fare. This is probably worth doing regularly because your algorithm is probably not changing at the rate that your work is.

**What advice would you give someone seeking a job?**

On the algorithmic side, our work finds that you need to apply to more jobs than ever before — and apply widely. Some employers use the same processes (sometimes literally the same vendor), so submitting more applications through identical pipelines won't generate new evaluations. That's part of why range matters. A few suggestions:

1. **Build demonstrable experience.** Internships, freelance work, project-based work, portfolios, public writing — anything that lets you show what you can do, not just what's on your resume. Concrete examples are harder for an algorithm to filter out.
2. **Lean on weak ties.** The people most likely to help you find a job aren't your closest friends — they're acquaintances who have different information than you do. In some cases, a referral can also bypass algorithmic screening altogether.
3. **Stay flexible.** Apply across roles, industries, and geographies. Be open to contract, temporary, or adjacent positions; organizations are running lean and a lot of opportunities show up in these forms.
4. **Build a routine.** A long job search is hard — emotionally as much as logistically. Track your progress, and connect with your communities. The risk in this market isn't that you can't find anything; it's that the search wears you down before it pays off.

*Read the paper on [arXiv](https://arxiv.org/abs/2605.27371). Coverage: [Stanford HAI](https://hai.stanford.edu/news/ai-hiring-tools-can-yield-racial-bias-and-systemic-rejection) and [Marketplace](https://www.marketplace.org/story/2026/05/28/ai-hiring-tools-can-still-have-racial-biases-study-finds).*
