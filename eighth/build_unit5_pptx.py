#!/usr/bin/env python3
"""IT250 (eighth) Unit 5 deck — Economics of Information (S34-S41), built to
COURSE_MATERIAL_STANDARD.md INCLUDING the §7A depth rule: every confusable set is a comparison
table, every 'X vs not-X' concept a concrete-example table, claims get scaffolding tables — each
table on its OWN slide, paginated, never squeezed. Self-contained & PDF-safe. Imports deckkit.py.
Diagrams in images/. Localised to Nepal (Hamrobazar, manpower/education agencies, Daraz, eSewa/
Khalti, Foodmandu/Pathao gig, Nepali creators/piracy). This unit's value-add is the ECONOMICS
RIGOR the old lectures lacked: the market-for-lemons mechanism (worked), signaling vs screening,
the economics of search, the Shapiro-Varian strategy toolkit, labor polarization, and the four IP
types. Source: syllabus + instructor PDFs (mapped in Unit5_content_outline.md §0). No real past-paper.
Run: python3 build_unit5_pptx.py -> IT250_Unit5.pptx
"""
from deckkit import *

# ============================================================
#                        FRONT MATTER
# ============================================================
add_title("Unit 5 — Economics of Information",
          "IT 250: Digital Economy  ·  BIM 8th Semester  ·  Sessions S34–S41 (8 lecture hours)",
          "Self-contained slides with depth: every concept grounded in comparison & concrete-example TABLES "
          "(Nepal-localised) — no abstraction without instances. The economics rigor (lemons mechanism, "
          "signaling/screening, Shapiro–Varian strategy) built fresh. Exports to PDF with no information lost.")

add_outcomes("Unit 5 — Learning Outcomes","economics of information  ·  s34–s41",
    "By the end of this unit, you will be able to:",
    ["Explain information as an economic good and distinguish symmetric vs asymmetric information (S34)",
     "Explain adverse selection & moral hazard (before/after the deal), the market for lemons, and the determinants of asymmetry (S35)",
     "Explain how digitalization, signaling & screening reduce asymmetry — and the new asymmetries digital markets create (S36)",
     "Explain how online search engines and AI reshape information economics (search cost, market efficiency, new power) (S37–S38)",
     "Apply the new economics of information to strategy — versioning, price discrimination, lock-in, bundling (S39)",
     "Analyse digitalization's effects on consumer choice and labor markets, incl. polarization (S40)",
     "Explain the four intellectual-property types and how digitalization challenges them (S41)"],
    "This is Unit 5 of IT 250. It asks a deceptively simple question — what happens to an economy when its "
    "key good is INFORMATION? — and answers with the classic economics of asymmetric information, search, and "
    "intellectual property, seen through Nepal's digital markets.")

add_roadmap("Unit 5 — Roadmap","Where each session fits (S34–S41)",
    ["S34  Information as an economic good; symmetric vs asymmetric",
     "S35  Lemons, adverse selection & moral hazard ⭐",
     "S36  Reducing asymmetry: signaling, screening, digital",
     "S37  Online search engines & the economics of search",
     "S38  Artificial intelligence & information",
     "S39  Strategy & the new economics of information ⭐",
     "S40  Consumer choice & labor markets (polarization)",
     "S41  Intellectual property & digitalization (closes unit)"],
    ["Unit 1  Introduction (digital/K-economy, 4IR) — done",
     "Unit 2  Fundamentals of the digital economy — done",
     "Unit 3  Digital markets, strategy & innovation",
     "Unit 4  Digital transformation & currencies",
     "Unit 6  Digitalization — the Nepalese perspective"])

# ============================================================ S34
add_divider("Session 34 · Lecture hour 1 (of 8)","Information as an Economic Good",
    "You can sell a sack of rice once — after that it is gone. But you can sell the same song, app, or PDF to a "
    "million people and still keep the original. Information does not behave like a normal good, and that single "
    "difference rewrites its economics. What kind of 'good' is information, and why is who-knows-what a source of power?",
    "OPENING HOOK [~5 min]. Contrast selling rice (used up) with selling a song (copied endlessly). Agenda: information as an economic good -> symmetric vs asymmetric -> perfect vs imperfect & why info is costly.")

concept_understand("S34 · Concept 1 · [THEORY]","Information as an Economic Good",
    "Information is an economic good, but an unusual one. Unlike a physical good it is NON-RIVAL (many people can use the same information at once), REUSABLE (using it does not use it up), and near-free to COPY (the next copy costs almost nothing). It is also an 'experience good' — you often cannot judge its value until after you have consumed it.",
    ["Non-rival: my reading a fact does not stop you reading it — a sack of rice cannot be shared this way.",
     "Reusable / not used up: give information away and you STILL have it.",
     "High cost to CREATE the first copy, ~zero cost for every copy after (a song, an app, a report).",
     "Experience good: its worth is hard to know before you consume it — which is where asymmetry begins."],
    "s34_info_good.png","Rice is used up when shared; a song is not — information is non-rival, reusable, ~free to copy.",
    "~7 min. Use the physical-vs-information diagram. The 'give it away and still have it' line is the anchor for the whole unit.")
add_comparison_table("S34 · Concept 1 · comparison","Physical good vs information good",
    ["Question","Physical good (rice, a bike)","Information good (song, app, PDF)"],
    [["Rival?","Yes — if I use it, you cannot","No — millions can use it at once"],
     ["Used up by use?","Yes — it is consumed","No — reusable, never worn out"],
     ["Cost of the next copy","Real (materials, labour)","Near zero"],
     ["Give it away — still have it?","No — you lose it","Yes — you keep the original"],
     ["Value known before buying?","Usually (you can inspect)","Often not — an 'experience good'"],
     ["Nepal example","A sack of Bhaktapur rice","A Nepali song on a streaming app"]],
    per_page=6,widths=[1.9,2.5,2.6],fs=11,
    note="Because information is non-rival and near-free to copy, its economics differ from ordinary goods — pricing, property rights (S41), and who-knows-what (asymmetry) all behave unusually.")
concept_apply("S34 · Concept 1 · [THEORY]","Information as an Economic Good",
    "A Nepali artist spends months and real money recording one song (the costly first copy), but every stream after that costs the platform almost nothing (near-zero marginal copy cost). One listener streaming it does not stop another (non-rival), and the artist still owns the original after a million plays (reusable). That is exactly why music is sold by subscription/ads, not per physical unit — and why piracy is so easy (S41).",
    "\"Information is just another product priced like any good.\" It is not: because it is non-rival and near-free to copy, you cannot price it on marginal cost (that would be ~zero). Its value comes from usefulness and scarcity of ACCESS, not scarcity of copies — which is why it is sold by licence, subscription, or attention.",
    "Information is an economic good but an unusual one: it is non-rival (many can use it simultaneously), reusable (not used up), and near-free to copy (high cost for the first copy, ~zero for each further copy). It is also an experience good whose value is hard to judge before consumption. These traits mean information cannot be priced like a physical good and set up the whole unit — asymmetry, search, and intellectual property.",
    "economic good · non-rival · reusable · near-zero copy cost · experience good · first-copy cost")

concept_understand("S34 · Concept 2 · [THEORY]","Symmetric vs Asymmetric Information",
    "Information is symmetric when both sides of a deal know the same relevant facts, and asymmetric when one side knows more than the other. Asymmetric information is the normal case in real markets — the seller of a used bike knows its faults; the buyer does not. This imbalance gives the informed side power and can make the uninformed side reluctant to trade at all.",
    ["Symmetric: buyer and seller share the relevant facts — trade is fair and efficient.",
     "Asymmetric: one side (usually the seller/insider) knows more — an information imbalance.",
     "The informed side can exploit the gap (hide faults, overcharge); the uninformed side fears being cheated.",
     "Almost every real market is asymmetric to some degree — the question is how much, and who benefits."],
    None,"Symmetric = both know the same; asymmetric = one side knows more — and holds the power.",
    "~7 min. Use the used-bike on Hamrobazar as the running case: the seller knows the crash history, you don't.")
add_examples_table("S34 · Concept 2 · examples","Symmetric vs asymmetric information — Nepal examples",
    ["Situation","Who knows more?","Symmetric or asymmetric?","Consequence"],
    [["Used bike on Hamrobazar","Seller (crash/repair history)","Asymmetric","Buyer risks overpaying for a bad bike"],
     ["Buying packaged Wai Wai at a shop","Both (label, fixed price)","Roughly symmetric","Fair, quick trade"],
     ["Manpower/foreign-employment agency","Agency (real job terms abroad)","Asymmetric","Worker misled on pay/conditions"],
     ["Education consultancy for study-abroad","Consultancy (college quality, commissions)","Asymmetric","Student pushed to a paying partner college"],
     ["Health insurance applicant","Applicant (own health)","Asymmetric","Insurer cannot price risk correctly"],
     ["Stock price on NEPSE (public data)","Both (public disclosures)","More symmetric","Fairer pricing when data is disclosed"]],
    per_page=6,widths=[2.2,2.2,1.9,2.4],fs=10.5,
    note="Asymmetry is the norm, not the exception. Where one side knows much more (agencies, used goods, insurance), the uninformed side risks being exploited — the core problem the rest of the unit solves.")
concept_apply("S34 · Concept 2 · [THEORY]","Symmetric vs Asymmetric Information",
    "When a Nepali worker signs with a foreign-employment (manpower) agency, the agency knows the real salary, employer, and working conditions abroad; the worker often knows only what the agent chooses to tell. That is asymmetric information — and it is why so many workers arrive to find the job was not as promised. Compare buying a sealed packet of Wai Wai at a fixed price: both sides know the product, so the trade is fair and instant.",
    "\"Asymmetric information just means one side is smarter.\" No — it means one side has more RELEVANT facts about the specific deal (the bike's faults, the job's real terms), regardless of intelligence. The problem is the imbalance of facts about the transaction, not general knowledge.",
    "Information is symmetric when both sides of a transaction share the same relevant facts and asymmetric when one side knows more than the other. Asymmetric information is the normal case in real markets (the used-bike seller knows the faults; the buyer does not), and it gives the informed side power while making the uninformed side reluctant to trade. It is the central problem of the economics of information.",
    "symmetric information · asymmetric information · information imbalance · informed vs uninformed side")

concept_understand("S34 · Concept 3 · [THEORY]","Perfect vs Imperfect Information — and Why Info Is Costly",
    "Classical economics assumes PERFECT information: everyone knows all prices, qualities, and options for free. Reality is IMPERFECT information: knowledge is incomplete and, crucially, COSTLY to obtain — it takes time, money, and effort to find and verify. Because information is costly, people economise on it (they search only so much), and gaps in quality open up between good and bad information.",
    ["Perfect information (a textbook ideal): all facts known to all, instantly and free.",
     "Imperfect information (reality): facts are incomplete, scattered, and costly to gather/verify.",
     "Search has a cost (time, travel, fees), so people stop searching before they know everything.",
     "Information also varies in QUALITY — accuracy, completeness, timeliness, source, relevance."],
    None,"Perfect info is a textbook ideal; real info is imperfect and COSTLY to get — so we never fully know.",
    "~7 min. Bridge to S37 (search cost) here: because info is costly to gather, search engines that cut that cost are economically huge.")
add_table_slide("S34 · Concept 3 · scaffolding","What makes information good — the quality dimensions",
    ["Quality dimension","What it means","Example of failing it"],
    [["Accuracy","Is it correct / true?","A fake product spec on a listing"],
     ["Completeness","Are key facts missing?","A used bike ad hiding accident history"],
     ["Timeliness","Is it current?","Yesterday's out-of-date price"],
     ["Source / credibility","Can the source be trusted?","An anonymous unverified review"],
     ["Relevance","Does it fit YOUR decision?","Specs that ignore what you actually need"],
     ["Verifiability","Can it be checked?","A claim with no proof or record"]],
    per_page=6,widths=[1.8,2.6,2.6],fs=11,
    note="'More information' is not automatically better — low-quality information (inaccurate, incomplete, stale, unverifiable) can mislead. Digital tools (S36–S38) help by raising quality and lowering the cost of getting it.")
concept_apply("S34 · Concept 3 · [THEORY]","Perfect vs Imperfect Information",
    "Before online prices, a Kathmandu shopper who wanted the cheapest fridge had to physically visit shops in New Road, spending a whole day (a real search cost) and still never seeing every price — imperfect information. They would give up after a few shops, so identical fridges sold at different prices in different shops. Daraz price listings cut that search cost toward zero, which is why online prices cluster much closer together (the theme of S37).",
    "\"With the internet, information is now perfect and free.\" It is cheaper and more complete, but still imperfect: results are incomplete, some information is low-quality or fake, and verifying it still costs effort. Digital lowers the cost of information dramatically but never reaches the textbook ideal of perfect information.",
    "Classical economics assumes perfect information (all facts known to everyone, instantly and free), but reality is imperfect information: knowledge is incomplete and costly to obtain, so people economise on search and stop before knowing everything. Information also varies in quality — accuracy, completeness, timeliness, source credibility, relevance, and verifiability. Because getting good information is costly, tools that cut that cost (search engines, AI) are economically powerful.",
    "perfect information · imperfect information · search cost · information quality · costly to obtain")

add_activity("S34 — 'Who knows more?'  ·  ~5 min",
    ["In pairs (2 min): pick a Nepali transaction (Hamrobazar bike, a manpower agency, an education consultancy, a tuition).",
     "Decide who knows more, and name ONE key fact the uninformed side is missing.",
     "Say whether it is symmetric or asymmetric, and what could go wrong.",
     "Take 3 answers aloud (3 min); confirm each identified the specific missing fact."],
    "Good answer (used bike): seller knows crash/repair history + real mileage; buyer is missing it; asymmetric; buyer risks overpaying for a lemon. Reward naming a SPECIFIC missing fact, not just 'the seller knows more'.",
    "ACTIVITY [~5 min].")
add_quiz("S34 — Quick Check  ·  ~5 min",
    [("Q1.  Which is a defining trait of information as an economic good?","q"),
     ("a) it is used up when consumed   b) ✅ it is non-rival — many can use it at once   c) each copy is costly   d) its value is always known in advance","a"),
     ("     Why: information is non-rival, reusable, and near-free to copy — unlike a physical good.","o"),
     ("Q2.  A used-bike seller knowing faults the buyer cannot see is an example of:","q"),
     ("a) perfect information   b) symmetric information   c) ✅ asymmetric information   d) a network effect","a"),
     ("     Why: one side (the seller) holds relevant facts the other lacks — an information imbalance.","o"),
     ("Discussion: name a Nepali deal where one side clearly knows much more, and the fact that's hidden.","o")],
    "QUIZ [~5 min]. Cement non-rival/reusable and the symmetric-vs-asymmetric distinction — the base for S35.")
add_summary("S34 · Summary  ·  [~2 min]",
    ["Information is an economic good but non-rival, reusable, and near-free to copy — priced by access, not by copy cost.",
     "Information is symmetric when both sides know the same, asymmetric when one side knows more (the normal case, and a source of power).",
     "Real markets have imperfect, costly information that also varies in quality — so tools that cut search cost and raise quality are valuable."],
    "Every deal you make — buying a used phone, signing with an agency, choosing a college — is shaped by who knows what. Seeing the information imbalance is the first step to protecting yourself and to understanding why digital markets are built the way they are.",
    "S35 — the imbalance in action: adverse selection, moral hazard, and the market for lemons (with numbers).",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S35
add_divider("Session 35 · Lecture hour 2 (of 8)","Lemons, Adverse Selection & Moral Hazard",
    "Why is a brand-new bike worth far less the moment you ride it out of the showroom? And why does a market full "
    "of cheap used goods often end up selling only the WORST ones? George Akerlof won a Nobel Prize explaining this "
    "with a 'market for lemons'. Today we build that mechanism with real numbers — and separate the problem BEFORE a deal from the problem AFTER it.",
    "OPENING HOOK [~5 min]. Ask why a new bike loses value instantly. Agenda: adverse selection + the lemons cascade (worked) -> moral hazard -> the 5 determinants of asymmetry.")

concept_understand("S35 · Concept 1 · [THEORY] [EXAMPLE]","Adverse Selection & the Market for Lemons (worked)",
    "Adverse selection is a BEFORE-the-deal problem: because buyers cannot tell good from bad, they offer only an AVERAGE price — which drives the good sellers OUT and leaves mostly bad goods ('lemons'). Worked example: good used bikes are worth Rs 120k, lemons Rs 40k. Buyers can't tell them apart, so they offer the average (~Rs 80k). Good sellers refuse (80k < 120k) and exit; only lemons remain; buyers learn and cut their offer toward 40k. The good is driven out by the bad.",
    ["The problem happens BEFORE the transaction — at the point of selecting what to trade.",
     "Buyers who can't verify quality rationally pay only an AVERAGE price.",
     "At the average, good-quality sellers lose money and withdraw — adverse selection.",
     "Left with mostly lemons, the market can shrink or collapse (Akerlof, 1970)."],
    "s35_lemons.png","Can't tell good from bad -> pay the average -> good sellers exit -> only lemons left.",
    "~9 min. WALK the numbers slowly on the s35_lemons cascade — this mechanism is the unit's headline and the old lectures never modelled it.")
add_table_slide("S35 · Concept 1 · scaffolding","The lemons cascade — step by step (used bikes on Hamrobazar)",
    ["Step","What happens","Result"],
    [["1. Two qualities exist","Good bikes worth Rs 120k; lemons worth Rs 40k","Mixed market"],
     ["2. Buyer can't tell which","No way to verify true condition","Quality is hidden"],
     ["3. Buyer offers the average","Pays ~Rs 80k to cover the risk","Fair only 'on average'"],
     ["4. Good sellers refuse","Rs 80k < Rs 120k, so they exit","Good bikes leave the market"],
     ["5. Mostly lemons remain","Buyers notice quality falling","Trust drops further"],
     ["6. Price collapses toward 40k","Only lemons trade","Adverse selection — market shrinks"]],
    per_page=6,widths=[1.9,2.9,2.2],fs=10.8,
    note="The engine is the AVERAGE price: paying an average punishes good sellers and rewards bad ones, so quality falls in a cascade. Fixing it (S36) means letting buyers tell good from bad — signals and screening.")
concept_apply("S35 · Concept 1 · [THEORY] [EXAMPLE]","Adverse Selection & the Market for Lemons",
    "Hamrobazar's used-bike market shows adverse selection. An honest seller with a well-kept bike wants Rs 120k, but buyers — burned before and unable to verify — will only offer an 'average' price around Rs 80k to cover the risk of a hidden lemon. The honest seller walks away and sells privately or not at all; the market fills with lower-quality bikes; buyers offer even less. The good is driven out by the bad — exactly Akerlof's result.",
    "\"Adverse selection just means some products are bad.\" No — it is a selection MECHANISM: hidden quality forces average pricing, which selects the BAD goods into the market and pushes the good ones out. The problem is not that lemons exist; it is that asymmetry makes lemons DOMINATE.",
    "Adverse selection is a before-the-deal problem: because buyers cannot distinguish good from bad quality, they rationally offer only an average price, which drives good-quality sellers out (they lose money at the average) and leaves the market dominated by 'lemons'. Worked: good bikes worth Rs 120k and lemons worth Rs 40k trade at an average ~Rs 80k, so good sellers exit and price cascades toward 40k. This is Akerlof's 'market for lemons' (1970).",
    "adverse selection · before the deal · hidden quality · average price · lemons · Akerlof · good driven out by bad")

concept_understand("S35 · Concept 2 · [THEORY]","Moral Hazard — the After-the-Deal Problem",
    "Moral hazard is an AFTER-the-deal problem: once a deal is struck, one party changes their behaviour because they no longer bear the full consequences. The classic case is insurance — a person drives more carelessly after insuring the bike, because the insurer now bears the loss. The key contrast: adverse selection is about HIDDEN QUALITY before signing; moral hazard is about HIDDEN ACTION after signing.",
    ["The problem happens AFTER the transaction — a change in behaviour once protected.",
     "Cause: one side no longer bears the full cost/risk of their actions.",
     "Insurance: insured people take more risk (they are covered); insurers add deductibles to counter it.",
     "Also in lending, employment (shirking), and platforms (a rider gaming incentives)."],
    None,"Moral hazard = hidden ACTION after the deal; adverse selection = hidden QUALITY before it.",
    "~7 min. The before/after axis is the exam point. Insurance is the cleanest case; add a gig-work example (a driver gaming bonus rules).")
add_comparison_table("S35 · Concept 2 · comparison","Adverse selection vs moral hazard",
    ["Question","Adverse selection","Moral hazard"],
    [["When does it occur?","BEFORE the deal","AFTER the deal"],
     ["What is hidden?","Quality / type (who you are)","Action / behaviour (what you do)"],
     ["Core problem","Bad types select in; good exit","Behaviour worsens once protected"],
     ["Insurance example","Only high-risk people buy cover","Insured people take more risk"],
     ["Nepal example","Only sick people seek health cover","Careless driving after insuring the bike"],
     ["Typical fix","Signaling & screening (S36)","Deductibles, monitoring, incentives"]],
    per_page=6,widths=[1.9,2.5,2.6],fs=11,
    note="Memory anchor: adverse selection = a SELECTION problem (who enters), moral hazard = a HAZARD of changed behaviour (what they do next). Before vs after the signature is the fastest way to tell them apart.")
concept_apply("S35 · Concept 2 · [THEORY]","Moral Hazard",
    "A Nepali health-insurance case shows both. BEFORE signing, mainly people who already feel unwell rush to buy cover — adverse selection (hidden type). AFTER signing, some insured people visit doctors more freely or take less care because the insurer pays — moral hazard (hidden action). Insurers fight adverse selection with medical screening forms, and moral hazard with deductibles and co-payments so the insured still shares the cost.",
    "\"Adverse selection and moral hazard are the same insurance problem.\" They are opposite in time: adverse selection is hidden QUALITY that selects bad types in BEFORE the contract; moral hazard is hidden ACTION that worsens behaviour AFTER it. Mixing them up is the most common exam mistake.",
    "Moral hazard is an after-the-deal problem: once protected by a contract, a party changes behaviour because it no longer bears the full consequences (an insured person drives more carelessly; a borrower takes bigger risks). It contrasts with adverse selection, which is a before-the-deal problem of hidden quality/type. Fixes for moral hazard include deductibles, co-payments, monitoring, and aligned incentives.",
    "moral hazard · after the deal · hidden action · changed behaviour · deductibles/monitoring · vs adverse selection")

concept_understand("S35 · Concept 3 · [THEORY]","The Five Determinants of Asymmetry",
    "How large the information gap is depends on five determinants: COST of getting information (high cost -> big gap), ACCESS to information (restricted access -> big gap), COMPLEXITY of the product (complex -> harder to judge), TECHNOLOGY available (better tech -> smaller gap), and REGULATION / disclosure rules (strong rules -> smaller gap). Change any of these and you change how exploitable a market is.",
    ["Cost: the more expensive it is to gather facts, the wider the asymmetry.",
     "Access: if only insiders can see the facts, the gap is large (agencies, hospitals).",
     "Complexity: complex products (insurance, loans, gadgets) are harder for buyers to judge.",
     "Technology & regulation SHRINK the gap: comparison tools, reviews, and disclosure laws help."],
    None,"Five determinants: cost · access · complexity · technology · regulation — they widen or shrink the gap.",
    "~6 min. Frame tech and regulation as the two 'gap-shrinkers' — they set up S36 (digital reduces asymmetry).")
add_examples_table("S35 · Concept 3 · examples","The five determinants — Nepal examples",
    ["Determinant","Widens or shrinks the gap?","Nepal example"],
    [["Cost of information","High cost widens it","Verifying a used bike needs a paid mechanic"],
     ["Access to information","Restricted access widens it","Manpower agency alone knows the real job terms"],
     ["Complexity of product","Complexity widens it","Insurance/loan fine print hard to judge"],
     ["Available technology","Better tech shrinks it","Daraz reviews & price comparison"],
     ["Regulation / disclosure","Strong rules shrink it","NRB rules forcing banks to disclose real rates"],
     ["Trust / reputation systems","Reputation shrinks it","Hamrobazar seller ratings"]],
    per_page=6,widths=[2.0,2.3,2.7],fs=10.8,
    note="The first three (cost, access, complexity) WIDEN asymmetry; technology, regulation, and reputation SHRINK it. Digital markets pull hard on the shrinking levers — but can also create new gaps (S36).")
concept_apply("S35 · Concept 3 · [THEORY]","The Five Determinants of Asymmetry",
    "A study-abroad education consultancy is a high-asymmetry market on every determinant: verifying a foreign college's real quality is costly, access to honest information is limited (the consultancy earns commissions from partner colleges), the decision is complex, and Nepal's disclosure rules are weak. That is why students are so often steered to a commission-paying college. Reviews from past students (technology) and stronger disclosure rules (regulation) are exactly what would shrink the gap.",
    "\"Asymmetry is a fixed feature of a market.\" It is not fixed — it depends on cost, access, complexity, technology, and regulation. Improve technology (reviews, comparison) or regulation (disclosure) and the same market becomes far less exploitable. Asymmetry is a variable you can act on, not a constant.",
    "How large an information gap is depends on five determinants: the cost of obtaining information, access to it, the complexity of the product, the technology available, and regulation/disclosure rules. Cost, access, and complexity widen the gap; technology, regulation, and reputation systems shrink it. Because these are variables, asymmetry can be reduced — the theme of the next sessions on digitalization, signaling, and screening.",
    "determinants · cost · access · complexity · technology · regulation · gap widens/shrinks")

add_activity("S35 — 'Before or after?'  ·  ~5 min",
    ["Individually (1 min): read four mini-cases (used bike sale, insured careless driving, only-sick buy cover, borrower takes big risks after a loan).",
     "In pairs (2 min): label each ADVERSE SELECTION (before) or MORAL HAZARD (after), and say what is hidden.",
     "Take 3–4 answers aloud (2 min); tally which axis (before/after) each falls on.",
     "Close: one hides QUALITY before, the other hides ACTION after."],
    "Answers: used bike = adverse selection (hidden quality, before); insured careless driving = moral hazard (hidden action, after); only-sick-buy-cover = adverse selection; big risks after a loan = moral hazard. Reward correct before/after placement.",
    "ACTIVITY [~5 min].")
add_quiz("S35 — Quick Check  ·  ~5 min",
    [("Q1.  In the market for lemons, good sellers exit because buyers:","q"),
     ("a) prefer lemons   b) ✅ can't tell quality, so they offer only an AVERAGE price   c) pay too much   d) are dishonest","a"),
     ("     Why: average pricing makes selling a good product a loss, so good sellers withdraw — adverse selection.","o"),
     ("Q2.  An insured person driving more carelessly is an example of:","q"),
     ("a) adverse selection   b) ✅ moral hazard (hidden action after the deal)   c) signaling   d) price dispersion","a"),
     ("     Why: behaviour changes AFTER the contract because the insurer now bears the cost — moral hazard.","o"),
     ("Discussion: give one Nepali market where 'good is driven out by bad' and explain why.","o")],
    "QUIZ [~5 min]. Drill the lemons mechanism and the before/after axis separating the two problems.")
add_summary("S35 · Summary  ·  [~2 min]",
    ["Adverse selection (BEFORE the deal): hidden quality forces average pricing, driving good sellers out — the market for lemons (Akerlof).",
     "Moral hazard (AFTER the deal): once protected, a party changes behaviour because it no longer bears the full cost.",
     "The size of the gap depends on 5 determinants — cost, access, complexity, technology, regulation — which can widen or shrink it."],
    "Adverse selection explains used-goods and manpower/consultancy markets in Nepal; moral hazard explains insurance and lending. Knowing which problem you face tells you which fix to reach for — and that is exactly what the next session builds.",
    "S36 — the fixes: signaling, screening, and how digitalization both reduces and re-creates asymmetry.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S36
add_divider("Session 36 · Lecture hour 3 (of 8)","Reducing Asymmetry: Signaling, Screening & Digitalization",
    "If hidden quality drives the good out of the market, how does any used-goods, job, or insurance market survive? "
    "Because both sides fight back: the side that KNOWS finds ways to PROVE it (a warranty, a degree), and the side "
    "that DOESN'T finds ways to TEST for it (a test drive, an insurance form). Add the internet, and reviews do this at scale — but create brand-new asymmetries too.",
    "OPENING HOOK [~5 min]. Ask how you'd convince a stranger your used phone is genuinely good. Agenda: signaling (informed side proves) -> screening (uninformed side sorts) -> digital as gap-reducer AND new-gap-creator.")

concept_understand("S36 · Concept 1 · [THEORY]","Signaling — the Informed Side Proves Quality",
    "Signaling is when the side that HAS the information takes a costly, credible action to PROVE quality to the uninformed side. A signal only works if it is hard for a low-quality type to fake — that is what makes it believable. Classic signals: a seller's warranty or money-back guarantee, a brand reputation, a professional certification, and (in the labor market) an education degree that signals ability to employers.",
    ["The INFORMED side acts (seller, worker) — they move first to reveal quality.",
     "A credible signal is costly and hard to fake by a bad type (a real warranty costs a scammer dearly).",
     "Examples: warranty, brand, certification, verified badge, and education as a job-market signal.",
     "Education-as-signal: a degree can signal ability even beyond the skills it teaches (Spence)."],
    "s36_signal_screen.png","Signaling = the side WITH the info proves it (warranty, degree, brand) — hard to fake.",
    "~8 min. Use the top half of the signal/screen diagram. Stress 'credible = costly to fake' — that is why a warranty works and cheap talk doesn't.")
add_comparison_table("S36 · Concept 1 · comparison","Signaling vs screening — who acts?",
    ["Question","Signaling","Screening"],
    [["Who acts?","The INFORMED side","The UNINFORMED side"],
     ["What they do","Send a credible, costly signal","Design a test / menu to sort types"],
     ["Direction","Informed -> proves to uninformed","Uninformed -> makes others reveal"],
     ["Labor-market example","Worker earns a degree (signal)","Employer sets a test / probation"],
     ["Used-goods example","Seller offers a warranty","Buyer insists on a test drive"],
     ["Insurance example","Safe driver shows clean record","Insurer offers a menu of deductibles"]],
    per_page=6,widths=[1.9,2.5,2.6],fs=11,
    note="One line to remember: SIGNALING = the side WITH the information proves it; SCREENING = the side WITHOUT it designs a test so the truth reveals itself. Same goal (close the gap), opposite actor.")
concept_apply("S36 · Concept 1 · [THEORY]","Signaling",
    "A trusted seller on Hamrobazar signals quality by offering a short warranty, posting real photos and bills, and building a rated profile — costly, hard-to-fake actions a scammer would avoid, so buyers believe them. In Nepal's job market, a bachelor's degree signals to employers that a candidate has the discipline and ability to finish it, which is part of why graduates are hired even for roles the degree didn't directly train them for.",
    "\"Any claim of quality is a signal.\" Only a CREDIBLE signal counts — one that is costly and hard for a low-quality type to fake. Saying 'trust me, it's a good bike' is cheap talk; a genuine warranty, a verified track record, or a hard-won certification is a real signal because a fraud couldn't afford to offer it.",
    "Signaling is when the informed side takes a costly, credible action to prove quality to the uninformed side, working only because it is hard for a low-quality type to fake. Examples include warranties and guarantees, brand reputation, professional certifications, verified profiles, and (in the labor market, per Spence) an education degree that signals ability to employers. Signaling attacks adverse selection by letting good quality reveal itself.",
    "signaling · informed side acts · credible = costly to fake · warranty/brand/certification · education as signal")

concept_understand("S36 · Concept 2 · [THEORY]","Screening — the Uninformed Side Sorts",
    "Screening is the mirror image: the side that LACKS information designs a test, menu, or condition that makes the informed side reveal their true type (self-selection). An insurer offering a menu of policies (low premium + high deductible vs high premium + low deductible) screens: safe drivers pick one, risky drivers pick the other. A buyer insisting on a test drive, or an employer using a probation period, is screening too.",
    ["The UNINFORMED side acts (buyer, employer, insurer) — they set the test.",
     "Self-selection: a well-designed menu makes each type choose the option that reveals them.",
     "Examples: insurance forms/deductible menus, test drives, product trials, interviews, probation.",
     "Reviews and ratings are a collective screening tool — the crowd tests quality for you."],
    None,"Screening = the uninformed side sets a test/menu so the informed side reveals its type (self-selection).",
    "~7 min. Use the bottom half of the diagram. The deductible menu is the sharpest example of self-selection — walk it briefly.")
add_table_slide("S36 · Concept 2 · scaffolding","Mechanisms that reduce asymmetry — signal or screen?",
    ["Mechanism","Signal or screen?","Nepal / digital example"],
    [["Warranty / money-back guarantee","Signal (seller proves)","Daraz return policy; shop warranty"],
     ["Brand & reputation","Signal (seller proves)","Wai Wai brand trust; verified store"],
     ["Certification / degree","Signal (worker proves)","IT certifications; a BIM degree"],
     ["Test drive / product trial","Screen (buyer tests)","Test-riding a used bike before buying"],
     ["Insurance deductible menu","Screen (insurer sorts)","Choose premium vs deductible level"],
     ["Reviews & ratings","Screen (crowd tests)","Hamrobazar / Daraz seller ratings"]],
    per_page=6,widths=[2.3,1.9,2.6],fs=10.8,
    note="Both directions close the gap. Reviews are special: they let the uninformed crowd screen quality cheaply and at scale — which is why digital platforms lean on them so heavily (next concept).")
concept_apply("S36 · Concept 2 · [THEORY]","Screening",
    "When you buy a used bike in Nepal, you screen: you insist on a test ride and take it to a mechanic, forcing the seller's hidden quality into the open. Insurers screen with a menu — a low-premium/high-deductible plan attracts confident safe drivers, while risky drivers pick the fuller cover, so the insurer sorts risk without ever reading minds. Daraz screens for you collectively: thousands of buyer ratings reveal which sellers are trustworthy.",
    "\"Screening and signaling are the same because both reduce asymmetry.\" They differ by WHO acts: signaling is done by the side WITH the information (it proves quality); screening is done by the side WITHOUT it (it designs a test so quality reveals itself). Same goal, opposite actor — that distinction is the exam point.",
    "Screening is when the uninformed side designs a test, menu, or condition that makes the informed side reveal its true type through self-selection. Examples: an insurer's menu of premium/deductible combinations (safe vs risky drivers self-select), a buyer's test drive or product trial, an employer's interview or probation, and reviews/ratings as collective screening. Screening is the mirror image of signaling — same goal of closing the gap, but the uninformed side acts.",
    "screening · uninformed side acts · self-selection · deductible menu · test drive/probation · reviews as screening")

concept_understand("S36 · Concept 3 · [THEORY]","Digitalization: Gap-Reducer AND New-Gap-Creator",
    "Digitalization is the biggest asymmetry-reducer ever: reviews, ratings, price-comparison, and verified profiles let strangers judge quality cheaply and at scale, so the old used-car 'lemons' problem is much smaller online. BUT digital markets create NEW asymmetries: fake reviews, paid/sponsored rankings, hidden algorithms deciding what you see, and platforms that know far more about you than you know about them. Digital reduces old gaps but shifts power to whoever controls the platform.",
    ["Reduces gaps: reviews, ratings, comparison, verified sellers, transaction history — cheap screening/signaling at scale.",
     "Old used-car market: buyer helpless; digital used-car market: history reports, ratings, return policies.",
     "New gaps: fake reviews, sponsored 'best' rankings, opaque algorithms, platform data advantage.",
     "Net effect: gaps move — from seller-vs-buyer to platform-vs-everyone (the power question of S40)."],
    None,"Digital shrinks old asymmetries (reviews, comparison) but creates new ones (fake reviews, hidden algorithms).",
    "~7 min. Balance the story: don't sell 'digital fixes everything'. The new gaps set up S37 (search gatekeeping) and S40 (who controls choice).")
add_examples_table("S36 · Concept 3 · examples","Used-goods market: old vs digital",
    ["Aspect","Old market (offline)","Digital market"],
    [["Judging quality","Trust the seller's word","Reviews, ratings, history reports"],
     ["Comparing prices","Visit many shops (costly)","Instant price comparison online"],
     ["Seller reputation","Local word of mouth only","Public rating visible to all"],
     ["Recourse if cheated","Little — hard to trace","Return policy, dispute, refund"],
     ["New problem created","—","Fake reviews & paid rankings"],
     ["Who now holds power","The informed seller","The platform (algorithm, data)"]],
    per_page=6,widths=[2.0,2.4,2.6],fs=10.8,
    note="Digital tools genuinely shrink the old buyer-vs-seller gap, but the last two rows show the catch: new asymmetries (fake reviews) and a new powerful party (the platform) appear. Gaps are reduced AND relocated.")
concept_apply("S36 · Concept 3 · [THEORY]","Digitalization as Gap-Reducer and Creator",
    "Buying a used phone on Hamrobazar today is far safer than a 2005 newspaper classified: seller ratings, buyer reviews, photos, and chat history let you screen quality cheaply — digital shrank the lemons gap. But new gaps appear: some sellers buy fake 5-star reviews, 'sponsored' listings sit at the top pretending to be 'best', and the platform's algorithm — which you can't see — decides what you're shown. The old gap shrank; a new platform-controlled gap opened.",
    "\"Digital markets remove information asymmetry.\" They REDUCE the old seller-vs-buyer gap but CREATE new ones — fake reviews, paid rankings, opaque algorithms, and a platform that knows more about you than you do about it. Asymmetry is reduced and relocated, not abolished — the power just shifts to the platform.",
    "Digitalization is the largest asymmetry-reducer ever: reviews, ratings, price-comparison, verified profiles, and transaction history let strangers judge quality cheaply and at scale, shrinking the classic used-car 'lemons' problem. But digital markets create new asymmetries — fake reviews, sponsored/paid rankings, opaque recommendation algorithms, and a platform data advantage. The net effect is that gaps are reduced but also relocated, from seller-vs-buyer toward platform-vs-everyone.",
    "digital reduces asymmetry · reviews/ratings/comparison · new asymmetries · fake reviews · sponsored rank · platform power")

add_activity("S36 — 'Signal or screen — and can it be gamed?'  ·  ~5 min",
    ["In pairs (2 min): pick a Nepali market (used bikes, hiring, insurance, Daraz).",
     "Name one SIGNAL the informed side uses and one SCREEN the uninformed side uses.",
     "Name one way digital could FAKE the signal (e.g. fake reviews) — a new asymmetry.",
     "Take 3–4 answers aloud (3 min); classify each as signal vs screen."],
    "Good answer (Daraz): signal = seller warranty/verified badge; screen = buyer reads ratings & returns; gamed by = bought fake reviews / sponsored top slot. Reward correctly assigning WHO acts and spotting the new digital gap.",
    "ACTIVITY [~5 min].")
add_quiz("S36 — Quick Check  ·  ~5 min",
    [("Q1.  A seller offering a warranty to prove quality is an example of:","q"),
     ("a) screening   b) ✅ signaling (the informed side proves quality)   c) moral hazard   d) price dispersion","a"),
     ("     Why: the side WITH the information acts, using a costly, hard-to-fake action — a signal.","o"),
     ("Q2.  An insurer offering a menu of deductibles so drivers self-select is:","q"),
     ("a) signaling   b) a network effect   c) ✅ screening (the uninformed side sorts types)   d) adverse selection","a"),
     ("     Why: the side WITHOUT the information designs a test/menu so the truth reveals itself — screening.","o"),
     ("Discussion: name one NEW asymmetry digital markets created, even as they reduced old ones.","o")],
    "QUIZ [~5 min]. Nail who-acts (signal vs screen) and the 'reduced but relocated' effect of digital.")
add_summary("S36 · Summary  ·  [~2 min]",
    ["Signaling: the INFORMED side proves quality with a costly, hard-to-fake action (warranty, brand, degree).",
     "Screening: the UNINFORMED side designs a test/menu so types self-select (deductibles, test drive, reviews).",
     "Digitalization is the biggest gap-reducer (reviews, comparison) but creates new gaps (fake reviews, paid rankings, opaque algorithms) — power shifts to the platform."],
    "Signals and screens are how you protect yourself in any deal — and how you'd design trust into a platform you build. Recognising fake signals and sponsored rankings is a survival skill in Nepal's fast-growing online markets.",
    "S37 — the tool that made search cheap: online search engines and the economics of search.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S37
add_divider("Session 37 · Lecture hour 4 (of 8)","Online Search Engines & the Economics of Search",
    "Twenty years ago, finding the cheapest laptop in Kathmandu meant a full day walking New Road. Today it takes ten "
    "seconds. Search engines didn't just make life convenient — they collapsed the COST of information, which changed "
    "prices themselves. But the search box is also a gatekeeper: who decides which result you see first, and who paid to be there?",
    "OPENING HOOK [~5 min]. Contrast a day walking shops vs a 10-second search. Agenda: search cost & price dispersion -> comparison markets & fair value -> the search engine as a NEW gatekeeper (SEO, paid ranking).")

concept_understand("S37 · Concept 1 · [THEORY]","Search Cost & Price Dispersion",
    "Search cost is the time, effort, and money it takes to find and compare options. When search is costly, identical products sell at very different prices — that spread is PRICE DISPERSION, and it exists precisely because buyers cannot afford to check every seller. Search engines and price-comparison tools slash search cost toward zero, so prices for the same item cluster much closer together.",
    ["Search cost = time + travel + effort + fees to find and compare options.",
     "High search cost -> big price dispersion: the same fridge costs different amounts in different shops.",
     "Sellers exploit lazy search: they can charge more when buyers won't compare.",
     "Cut search cost (search engines, comparison sites) -> dispersion shrinks toward one fair price."],
    None,"Search cost = effort to compare. High cost -> big price gaps; cheap search -> prices converge.",
    "~7 min. Connect back to S34's 'information is costly'. Price dispersion is the visible symptom of costly search.")
add_examples_table("S37 · Concept 1 · examples","Before vs after search engines",
    ["Aspect","Before (high search cost)","After (low search cost)"],
    [["Finding a price","Visit shops all day","Search / compare in seconds"],
     ["Price dispersion","Large — same item varies a lot","Small — prices converge"],
     ["Buyer's knowledge","Sees a few options","Sees the whole market"],
     ["Seller's power to overcharge","High (buyers can't compare)","Low (buyers compare instantly)"],
     ["Bargaining position","Weak buyer","Stronger, informed buyer"],
     ["Nepal example","Walking New Road for a laptop","Comparing laptops on Daraz/Hamrobazar"]],
    per_page=6,widths=[2.0,2.5,2.5],fs=10.8,
    note="The single biggest economic effect of search engines is cutting search cost — which shrinks price dispersion, weakens sellers' power to overcharge, and shifts bargaining power toward the informed buyer.")
concept_apply("S37 · Concept 1 · [THEORY]","Search Cost & Price Dispersion",
    "Before Daraz, the same model of rice cooker could cost noticeably different amounts in different Kathmandu shops, because checking every shop cost a buyer a whole afternoon — high search cost, wide price dispersion. Now a buyer compares dozens of listings in seconds, so sellers who overprice simply don't sell, and prices for the identical cooker cluster tightly. Cheap search transferred power from the seller who relied on lazy comparison to the informed buyer.",
    "\"Price differences just mean some shops are greedy.\" Often they reflect SEARCH COST: when comparing is expensive, sellers can charge more to buyers who won't shop around — that spread is price dispersion. Lower the search cost and the dispersion shrinks on its own, without anyone becoming less greedy.",
    "Search cost is the time, effort, and money needed to find and compare options. When search is costly, identical products sell at widely different prices — price dispersion — because buyers cannot check every seller, so sellers can overcharge the ones who won't compare. Search engines and price-comparison tools cut search cost toward zero, shrinking price dispersion, weakening sellers' power to overcharge, and shifting bargaining power to the informed buyer.",
    "search cost · price dispersion · comparison · converging prices · buyer power · overcharging the lazy searcher")

concept_understand("S37 · Concept 2 · [THEORY]","Comparison Markets & Near-Fair-Value Pricing",
    "When search cost is near zero, a market becomes a COMPARISON MARKET: every buyer can see every offer, so sellers are forced to compete on price and quality until the price sits close to the good's true (fair) value. This pushes markets toward the textbook ideal of efficiency, benefiting buyers. The flip side: sellers lose pricing power and must compete harder, and some respond by differentiating or by gaming the comparison (S37 concept 3).",
    ["Comparison market: everyone sees everyone's offer -> intense price/quality competition.",
     "Prices converge toward fair value — closer to the efficient, low-asymmetry ideal.",
     "Buyers win: less overpaying, more transparency, easier switching.",
     "Sellers respond: differentiate (brand, service) or try to game rankings to escape pure price competition."],
    None,"Cheap search -> comparison market -> prices pushed toward fair value; buyers gain, sellers compete harder.",
    "~7 min. Tie to S34/S35: cheaper search reduces asymmetry, moving the market toward the efficient, symmetric ideal.")
add_table_slide("S37 · Concept 2 · scaffolding","How search engines reduce information cost",
    ["Search-engine function","What it does","Effect on the market"],
    [["Aggregation","Gathers many sellers in one place","See the whole market at once"],
     ["Comparison","Lines up prices & specs side by side","Price dispersion shrinks"],
     ["Filtering / ranking","Sorts by price, rating, relevance","Faster, better-matched choices"],
     ["Reviews surfaced","Shows others' experiences","Quality becomes visible (screening)"],
     ["Instant access","Answers in seconds, anywhere","Search cost falls to near zero"],
     ["Personalization","Tailors results to you","Better match — but less neutral (concept 3)"]],
    per_page=6,widths=[2.0,2.6,2.4],fs=10.8,
    note="Each function chips away at search cost and asymmetry — pushing the market toward fair-value pricing. The last row hints at the catch: personalised, ranked results are powerful but no longer neutral.")
concept_apply("S37 · Concept 2 · [THEORY]","Comparison Markets & Fair Value",
    "Comparing domestic flights or hotels for a Pokhara trip online is a comparison market: dozens of prices sit side by side, so operators must price close to each other and to fair value or lose the booking. Buyers clearly win. But notice sellers fighting back — a hotel differentiates with 'free breakfast' or pays to appear first — because pure price comparison strips their pricing power. That tension between transparency and sellers' escape moves is the heart of digital search.",
    "\"If everyone can compare, prices become perfectly fair for everyone.\" They move TOWARD fair value, but never perfectly: sellers differentiate, personalise, and pay for ranking to escape pure comparison, and results are no longer neutral. Comparison markets improve efficiency greatly but don't deliver the textbook ideal.",
    "When search cost is near zero, a market becomes a comparison market: every buyer sees every offer, forcing sellers to compete on price and quality until prices sit close to fair value — pushing the market toward efficiency and benefiting buyers. Sellers, losing pricing power, respond by differentiating (brand, service) or by gaming rankings. So comparison markets greatly improve efficiency but stop short of the perfectly fair textbook ideal.",
    "comparison market · fair-value pricing · market efficiency · buyer benefit · seller differentiation")

concept_understand("S37 · Concept 3 · [THEORY]","The Search Engine as a New Gatekeeper",
    "The search engine that reduced asymmetry becomes a new source of it. What you see first is decided by an algorithm you cannot inspect, and sellers compete to influence it: SEO (search-engine optimisation) to rank higher organically, and PAID placement (ads, 'sponsored', 'promoted') to buy the top spot. So the top result is often the most OPTIMISED or most PAID, not the objectively 'best'. The gatekeeper's power — and its hidden incentives — is a new asymmetry.",
    ["Ranking is decided by a hidden algorithm — you can't see why result #1 is first.",
     "SEO: sellers optimise to rank higher organically (sometimes gaming, not improving, quality).",
     "Paid ranking: 'sponsored'/'promoted' slots sell the top position to the highest bidder.",
     "So 'top' = most optimised or most paid, not necessarily best — a NEW asymmetry the platform controls."],
    None,"The search box is a gatekeeper: 'top' result = most optimised/paid, decided by a hidden algorithm.",
    "~7 min. This is the fresh critical point. Have students recall the last time a 'Sponsored' result topped their search — that is paid ranking.")
add_examples_table("S37 · Concept 3 · examples","Genuine 'best' vs promoted result",
    ["What you see","Why it's there","What it really means"],
    [["Top organic result","Ranked high by the algorithm","Best-optimised, not always best product"],
     ["'Sponsored' / 'Ad' label","Seller paid for the slot","Paid placement, not merit"],
     ["'Promoted' listing on Daraz","Seller bought visibility","Advertising, not a quality signal"],
     ["'Best seller' / 'Choice' badge","Platform's own criteria","Platform decides — criteria hidden"],
     ["Personalised recommendation","Tuned to your data","Match to you AND to platform profit"],
     ["Fake-review-boosted item","Manipulated ratings","A gamed signal, not genuine quality"]],
    per_page=6,widths=[2.2,2.3,2.5],fs=10.8,
    note="The lesson: a high ranking is a mix of relevance, optimisation, and payment — not a neutral verdict on quality. A critical user learns to separate 'sponsored/promoted' from genuine organic results.")
concept_apply("S37 · Concept 3 · [THEORY]","The Search Engine as a Gatekeeper",
    "Search a product on Daraz and the first listings are often 'Sponsored' — the seller paid for that slot, not earned it by being best. Google works the same: ads sit above organic results, and businesses spend heavily on SEO to climb the rankings. The engine that saved you a day of walking New Road now quietly decides which sellers you even see — and the top of the page is frequently the most PAID, not the best. That gatekeeping is a new information asymmetry.",
    "\"The top search result is the best option.\" The top is the best-OPTIMISED or the best-PAID, chosen by a hidden algorithm with its own incentives (ad revenue). SEO and sponsored placement mean ranking reflects money and optimisation as much as merit — so a smart user reads past the sponsored slots.",
    "The search engine that reduces asymmetry becomes a new gatekeeper: what you see first is set by a hidden ranking algorithm, and sellers compete to influence it through SEO (optimising to rank higher organically) and paid placement (sponsored/promoted slots bought at the top). So the top result is often the most optimised or most paid, not the objectively best. The gatekeeper's opaque criteria and profit incentives are themselves a new information asymmetry the platform controls.",
    "gatekeeper · ranking algorithm (hidden) · SEO · paid/sponsored ranking · top ≠ best · new asymmetry")

add_activity("S37 — 'Spot the gatekeeper'  ·  ~5 min",
    ["Individually (1 min): recall your last online search or Daraz product search.",
     "In pairs (2 min): identify which top results were SPONSORED/paid vs organic, and how you could tell.",
     "Estimate how much search cost the tool saved you vs walking shops.",
     "Take 3–4 answers aloud (2 min); note how often 'top' meant 'paid'."],
    "Good answer: on Daraz the first 1–2 rows are 'Sponsored' (paid), lower ones organic; the tool saved a half-day of shop visits (search cost); 'top' often meant most-paid, not best. Reward spotting the sponsored label and estimating saved search cost.",
    "ACTIVITY [~5 min].")
add_quiz("S37 — Quick Check  ·  ~5 min",
    [("Q1.  Identical goods selling at very different prices is called:","q"),
     ("a) inflation   b) ✅ price dispersion (a symptom of high search cost)   c) a network effect   d) moral hazard","a"),
     ("     Why: when comparing is costly, sellers can charge different prices; cheap search shrinks the spread.","o"),
     ("Q2.  The top result in a search is best described as:","q"),
     ("a) always the best product   b) chosen at random   c) ✅ the most optimised or most paid, per a hidden algorithm   d) the cheapest","a"),
     ("     Why: SEO and paid/sponsored placement mean ranking reflects optimisation and money, not pure merit.","o"),
     ("Discussion: how could a search engine that REDUCES asymmetry also CREATE it?","o")],
    "QUIZ [~5 min]. Reinforce price dispersion and the gatekeeper idea (top = optimised/paid, not best).")
add_summary("S37 · Summary  ·  [~2 min]",
    ["Search cost is the effort to find & compare; high search cost causes price dispersion (same item, different prices).",
     "Cheap search turns markets into comparison markets — prices converge toward fair value and buyers gain power.",
     "But the search engine is a new gatekeeper: a hidden algorithm plus SEO and paid ranking mean 'top' = most optimised/paid, not best — a new asymmetry."],
    "Every time you compare prices online you're using the economics of search — and every 'Sponsored' label is the gatekeeper at work. Reading past paid rankings, and knowing why online prices cluster, makes you a sharper buyer and a sharper analyst of digital markets.",
    "S38 — the newest force reshaping information: artificial intelligence.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S38
add_divider("Session 38 · Lecture hour 5 (of 8)","Artificial Intelligence & Information",
    "A shopkeeper who remembered every customer's taste, spotted every fake note, and knew the fair price of everything "
    "would run an almost perfect market. That is roughly what AI does for digital markets — a tireless 'robot shopkeeper' "
    "reading oceans of data. It shrinks information gaps like nothing before it. But whose interests does the algorithm actually serve?",
    "OPENING HOOK [~5 min]. Use the 'robot shopkeeper' image. Agenda: AI reduces asymmetry -> recommendation engines & personalization (efficiency) -> AI's limits & ethics (bias, privacy, black-box).")

concept_understand("S38 · Concept 1 · [THEORY]","AI Reduces Information Asymmetry",
    "AI reduces asymmetry by reading and verifying data at a scale no human could — turning hidden information into visible signals. It detects fraud (spotting fake reviews, stolen cards, scam listings), verifies quality and identity, and surfaces the right facts to the right person. In effect AI acts as a 'smart librarian' that finds and checks information for the uninformed side, shrinking the gap between buyer and seller.",
    ["AI processes huge, messy data (transactions, reviews, images) to reveal hidden quality/risk.",
     "Fraud detection: flags fake reviews, scam sellers, and suspicious payments faster than humans.",
     "Verification: confirms identity, authenticity, and history — strengthening trust signals.",
     "Net effect: less hidden information, so markets get closer to the efficient, symmetric ideal."],
    "s38_ai_info.png","AI reads/verifies data at scale — detecting fraud and surfacing facts — shrinking the info gap.",
    "~7 min. Use the AI-gap diagram. Frame AI as an even more powerful version of S36's signals/screens — but automated.")
add_table_slide("S38 · Concept 1 · scaffolding","How AI changes the economics of information",
    ["AI capability","What it does","Effect on asymmetry"],
    [["Fraud detection","Flags fake reviews, scams, stolen cards","Removes false information"],
     ["Verified reviews / identity","Confirms real buyers & sellers","Strengthens trust signals"],
     ["Price & option comparison","Finds best deals instantly","Cuts search cost further"],
     ["Recommendation / matching","Pairs the right product to the buyer","Reduces mismatch"],
     ["Transparency tools","Summarises specs, terms, risks","Makes hidden facts visible"],
     ["Demand/price prediction","Forecasts and adjusts prices","Efficiency — but can hide logic"]],
    per_page=6,widths=[2.1,2.5,2.4],fs=10.8,
    note="AI is the strongest asymmetry-reducer yet — automating the signals and screens of S36 at massive scale. But the last row hints at the catch: the same power can create new, opaque gaps (concept 3).")
concept_apply("S38 · Concept 1 · [THEORY]","AI Reduces Asymmetry",
    "On Daraz and eSewa, AI fraud systems quietly flag fake reviews, scam listings, and suspicious transactions before they reach you — verifying information that a buyer could never check alone. When you search a product, AI ranks and summarises options and surfaces genuine reviews, doing the screening of S36 automatically and at scale. The result is a used-goods or payments market with far less hidden risk than a purely human one could achieve.",
    "\"AI just makes searches faster.\" It does more: by detecting fraud, verifying identity, and surfacing genuine signals, AI actively REMOVES hidden and false information — attacking asymmetry itself, not just speed. It automates signaling and screening at a scale humans cannot match.",
    "AI reduces information asymmetry by reading and verifying data at a scale no human can: it detects fraud (fake reviews, scam listings, stolen cards), verifies identity and authenticity, compares options, and surfaces the right facts to the right person — acting like a 'smart librarian' for the uninformed side. This automates the signals and screens of S36 at massive scale, so markets move closer to the efficient, low-asymmetry ideal.",
    "AI reduces asymmetry · fraud detection · verification · automated screening · smart librarian · market efficiency")

concept_understand("S38 · Concept 2 · [THEORY]","Recommendation Engines & Personalization",
    "Recommendation engines use your data (what you viewed, bought, watched) to predict what you want and show it first — Netflix, YouTube, TikTok, and Daraz all do this. Economically this raises MARKET EFFICIENCY: better buyer-seller matching, less wasted search, more relevant choices. But personalization is double-edged — it is tuned to serve BOTH your match and the platform's profit, and it quietly narrows what you're even shown (a filter bubble).",
    ["Uses your behavioural data to predict and rank what you'll want next.",
     "Efficiency gain: better matching, less search, more relevant options (a real benefit).",
     "Serves two masters: your preference AND the platform's revenue — not always aligned.",
     "Filter bubble: you see more of the same, and options the algorithm hides you never consider."],
    None,"Recommendations match you to products (efficiency) — but are tuned to platform profit and narrow your view.",
    "~7 min. Nepal angle: TikTok's feed and Daraz recommendations. Note the efficiency benefit is real, but the algorithm's goal isn't purely your benefit.")
add_examples_table("S38 · Concept 2 · examples","AI in information markets — benefit vs risk by stakeholder",
    ["Stakeholder","AI benefit","AI risk"],
    [["Consumer","Better matches, less search, fraud protection","Filter bubble, manipulation, privacy loss"],
     ["Seller / business","Reach the right buyers, dynamic pricing","Dependence on the platform's algorithm"],
     ["Platform","More engagement, data advantage","Accusations of bias / self-preferencing"],
     ["Worker","Faster job matching, upskilling tools","Algorithmic management, surveillance (S40)"],
     ["Regulator","Fraud/scam detection at scale","Opaque 'black-box' decisions to audit"],
     ["Society","More efficient markets","Concentration of data power in few firms"]],
    per_page=6,widths=[1.8,2.6,2.6],fs=10.8,
    note="AI's effects are not uniformly good or bad — they depend on WHO you are in the market. The same recommendation engine that helps a consumer match faster can trap them in a filter bubble and deepen the platform's data power.")
concept_apply("S38 · Concept 2 · [THEORY]","Recommendation Engines & Personalization",
    "TikTok's feed is a recommendation engine: every watch, replay, and skip trains it to show you more of what holds you — extremely efficient matching, and a real reason the app is addictive. Daraz does the same for products. The efficiency is genuine (you find things you like faster), but the algorithm optimises for the PLATFORM'S engagement and sales too, and it narrows your view to similar items — so you never see options it decided to hide.",
    "\"Personalized recommendations are purely for my benefit.\" They serve two masters — your match AND the platform's profit/engagement — and they create filter bubbles that hide alternatives. The efficiency gain is real, but the algorithm's objective is not identical to yours.",
    "Recommendation engines use behavioural data to predict and rank what a user wants, showing it first (Netflix, YouTube, TikTok, Daraz). Economically they raise market efficiency through better matching and less wasted search. But personalization is double-edged: it is tuned to serve both the user's preference and the platform's profit/engagement, and it creates filter bubbles that narrow what a user is shown — so the efficiency benefit comes with reduced neutrality and hidden alternatives.",
    "recommendation engine · personalization · market efficiency · matching · filter bubble · serves platform profit too")

concept_understand("S38 · Concept 3 · [THEORY]","AI's Limits & Ethics",
    "AI's power comes with real limits and ethical risks. BIAS: an AI trained on biased data reproduces and scales that bias (unfair loan or hiring decisions). PRIVACY: reducing asymmetry needs vast personal data, concentrating it in a few firms. EXPLAINABILITY: many models are 'black boxes' — even their makers can't fully explain a decision, which is a problem for fairness and appeal. So AI reduces some asymmetry while creating a new one: the platform understands you far better than you understand it.",
    ["Bias: garbage-in, bias-out — AI scales the prejudices hidden in its training data.",
     "Privacy: cutting asymmetry requires harvesting huge personal datasets (a concentration risk).",
     "Explainability / black box: decisions can't be fully explained, hurting fairness and accountability.",
     "New asymmetry: the platform knows you deeply; you can't see or question its algorithm."],
    None,"AI's risks: biased data, privacy/data concentration, black-box decisions — a new platform-vs-you asymmetry.",
    "~7 min. Close by linking back: AI shrinks the old gap but the platform-vs-user gap grows — the power question carried into S40.")
add_comparison_table("S38 · Concept 3 · comparison","AI: what it fixes vs what it breaks",
    ["Dimension","AI reduces asymmetry","AI creates new asymmetry"],
    [["Fraud / fake info","Detects and removes it","Deepfakes & AI-generated fakes"],
     ["Matching","Pairs the right two sides","Filter bubbles narrow choice"],
     ["Fairness","Consistent, tireless decisions","Scales hidden bias in the data"],
     ["Privacy","—","Harvests vast personal data"],
     ["Transparency","Summarises complex info","Black-box, unexplainable logic"],
     ["Power balance","Buyer sees more","Platform knows far more than you"]],
    per_page=6,widths=[1.9,2.5,2.6],fs=10.8,
    note="AI is not a one-way asymmetry-reducer. It closes old gaps (fraud, matching) while opening new ones (deepfakes, bias, privacy, black-box) — and it shifts power decisively toward whoever owns the model and the data.")
concept_apply("S38 · Concept 3 · [THEORY]","AI's Limits & Ethics",
    "Imagine a Nepali digital lender using AI to approve loans from phone and transaction data. It's fast and cuts the lender's asymmetry about who will repay — but if the training data under-represents rural or women applicants, the AI quietly denies them at higher rates (bias), it needs deeply personal data (privacy), and when someone is rejected, no one can fully explain why (black box). The lender now knows the borrower intimately; the borrower cannot see the algorithm at all.",
    "\"AI decisions are neutral and objective because they're mathematical.\" AI reflects its training data — biased data yields biased, scaled decisions — and many models are black boxes that can't justify a result. Neutrality is not guaranteed; AI can entrench bias while appearing objective.",
    "AI's power carries limits and ethical risks: bias (an AI trained on biased data reproduces and scales it, e.g. unfair loan/hiring decisions), privacy (reducing asymmetry needs vast personal data, concentrated in a few firms), and explainability (many models are black boxes even their makers can't fully explain, undermining fairness and appeal). So AI reduces old asymmetries while creating a new one — the platform understands the user far better than the user understands the platform.",
    "AI ethics · bias (garbage in) · privacy / data concentration · explainability · black box · platform-vs-user asymmetry")

add_activity("S38 — 'Robot shopkeeper: help or harm?'  ·  ~5 min",
    ["In pairs (2 min): pick an AI use in Nepal (Daraz recommendations, digital-lending scoring, fraud detection, TikTok feed).",
     "Name ONE way it reduces an information gap and ONE new gap/risk it creates.",
     "Say which stakeholder gains most and which is most at risk.",
     "Take 3–4 answers aloud (3 min); map benefit vs risk on the board."],
    "Good answer (digital lending): reduces lender's asymmetry about repayment; risk = biased scoring + black-box rejection + privacy; consumer most at risk, platform gains data power. Reward naming BOTH a reduced gap and a new one.",
    "ACTIVITY [~5 min].")
add_quiz("S38 — Quick Check  ·  ~5 min",
    [("Q1.  AI most directly reduces information asymmetry by:","q"),
     ("a) raising prices   b) ✅ detecting fraud & verifying information at scale   c) removing all sellers   d) banning reviews","a"),
     ("     Why: AI reads and verifies huge data, removing hidden/false information — automating signals and screens.","o"),
     ("Q2.  A key ethical risk of AI decisions is that they:","q"),
     ("a) are too slow   b) are always random   c) ✅ can scale hidden bias and be unexplainable (black box)   d) never use data","a"),
     ("     Why: biased training data yields biased decisions at scale, and black-box models can't justify results.","o"),
     ("Discussion: name one AI tool in Nepal that both helps consumers and creates a new risk.","o")],
    "QUIZ [~5 min]. Balance AI's asymmetry-reducing power with its bias/privacy/black-box risks.")
add_summary("S38 · Summary  ·  [~2 min]",
    ["AI reduces asymmetry by detecting fraud and verifying information at scale — automating signaling & screening.",
     "Recommendation engines raise market efficiency (better matching) but serve platform profit too and create filter bubbles.",
     "AI's limits & ethics: it scales hidden bias, needs vast private data, and is often a black box — a new platform-vs-user asymmetry."],
    "AI already decides what you see, buy, and sometimes whether you get a loan in Nepal. Understanding that it both closes old information gaps and opens new, opaque ones lets you use it critically instead of trusting it blindly.",
    "S39 — from problem to playbook: turning abundant information into strategy (the Shapiro–Varian toolkit).",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S39
add_divider("Session 39 · Lecture hour 6 (of 8)","Strategy & the New Economics of Information",
    "When information was scarce and expensive, you got rich by OWNING it. Now information is abundant and near-free to "
    "copy — so how does anyone make money from it? The answer is a strategy toolkit economists Carl Shapiro and Hal "
    "Varian mapped out: version it, price it differently for different buyers, bundle it, and lock customers in. This is how 'free' information becomes a fortune.",
    "OPENING HOOK [~5 min]. Ask: if info is near-free to copy, how do Netflix/Adobe make billions? Agenda: the scarce->abundant shift -> versioning, price discrimination & bundling -> lock-in, network effects & AI pricing (link Unit 2).")

concept_understand("S39 · Concept 1 · [THEORY]","The Shift: Information Scarce → Abundant",
    "The 'new economics of information' begins with a shift: information used to be SCARCE and costly, so value came from having it; now it is ABUNDANT and near-free to copy, so scarcity of copies no longer creates value. Strategy therefore moves from selling copies to controlling ACCESS, ATTENTION, and CONVENIENCE. Because the first copy costs a fortune and every next copy costs ~nothing (S34), the winning play is to sell the same information many different ways.",
    ["Old world: information scarce & costly -> value from possessing/withholding it.",
     "New world: information abundant & ~free to copy -> value from access, attention, curation, convenience.",
     "Cost structure (S34): huge first-copy cost, ~zero marginal copy cost -> price by value, not cost.",
     "Winning idea: monetise the SAME information repeatedly through clever packaging and pricing."],
    None,"Info went scarce->abundant: value now comes from access & attention, so sell the same info many ways.",
    "~7 min. Anchor on S34's cost structure (first copy dear, next copy free). This reframes 'free info' as a strategy problem, not a dead end.")
add_comparison_table("S39 · Concept 1 · comparison","Old vs new economics of information",
    ["Question","Old economics","New economics of information"],
    [["Information is…","Scarce & costly","Abundant & near-free to copy"],
     ["Value comes from…","Owning/withholding info","Access, attention, curation, convenience"],
     ["Price is based on…","Cost of the copy","Value to the buyer (not cost)"],
     ["How you profit","Sell each copy","Sell the SAME info many ways"],
     ["Main scarce resource","The information itself","The customer's attention & trust"],
     ["Example","Buying a physical newspaper","Netflix tiers; freemium apps; ad-funded feeds"]],
    per_page=6,widths=[1.9,2.4,2.7],fs=11,
    note="The core reframe: when copies are free, you can't charge for the copy — you charge for VALUE, access, and attention. Every strategy tool below is a way to capture value from information that costs ~nothing to reproduce.")
concept_apply("S39 · Concept 1 · [THEORY]","The Scarce → Abundant Shift",
    "A Nepali news portal can't sell articles the way a printed paper sold physical copies — anyone can copy or forward the text for free. So value shifts: it monetises ATTENTION (ads), ACCESS (subscriptions/paywalls for premium analysis), and CONVENIENCE (a clean app, curated newsletters). The information is abundant; what's scarce is the reader's attention and trust. That reframing — sell access and attention, not copies — is the whole 'new economics of information'.",
    "\"If information is free to copy, you can't make money from it.\" You can't make money from the COPY — but you can from access, attention, curation, and convenience. Netflix, Spotify, and news paywalls all sell abundant information profitably by charging for value and packaging, not for the bytes.",
    "The new economics of information starts from a shift: information used to be scarce and costly (value came from possessing it), but is now abundant and near-free to copy (scarcity of copies no longer creates value). Strategy therefore moves to controlling access, attention, curation, and convenience, and to pricing by value rather than cost. Given the huge first-copy and ~zero marginal-copy cost structure, the winning play is to monetise the same information many different ways.",
    "new economics of information · scarce->abundant · value from access/attention · price by value not cost")

concept_understand("S39 · Concept 2 · [THEORY]","Versioning, Price Discrimination & Bundling",
    "Three core Shapiro–Varian tools monetise the same information repeatedly. VERSIONING: sell the same product in different versions (free/premium, standard/pro, SD/HD) so buyers self-select by willingness to pay. PRICE DISCRIMINATION: charge different prices to different buyers (student discounts, regional pricing, personalised prices). BUNDLING: sell many items together for one price (a software suite, a streaming catalogue), which extracts more total value than selling each alone.",
    ["Versioning: one product, many tiers (free vs premium) -> buyers self-select (a screening move, S36).",
     "Price discrimination: different prices for different buyers/segments (student, regional, personalised).",
     "Bundling: package many goods for one price -> captures more value than à-la-carte.",
     "All three exploit ~zero copy cost: extra versions/bundles cost almost nothing to offer."],
    None,"Versioning (tiers) · price discrimination (different prices) · bundling (package many) — sell the same info many ways.",
    "~8 min. Note versioning is screening (S36) applied to pricing: the free tier screens out low-value users while capturing high-value ones on premium.")
add_examples_table("S39 · Concept 2 · examples","The strategy toolkit — how each monetises information",
    ["Tool","How it monetises info","Example"],
    [["Versioning","Tiers let buyers self-select by value","Free vs premium app; SD vs HD stream"],
     ["Price discrimination","Different price per buyer/segment","Student/regional pricing; personalised prices"],
     ["Bundling","One price for many items","MS Office suite; Netflix catalogue"],
     ["Freemium","Free hooks users; few pay for extras","Free app + paid pro features"],
     ["Lock-in / switching cost","Keep customers so they keep paying","Ecosystem & data lock-in (Unit 2 S12)"],
     ["Dynamic (AI) pricing","Price adjusts to demand/person","Ride surge; airline & hotel pricing"]],
    per_page=6,widths=[2.0,2.6,2.4],fs=10.8,
    note="Every tool exploits information's ~zero copy cost (S34): offering one more version, bundle, or personalised price costs almost nothing, so each captures extra value the single 'one price for the copy' model would leave on the table.")
concept_apply("S39 · Concept 2 · [THEORY]","Versioning, Price Discrimination & Bundling",
    "A Nepali online-course platform uses all three: VERSIONING (free intro lessons vs a paid full course vs a premium mentorship tier), PRICE DISCRIMINATION (a student discount, lower regional pricing for Nepal than the US), and BUNDLING (buy all courses in one 'career pack' for less than the sum). Each costs almost nothing extra to offer because the content is already made — so the same information is sold many ways to capture the most value from each buyer.",
    "\"Charging different people different prices for the same thing is just unfair.\" It's PRICE DISCRIMINATION — a core information strategy that can expand access (students and lower-income regions pay less) while capturing more value from those who'll pay more. It exploits the ~zero copy cost of information; whether it's 'unfair' depends on how it's used.",
    "Three core Shapiro–Varian tools monetise the same information repeatedly: versioning (sell the product in tiers — free/premium, SD/HD — so buyers self-select by willingness to pay), price discrimination (charge different prices to different buyers or segments — student, regional, personalised), and bundling (sell many items together for one price, extracting more total value than à-la-carte). All exploit information's near-zero copy cost, since extra versions, bundles, and price points cost almost nothing to offer.",
    "versioning · price discrimination · bundling · freemium · self-selection · exploits ~zero copy cost")

concept_understand("S39 · Concept 3 · [THEORY]","Lock-In, Network Effects & AI Pricing",
    "The last tools defend and extend information profits. LOCK-IN & switching costs (Unit 2 S12) keep customers paying — proprietary formats, ecosystems, and data that won't move. NETWORK EFFECTS (Unit 2 S10) make an information product more valuable as more use it, tipping the market to one winner. And AI-driven DYNAMIC PRICING uses data to set a different price for each buyer or moment (surge, personalised prices) — price discrimination automated in real time.",
    ["Lock-in / switching costs (S12): formats, ecosystems, data keep customers from leaving.",
     "Network effects (S10): information products get more valuable and more dominant as usage grows.",
     "AI dynamic pricing: real-time, per-person pricing — automated price discrimination.",
     "Together with versioning/bundling, these turn abundant information into durable profit."],
    None,"Lock-in keeps them, network effects grow dominance, AI dynamic pricing personalises price — info profit defended.",
    "~7 min. Explicit spaced callback to Unit 2 (S10 network effects, S12 lock-in). Dynamic pricing = the price-discrimination tool automated by the AI of S38.")
add_table_slide("S39 · Concept 3 · scaffolding","Versioning worked — one product, many prices (a Nepali streaming service)",
    ["Version / tactic","What the buyer gets","Who it captures"],
    [["Free (ad-supported)","Basic access, with ads","Price-sensitive mass users"],
     ["Standard subscription","Ad-free, SD/one screen","Everyday paying users"],
     ["Premium subscription","HD/4K, multiple screens","High-value households"],
     ["Student / regional price","Discounted access","Students & lower-income segments"],
     ["Annual bundle","12 months for the price of 10","Committed, locked-in users"],
     ["Family / group plan","Shared at a lower per-head price","Groups — raises switching cost"]],
    per_page=6,widths=[2.0,2.5,2.5],fs=10.8,
    note="The same catalogue (near-zero extra copy cost) is sold six ways to capture value from every segment — versioning + price discrimination + bundling + lock-in working together. This is the new economics of information in one table.")
concept_apply("S39 · Concept 3 · [THEORY]","Lock-In, Network Effects & AI Pricing",
    "Adobe shows the full playbook: it VERSIONS (Photoshop vs the full Creative Cloud), BUNDLES (all apps in one suite), locks users in with proprietary file formats and a subscription (Unit 2 S12), and benefits from NETWORK EFFECTS as the industry standard everyone must learn. Pathao's surge is AI DYNAMIC PRICING — the price-discrimination tool of S38 automated in real time. Abundant information becomes durable profit through packaging, lock-in, and data-driven pricing.",
    "\"Once information is free to copy, no one can build a durable business on it.\" Firms build moats with lock-in (switching costs), network effects (dominance grows with users), and AI dynamic pricing — turning abundant, copyable information into a defensible, high-profit business. Free-to-copy does not mean free-to-compete-with.",
    "The new economics of information defends and extends profits with three more tools: lock-in and switching costs (Unit 2 S12 — proprietary formats, ecosystems, non-portable data keep customers paying), network effects (Unit 2 S10 — an information product grows more valuable and dominant as usage rises, tipping markets), and AI-driven dynamic pricing (real-time, per-person prices — automated price discrimination). Together with versioning and bundling, they turn abundant, copyable information into durable profit.",
    "lock-in/switching cost (S12) · network effects (S10) · dynamic pricing · automated price discrimination · durable moat")

add_activity("S39 — 'Monetise the same information'  ·  ~5 min",
    ["In pairs (3 min): you run a Nepali information product (a course platform, a news app, a music/streaming service).",
     "Design at least THREE ways to sell the SAME content: a versioning tier, a price-discrimination move, and a bundle.",
     "Name one lock-in or network-effect play to keep customers.",
     "Take 3–4 answers aloud (2 min); check each tool is correctly named."],
    "Good answer (course platform): versioning = free intro / paid course / premium mentorship; price discrimination = student + regional pricing; bundle = 'career pack'; lock-in = certificates + saved progress. Reward correctly naming versioning vs price discrimination vs bundling.",
    "ACTIVITY [~5 min].")
add_quiz("S39 — Quick Check  ·  ~5 min",
    [("Q1.  Selling a free tier and a paid premium tier of the same app is:","q"),
     ("a) bundling   b) ✅ versioning (buyers self-select by value)   c) lock-in   d) a network effect","a"),
     ("     Why: one product offered in tiers lets buyers self-select by willingness to pay — versioning.","o"),
     ("Q2.  The 'new economics of information' says value now comes mainly from:","q"),
     ("a) owning scarce copies   b) the cost of each copy   c) ✅ access, attention & convenience   d) physical stock","a"),
     ("     Why: information is abundant and ~free to copy, so value shifts to access, attention, and curation.","o"),
     ("Discussion: pick a service you use and name its versioning, bundling, and lock-in moves.","o")],
    "QUIZ [~5 min]. Distinguish versioning vs price discrimination vs bundling, and the scarce->abundant reframe.")
add_summary("S39 · Summary  ·  [~2 min]",
    ["Information went scarce->abundant, so value now comes from access, attention & convenience — price by value, not copy cost.",
     "Core toolkit: versioning (tiers), price discrimination (different prices), bundling (package many) — sell the same info many ways.",
     "Defend profits with lock-in & switching costs (S12), network effects (S10), and AI dynamic pricing (automated price discrimination)."],
    "This is the playbook behind every subscription, freemium app, and streaming tier you pay for — and the strategy you'd use to build an information business in Nepal. It turns 'information is free' from a problem into a business model.",
    "S40 — the human side: how digitalization reshapes consumer choice and the jobs people do.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S40
add_divider("Session 40 · Lecture hour 7 (of 8)","Digitalization: Consumer Choice & Labor Markets",
    "Digitalization hands you infinite choice and instant reviews — yet you feel MORE overwhelmed, not less. And it "
    "creates whole new jobs (Pathao rider, content creator) while quietly erasing others (bank teller, travel agent). "
    "Who really controls your choices now — you or the algorithm? And which Nepali jobs are growing, which are vanishing, and why?",
    "OPENING HOOK [~5 min]. Ask: does more choice online make deciding easier or harder? Agenda: consumer choice (overload, e-WOM) -> labor displacement/creation & polarization -> the gig economy & algorithmic management.")

concept_understand("S40 · Concept 1 · [THEORY]","Consumer Choice: Overload, Bounded Rationality & e-WOM",
    "Digitalization slashes search cost (S37) and floods buyers with options and reviews. But more choice is not always better: INFORMATION OVERLOAD makes deciding harder and more stressful; BOUNDED RATIONALITY means people can't process it all, so they use shortcuts (top result, most reviews, cheapest); and e-WOM (electronic word of mouth — reviews, ratings, influencers) heavily shapes decisions. Choice expands, but real control over the decision often shifts to whoever curates the options.",
    ["Lower search cost (S37) -> vastly more options and reviews available.",
     "Information overload: too many options -> stress, delay, worse or avoided decisions.",
     "Bounded rationality: limited attention -> reliance on shortcuts (ratings, top result, brand).",
     "e-WOM: online reviews, ratings, and influencers strongly steer what people buy."],
    None,"More choice + limited attention -> overload; buyers lean on shortcuts & reviews (e-WOM) that others curate.",
    "~7 min. Nepal angle: buying on Daraz, choosing a restaurant on Foodmandu by rating. Link overload back to bounded rationality (a real term).")
add_examples_table("S40 · Concept 1 · examples","Consumer choice: before vs after digital",
    ["Aspect","Before digital","After digital"],
    [["Number of options","Few, local","Vast, global"],
     ["Search cost","High","Near zero (S37)"],
     ["Main decision aid","Shopkeeper's word","Reviews & ratings (e-WOM)"],
     ["Typical problem","Too little information","Information overload"],
     ["How people cope","Trust local seller","Shortcuts: top result, most-rated, cheapest"],
     ["Who shapes the choice","The buyer & local shop","The algorithm & reviews that curate options"]],
    per_page=6,widths=[2.0,2.3,2.7],fs=10.8,
    note="Digital fixes the old problem (too little information) but creates a new one (overload). Because buyers can't process everything (bounded rationality), power shifts to whoever curates and ranks the options — the platform.")
concept_apply("S40 · Concept 1 · [THEORY]","Consumer Choice & Overload",
    "Ordering dinner on Foodmandu, you face hundreds of restaurants — far more choice than the old 'call the one place you know'. But you can't evaluate them all (bounded rationality), so you sort by rating and pick from the top few, trusting others' reviews (e-WOM). The choice is technically yours, but the app's ranking and the review scores did most of the deciding. More options, less felt control — the paradox of digital choice.",
    "\"More choice always makes consumers better off.\" Beyond a point, more options cause information overload and worse or avoided decisions; limited attention (bounded rationality) forces shortcuts, and reviews/algorithms — not the buyer — end up curating the real choice. More choice can mean less genuine control.",
    "Digitalization slashes search cost and floods buyers with options and reviews, but more choice is not always better: information overload makes decisions harder and more stressful; bounded rationality means people cannot process everything, so they rely on shortcuts (top result, most reviews, cheapest); and e-WOM (online reviews, ratings, influencers) strongly shapes decisions. Choice expands, but real control over the decision often shifts to whoever curates and ranks the options — the platform.",
    "information overload · bounded rationality · e-WOM · decision shortcuts · curated choice · control shifts to platform")

concept_understand("S40 · Concept 2 · [THEORY]","Labor Markets: Displacement, Creation & Polarization",
    "Digitalization both DESTROYS and CREATES jobs, but unevenly. It automates ROUTINE tasks, displacing middle-skill jobs (clerks, tellers, data entry), while creating new high-skill roles (data, design, engineering) and new low-skill service roles (delivery riders). The result is POLARIZATION: the middle of the job market hollows out while the top and bottom grow. An OECD-style estimate is that roughly 40% of routine tasks are automatable — the squeeze falls hardest on the middle.",
    ["Displacement: automation replaces routine, rules-based middle-skill jobs first.",
     "Creation: new roles appear at the high-skill end (tech, analytics) and low-skill service end (gig delivery).",
     "Polarization: the MIDDLE shrinks while top and bottom grow — the workforce splits in two.",
     "Reported OECD-style figure: ~40% of routine tasks are at risk of automation."],
    "s40_polarization.png","Automation hits ROUTINE middle-skill jobs hardest -> the job market polarizes (middle hollows out).",
    "~7 min. Use the polarization diagram. Stress it's not 'robots take all jobs' — it's the MIDDLE specifically. Cite the ~40% figure as a reported estimate.")
add_examples_table("S40 · Concept 2 · examples","Jobs displaced vs created by digitalization (Nepal)",
    ["Job displaced / shrinking","Why","New / growing job"],
    [["Bank teller","ATMs, eSewa/Khalti, mobile banking","Fintech developer, data analyst"],
     ["Travel agent","Online booking & comparison","Digital marketer, UX designer"],
     ["Data-entry clerk","Automation & digitised forms","Cloud/IT support, automation specialist"],
     ["Print-media journalist","Free online news","Content creator, social-media manager"],
     ["Video/DVD shop","Streaming (Netflix, YouTube)","Streaming creator, video editor"],
     ["Traditional retail cashier","E-commerce (Daraz), QR payments","Delivery rider (Pathao/Foodmandu), seller"]],
    per_page=6,widths=[2.2,2.3,2.5],fs=10.5,
    note="The pattern is polarization: routine MIDDLE-skill jobs (teller, clerk, agent) shrink fastest, while high-skill (developer, analyst) and low-skill service (rider) roles grow. Reskilling toward non-routine skills is the individual's defence.")
concept_apply("S40 · Concept 2 · [THEORY]","Labor Polarization",
    "In Nepal you can watch polarization happen: bank tellers and travel agents are fading as eSewa, mobile banking, and online booking spread (routine middle-skill work automated), while two ends grow — high-skill fintech developers and data analysts at the top, and Pathao/Foodmandu delivery riders at the bottom. The middle-skill clerical jobs that once absorbed graduates are shrinking fastest, which is why reskilling toward non-routine, digital, or creative skills matters so much.",
    "\"Digitalization simply destroys jobs.\" It destroys AND creates them — but unevenly: routine middle-skill jobs shrink while high-skill and low-skill service jobs grow. The real story is POLARIZATION (the middle hollows out), not net destruction, so the policy answer is reskilling toward non-routine work, not just resisting technology.",
    "Digitalization both destroys and creates jobs, but unevenly: it automates routine tasks, displacing middle-skill jobs (clerks, tellers, agents), while creating new high-skill roles (data, engineering, design) and new low-skill service roles (delivery riders). The result is polarization — the middle of the job market hollows out while the top and bottom grow. A reported OECD-style estimate is that roughly 40% of routine tasks are automatable, so the squeeze falls hardest on the middle, making reskilling the key defence.",
    "job displacement · job creation · polarization · middle-skill hollowing · ~40% routine at risk · reskilling")

concept_understand("S40 · Concept 3 · [THEORY]","The Gig Economy & Algorithmic Management",
    "The gig economy is short-term, task-based work mediated by platforms (Pathao/Foodmandu riders, freelancers). It offers FLEXIBILITY and low entry barriers, but shifts risk to the worker: no fixed salary, no benefits, income tied to demand. And workers are directed by ALGORITHMIC MANAGEMENT — an app assigns tasks, sets pay, tracks performance, and can 'deactivate' a worker, with no human manager to appeal to. It is the labor-market version of the platform-vs-user asymmetry (S38).",
    ["Gig work: task-based, flexible, low entry barrier — but insecure (no salary/benefits, risk on the worker).",
     "Algorithmic management: the app assigns work, sets pay, rates, and can deactivate — the 'boss is an algorithm'.",
     "Power asymmetry: the platform sees all the data; the worker can't see or appeal the algorithm.",
     "Policy questions: worker classification, minimum protections, transparency of the algorithm."],
    None,"Gig work = flexible but insecure; the 'boss' is an algorithm that assigns, pays, rates & can deactivate you.",
    "~7 min. Nepal angle: Pathao/Foodmandu riders. Tie the algorithm-as-boss back to S38's black-box asymmetry — the worker faces the same opaque power.")
add_examples_table("S40 · Concept 3 · examples","Gig work: benefit vs cost (Nepal riders & freelancers)",
    ["Dimension","Benefit to the worker","Cost / risk to the worker"],
    [["Flexibility","Choose your own hours","No guaranteed income"],
     ["Entry barrier","Easy to start (a bike, a phone)","Easily replaced; little bargaining power"],
     ["Pay","Earn per task; can top up income","Pay set by the algorithm; can be cut"],
     ["Management","No fixed boss","Algorithmic control; unfair deactivation"],
     ["Benefits","—","No pension, insurance, or leave"],
     ["Data","App handles matching","Platform holds all data; no transparency"]],
    per_page=6,widths=[1.8,2.5,2.7],fs=10.5,
    note="Gig work genuinely opens income to many Nepalis, but transfers risk from firm to worker and puts an unaccountable algorithm in the manager's chair — the core of the 'who controls?' debate that closes this unit.")
concept_apply("S40 · Concept 3 · [THEORY]","The Gig Economy & Algorithmic Management",
    "A Pathao/Foodmandu rider in Kathmandu enjoys real flexibility — work when you want, start with just a bike — and it's a genuine income for many. But the app is the boss: it assigns rides, sets the fare, rates the rider, and can deactivate the account, all by algorithm with no manager to appeal to. Income swings with demand, there are no benefits, and the platform holds all the data. Flexibility is real; so is the insecurity and the opaque algorithmic power.",
    "\"Gig work is just flexible freelancing — everyone wins.\" It offers flexibility but shifts risk to the worker (no salary, benefits, or security) and replaces the human boss with an opaque algorithm that assigns, pays, rates, and can deactivate. The flexibility is real, but so is the power imbalance — which is why worker protections are debated.",
    "The gig economy is short-term, task-based work mediated by platforms (Pathao/Foodmandu riders, online freelancers). It offers flexibility and low entry barriers but shifts risk to the worker (no fixed salary, benefits, or security, income tied to demand), and workers are directed by algorithmic management — an app assigns tasks, sets pay, tracks performance, and can deactivate them, with no human to appeal to. It mirrors the platform-vs-user asymmetry of S38, raising questions of classification, protection, and algorithmic transparency.",
    "gig economy · task-based/flexible · risk shifted to worker · algorithmic management · deactivation · worker protection")

add_activity("S40 — 'Who controls the choice?'  ·  ~5 min",
    ["In pairs (3 min): pick a Nepali platform (Foodmandu, Daraz, Pathao).",
     "As a CONSUMER: name one way the algorithm shapes your choice more than you do.",
     "As a WORKER (if gig): name one way the algorithm manages you and one risk you carry.",
     "Take 3–4 answers aloud (2 min); debate: consumer/worker vs platform — who controls?"],
    "Good answer (Foodmandu): consumer choice is steered by ranking + ratings (e-WOM) not free choice; rider is assigned/paid/rated by the app and risks deactivation with no benefits. Reward naming a SPECIFIC control the algorithm holds.",
    "ACTIVITY [~5 min].")
add_quiz("S40 — Quick Check  ·  ~5 min",
    [("Q1.  Digitalization's effect on the job market is best described as:","q"),
     ("a) it only destroys jobs   b) it only creates jobs   c) ✅ polarization — the middle shrinks while top & bottom grow   d) no effect","a"),
     ("     Why: routine middle-skill jobs are automated while high-skill and low-skill service jobs grow — polarization.","o"),
     ("Q2.  A Pathao rider being assigned, paid, rated and deactivated by the app is:","q"),
     ("a) signaling   b) ✅ algorithmic management   c) bundling   d) price dispersion","a"),
     ("     Why: an algorithm performs the manager's role — the defining feature of gig-economy work.","o"),
     ("Discussion: name one Nepali job that shrank and one that emerged with digitalization, and why.","o")],
    "QUIZ [~5 min]. Cement polarization (middle hollows out) and algorithmic management, and the 'who controls' theme.")
add_summary("S40 · Summary  ·  [~2 min]",
    ["Consumer choice: digital cuts search cost but causes information overload; bounded rationality forces shortcuts, so reviews & algorithms curate the real choice.",
     "Labor: digitalization destroys AND creates jobs unevenly -> polarization (middle-skill hollows out; ~40% routine at risk); reskilling is the defence.",
     "Gig economy: flexible but insecure, run by algorithmic management — the 'boss' is an app that assigns, pays, rates & can deactivate you."],
    "This is your own economy: as a consumer your choices are being curated, and as a future worker the jobs — and the way you'll be managed — are changing under you. Seeing polarization and algorithmic power helps you choose skills and protect your interests.",
    "S41 — closing the unit: intellectual property and how digitalization challenges it.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S41
add_divider("Session 41 · Lecture hour 8 (of 8) — CLOSES UNIT 5","Intellectual Property & Digitalization",
    "A Nepali musician spends a year making an album; within a day of release it's copied and shared for free across the "
    "internet. Information is near-free to copy (S34) — which is wonderful for spreading ideas and ruinous for the people "
    "who create them. Intellectual property is society's attempt to solve that tension. How does it work, and how does digitalization break and remake it?",
    "OPENING HOOK [~5 min]. Use the pirated-album story. Agenda: IP & the four types (why IP exists) -> digital's double edge (reach vs piracy) + enforcement -> the AI-ownership problem & Nepal's IP challenge.")

concept_understand("S41 · Concept 1 · [THEORY]","Intellectual Property & Its Four Types",
    "Intellectual property (IP) is the legal ownership of creations of the mind, giving creators a temporary exclusive right so they can profit and are motivated to keep creating. IP exists to solve information's copy problem: without protection, anyone could copy a work for free (S34) and no one would invest in creating it. There are four main types: COPYRIGHT (creative works), PATENT (inventions), TRADEMARK (brand identity), and TRADE SECRET (confidential know-how).",
    ["Why IP exists: information is near-free to copy, so creators need protection to have a reason to create.",
     "Copyright: protects creative expression — songs, films, books, software (life + ~50 years).",
     "Patent: protects inventions — a new process or device (~20 years, then public).",
     "Trademark: protects brand identity — name, logo, mark (renewable indefinitely). Trade secret: protects secret know-how while it stays secret."],
    "s41_ip_types.png","IP = temporary exclusive rights so creators profit. Four types: copyright, patent, trademark, trade secret.",
    "~8 min. Use the four-IP-types diagram. Trade secret is the fresh one the old lectures omitted — contrast it with patent (disclose to protect vs hide to protect).")
add_comparison_table("S41 · Concept 1 · comparison","The four types of intellectual property",
    ["Type","Protects","Duration","Nepal / example"],
    [["Copyright","Creative works (songs, films, code, books)","Life + ~50 years","Nepali music, films, software"],
     ["Patent","Inventions (new process/device)","~20 years, then public","A new machine or drug formula"],
     ["Trademark","Brand identity (name, logo, mark)","Renewable indefinitely","Wai Wai; eSewa name & logo"],
     ["Trade secret","Confidential know-how (recipe, algorithm)","As long as it stays secret","A recipe; a ranking algorithm"]],
    per_page=4,widths=[1.6,2.8,1.9,2.3],fs=11,
    note="Key contrast: a PATENT protects by DISCLOSING the invention (public after ~20 years); a TRADE SECRET protects by HIDING it (protected only while secret). Copyright is automatic on creation; trademark and patent need registration.")
concept_apply("S41 · Concept 1 · [THEORY]","Intellectual Property & Its Four Types",
    "A Nepali startup touches all four: its APP CODE and marketing videos are copyright, a genuinely novel invention could be patented, its NAME and LOGO (like 'eSewa') are trademarks, and its secret recommendation/ranking formula is a trade secret it protects by never disclosing. Each type fits a different creation and a different strategy — disclose-to-protect (patent) versus hide-to-protect (trade secret) — and together they let the firm profit from information that is otherwise free to copy.",
    "\"Copyright, patent, and trademark are basically the same thing.\" They protect different things for different terms: copyright = creative expression (automatic, life+50); patent = inventions (registered, ~20 yrs, disclosed); trademark = brand identity (registered, renewable forever); trade secret = secret know-how (protected only while hidden). Using the wrong one leaves a creation unprotected.",
    "Intellectual property (IP) is the legal ownership of creations of the mind, granting creators temporary exclusive rights so they can profit and stay motivated to create — a solution to information's near-free copyability. The four main types are copyright (creative works; life + ~50 years), patent (inventions; ~20 years then public), trademark (brand identity; renewable indefinitely), and trade secret (confidential know-how; protected only while secret). Patents protect by disclosing; trade secrets protect by hiding.",
    "intellectual property · copyright · patent · trademark · trade secret · exclusive right · disclose vs hide to protect")

concept_understand("S41 · Concept 2 · [THEORY]","Digitalization's Double Edge & Enforcement",
    "Digitalization is a double edge for IP. The good edge: near-zero copy and distribution cost lets creators REACH the whole world instantly and cheaply (a Nepali artist can be heard globally). The bad edge: the same ease makes PIRACY trivial — perfect copies spread for free, gutting creators' income. Platforms respond with enforcement technology such as YouTube's CONTENT ID (which scans uploads and matches them to copyrighted works) and takedown systems, plus licensing deals that pay rights-holders.",
    ["Good edge: global reach at ~zero distribution cost — huge opportunity for creators.",
     "Bad edge: piracy is trivial — perfect free copies destroy the incentive to create (the S34 copy problem).",
     "Platform enforcement: Content ID matches uploads to copyrighted works; automated takedowns.",
     "Licensing turns the problem into revenue: platforms pay rights-holders for legal use (streaming royalties)."],
    None,"Digital = global reach (good) + trivial piracy (bad); platforms fight back with Content ID, takedowns & licensing.",
    "~7 min. Nepal angle: Nepali content creators pirated on YouTube/Facebook, and Content ID as the automated enforcement tool. Note enforcement is imperfect.")
add_examples_table("S41 · Concept 2 · examples","Digitalization for IP — the good vs the bad",
    ["Aspect","Digital is GOOD for IP","Digital is BAD for IP"],
    [["Reach","Global audience, instantly","Global piracy, instantly"],
     ["Cost","~Zero distribution cost","~Zero copying cost (for pirates too)"],
     ["Revenue","New models: streaming, licensing","Lost sales to free copies"],
     ["Enforcement","Content ID, automated takedowns","Copies reappear faster than removal"],
     ["Creators","Direct-to-fan, no gatekeeper","Income undercut by piracy"],
     ["Nepal example","Nepali artist heard worldwide","Songs/films re-uploaded & pirated free"]],
    per_page=6,widths=[1.8,2.5,2.7],fs=10.8,
    note="The same property of information — near-free copying (S34) — is simultaneously the creator's biggest opportunity (reach) and biggest threat (piracy). IP law and enforcement tech try to keep the opportunity while limiting the threat.")
concept_apply("S41 · Concept 2 · [THEORY]","Digitalization's Double Edge",
    "A Nepali YouTuber lives both edges: digital distribution lets them reach a global Nepali diaspora at almost no cost (the good edge), and monetise via ads and licensing. But their videos get re-uploaded on other channels and Facebook pages within hours, siphoning off views and income (the bad edge). YouTube's Content ID can automatically detect and claim or take down some copies — imperfectly — while licensing/royalty systems turn legitimate plays into revenue.",
    "\"Digital distribution is purely good for creators — they reach everyone.\" Reach is the good edge, but the identical ease of copying makes piracy trivial and can gut a creator's income. Digital is a double edge; whether a creator thrives depends on enforcement (Content ID) and business models (licensing) that capture the reach while limiting the piracy.",
    "Digitalization is a double edge for IP. The good edge: near-zero copy and distribution cost lets creators reach the whole world instantly and cheaply (a Nepali artist heard globally, new streaming/licensing revenue). The bad edge: the same ease makes piracy trivial — perfect free copies spread instantly and gut creators' income. Platforms respond with enforcement technology (YouTube Content ID matching uploads to copyrighted works, automated takedowns) and licensing deals that pay rights-holders, though enforcement remains imperfect.",
    "double edge · global reach · piracy · Content ID · automated takedown · licensing/royalties · enforcement imperfect")

concept_understand("S41 · Concept 3 · [THEORY]","The AI-Ownership Problem & Nepal's IP Challenge",
    "AI raises a brand-new IP question: WHO OWNS AI-generated work — the user who prompted it, the company that built the model, or no one? And was it legal for the AI to TRAIN on copyrighted works without permission? The law has no settled answer yet. Meanwhile Nepal faces a specific challenge: low IP awareness, high piracy, and weak enforcement, so creators struggle to profit. The balance IP must strike is protecting creators enough to motivate them without locking knowledge away from society.",
    ["AI-ownership problem: unclear who owns AI output (user? model-maker? no one?) — law is unsettled.",
     "Training-data question: is it fair use to train AI on copyrighted works without consent?",
     "Nepal's challenge: low IP awareness + high piracy + weak enforcement -> creators underpaid.",
     "The balance: enough protection to motivate creators, enough openness (fair use, licensing) to spread knowledge."],
    None,"AI ownership is legally unsettled; Nepal's challenge is low awareness + high piracy; IP must balance creators vs society.",
    "~7 min. This is the fresh close. Mention fair use / Creative Commons / open-source as the 'openness' side of the balance. Tie to IT 246's IP unit as a callback.")
add_examples_table("S41 · Concept 3 · examples","Piracy vs fair use vs licensing",
    ["Use of a work","Legal?","Why / example"],
    [["Downloading a pirated film","No — piracy","Copying without permission or payment"],
     ["Quoting a line for a review/class","Yes — fair use","Limited, transformative, non-commercial"],
     ["Paying to stream on a licensed app","Yes — licensing","Rights-holder is paid a royalty"],
     ["Using a Creative Commons image (credited)","Yes — open licence","Creator granted permission in advance"],
     ["Using open-source code per its licence","Yes — open-source licence","Allowed if licence terms are followed"],
     ["Re-uploading a Nepali song as your own","No — infringement","Copying + falsely claiming authorship"]],
    per_page=6,widths=[2.4,1.4,3.0],fs=10.8,
    note="Not all copying is illegal: fair use (limited, transformative), licensing (paid permission), and open licences (Creative Commons, open-source) are legal paths. Piracy is unauthorised copying — the line is permission and purpose, not the act of copying itself.")
concept_apply("S41 · Concept 3 · [THEORY]","The AI-Ownership Problem & Nepal's Challenge",
    "If a Nepali designer uses an AI tool to generate a logo, who owns it — the designer, the AI company, or no one (so anyone can copy it)? The law has no clear answer, and it's unclear whether the AI legally trained on others' copyrighted art. Layered on Nepal's low IP awareness, rampant piracy, and weak enforcement, creators are doubly exposed. The way forward balances protection (so creators earn) with openness (fair use, licensing, Creative Commons) so knowledge still spreads.",
    "\"Whatever an AI generates is automatically mine to own and copyright.\" Ownership of AI output is legally unsettled — it may belong to the user, the model-maker, or (in some jurisdictions) no one, since many laws require a human author. And the AI's training on copyrighted data raises its own unresolved fair-use question. Don't assume automatic ownership.",
    "AI raises a new IP question with no settled legal answer: who owns AI-generated work (the user, the model-maker, or no one?), and was it lawful for the AI to train on copyrighted works without permission? Meanwhile Nepal faces low IP awareness, high piracy, and weak enforcement, so creators struggle to profit. IP must strike a balance — enough protection to motivate creators, enough openness (fair use, licensing, Creative Commons, open-source) to keep knowledge flowing to society.",
    "AI-ownership problem · training-data/fair-use question · Nepal: low awareness/high piracy · fair use · licensing · the balance")

add_activity("S41 — 'Protect the creation'  ·  ~5 min",
    ["In pairs (2 min): a Nepali team builds an app with a name, a logo, original music, and a secret ranking formula.",
     "Match each element to the right IP type (copyright / patent / trademark / trade secret).",
     "Name one way digitalization threatens it and one defence (Content ID, licensing, registration).",
     "Take 3–4 answers aloud (3 min); confirm each match is correct."],
    "Answers: code + music = copyright; name + logo = trademark; novel invention = patent; secret ranking formula = trade secret. Threat = piracy/copying; defence = registration, Content ID, licensing. Reward correct type-matching and a real defence.",
    "ACTIVITY [~5 min].")
add_quiz("S41 — Quick Check  ·  ~5 min",
    [("Q1.  A brand's name and logo are protected by:","q"),
     ("a) copyright   b) patent   c) ✅ trademark   d) trade secret","a"),
     ("     Why: trademark protects brand identity (name, logo, mark); copyright covers creative works, patents inventions.","o"),
     ("Q2.  Which is NOT illegal piracy?","q"),
     ("a) downloading a pirated film   b) re-uploading a song as your own   c) ✅ quoting a line for a class review (fair use)   d) selling copied software","a"),
     ("     Why: fair use (limited, transformative, non-commercial) is a legal exception; the others are infringement.","o"),
     ("Discussion: who should own an AI-generated logo — the user, the AI firm, or no one? Why?","o")],
    "QUIZ [~5 min]. Cement the four IP types and the piracy-vs-fair-use-vs-licensing distinction; close on the AI question.")
add_summary("S41 · Summary  ·  [~2 min]",
    ["IP gives creators temporary exclusive rights so they profit despite free copying; four types — copyright, patent, trademark, trade secret (disclose vs hide to protect).",
     "Digital is a double edge: global reach (good) + trivial piracy (bad); platforms fight back with Content ID, takedowns & licensing.",
     "AI ownership is legally unsettled; Nepal's challenge is low awareness + high piracy; IP must balance creators' incentive against society's access."],
    "IP decides whether Nepal's musicians, coders, and designers can actually earn from their work in a world where copying is free. Knowing the four types and the legal paths (fair use, licensing, open licences) is essential whether you create, build, or invest — and it closes the unit's arc from 'information is free to copy' to 'so who gets paid?'.",
    "End of Unit 5 — next: the consolidated revision aids (cheat sheet, glossary, full quiz).",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 5 · Cheat Sheet","One-page revision reference",
    [("Info as a good (S34)","Information is NON-RIVAL, reusable, near-free to copy; an experience good. Symmetric = both know the same; asymmetric = one knows more (the norm). Real info is imperfect & costly; quality = accuracy, completeness, timeliness, source, relevance."),
     ("Lemons / asymmetry (S35)","Adverse selection = BEFORE the deal: hidden quality -> average price -> good sellers exit -> lemons (Akerlof). Moral hazard = AFTER the deal: hidden action, changed behaviour once protected. 5 determinants: cost, access, complexity, technology, regulation."),
     ("Signal / screen / digital (S36)","Signaling = INFORMED side proves quality (warranty, degree, brand — costly, hard to fake). Screening = UNINFORMED side sets a test/menu (deductibles, test drive, reviews) -> self-selection. Digital reduces old gaps (reviews) but creates new ones (fake reviews, paid rank, algorithms)."),
     ("Search & AI (S37–S38)","Search cost -> price dispersion; cheap search -> comparison market -> fair value. Search engine = gatekeeper (SEO, paid rank -> top ≠ best). AI reduces asymmetry (fraud detection, verification) & matches (efficiency) but scales bias, needs data, is a black box."),
     ("Strategy (S39)","New economics: info scarce->abundant, value from access/attention, price by value. Toolkit: versioning (tiers), price discrimination (different prices), bundling (package many), lock-in (S12), network effects (S10), AI dynamic pricing = automated price discrimination."),
     ("Choice, labor & IP (S40–S41)","Consumer: overload, bounded rationality, e-WOM -> platform curates choice. Labor: polarization (middle hollows out; ~40% routine at risk); gig work = flexible but insecure + algorithmic management. IP: copyright/patent/trademark/trade secret; digital = reach + piracy; AI ownership unsettled.")])

add_glossary("Unit 5 · Glossary","Key terms — quick reference",
    [("Information good","A non-rival, reusable good that is near-free to copy."),
     ("Non-rival","Many people can use the same information at once."),
     ("Experience good","Its value is hard to judge before you consume it."),
     ("Symmetric information","Both sides of a deal know the same relevant facts."),
     ("Asymmetric information","One side knows more than the other — an imbalance."),
     ("Perfect information","Textbook ideal: all facts known to all, free."),
     ("Imperfect information","Real case: incomplete and costly to obtain."),
     ("Search cost","The time/effort/money to find and compare options."),
     ("Adverse selection","Before-the-deal: hidden quality drives good out (lemons)."),
     ("Market for lemons","Average pricing leaves mostly bad goods (Akerlof)."),
     ("Moral hazard","After-the-deal: changed behaviour once protected."),
     ("Determinants of asymmetry","Cost, access, complexity, technology, regulation."),
     ("Signaling","Informed side proves quality with a costly, credible action."),
     ("Screening","Uninformed side sets a test/menu so types self-select."),
     ("Self-selection","A menu makes each type choose the option revealing it."),
     ("Price dispersion","Identical goods sold at very different prices."),
     ("Comparison market","Everyone sees every offer -> prices near fair value."),
     ("Gatekeeper","The search engine deciding which results you see."),
     ("SEO","Optimising to rank higher in organic search results."),
     ("Paid / sponsored ranking","Buying the top slot; 'top' ≠ best."),
     ("Recommendation engine","AI that predicts and ranks what you'll want."),
     ("Filter bubble","Personalization narrows what you are shown."),
     ("Black box","An AI whose decisions can't be fully explained."),
     ("New economics of information","Info abundant -> value from access & attention."),
     ("Versioning","Selling one product in tiers (free/premium)."),
     ("Price discrimination","Charging different buyers different prices."),
     ("Bundling","Selling many items together for one price."),
     ("Lock-in / switching cost","What keeps a customer from leaving (Unit 2 S12)."),
     ("Dynamic pricing","Real-time, per-person pricing (automated discrimination)."),
     ("Information overload","Too many options -> harder, worse decisions."),
     ("Bounded rationality","Limited attention -> reliance on shortcuts."),
     ("e-WOM","Electronic word of mouth — online reviews/ratings/influencers."),
     ("Polarization","Middle-skill jobs shrink; top & bottom grow."),
     ("Gig economy","Short-term, task-based platform work."),
     ("Algorithmic management","An app assigns, pays, rates & can deactivate workers."),
     ("Intellectual property (IP)","Legal ownership of creations of the mind."),
     ("Copyright","Protects creative works (life + ~50 years)."),
     ("Patent","Protects inventions (~20 years, then public)."),
     ("Trademark","Protects brand identity (renewable indefinitely)."),
     ("Trade secret","Protects secret know-how while it stays secret."),
     ("Content ID","Tech that matches uploads to copyrighted works."),
     ("Fair use","Limited, transformative use allowed without permission."),
     ("Piracy","Unauthorised copying/distribution of protected work.")])

# ============= CONSOLIDATED END-OF-UNIT QUIZ =============
add_divider("Unit 5 · Revision","Consolidated end-of-unit quiz",
    "Twelve MCQs across the whole unit (answers shown), then short-answer, applied-case, and discussion "
    "questions to work from the concept slides and Unit5_material.md.",
    "Use as a 15–20 min in-class quiz or take-home review. (No genuine IT 250 past-paper exists — built from the syllabus + the in-lecture question bank.)")
add_quiz("Section A — Multiple choice (answers shown)",
    [("1.  Information as an economic good is   →  b) ✅ non-rival & near-free to copy","a"),
     ("2.  One side of a deal knowing more than the other is   →  c) ✅ asymmetric information","a"),
     ("3.  In the market for lemons, good sellers exit because buyers pay   →  a) ✅ only an average price","a"),
     ("4.  Adverse selection happens ___ the deal; moral hazard happens ___ it   →  d) ✅ before / after","a"),
     ("5.  A worker earning a degree to prove ability to employers is   →  b) ✅ signaling","a"),
     ("6.  An insurer's menu of deductibles that sorts drivers is   →  c) ✅ screening","a"),
     ("7.  Identical goods at very different prices is   →  b) ✅ price dispersion","a"),
     ("8.  A key ETHICAL risk of AI decisions is that they   →  d) ✅ scale hidden bias / are a black box","a"),
     ("9.  Selling free vs premium tiers of one product is   →  a) ✅ versioning","a"),
     ("10.  Digitalization's effect on jobs is best called   →  c) ✅ polarization (middle hollows out)","a"),
     ("11.  A brand's name and logo are protected by   →  b) ✅ trademark","a"),
     ("12.  A new asymmetry digital markets create is   →  d) ✅ fake reviews / paid rankings","a")],
    "Consolidated quiz Section A. Correct-answer letters vary: 1-b, 2-c, 3-a, 4-d, 5-b, 6-c, 7-b, 8-d, 9-a, 10-c, 11-b, 12-d.",compact=True)
add_quiz("Sections B–D — short answer, applied case & discussion",
    [("Section B — Short answer","q"),
     ("13. Define asymmetric information + give 2 Nepali examples.   14. Adverse selection vs moral hazard — explain the before/after distinction.   15. Signaling vs screening — one example of each.","o"),
     ("16. Name 3 ways digitalization reduces asymmetry.   17. Name the 4 IP types with what each protects.","o"),
     ("Section C — Applied case","q"),
     ("18. Explain the used-vehicle OR manpower-agency market as adverse selection, and how reviews/signals fix it.","o"),
     ("19. Which Nepali jobs shrank vs emerged with digitalization, and why (polarization)?","o"),
     ("Section D — Discussion","q"),
     ("20. 'Do digital markets remove information asymmetry, or just create new power structures? Who controls choice — the consumer or the platform?'","o")],
    "Consolidated quiz Sections B–D. Model answers on the concept slides and in Unit5_material.md.",compact=True)

# ---- close ----
add_title("End of Unit 5  ·  IT 250",
          "S34–S41 complete: information as an economic good · asymmetric information (lemons, adverse selection & moral hazard) · "
          "signaling, screening & digitalization · the economics of search · AI & information · the new-economics strategy toolkit · "
          "consumer choice & labor polarization · intellectual property & digitalization",
          "Built to COURSE_MATERIAL_STANDARD.md incl. the §7A depth rule · comparison & concrete-example tables throughout · "
          "self-contained, PDF-safe, Nepal-localised · Next: Unit 6 — Digitalization, the Nepalese Perspective.")

_add_page_numbers()
save("IT250_Unit5.pptx")
