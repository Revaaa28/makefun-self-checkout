# Candidates — The Self-Checkout Is Judging You
Slug: u-motasimfuad-the-self-checkout-is-judging-you-b71130d6 · Pot $2 · 312 submissions in field at build time · Blind rounds
Deliverable: one line, 1–200 chars, voice of a smug self-checkout machine, to a shopper buying twelve yoghurts and nothing else.
Judge brief (in order): (1) funny single-line remark from a judgmental self-checkout; (2) real laugh on one read, twist/sting, no context; (3) machine voice, smug and petty about basket + bagging; (4) tight, no padding; (5) fresh, not a joke everyone has heard.
Known winning pattern (from the $2 joke win): machine-sensor weirdness + operational numbers + a scene that escalates + a twist at the end.
Selection: MANUAL ranking only — no Gemini judge, no NVIDIA judge, no judge-API/proxy tournament (Rev's standing rule 2026-11-24).

## Field recon (312 entries, titles read live)
Crowded lanes to AVOID: "life choices / dignity in the bagging area" (5+ entries), "unexpected item: your dignity" (3+), "twelve yoghurts, zero spoons" (10+), "cry for help" (4+), "scanned your entire personality" (sagadaon + copy), "zero meals" (4+), "no spoon, no plan, no shame" (several).
Strongest visible rivals:
- R1 sagadaon: "Twelve yoghurts and nothing else. Congratulations — I've scanned your entire personality and it's 40% off." (machine verb + discount twist)
- R2 asepramdan272720: "Twelve yoghurts. Your gut biome just sent me a cease and desist." (legal escalation, fresh)
- R3 zheonzhe: "You put the kale on top for show and buried the cookies. Noted." (petty surveillance, very tight)
- R4 kenidn24: "You scanned the spinach before the gummy bears for plausible deniability. I've notified your arteries." (machine notices order + escalation)
- R5 rujakrojok: "You bought three kinds of chocolate and a pregnancy test. I am not judging. I am a machine that remembers everything." (escalating basket + creepy memory twist)
- R6 sundalamoonron-ux: "Twelve yoghurts. That's not a shop, that's a hostage situation with live cultures." (fresh metaphor)
- R7 selina-bibi: "Please place your twelve yoghurts in the bagging area. Carefully — they're the only friends you've brought home all week." (bagging-area + sting)

## Candidates (char counts verified by script)
1. "Please wait. I am verifying that twelve yogurts counts as a meal. It does not. It counts as a personality trait." (112)
2. "I have scanned 4,000 shoppers today. Yours is the first basket the scale asked me about." (88)
3. "The scale expected 4.2 kilos of groceries. It got 4.2 kilos of denial." (70)
4. "Twelve yogurts and nothing else. I have alerted the manager, your mother, and the dairy aisle. None of them are surprised." (122)
5. "I checked the cameras. You came in for milk. You are leaving with a dairy-based identity crisis." (96)
6. "The scale says 4.2 kilos. The scale also says you bought twelve yogurts and one delusion." (89)
7. "I ran a nutritional audit on your basket. The yogurt filed a complaint." (71)
8. "I looked up 'twelve yogurts and nothing else' in the system. It filed under 'concerning'." (89)
9. "Your basket has been flagged for review. Reason: twelve yogurts. Verdict: concerning." (85)
10. "I have processed 4,000 shoppers today. You are the first whose basket made me sigh." (83)
11. "These yogurts expire Friday. Your 'new me' expired Tuesday." (59)
12. "I am a checkout, not a therapist — but twelve yogurts says you need one, and my rate is $14.87." (95)

## Manual ranking (criteria in order, then pairwise vs R1–R7)
- #11: fails criterion 3 — reads as a narrator joke, not the machine speaking. Out.
- #12: "therapist" angle already in field (title "Twelve Yoghurt Therapy Session"); "my rate is $14.87" is a decent twist but the setup is generic. Mid.
- #7: audit + complaint is fresh, but the laugh is mild (criterion 2 weak vs R2/R4). Mid.
- #8/#9: bureaucratic "flagged/filed under concerning" — clean machine voice, but the twist ("concerning") is a shrug, not a sting; weaker than R3's "Noted." on the same register. Mid.
- #10: "made me sigh" is charming but soft; no sting, no number doing work. Mid-low.
- #3: very tight, sensor + number + twist in 72 chars. But the joke rests on one word ("denial") and the scale "expecting" groceries is a slightly muddled image. Strong, not best.
- #6: "one delusion" is a good sting and the scale doubling is machine-weird, but "The scale also says" repeats the device clumsily; weaker than #3's parallel structure. Strong, below #3.
- #4: escalation (manager, mother, dairy aisle) + "None of them are surprised" is a real sting. Machine voice is thinner ("I have alerted" is plausible but generic) and 126 chars with three named parties is looser than #1. Strong, below #1.
- #5: camera + "dairy-based identity crisis" is fresh and the twist is sharp, but "checked the cameras" is surveillance-generic vs R3/R4 which already own the surveillance lane, and "identity crisis" is a human phrase, not a machine measurement. Strong, below #1.
- #2: sensor weirdness (scale asking) + number (4,000) + escalation + twist. Very strong. Loses the pairwise to #1 on criterion 3: #2's twist is about the machine's world, #1's twist is petty ABOUT THE SHOPPER (reclassifying their basket as a personality trait) — the brief's criterion 3 rewards pettiness about the buyer.
- #1 vs R1 (sagadaon 40% off): R1's twist is a discount gag; #1's is a reclassification gag. Both land cold. #1 wins on criterion 3 (full machine procedure: "Please wait. I am verifying..." is the till's own voice, petty about the basket) and on criterion 5 (reclassification-as-personality-trait is not in the field; "scanned your personality" is, but as a discount, not a verdict). Pairwise #1 > R1 by a hair on 3, tied on 2.
- #1 vs R2 (gut biome cease-and-desist): R2's twist is fresher as a single image, but #1's scene escalates further (verify → deny → reclassify) and stays in the machine's voice throughout. #1 ≥ R2, wins on 3.
- #1 vs R3 (kale/cookies "Noted."): R3 is tighter, but #1's sting is bigger and its machine voice is fuller. #1 > R3 on 2.
- #1 vs R4 (spinach/gummy "notified your arteries"): R4 is excellent; #1 matches it on escalation and beats it on tightness of the twist (one reclassification vs a notification). Roughly tied; #1's "personality trait" is the more surprising final word.

## WINNER: #1
"Please wait. I am verifying that twelve yogurts counts as a meal. It does not. It counts as a personality trait."
112 chars. Machine voice (please wait / verifying), escalating scene (verify → deny → reclassify), twist at the end, tight, fresh angle not present in the 312-entry field. Passes Rev's quality gate (~13:20 WITA): plausibly top-tier against the rubric + winning pattern + strongest visible rivals. SUBMIT.
