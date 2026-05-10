---
tags: [reference, writing, tools]
created: 2026-01-31T10:00:00
modified: 2026-02-08T09:00:00
---

# Writing Tips

Notes on academic writing — accumulated from paper feedback, reading group discussions, and Professor Chen's comments on drafts. Distilled here so I don't repeat the same mistakes.

## Paper Structure

**Introduction**: Problem → why it matters → what others have tried → what we do → what we found. The reader should know your main result by the end of the introduction, not at the end of the paper.

**Related Work**: Position, don't just describe. Every cited paper should relate to yours in a specific way — it solves a related problem differently, or solves a component of your problem, or is the baseline you beat.

**Method**: Be precise. Every symbol needs a definition. Every design choice needs a justification, even if brief. A skeptical reviewer should be able to re-implement your method from the method section alone.

**Experiments**: Ablations should be motivated — explain *why* each ablation tests a specific hypothesis, not just what was removed.

**Conclusion**: Don't just summarize. Interpret — what do the results mean? What are the limitations? What's the most important direction to pursue next?

## Writing Style

**Active voice**: "We compute attention scores" not "Attention scores are computed." Active voice is clearer and more direct. Most passive-voice sentences in papers are passive for no good reason.

**Precision over brevity**: Vague language in papers is worse than wordiness. "Our method is better" is meaningless. "Our method achieves 3.2% higher F1 on the test set (p < 0.05, paired bootstrap)" is what reviewers want.

**One idea per sentence**: Long sentences with multiple clauses are hard to parse. If a sentence contains "and" or "which" more than once, break it up.

**Transitions**: Every paragraph should begin with a sentence that connects to the previous one. Every section should begin with a sentence that signals what's coming.

## Revision Process

Professor Chen's approach: write a complete draft first, then revise. Never write and edit simultaneously — it kills momentum.

Revision passes (in order):
1. Structure: does the argument flow? Is anything missing or out of order?
2. Paragraphs: does each paragraph have a clear point? Does it earn its place?
3. Sentences: are they clear, precise, and active?
4. Words: any jargon that could be plainer? Any weasel words ("seems", "perhaps")?
5. Formatting: figures referenced before they appear? Tables properly captioned?

## LaTeX Workflow

See [[LaTeX_Formatting]] for the technical side. Write in LaTeX from the start — converting a Word draft to LaTeX late is painful.

Compile frequently. Don't wait until the end to discover that a figure reference is broken or a bibliography entry is malformed.

## Common Mistakes I Make

- Forgetting to define notation before using it
- Burying the main contribution in the middle of the introduction
- Not checking if conclusions are actually supported by the experiments shown
- Using "we" and "our method" inconsistently
