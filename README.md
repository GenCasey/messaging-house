# Messaging House

![Messaging House: four value boxes across the top, specs stacked beneath. Four reasons to buy; every feature underneath the one it proves.](docs/assets/social-preview.png)

**A Claude skill that turns any product, app or service into messaging people actually respond to.**

Most product copy fails for one reason: it lists what the product does instead of saying why anyone should care. Messaging House fixes that with a method built on a decade of launches at Microsoft, NVIDIA and Alaska Airlines, and on Strategyzer's Value Proposition Design. You start with one real customer. You end with a messaging house, a value proposition, and a homepage, every line of which traces back to a job that customer is trying to get done.

It works for a consumer app, a developer API, a services firm, or a physical product. It works if you have never heard the words "value proposition" before. And it refuses to make things up: if your spec sheet has eight facts, the output has eight facts.

## What you walk away with

One file, `messaging-house.md`, containing:

- **A customer profile.** One named person, and the jobs, pains and gains behind the moment they reach for your product.
- **A value map.** How your product answers each of those, with an honest fit rating. Weak fits are findings, not failures.
- **Four why-buys.** The four reasons to buy, named as outcomes a customer would recognise, not technologies.
- **The messaging house.** A table with the four why-buys across the top and every feature you gave it stacked beneath the one it proves. This is the one document your team argues about instead of arguing about sentences.
- **A value proposition.** Four or five sentences that name your product once and end on the emotional job.
- **A four-blade homepage.** The value proposition as the intro, then one blade per why-buy, with features as proof. Or a press release, ad set, email sequence, or sales one-pager, if that is what you asked for.

Here is what the why-buys and value proposition look like for a fictional e-signature API (full example in [`examples/sealed-esignature-api`](examples/sealed-esignature-api)):

> 1. **Signing that never leaves your product**
> 2. **Signed in the sandbox before lunch**
> 3. **Holds up when someone challenges it**
> 4. **Pay per signature, nothing else**
>
> Your product handles the whole lease, the whole hire or the whole loan, and then sends the user somewhere else to sign it, or leans on a signer one engineer built and nobody wants to touch. Sealed puts signing inside your product: your pages, your brand, your data filled in, and a webhook the moment it is done. Integrate it from the language you already use and have a signed document in the sandbox in a median of 22 minutes, then pay $0.40 per completed envelope with no platform fee. Every signature comes with a tamper-evident audit trail, SOC 2 Type II and eIDAS advanced signatures behind it. Ship signing this sprint, and stop being the person who has to defend it.

Notice that "Built for developers" is not a why-buy. The skill considered it and threw it out, because the customer does not want a developer product; she wants signing shipped.

## Install

**Claude Code**

```
/plugin marketplace add GenCasey/messaging-house
/plugin install messaging-house@gencasey
```

**Any agent that reads skills** (Cursor, Codex, Claude Code and others, via the [skills CLI](https://github.com/vercel-labs/skills))

```
npx skills add GenCasey/messaging-house
```

**Claude Cowork or claude.ai**

Download `messaging-house.skill` from the [latest release](https://github.com/GenCasey/messaging-house/releases) and add it under Skills.

**By hand**

Copy `skills/messaging-house` into `~/.claude/skills/` (or your project's `.claude/skills/`).

## Use

Just describe what you sell and who buys it. You do not need to name the skill; it triggers on requests like these:

- "Our homepage is a feature soup and nobody understands why they should care."
- "We need positioning we can hand to the web and PR people."
- "Write the landing page for my app."
- "Give me messaging so the whole launch stays consistent."

If you are new to this, the skill will explain the one idea it stands on (jobs to be done), ask you for one real customer, and draft each stage for you to correct. It asks one question at a time. If you already have a spec sheet and know your customer, say so and it runs end to end with its assumptions listed at the top.

For a Word version of the house, run:

```
python skills/messaging-house/scripts/export_docx.py messaging-house.md
```

## How it works

1. **One real customer.** Not a segment. A person, what they are trying to get done, what gets in the way, what a win looks like.
2. **Value map.** Each feature against the job, pain or gain it answers, with a fit rating.
3. **Four why-buys.** Chosen from the tightest fits, tested for evidence, distinctness, and whether the customer would recognise them. You get to argue with them before anything is built on them.
4. **The house.** Every feature stacked under the why-buy it proves. Stacking runs both ways: sometimes a why-buy bends to fit the product, sometimes the specs move. A feature that fits nowhere is a message to product, not a footnote.
5. **Copy.** A section per why-buy, a value proposition written from all four, then the channel you need.

The method comes from stitching two things together: the messaging houses used to launch Surface at Microsoft (four why-buys over stacked specs) and Strategyzer's canvas, which turned out to be the missing way to derive those four reasons instead of guessing them. The [references](skills/messaging-house/references) folder has the full method, including the interview questions and a worked example.

## Why this and not a prompt

A one-line prompt gives you a plausible marketing guide with invented features in it. In testing across six briefs (a consumer app, a developer API, a services firm, a legal-tech SaaS, and two physical products), Claude without this skill invented product behaviour in every single run: a "one-tap swap" nobody built, "no minimums, no seats" for a product with no such terms, a "20-minute warm-up" for a machine that heats in 45 seconds. With the skill it invented none, and marked the gaps as "needed from engineering" instead. The skill passed 89% of a strict checklist on the software and service briefs; the unaided baseline passed 24%.

## Examples

- [`examples/sealed-esignature-api`](examples/sealed-esignature-api): a developer API. Why-buys for a CTO, a docs homepage, pricing page framing, and an outbound sequence.
- [`examples/pantry-meal-planning`](examples/pantry-meal-planning): a consumer app with a thin, first-founder brief. Shows the skill drawing three why-buys from six features and flagging what a fourth would need.

Both products are fictional.

## Credits

Method by [Casey Milone](https://caseymilone.com). Value Proposition Design and the canvas are the work of Alex Osterwalder and Yves Pigneur at [Strategyzer](https://www.strategyzer.com). Jobs to be done, and the milkshake, belong to Clayton Christensen and Bob Moesta.

MIT licensed. Issues and pull requests welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).
