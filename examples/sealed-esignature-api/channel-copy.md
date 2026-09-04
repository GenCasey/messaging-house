# Sealed Channel Copy

Derived from `messaging-house.md`. Every line below traces to a cell in the house; the why-buy names are identical on every channel and should stay identical. Where a channel needs a fact the house does not hold, it is marked "needed" rather than invented.

## 1. Developer docs homepage (four-blade)

The docs homepage is the homepage for this product, because the buyer evaluates by reading docs and trying the sandbox. Structure: headline, subhead, value proposition intro, four blades in column order, a strip for the facts that belong beside the blades rather than in them, then the specification list. Calls to action match the customer's next job, which is to make a call, not to learn more.

### Headline

Signing that never leaves your product.

### Subhead

Sealed is an e-signature API for software companies. Embed signing in your own pages, get a webhook when it is done, pay $0.40 per completed envelope.

### Intro

Your product handles the whole lease, the whole hire or the whole loan, and then sends the user somewhere else to sign it, or leans on a signer one engineer built and nobody wants to touch. Sealed puts signing inside your product: your pages, your brand, your data filled in, and a webhook the moment it is done. Integrate it from the language you already use and have a signed document in the sandbox in a median of 22 minutes, then pay $0.40 per completed envelope with no platform fee. Every signature comes with a tamper-evident audit trail, SOC 2 Type II and eIDAS advanced signatures behind it. Ship signing this sprint, and stop being the person who has to defend it.

Primary call to action: Get a sandbox key
Secondary call to action: Read the quickstart

### Blade 1: Signing that never leaves your product

The lease is drafted in your product, reviewed in your product, and stored in your product. Sealed lets it be signed there too. Your user never leaves for another company's page, never sees another company's logo at the most important step, and never has to come back and tell your app what happened. Your customers see one product doing the whole job, which is what they thought they were buying.

- Embedded signing UI that renders inside your own pages
- White-labelled, so the signing step carries your brand
- Templates with merge fields filled from your application's data
- Webhooks for every event: sent, viewed, signed, declined

Call to action: See the embed in the quickstart

### Blade 2: Signed in the sandbox before lunch

Signing has probably slipped a sprint or two already. Sealed is built so that the evaluation and the first working integration are the same afternoon. You read the docs, make a call from the language you already use, and have a signed test document before you have decided whether to book a demo.

- REST API covering the whole signing flow
- SDKs for Node, Python and Ruby
- Median time from first call to first signed document in the sandbox: 22 minutes

Call to action: Start the quickstart in Node, Python or Ruby

Note for the docs team: publish how the 22-minute median is measured directly beneath the number. An engineer will ask, and an unexplained median reads as marketing.

### Blade 3: Holds up when someone challenges it

A signature only matters on the day someone disputes it. A tenant says they never agreed to that clause; a borrower says the document changed after they signed. With a home-built signer, that day is yours to defend. With Sealed, every envelope arrives with the evidence already attached, and the compliance questions that follow have short answers.

- Audit trail with tamper-evident hashes on every envelope
- SOC 2 Type II
- eIDAS advanced signatures

Call to action: Read the audit trail reference

### Blade 4: Pay per signature, nothing else

Vertical SaaS sells by the door, the employee or the loan, and a cost that arrives as seats or a platform fee never maps to that. Sealed charges for the thing your customer values, a completed signature, and nothing else. You can put the number into your own pricing model and know it will still be true next quarter.

- $0.40 per completed envelope
- No platform fee
- Sandbox with unlimited test envelopes

Call to action: See pricing

### Supporting strip (below the blades)

Three short tiles, each a fact from the house restated for scanning: "SDKs: Node, Python, Ruby", "SOC 2 Type II and eIDAS advanced signatures", "$0.40 per completed envelope, no platform fee". A fourth tile is needed for a fact the house does not hold yet: uptime or status page. Leave it out until there is a number.

### Specifications (bottom of page, numeric)

- API: REST
- SDKs: Node, Python, Ruby
- Signing UI: embedded, white-labellable
- Templates: merge fields
- Webhooks: every envelope event
- Audit trail: tamper-evident hashes
- Compliance: SOC 2 Type II; eIDAS advanced signatures
- Sandbox: unlimited test envelopes
- Pricing: $0.40 per completed envelope; no platform fee
- Median time to first signed document in sandbox: 22 minutes
- Rate limits, retention, uptime: needed

## 2. Pricing page framing

The pricing page is why-buy four expanded, with the other three why-buys present as one line each so the page does not read as a price without a reason. It has one price and no plan grid, because the house holds one price. Do not add tiers, seat counts or a "contact sales" column; there is no fact behind any of them.

### Headline

Pay per signature, nothing else.

### Subhead

$0.40 per completed envelope. No platform fee. Unlimited test envelopes in the sandbox.

### Framing paragraph

Vertical SaaS sells by the door, the employee or the loan, and a cost that arrives as seats or a platform fee never maps to that. Sealed charges for the thing your customer values, a completed signature, and nothing else. Put the number into your own pricing model and know it will still be true next quarter.

### The price, stated three ways

One completed envelope: $0.40.
One thousand completed envelopes: $400.
Zero completed envelopes: $0. There is no platform fee, so a quiet month costs nothing.

(The arithmetic is the supplied price multiplied out, not a volume tier. If volume pricing exists, it is a new fact for the house first.)

### What is included at that price

Every completed envelope carries the same product, whatever the volume:

- Embedded, white-labelled signing UI (Signing that never leaves your product)
- Templates with merge fields and webhooks for every event (Signing that never leaves your product)
- REST API and SDKs for Node, Python and Ruby (Signed in the sandbox before lunch)
- Audit trail with tamper-evident hashes, SOC 2 Type II, eIDAS advanced signatures (Holds up when someone challenges it)

### Sandbox

The sandbox includes unlimited test envelopes and is free. Evaluate, test and build without a bill. Median time from first call to first signed document in the sandbox is 22 minutes.

### Questions a buyer will ask on this page

Answer each with a fact from the house, and mark the rest as needed before the page ships.

What counts as a completed envelope? Needed: the team's definition. The house reads "completed" literally, so an envelope that is never completed is not billed; confirm before publishing.

Is there a minimum, a contract or a setup fee? The house says no platform fee. Minimums and contracts are not in the intake; state them or state their absence.

Does the price change with volume? Not in the intake. Say nothing until there is a fact.

Is the sandbox limited in time or envelopes? Unlimited test envelopes. Time limits are not in the intake.

Call to action: Get a sandbox key

## 3. Outbound emails

A four-touch sequence to a CTO or founding engineer at a vertical SaaS company. Touch one has two versions, one for each starting position in the brief; touches two to four are the same for both. Each touch carries one why-buy, in column order after the opener. Plain text, no images, one call to action per email, and the ask is always a sandbox key rather than a meeting because that is the customer's next job.

Personalisation slots are in square brackets. Fill them from research, not from guesses about the prospect's stack.

### Touch 1, version A: prospect links out to DocuSign today

Subject: The signing step in [Product]

[First name],

I noticed [Product] sends [tenants / new hires / borrowers] to DocuSign to sign. Everything before that step is yours; that one step is somebody else's brand.

Sealed is an e-signature API built so the signing happens inside your product. The signing UI embeds in your pages and can be white-labelled, templates fill from your own data with merge fields, and a webhook fires for every event so your records update the moment a document is signed.

It is $0.40 per completed envelope with no platform fee, and the sandbox has unlimited test envelopes. Median time from first call to first signed document in the sandbox is 22 minutes.

Would a sandbox key be useful? I can send one without a call.

[Sender]

### Touch 1, version B: prospect built an in-house signer

Subject: The signer in [Product]

[First name],

Most vertical SaaS teams I talk to have a home-built signing flow that one engineer understands and nobody wants to change. It worked when it was built; now it is the thing everyone routes around.

Sealed is an e-signature API that replaces the pieces you are maintaining: an embedded, white-labelled signing UI, templates with merge fields, webhooks for every event, and an audit trail with tamper-evident hashes on every envelope. It is SOC 2 Type II and supports eIDAS advanced signatures, which turns the signing section of a security questionnaire into a yes.

It is $0.40 per completed envelope, no platform fee, and the sandbox has unlimited test envelopes.

Would a sandbox key be useful? No call needed.

[Sender]

### Touch 2: Signing that never leaves your product

Subject: Signing that never leaves your product

[First name],

One thing from my last note, in case it was buried: the whole point of Sealed is that your user signs where they were already working.

The signing UI embeds in your own pages and is white-labelled, so the signing step carries your brand. Templates with merge fields pull [rent, dates and names / salary, start date and title / loan amount and terms] from data you already hold, so the user checks the document instead of retyping it. Webhooks fire for every event, so your own records know the moment a document is sent, viewed, signed or declined.

Happy to send a sandbox key if you want to see the embed in your own page.

[Sender]

### Touch 3: Signed in the sandbox before lunch

Subject: 22 minutes

[First name],

The number I keep coming back to: in the Sealed sandbox, the median time from first call to first signed document is 22 minutes.

That is with the REST API and an SDK in Node, Python or Ruby, so the first call looks like the rest of your codebase. Test envelopes are unlimited, so the evaluation is an afternoon rather than a project.

If signing has slipped a sprint at [Product], a sandbox key is the fastest way to find out whether it needs to slip again.

[Sender]

### Touch 4: Holds up when someone challenges it

Subject: When a [tenant / employee / borrower] disputes a signature

[First name],

Last note from me. A signature only matters on the day someone challenges it, and with a home-built or linked-out flow, that day lands on you.

Every Sealed envelope carries an audit trail with tamper-evident hashes, so you can show what was signed, by whom, and that nothing changed afterwards. Sealed is SOC 2 Type II and supports eIDAS advanced signatures, so the compliance section of a security review gets a report rather than a paragraph.

If it is not the right time, no problem. If it is, reply and I will send a sandbox key.

[Sender]

### Sequence notes

Timing is not in the house and is the team's call; a common pattern is day 0, 3, 7, 12. Do not merge two why-buys into one email; each touch is a test of which reason the market answers, and the replies tell you the order of the homepage blades.

If a prospect is US-only, drop the eIDAS line from touches 1B and 4 and let the audit trail and SOC 2 carry the claim; the house has no US legal-framework fact yet.

Pay per signature has no touch of its own because the price appears in the opener; if replies show cost is the reason that lands, promote it to touch 2 and move the others down.
