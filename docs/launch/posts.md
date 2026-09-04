# Launch posts

Ready to paste. Plain text, paragraph breaks, no markdown. None of them mentions availability, hiring, or anything other than the work.

## LinkedIn

I spent a decade launching products at Microsoft, NVIDIA and Alaska Airlines, and then years running the same messaging process for startups as a consultant. Today I put the whole method into a free Claude skill.

It is called Messaging House. You describe what you sell and one real customer. It walks you from that customer's jobs, pains and gains to four reasons to buy, then stacks every feature you gave it under the reason it proves. That table is the messaging house. From it you get a value proposition and a homepage, and every sentence traces back to a job your customer is trying to get done.

The part I care most about: it refuses to make things up. In testing, Claude on its own invented product features in every single run. A one-tap swap nobody built. A warm-up time that was wrong. With the skill, zero. It marks the gaps as "needed from engineering" instead.

It works for a consumer app, a developer API, a services firm, or a physical product, and it works if you have never heard of a value proposition canvas. It will teach you the one idea it stands on and ask you one question at a time.

Two lines to install in Claude Code, or one command for Cursor and Codex. MIT licensed. Link in the comments.

Credit where it is due: the canvas is Osterwalder and Pigneur's at Strategyzer, and jobs to be done is Christensen and Moesta's. What I added is the bridge from the canvas to the copy.

## X / Threads (thread)

1/ I turned ten years of product-launch messaging into a free Claude skill. Describe what you sell and one real customer; it gives you four reasons to buy, a messaging house, a value proposition, and a homepage. github.com/GenCasey/messaging-house

2/ The method: Strategyzer's Value Proposition Canvas to find the tightest fit between what a customer is trying to get done and what your product does, then a messaging house that stacks every feature under the reason it proves. Surface launches at Microsoft ran on exactly this table.

3/ What makes it different from a prompt: it does not invent features. Unaided, Claude made something up in every test run. With the skill, none. Gaps get labelled "needed from engineering."

4/ It is built for people coming in cold. It explains jobs to be done in plain words, asks one question at a time, and shows its work before building on it. If you already know your customer, it has a fast track.

5/ Install: /plugin marketplace add GenCasey/messaging-house then /plugin install messaging-house@gencasey. Or npx skills add GenCasey/messaging-house. MIT.

## Show HN

Title: Show HN: A Claude skill that builds a messaging house from one real customer

I spent years at Microsoft and NVIDIA launching products with a messaging house: four "why buy" reasons across the top, engineering's spec list stacked beneath. Later, after getting certified in Strategyzer's Value Proposition Design, I realised the canvas's fit map was the missing way to derive those four reasons instead of guessing them. This skill is that method, written down so an agent can run it with someone who has never done it.

You give it what you sell and one real customer. It maps that person's jobs, pains and gains, builds a value map with honest fit ratings, proposes four why-buys and asks you to argue with them, then stacks every feature under the one it proves. From the table it writes a value proposition and a four-blade homepage (or a press release, ad set, or email sequence).

The design constraint I cared about most was hallucinated features. In six test briefs, Claude without the skill invented product behaviour every time. With the skill it invented none; it labels gaps "needed from engineering." The evals and grading checklist are in the repo.

MIT. Works with Claude Code as a plugin, or with Cursor/Codex via the skills CLI. Two fictional worked examples included (a developer API and a consumer app). Happy to hear where it breaks on your product.

## Reddit (r/ClaudeAI, r/marketing, r/startups; adjust the first line per sub)

I open-sourced the messaging method I used on product launches at Microsoft and NVIDIA as a Claude skill.

Short version: you describe your product and one real customer. It walks you from that customer's jobs, pains and gains to four reasons to buy, stacks every feature under the reason it proves (that table is the messaging house), and then writes a value proposition and a homepage from it.

It is meant for people who have never done positioning before. It explains jobs to be done in plain words and asks one question at a time. If you know your customer already, there is a fast track.

The thing I tested hardest: it does not invent features. Plain Claude did in every run; with the skill it labels gaps instead. Evals are in the repo.

Free, MIT, two-line install for Claude Code, one command for Cursor and Codex. Would love to see the four why-buys you get for your product.
