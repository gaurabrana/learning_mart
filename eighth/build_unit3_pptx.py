#!/usr/bin/env python3
"""IT250 (eighth) Unit 3 deck — Digital Markets, Strategy & Innovation (S16-S25), built to
COURSE_MATERIAL_STANDARD.md INCLUDING the §7A depth rule: every confusable set is a comparison
table, every 'X vs not-X' concept a concrete-example table (>=6 Nepal-localised rows), claims get
scaffolding tables — each table on its OWN slide, paginated, never squeezed. Self-contained &
PDF-safe. Imports eighth/deckkit.py. Diagrams in images/. Localised to Nepal's digital economy.
Source: syllabus + instructor lecture PDFs L1-L10 (mapped in Unit3_content_outline.md §0).
Builds directly on Unit 2 — network effects & two-sided markets are cross-referenced, not re-derived.
Fresh frameworks added for rigor: Porter's Five Forces (light), Value-Net co-opetition, disruptive
innovation, and the classic value chain / value shop / value network.
Run: python3 build_unit3_pptx.py -> IT250_Unit3.pptx
"""
from deckkit import *

# ============================================================
#                        FRONT MATTER
# ============================================================
add_title("Unit 3 — Digital Markets, Strategy & Innovation",
          "IT 250: Digital Economy  ·  BIM 8th Semester  ·  Sessions S16–S25 (10 lecture hours)",
          "Self-contained slides with depth: every concept grounded in comparison & concrete-example TABLES "
          "(Nepal-localised) — no abstraction without instances. Builds on Unit 2 (platforms, network effects). "
          "Exports to PDF with no information lost.")

add_outcomes("Unit 3 — Learning Outcomes","digital markets & strategy  ·  s16–s25",
    "By the end of this unit, you will be able to:",
    ["Describe digital markets — their 4 characteristics, 5 components, and 5 types (S16)",
     "Distinguish competition, cooperation & co-opetition, and explain why digital markets reward cooperation (S17–S19)",
     "Explain the layered internet model (infrastructure/platform/application) and why layer control confers power (S20)",
     "Define digital innovation, its types & enablers, and distinguish innovation from invention (sustaining vs disruptive) (S21)",
     "Compare the 10 digital business models and the value-creation models (incl. value chain/shop/network) (S22–S23)",
     "Explain how digital markets are modelled — pricing, dynamic pricing, two-sided markets, tipping (S24)",
     "Explain digital strategy — value capture, ecosystem strategy, control points — and integrate all dimensions (S25)"],
    "This is Unit 3 of IT 250. Unit 2 opened the 'engine room' (why platforms win). Unit 3 zooms out to the MARKET: how digital firms compete AND cooperate, how the internet is layered, how they innovate, the business & value models they run on, and the STRATEGY that ties it together.")

add_roadmap("Unit 3 — Roadmap","Where each session fits (S16–S25)",
    ["S16  Introduction to digital markets",
     "S17  Competition in digital markets",
     "S18  Cooperation in digital markets",
     "S19  Co-opetition (cooperate + compete)",
     "S20  The layered internet model",
     "S21  Digital innovation",
     "S22  Digital business models (the 10)",
     "S23  Value-creation models",
     "S24  Modelling digital markets",
     "S25  Strategy & integration (closes unit)"],
    ["Unit 1  Introduction (digital/K-economy, 4IR) — done",
     "Unit 2  Fundamentals (platforms, network effects) — done",
     "Unit 4  Digital transformation & currencies",
     "Unit 5  Economics of information",
     "Unit 6  Digitalization — the Nepalese perspective"])

# ============================================================ S16
add_divider("Session 16 · Lecture hour 1 (of 10)","Introduction to Digital Markets",
    "Fifty years ago a 'market' was a physical place — Asan Bazaar, a shop, a mandi — where you went, haggled, and carried goods home. Today you buy a phone on Daraz at midnight, pay with eSewa, and a rider brings it tomorrow. The market never closed and you never left home. What exactly IS a digital market, and how is it different from the bazaar?",
    "OPENING HOOK [~5 min]. Contrast Asan Bazaar with buying on Daraz. Agenda: what a digital market is + its 4 characteristics -> the 5 components it runs on -> the 5 types (B2C/B2B/C2C/C2B/P2P).")

concept_understand("S16 · Concept 1 · [THEORY]","What a Digital Market Is + 4 Characteristics",
    "A digital market is an online space where buyers and sellers discover each other, agree a price, and transact — matched, priced, and settled electronically instead of in a physical place. Four characteristics set it apart from a traditional market: SPEED (near-instant search and transactions), SCALE (reach beyond geography), NETWORK EFFECTS (more users make it more valuable — see Unit 2), and LOW MARGINAL COST (serving one more buyer costs almost nothing).",
    ["Speed: search, compare, pay and confirm in seconds, 24/7 — no travel, no opening hours.",
     "Scale: a Kathmandu seller can reach all of Nepal (and abroad) without a second shop.",
     "Network effects (from Unit 2): each extra buyer/seller makes the market more useful to the others.",
     "Low marginal cost: once the platform exists, one more listing or user is almost free to serve."],
    "s16_digital_market.png","Digital market = buyers + sellers meeting online; marked by speed, scale, network effects, low marginal cost.",
    "~7 min. Use the diagram. Cross-ref Unit 2 for network effects & low marginal cost — here they are two of four DEFINING traits of a digital market.")
add_comparison_table("S16 · Concept 1 · comparison","Traditional market vs digital market",
    ["Dimension","Traditional market","Digital market"],
    [["Where it happens","A physical place (shop, bazaar)","An online platform (app/website)"],
     ["Hours & speed","Opening hours; slow search","24/7; near-instant search & pay"],
     ["Reach","Local, limited by geography","National/global, geography-free"],
     ["Cost of one more sale","Real (space, stock, staff)","Near-zero (a listing, a login)"],
     ["Information","Scarce; you must ask around","Abundant: prices, reviews, ratings"],
     ["Value with more users","Roughly flat","Rises (network effects)"]],
    per_page=6,widths=[1.8,2.5,2.6],fs=11,
    note="The four characteristics — speed, scale, network effects, low marginal cost — are exactly the columns where a digital market pulls away from the bazaar. They are why online markets grow so fast.")
concept_apply("S16 · Concept 1 · [THEORY]","What a Digital Market Is + 4 Characteristics",
    "Daraz is a digital market: at midnight you search thousands of products (speed), from sellers across Nepal you'd never reach on foot (scale), on a platform that is more useful because millions already shop there (network effect), and Daraz can add your order at almost no extra cost (low marginal cost). Asan Bazaar has none of these four at the same time — that is the structural leap from bazaar to platform.",
    "\"A digital market is just a shop with a website.\" A website is only a shopfront. A digital market is where independent buyers and sellers actually meet, match, price, and settle online — with speed, geography-free scale, network effects, and near-zero marginal cost. Those four traits, not the web address, make it a market.",
    "A digital market is an online space where buyers and sellers discover each other, agree a price, and transact electronically rather than in a physical place. Four characteristics distinguish it from a traditional market: speed (instant search/transactions, 24/7), scale (reach beyond geography), network effects (more users add value — Unit 2), and low marginal cost (serving one more user is almost free). Daraz shows all four at once.",
    "digital market · speed · scale · network effects · low marginal cost · online matching")

concept_understand("S16 · Concept 2 · [THEORY]","The 5 Components of a Digital Market",
    "A digital market is not one thing — it runs on five components working together. (1) The PLATFORM (app/website) hosts the marketplace and matches sides. (2) PAYMENTS move money safely (wallets, gateways, banks). (3) LOGISTICS deliver the goods (couriers, tracking, warehouses). (4) DATA & ANALYTICS power search, recommendations, pricing, and fraud checks. (5) SUPPORT & TRUST (ratings, returns, help desks, dispute resolution) keep strangers transacting.",
    ["Platform: the software that lists, searches, and matches buyers and sellers.",
     "Payments + logistics: the two rails that turn a click into money moved and goods delivered.",
     "Data & analytics: recommendations, dynamic pricing, and fraud detection all run on data.",
     "Support & trust: ratings, returns, and dispute handling — without trust the market collapses."],
    None,"Five components: platform · payments · logistics · data & analytics · support/trust.",
    "~7 min. Stress that a missing component breaks the market — great platform but no delivery, or no trust layer, and buyers leave. Nepal's weak logistics is the usual bottleneck.")
add_examples_table("S16 · Concept 2 · examples","The 5 components — with Nepal examples",
    ["Component","What it does","Nepal example"],
    [["Platform","Hosts listings, search & matching","Daraz app, Foodmandu, Hamrobazar"],
     ["Payments","Moves money safely","eSewa, Khalti, Fonepay, ConnectIPS"],
     ["Logistics","Delivers goods, tracks orders","Pathao/Aramex couriers, Daraz hubs"],
     ["Data & analytics","Search, recommendations, pricing, fraud","Daraz recommendations; surge pricing"],
     ["Support & trust","Ratings, returns, help, disputes","Seller ratings, return policy, call centre"]],
    per_page=5,widths=[1.8,2.7,2.6],fs=11,
    note="A digital market is only as strong as its weakest component. In Nepal, payments and platforms are mature, but logistics (last-mile delivery outside cities) and trust (fake products) are the common weak links.")
concept_apply("S16 · Concept 2 · [THEORY]","The 5 Components of a Digital Market",
    "When you order on Daraz, all five components fire: the platform lists and matches the product, Khalti/eSewa or cash-on-delivery handles payment, a Pathao/Aramex rider delivers it, data decides what Daraz showed you and flags fraud, and ratings + a return policy give you the confidence to buy from an unknown seller. Remove any one — say delivery fails outside the valley — and the market stops working there.",
    "\"The platform IS the digital market.\" The platform is only one of five components. Payments, logistics, data, and trust are equally load-bearing: a slick app with no reliable delivery or no return policy will not sustain a market. In Nepal, logistics and trust — not the app — are usually what limits growth.",
    "A digital market runs on five components: the platform (hosts and matches), payments (move money — eSewa/Khalti/Fonepay), logistics (deliver goods — couriers, tracking), data & analytics (search, recommendations, pricing, fraud), and support & trust (ratings, returns, dispute resolution). All five must work together; the market is only as strong as its weakest component — in Nepal usually logistics or trust.",
    "platform · payments · logistics · data & analytics · support/trust · weakest-link")

concept_understand("S16 · Concept 3 · [THEORY]","The 5 Types of Digital Market",
    "Digital markets are classified by WHO transacts with WHOM. B2C (business-to-consumer): a firm sells to individuals (Daraz, Netflix). B2B (business-to-business): firms sell to firms (a cloud provider, a wholesale portal). C2C (consumer-to-consumer): individuals sell to each other (Hamrobazar, Facebook Marketplace). C2B (consumer-to-business): individuals sell to firms (a freelancer on Fiverr, a creator selling content). P2P (peer-to-peer): individuals share/exchange directly, often an asset (a room on Airbnb, a ride on InDrive).",
    ["B2C & B2B are the two 'business-sells' types — to consumers or to other businesses.",
     "C2C & C2B flip the direction: individuals are the sellers (to peers, or to firms).",
     "P2P: peers transact/share directly, with the platform only mediating (Airbnb, InDrive).",
     "A single platform can span types: Daraz is mainly B2C but its marketplace sellers add C2C/B2B."],
    None,"Five types by who-sells-to-whom: B2C · B2B · C2C · C2B · P2P.",
    "~7 min. Have students place Nepali platforms into the five boxes; note many are hybrids (Daraz = B2C + marketplace).")
add_examples_table("S16 · Concept 3 · examples","The 5 types of digital market — Nepal & global",
    ["Type","Who -> who","Example"],
    [["B2C","Business sells to consumers","Daraz, Foodmandu, Netflix, Sastodeal"],
     ["B2B","Business sells to business","AWS/cloud, wholesale portals, SaaS tools"],
     ["C2C","Consumer sells to consumer","Hamrobazar, Facebook Marketplace, eBay"],
     ["C2B","Consumer sells to business","Freelancers on Fiverr/Upwork; stock photos"],
     ["P2P","Peers share/exchange directly","Airbnb (rooms), InDrive, ride/asset sharing"]],
    per_page=5,widths=[1.2,2.6,3.0],fs=11,
    note="The type tells you who the customer is and how money flows. Many real platforms are hybrids — Daraz is B2C for its own stock and C2C/B2B for third-party sellers — so name the DOMINANT relationship first.")
concept_apply("S16 · Concept 3 · [THEORY]","The 5 Types of Digital Market",
    "Hamrobazar is C2C — ordinary Nepalis buy and sell used goods to each other, with the platform only providing the meeting place and trust tools. Daraz is mainly B2C (businesses selling to consumers) but becomes C2C/B2B where independent sellers list. A Nepali designer selling gigs on Fiverr is C2B (an individual selling to firms). Naming the type tells you instantly who the paying customer is.",
    "\"All e-commerce is B2C.\" B2C is only one of five types. C2C (Hamrobazar), C2B (freelancers selling to firms), B2B (cloud/wholesale), and P2P (Airbnb/InDrive) are all digital markets with different customers and money flows. Classifying by who-sells-to-whom, not just 'it's online', is what the exam rewards.",
    "Digital markets are classified by who transacts with whom: B2C (business to consumer — Daraz, Netflix), B2B (business to business — cloud, wholesale), C2C (consumer to consumer — Hamrobazar, Marketplace), C2B (consumer to business — freelancers, creators), and P2P (peers share/exchange directly — Airbnb, InDrive). Many platforms are hybrids, so identify the dominant relationship first.",
    "B2C · B2B · C2C · C2B · P2P · classify by who-sells-to-whom · hybrids")

add_activity("S16 — 'Classify the market'  ·  ~5 min",
    ["In pairs (2 min): pick 3 Nepali digital services (Daraz, eSewa, Hamrobazar, Foodmandu, InDrive…).",
     "For each, name its TYPE (B2C/B2B/C2C/C2B/P2P) and the 5 components it relies on.",
     "Flag any component that is weak for that service in Nepal.",
     "Take 3 answers aloud (3 min); resolve hybrids by naming the dominant relationship."],
    "Good answers: Daraz = mainly B2C (weak link: logistics outside valley + trust/fake goods); Hamrobazar = C2C (weak link: trust/escrow); Foodmandu = B2C (weak link: rider logistics at peak). Reward naming the DOMINANT type and a real weak component.",
    "ACTIVITY [~5 min].")
add_quiz("S16 — Quick Check  ·  ~5 min",
    [("Q1.  Which is NOT one of the four characteristics of a digital market?","q"),
     ("a) speed   b) scale   c) ✅ high marginal cost per user   d) network effects","a"),
     ("     Why: digital markets have LOW (near-zero) marginal cost — the opposite of high.","o"),
     ("Q2.  Ordinary people buying and selling used phones to each other on Hamrobazar is:","q"),
     ("a) B2C   b) ✅ C2C (consumer-to-consumer)   c) B2B   d) C2B","a"),
     ("     Why: both sides are consumers; the platform only provides the meeting place and trust.","o"),
     ("Discussion: pick a Nepali platform — name its type and its weakest of the 5 components.","o")],
    "QUIZ [~5 min]. Cement the 4 characteristics (esp. LOW marginal cost) and classifying by type.")
add_summary("S16 · Summary  ·  [~2 min]",
    ["A digital market matches buyers & sellers online; 4 traits: speed, scale, network effects, low marginal cost.",
     "It runs on 5 components: platform, payments, logistics, data & analytics, support/trust — only as strong as the weakest.",
     "Five types by who-sells-to-whom: B2C, B2B, C2C, C2B, P2P — many platforms are hybrids."],
    "Every Nepali digital business you use is one of these types running on these five components — spotting the type and the weak component is exactly how a founder finds a gap (e.g. better rural logistics) or how you assess where a platform is fragile.",
    "S17 — how digital markets COMPETE: why online competition differs from the bazaar, and winner-take-most.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S17
add_divider("Session 17 · Lecture hour 2 (of 10)","Competition in Digital Markets",
    "In Asan, ten shops sell the same rice and compete on price and a friendly smile. Online, one search engine has ~90% of the world and one messenger owns Nepal. Why does competition online so often end with ONE big winner, when the bazaar keeps many sellers alive? Digital competition follows different rules.",
    "OPENING HOOK [~5 min]. Contrast ten rice shops with one search engine. Agenda: traditional vs digital competition (+ a light Porter Five Forces) -> winner-take-most & dominance -> effects on consumers & startups.")

concept_understand("S17 · Concept 1 · [THEORY]","Traditional vs Digital Competition",
    "Traditional firms compete mainly on price, location, and product quality within a local area. Digital firms compete on data, network size, speed of innovation, ecosystem, and user experience — often globally and at near-zero marginal cost. A useful lens is Porter's Five Forces (rivalry, new entrants, buyer power, supplier power, substitutes): online, low entry cost raises the threat of new entrants, but network effects and data raise the barriers protecting the leader — so competition is fiercer AND more concentrated.",
    ["Basis of competition shifts: from price/location to data, network size, and user experience.",
     "Reach & speed: local and slow becomes global and near-instant.",
     "Switching costs & data become weapons — the leader learns faster and locks users in (Unit 2).",
     "Porter's Five Forces still apply, but digital changes their strength (easy entry, high moats)."],
    None,"Traditional competes on price/place/quality; digital competes on data, network, speed, UX — global & concentrated.",
    "~8 min. Introduce Porter's Five Forces LIGHTLY as a lens; the deep point is HOW digital shifts each force. Cross-ref Unit 2 network effects.")
add_comparison_table("S17 · Concept 1 · comparison","Traditional competition vs digital competition",
    ["Dimension","Traditional competition","Digital competition"],
    [["Basis","Price, location, product quality","Data, network size, UX, speed of innovation"],
     ["Reach","Local / regional","National / global"],
     ["Speed","Slow (months to react)","Fast (features ship in days)"],
     ["Cost of growth","High (each unit costs)","Low (near-zero marginal cost)"],
     ["Switching cost for buyer","Low (walk to next shop)","Often high (data, habit, network)"],
     ["Role of data","Minor","Central — a competitive weapon"],
     ["Typical outcome","Many firms coexist","Winner-take-most (one dominant)"]],
    per_page=8,widths=[1.7,2.5,2.7],fs=11,
    note="Same five Porter forces, different strengths: online entry is cheap (more entrants) yet network effects and data build high moats (fewer survive) — which is why digital competition is both fiercer and more concentrated.")
add_table_slide("S17 · Concept 1 · scaffolding","Porter's Five Forces — the digital twist",
    ["Force","What it asks","Digital twist (example)"],
    [["Rivalry among firms","How intense is competition?","Fierce but often winner-take-most (search)"],
     ["Threat of new entrants","How easy to enter?","Easy to start, hard to scale vs network effects"],
     ["Buyer power","Can buyers push back?","High — reviews & one-click switching (small items)"],
     ["Supplier power","Can suppliers squeeze you?","Sellers depend on the platform (low power)"],
     ["Threat of substitutes","Is there another way?","Many apps substitute (super-apps absorb them)"]],
    per_page=5,widths=[1.9,2.2,3.0],fs=10.5,
    note="Porter's framework still works as a checklist, but network effects, data, and low marginal cost bend every force toward the incumbent once a platform gets ahead — the moat, not the smile, wins online.")
concept_apply("S17 · Concept 1 · [THEORY]","Traditional vs Digital Competition",
    "Two Kathmandu grocery shops compete on price and location; a customer walks to whichever is cheaper. Daraz vs a new e-commerce startup is different — Daraz competes with data (it knows what you buy), a huge seller network, faster feature updates, and switching costs (your saved cards, order history). The startup can copy the app in months but cannot copy Daraz's network or data, so digital competition concentrates.",
    "\"Online competition is just offline competition with a website.\" The BASIS changes: from price/location to data, network size, speed, and user experience, at global scale and near-zero marginal cost. Porter's five forces still apply, but network effects and data tilt them toward whoever leads — so digital markets concentrate far more than the bazaar.",
    "Traditional firms compete on price, location, and quality locally; digital firms compete on data, network size, speed of innovation, ecosystem, and user experience, usually globally and at near-zero marginal cost. Porter's Five Forces (rivalry, entrants, buyer power, supplier power, substitutes) still apply, but online, easy entry raises the entrant threat while network effects and data raise the incumbent's moat — making competition both fiercer and more concentrated.",
    "basis of competition · data as weapon · global reach · Porter's Five Forces · concentration")

concept_understand("S17 · Concept 2 · [THEORY]","Winner-Take-Most & Platform Dominance",
    "In many digital markets competition ends in 'winner-take-most' — the leader captures the bulk of the market, one small rival survives, and the rest fade. This is the same mechanism as Unit 2's tipping: network effects + economies of scale + switching costs create increasing returns, so being slightly ahead compounds into dominance. But not every market tips — where multi-homing is easy and needs are local (ride-hailing, food delivery), several players coexist.",
    ["Winner-take-most, not always winner-take-ALL: a small rival usually lingers.",
     "Driver = increasing returns (network effects + scale + lock-in — all from Unit 2).",
     "Past a tipping point, users pile onto the leader and reversal becomes very hard.",
     "Not universal: easy multi-homing + local needs keep some markets contested (Pathao vs InDrive)."],
    None,"Winner-take-most: increasing returns tip many digital markets to one leader — but not all (multi-homing keeps some contested).",
    "~7 min. Explicitly a callback to Unit 2 S13 tipping — reuse, don't re-derive. Contrast search (tipped) with ride-hailing (contested).")
add_examples_table("S17 · Concept 2 · examples","Nepali digital markets — tipped vs contested",
    ["Market","Leader(s)","Tipped or contested?","Why"],
    [["Search","Google","Tipped (global)","Strong data + habit; no reason to multi-home"],
     ["Messaging","WhatsApp/Viber","Tipped to WhatsApp","Contacts settled on one; high switching cost"],
     ["Digital wallet","eSewa, Khalti","Concentrating","Network + merchant lock-in, but 2-3 survive"],
     ["Ride-hailing","Pathao, InDrive","Contested","Easy multi-homing; local, low switching cost"],
     ["Food delivery","Foodmandu, Pathao","Contested","Restaurants & riders multi-home; local needs"],
     ["E-commerce","Daraz","Leading, not sole","Scale + data lead, but niche sellers persist"]],
    per_page=6,widths=[1.5,1.8,1.9,2.8],fs=10.5,
    note="Same country, different outcomes: search and messaging tip to one winner (strong effects, high switching); ride-hailing and food delivery stay contested (easy multi-homing, local needs). Knowing which is a strategic and regulatory question.")
concept_apply("S17 · Concept 2 · [THEORY]","Winner-Take-Most & Platform Dominance",
    "Nepal's messaging market tipped to WhatsApp — once contacts settled there, its value rose for everyone and Viber faded (high network effects, high switching cost, little multi-homing). Ride-hailing has NOT tipped: Pathao and InDrive coexist because drivers and riders happily run both apps and needs are local. Same digital economy, opposite outcomes, decided by network-effect strength and multi-homing.",
    "\"Every digital market ends in one monopoly.\" Only markets with strong network effects, high switching costs, and little multi-homing tip to one winner (search, messaging). Where multi-homing is easy and needs differ (ride-hailing, food delivery), several players persist. Tipping is a tendency, not a law — this is Unit 2's tipping applied to competition.",
    "Digital competition often ends in 'winner-take-most' — the leader takes the bulk, a small rival survives, and the rest fade — driven by increasing returns (network effects + scale + switching costs, from Unit 2). Past a tipping point the leader is hard to beat. But not every market tips: where multi-homing is easy and needs are local (ride-hailing, food delivery), several platforms coexist. WhatsApp tipped in Nepal; ride-hailing did not.",
    "winner-take-most · increasing returns · tipping point (Unit 2) · multi-homing keeps markets contested")

concept_understand("S17 · Concept 3 · [THEORY]","Effects on Consumers & Startups",
    "Digital competition is double-edged. For CONSUMERS, early competition brings lower prices, more choice, and better service — but once a market tips, dominance can mean fewer choices, data harvesting, and terms set by the gatekeeper. For STARTUPS, low entry cost makes it easy to launch but brutally hard to scale against an incumbent's network effects and data. The result: a burst of new entrants, most of whom cannot cross the chasm to critical mass.",
    ["Consumers early: lower prices, more choice, better UX from fierce competition.",
     "Consumers late: after tipping — fewer alternatives, data extraction, gatekeeper terms.",
     "Startups: cheap to launch, hard to scale past the incumbent's network effect (the moat).",
     "Net effect: many launch, few reach critical mass — a 'winner-take-most' funnel."],
    None,"Consumers: cheaper & better early, then fewer choices after tipping. Startups: easy to launch, hard to scale vs the moat.",
    "~6 min. Balance the story: competition benefits consumers UNTIL dominance; startups face an easy-entry/hard-scale trap. Sets up why cooperation (S18) is often the survival move.")
add_comparison_table("S17 · Concept 3 · comparison","Dominance — effect on consumers vs startups",
    ["Aspect","Effect on consumers","Effect on startups"],
    [["Early competition","Lower prices, more choice","Easy, cheap to launch"],
     ["After tipping","Fewer alternatives, lock-in","Hard to scale vs incumbent moat"],
     ["Data","Personalised service…","…but incumbent's data edge is un-catchable"],
     ["Innovation","Fast at first, can stall later","Must find a niche the giant ignores"],
     ["Prices/terms","Gatekeeper can raise fees/terms","Commissions & platform rules squeeze margins"]],
    per_page=5,widths=[1.7,2.6,2.7],fs=11,
    note="The same dominance that once delivered cheap, convenient service can later reduce choice and squeeze the small players who depend on the platform — which is exactly why Nepali startups so often COOPERATE rather than fight head-on (S18).")
concept_apply("S17 · Concept 3 · [THEORY]","Effects on Consumers & Startups",
    "Nepal's wallet war benefited consumers with cashbacks and free transfers while eSewa and Khalti fought hard. A new wallet startup, though, faces the trap: launching an app is cheap, but pulling users off eSewa/Khalti's merchant network is nearly impossible. So many Nepali startups do NOT fight the giant head-on — they integrate with it (build on Fonepay rails) or serve a niche the giant ignores, which is the cooperation logic of the next session.",
    "\"Competition is always good for consumers, always bad for big firms.\" Competition helps consumers EARLY (price, choice) but a tipped market can then reduce choice and set terms. And low entry cost flatters startups — the hard part is scaling against the moat, not launching. Dominance is double-edged for both sides.",
    "Digital competition is double-edged. Consumers gain lower prices, more choice, and better service while competition is fierce, but a tipped market can bring fewer alternatives, data harvesting, and gatekeeper-set terms. Startups find it cheap to launch but brutally hard to scale against an incumbent's network effects and data, so most cannot reach critical mass. This is why many Nepali startups cooperate or find niches rather than fight head-on (S18).",
    "consumer benefit early · lock-in late · easy launch, hard scale · incumbent moat · niche or cooperate")

add_activity("S17 — 'Will it tip, and who wins?'  ·  ~5 min",
    ["In pairs (3 min): pick a Nepali digital market (wallets, ride-hailing, e-commerce, food, messaging).",
     "Decide: will it tip to one winner or stay contested? Use network effects, switching cost, multi-homing.",
     "Name one effect on consumers and one on a would-be startup entrant.",
     "Take 3–4 answers aloud (2 min); compare predictions with the tipped/contested table."],
    "Good reasoning: messaging/search tip (strong effects, high switching); ride-hailing/food stay contested (easy multi-homing). Consumers gain early then risk lock-in; startups launch easily but struggle to scale. Reward using the factors explicitly.",
    "ACTIVITY [~5 min].")
add_quiz("S17 — Quick Check  ·  ~5 min",
    [("Q1.  Compared with a bazaar, digital competition is mainly fought on:","q"),
     ("a) rent & smiles   b) ✅ data, network size, speed & user experience   c) shop location   d) shouting","a"),
     ("     Why: online the basis shifts from price/location to data, network, speed, and UX — often global.","o"),
     ("Q2.  Ride-hailing in Nepal stays contested (Pathao + InDrive) mainly because:","q"),
     ("a) weak apps   b) ✅ easy multi-homing & local needs   c) no network effects at all   d) government rule","a"),
     ("     Why: drivers/riders run both apps and needs are local, so the market does not tip to one.","o"),
     ("Discussion: name a Nepali market that tipped and one that stayed contested — why?","o")],
    "QUIZ [~5 min]. Reinforce the basis-of-competition shift and tipped-vs-contested (callback to Unit 2).")
add_summary("S17 · Summary  ·  [~2 min]",
    ["Digital competition shifts the basis from price/location to data, network size, speed & UX — global, near-zero marginal cost.",
     "Winner-take-most via increasing returns (Unit 2 tipping) — but easy multi-homing & local needs keep some markets contested.",
     "Double-edged: consumers gain early then risk lock-in; startups launch easily but struggle to scale vs the moat."],
    "This explains why Nepal tends to get one dominant player per category and why challengers struggle — and it sets up the surprising survival strategy of the next three sessions: in digital markets, firms often COOPERATE with rivals rather than only fight them.",
    "S18 — the counter-move: cooperation in digital markets, and why 'grow the pie first' beats fighting.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S18
add_divider("Session 18 · Lecture hour 3 (of 10)","Cooperation in Digital Markets",
    "eSewa and Khalti are rivals — yet both settle through the same NCHL/ConnectIPS rails, and any wallet can scan a Fonepay QR. Rivals sharing the very pipes they compete on sounds mad in the bazaar. Online it is normal, even necessary. Why do digital firms cooperate with their competitors?",
    "OPENING HOOK [~5 min]. Point out rivals sharing ConnectIPS/QR rails. Agenda: what cooperation is + why digital encourages it -> the 5 reasons ('grow the pie first') -> the 3 forms of cooperation.")

concept_understand("S18 · Concept 1 · [THEORY]","What Cooperation Is + Why Digital Encourages It",
    "Cooperation is when firms work together — sharing infrastructure, standards, data, or customers — to create value they could not create alone. Digital markets encourage it more than traditional ones for four reasons: MODULARITY (products are built from interchangeable parts that must interconnect), APIs (software makes plugging systems together cheap), NETWORK EFFECTS (a shared standard grows everyone's value), and CONVENIENCE (users want one seamless experience, not ten disconnected apps).",
    ["Cooperation = jointly creating value (shared rails, standards, data) beyond what one firm can.",
     "Modularity + APIs make interconnection cheap and technical — plug in, don't rebuild.",
     "Network effects reward shared standards: a QR everyone accepts is worth more to all.",
     "Convenience: users demand seamless journeys, forcing rivals to interoperate."],
    None,"Cooperation = create value together; digital encourages it via modularity, APIs, network effects & convenience.",
    "~7 min. Contrast with zero-sum bazaar thinking. The key: online, a shared standard makes the whole market bigger — cooperation and competition coexist.")
add_table_slide("S18 · Concept 1 · scaffolding","Why digital markets encourage cooperation — cause -> effect",
    ["Driver","Why it pushes firms to cooperate","Nepal example"],
    [["Modularity","Products are parts that must interconnect","Wallet + bank + biller must link up"],
     ["APIs","Plugging systems together is cheap & fast","eSewa integrating a bank via API"],
     ["Network effects","A shared standard grows everyone's value","QR interoperability (any wallet, any QR)"],
     ["Convenience","Users want one seamless experience","Pay any biller from one wallet app"],
     ["Cost sharing","Building rails alone is too expensive","Banks jointly funding NCHL/ConnectIPS"]],
    per_page=5,widths=[1.6,3.0,2.4],fs=11,
    note="In the bazaar, helping a rival is loss. Online, shared standards and rails make the WHOLE market bigger and cheaper to serve — so cooperating on the plumbing while competing on the product is rational.")
concept_apply("S18 · Concept 1 · [THEORY]","What Cooperation Is + Why Digital Encourages It",
    "Nepal's banks jointly built and fund NCHL/ConnectIPS — shared payment rails no single bank would build alone. Because payments are modular and API-connected, and because a standard everyone accepts is worth more to everyone (network effect), rivals cooperate on the plumbing. QR interoperability is the clearest case: eSewa, Khalti, and banks agreed a common QR so any customer can pay any merchant — growing the whole cashless market.",
    "\"Cooperating with a competitor is always a mistake.\" In digital markets, shared standards and rails enlarge the whole market via network effects, and modular/API architecture makes interconnection cheap. Firms cooperate on the infrastructure (the pipes) while still competing on the product (the app and customers) — cooperation and competition coexist.",
    "Cooperation is firms working together — sharing infrastructure, standards, data, or customers — to create value none could alone. Digital markets encourage it more than traditional ones because of modularity (products are interconnecting parts), APIs (cheap technical integration), network effects (a shared standard grows everyone's value), and convenience (users want one seamless experience). Nepal's banks cooperating on ConnectIPS and QR interoperability shows the logic.",
    "cooperation · modularity · APIs · network effects · convenience · shared standards/rails")

concept_understand("S18 · Concept 2 · [THEORY]","The 5 Reasons to Cooperate ('Grow the Pie First')",
    "Firms cooperate for five concrete reasons: (1) GROW THE MARKET — a bigger cashless pie helps every wallet before they fight for slices; (2) SHARE COSTS & RISK — jointly building rails or standards no one can afford alone; (3) ACCESS CAPABILITIES — borrow a partner's logistics, licence, or user base; (4) SET STANDARDS — agree a common format so the market interoperates; (5) SPEED & REACH — enter a market or launch faster together than alone. The mindset: 'grow the pie first, then compete for slices.'",
    ["Grow the market: cooperation expands total demand before anyone competes for share.",
     "Share cost & risk: expensive infrastructure (rails, standards) is built jointly.",
     "Access capabilities & set standards: borrow strengths; agree interoperable formats.",
     "Speed & reach: partnerships enter markets and scale faster than going alone."],
    None,"Five reasons: grow the market · share cost/risk · access capabilities · set standards · speed & reach.",
    "~7 min. 'Grow the pie first, then compete for slices' is the memory hook. In Nepal, collaboration is often survival, not luxury.")
add_table_slide("S18 · Concept 2 · scaffolding","The 5 reasons to cooperate — with payoff",
    ["Reason","What the firm gains","Nepal example"],
    [["Grow the market","A bigger total pie for all","Wallets pushing 'go cashless' together"],
     ["Share cost & risk","Afford what none could alone","Banks co-funding NCHL/ConnectIPS"],
     ["Access capabilities","Borrow a partner's strength","Daraz using Pathao/Aramex for delivery"],
     ["Set standards","An interoperable market","Common QR standard across wallets"],
     ["Speed & reach","Enter/scale faster","A bank + fintech co-launching a product"]],
    per_page=5,widths=[1.7,2.4,2.9],fs=11,
    note="Each reason is a payoff: cooperation is not charity but strategy. 'Grow the pie first, then compete for slices' — in a small market like Nepal, cooperation is often the only way any player reaches scale.")
concept_apply("S18 · Concept 2 · [THEORY]","The 5 Reasons to Cooperate",
    "Daraz doesn't own a delivery fleet — it partners with Pathao and Aramex (accessing a capability) rather than burning cash to build logistics alone. Nepali wallets jointly promote 'go cashless' (growing the market) before fighting for users, and co-fund shared rails (sharing cost & risk). Each is a concrete reason from the five: cooperation lets a Nepali firm reach scale it could never afford by fighting alone.",
    "\"Firms only cooperate when they're weak.\" Cooperation is a deliberate strategy for the strong too: grow the total market, share the cost of expensive infrastructure, borrow capabilities, set standards, and move faster. 'Grow the pie first, then compete for slices' — enlarging the market first often beats fighting over today's small one.",
    "Firms cooperate for five reasons: grow the total market (a bigger pie for all), share cost and risk (build expensive rails jointly), access capabilities (borrow a partner's logistics/licence/users), set standards (make the market interoperable), and gain speed and reach (enter or scale faster). The mindset is 'grow the pie first, then compete for slices' — in a small market like Nepal, cooperation is often survival, not luxury.",
    "grow the market · share cost & risk · access capabilities · set standards · speed & reach · grow the pie first")

concept_understand("S18 · Concept 3 · [THEORY]","The 3 Forms of Cooperation",
    "Cooperation takes three main forms. (1) JOINT PLATFORMS / shared infrastructure — rivals build or use common rails (NCHL, ConnectIPS, SWIFT, a shared QR). (2) PARTNERSHIPS — two firms combine strengths through co-branding, logistics deals, or joint marketing (Daraz + a courier; a bank + a fintech). (3) SERVICE INTEGRATION — one service embeds another so the user gets a seamless experience (pay a utility bill inside a wallet; log in with Google). Each deepens interdependence.",
    ["Joint platforms: shared rails/standards owned or used by rivals (ConnectIPS, SWIFT, QR).",
     "Partnerships: co-branding, logistics, or marketing deals combining two firms' strengths.",
     "Service integration: one app embeds another's service for a seamless user journey.",
     "The forms stack: two firms can partner AND integrate AND share a platform at once."],
    None,"Three forms: joint platforms (shared rails) · partnerships (co-brand/logistics/marketing) · service integration.",
    "~7 min. Give one Nepal case per form. Note these set up S19: cooperating on rails while competing for customers = co-opetition.")
add_examples_table("S18 · Concept 3 · examples","The 3 forms of cooperation — Nepal examples",
    ["Form","How it works","Nepal / global example"],
    [["Joint platform","Rivals share common rails/standards","NCHL, ConnectIPS, SWIFT, shared QR"],
     ["Partnership (logistics)","Combine delivery strengths","Daraz + Pathao/Aramex couriers"],
     ["Partnership (co-brand)","Two brands launch together","Bank + fintech co-branded card/wallet"],
     ["Partnership (marketing)","Joint campaigns/cashback","Wallet + merchant festival offers"],
     ["Service integration","Embed one service in another","Pay NEA/water bills inside eSewa/Khalti"],
     ["Service integration","Single sign-on / embedded pay","'Login with Google'; in-app Fonepay"]],
    per_page=6,widths=[1.9,2.3,2.8],fs=10.5,
    note="These forms explain HOW Nepali firms cooperate in practice — and they set up S19: when firms cooperate on the rails (upstream) while competing for customers (downstream), that is co-opetition.")
concept_apply("S18 · Concept 3 · [THEORY]","The 3 Forms of Cooperation",
    "eSewa lets you pay your NEA electricity bill and Ncell top-up inside the app — service integration that makes the wallet stickier. Daraz partners with Pathao and Aramex for delivery (a logistics partnership). And every wallet plugs into NCHL/ConnectIPS (a joint platform). Often all three stack: two firms partner, integrate services, and share rails at once — deepening cooperation while they still compete for the customer.",
    "\"Cooperation means merging or becoming friends.\" It has three concrete forms — joint platforms (shared rails), partnerships (co-branding, logistics, marketing), and service integration (embedding one service in another) — none of which require merging. Firms stay independent rivals while cooperating on specific layers, which is exactly the setup for co-opetition (S19).",
    "Cooperation takes three forms: joint platforms / shared infrastructure (rivals build or use common rails — NCHL, ConnectIPS, SWIFT, a shared QR); partnerships (co-branding, logistics, or marketing deals combining strengths — Daraz + a courier); and service integration (one service embeds another for a seamless experience — bill payment inside a wallet, 'login with Google'). The forms stack, deepening interdependence while firms stay independent.",
    "joint platforms · partnerships (co-brand/logistics/marketing) · service integration · forms stack")

add_activity("S18 — 'Design a cooperation'  ·  ~5 min",
    ["In pairs (3 min): you run a small Nepali fintech. Pick ONE rival or partner to cooperate with.",
     "Choose the FORM (joint platform / partnership / service integration) and the REASON (one of the 5).",
     "State what you'd still compete on afterwards.",
     "Take 3–4 answers aloud (2 min); check the reason and form are named explicitly."],
    "Good answer: integrate with ConnectIPS (joint platform) to share cost & grow the cashless market, partner with a courier for reach — but still compete on app UX and cashback. Reward naming FORM + REASON and what stays competitive (the S19 hook).",
    "ACTIVITY [~5 min].")
add_quiz("S18 — Quick Check  ·  ~5 min",
    [("Q1.  Nepali banks jointly building and funding ConnectIPS is cooperation via:","q"),
     ("a) a price war   b) ✅ a joint platform (shared rails)   c) an acquisition   d) advertising","a"),
     ("     Why: rivals share common payment infrastructure none would build alone — a joint platform.","o"),
     ("Q2.  'Grow the pie first, then compete for slices' means:","q"),
     ("a) never compete   b) ✅ enlarge the whole market together before fighting for share   c) merge   d) cut prices","a"),
     ("     Why: cooperation expands total demand first; firms compete for share of the bigger market after.","o"),
     ("Discussion: name a Nepali cooperation and its form (joint platform / partnership / integration).","o")],
    "QUIZ [~5 min]. Cement the 3 forms and the 'grow the pie' mindset — the bridge to co-opetition.")
add_summary("S18 · Summary  ·  [~2 min]",
    ["Cooperation = creating value together (rails, standards, data); digital encourages it via modularity, APIs, network effects, convenience.",
     "Five reasons: grow the market, share cost/risk, access capabilities, set standards, speed & reach ('grow the pie first').",
     "Three forms: joint platforms (shared rails), partnerships (co-brand/logistics/marketing), service integration."],
    "In a small market like Nepal, cooperation is often the only route to scale — which is why rivals share rails like ConnectIPS while still fighting for customers. That exact combination is the subject of the next session.",
    "S19 — the paradox resolved: co-opetition — cooperating and competing with the same firm at once.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S19
add_divider("Session 19 · Lecture hour 4 (of 10)","Co-opetition: Cooperate + Compete at Once",
    "eSewa and Nabil Bank need each other — the wallet needs the bank's accounts, the bank wants the wallet's reach — yet both chase the same customer's money. They cooperate and compete at the same time, with the same firm. That is co-opetition, and in layered digital markets it is the norm, not the exception.",
    "OPENING HOOK [~5 min]. Name the eSewa+Nabil paradox. Agenda: co-opetition = cooperate upstream + compete downstream (+ the Value-Net) -> why it's so common -> its benefits & risks.")

concept_understand("S19 · Concept 1 · [THEORY]","Co-opetition = Cooperate Upstream, Compete Downstream",
    "Co-opetition is cooperating and competing with the same firm at the same time. The pattern is UPSTREAM cooperation (shared technology, infrastructure, and standards — the 'pipes') and DOWNSTREAM competition (for customers, brand, and price — the 'product'). Brandenburger & Nalebuff's Value-Net names the players around a firm: customers, suppliers, competitors, and complementors — and shows a rival can be a complementor upstream while a competitor downstream.",
    ["Upstream (pipes): cooperate on shared rails, tech, and standards — cheaper and interoperable.",
     "Downstream (product): compete hard for the customer, the brand, and the price.",
     "Value-Net: customers + suppliers + competitors + complementors surround every firm.",
     "A rival can be a complementor (grows the market) AND a competitor (splits it) at once."],
    "s19_coopetition.png","Co-opetition = cooperate UPSTREAM (shared tech/rails) + compete DOWNSTREAM (customers/brand).",
    "~8 min. Use the diagram. Introduce the Value-Net LIGHTLY: the fresh framework naming complementors alongside competitors. Upstream/downstream is the exam line.")
add_examples_table("S19 · Concept 1 · examples","Cooperate upstream vs compete downstream",
    ["Case","Cooperate UPSTREAM (shared)","Compete DOWNSTREAM (for customers)"],
    [["eSewa & Khalti","Same ConnectIPS/QR rails","App UX, cashback, merchant deals"],
     ["Daraz & Pathao","Share delivery logistics","Pathao's own Foodmandu-style services"],
     ["Banks & ConnectIPS","Shared clearing/settlement","Interest rates, branches, own apps"],
     ["Apple & Samsung","Samsung supplies Apple chips/screens","Compete fiercely in phone sales"],
     ["Airlines (codeshare)","Share routes & booking systems","Compete on price & loyalty"],
     ["Google & Apple","Google pays to be default on iPhone","Android vs iOS ecosystems compete"]],
    per_page=6,widths=[1.6,2.5,2.9],fs=10.5,
    note="The consistent split: cooperate on the expensive shared 'pipes' (rails, chips, routes) that grow the whole market, then compete on the 'product' the customer actually chooses. That is co-opetition in one line.")
concept_apply("S19 · Concept 1 · [THEORY]","Co-opetition = Cooperate Upstream, Compete Downstream",
    "eSewa and Nabil Bank co-opete: upstream they cooperate — eSewa needs Nabil's banking rails and accounts, and both use ConnectIPS — while downstream they compete for the same customer's wallet share and daily transactions. Globally, Samsung sells Apple the screens and chips for iPhones (upstream) while battling Apple in phone sales (downstream). Cooperate on the pipes, compete for the customer.",
    "\"You either compete with a firm or cooperate with it — not both.\" Co-opetition is doing both at once with the SAME firm: cooperate upstream on shared tech/rails/standards, compete downstream for customers and brand. The Value-Net shows a rival can be a complementor (grows the pie) and a competitor (splits it) simultaneously.",
    "Co-opetition is cooperating and competing with the same firm at the same time: cooperate UPSTREAM on shared technology, infrastructure, and standards (the pipes), and compete DOWNSTREAM for customers, brand, and price (the product). Brandenburger & Nalebuff's Value-Net names the players around a firm — customers, suppliers, competitors, complementors — and shows a rival can be a complementor upstream and a competitor downstream (eSewa & Nabil; Samsung & Apple).",
    "co-opetition · cooperate upstream · compete downstream · Value-Net · complementor vs competitor")

concept_understand("S19 · Concept 2 · [THEORY]","Why Co-opetition Is So Common Online",
    "Co-opetition is common in digital markets because products are LAYERED and MODULAR: no single firm owns the whole stack (device, OS, network, payment, app), so firms must interconnect at some layers even while competing at others. Ecosystems, not lone products, win — a firm that cooperates to enrich a shared platform captures more value than one that walls itself off. Network effects reward shared standards, and specialisation means everyone depends on partners' pieces.",
    ["Layered products: no one owns device + OS + network + payment + app — you must interconnect.",
     "Ecosystems win: a rich shared platform beats an isolated product (complementors add value).",
     "Standards & network effects reward cooperating on the interface everyone uses.",
     "Specialisation: each firm is best at one layer, so it buys/partners for the rest."],
    None,"Common because products are layered/modular: no one owns the whole stack, and ecosystems beat isolated products.",
    "~6 min. Tie to S20's layered model coming next. The point: layered products FORCE some cooperation even among rivals.")
add_table_slide("S19 · Concept 2 · scaffolding","Why co-opetition happens — the forces",
    ["Force","Why it drives co-opetition","Example"],
    [["Layered products","No one owns the whole stack","Wallet needs bank + network + device"],
     ["Ecosystem advantage","Rich shared platform beats isolation","App stores enrich iOS/Android"],
     ["Standards & network effects","Shared interface grows all value","QR standard adopted by all wallets"],
     ["Specialisation","Each firm best at one layer","Daraz retails; Pathao delivers"]],
    per_page=4,widths=[1.9,2.7,2.5],fs=11,
    note="Because digital products are stacks of layers owned by different firms, interconnection is unavoidable — so rivals cooperate at some layers while competing at others. Co-opetition is the natural shape of a layered market (S20).")
concept_apply("S19 · Concept 2 · [THEORY]","Why Co-opetition Is So Common Online",
    "A Nepali wallet cannot function alone: it needs banks (accounts), telecoms (data/SMS), device makers (phones), and merchants — none of which it owns. So it cooperates across the stack while competing for the customer's daily use. Globally, Apple's App Store thrives because it lets even rival developers build on it — the ecosystem enriched by 'complementors' beats a walled-off product. Layered markets make co-opetition unavoidable.",
    "\"Firms should own their whole stack to avoid depending on rivals.\" In layered digital markets no one can own device + OS + network + payment + app, and a rich ecosystem (with complementors, even rivals) beats an isolated product. Interconnection is unavoidable, so cooperating at some layers while competing at others is the rational default.",
    "Co-opetition is common online because digital products are layered and modular: no single firm owns the whole stack (device, OS, network, payment, app), so firms must interconnect at some layers while competing at others. Ecosystems beat isolated products — cooperating to enrich a shared platform (with complementors, even rivals) captures more value than walling off. Network effects reward shared standards, and specialisation makes every firm depend on partners' pieces.",
    "layered products · ecosystems win · shared standards · specialisation · interconnection unavoidable")

concept_understand("S19 · Concept 3 · [THEORY]","Benefits & Risks of Co-opetition",
    "Co-opetition has real benefits: it grows the whole market, shares cost and risk, speeds innovation, and lets small firms reach scale via shared rails. But it carries risks: DEPENDENCY (you rely on a rival's infrastructure), POWER IMBALANCE (the bigger partner sets terms), LOCK-IN (hard to leave a shared standard), knowledge/data LEAKAGE (a partner learns your moves), and conflict when cooperation and competition collide. The skill is deciding which layers to share and which to guard.",
    ["Benefits: bigger market, shared cost/risk, faster innovation, scale for small players.",
     "Risks: dependency on a rival's rails; power imbalance (big partner dictates terms).",
     "Risks: lock-in to a shared standard; data/knowledge leakage to the partner-rival.",
     "The skill: choose which layers to cooperate on (pipes) and which to protect (data, customer)."],
    None,"Benefits (bigger market, shared cost, speed, scale) vs risks (dependency, power imbalance, lock-in, leakage).",
    "~7 min. Balance: co-opetition is powerful but not free. Nepal's small wallets gain scale via shared rails yet depend on banks that could squeeze them.")
add_comparison_table("S19 · Concept 3 · comparison","Co-opetition — benefits vs risks",
    ["Dimension","Benefit","Risk"],
    [["Market size","Grows the whole pie","Rival grows too — you may lose share"],
     ["Cost & risk","Shared, so affordable","Dependency on a rival's infrastructure"],
     ["Innovation","Faster via shared standards","Lock-in to a standard you can't leave"],
     ["Bargaining","Small firm gains scale","Power imbalance — big partner sets terms"],
     ["Information","Learn from the partner","Data/knowledge leaks to the rival"]],
    per_page=5,widths=[1.6,2.6,2.7],fs=11,
    note="Every benefit has a shadow risk. The strategic question is WHICH layers to share (the expensive pipes) and WHICH to guard (your data and the customer relationship — the control points of S25).")
concept_apply("S19 · Concept 3 · [THEORY]","Benefits & Risks of Co-opetition",
    "A small Nepali wallet gains huge benefit from shared ConnectIPS/QR rails — instant national reach it could never build alone. But the risk is dependency and power imbalance: it relies on banks that also run their own apps and could change terms or fees. The wallet's skill is cooperating on the shared rails (cheap, necessary) while guarding its own customer data and app experience — the assets that keep it independent.",
    "\"Co-opetition is win-win with no downside.\" Cooperating with a rival creates dependency, power imbalance, lock-in, and data leakage — the partner can squeeze or out-learn you. The benefits (scale, shared cost, speed) are real, but so are the risks; the skill is choosing which layers to share and which to protect.",
    "Co-opetition's benefits: it grows the whole market, shares cost and risk, speeds innovation via shared standards, and gives small firms scale through shared rails. Its risks: dependency on a rival's infrastructure, power imbalance (the bigger partner dictates terms), lock-in to a shared standard, and data/knowledge leakage. The skill is deciding which layers to cooperate on (the expensive pipes) and which to guard (data, the customer relationship).",
    "benefits: bigger market/shared cost/speed/scale · risks: dependency/power imbalance/lock-in/leakage · guard control points")

add_activity("S19 — 'Split the layers'  ·  ~5 min",
    ["In pairs (3 min): pick two Nepali rivals (eSewa & Khalti, Daraz & Pathao, two banks).",
     "List what they cooperate on UPSTREAM and what they compete on DOWNSTREAM.",
     "Name one benefit and one risk of that co-opetition for the smaller firm.",
     "Take 3–4 answers aloud (2 min); check the upstream/downstream split is explicit."],
    "Good answer (eSewa & Khalti): cooperate on ConnectIPS/QR rails (upstream), compete on app UX & cashback (downstream); benefit = national reach cheaply, risk = dependency on bank rails/power imbalance. Reward the explicit split + one benefit/risk.",
    "ACTIVITY [~5 min].")
add_quiz("S19 — Quick Check  ·  ~5 min",
    [("Q1.  Co-opetition typically means firms:","q"),
     ("a) compete on everything   b) cooperate on everything   c) merge   d) ✅ cooperate upstream (tech/rails) and compete downstream (customers)","a"),
     ("     Why: shared infrastructure/standards upstream; competition for customers and brand downstream.","o"),
     ("Q2.  A key RISK of co-opetition for a small firm is:","q"),
     ("a) lower costs   b) ✅ dependency & power imbalance vs the larger partner   c) more customers   d) faster innovation","a"),
     ("     Why: relying on a rival's rails creates dependency; the bigger partner can set terms.","o"),
     ("Discussion: name a Nepali co-opetition and split its upstream cooperation vs downstream competition.","o")],
    "QUIZ [~5 min]. Nail the upstream/compete-downstream line and one real benefit + risk.")
add_summary("S19 · Summary  ·  [~2 min]",
    ["Co-opetition = cooperate + compete with the same firm: cooperate UPSTREAM (tech/rails/standards), compete DOWNSTREAM (customers/brand). Value-Net adds complementors.",
     "Common online because products are layered/modular — no one owns the whole stack; ecosystems beat isolated products.",
     "Benefits (bigger market, shared cost, speed, scale) come with risks (dependency, power imbalance, lock-in, data leakage)."],
    "Co-opetition is how Nepal's small digital firms survive giants — sharing rails to reach scale while guarding the customer. Deciding which layers to share and which to protect is a strategic choice we'll formalise as 'control points' in S25.",
    "S20 — WHY 'upstream' and 'downstream' exist at all: the layered internet model and layer power.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S20
add_divider("Session 20 · Lecture hour 5 (of 10)","The Layered Internet Model",
    "When you watch a video on Foodmandu's app, you touch an APPLICATION — but under it sits a PLATFORM (Android, cloud), and under that the INFRASTRUCTURE (Ncell's network, data centres, fibre). You see the top; the power often sits at the bottom. Why does controlling a lower layer give power over everything above it?",
    "OPENING HOOK [~5 min]. Trace one Netflix stream down through the layers. Agenda: the 3 layers (+ user) -> value flows bottom-up -> power: control lower = power over higher.")

concept_understand("S20 · Concept 1 · [THEORY]","The Three Layers (+ the User)",
    "The layered internet model (a business/economic view, not the technical OSI/TCP-IP stack) has three layers plus the user. INFRASTRUCTURE — the technical base: fibre, data centres, connectivity, devices, cloud (NTC/Ncell, AWS). PLATFORM — the capability layer: operating systems, payment rails, cloud services, app stores (Android/iOS, eSewa/Fonepay, AWS). APPLICATION — the experience layer: the apps people actually use (Daraz, Foodmandu, Netflix). The USER sits on top, consuming the experience.",
    ["Infrastructure = the technical base (networks, data centres, devices, cloud).",
     "Platform = the capability layer (OS, payment rails, cloud services, app stores).",
     "Application = the experience layer (the apps users open — Daraz, Netflix).",
     "This is the ECONOMIC 3-layer view, distinct from the technical OSI/TCP-IP layers."],
    "s20_layers.png","Three layers: Infrastructure (base) -> Platform (capability) -> Application (experience) -> User.",
    "~7 min. Use the stacked diagram. Flag the divergence: this is the business framing, NOT the 7-layer OSI model — students confuse them.")
add_examples_table("S20 · Concept 1 · examples","The 3 layers — role, global vs Nepal example",
    ["Layer","Role","Global example","Nepal example"],
    [["Infrastructure","Technical base: network, data centre, device","AWS, Google fibre, cables","NTC/Ncell, data centres, ISPs"],
     ["Platform","Capability: OS, payment rails, cloud, app store","Android/iOS, AWS, Visa","eSewa/Fonepay, ConnectIPS, Android"],
     ["Application","Experience: the app users open","Netflix, Uber, Amazon app","Daraz, Foodmandu, Pathao app"],
     ["User","Consumes the experience","People, firms, government","Nepali consumers & businesses"]],
    per_page=4,widths=[1.4,2.4,2.3,2.4],fs=10.5,
    note="Read any digital service top-to-bottom and you'll find all three layers. Note Nepal mostly owns the APPLICATION layer while depending on foreign PLATFORM and INFRASTRUCTURE (Android, AWS) — the structural-dependence point of Concept 3.")
concept_apply("S20 · Concept 1 · [THEORY]","The Three Layers (+ the User)",
    "Trace a Foodmandu order: you use the APPLICATION (Foodmandu app), which runs on a PLATFORM (Android/iOS, cloud hosting, a payment rail like Khalti/Fonepay), which sits on INFRASTRUCTURE (Ncell/NTC data, servers, fibre). You, the USER, only see the top layer. Netflix is the same: app on top, AWS/Android platform beneath, global fibre and data centres at the base.",
    "\"The internet is one flat thing.\" It is a STACK of layers: infrastructure (base), platform (capability), application (experience), with the user on top. And note this is the ECONOMIC layered model — not the technical 7-layer OSI/TCP-IP stack, which students often confuse it with. The business layers are about who owns value and power, not protocols.",
    "The layered internet model (a business/economic view, distinct from the technical OSI/TCP-IP stack) has three layers plus the user: infrastructure (the technical base — fibre, data centres, connectivity, devices, cloud), platform (the capability layer — OS, payment rails, cloud services, app stores), and application (the experience layer — the apps people use). The user sits on top, consuming the experience. Every digital service can be read down through all three.",
    "layered internet model · infrastructure · platform · application · user · business (not OSI) view")

concept_understand("S20 · Concept 2 · [THEORY]","Value Flows Bottom-Up",
    "Value is built from the bottom up: each layer adds value to the one below it. Infrastructure provides raw TECHNICAL capability (bandwidth, compute, connectivity). The platform turns that into usable CAPABILITY (an OS, a payment rail, cloud services others can build on). The application turns capability into EXPERIENCE (a service the user enjoys). So raw fibre becomes cloud compute becomes a streaming app becomes a movie night — technical to capability to experience.",
    ["Infrastructure -> technical value (bandwidth, compute, connectivity).",
     "Platform -> capability value (usable services others build on).",
     "Application -> experience value (what the user actually enjoys).",
     "Each layer is worthless to the user without the layers below carrying it up."],
    None,"Value flows UP: technical (infra) -> capability (platform) -> experience (application).",
    "~7 min. Use a worked trace (banking or Netflix). The bottom-up flow sets up why the bottom holds power (Concept 3).")
add_table_slide("S20 · Concept 2 · scaffolding","Value type by layer — a worked trace",
    ["Layer","Value type","Banking example","Netflix example"],
    [["Infrastructure","Technical (compute, network)","Data centre, bank network","AWS servers, global fibre"],
     ["Platform","Capability (usable service)","ConnectIPS rails, core banking","AWS services, Android/iOS"],
     ["Application","Experience (what user enjoys)","Your bank's mobile app","Netflix app & recommendations"],
     ["User","Consumption","You transfer money in seconds","You watch a film instantly"]],
    per_page=4,widths=[1.5,2.1,2.4,2.5],fs=10.5,
    note="Trace any service down and value climbs back up: technical capacity becomes a usable platform becomes an experience. The user sees only the experience but relies on every layer beneath.")
concept_apply("S20 · Concept 2 · [THEORY]","Value Flows Bottom-Up",
    "Your bank's app (application) gives you the EXPERIENCE of transferring money in seconds. That rests on ConnectIPS and core-banking CAPABILITY (platform), which rests on data centres and the bank network's TECHNICAL capacity (infrastructure). Netflix is identical: AWS fibre and servers (technical) become AWS/Android services (capability) become the Netflix app (experience). Value is assembled bottom-up, layer by layer.",
    "\"The app creates all the value.\" The app only delivers the EXPERIENCE; the value beneath it — capability from the platform, technical capacity from infrastructure — is what makes the experience possible. Value flows bottom-up (technical -> capability -> experience); the visible top layer sits on invisible value from below.",
    "Value flows bottom-up: each layer adds value to the one below. Infrastructure provides technical value (bandwidth, compute, connectivity); the platform turns it into capability value (usable services others build on — OS, payment rails, cloud); the application turns capability into experience value (the service the user enjoys). Raw fibre becomes cloud compute becomes a streaming app becomes a movie night — technical to capability to experience.",
    "value flows up · technical -> capability -> experience · each layer adds to the one below")

concept_understand("S20 · Concept 3 · [THEORY]","Layer Power: Control Lower = Power Over Higher",
    "While value flows UP, power flows DOWN: whoever controls a lower layer holds power over everything above it. An app depends on the platform (app-store rules, payment cut), and the platform depends on infrastructure. Apple's App Store (platform) can take ~30% from any app; a cloud provider can raise prices on everyone hosted on it. This is why Nepal's structural dependence matters: Nepali firms own the APPLICATION layer but rent the PLATFORM and INFRASTRUCTURE (Android, AWS, foreign cloud) — so foreign firms hold power over local apps.",
    ["Value flows up, but POWER flows down — the lower layer sets terms for the higher.",
     "App-store cut, cloud pricing, OS rules: the platform controls the apps on it.",
     "Owning infrastructure/platform is the deepest moat — hardest to replace.",
     "Nepal dependence: local apps, foreign platform & infrastructure = power sits abroad."],
    None,"Power flows DOWN: control a lower layer (platform/infra) and you hold power over every layer above.",
    "~7 min. This is the strategic punchline of the unit — links to co-opetition (S19) and control points (S25). Nepal owns apps but rents the layers beneath.")
add_table_slide("S20 · Concept 3 · scaffolding","Benefits of layered architecture (and the power it hides)",
    ["Benefit","What it enables","But note the power"],
    [["Specialisation","Each firm masters one layer","Layer owners set terms for others"],
     ["Modularity / reuse","Build apps fast on shared platforms","App depends on platform's rules"],
     ["Innovation at the top","Anyone can launch an app","Platform can copy or tax the app"],
     ["Scalability","Cloud scales apps instantly","Cloud provider controls pricing"],
     ["Lower entry cost","No need to build infra","Deep dependence on infra/platform owner"]],
    per_page=5,widths=[1.7,2.5,2.6],fs=11,
    note="Layering is hugely beneficial — it lets a Nepali startup launch an app without building fibre or a cloud. But every benefit comes with dependence: whoever owns the layer you build on holds power over you (the App Store's 30%).")
concept_apply("S20 · Concept 3 · [THEORY]","Layer Power: Control Lower = Power Over Higher",
    "A Nepali app maker owns the APPLICATION but rents everything below: it ships through Apple/Google's app stores (which can take a cut or set rules), hosts on AWS/foreign cloud (which sets prices), and runs on Android/iOS. So power over a local app sits with foreign platform and infrastructure owners — the App Store's ~30% cut is felt by any Nepali developer. This is why owning a lower layer (or a control point, S25) is the real strategic prize.",
    "\"The app on top is the most powerful part.\" Value flows up but POWER flows down: the platform and infrastructure beneath set the terms (app-store cut, cloud pricing, OS rules). The visible top layer is often the least powerful — which is why Nepal owning apps but renting the layers beneath leaves real power abroad.",
    "While value flows up, power flows down: whoever controls a lower layer holds power over everything above it. An app depends on the platform (app-store rules, ~30% cut), and the platform depends on infrastructure (cloud pricing). Owning the platform or infrastructure is the deepest moat. Nepal's structural dependence follows: local firms own the application layer but rent the platform and infrastructure (Android, AWS), so foreign firms hold power over Nepali apps.",
    "power flows down · lower layer controls higher · App Store 30% · structural dependence · own the layer beneath")

add_activity("S20 — 'Trace the stack'  ·  ~5 min",
    ["In pairs (3 min): pick a Nepali service (your bank app, Daraz, Foodmandu, Netflix in Nepal).",
     "Name what sits at each layer: infrastructure, platform, application, user.",
     "Identify which layers are Nepali-owned and which are foreign — where does power sit?",
     "Take 3–4 answers aloud (2 min); highlight the app-owned-locally, platform-rented pattern."],
    "Good answer (Daraz): app = Daraz (application), platform = Android/iOS + cloud + Fonepay rails, infrastructure = NTC/Ncell + foreign cloud + devices. Nepal owns the app; platform/infra largely foreign -> power sits abroad. Reward the ownership/power observation.",
    "ACTIVITY [~5 min].")
add_quiz("S20 — Quick Check  ·  ~5 min",
    [("Q1.  Cloud, data centres, connectivity and devices belong to which layer?","q"),
     ("a) application   b) ✅ infrastructure   c) user   d) payment","a"),
     ("     Why: infrastructure is the technical base — networks, data centres, devices, cloud.","o"),
     ("Q2.  'Control of a lower layer gives power over higher layers' is shown by:","q"),
     ("a) users choosing apps   b) ✅ an app store taking a ~30% cut from every app   c) fast internet   d) free apps","a"),
     ("     Why: the platform (app store) beneath the app sets terms the app must accept — power flows down.","o"),
     ("Discussion: for a Nepali service, which layers are local and which foreign — where's the power?","o")],
    "QUIZ [~5 min]. Cement the 3 layers, bottom-up value, and top-down power — plus Nepal's dependence.")
add_summary("S20 · Summary  ·  [~2 min]",
    ["Three layers (+ user): infrastructure (technical base), platform (capability), application (experience) — the business, not OSI, view.",
     "Value flows bottom-up: technical -> capability -> experience; each layer adds to the one below.",
     "Power flows top-down: control a lower layer and you hold power over higher ones — Nepal owns apps but rents platform & infrastructure."],
    "The layered model explains WHY co-opetition happens (S19) and where real power lives — and it sets up S25's 'control points'. For Nepal, it's a strategic warning: owning apps while renting the layers beneath leaves power (and profit) abroad.",
    "S21 — what drives NEW value in these markets: digital innovation, and innovation vs invention.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S21
add_divider("Session 21 · Lecture hour 6 (of 10)","Digital Innovation",
    "eSewa didn't invent the internet, smartphones, or QR codes — yet it changed how millions of Nepalis pay. Meanwhile, brilliant inventions sit unused in labs. What is the difference between INVENTING something and INNOVATING with it — and why do cheap, 'good-enough' newcomers so often topple better-funded incumbents?",
    "OPENING HOOK [~5 min]. Contrast an unused lab invention with eSewa's impact. Agenda: definition + innovation != invention + sustaining vs disruptive -> the 6 types -> enablers, process & Nepal challenges.")

concept_understand("S21 · Concept 1 · [THEORY]","Innovation != Invention; Sustaining vs Disruptive",
    "Digital innovation is creating new value — in products, processes, services, or business models — using digital technology. Crucially, INNOVATION != INVENTION: invention is creating something new (a technology); innovation is turning an idea into VALUE that people actually use. Innovation also comes in two strategic kinds: SUSTAINING (improving an existing product for existing customers — a better camera each year) and DISRUPTIVE (a cheaper, simpler, 'good-enough' offering that enters at the low end and rises to overtake incumbents — Christensen).",
    ["Invention = create a new technology; innovation = create VALUE people use from it.",
     "Innovation can be about context/business model, not just new technology.",
     "Sustaining: improve for existing customers (incremental or radical, but same market).",
     "Disruptive: enter cheap & 'good enough' at the bottom, then climb to overtake the incumbent."],
    "s21_innovation.png","Innovation != invention (value, not just new tech). Sustaining improves; disruptive enters low, then overtakes.",
    "~8 min. Use the disruptive-innovation curve. The exam line: innovation = value from an idea; disruptive = low-end entry that rises. Add Christensen lightly.")
add_comparison_table("S21 · Concept 1 · comparison","Sustaining vs disruptive innovation",
    ["Dimension","Sustaining innovation","Disruptive innovation"],
    [["Aim","Improve for existing customers","Serve overlooked / new customers"],
     ["Starting point","Better than current product","Simpler, cheaper, 'good enough'"],
     ["Who does it","Usually incumbents","Usually new entrants"],
     ["Price","Same or higher","Lower / more accessible"],
     ["Trajectory","Steady improvement","Enters low, then climbs to overtake"],
     ["Example","Yearly phone camera upgrade","eSewa vs bank queues; Netflix vs cable"]],
    per_page=6,widths=[1.6,2.6,2.7],fs=11,
    note="Incumbents win at sustaining innovation but are blindsided by disruption because the newcomer looks too cheap/basic to matter — until it climbs. This is why 'good enough & cheap' beats 'better & pricey' in digital markets.")
concept_apply("S21 · Concept 1 · [THEORY]","Innovation != Invention; Sustaining vs Disruptive",
    "eSewa invented nothing new technically — QR, internet, and phones already existed — but it INNOVATED by turning them into a payment service millions use, creating real value. It was also DISRUPTIVE: a simpler, cheaper alternative to bank queues that started with small top-ups and bills, then climbed to serious payments. Banks did sustaining innovation (better branch apps) and were caught off guard by the 'good-enough' wallet.",
    "\"Innovation means inventing brand-new technology.\" Innovation is creating VALUE people use, which often reuses existing tech in a new context or business model — eSewa invented nothing but changed everything. And the dangerous kind is disruptive: a cheap, 'good-enough' entrant that looks unthreatening until it climbs and overtakes the incumbent.",
    "Digital innovation is creating new value — in products, processes, services, or business models — using digital technology. Innovation is not invention: invention creates a new technology, while innovation turns an idea into value people actually use (often reusing existing tech). It comes in two strategic kinds: sustaining (improving an existing product for existing customers) and disruptive (a cheaper, simpler, 'good-enough' entrant that starts at the low end and rises to overtake incumbents — Christensen). eSewa is both an innovation and a disruptor.",
    "innovation != invention · value not just tech · sustaining vs disruptive · low-end entry · Christensen")

concept_understand("S21 · Concept 2 · [THEORY]","The Six Types of Digital Innovation",
    "Digital innovation shows up in six types. PRODUCT (a new/improved offering — a smart device). PROCESS (a better way of doing work — automated warehousing). BUSINESS-MODEL (a new way to create/capture value — subscription instead of sale). SERVICE (a new service experience — online support, streaming). MARKETING (new ways to reach/engage customers — social, influencer). ORGANIZATIONAL (new internal structures/culture — agile teams, remote work). The most powerful digital shifts are usually business-model innovations, not just product ones.",
    ["Product & process: what you offer, and how you make/deliver it.",
     "Business-model & service: how you create/capture value, and the experience delivered.",
     "Marketing & organizational: how you reach customers, and how you're structured inside.",
     "Business-model innovation often matters most digitally (subscription, platform, freemium)."],
    None,"Six types: product · process · business-model · service · marketing · organizational.",
    "~7 min. Stress that business-model innovation (S22) is often the biggest lever — Netflix's shift beat any single product feature.")
add_examples_table("S21 · Concept 2 · examples","The 6 types of digital innovation — Nepal & global",
    ["Type","What changes","Example"],
    [["Product","A new/improved offering","Smart devices; a new app feature"],
     ["Process","A better way of working","Daraz automated warehousing; e-invoicing"],
     ["Business-model","New way to create/capture value","Netflix subscription; eSewa wallet model"],
     ["Service","A new service experience","Online banking; streaming; e-tickets"],
     ["Marketing","New ways to reach customers","TikTok/influencer marketing; app cashback"],
     ["Organizational","New internal structure/culture","Agile teams; remote work; digital HR"]],
    per_page=6,widths=[1.7,2.4,2.9],fs=10.5,
    note="A single company often innovates on several types at once. The type that reshapes an industry is usually business-model innovation (S22) — changing HOW value is earned, not just WHAT is sold.")
concept_apply("S21 · Concept 2 · [THEORY]","The Six Types of Digital Innovation",
    "Daraz shows several types: automated warehousing (process), app features and recommendations (product), a marketplace-commission model (business-model), buyer protection & returns (service), festival cashback campaigns (marketing), and agile internal teams (organizational). The biggest lever, though, was business-model innovation — the marketplace model itself — not any single feature. Netflix likewise won on its subscription business model, not one product tweak.",
    "\"Innovation just means new products/features.\" Product is only one of six types — process, business-model, service, marketing, and organizational innovation matter too, and business-model innovation often reshapes whole industries (subscription, platform). Focusing only on product features misses the innovations that actually move markets.",
    "Digital innovation appears in six types: product (a new/improved offering), process (a better way of working), business-model (a new way to create/capture value), service (a new service experience), marketing (new ways to reach customers), and organizational (new internal structure/culture). A firm often innovates on several at once, but the most powerful digital shifts are usually business-model innovations (subscription, platform, freemium) rather than single product features.",
    "product · process · business-model · service · marketing · organizational · business-model matters most")

concept_understand("S21 · Concept 3 · [THEORY]","Enablers, the Process & Nepal's Challenges",
    "Six technologies enable most digital innovation: AI, IoT, cloud, big data, AR, and VR. The innovation PROCESS runs ideation (spot a problem/idea) -> MVP (build a minimum viable product to test) -> scale (grow what works). But innovation faces challenges — especially in Nepal: limited funding/venture capital, small market size, talent and skills gaps, weak digital infrastructure outside cities, regulatory uncertainty, and low digital/financial literacy. Innovation is about CONTEXT, not just technology — an idea must fit Nepal's realities.",
    ["Enablers: AI, IoT, cloud, big data, AR, VR — the toolkit of digital innovation.",
     "Process: ideation -> MVP (test cheaply) -> scale (grow what works).",
     "Nepal challenges: funding, small market, talent gap, weak rural infra, regulation, literacy.",
     "Innovation is about CONTEXT — fitting the idea to local realities, not copying Silicon Valley."],
    None,"Enablers: AI/IoT/cloud/big data/AR/VR. Process: ideation -> MVP -> scale. Nepal: funding, market, talent, infra, regulation.",
    "~7 min. 'Innovation is about context, not just technology.' Nepal fintech/agri-tech succeed by fitting local realities, not importing models wholesale.")
add_examples_table("S21 · Concept 3 · examples","Innovation challenges — general vs Nepal-specific",
    ["Challenge","General","Nepal-specific angle"],
    [["Funding","Scaling needs capital","Thin VC/angel ecosystem; hard to raise"],
     ["Market size","Need enough users","Small population; low per-capita spend"],
     ["Talent","Skilled builders scarce","Brain-drain of engineers abroad"],
     ["Infrastructure","Reliable connectivity/power","Weak rural internet & power outages"],
     ["Regulation","Rules lag innovation","Unclear fintech/data rules; slow approvals"],
     ["Literacy","Users must adopt","Low digital/financial literacy outside cities"]],
    per_page=6,widths=[1.6,2.3,3.0],fs=10.5,
    note="Nepal's fintech (eSewa/Khalti) and agri-tech successes worked by fitting the LOCAL context — solving a real Nepali problem cheaply — rather than importing a Silicon Valley model. Innovation is context, not just technology.")
concept_apply("S21 · Concept 3 · [THEORY]","Enablers, the Process & Nepal's Challenges",
    "A Nepali agri-tech startup might use cloud + big data + mobile (enablers) to connect farmers to buyers. It follows the process: ideation (farmers get poor prices) -> MVP (a simple SMS/app price service in one district) -> scale. But it hits Nepal's challenges — thin funding, low rural connectivity, digital literacy. The winners fit the CONTEXT: a lightweight, SMS-friendly, cash-aware design beats a data-heavy app copied from abroad.",
    "\"With the right technology, any innovation will succeed.\" Technology is only the enabler; success depends on CONTEXT — funding, market size, talent, infrastructure, regulation, and literacy. In Nepal, a 'lower-tech' solution that fits local realities (SMS, cash-aware, offline-tolerant) often beats a sophisticated one copied from Silicon Valley.",
    "Six technologies enable digital innovation: AI, IoT, cloud, big data, AR, and VR. The process runs ideation -> MVP (test cheaply) -> scale (grow what works). Innovation faces challenges, sharpened in Nepal: limited funding, small market, talent/brain-drain, weak rural infrastructure, regulatory uncertainty, and low digital/financial literacy. Innovation is about context, not just technology — Nepal's fintech and agri-tech win by fitting local realities, not importing models wholesale.",
    "enablers: AI/IoT/cloud/big data/AR/VR · ideation -> MVP -> scale · Nepal challenges · context over technology")

add_activity("S21 — 'Pitch a Nepali innovation'  ·  ~5 min",
    ["In pairs (3 min): propose one digital innovation for a real Nepali problem (agriculture, health, transport).",
     "Name its TYPE (product/process/business-model/…), its ENABLER tech, and whether it's sustaining or disruptive.",
     "Name the biggest Nepal-specific CHALLENGE it must overcome.",
     "Take 3–4 answers aloud (2 min); reward context-fit over tech sophistication."],
    "Good pitch: an SMS-based crop-price service = service + business-model innovation, enabler = cloud/big data, disruptive (cheap, good-enough), biggest challenge = rural literacy/connectivity. Reward naming type + enabler + sustaining/disruptive + a real local challenge.",
    "ACTIVITY [~5 min].")
add_quiz("S21 — Quick Check  ·  ~5 min",
    [("Q1.  'Innovation is not invention' means innovation is about:","q"),
     ("a) ✅ creating value people use from an idea, not just inventing the tech   b) patents only   c) pure lab research   d) copying rivals","a"),
     ("     Why: invention creates a technology; innovation turns it into value people actually use.","o"),
     ("Q2.  A cheaper, 'good-enough' newcomer that enters low and rises to overtake incumbents is:","q"),
     ("a) sustaining innovation   b) ✅ disruptive innovation   c) invention   d) marketing innovation","a"),
     ("     Why: disruptive innovation enters at the low end and climbs to displace better, pricier incumbents.","o"),
     ("Discussion: name a Nepali innovation — its type, and whether it is sustaining or disruptive.","o")],
    "QUIZ [~5 min]. Nail innovation != invention and sustaining vs disruptive.")
add_summary("S21 · Summary  ·  [~2 min]",
    ["Digital innovation = creating value with digital tech; innovation != invention (value, not just new tech). Sustaining improves; disruptive enters cheap & rises.",
     "Six types: product, process, business-model, service, marketing, organizational — business-model innovation matters most.",
     "Enablers: AI/IoT/cloud/big data/AR/VR; process ideation -> MVP -> scale; Nepal challenges make CONTEXT decisive."],
    "Innovation is how a Nepali startup can beat a giant without out-spending it — by fitting the local context and disrupting from below. The most powerful kind, business-model innovation, is exactly the subject of the next session.",
    "S22 — the innovation that reshapes markets: digital business models and the value triad.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S22
add_divider("Session 22 · Lecture hour 7 (of 10)","Digital Business Models",
    "Netflix charges a flat monthly fee; Google is free but sells ads; Daraz takes a cut of each sale; Spotify gives you free-with-ads or paid. Same internet, wildly different ways to make money. A business model is the answer to one question: how do you CREATE, DELIVER, and CAPTURE value? Let's map the ten ways digital firms do it.",
    "OPENING HOOK [~5 min]. List four firms' money logic. Agenda: the value triad (create/deliver/capture) -> the 10 model types (part 1) -> the 10 model types (part 2) + hybrids.")

concept_understand("S22 · Concept 1 · [THEORY]","The Value Triad: Create, Deliver, Capture",
    "A business model describes how a firm creates, delivers, and captures value. CREATE value: what problem you solve and for whom (the value proposition). DELIVER value: how you get it to customers (channels, platform, logistics). CAPTURE value: how you make money from it (the revenue mechanism — subscription, commission, ads). Many digital firms are brilliant at creating and delivering value but must think hard about capture — which is why 'free' products (Unit 2) still need a money side.",
    ["Create: the value proposition — the problem solved and for whom.",
     "Deliver: channels, platform, and logistics that get value to the user.",
     "Capture: the revenue mechanism — how the created value turns into money.",
     "Digital splits create/deliver (easy, cheap) from capture (the hard design choice)."],
    None,"Business model = how you CREATE (proposition) + DELIVER (channels) + CAPTURE (revenue) value.",
    "~7 min. The triad frames all 10 models: they differ mainly in the CAPTURE mechanism. Cross-ref Unit 2 two-sided pricing for capture on 'free' products.")
add_table_slide("S22 · Concept 1 · scaffolding","The value triad — with a Nepal example",
    ["Element","The question","Foodmandu example"],
    [["Create value","What problem, for whom?","Get restaurant food to busy customers"],
     ["Deliver value","How does it reach the user?","App + rider network + live tracking"],
     ["Capture value","How is money made?","Commission per order + delivery fee"]],
    per_page=3,widths=[1.6,2.4,3.0],fs=11,
    note="Every business model answers these three. Most digital firms find create and deliver relatively easy (software scales); the hard, distinctive choice is CAPTURE — which revenue mechanism, and from which side (Unit 2).")
concept_apply("S22 · Concept 1 · [THEORY]","The Value Triad: Create, Deliver, Capture",
    "Foodmandu CREATES value by getting restaurant meals to busy customers, DELIVERS it via its app and rider network with live tracking, and CAPTURES it through a commission per order plus a delivery fee. Netflix creates value with content, delivers via streaming, and captures via a flat subscription. The triad shows why the same 'deliver food/video' idea can be monetised in very different ways — capture is the design choice.",
    "\"A business model is just how a company makes money.\" Making money is only the CAPTURE part. A full model also covers how value is CREATED (the proposition) and DELIVERED (channels/platform). Two firms can create and deliver the same value yet capture it differently (commission vs subscription vs ads) — capture is where models diverge.",
    "A business model describes how a firm creates, delivers, and captures value. Create = the value proposition (what problem, for whom). Deliver = the channels, platform, and logistics that get value to the customer. Capture = the revenue mechanism (subscription, commission, ads). Digital firms often find create and deliver easy but must carefully design capture — which is why even 'free' products need a money side (Unit 2). Foodmandu: create (food to customers), deliver (app + riders), capture (commission + fee).",
    "value triad · create (proposition) · deliver (channels) · capture (revenue) · capture is the design choice")

concept_understand("S22 · Concept 2 · [THEORY]","The 10 Business Models — Part 1",
    "Digital firms mostly use ten model types. Part 1 covers the first five. PLATFORM/MARKETPLACE-adjacent models begin here: (1) PLATFORM — connect groups and take a cut (Daraz, Pathao). (2) SUBSCRIPTION — recurring fee for ongoing access (Netflix, Spotify Premium). (3) FREEMIUM — free basic tier, pay to upgrade (Spotify free vs paid, Zoom). (4) SHARING/ACCESS — pay to use, not own, an asset (Airbnb, ride/asset sharing). (5) MARKETPLACE — match many buyers and sellers, earn commission (Hamrobazar, eBay).",
    ["Platform: connect interdependent groups, capture via commission/fees (Unit 2 MSP).",
     "Subscription: recurring fee for continuous access — predictable revenue.",
     "Freemium: free base tier converts a fraction to paid — reach then upsell.",
     "Sharing & marketplace: monetise access to assets / matching many sides."],
    None,"Part 1: platform · subscription · freemium · sharing/access · marketplace.",
    "~7 min. Use the big table (paginated). Cross-ref Unit 2: platform & marketplace are MSPs; freemium/subscription are capture choices.")
concept_apply("S22 · Concept 2 · [THEORY]","The 10 Business Models — Part 1",
    "In Nepal: Daraz runs a PLATFORM/MARKETPLACE model (commission on sales), a gym app might use SUBSCRIPTION (monthly fee), a learning app uses FREEMIUM (free lessons, pay to unlock), and InDrive uses a SHARING/access model (pay to use a ride, not own the car). Each solves value capture differently — the same digital reach, monetised through commission, recurring fee, upsell, or usage.",
    "\"Every online business just sells things (e-commerce).\" E-commerce is only one of ten models. Platform, subscription, freemium, sharing, and marketplace all capture value differently — via commission, recurring fees, upsell, or access — and most successful digital firms combine several rather than simply 'selling things'.",
    "Digital firms use ten model types; part 1 covers five. Platform: connect groups and take a cut (Daraz, Pathao) — an MSP (Unit 2). Subscription: recurring fee for ongoing access (Netflix, Spotify Premium). Freemium: free basic tier, pay to upgrade (Spotify, Zoom). Sharing/access: pay to use, not own, an asset (Airbnb, ride sharing). Marketplace: match many buyers and sellers for commission (Hamrobazar, eBay). Each captures value through a different mechanism.",
    "platform · subscription · freemium · sharing/access · marketplace · different capture mechanisms")
add_examples_table("S22 · Concepts 2–3 · examples","The 10 digital business models — revenue mechanism & example",
    ["Model","How it captures value","Example (Nepal / global)"],
    [["Platform","Commission/fee on interactions","Pathao, Daraz / Uber, Airbnb"],
     ["Subscription","Recurring fee for access","Netflix, Spotify Premium, SaaS"],
     ["Freemium","Free base, pay to upgrade","Spotify free/paid, Zoom, LinkedIn"],
     ["Sharing / access","Pay to use, not own","Airbnb, InDrive, asset sharing"],
     ["Marketplace","Commission on matched trades","Hamrobazar, eBay, Etsy"],
     ["Advertising","Sell user attention to advertisers","Google, Meta, YouTube, TikTok"],
     ["E-commerce","Margin on goods sold online","Sastodeal, Amazon retail, brand stores"],
     ["Ecosystem","Lock-in across bundled services","Apple, Google, Amazon ecosystems"],
     ["Usage / on-demand","Pay per use / API call","AWS pay-as-you-go, cloud, SMS API"],
     ["Experience","Charge for a premium experience","Netflix originals, events, premium UX"]],
    per_page=5,widths=[1.5,2.6,2.9],fs=10.5,
    note="Read the middle column: models differ mainly in HOW they capture value (commission, subscription, upsell, ads, margin, usage). Most real firms are HYBRIDS — Daraz combines marketplace + advertising + e-commerce; Google combines advertising + ecosystem + usage (cloud). Data-monetization underlies the ad models.")

concept_understand("S22 · Concept 3 · [THEORY]","The 10 Business Models — Part 2 + Hybrids",
    "Part 2 covers the other five, plus hybrids. (6) ADVERTISING — give a service free, sell user attention (Google, Meta, TikTok). (7) E-COMMERCE — sell goods online for a margin (Sastodeal, brand stores). (8) ECOSYSTEM — bundle many services so users stay (Apple, Google). (9) USAGE/ON-DEMAND — pay per use or API call (AWS pay-as-you-go). (10) EXPERIENCE — charge for a premium experience (Netflix originals). Most real firms are HYBRIDS, and DATA-MONETIZATION (selling insights or targeting) underlies the advertising models.",
    ["Advertising & data-monetization: free service, revenue from attention/data (Unit 2 subsidy side).",
     "E-commerce & experience: margin on goods, or premium for a superior experience.",
     "Ecosystem & usage: bundle to lock in, or charge pay-as-you-go per use.",
     "Real firms are hybrids: Daraz = marketplace + ads + e-commerce; Google = ads + ecosystem + cloud."],
    None,"Part 2: advertising · e-commerce · ecosystem · usage/on-demand · experience (+ hybrid, data-monetization).",
    "~7 min. Reuse the 10-model table. Stress hybrids are the norm and advertising = Unit 2's subsidy-side monetization.")
concept_apply("S22 · Concept 3 · [THEORY]","The 10 Business Models — Part 2 + Hybrids",
    "Google gives search free and captures value via ADVERTISING (Unit 2's money side), while also running an ECOSYSTEM (Android, Maps, Gmail) and USAGE-based cloud (Google Cloud) — a hybrid. In Nepal, Daraz is a hybrid too: a MARKETPLACE (commission), plus ADVERTISING (sellers pay for placement), plus E-COMMERCE (its own stock). Naming the mix — not a single label — is what describes a real firm accurately.",
    "\"Each company has exactly one business model.\" Most successful digital firms are HYBRIDS, combining several models — marketplace + advertising + e-commerce, or advertising + ecosystem + cloud. Advertising models are really data-monetization (Unit 2's subsidy side). Describe a firm by its MIX of capture mechanisms, not one label.",
    "Part 2 of the ten models: advertising (free service, sell attention — Google, Meta), e-commerce (margin on goods — Sastodeal), ecosystem (bundle services to lock in — Apple, Google), usage/on-demand (pay per use/API — AWS), and experience (charge for premium experience — Netflix originals). Most real firms are hybrids (Daraz = marketplace + ads + e-commerce), and data-monetization underlies the advertising models — the subsidy-side logic of Unit 2.",
    "advertising · e-commerce · ecosystem · usage/on-demand · experience · hybrids · data-monetization")
add_table_slide("S22 · Concept 3 · scaffolding","How digital lowers entry barriers (why so many models exist)",
    ["Barrier lowered","How digital lowers it","Effect"],
    [["Physical assets","Cloud rents compute; no factory needed","Start with little capital"],
     ["Distribution","App stores & internet reach all","Global reach from day one"],
     ["Inventory","Marketplace lists others' stock","Sell without owning goods"],
     ["Marketing","Social/targeted ads are cheap","Reach niche customers cheaply"],
     ["Payments","Wallets/gateways plug in","Collect money instantly"]],
    per_page=5,widths=[1.7,2.7,2.4],fs=11,
    note="Because digital slashes the cost of assets, distribution, inventory, marketing, and payments, almost anyone can launch a business model — which is why so many models coexist and why competition is easy to START but hard to WIN (S17).")

add_activity("S22 — 'Name the model(s)'  ·  ~5 min",
    ["In pairs (3 min): pick 3 digital firms (Nepali or global).",
     "Name each firm's business model(s) from the 10 — and its capture mechanism.",
     "Spot at least one HYBRID (a firm using two or more models).",
     "Take 3–4 answers aloud (2 min); reward correctly naming the capture mechanism + a hybrid."],
    "Good answers: Netflix = subscription + experience; Daraz = marketplace + advertising + e-commerce (hybrid); Spotify = freemium + subscription + advertising. Reward naming the capture mechanism and spotting hybrids.",
    "ACTIVITY [~5 min].")
add_quiz("S22 — Quick Check  ·  ~5 min",
    [("Q1.  Netflix charging a flat monthly fee for access is which model?","q"),
     ("a) freemium   b) marketplace   c) ✅ subscription   d) advertising","a"),
     ("     Why: a recurring fee for ongoing access is the subscription model.","o"),
     ("Q2.  Google giving search free and earning from ads is capturing value via:","q"),
     ("a) subscription   b) ✅ advertising (selling user attention)   c) e-commerce   d) usage fees","a"),
     ("     Why: the advertising model gives the service free and monetises attention/data — Unit 2's money side.","o"),
     ("Discussion: name a Nepali hybrid firm and the two-plus models it combines.","o")],
    "QUIZ [~5 min]. Cement the value triad, the 10 models, and that hybrids are normal.")
add_summary("S22 · Summary  ·  [~2 min]",
    ["A business model = how you CREATE (proposition) + DELIVER (channels) + CAPTURE (revenue) value; capture is the key design choice.",
     "Ten models: platform, subscription, freemium, sharing, marketplace, advertising, e-commerce, ecosystem, usage/on-demand, experience.",
     "Most real firms are HYBRIDS; digital lowers entry barriers (assets, distribution, inventory, marketing, payments) so many models coexist."],
    "Knowing the models lets you read any digital firm's money logic and design your own — the single most powerful innovation lever (S21). But a business model (how you EARN) is not the same as how value is GENERATED, which is the distinction the next session draws out.",
    "S23 — how value is actually generated: value-creation models and the classic chain/shop/network.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S23
add_divider("Session 23 · Lecture hour 8 (of 10)","Value-Creation Models",
    "A factory MAKES value by turning raw materials into products. A hospital SOLVES a problem to create value. Pathao creates value by CONNECTING riders and drivers — it builds nothing and solves no single problem, yet creates huge value. These are three fundamentally different ways to create value. Which one is a digital platform?",
    "OPENING HOOK [~5 min]. Contrast factory, hospital, and Pathao. Agenda: value creation vs capture + chain/shop/network -> the 7 digital value-creation models -> orchestration + Inputs->Process->Outputs->Impact.")

concept_understand("S23 · Concept 1 · [THEORY]","Value Creation vs Capture; Chain, Shop, Network",
    "Value CREATION is how a firm generates value; value CAPTURE (the business model, S22) is how it earns money from that value — two different questions. Stabell & Fjeldstad's classic framework gives three ways to CREATE value: the VALUE CHAIN (transform inputs into outputs, like a factory or handset maker), the VALUE SHOP (solve a customer's unique problem, like a hospital, law firm, or IT consultancy), and the VALUE NETWORK (connect members so they create value for each other, like a bank, telecom, or platform).",
    ["Value creation = how value is GENERATED; value capture = how money is EARNED (S22).",
     "Value chain: transform inputs -> outputs, sequential (factory, manufacturer).",
     "Value shop: diagnose and solve a unique problem, cyclical (hospital, consultancy).",
     "Value network: connect members to each other, mediating (bank, telecom, platform)."],
    "s23_value_creation.png","Three ways to CREATE value: chain (make), shop (solve), network (connect) — most platforms are networks.",
    "~8 min. Use the 3-configuration diagram. This is the fresh Stabell-Fjeldstad framework. The punchline: digital platforms are value NETWORKS.")
add_comparison_table("S23 · Concept 1 · comparison","Value chain vs value shop vs value network",
    ["Dimension","Value chain","Value shop","Value network"],
    [["Logic","Transform inputs -> outputs","Diagnose & solve a problem","Connect members to each other"],
     ["Shape","Sequential / linear","Cyclical / iterative","Mediating / hub"],
     ["Key activity","Production","Problem-solving","Matching & facilitation"],
     ["Value driver","Efficiency, scale","Expertise, solution quality","Size of the network"],
     ["Example","Factory, handset maker","Hospital, law/audit, IT consult","Bank, telecom, Pathao, marketplace"]],
    per_page=5,widths=[1.5,2.2,2.3,2.5],fs=10.5,
    note="Most digital platforms are value NETWORKS: their value grows with the number of connected members (network effects, Unit 2), not with production efficiency (chain) or expertise (shop). Naming the configuration tells you what drives the firm's value.")
concept_apply("S23 · Concept 1 · [THEORY]","Value Creation vs Capture; Chain, Shop, Network",
    "A Nepali handset assembler is a value CHAIN (inputs -> phones). A Kathmandu hospital or an audit firm is a value SHOP (diagnose and solve each client's problem). Pathao and eSewa are value NETWORKS — they create value by connecting members, and that value grows with network size. Separately, HOW each captures value (its business model, S22) is a different question: the network Pathao creates is captured via commission.",
    "\"Every business creates value the same way.\" There are three distinct configurations: chain (make things), shop (solve problems), network (connect people). And value CREATION (how value is generated) is not value CAPTURE (how money is earned, S22). A firm can create value as a network yet capture it via commission, ads, or subscription.",
    "Value creation is how a firm generates value; value capture (the business model, S22) is how it earns money — two different questions. Stabell & Fjeldstad give three creation configurations: value chain (transform inputs into outputs — factory), value shop (diagnose and solve a unique problem — hospital, consultancy), and value network (connect members so they create value for each other — bank, telecom, platform). Most digital platforms are value networks, whose value grows with network size.",
    "value creation vs capture · value chain (make) · value shop (solve) · value network (connect) · platforms = networks")

concept_understand("S23 · Concept 2 · [THEORY]","The 7 Digital Value-Creation Models",
    "Beyond the classic three, digital markets create value in seven observed ways: (1) PLATFORM/ECOSYSTEM (connect and orchestrate many participants); (2) DATA-DRIVEN (turn usage data into a better product); (3) DATA-MONETIZATION (sell insights/targeting); (4) ADVERTISING/ATTENTION (monetise engagement); (5) MULTI-STAKEHOLDER (create value for several groups at once); (6) EXPERIENCE (a superior, personalised experience); (7) VALUE-LOOP (a self-reinforcing feedback loop where use creates more value). These are digital SPECIALISATIONS of the value-network logic.",
    ["Platform/ecosystem & multi-stakeholder: orchestrate value among many connected groups.",
     "Data-driven & data-monetization: usage data becomes a better product or a sold asset.",
     "Advertising/attention & experience: monetise engagement, or a superior experience.",
     "Value-loop: a self-reinforcing loop (use -> data/value -> more use) — like Unit 2's flywheel."],
    None,"Seven digital value-creation models: platform/ecosystem · data-driven · data-monetization · advertising · multi-stakeholder · experience · value-loop.",
    "~7 min. Reconcile with the classic three: these seven are digital variants of the value-NETWORK logic. Cross-ref Unit 2 flywheel for the value-loop.")
add_examples_table("S23 · Concept 2 · examples","The 7 digital value-creation models — examples",
    ["Model","How value is created","Example"],
    [["Platform / ecosystem","Orchestrate many participants","Pathao, Daraz, Apple ecosystem"],
     ["Data-driven","Usage data -> better product","Google Maps, TikTok feed"],
     ["Data-monetization","Sell insights / targeting","Ad networks, analytics firms"],
     ["Advertising / attention","Monetise engagement","Meta, YouTube, TikTok"],
     ["Multi-stakeholder","Value for several groups at once","eSewa (users/merchants/banks)"],
     ["Experience","Superior, personalised experience","Netflix, Spotify personalisation"],
     ["Value-loop","Self-reinforcing feedback loop","Amazon flywheel; TikTok use->feed"]],
    per_page=7,widths=[1.7,2.5,2.6],fs=10.5,
    note="These seven overlap and combine — they are digital specialisations of the value-NETWORK logic. Notice several depend on data and network size, the forces from Unit 2, and the value-loop is the flywheel by another name.")
concept_apply("S23 · Concept 2 · [THEORY]","The 7 Digital Value-Creation Models",
    "eSewa creates value as a MULTI-STAKEHOLDER platform (users, merchants, banks, billers all gain) and a PLATFORM/ECOSYSTEM (orchestrating payments). TikTok creates value as DATA-DRIVEN (every swipe improves the feed), ADVERTISING/ATTENTION, and a VALUE-LOOP (use -> better feed -> more use). Firms usually combine several of the seven — and all are digital versions of the value-network logic, powered by data and network size.",
    "\"Digital firms all create value the same way (they just connect people).\" Connecting is the base, but digital value creation specialises into seven forms — data-driven, data-monetization, advertising, multi-stakeholder, experience, value-loop, and platform/ecosystem. Most firms combine several, and the value-loop is Unit 2's flywheel reappearing as value creation.",
    "Digital markets create value in seven observed ways: platform/ecosystem (connect and orchestrate participants), data-driven (usage data -> better product), data-monetization (sell insights/targeting), advertising/attention (monetise engagement), multi-stakeholder (value for several groups at once), experience (superior personalised experience), and value-loop (self-reinforcing feedback — Unit 2's flywheel). These are digital specialisations of the value-network logic; firms usually combine several.",
    "platform/ecosystem · data-driven · data-monetization · advertising · multi-stakeholder · experience · value-loop")

concept_understand("S23 · Concept 3 · [THEORY]","Orchestration & the Inputs->Process->Outputs->Impact Framework",
    "A platform does not produce value directly — it ORCHESTRATES it: setting the rules, matching participants, ensuring trust, and steering the ecosystem so members create value for each other ('Uber doesn't drive cars — it orchestrates value creation'). A simple way to map any value-creation process is Inputs -> Process -> Outputs -> Impact: what goes in (participants, data), what the platform does (match, govern), what comes out (transactions, experiences), and the wider impact (jobs, market growth, financial inclusion).",
    ["Orchestration: the platform sets rules, matches, ensures trust, steers the ecosystem.",
     "It enables value it doesn't produce — participants create it for each other.",
     "Inputs -> Process -> Outputs -> Impact maps any value-creation flow end to end.",
     "Impact is the wider effect: jobs, market growth, financial inclusion (Nepal)."],
    None,"Platforms ORCHESTRATE value (don't produce it). Map it: Inputs -> Process -> Outputs -> Impact.",
    "~7 min. 'Uber doesn't drive cars — it orchestrates value creation' is the memory line. Tie orchestration to the value-network logic and Nepal impact (jobs, inclusion).")
add_comparison_table("S23 · Concept 3 · comparison","Business model vs value-creation model (disambiguation)",
    ["Question","Business model (S22)","Value-creation model (S23)"],
    [["Asks","How do you EARN money?","How is value GENERATED?"],
     ["Focus","Revenue / capture mechanism","Configuration of value activities"],
     ["Example labels","Subscription, ads, commission","Chain, shop, network; the 7 digital"],
     ["Pathao","Commission (platform model)","Value network (connect riders/drivers)"],
     ["Relationship","How you capture the value…","…the value you created here"]],
    per_page=5,widths=[1.6,2.6,2.7],fs=11,
    note="Keep them distinct: value CREATION is how value is generated (chain/shop/network + the 7); the business model is how that value is CAPTURED as revenue (S22). A firm chooses both — Pathao creates as a network, captures via commission.")
concept_apply("S23 · Concept 3 · [THEORY]","Orchestration & Inputs->Process->Outputs->Impact",
    "Pathao orchestrates rather than produces: it sets fares and rules, matches riders to drivers, and ensures trust via ratings — the drivers create the rides. Mapped: Inputs (drivers, riders, data) -> Process (match, price, govern) -> Outputs (completed rides, ratings) -> Impact (driver incomes, urban mobility, less idle capacity). This shows value CREATION (a network, orchestrated); its business model (S22) is how it CAPTURES that value — commission.",
    "\"A platform produces its service like a factory.\" A platform ORCHESTRATES value it doesn't produce — it sets rules, matches, and ensures trust while members create the value. And don't confuse value creation (how value is generated — a network here) with the business model (how it's captured — commission). Both are chosen deliberately.",
    "A platform orchestrates value rather than producing it: it sets rules, matches participants, ensures trust, and steers the ecosystem so members create value for each other ('Uber doesn't drive cars — it orchestrates value creation'). Any value-creation flow maps as Inputs -> Process -> Outputs -> Impact: inputs (participants, data), process (match, govern), outputs (transactions, experiences), impact (jobs, market growth, financial inclusion). Value creation (how value is generated) stays distinct from the business model (how it is captured, S22).",
    "orchestration · enable not produce · Inputs -> Process -> Outputs -> Impact · creation vs capture")

add_activity("S23 — 'Chain, shop, or network?'  ·  ~5 min",
    ["In pairs (3 min): classify 4 organisations (a factory, a hospital, a bank, Pathao) as chain / shop / network.",
     "For the network one, map it as Inputs -> Process -> Outputs -> Impact.",
     "Separately, state its business model (how it captures value) to show creation != capture.",
     "Take 3–4 answers aloud (2 min); check chain/shop/network is justified by its LOGIC."],
    "Good answers: factory = chain, hospital = shop, bank & Pathao = network. Pathao IPOI: inputs (riders/drivers/data) -> process (match/price) -> outputs (rides) -> impact (incomes, mobility); captures via commission. Reward justifying the configuration + separating creation from capture.",
    "ACTIVITY [~5 min].")
add_quiz("S23 — Quick Check  ·  ~5 min",
    [("Q1.  A hospital or IT consultancy that diagnoses and solves a client's problem is a:","q"),
     ("a) value chain   b) ✅ value shop   c) value network   d) value pipe","a"),
     ("     Why: the value shop creates value by solving a unique problem, iteratively — not by production or connection.","o"),
     ("Q2.  A business model and a value-creation model differ in that the business model answers:","q"),
     ("a) how value is generated   b) ✅ how you EARN money (capture)   c) the logo   d) the tax rate","a"),
     ("     Why: value creation = how value is generated; business model = how that value is captured as revenue.","o"),
     ("Discussion: classify a Nepali firm as chain/shop/network and name its business model.","o")],
    "QUIZ [~5 min]. Nail chain/shop/network and the creation-vs-capture distinction.")
add_summary("S23 · Summary  ·  [~2 min]",
    ["Value creation (how value is generated) != value capture (how money is earned, S22). Classic configs: chain (make), shop (solve), network (connect).",
     "Seven digital value-creation models (platform/ecosystem, data-driven, data-monetization, advertising, multi-stakeholder, experience, value-loop) specialise the network logic.",
     "Platforms ORCHESTRATE value they don't produce; map it as Inputs -> Process -> Outputs -> Impact."],
    "Separating how value is created from how it's captured is what lets you design a platform deliberately — create as a network, capture via the right model. Next we make the market itself DYNAMIC: how it behaves and how pricing steers it over time.",
    "S24 — putting it in motion: modelling digital markets — static business model vs dynamic market model.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S24
add_divider("Session 24 · Lecture hour 9 (of 10)","Modelling Digital Markets",
    "A business model is a snapshot — it tells you how a firm earns today. But markets MOVE: users sign up, convert, stay, or churn; prices rise at peak and fall off-peak; a market tips to one winner. To run or predict a digital market you need a MODEL of how it behaves over time, not just a snapshot. How do we model a market in motion?",
    "OPENING HOOK [~5 min]. Snapshot vs motion picture. Agenda: business model (static) vs market model (dynamic) -> pricing as a lever + dynamic/algorithmic pricing -> two-sided balance & tipping (cross-ref U2).")

concept_understand("S24 · Concept 1 · [THEORY]","Business Model (Static) vs Market Model (Dynamic)",
    "A business model is largely STATIC — it describes how a firm creates, delivers, and captures value at a point in time (S22). A market model is DYNAMIC — it describes how the market behaves and evolves over time: how users are ACQUIRED, how many CONVERT (from free to paid or visitor to buyer), how many are RETAINED, and how many CHURN (leave). Modelling these flows lets a firm predict growth, spot when a market will tip, and test 'what-if' pricing or promotion decisions.",
    ["Business model = static snapshot (how you earn now).",
     "Market model = dynamic: adoption -> conversion -> retention -> churn over time.",
     "It predicts growth, tipping, and the effect of pricing/promotion changes.",
     "Same firm, two views: the model of the firm vs the model of the market it lives in."],
    None,"Business model = static (how you earn now); market model = dynamic (adoption, conversion, retention, churn over time).",
    "~7 min. Contrast snapshot vs motion. The four flows (acquire/convert/retain/churn) are the dynamic variables — link back to Unit 2 flywheel.")
add_comparison_table("S24 · Concept 1 · comparison","Business model vs market model",
    ["Dimension","Business model (static)","Market model (dynamic)"],
    [["Question","How does the firm earn?","How does the market behave over time?"],
     ["Time","A snapshot","Evolution / motion"],
     ["Key variables","Value proposition, revenue","Adoption, conversion, retention, churn"],
     ["Use","Describe the firm","Predict growth & tipping; test decisions"],
     ["Example","Freemium (free + paid tiers)","How many free users convert & stay per month"]],
    per_page=5,widths=[1.6,2.6,2.7],fs=11,
    note="You need BOTH: the business model says how a freemium app earns; the market model predicts how many free users will convert and how fast churn erodes them — which decides whether the business model actually works at scale.")
concept_apply("S24 · Concept 1 · [THEORY]","Business Model (Static) vs Market Model (Dynamic)",
    "A Nepali streaming startup's BUSINESS MODEL might be freemium (free tier + paid). Its MARKET MODEL asks the dynamic questions: how many users do we acquire per month, what fraction convert to paid, how many stay, how many churn? The business model can look great on paper yet fail if the market model shows churn outpacing acquisition. You need both — the snapshot and the motion picture.",
    "\"If the business model is sound, the firm will succeed.\" A sound business model can still fail if the market DYNAMICS are bad — high churn, low conversion, slow adoption. The market model captures that motion (acquire/convert/retain/churn) which the static business model cannot; both are needed to judge viability.",
    "A business model is largely static — it describes how a firm creates, delivers, and captures value at a point in time (S22). A market model is dynamic — it describes how the market behaves over time: how users are acquired, how many convert (free to paid, visitor to buyer), how many are retained, and how many churn. Modelling these flows lets a firm predict growth, anticipate tipping, and test pricing/promotion decisions. A freemium business model only works if its market model (conversion vs churn) adds up.",
    "business model (static) · market model (dynamic) · adoption · conversion · retention · churn · predict tipping")

concept_understand("S24 · Concept 2 · [THEORY]","Pricing as a Lever; Dynamic & Algorithmic Pricing",
    "Price is the most powerful LEVER in a market model — small changes swing adoption, conversion, and churn. Firms use several pricing strategies: fixed subscription, freemium (free + paid), loss-leader (sell below cost to win the market), penetration (low to grow fast), and DYNAMIC/ALGORITHMIC pricing — prices that change automatically with demand, time, or user data (surge pricing). Dynamic pricing maximises revenue and balances supply/demand, but can anger users and raise fairness concerns.",
    ["Price is the main lever: it moves adoption, conversion, and churn together.",
     "Strategies: fixed subscription, freemium, loss-leader, penetration pricing.",
     "Dynamic/algorithmic pricing: prices auto-adjust to demand, time, or user data (surge).",
     "Trade-off: dynamic pricing maximises revenue & balances supply, but risks anger & unfairness."],
    None,"Price is the key lever. Strategies incl. subscription, freemium, loss-leader, and dynamic/algorithmic (surge) pricing.",
    "~7 min. Pathao surge is the local dynamic-pricing case. Note the fairness tension: efficient but resented. Cross-ref Unit 2 negative network effect (surge).")
add_examples_table("S24 · Concept 2 · examples","Pricing strategies — how they work & examples",
    ["Strategy","How it works","Example"],
    [["Subscription","Flat recurring fee","Netflix, Spotify Premium"],
     ["Freemium","Free base, pay to upgrade","Spotify, Zoom, LinkedIn"],
     ["Loss-leader","Sell below cost to win market","Launch discounts; free delivery deals"],
     ["Penetration","Low price to grow fast","New wallet's heavy cashback"],
     ["Dynamic / surge","Auto-adjust to demand/time","Pathao peak fares; airline seats"],
     ["Algorithmic","Price set by data/algorithm","E-commerce price changes by demand"]],
    per_page=6,widths=[1.6,2.5,2.8],fs=10.5,
    note="Pricing is the fastest lever in the market model: a loss-leader launch buys adoption, freemium buys reach, surge balances supply. Dynamic/algorithmic pricing is efficient but can feel unfair — a real tension for Pathao at peak.")
concept_apply("S24 · Concept 2 · [THEORY]","Pricing as a Lever; Dynamic & Algorithmic Pricing",
    "Pathao uses DYNAMIC (surge) pricing: when rush-hour demand exceeds available drivers, fares rise automatically to attract more drivers and ration rides. It balances supply and demand and lifts revenue — but riders resent paying more in the rain, a fairness tension. A new wallet instead uses PENETRATION pricing (heavy cashback) to win users fast, accepting losses now to build the network.",
    "\"Dynamic pricing is just greed / random price hikes.\" Surge pricing is an algorithmic balancing tool — it raises price when demand exceeds supply to attract more supply and ration scarce capacity. It is efficient and often necessary, though it can feel unfair; the design challenge is transparency, not abandoning the lever.",
    "Price is the most powerful lever in a market model — small changes swing adoption, conversion, and churn. Strategies include fixed subscription, freemium, loss-leader (below cost to win the market), penetration (low to grow fast), and dynamic/algorithmic pricing — prices that auto-adjust to demand, time, or user data (surge). Dynamic pricing maximises revenue and balances supply and demand (Pathao at peak) but can anger users and raise fairness concerns.",
    "price as lever · subscription · freemium · loss-leader · penetration · dynamic/algorithmic (surge) pricing · fairness tension")

concept_understand("S24 · Concept 3 · [THEORY]","Two-Sided Balance & Tipping (cross-ref Unit 2)",
    "Modelling a digital market must handle its two-sided nature (Unit 2 S11): the platform decides who to SUBSIDISE and who to CHARGE, and must keep both sides in balance — too few drivers and riders leave; too few riders and drivers leave. The model also predicts TIPPING: with strong network effects and switching costs, the market can tip to one winner (winner-take-most, Unit 2 S13). Good market models track both sides' growth and watch for the tipping point.",
    ["Two-sided balance: subsidise one side, charge the other, keep both growing together (Unit 2 S11).",
     "Imbalance kills the market: too few on either side and the other leaves.",
     "Tipping: strong network effects + switching costs -> winner-take-most (Unit 2 S13).",
     "A market model tracks both sides and forecasts if/when the market will tip."],
    None,"Model both sides (subsidise/charge, keep balanced) and watch for tipping (winner-take-most) — cross-ref Unit 2.",
    "~6 min. Explicit callback to Unit 2 S11 (two-sided pricing) & S13 (tipping). Here they're VARIABLES in a dynamic market model, not new theory.")
add_examples_table("S24 · Concept 3 · examples","Two-sided pricing cases — who subsidises whom",
    ["Case","Subsidised side","Paying side","Why"],
    [["Credit card","Cardholders (rewards)","Merchants (fees)","Shoppers attract merchants who pay to accept"],
     ["Adobe (PDF/Reader)","Readers (free)","Creators (pay for Acrobat)","Free readers make the paid tool worth buying"],
     ["Pathao","Riders (low fares off-peak)","Riders at peak / commission","Balance demand; drivers earn, platform takes cut"],
     ["Gillette (razor-blade)","Buyers (cheap razor)","Buyers (pricey blades)","Cheap razor locks in profitable blade sales"],
     ["Google","Users (free search)","Advertisers","Users' attention is sold to advertisers"],
     ["Console gaming","Gamers (cheap console)","Game publishers (licence fees)","Cheap console builds base; games earn"]],
    per_page=6,widths=[1.6,2.0,1.9,2.8],fs=10.5,
    note="The razor-and-blades and credit-card cases show two-sided pricing predates the internet — but digital markets run it dynamically. Modelling WHO subsidises WHOM, and keeping both sides balanced, is central to any market model (Unit 2 S11).")
concept_apply("S24 · Concept 3 · [THEORY]","Two-Sided Balance & Tipping",
    "Pathao's market model must balance two sides: subsidise/attract enough drivers (bonuses, fair fares) or riders face long waits and leave; keep fares acceptable or riders leave and drivers idle. It also watches tipping — if it can lock in enough drivers and riders in a city, the market could tip its way (Unit 2 S13). Gillette's razor-and-blades and credit cards show the same two-sided logic long before the internet.",
    "\"Two-sided pricing and tipping are new internet ideas.\" Razor-and-blades (Gillette) and credit cards ran two-sided pricing for decades; digital just runs it dynamically and at scale. In a market model these are VARIABLES — who to subsidise, whether the market will tip — not fresh theory; they're Unit 2's concepts applied to the dynamic market.",
    "Modelling a digital market must handle its two-sided nature (Unit 2 S11): the platform decides whom to subsidise and whom to charge, and must keep both sides balanced — too few on one side and the other leaves. The model also predicts tipping: strong network effects and switching costs can tip the market to one winner (winner-take-most, Unit 2 S13). Credit cards and Gillette's razor-and-blades show two-sided pricing predates the internet; digital runs it dynamically.",
    "two-sided balance · subsidise/charge · keep both sides growing · tipping (Unit 2) · razor-and-blades · credit cards")

add_activity("S24 — 'Model the market'  ·  ~5 min",
    ["In pairs (3 min): pick a Nepali platform (Pathao, a streaming app, a wallet).",
     "State its business model (static) AND its market-model variables (adoption/conversion/retention/churn).",
     "Choose a pricing strategy and predict whether the market will tip or stay contested.",
     "Take 3–4 answers aloud (2 min); check the static/dynamic distinction is explicit."],
    "Good answer (a streaming app): business model = freemium; market model = acquire via ads, ~5% convert, watch churn; pricing = penetration then subscription; likely contested (easy multi-homing). Reward separating static business model from dynamic market variables + a tipping call.",
    "ACTIVITY [~5 min].")
add_quiz("S24 — Quick Check  ·  ~5 min",
    [("Q1.  A business model describes how you EARN; a market model describes:","q"),
     ("a) the logo   b) the office   c) ✅ how the market behaves over time (adoption, churn, tipping)   d) the tax rate","a"),
     ("     Why: the market model is dynamic — acquisition, conversion, retention, churn, and tipping over time.","o"),
     ("Q2.  Pathao raising fares automatically at peak demand is:","q"),
     ("a) freemium   b) a subsidy   c) loss-leader   d) ✅ dynamic (surge) pricing","a"),
     ("     Why: prices auto-adjust to demand/time — dynamic/algorithmic (surge) pricing.","o"),
     ("Discussion: for a Nepali platform, name its market-model variables and one pricing lever.","o")],
    "QUIZ [~5 min]. Cement static-vs-dynamic, dynamic pricing, and two-sided balance/tipping (Unit 2 callback).")
add_summary("S24 · Summary  ·  [~2 min]",
    ["Business model = static (how you earn); market model = dynamic (adoption, conversion, retention, churn) — you need both.",
     "Price is the key lever: subscription, freemium, loss-leader, penetration, and dynamic/algorithmic (surge) pricing — efficient but with a fairness tension.",
     "Model both sides (subsidise/charge, keep balanced) and watch for tipping (winner-take-most) — Unit 2 S11 & S13 applied dynamically."],
    "Modelling the market in motion is how a firm predicts growth, prices smartly, and spots tipping before rivals do — the analytical core of digital strategy. The final session ties everything together: how firms create, capture, and DEFEND value.",
    "S25 — the capstone: digital strategy, strategic control points, and the integrated framework.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S25
add_divider("Session 25 · Lecture hour 10 (of 10) — CLOSES UNIT 3","Strategy & Integration",
    "You now know how digital markets compete, cooperate, layer, innovate, earn, create value, and move. Strategy is what ties them together — and its hardest part is not creating or capturing value, but DEFENDING it. Why can two firms create the same value, yet one keeps the profit and the other loses it? The answer is control points — and it closes the unit.",
    "OPENING HOOK [~5 min]. Pose the 'who keeps the profit?' puzzle. Agenda: strategy = create+capture+DEFEND value + control points -> strategy trade-offs -> the integrated framework applied to Pathao + trends & Nepal.")

concept_understand("S25 · Concept 1 · [THEORY]","Strategy = Create + Capture + Defend; Control Points",
    "Digital strategy has three jobs: CREATE value (S23), CAPTURE it (S22), and — the hardest — DEFEND it against imitation and rivals. Value is defended through STRATEGIC CONTROL POINTS: the chokepoints others must pass through, which confer lasting power. The four main control points are DATA (who owns the user data), ALGORITHMS (who runs the matching/ranking), STANDARDS (the format others must adopt), and USER RELATIONSHIPS (who owns the customer). 'Whoever controls the control point controls the market.'",
    ["Strategy = create + capture + DEFEND value; defending is the hardest and most overlooked.",
     "Control point = a chokepoint others must pass through -> lasting power (moat).",
     "Four control points: data, algorithms, standards, user relationships.",
     "Ecosystem strategy: own a control point, let others build around you (App Store, AWS)."],
    "s25_control_points.png","Strategy = create + capture + DEFEND. Control points (data, algorithms, standards, user relationship) hold the power.",
    "~8 min. Use the control-points diagram. Link to S20 layer power: owning a lower layer or a control point is the moat. This is the unit's strategic climax.")
add_examples_table("S25 · Concept 1 · examples","Strategic control points — who controls, and how",
    ["Control point","Why it confers power","Who holds it (example)"],
    [["Data","Un-copyable user data -> better product","Google, Meta, Amazon"],
     ["Algorithms","Owns the matching/ranking/feed","TikTok feed; Uber/Pathao dispatch"],
     ["Standards","Others must adopt the format","Visa, Fonepay QR, Windows, USB-C"],
     ["User relationship","Owns the customer & the demand","Apple, Amazon, the bank's app"],
     ["App store / gateway","Others must pass through to reach users","Apple/Google Play (~30% cut)"],
     ["Infrastructure / cloud","Everyone builds on it, pays rent","AWS, foreign cloud (Nepal depends)"]],
    per_page=6,widths=[1.8,2.7,2.5],fs=10.5,
    note="Two firms can create the same value; the one holding a control point (data, algorithm, standard, or the customer) keeps the profit. For Nepal, the warning from S20 repeats: control points (cloud, app stores) sit largely abroad.")
concept_apply("S25 · Concept 1 · [THEORY]","Strategy = Create + Capture + Defend; Control Points",
    "Pathao's real defence is its control points: the DATA on riders/drivers and city demand, the ALGORITHM that dispatches efficiently, and the USER RELATIONSHIP with everyday riders. A new rival can copy the app (create the same value) but not instantly copy Pathao's data, dispatch quality, or user base — that is what defends the profit. Globally, Apple defends via the App Store standard and the customer relationship (the ~30% cut).",
    "\"If you create value, you'll automatically keep the profit.\" Value that isn't DEFENDED is competed away — rivals copy it. Profit is kept by holding a control point (data, algorithms, standards, or the customer relationship) that others must pass through. Strategy is create + capture + DEFEND, and defending is the part firms most often neglect.",
    "Digital strategy has three jobs: create value (S23), capture it (S22), and defend it against imitation — the hardest. Value is defended through strategic control points: chokepoints others must pass through that confer lasting power. The four main ones are data (who owns user data), algorithms (who runs matching/ranking), standards (the format others must adopt), and user relationships (who owns the customer). 'Whoever controls the control point controls the market' — Pathao's data/dispatch/users; Apple's App Store.",
    "create + capture + DEFEND · strategic control point · data · algorithms · standards · user relationship · ecosystem strategy")

concept_understand("S25 · Concept 2 · [THEORY]","Strategy Trade-Offs",
    "Digital strategy is a series of trade-offs, not a single best answer. GROWTH vs PROFIT: chase market share now (subsidise, burn cash) or profit today? OPENNESS vs CONTROL: an open platform (anyone builds on it) grows faster but you control less; a closed one controls more but grows slower. Other trade-offs: scale vs focus, cooperation vs competition, and short-term revenue vs long-term trust. Amazon famously chose growth and cross-subsidy for years; a focused Nepali startup may choose profit and a niche instead.",
    ["Growth vs profit: win share now (subsidise) or earn today? — a core digital tension.",
     "Openness vs control: open grows faster but yields control; closed controls but grows slower.",
     "Scale vs focus, cooperation vs competition, short-term revenue vs long-term trust.",
     "No universal winner: the right trade-off depends on the market and the firm's position."],
    None,"Strategy = trade-offs: growth vs profit, openness vs control, scale vs focus, short-term vs long-term.",
    "~7 min. Amazon = growth/cross-subsidy for years; Daraz = scale + data. A Nepali startup often must pick focus + profit. No single right answer.")
add_comparison_table("S25 · Concept 2 · comparison","Strategy trade-offs — the two sides",
    ["Trade-off","Choose one side…","…or the other"],
    [["Growth vs profit","Growth: subsidise, win share now","Profit: earn today, grow slower"],
     ["Openness vs control","Open: grow fast, control less","Closed: control more, grow slower"],
     ["Scale vs focus","Scale: go broad, many markets","Focus: one niche done best"],
     ["Cooperate vs compete","Cooperate: grow the pie (co-opetition)","Compete: fight for the whole slice"],
     ["Short vs long term","Short: revenue now","Long: build trust, monetise later"]],
    per_page=5,widths=[1.8,2.6,2.5],fs=11,
    note="There is no universally right choice — the answer depends on the market, the firm's resources, and its position. Amazon chose growth/openness for years; a small Nepali startup usually wins by choosing focus and long-term trust.")
concept_apply("S25 · Concept 2 · [THEORY]","Strategy Trade-Offs",
    "Amazon chose GROWTH over PROFIT for years — cross-subsidising, reinvesting, running thin margins to win share — a strategy only deep capital allows. Daraz pursued SCALE and data in Nepal. But a small Nepali startup usually cannot out-spend giants, so it should choose FOCUS over scale and PROFIT/trust over growth-at-all-costs — win one niche deeply (a district, a category) rather than fight everywhere. The right trade-off depends on your position.",
    "\"There is one winning digital strategy (just grow fast like Amazon).\" Growth-at-all-costs suits firms with deep capital and tipping markets; it bankrupts a small player in a contested one. Strategy is trade-offs — growth vs profit, openness vs control, scale vs focus — and the right choice depends on the market and your resources. For most Nepali startups, focus beats scale.",
    "Digital strategy is a set of trade-offs, not one best answer: growth vs profit (win share now or earn today), openness vs control (open grows faster but yields control), scale vs focus, cooperation vs competition, and short-term revenue vs long-term trust. No choice is universally right — it depends on the market and the firm's position. Amazon chose growth and cross-subsidy for years; a focused Nepali startup usually wins by choosing profit and a niche.",
    "growth vs profit · openness vs control · scale vs focus · cooperate vs compete · short vs long term · no universal answer")

concept_understand("S25 · Concept 3 · [THEORY]","The Integrated Framework + Trends + Nepal",
    "Everything in this unit fits one integrated framework: a digital firm chooses a VALUE-CREATION model (S23), a BUSINESS model to capture it (S22), operates in a MARKET model it must manage (S24), and defends it all with STRATEGY and control points (S25) — while competing, cooperating, and co-opeting (S17–S19) across a layered internet (S20) through innovation (S21). Emerging trends (AI, blockchain, IoT) and regulation will reshape all four. For Nepal, the strategic lesson is 'focus, not scale': win a niche, fit the local context.",
    ["The four dimensions integrate: value creation + business model + market model + strategy.",
     "They sit on competition/cooperation/co-opetition, the layered model, and innovation.",
     "Trends: AI, blockchain, IoT — and regulation — will reshape all four dimensions.",
     "Nepal strategy: 'focus, not scale' — win a niche, fit local context, build trust."],
    None,"Integrated: value creation + business model + market model + strategy — on competition/co-opetition, layers & innovation. Nepal: focus, not scale.",
    "~7 min. The capstone synthesis — show the four dimensions as one picture. Close with trends + Nepal's 'focus, not scale'. This closes Unit 3.")
add_table_slide("S25 · Concept 3 · scaffolding","The integrated framework applied to Pathao (4 dimensions)",
    ["Dimension","What it asks","Pathao"],
    [["Value creation (S23)","How is value generated?","Value NETWORK — connects riders & drivers"],
     ["Business model (S22)","How is value captured?","Platform/commission per ride (+ Food)"],
     ["Market model (S24)","How does the market behave?","Two-sided; surge pricing; contested (multi-homing)"],
     ["Strategy (S25)","How is value defended?","Data, dispatch algorithm, user relationship; focus on Nepal"]],
    per_page=4,widths=[1.7,2.2,3.1],fs=10.5,
    note="This one table IS the unit: any digital firm can be read across the four dimensions — how it creates value, captures it, behaves as a market, and defends it. Pathao's edge is local focus + control points, not out-spending global giants.")
concept_apply("S25 · Concept 3 · [THEORY]","The Integrated Framework + Trends + Nepal",
    "Read Pathao across the four dimensions: it CREATES value as a network (S23), CAPTURES it via commission (S22), operates a two-sided, surge-priced, contested MARKET (S24), and DEFENDS it with data, its dispatch algorithm, and local user relationships (S25) — competing with InDrive while co-opeting with banks. Trends (AI dispatch, digital ID) will reshape it. Its winning Nepal strategy is focus, not scale — own the local market giants underprioritise.",
    "\"The four topics — value, business model, market, strategy — are separate.\" They are one integrated system: value creation feeds the business model, which plays out in a market model, all defended by strategy and control points, on top of the layered internet and driven by innovation. Analysing a firm on ALL four at once (as the exam's Pathao question asks) is the point of Unit 3.",
    "One integrated framework ties the unit together: a firm chooses a value-creation model (S23), a business model to capture it (S22), operates in a market model it must manage (S24), and defends it with strategy and control points (S25) — while competing, cooperating, and co-opeting (S17–S19) across a layered internet (S20) via innovation (S21). Trends (AI, blockchain, IoT) and regulation will reshape all four. Nepal's lesson: focus, not scale — win a niche and fit local context.",
    "integrated framework · value creation + business model + market model + strategy · trends AI/blockchain/IoT · Nepal: focus not scale")

add_activity("S25 — 'Integrate a Nepali platform'  ·  ~5 min",
    ["In pairs (4 min): pick a Nepali platform (eSewa, Daraz, Foodmandu — not Pathao).",
     "Map it across ALL FOUR dimensions: value creation, business model, market model, strategy/control points.",
     "Name its strongest control point and one strategy trade-off it faces.",
     "Take 3–4 answers aloud (1 min); this rehearses the integration exam question directly."],
    "Good answer (eSewa): creation = multi-stakeholder network; business model = platform/commission + float; market = two-sided, concentrating; strategy = control points (merchant network, data, user relationship), trade-off = openness vs control. Reward all four dimensions + a named control point.",
    "ACTIVITY [~5 min].")
add_quiz("S25 — Quick Check  ·  ~5 min",
    [("Q1.  Controlling the data, algorithms, or standards others must pass through is holding a:","q"),
     ("a) ✅ strategic control point   b) a patent   c) a subsidy   d) a pipe","a"),
     ("     Why: a control point is a chokepoint others must pass through — it defends value and confers power.","o"),
     ("Q2.  For most Nepali startups facing global giants, the wisest strategy is usually:","q"),
     ("a) out-spend them on scale   b) ✅ focus on a niche and fit local context   c) copy them exactly   d) avoid digital","a"),
     ("     Why: small players can't win a spending war; 'focus, not scale' wins a niche giants underprioritise.","o"),
     ("Discussion: map any Nepali platform across value creation, business model, market model, strategy.","o")],
    "QUIZ [~5 min]. Cement control points and 'focus, not scale' — and rehearse the integration question.")
add_summary("S25 · Summary  ·  [~2 min]",
    ["Digital strategy = create + capture + DEFEND value; defence comes from control points (data, algorithms, standards, user relationships).",
     "Strategy is trade-offs: growth vs profit, openness vs control, scale vs focus — no universally right answer.",
     "Integrated framework: value creation + business model + market model + strategy, on competition/co-opetition, layers & innovation. Nepal: focus, not scale."],
    "This closes Unit 3: you can now analyse ANY digital firm across all four dimensions and judge how it competes, cooperates, and defends its value — the exact skill the integration exam question tests, and the skill a founder or analyst uses in the real Nepali market.",
    "Unit 4 — Digital transformation & currencies: how organisations and money themselves go digital.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 3 · Cheat Sheet","One-page revision reference",
    [("Digital markets (S16)","Online space matching buyers & sellers. 4 traits: speed, scale, network effects, LOW marginal cost. 5 components: platform, payments, logistics, data & analytics, support/trust. 5 types: B2C, B2B, C2C, C2B, P2P."),
     ("Competition & cooperation (S17–S18)","Digital competes on data, network, speed, UX (Porter's 5 forces bent by network effects) -> winner-take-most, but multi-homing keeps some contested. Cooperation (grow the pie first): 5 reasons; 3 forms = joint platforms, partnerships, service integration."),
     ("Co-opetition & layers (S19–S20)","Co-opetition = cooperate UPSTREAM (tech/rails/standards) + compete DOWNSTREAM (customers); Value-Net adds complementors. Layered internet: infrastructure -> platform -> application (+user); value flows UP, power flows DOWN (control lower = power over higher)."),
     ("Innovation & business models (S21–S22)","Innovation != invention (value, not just tech); sustaining vs disruptive; 6 types; enablers AI/IoT/cloud/big data/AR/VR; ideation->MVP->scale. Value triad: create/deliver/capture. 10 models (platform, subscription, freemium, sharing, marketplace, advertising, e-commerce, ecosystem, usage, experience) — hybrids normal."),
     ("Value creation & market model (S23–S24)","Creation != capture. Chain (make) / shop (solve) / network (connect); platforms = networks; 7 digital models; orchestration; Inputs->Process->Outputs->Impact. Business model (static) vs market model (dynamic: adoption/conversion/retention/churn). Pricing lever incl. dynamic/surge; two-sided balance & tipping."),
     ("Strategy & integration (S25)","Strategy = create + capture + DEFEND. Control points: data, algorithms, standards, user relationships. Trade-offs: growth vs profit, openness vs control, scale vs focus. Integrated framework = value creation + business model + market model + strategy. Nepal: focus, not scale.")])

add_glossary("Unit 3 · Glossary","Key terms — quick reference (1 of 2)",
    [("Digital market","An online space where buyers & sellers match, price & transact."),
     ("Marginal cost","Cost of serving one more user — near-zero for digital markets."),
     ("Digital market types","B2C, B2B, C2C, C2B, P2P — classified by who sells to whom."),
     ("Winner-take-most","The leading platform captures the bulk of the market."),
     ("Multi-homing","Users/suppliers using several competing platforms at once."),
     ("Porter's Five Forces","Rivalry, entrants, buyer power, supplier power, substitutes."),
     ("Cooperation","Firms working together to create value none could alone."),
     ("Joint platform","Rivals sharing common rails/standards (ConnectIPS, SWIFT)."),
     ("Service integration","Embedding one service inside another for seamlessness."),
     ("Co-opetition","Cooperating & competing with the same firm at once."),
     ("Upstream / downstream","Shared tech/rails (upstream) vs customers/brand (downstream)."),
     ("Value-Net","Customers, suppliers, competitors & complementors around a firm."),
     ("Complementor","A firm whose product makes yours more valuable."),
     ("Layered internet model","Infrastructure -> platform -> application (+ user), business view."),
     ("Layer power","Control of a lower layer confers power over higher layers."),
     ("Digital innovation","Creating new value with digital tech (product, process, model…).")])
add_glossary("Unit 3 · Glossary","Key terms — quick reference (2 of 2)",
    [("Innovation vs invention","Value people use (innovation) vs a new technology (invention)."),
     ("Sustaining innovation","Improving a product for existing customers."),
     ("Disruptive innovation","Cheap, 'good-enough' entry that rises to overtake incumbents."),
     ("Business model","How a firm creates, delivers & captures value."),
     ("Value triad","Create + deliver + capture value."),
     ("Freemium","Free base tier, pay to upgrade."),
     ("Ecosystem model","Bundling services to lock users in."),
     ("Value creation","How a firm generates value (vs capture = how it earns)."),
     ("Value chain / shop / network","Make / solve a problem / connect members (Stabell-Fjeldstad)."),
     ("Orchestration","A platform enabling value it does not itself produce."),
     ("Inputs->Process->Outputs->Impact","A map of any value-creation flow end to end."),
     ("Market model","Dynamic view: adoption, conversion, retention, churn over time."),
     ("Dynamic / surge pricing","Prices that auto-adjust to demand, time, or data."),
     ("Two-sided balance","Keeping both platform sides growing (subsidise/charge)."),
     ("Strategic control point","A chokepoint (data, algorithm, standard, customer) that defends value."),
     ("Focus, not scale","Nepal strategy: win a niche & fit local context, don't out-spend giants.")])

# ============= CONSOLIDATED END-OF-UNIT QUIZ =============
add_divider("Unit 3 · Revision","Consolidated end-of-unit quiz",
    "Twelve MCQs across the whole unit with real a/b/c/d options (correct answer varies position; answers shown), then short-answer, applied-case, and discussion questions to work from the concept slides and Unit3_material.md.",
    "Use as a 15–20 min in-class quiz or take-home review. (No genuine IT 250 past-paper exists — built from the syllabus + the concept slides. Answer key follows Section A.)")
add_quiz("Section A — Multiple choice (answers shown · correct letter varies)",
    [("1.  A defining characteristic of a digital market is:  a) high marginal cost per user  b) ✅ near-zero marginal cost & network effects  c) fixed local reach  d) slow price changes","a"),
     ("2.  'Winner-take-most' means:  a) all firms share equally  b) the newest firm wins  c) ✅ the leading platform captures the bulk of the market  d) government picks the winner","a"),
     ("3.  Two banks jointly running ConnectIPS is cooperation via:  a) ✅ a joint platform  b) a price war  c) an acquisition  d) advertising","a"),
     ("4.  Co-opetition typically means firms:  a) compete on everything  b) cooperate on everything  c) merge  d) ✅ cooperate upstream (tech) & compete downstream (customers)","a"),
     ("5.  Cloud, data-centres & connectivity belong to which layer?  a) application  b) ✅ infrastructure  c) user  d) payment","a"),
     ("6.  'Innovation is not invention' means innovation is about:  a) ✅ creating value people use, not just inventing tech  b) patents only  c) pure research  d) copying","a"),
     ("7.  A cheap, 'good-enough' entrant that rises to overtake incumbents is:  a) sustaining innovation  b) ✅ disruptive innovation  c) invention  d) marketing innovation","a"),
     ("8.  Netflix charging a flat monthly fee is which business model?  a) freemium  b) marketplace  c) ✅ subscription  d) advertising","a"),
     ("9.  A hospital or consultancy that diagnoses & solves a problem is a:  a) value chain  b) ✅ value shop  c) value network  d) value pipe","a"),
     ("10.  A business model shows how you EARN; a market model shows:  a) the logo  b) the office  c) ✅ how the market behaves over time (adoption, churn, tipping)  d) the tax rate","a"),
     ("11.  Pathao raising fares automatically at peak demand is:  a) freemium  b) a subsidy  c) loss-leader  d) ✅ dynamic (surge) pricing","a"),
     ("12.  Controlling data/algorithms/standards others must pass through is holding a:  a) ✅ strategic control point  b) a patent  c) a subsidy  d) a pipe","a")],
    "Consolidated quiz Section A. Answer key: 1-b 2-c 3-a 4-d 5-b 6-a 7-b 8-c 9-b 10-c 11-d 12-a.",compact=True)
add_quiz("Sections B–D — short answer, applied case & discussion",
    [("Section B — Short answer","q"),
     ("13. Define co-opetition and give a Nepali example.   14. Name the 3 internet layers and the direction value flows.   15. Name 3 digital business-model types.","o"),
     ("16. Explain value chain vs value shop vs value network.   17. What is a strategic control point? Name two.","o"),
     ("Section C — Applied case","q"),
     ("18. Map Pathao across ALL FOUR dimensions: value creation · business model · market model · strategy (the integration question).","o"),
     ("19. Explain a Nepali co-opetition case (eSewa + Nabil, or Daraz + Pathao): what is shared upstream, what is competed downstream?","o"),
     ("Section D — Discussion","q"),
     ("20. Is Pathao's dominance good for Nepal? Should digital platforms be regulated? Can Nepali startups compete — focus or scale?","o")],
    "Consolidated quiz Sections B–D. Model answers on the concept slides and in Unit3_material.md.",compact=True)

# ---- close ----
add_title("End of Unit 3  ·  IT 250",
          "S16–S25 complete: digital markets · competition, cooperation & co-opetition · the layered internet model · "
          "digital innovation · business models (the 10) · value-creation models (chain/shop/network + the 7) · "
          "modelling markets (pricing, two-sided, tipping) · strategy, control points & integration",
          "Built to COURSE_MATERIAL_STANDARD.md incl. the §7A depth rule · comparison & concrete-example tables throughout · "
          "self-contained, PDF-safe, Nepal-localised · builds on Unit 2 · Next: Unit 4 — Digital Transformation & Currencies.")

_add_page_numbers()
save("IT250_Unit3.pptx")
