# Sealed Messaging House

Prepared 3 September 2026. Customer: Dana, CTO of a 30-person property-management SaaS, who today sends tenants and owners out to DocuSign to sign leases and is fielding a security questionnaire that asks how those signatures are kept.

## Assumptions

Run on the fast track with no interview, so the following were decided rather than confirmed. Correct any of them and the rest of the document should be re-checked.

The hero customer is invented from the brief. "Dana" stands in for the CTO or founding engineer at a vertical SaaS company; property management was chosen because leases are the highest-volume, most-contested document of the three verticals named. Swap in a real customer's name and situation before the house is shared, and check the jobs list against what that person actually said.

The two starting positions in the brief (linking out to DocuSign, or maintaining a fragile in-house signer) are treated as one customer with one set of jobs, because the jobs are the same; only the pains differ. Both pain sets are in the profile, and the outbound sequence has a different opening email for each.

The four why-buys are candidates that would normally go through a second interview. The order chosen puts "Signing that never leaves your product" first because it is the reason the category exists; if outbound replies say cost or compliance is what lands, reorder the blades, not the house.

"Per completed envelope" is read literally: an envelope that is never completed is not billed. If billing works differently, the pricing column and pricing page must change.

No brand voice guide was supplied. The default voice is used: short sentences, second person, concrete nouns. Copy reads to an engineer, so proof comes before adjectives.

DocuSign is named in the customer profile and outbound copy because the brief names it as what the customer uses today. Nothing is claimed about DocuSign's pricing, features or contracts; the only comparison made is that the user leaves your product to sign.

## Customer profile

### Jobs (ranked; practical, social, emotional)

1. Get a lease signed by tenant and landlord from inside our app, so the workflow that starts in our product finishes there (practical).
2. Ship signing in the current sprint without pulling engineers off the roadmap (practical).
3. Know, in our own system, the moment a document is sent, viewed, signed or declined, so the lease record updates itself (practical).
4. Answer the customer's security questionnaire on signatures with a yes rather than a paragraph (social).
5. Prefill every lease from the data we already hold so the user never retypes a rent amount or a move-in date (practical).
6. Look like a complete product to the customer, not a product that hands off to someone else's brand at the most important step (social).
7. Price signing into our own plans without a cost line we cannot predict (practical).
8. Be certain a signature will stand up if a tenant or landlord disputes it later (emotional).
9. Stop being the person on the hook for a home-built signer nobody wants to maintain (emotional).
10. Evaluate an e-signature vendor without a sales call, by reading the docs and trying it (practical).

### Pains (ranked)

1. Linking out breaks the product: the user leaves for another brand's page at the moment that matters most, and the customer notices.
2. The in-house signer is fragile: one engineer understands it, and every change to the lease flow risks breaking it.
3. No reliable signal when a document is signed, so lease status is updated by polling, by email, or by hand.
4. Security questionnaires ask for SOC 2 and a defensible audit trail, and neither "we use a link-out" nor "we built it ourselves" answers cleanly.
5. Fear that a home-built signature has no legal standing when it is challenged.
6. Per-seat or platform pricing does not map to a product that sells by units, doors or employees, so signing costs cannot be passed through cleanly.
7. Weeks of integration and procurement before anything is signed, which means signing keeps slipping to next quarter.
8. Vendors that gate the sandbox or ration test documents, so the evaluation itself needs a budget.
9. Templates that cannot be filled from application data, so users retype what the product already knows.
10. Being unable to test the whole flow end to end before committing.

### Gains (ranked)

1. Signing that happens in our UI, under our brand, in one continuous flow.
2. A signed document in the sandbox on day one, and signing in production this sprint.
3. Every signing event lands in our system as it happens, with no polling.
4. A clean answer to the compliance section of any customer's security review.
5. A signature that carries an evidence trail we could hand to a lawyer.
6. A cost per signed document that we can price into our own plans.
7. One SDK call in the language we already use, rather than a hand-rolled HTTP client.
8. Templates filled from our data so the user only signs.
9. Unlimited testing at no cost, so the evaluation is an afternoon rather than a project.
10. One less system that is ours to maintain.

## Value map

| Profile item | How Sealed answers it | Fit |
|---|---|---|
| Job 1: sign from inside our app | Embedded signing UI, white-labelled | strong |
| Job 2: ship this sprint | REST API; SDKs for Node, Python and Ruby; sandbox; 22-minute median to first signed document | strong |
| Job 3: know the moment it is signed | Webhooks for every event | strong |
| Job 4: answer the questionnaire with a yes | SOC 2 Type II; eIDAS advanced signatures; tamper-evident audit trail | strong |
| Job 5: prefill from our data | Templates with merge fields | strong |
| Job 6: look complete, not handed off | White-labelled embedded UI | strong |
| Job 7: predictable pricing | $0.40 per completed envelope, no platform fee | strong |
| Job 8: certain it holds up | Audit trail with tamper-evident hashes; eIDAS advanced signatures | strong |
| Job 9: stop owning the signer | Whole product; no single feature | weak (implied by the product, not proven by a spec) |
| Job 10: evaluate without a sales call | Sandbox with unlimited test envelopes; docs homepage | strong |
| Pain 1: link-out breaks the product | Embedded, white-labelled signing UI | strong |
| Pain 2: fragile in-house signer | SDKs, templates, webhooks replace the home-built pieces | strong |
| Pain 3: no signal on signing | Webhooks for every event | strong |
| Pain 4: questionnaire has no clean answer | SOC 2 Type II; eIDAS advanced signatures | strong |
| Pain 5: signature will not stand up | Tamper-evident audit trail; eIDAS advanced signatures | strong |
| Pain 6: pricing does not map to our model | $0.40 per completed envelope, no platform fee | strong |
| Pain 7: weeks before anything is signed | 22-minute median to first signed document in sandbox | strong |
| Pain 8: rationed testing | Unlimited test envelopes in sandbox | strong |
| Pain 9: templates cannot be filled from data | Templates with merge fields | strong |
| Pain 10: cannot test end to end | Sandbox with unlimited test envelopes | strong |
| Gain 1: signing in our UI, our brand | Embedded, white-labelled UI | strong |
| Gain 2: signed in sandbox day one, production this sprint | 22-minute median; SDKs | strong |
| Gain 3: events land as they happen | Webhooks for every event | strong |
| Gain 4: clean compliance answer | SOC 2 Type II; eIDAS | strong |
| Gain 5: evidence trail for a lawyer | Audit trail with tamper-evident hashes | strong |
| Gain 6: cost we can price into plans | $0.40 per completed envelope, no platform fee | strong |
| Gain 7: one SDK call in our language | SDKs for Node, Python and Ruby | strong |
| Gain 8: templates filled from our data | Merge fields | strong |
| Gain 9: unlimited free testing | Sandbox with unlimited test envelopes | strong |
| Gain 10: one less system to maintain | Whole product | weak (a consequence, not a spec) |

Findings from the map. Every spec supplied has at least one strong fit, which is unusual and means the product is well matched to this customer. Two gaps that are not marketing's to fix: nothing in the intake speaks to what a signer sees on a phone, or to where signed documents are stored and for how long; both come up in property-management and lending reviews, and neither may be claimed until the facts arrive. Nothing in the intake addresses US-specific legal frameworks (ESIGN, UETA); eIDAS is a European standard, so US-facing copy proves "holds up" with the audit trail and SOC 2 rather than with eIDAS.

## Why-buys

1. **Signing that never leaves your product**: answers the top job and the top pain for both starting positions; proven by the embedded UI, white-labelling, merge-field templates and webhooks.
2. **Signed in the sandbox before lunch**: answers "ship this sprint" and the fear that signing keeps slipping; proven by the REST API, three SDKs and the 22-minute median.
3. **Holds up when someone challenges it**: answers the questionnaire pain and the emotional job of being certain; proven by the tamper-evident audit trail, SOC 2 Type II and eIDAS advanced signatures.
4. **Pay per signature, nothing else**: answers the pricing pain that vertical SaaS feels more than most; proven by the per-envelope price, the absence of a platform fee and the free, unlimited sandbox.

Candidates dropped. "Built for developers" was a candidate and failed the customer test: Dana does not want a developer product, she wants signing shipped, and every proof point for it belonged under why-buy two. "Compliant out of the box" was folded into why-buy three because the customer recognises the fear (a challenged signature) more readily than the category (compliance). "Replace your in-house signer" was considered and rejected as a why-buy because it describes the customer's situation rather than an outcome; it survives as the opening of one outbound email.

On the fourth column: it holds exactly three rows, and the sandbox row was placed there rather than under why-buy two because unlimited free testing is a cost fact before it is a speed fact. If the team would rather the sandbox sit under speed, why-buy four drops to two rows and should become a pricing strip below the blades instead of a blade. That is a legitimate choice; the house as written keeps it a why-buy because the pricing page is one of the three channels asked for.

## Messaging house

| Signing that never leaves your product | Signed in the sandbox before lunch | Holds up when someone challenges it | Pay per signature, nothing else |
|---|---|---|---|
| The signing UI embeds in your own pages, so the user signs where they were already working. | A REST API covers the whole signing flow, so anything you can call over HTTP can send, track and collect a signature. | Every envelope carries an audit trail with tamper-evident hashes, so you can show what was signed, by whom, and that nothing changed afterwards. | Each completed envelope costs $0.40, so signing is a unit cost you can price into your own plans. |
| The embedded UI can be white-labelled, so the customer sees your brand at the signing step, not ours. | Official SDKs for Node, Python and Ruby wrap the API, so your first call is in the language you already ship in. | Sealed is SOC 2 Type II, so the security questionnaire's signing section gets a yes and a report, not a paragraph. | There is no platform fee, so a slow month costs nothing and a busy month costs exactly what it signed. |
| Templates with merge fields take data from your application, so the user checks a lease instead of retyping one. | In the sandbox, the median time from first call to first signed document is 22 minutes. | Signatures meet the eIDAS advanced signature standard, so a signature collected through your product has a recognised legal basis in the EU. | The sandbox includes unlimited test envelopes, so evaluating and testing costs nothing and never runs out. |
| Webhooks fire for every event, so your lease record updates the moment a document is sent, viewed, signed or declined. | | | |

Parking lot: none. All eleven facts from the intake sit in a column.

Column check. Column one has four rows, columns two, three and four have three each. No feature could sit under two columns without stretching it: webhooks were tested against column two (they speed integration) and stayed in column one because the customer's job for them is "know the moment it is signed", not "integrate faster". The sandbox is the one row with a genuine claim to two columns; see the note under why-buys.

## Why-buy copy

### Signing that never leaves your product

The lease is drafted in your product, reviewed in your product, and stored in your product. Sealed lets it be signed there too. Your user never leaves for another company's page, never sees another company's logo at the most important step, and never has to come back and tell your app what happened. Your customers see one product doing the whole job, which is what they thought they were buying.

The signing UI embeds in your own pages and can be white-labelled, so the signing step carries your brand. Templates with merge fields pull rent, dates and names from data you already hold, so the user checks the document instead of retyping it. Webhooks fire for every event, so the moment a document is sent, viewed, signed or declined, your own records know without polling or a copied email.

### Signed in the sandbox before lunch

Signing has probably slipped a sprint or two already. Sealed is built so that the evaluation and the first working integration are the same afternoon. You read the docs, make a call from the language you already use, and have a signed test document before you have decided whether to book a demo.

The REST API covers the whole signing flow, and official SDKs for Node, Python and Ruby wrap it so the first call looks like the rest of your codebase. In the sandbox, the median time from first call to first signed document is 22 minutes.

### Holds up when someone challenges it

A signature only matters on the day someone disputes it. A tenant says they never agreed to that clause; a borrower says the document changed after they signed. With a home-built signer, that day is yours to defend. With Sealed, every envelope arrives with the evidence already attached, and the compliance questions that follow have short answers.

Every envelope carries an audit trail with tamper-evident hashes, so you can show what was signed, by whom, and that nothing was altered afterwards. Sealed is SOC 2 Type II, which gives the security questionnaire a report rather than a paragraph. Signatures meet the eIDAS advanced signature standard, so a signature collected through your product has a recognised legal basis in the EU.

### Pay per signature, nothing else

Vertical SaaS sells by the door, the employee or the loan, and a cost that arrives as seats or a platform fee never maps to that. Sealed charges for the thing your customer values, a completed signature, and nothing else. You can put the number into your own pricing model and know it will still be true next quarter.

Each completed envelope is $0.40. There is no platform fee, so a quiet month costs nothing and a busy month costs exactly what it signed. The sandbox includes unlimited test envelopes, so evaluating and testing never touch the bill.

## Value proposition

Your product handles the whole lease, the whole hire or the whole loan, and then sends the user somewhere else to sign it, or leans on a signer one engineer built and nobody wants to touch. Sealed puts signing inside your product: your pages, your brand, your data filled in, and a webhook the moment it is done. Integrate it from the language you already use and have a signed document in the sandbox in a median of 22 minutes, then pay $0.40 per completed envelope with no platform fee. Every signature comes with a tamper-evident audit trail, SOC 2 Type II and eIDAS advanced signatures behind it. Ship signing this sprint, and stop being the person who has to defend it.

## Channel copy

The three channels requested (developer docs homepage, pricing page framing, outbound emails) are in `channel-copy.md` beside this file. Each line there points to a cell in the house above. The four why-buy names are identical across all three channels and should stay that way.

## Open questions

- Who is the real customer? Replace Dana with a named CTO or founding engineer and check jobs 1 to 4 against what they actually said.
- Is an envelope billed only when completed, or when sent? The pricing column and the "abandoned envelopes cost nothing" line depend on the literal reading.
- What is the legal position outside the EU? eIDAS covers Europe; US buyers will ask about ESIGN and UETA. Until there is a fact, US-facing copy proves "holds up" with the audit trail and SOC 2 only.
- What does a signer see on a phone? Property and lending signers sign on phones; nothing in the intake speaks to it, so nothing is claimed.
- Where are signed documents stored, for how long, and who can retrieve them? Expect the question in every security review.
- How is the 22-minute median measured (from first API call, from sandbox signup, over what sample)? The number is used as supplied; the definition should be published beside it on the docs homepage.
- Is there a rate limit, uptime commitment or support tier a buyer would expect on the pricing page? None is in the intake, so the pricing page carries none.
- Is "envelope" the term the team wants customers to learn, or is "document" preferred? The house uses "envelope" because the pricing fact does.

## What to do with this

Share the house with the team as the one document to argue about. Derive every channel from it, and change the house first when a claim needs to change. For a Word version, run `python scripts/export_docx.py messaging-house.md` from the skill directory once the markdown is final.
