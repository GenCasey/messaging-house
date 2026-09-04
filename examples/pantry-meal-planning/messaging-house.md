# Pantry Messaging House

Prepared 3 September 2026. Customer: Dana, 36, two kids, standing at the fridge door at 5:40 on a Tuesday with no idea what's for dinner.

## Assumptions

This ran on the fast track, with no one to interview. Correct any of these and the house changes.

1. **The hero customer is a composite.** The brief says users are mostly people in their 30s with kids who hate deciding what's for dinner. I built one person from that, called her Dana, and gave her a working partner, a seven-year-old and a four-year-old. If you have a real user who fits, swap her in; her actual words will beat mine.
2. **What she used before:** a rotation of the same six dinners held in her head, the "what do you want for dinner?" text loop with her partner, takeout on the nights the loop failed, and a meal-planning app she abandoned because it wanted her to type in every item in the pantry. Nothing in the brief contradicts this, but it is inferred.
3. **The spec list is the five sentences in the brief, plus pricing.** Photograph groceries; scan receipts; suggest a week of dinners from what you have; build a shopping list for the gaps; remind you what's about to go off; free with ads or $6/month without. That is the marketing version. The house needs the engineering version, and its thinness shows in the table below: every column is one row short. This is the main finding, and it is fixable in an hour with whoever built the app.
4. **Three why-buys, not four.** Four columns cannot hold on six features without the same feature sitting under two headings, which breaks the house. Three is fine for a narrow product, and this is a narrow product. A fourth column may appear once the engineering spec list arrives (see open questions).
5. **The app is live and downloadable**, since it has users. The calls to action assume that. If the landing page is for a waitlist, swap the CTA (noted in the channel copy).
6. **No brand voice was given.** Copy uses the defaults: short sentences, second person, concrete nouns, no stacked adjectives.
7. **Nothing is claimed that the brief does not say.** In particular, the copy does not say how far ahead the expiry reminder fires, how expiry is known, how accurate the photo recognition is, whether the plan can be shared with a partner, whether dinners can be filtered for kids or diets, or how long any dinner takes to cook. Each of those is marked "needed" where it would strengthen a column.

## Customer profile

Dana works, her partner works, and dinner is hers by default because nobody else will decide. The moment she reaches for the product is the fridge door at 5:40, kids circling, with a vague memory of chicken bought on Saturday.

### Jobs (ranked; practical, social, emotional)

1. Answer "what's for dinner" without deliberating, on a weeknight, at the worst hour. (practical, emotional)
2. Stop dreading 5 o'clock; get the decision off her mind before she is tired. (emotional)
3. Use the food she already bought before it goes off. (practical)
4. Get something on the table the kids will actually eat, in the time she has. (practical)
5. Do one grocery run that covers the whole week, with no mid-week dash for one ingredient. (practical)
6. Stop being the household's default menu planner; share the deciding. (social)
7. Not throw money in the bin, and not feel guilty about the bin. (emotional)
8. Keep the grocery bill from creeping. (practical)
9. Know what is in the fridge while standing in the store. (practical)
10. Feel like a parent who has the house under control. (social, emotional)
11. Eat something other than the same six dinners. (practical)

### Pains (ranked)

1. The decision itself, seven times a week, and nobody else will make it.
2. Meal-planning apps and recipe sites that want her to type in everything she owns; she quits within a week.
3. Finding the spinach gone slimy and the chicken past its date, and the guilt and money that go with it.
4. Buying things she already has; the second jar of tahini, the third bag of rice.
5. Recipes that assume a stocked pantry and a free evening.
6. The mid-week store dash for the one thing the recipe needed.
7. The "I don't know, what do you want?" text loop with her partner.
8. Takeout as the fallback, and the bill at the end of the month.
9. Kids rejecting the new thing she tried.
10. Being the one who always has to know what is in the house.

### Gains (ranked)

1. Dinner is decided before she is tired, ideally for the whole week at once.
2. Setup takes minutes, not an evening of typing.
3. Less in the bin; the feeling of having used what she bought.
4. One shop a week that actually covers the week.
5. Fewer "what's for dinner" texts.
6. The grocery bill stops creeping.
7. Feeling on top of the house.
8. The kids eat it.
9. Her partner can see the plan and pick up the slack.
10. Dinner on the table in a time she can name.

## Value map

| Profile item | How Pantry answers it | Fit |
|---|---|---|
| Job 1: answer "what's for dinner" without deliberating | Suggests dinners for the week | strong |
| Job 2: stop dreading 5 o'clock | A week of dinners decided at once takes the decision off the weeknight | strong |
| Job 3: use what she bought before it goes off | Dinners are suggested from what she already has; reminds her what's about to go off | strong |
| Job 4: something the kids will eat, in the time she has | Nothing in the intake about kid-friendliness, dietary filters or cook time | none (needed) |
| Job 5: one grocery run that covers the week | Builds a shopping list for the gaps between the plan and the fridge | strong |
| Job 6: share the deciding with her partner | Nothing in the intake about household sharing | none (needed) |
| Job 7: not throw money in the bin | Expiry reminders; dinners from what she has | strong |
| Job 8: keep the bill from creeping | Implied by the above, but no number to prove it | weak |
| Job 9: know what's in the fridge from the store | Photo and receipt capture mean Pantry knows what's at home; the list for the gaps is the practical answer | strong |
| Job 10: feel like the house is under control | Sum of the above; no single feature | weak |
| Job 11: eat something other than six dinners | Suggestions come from Pantry, not her head; variety is implied, not specified | weak |
| Pain 1: the decision, seven times a week | A week of dinners suggested at once | strong |
| Pain 2: apps that make her type everything | Photograph groceries; scan receipts | strong |
| Pain 3: slimy spinach, guilt, money | Reminds her what's about to go off | strong |
| Pain 4: buying what she already has | Shopping list built for the gaps only | strong |
| Pain 5: recipes that assume a stocked pantry | Suggestions start from what's actually in the fridge | strong |
| Pain 6: mid-week dash for one thing | Shopping list for the gaps, built from the week's plan | strong |
| Pain 7: the text loop with her partner | Only indirectly (the decision is made); no sharing feature in the intake | weak |
| Pain 8: takeout as fallback | A decided plan reduces the fallback; nothing specific | weak |
| Pain 9: kids rejecting new food | Nothing in the intake | none (needed) |
| Pain 10: being the one who has to know | Pantry knows what's in the fridge because she showed it | strong |
| Gain 1: decided before she's tired | Week of dinners at once | strong |
| Gain 2: setup in minutes | Photo and receipt capture | strong |
| Gain 3: less in the bin | Expiry reminders; dinners from what's there | strong |
| Gain 4: one shop that covers the week | Shopping list for the gaps | strong |
| Gain 5: fewer texts | Indirect | weak |
| Gain 6: bill stops creeping | No number | weak |
| Gain 7: on top of the house | Sum of the above | weak |
| Gain 8: kids eat it | Nothing in the intake | none (needed) |
| Gain 9: partner sees the plan | Nothing in the intake | none (needed) |
| Gain 10: dinner in a time she can name | Nothing in the intake | none (needed) |

Findings for product, not marketing: the four "none" lines (kids, sharing, cook time, dietary) are the top of Dana's list after the decision itself. If any of them already exists in the app and was left out of the brief, it belongs in the house. If none exist, they are the roadmap.

## Why-buys

1. **Dinner, decided**: answers job 1, job 2, pain 1 and gain 1, which are the top of every list. The week's dinners are suggested at once, and the list for the gaps means the plan holds until Sunday.
2. **Nothing goes off**: answers job 3, job 7, pain 3 and gain 3. Dinners are drawn from what is already in the fridge, and Pantry warns before something turns.
3. **Nothing to type**: answers pain 2 and gain 2, and it is the claim a competitor meal planner cannot make. Photograph the groceries or scan the receipt; the fridge is in the app without a keyboard.

Candidates dropped or merged:

- **One trip, no dashes** (job 5, pains 4 and 6): a real outcome, but only one feature proves it, the shopping list for the gaps. One feature is a feature, not a why-buy. It became the second row of "Dinner, decided," where it does the work of making the plan hold for a week.
- **Cheaper weeks** (job 8, gain 6): every parent would recognise it, but the intake has no number, and "Nothing goes off" already carries the money argument. Promote it only when there is a figure to stand behind.
- **Free to start**: pricing, not a reason to buy. Parked; it gets its own strip on the page.

## Messaging house

| Dinner, decided | Nothing goes off | Nothing to type |
|---|---|---|
| Pantry suggests dinners for the whole week at once, so the question gets answered once on the weekend instead of seven times at 5:40. | Every dinner Pantry suggests starts from what is already in your fridge, so the chicken you bought on Saturday becomes Tuesday's dinner instead of next week's bin. | Photograph your groceries and Pantry knows what is in the fridge; there is no list to type. |
| Pantry builds the shopping list for whatever the week's dinners need that you do not already have, so the plan survives to Thursday without a dash to the store. | Pantry reminds you what is about to go off before it does, so you find out while there is still time to cook it. | Scan the receipt and the whole shop goes in at once. |
| **Needed from engineering:** how many suggestions per night, whether a night can be swapped, and whether dinners can be filtered for kids, diets or cook time. Any one of these is the third row. | **Needed from engineering:** how many days ahead the reminder fires, how Pantry knows the date (receipt date, typical shelf life, something else), and where the reminder arrives. A number here is the third row. | **Needed from engineering:** which stores' receipts scan, how many items a photo can read, and any accuracy figure. A number here would be the strongest row on the page. |

Parking lot:

- **Free with ads.** Pricing fact; goes in the pricing strip, not a column.
- **$6/month, no ads.** Same. Note that the intake says nothing else differs between tiers, so the page must not imply the paid tier has more features.

Every column is one row short. The cause is the spec list, not the why-buys: the brief gave six feature sentences, and the columns held all six without a single feature needing to sit under two headings. That is a good sign for the why-buys. Get the engineering version of the feature list and the third rows will fill.

## Why-buy copy

### Dinner, decided

You decide dinner once, on the weekend, for the whole week, and then you stop deciding. No more standing at the fridge at 5:40 with two hungry children and a blank mind. No more "I don't know, what do you want?" The question that has been yours by default every night of the week gets answered in one sitting, and the answer holds.

Pantry suggests dinners for the week at once, so the decision happens when you have the energy for it, not when you are out of it. It then builds the shopping list for whatever those dinners need that you do not already have, so the plan does not collapse on Wednesday for want of one onion. Plan, shop, and the week is handled.

### Nothing goes off

The chicken you bought on Saturday gets cooked, not found. So does the spinach, the half-tub of yoghurt, and the herbs you swore you would use. You stop throwing food and money into the bin at the end of the week, and you stop feeling bad about it, because the bin stays empty.

Pantry builds every dinner suggestion from what is already in your fridge, so the food you paid for is the food you eat. When something is close to turning, Pantry reminds you before it does, while there is still time to make it dinner. Nothing is discovered too late, because Pantry knew it was there.

### Nothing to type

You never type in what you own. Every meal-planning app you have abandoned wanted an evening of data entry before it would help you, and you had no evening to give. Pantry asks for a photo. Your fridge is in the app without a keyboard.

Photograph the groceries as they come in and Pantry knows what is in the fridge. Scan the receipt and the whole shop goes in at once, including the things you did not feel like photographing. The list, the plan and the reminders all start from what Pantry saw, which is what you actually have.

## Value proposition

Somebody in your house has to decide what is for dinner, seven nights a week, and it is always you, at the worst hour of the day. Pantry looks at what is already in your fridge, from a photo of your groceries or a scan of the receipt, and suggests the week's dinners from it, with a shopping list for only the gaps. The chicken gets cooked before it turns, because you are reminded in time, and you stop paying twice for things you already had. You decide once, on Sunday, with a cup of tea. Then the fridge door is just a fridge door.

## Channel copy

### Landing page

See `landing-page.md` for the full page. Structure: value proposition as the intro, three blades in column order, pricing strip, closing call to action. Every line on it points to a cell above.

## Open questions

- **The engineering feature list.** Every setting, limit, integration and number: suggestions per night, swap-a-night, filters, reminder lead time, how expiry is known, receipt formats, photo accuracy, household sharing. This is the one thing that would change the house most. An hour with whoever built the app.
- **Is there a fourth why-buy hiding in the app?** If dinners can be filtered for kids, diets or cook time, "Dinners the kids will eat" or "On the table in thirty minutes" is a column, and it answers job 4, which is the highest job the current house does not touch. If the plan can be shared with a partner, "Not just your job" is a column, and it answers job 6.
- **A real Dana.** Any user who has said "I hate deciding what's for dinner" in her own words. One quote from her would replace the value proposition's first sentence and be better.
- **Is the page for a download or a waitlist?** The copy assumes download. The CTA swap is marked in the page.
- **Do the tiers differ on anything but ads?** The page currently says they do not. If the paid tier has more, the pricing strip changes and possibly the house.
- **A number for waste or money.** "Nothing goes off" would be twice as strong with one real figure, even from a small user sample: meals cooked from the reminder, items saved, dollars per week. Do not invent one.

## What to do with this

Share the house with the team as the one document to argue about. Argue about the three why-buys first, then the third rows, then the copy, in that order. Derive every channel from it, and change the house first when a claim needs to change. When the engineering list arrives, re-stack, and if a fourth column holds with three rows, add a fourth blade to the page.
