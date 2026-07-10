#!/usr/bin/env python3
"""IT250 (eighth) Unit 2 deck — Fundamentals of Digital Economy (S9–S15), built to
COURSE_MATERIAL_STANDARD.md INCLUDING the §7A depth rule: every confusable set is a comparison
table, every 'X vs not-X' concept a concrete-example table, claims get scaffolding tables — each
table on its OWN slide, paginated, never squeezed. Generous slide count by design. Self-contained
& PDF-safe. Imports eighth/deckkit.py. Diagrams in images/. Localised to Nepal's digital economy.
Source: syllabus (course.txt) + instructor lecture PDFs (mapped in Unit2_content_outline.md §0).
NOTE: S11 absorbs the platform ECONOMICS deferred from Unit 1 S1 (two-sided pricing, cross-subsidy).
Run: python3 build_unit2_pptx.py -> IT250_Unit2.pptx
"""
from deckkit import *

# ============================================================
#                        BUILD
# ============================================================
add_title("Unit 2 — Fundamentals of the Digital Economy",
          "IT 250: Digital Economy  ·  BIM 8th Semester  ·  Sessions S9–S15 (7 lecture hours)",
          "Self-contained slides with depth: every concept grounded in comparison & concrete-example TABLES "
          "(Nepal-localised) — no abstraction without instances. Exports to PDF with no information lost.")

add_outcomes("Unit 2 — Learning Outcomes","fundamentals  ·  s9–s15",
    "By the end of this unit, you will be able to:",
    ["Distinguish a platform business from a traditional (pipe) business and define a multi-sided platform (S9)",
     "Explain network effects (direct, indirect, data, standard) and positive feedback, and their limits (S10)",
     "Explain two-sided pricing — cross-subsidy, the money side vs the subsidy side, why one side is free (S11)",
     "Explain lock-in and switching costs (five types), the flywheel, and multi-homing (S12)",
     "Explain how digital monopolies form (the six forces, tipping), their risks, and how they are regulated (S13–S14)",
     "Describe the World Bank DAI (3 pillars) & OECD DGI (6 dimensions) and assess Nepal's position (S15)"],
    "This is Unit 2 of IT 250. It opens the 'engine room' of the digital economy: WHY platforms win, how value and prices really work in two-sided markets (the economics deferred from Unit 1), and how dominance — and the tools to check it — arise.")

add_roadmap("Unit 2 — Roadmap","Where each session fits (S9–S15)",
    ["S9   Multi-sided platforms (pipes vs platforms)",
     "S10  Network effects & positive feedback",
     "S11  Two-sided pricing — who pays, who's subsidised ⭐",
     "S12  Lock-in, switching costs & the flywheel",
     "S13  Formation of monopolies (the six forces)",
     "S14  Monopoly risks, regulation & counter-cases",
     "S15  Measuring digital adoption (DAI & OECD DGI)"],
    ["Unit 1  Introduction (digital/K-economy, 4IR) — done",
     "Unit 3  Digital markets, strategy & innovation",
     "Unit 4  Digital transformation & currencies",
     "Unit 5  Economics of information",
     "Unit 6  Digitalization — the Nepalese perspective"])

# ============================================================ S9
add_divider("Session 9 · Lecture hour 1 (of 7)","Multi-Sided Platforms: Pipes vs Platforms",
    "Daraz owns almost no products, Pathao owns no taxis, Airbnb owns no hotels — yet each is worth more than firms that own everything they sell. How does a company that MAKES nothing become so valuable? The answer is the platform business model — the core of the modern digital economy.",
    "OPENING HOOK [~5 min]. Draw out the paradox (owns nothing, worth the most). Agenda: pipe vs platform → what a multi-sided platform is → how platforms create value.")

concept_understand("S9 · Concept 1 · [THEORY]","Pipe (Linear) vs Platform Business",
    "A pipe (linear) business creates a product or service and sells it to customers — value flows one way, Business → Customer. A platform business instead connects two or more groups and lets them create value for each other — value flows in many directions. The platform does not make all the value; it makes the interactions possible.",
    ["Pipe: the firm produces the value (Netflix originals, a software licence, a factory's goods).",
     "Platform: the firm produces the MARKETPLACE; users produce the value for each other.",
     "A pipe grows by making/selling more units; a platform grows by adding more participants.",
     "Most valuable digital firms are platforms because participants — not the firm — do the producing."],
    "s9_pipe_platform.png","Pipe MAKES & sells value (one way); platform CONNECTS groups (many ways).",
    "~7 min. Use the diagram. The key shift: a platform's suppliers are its users, so it scales without making the goods itself.")
add_table_slide("S9 · Concept 1 · comparison","Pipe business vs platform business",
    ["Question","Pipe (linear) business","Platform business"],
    [["Who creates the value?","The firm itself","The users, for each other"],
     ["Direction of value","One way: business → customer","Many ways: user ↔ platform ↔ user"],
     ["How it grows","Make/sell more units","Add more participants"],
     ["Main asset","Products, factories, inventory","The network of users & the matching"],
     ["Cost of one more unit","Real (materials, labour)","Near-zero (a new listing/user)"],
     ["Nepal example","A shop selling its own goods","Daraz, Pathao, Hamrobazar, Foodmandu"]],
    per_page=6,widths=[1.8,2.5,2.6],fs=11,
    note="The platform's genius is that its 'suppliers' are its users — so it can scale to millions of listings or rides without ever making a product itself.")
concept_apply("S9 · Concept 1 · [THEORY]","Pipe vs Platform Business",
    "Foodmandu makes no food and owns no kitchens — it connects restaurants, riders, and hungry customers, and takes a cut of the interactions it enables. That is a platform. A traditional restaurant that cooks and sells its own meals is a pipe. Foodmandu can add a thousand restaurants without building a single kitchen; the restaurant can only grow by cooking more — that is the structural difference.",
    "\"A platform is just a website or a middleman.\" A website is a channel; a platform is a business model where value is created by users interacting, not by the firm producing. The firm builds and governs the marketplace (matching, trust, tools) — it does not make the goods, which is exactly why it scales.",
    "A pipe (linear) business creates a product or service and sells it to customers, with value flowing one way (business → customer) and growth coming from making/selling more units. A platform business connects two or more groups and enables them to create value for each other, with value flowing in many directions and growth coming from adding participants. The most valuable digital firms are platforms because their users, not the firm, do the producing.",
    "pipe vs platform · one-way vs multi-way value · users create value · scale by adding participants · Daraz/Pathao")

concept_understand("S9 · Concept 2 · [THEORY]","What a Multi-Sided Platform Is",
    "A multi-sided platform (MSP) is a business model that connects two or more interdependent user groups to enable interactions and create value. It solves a matching problem — buyers↔sellers, riders↔drivers, creators↔audiences — where each side needs the other. Its defining trait: the value to any one side rises as more participants join the other side.",
    ["Interdependent groups: sellers are useless without buyers, drivers useless without riders.",
     "The platform solves the MATCHING problem (who connects with whom, at what price).",
     "Five features: facilitation (not production), 2+ groups, interaction-based value, low marginal cost, scalability.",
     "'Sides' can be more than two: Daraz has buyers, sellers, advertisers, and delivery partners."],
    None,"MSP = connects 2+ interdependent groups to interact; value rises as each side grows.",
    "~7 min. Stress interdependence and 'matching problem'. Have students name the sides of eSewa (users, banks, merchants, billers).")
add_table_slide("S9 · Concept 2 · examples","Multi-sided platforms — the sides they connect",
    ["Platform","Side A","Side B (and more)","The matching problem solved"],
    [["Pathao","Riders/passengers","Drivers (+ restaurants for Food)","Who gives whom a ride, at what price"],
     ["Daraz","Buyers","Sellers (+ advertisers, couriers)","Which product from which seller"],
     ["eSewa / Fonepay","Users/payers","Merchants, banks, billers","Who pays whom, settled instantly"],
     ["Foodmandu","Hungry customers","Restaurants (+ delivery riders)","Which meal, cooked & delivered by whom"],
     ["Hamrobazar","Buyers","Individual sellers","Matching second-hand supply & demand"],
     ["YouTube","Viewers","Creators (+ advertisers)","Which video for which viewer"]],
    per_page=6,widths=[1.4,1.7,2.5,3.0],fs=10.5,
    note="Notice the interdependence in every row: each side is worthless to the platform without the other. Getting BOTH sides on board at once is the 'chicken-and-egg' problem (S11).")
concept_apply("S9 · Concept 2 · [THEORY]","What a Multi-Sided Platform Is",
    "eSewa is a multi-sided platform: it links users who want to pay, merchants who want to be paid, banks that hold the money, and billers (NEA, water, ISPs) who want collection. None of these sides is useful to eSewa alone — the value is in matching them so a payment flows instantly. Add more merchants and the wallet is more useful to users; add more users and it is more useful to merchants.",
    "\"A multi-sided platform is just a company with many customers.\" The difference is interdependence: the groups need EACH OTHER, and the platform's job is to match them. A supermarket has many customers but one side; eSewa's users and merchants are two interdependent sides whose value to each other the platform creates.",
    "A multi-sided platform (MSP) is a business model connecting two or more interdependent user groups to enable interactions and create value, solving a matching problem (buyers↔sellers, riders↔drivers, creators↔audiences) where each side needs the other. Its five features are facilitation (not production), two-or-more groups, interaction-based value, low marginal cost, and scalability — and the value to any side rises as the other side grows.",
    "multi-sided platform · interdependent groups · matching problem · facilitation not production · value rises with each side")

concept_understand("S9 · Concept 3 · [THEORY]","How Platforms Create Value",
    "Platforms create value in five ways, even though they make nothing themselves: they reduce transaction costs (search, negotiation, enforcement), match efficiently using data and algorithms, build trust through reputation systems (ratings, reviews, verification), provide tools and infrastructure (payments, logistics, dashboards), and create network value (each user makes the platform more useful).",
    ["Reduce transaction costs: finding and trusting a stranger to transact with becomes cheap.",
     "Efficient matching: algorithms pair the right buyer/seller, rider/driver faster than any market square.",
     "Trust: ratings, reviews, verification, and dispute resolution let strangers transact safely.",
     "Tools + network value: payment gateways, tracking, and the sheer number of users add value."],
    None,"Platforms add value 5 ways: lower transaction costs · matching · trust · tools · network value.",
    "~7 min. Trust is the underrated one — ratings let you buy from a stranger on Hamrobazar you'd never trust offline.")
add_table_slide("S9 · Concept 3 · scaffolding","The five ways platforms create value — with Nepal examples",
    ["Value mechanism","What it does","Nepal example"],
    [["Reduce transaction costs","Cuts search, negotiation, enforcement effort","Daraz: find & buy without visiting shops"],
     ["Efficient matching","Algorithms pair the right two sides fast","Pathao matches nearest driver to rider"],
     ["Trust / reputation","Ratings, reviews, verification, disputes","Hamrobazar seller ratings; Daraz returns"],
     ["Tools & infrastructure","Payments, logistics, tracking, dashboards","eSewa payment gateway; Foodmandu tracking"],
     ["Network value","More users → more useful for everyone","Fonepay: accepted almost everywhere"]],
    per_page=5,widths=[1.9,2.7,2.6],fs=11,
    note="A platform earns its cut by removing friction (cost, matching, trust) that individuals could not remove alone. This is the value it captures via commissions, ads, or subscriptions.")
concept_apply("S9 · Concept 3 · [THEORY]","How Platforms Create Value",
    "On Hamrobazar you buy a used phone from a stranger you'll never meet — something risky in a newspaper classified — because ratings, reviews, and the platform's dispute process create trust. Daraz reduces your search cost (no visiting ten shops), matches you to sellers, handles payment and returns, and is more useful because millions already use it. Those are the five mechanisms in one purchase.",
    "\"Platforms just take a commission for doing nothing.\" They capture value because they REMOVE real friction — search cost, matching, trust, payments, logistics — that buyers and sellers could not remove alone. The commission is the price of the friction they eliminate, not a toll for nothing.",
    "Platforms create value in five ways despite making nothing themselves: reducing transaction costs (search, negotiation, enforcement), enabling efficient matching (data/algorithms), building trust (ratings, reviews, verification, dispute resolution), providing tools and infrastructure (payments, logistics, dashboards), and creating network value (each user makes the platform more useful). They capture a share of this value through commissions, advertising, or subscriptions.",
    "reduce transaction costs · efficient matching · trust/reputation · tools & infrastructure · network value")

add_activity("S9 — 'Name the sides'  ·  ~5 min",
    ["In pairs (2 min): pick a Nepali platform (eSewa, Pathao, Daraz, Foodmandu, Hamrobazar).",
     "List every distinct SIDE it connects, and the matching problem it solves.",
     "Name which of the 5 value mechanisms it relies on most.",
     "Take 3 answers aloud (3 min); check each named at least two interdependent sides."],
    "Good answer for Daraz: buyers, sellers, advertisers, couriers; matching product↔buyer; relies on trust (ratings/returns) + reduced transaction cost. Reward spotting more than two sides and the interdependence.",
    "ACTIVITY [~5 min].")
add_quiz("S9 — Quick Check  ·  ~5 min",
    [("Q1.  The key difference between a pipe and a platform business is:","q"),
     ("a) size   b) ✅ who creates the value — the firm (pipe) vs the users, for each other (platform)   c) profit   d) age","a"),
     ("     Why: a pipe produces and sells value; a platform enables users to create value for each other.","o"),
     ("Q2.  A multi-sided platform's defining feature is that its user groups are:","q"),
     ("a) unrelated   b) all buyers   c) ✅ interdependent — each side needs the other   d) employees","a"),
     ("     Why: sellers are useless without buyers and vice versa; the platform's job is to match interdependent sides.","o"),
     ("Discussion: name a Nepali platform and every side it connects.","o")],
    "QUIZ [~5 min]. Cement 'users create the value' and interdependence — the foundation for network effects (S10).")
add_summary("S9 · Summary  ·  [~2 min]",
    ["Pipe business MAKES & sells value one way; a platform CONNECTS groups so users create value for each other.",
     "A multi-sided platform links 2+ interdependent groups and solves a matching problem; value rises as each side grows.",
     "Platforms create value 5 ways: lower transaction costs, matching, trust, tools/infrastructure, network value."],
    "Almost every fast-growing Nepali digital business is a platform, not a pipe — understanding the model explains why they scale so fast and where their money comes from, which you'll need whether you build one or compete with one.",
    "S10 — the force that makes platforms win: network effects and positive feedback.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S10
add_divider("Session 10 · Lecture hour 2 (of 7)","Network Effects & Positive Feedback",
    "Why don't we juggle 20 messaging apps? Why did WhatsApp take over Nepal while Viber quietly faded? WhatsApp isn't twenty times better as software — but its USERS are. The value isn't only in the app; it's in who else is on it. That is the network effect, the single most important force in the digital economy.",
    "OPENING HOOK [~5 min]. Ask which messaging app everyone uses and why. Agenda: network effects & positive feedback → the four types → the limits (negative network effects).")

concept_understand("S10 · Concept 1 · [THEORY]","Network Effects & the Positive Feedback Loop",
    "A network effect exists when a product becomes more valuable as more people use it. One fax machine is useless; a million are essential. This creates a positive feedback loop: more users → more value → attracts more users → more value. Because digital goods scale cheaply, this loop can run explosively — a rough intuition (Metcalfe) is that value grows with the number of possible connections, not just the number of users.",
    ["The value is in the network, not just the product — a phone nobody else has is worthless.",
     "Positive feedback: success breeds success (users → value → more users).",
     "Metcalfe intuition: 2 users = 1 link, 5 users = 10 links — value rises faster than user count.",
     "Digital + low marginal cost lets the loop spin fast, unlike physical networks (roads, rail)."],
    "s10_networkloop.png","Network effect: more users → more value → more users (positive feedback).",
    "~7 min. Use the loop diagram. The fax/phone example makes 'value is in the network' concrete before the four types.")
add_table_slide("S10 · Concept 1 · scaffolding","Network effect vs viral effect — often confused",
    ["Question","Network effect","Viral effect"],
    [["What happens","Product gets more USEFUL as users join","Content SPREADS fast via sharing"],
     ["Does it add lasting value?","Yes — each user improves the product","Not necessarily — a meme fades"],
     ["Time horizon","Long-term competitive advantage","Often a short-lived spike"],
     ["Example","WhatsApp more useful as friends join","A viral TikTok clip or forwarded joke"],
     ["Can you have one without the other?","Yes — a useful tool few share","Yes — viral content on a weak platform"]],
    per_page=5,widths=[2.0,2.6,2.6],fs=11,
    note="Going viral is not the same as a network effect: virality is fast spread; a network effect is durable added value. Google+ went viral on launch but had no lasting network effect and died.")
concept_apply("S10 · Concept 1 · [THEORY]","Network Effects & Positive Feedback",
    "WhatsApp won Nepal not by being the best-engineered app but because everyone's family, college group, and workplace is already on it — each new user made it more useful to the rest. Viber and others faced the reverse: fewer contacts meant less value, so users drifted to where the network was. The positive feedback loop rewarded the platform that got ahead first.",
    "\"The best app always wins.\" In network markets the best-CONNECTED app wins, not necessarily the best-built one. A technically superior messenger with few of your contacts is less useful to you than a plainer one where everyone already is — value lives in the network, not only the features.",
    "A network effect exists when a product becomes more valuable as more people use it, creating a positive feedback loop (more users → more value → more users). A rough intuition from Metcalfe is that value rises with the number of possible connections, faster than the raw user count. Because digital goods scale at low marginal cost, the loop can run explosively — which is why the best-connected platform, not always the best-built one, tends to win.",
    "network effect · value rises with users · positive feedback loop · Metcalfe intuition · best-connected wins")

concept_understand("S10 · Concept 2 · [THEORY]","The Four Types of Network Effect",
    "Network effects come in four kinds. Direct (same-side): more users of the SAME type add value — WhatsApp, Facebook. Indirect (cross-side): more users on one side attract the other — Uber riders↔drivers, app developers↔users. Data: more users → more data → a better product → more users — Google Maps, TikTok. Standard/technology: a technical standard grows more valuable as it dominates — Fonepay QR, USB-C.",
    ["Direct / same-side: value from others LIKE you (more friends on the same app).",
     "Indirect / cross-side: value from the OTHER side (more drivers → better for riders).",
     "Data network effect: usage generates data that makes the product smarter (TikTok's feed).",
     "Standard/technology: the more a standard is adopted, the more valuable it is (QR, USB-C)."],
    None,"Four types: direct (same-side) · indirect (cross-side) · data · standard/technology.",
    "~8 min. Use the comparison table. TikTok is the clearest DATA network effect — every swipe trains the feed.")
add_table_slide("S10 · Concept 2 · comparison","The four types of network effect",
    ["Type","How value grows","Nepal / global example"],
    [["Direct (same-side)","More users of the SAME group add value","WhatsApp, Facebook, online games"],
     ["Indirect (cross-side)","More users on one side attract the other","Pathao riders↔drivers; app stores"],
     ["Data","Usage → data → smarter product → users","TikTok feed; Google Maps traffic"],
     ["Standard / technology","A standard grows more valuable as it dominates","Fonepay QR; USB-C; GSM; PDF"]],
    per_page=4,widths=[1.9,2.9,2.6],fs=11,
    note="Many platforms have several at once: Daraz has indirect (buyers↔sellers) AND data (recommendations) effects. Identifying which type is at work tells you how the platform defends its lead.")
concept_apply("S10 · Concept 2 · [THEORY]","The Four Types of Network Effect",
    "TikTok shows the data network effect vividly: every swipe, watch-time, and replay trains its algorithm, so the feed gets more addictive the more you (and everyone) use it — a better product that attracts more users who generate more data. Fonepay shows the standard effect: once most Nepali merchants display a Fonepay QR, every wallet wants to work with it, and every user expects it — the standard's dominance is its value.",
    "\"All network effects are the same 'more users = better' idea.\" They differ in HOW value grows: same-side (friends), cross-side (the other group), data (a smarter product), or a standard (adoption itself). Knowing the type matters — a data effect is defended by data, a standard effect by ubiquity.",
    "Network effects come in four types: direct/same-side (more users of the same group add value — WhatsApp), indirect/cross-side (more users on one side attract the other — Pathao riders↔drivers), data (usage generates data that makes the product smarter — TikTok, Google Maps), and standard/technology (a standard grows more valuable as it dominates — Fonepay QR, USB-C). A platform often has several at once, and the type determines how it defends its lead.",
    "direct/same-side · indirect/cross-side · data network effect · standard/technology effect · often combined")

concept_understand("S10 · Concept 3 · [THEORY]","The Limits: Negative Network Effects",
    "Network effects are not infinite or always positive. Beyond some point, more users can REDUCE value — congestion (a video call that lags at peak), spam and low-quality content, toxicity, or price surges that anger users. These negative network effects, plus failure cases like Google+ and Clubhouse, show the loop can stall or reverse; growth must be managed, not assumed.",
    ["Congestion: too many users strain capacity (peak-time app slowdowns).",
     "Quality dilution: too many low-quality sellers/posts crowd out the good ones.",
     "Toxicity & noise: unmoderated growth drives good users away.",
     "The loop can reverse: users leaving makes a platform less valuable, accelerating decline."],
    None,"More users can HURT: congestion, spam, toxicity, surge — network effects have limits & can reverse.",
    "~6 min. Balance the winner-take-all story: Clubhouse grew fast then collapsed when the novelty and network thinned. Growth isn't destiny.")
add_table_slide("S10 · Concept 3 · examples","Positive vs negative network effects",
    ["Situation","Positive network effect","Negative network effect (too many / wrong users)"],
    [["Messaging app","More friends → more useful","(few negatives — scales well)"],
     ["Ride-hailing at peak","More drivers → shorter waits","Too many riders → surge pricing, long waits"],
     ["Marketplace","More sellers → more choice","Too many low-quality sellers → hard to trust"],
     ["Social feed","More friends → more relevant","Too many ads/spam → users leave"],
     ["Video calls","More contacts reachable","Peak congestion → lag, dropped calls"]],
    per_page=5,widths=[1.8,2.5,2.9],fs=10.5,
    note="The same growth that creates value can, unmanaged, destroy it. Platforms invest in moderation, capacity, and quality control precisely to keep the network effect positive.")
concept_apply("S10 · Concept 3 · [THEORY]","The Limits: Negative Network Effects",
    "Pathao at rush hour shows both edges: normally more drivers mean shorter waits (positive), but when demand spikes, surge pricing and long waits frustrate riders (negative). A marketplace flooded with low-quality or scam sellers becomes harder to trust, driving good buyers away. Platforms spend heavily on moderation, capacity, and quality control to keep the loop positive.",
    "\"Network effects mean a platform's growth is unstoppable.\" Growth can dilute quality, congest capacity, or turn toxic — and the loop can reverse when users leave (Google+, Clubhouse). Network effects are powerful but must be managed; they are not a guarantee of permanent dominance.",
    "Network effects have limits and can turn negative: beyond a point more users can reduce value through congestion (peak lag), quality dilution (too many low-quality sellers/posts), toxicity, or anger-inducing surge pricing. Failure cases like Google+ and Clubhouse show the positive feedback loop can stall or reverse when users leave. Platforms actively manage growth — moderation, capacity, quality control — to keep the effect positive.",
    "negative network effects · congestion · quality dilution · toxicity · loop can reverse · growth must be managed")

add_activity("S10 — 'Which effect, and could it reverse?'  ·  ~5 min",
    ["In pairs (2 min): pick a platform and identify which of the 4 network-effect types it relies on.",
     "Name one way its network effect could turn NEGATIVE.",
     "Take 3–4 answers aloud (3 min); classify each effect type on the board.",
     "Close: strong platforms actively defend against the negative side."],
    "Seeds: TikTok (data; negative = toxic/low-quality flood), Pathao (indirect; negative = surge), Daraz (indirect+data; negative = scam sellers), WhatsApp (direct; negative = spam/forwarded misinformation).",
    "ACTIVITY [~5 min].")
add_quiz("S10 — Quick Check  ·  ~5 min",
    [("Q1.  Uber/Pathao's riders-attract-drivers-attract-riders is which type?","q"),
     ("a) direct   b) ✅ indirect / cross-side   c) data   d) standard","a"),
     ("     Why: value on one side (riders) grows the other side (drivers) — a cross-side (indirect) network effect.","o"),
     ("Q2.  Going viral is the same as a network effect:","q"),
     ("a) true   b) ✅ false — viral = fast spread; network effect = lasting added value   c) only for TikTok   d) only offline","a"),
     ("     Why: a meme spreads (viral) without making the platform more useful; a network effect durably adds value.","o"),
     ("Discussion: name a Nepali platform's network-effect type and one way it could turn negative.","o")],
    "QUIZ [~5 min]. Drill the four types and the viral-vs-network distinction — both common confusions.")
add_summary("S10 · Summary  ·  [~2 min]",
    ["Network effect = a product gets more valuable as more use it → positive feedback loop (best-connected wins).",
     "Four types: direct (same-side), indirect (cross-side), data, standard/technology — often combined.",
     "Limits: more users can HURT (congestion, spam, toxicity, surge); the loop can reverse — growth must be managed."],
    "Network effects explain why one Nepali platform in each category tends to dominate — and why a better-built challenger still struggles. If you launch a platform, engineering a network effect (and defending its positive side) is the whole game.",
    "S11 — the economics Unit 1 promised: in a two-sided market, who actually pays, and who gets it free?",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S11
add_divider("Session 11 · Lecture hour 3 (of 7) — the economics Unit 1 deferred","Two-Sided Pricing: Who Pays, Who's Subsidised",
    "Google Search is free. TikTok is free. Adobe Reader is free. Facebook is free. So who pays the enormous bills? Someone always does — and the genius of a platform is charging the RIGHT side while giving the other side away. This is two-sided pricing, the real economics behind 'free'.",
    "OPENING HOOK [~5 min]. Ask 'if it's free, how is Google worth trillions?'. Agenda: the money side vs subsidy side → zero marginal cost & scale → the chicken-and-egg launch problem.")

concept_understand("S11 · Concept 1 · [THEORY]","The Money Side and the Subsidy Side",
    "In a two-sided market a platform charges one group (the money side) and subsidises the other (the subsidy side) — often giving it away free. This is cross-subsidy: you subsidise the side that ATTRACTS the side that pays. Google gives search to users free because their attention is what advertisers (the money side) pay for. The free side is bait, not charity.",
    ["Money side: the group that pays (advertisers, sellers, creators, premium users).",
     "Subsidy side: the group kept free/cheap because it attracts the money side (users, readers).",
     "Which side pays is a DESIGN choice: the platform charges where willingness-to-pay is highest.",
     "Get it wrong (charge the side you should subsidise) and the network never forms."],
    "s11_crosssubsidy.png","Charge the money side; subsidise the side that attracts it. 'Free' has a payer.",
    "~8 min. Use the cross-subsidy diagram. Hammer: the free side is bait — it is monetised indirectly through the paying side.")
add_table_slide("S11 · Concept 1 · examples","Who's free, who pays — two-sided pricing in practice",
    ["Platform","Subsidy side (free/cheap)","Money side (pays)","Why this split"],
    [["Google Search","Users (search free)","Advertisers","Users' attention is what advertisers buy"],
     ["Daraz","Buyers (browse free)","Sellers (commission)","Buyers attract sellers who will pay to reach them"],
     ["Facebook / TikTok","Users (free)","Advertisers","Engagement/data is sold to advertisers"],
     ["Adobe Reader / PDF","Readers (free)","Creators (pay for Acrobat)","Free readers make the paid format worth buying"],
     ["Credit / QR (Visa, Fonepay)","Cardholders/payers","Merchants (fees)","Shoppers attract merchants who pay to accept"],
     ["Newspapers (classic)","Readers (cheap)","Advertisers","Readership is sold to advertisers"]],
    per_page=6,widths=[1.9,2.3,1.9,2.6],fs=10.5,
    note="The pattern: subsidise the side whose presence is most valuable to the other side, and charge the side willing to pay to reach them. 'Free to users' almost always means 'someone else is the customer'.")
concept_apply("S11 · Concept 1 · [THEORY]","The Money Side and the Subsidy Side",
    "Daraz lets you browse and search for free, and charges sellers a commission. Why that way round? Buyers are the scarce, valuable side — sellers will happily pay to reach a crowd of ready buyers, but buyers would leave if charged to shop. Subsidising buyers builds the crowd; charging sellers monetises it. If Daraz charged buyers an entry fee, the crowd — and therefore the sellers — would vanish.",
    "\"A free service must be losing money or doing charity.\" Free-to-you usually means you are the bait, not the customer: the platform monetises your attention or data via the paying side (advertisers, sellers). Understanding this reveals who the real customer is — and why 'free' products still answer to someone.",
    "In a two-sided market a platform charges one group (the money side) and subsidises another (the subsidy side), often giving it away free — a cross-subsidy where you subsidise the side that attracts the paying side. Which side pays is a deliberate design choice: charge where willingness-to-pay is highest, subsidise where presence is most valuable to the other side. Google users are free because advertisers pay for their attention; Daraz buyers are free because sellers pay to reach them.",
    "two-sided pricing · money side vs subsidy side · cross-subsidy · free side is bait · pricing is a design choice")

concept_understand("S11 · Concept 2 · [THEORY]","Zero Marginal Cost & Economies of Scale",
    "Digital platforms have high fixed costs (build the software, the network) but a near-zero marginal cost — serving one more user costs almost nothing. So as users grow, the fixed cost is spread over more people and the average cost per user keeps falling. This is why platforms chase scale relentlessly and why a giant can undercut any small rival: its per-user cost is lower.",
    ["Fixed cost: large, one-time (engineering, infrastructure) — paid whether you have 1 user or 1M.",
     "Marginal cost: cost of ONE more user — near zero for digital goods (a copy, a login).",
     "Average cost falls with scale: fixed cost ÷ more users → cheaper per user.",
     "Consequence: bigger platforms are cheaper to run per user — a structural advantage over small rivals."],
    None,"High fixed cost + ~0 marginal cost → average cost falls with scale → big beats small.",
    "~7 min. Contrast with a physical business (each extra unit costs materials). This is the mechanism behind Unit 1's 'scalability' claim.")
add_table_slide("S11 · Concept 2 · comparison","Cost structure — traditional (pipe) vs digital platform",
    ["Cost question","Traditional / physical business","Digital platform"],
    [["Cost of one more unit/user","Real & repeated (materials, labour)","Near zero (a copy, a new account)"],
     ["Main cost","Variable (rises with output)","Fixed (build once, up front)"],
     ["Average cost as you grow","Roughly flat or rises","Falls — fixed cost spread thinner"],
     ["Limit to scale","Capacity, materials, geography","Very high — software copies freely"],
     ["Who can undercut whom","Similar-cost rivals compete","The biggest has the lowest per-user cost"]],
    per_page=5,widths=[2.2,2.6,2.4],fs=11,
    note="Near-zero marginal cost is the engine of digital scale — and a driver of monopoly (S13): the largest platform has the lowest cost per user, so it can invest more, charge less, and pull further ahead.")
concept_apply("S11 · Concept 2 · [THEORY]","Zero Marginal Cost & Economies of Scale",
    "It cost eSewa a great deal to build its platform, banking integrations, and security — but processing your next transaction costs almost nothing. So the more Nepalis use eSewa, the lower its cost per user and the more it can spend improving the app. A new wallet with few users carries the same kind of fixed costs spread over far fewer people, so its per-user cost is higher — a structural disadvantage.",
    "\"Scale just means more customers.\" For digital platforms, scale changes the ECONOMICS: because marginal cost is near zero, average cost per user falls as you grow, so the leader gets cheaper to run than challengers. Scale is not just more revenue — it is a widening cost advantage that helps tip markets (S13).",
    "Digital platforms have high fixed costs (build the software and network) but near-zero marginal cost (serving one more user costs almost nothing), so average cost per user falls as the user base grows — economies of scale. This is the mechanism behind Unit 1's 'scalability': the largest platform has the lowest per-user cost, letting it invest more and undercut smaller rivals, which is also a force pushing digital markets toward concentration.",
    "high fixed + ~0 marginal cost · average cost falls with scale · economies of scale · size = cost advantage")

concept_understand("S11 · Concept 3 · [THEORY]","The Chicken-and-Egg Problem",
    "Every new platform faces a chicken-and-egg problem: buyers won't come without sellers, and sellers won't come without buyers — neither side wants to be first. Platforms solve it with deliberate strategies: subsidise one side, seed inventory/supply manually, sign exclusive early partners, offer freemium or zero commission at launch, and use incentives to attract the first critical mass.",
    ["The launch trap: each side is waiting for the other, so the platform starts empty and useless.",
     "Subsidise/seed: pay or manually recruit the harder side first (drivers, sellers).",
     "Exclusive partners & incentives: lock in a few big draws so users have a reason to come.",
     "Reach 'critical mass' / liquidity and the network effect (S10) takes over on its own."],
    None,"Neither side comes first — solve with: subsidise a side, seed supply, exclusives, freemium, incentives.",
    "~7 min. Tie to liquidity: below critical mass the platform is dead; the launch strategies exist to reach it. Pathao subsidising early drivers is the local example.")
add_table_slide("S11 · Concept 3 · scaffolding","Solving chicken-and-egg — five launch strategies",
    ["Strategy","What the platform does","Example"],
    [["Subsidise one side","Pay/reward the harder side to join first","Pathao bonuses for early drivers"],
     ["Seed supply manually","Build initial inventory yourself","Amazon stocking its own goods early"],
     ["Exclusive partners","Sign a few big draws for early users","A platform signing a popular brand first"],
     ["Freemium / zero commission","Waive fees to remove the barrier","No seller commission at launch"],
     ["Incentives / referrals","Reward users for bringing others","Sign-up cashback; refer-a-friend credit"]],
    per_page=5,widths=[2.0,2.7,2.5],fs=11,
    note="All five aim at the same target: reach critical mass (liquidity) fast, so the network effect becomes self-sustaining and the subsidies can be dialled back.")
concept_apply("S11 · Concept 3 · [THEORY]","The Chicken-and-Egg Problem",
    "When Pathao launched, riders wouldn't open an app with no nearby drivers, and drivers wouldn't join with no riders. Pathao broke the deadlock by subsidising the supply side — bonuses and incentives to get enough drivers on the road that waits were short — which drew riders, whose demand then drew more drivers. Once it hit critical mass in a city, the network effect sustained itself and the incentives could shrink.",
    "\"Build a great app and users will come.\" A platform launches empty and useless — the hard part is the cold start, not the code. Without a deliberate strategy to seed one side and reach critical mass, even a superb platform dies waiting for the other side to show up first.",
    "Every new platform faces a chicken-and-egg problem: neither side (buyers/sellers, riders/drivers) will join before the other. Platforms solve it deliberately — subsidise one side, seed supply/inventory manually, sign exclusive early partners, waive fees (freemium/zero commission), and use incentives/referrals — all aimed at reaching critical mass (liquidity), after which the network effect becomes self-sustaining and subsidies can be reduced.",
    "chicken-and-egg · cold start · subsidise a side · seed supply · exclusives · freemium · critical mass / liquidity")

add_activity("S11 — 'Design the price'  ·  ~5 min",
    ["In pairs (3 min): you're launching a new Nepali platform (tutoring, farm produce, home services).",
     "Decide which side is FREE and which PAYS — and justify using cross-subsidy.",
     "Name one chicken-and-egg launch move you'd make first.",
     "Take 3–4 answers aloud (2 min); check the paying side is the one with willingness-to-pay."],
    "Good reasoning: subsidise the scarce/valuable side (e.g. students free, tutors pay a cut; or buyers free, farmers pay commission), and seed the hard side first. Reward answers that name WHO attracts WHOM.",
    "ACTIVITY [~5 min].")
add_quiz("S11 — Quick Check  ·  ~5 min",
    [("Q1.  Google Search is free to users because:","q"),
     ("a) it is charity   b) ✅ users are the subsidy side; advertisers (money side) pay for their attention   c) it loses money   d) the government funds it","a"),
     ("     Why: cross-subsidy — subsidise the side (users) that attracts the paying side (advertisers).","o"),
     ("Q2.  'Near-zero marginal cost' means, as a platform grows, its average cost per user:","q"),
     ("a) rises   b) stays flat   c) ✅ falls (fixed cost spread over more users)   d) becomes negative","a"),
     ("     Why: high fixed + ~0 marginal cost → the bigger the base, the cheaper per user — economies of scale.","o"),
     ("Discussion: for a new Nepali platform, which side would you make free and why?","o")],
    "QUIZ [~5 min]. This is the deferred-economics session — make sure cross-subsidy and falling average cost land.")
add_summary("S11 · Summary  ·  [~2 min]",
    ["Two-sided pricing: charge the money side, subsidise the side that attracts it (cross-subsidy) — 'free' has a payer.",
     "High fixed + near-zero marginal cost → average cost per user falls with scale → the biggest platform is cheapest per user.",
     "Chicken-and-egg: neither side comes first; solve with subsidies, seeding, exclusives, freemium, incentives → critical mass."],
    "This is the money logic of every 'free' app you use — and the playbook you'd need to launch one. Knowing who the real customer is (the money side) and how to beat the cold start separates a platform that scales from one that dies empty.",
    "S12 — once users are in, how platforms keep them: lock-in, switching costs, and the flywheel.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S12
add_divider("Session 12 · Lecture hour 4 (of 7)","Lock-In, Switching Costs & the Flywheel",
    "You've half-thought about leaving eSewa, or WhatsApp, or your bank's app — for months — and you're still there. That's not laziness; it's engineered. Platforms deliberately raise the cost of leaving until staying feels easier than switching. Meet switching costs, lock-in, and the flywheel that spins them.",
    "OPENING HOOK [~5 min]. Ask who has considered switching a service and didn't — why not? Agenda: the flywheel (designed feedback) → five switching costs → how platforms engineer lock-in.")

concept_understand("S12 · Concept 1 · [THEORY]","The Flywheel: a Designed Feedback Loop",
    "A flywheel is a deliberately designed positive-feedback loop that a platform engineers to grow: acquire users → activate them (first real value) → engage them (regular use) → retain them (lock-in), and retention feeds back into acquisition. The key distinction from a network effect: a network effect is natural (it arises from users needing each other); a flywheel is designed (the company builds the loop on purpose).",
    ["Acquire → Activate → Engage → Retain — then retention (referrals, reputation) feeds acquisition.",
     "Network effect = natural byproduct of users; flywheel = engineered strategy to spin faster.",
     "The loop compounds: each turn is cheaper and stronger than the last (Amazon's classic flywheel).",
     "Below 'liquidity' (supply meets demand fast) the flywheel won't spin — it needs critical mass first."],
    "s12_flywheel.png","Flywheel = designed loop: acquire → activate → engage → retain → (feeds acquisition).",
    "~7 min. Use the flywheel diagram. The natural-vs-designed contrast is the exam point; the flywheel is how firms operationalise the network effect.")
add_table_slide("S12 · Concept 1 · comparison","Network effect vs flywheel — natural vs designed",
    ["Question","Network effect","Flywheel"],
    [["What is it?","Value rises as more users join","A designed loop that compounds growth"],
     ["Natural or designed?","Natural — emerges from users needing each other","Designed — the company engineers it"],
     ["Focus","The value of the network","The growth process (acquire→retain)"],
     ["Example","WhatsApp more useful with more contacts","Amazon: low price → traffic → sellers → lower price"],
     ["Relationship","The force…","…the machine built to harness the force"]],
    per_page=5,widths=[1.8,2.7,2.7],fs=11,
    note="They work together: the network effect is the physics; the flywheel is the engine a company builds to exploit it. A platform can have a network effect but a poorly-designed flywheel (and stall).")
concept_apply("S12 · Concept 1 · [THEORY]","The Flywheel",
    "Amazon's flywheel is the classic case: lower prices attract more customers, more customers attract more sellers, more sellers mean more selection and scale, which lowers costs and prices again. Each turn strengthens the next. Daraz runs a similar loop in Nepal — more buyers draw more sellers, whose competition and variety draw more buyers. The company designs and tunes this loop; it does not just hope for it.",
    "\"A network effect and a flywheel are the same thing.\" A network effect is a natural force (value rises with users); a flywheel is the deliberate business machine built to harness it (acquire → activate → engage → retain). A platform can enjoy a network effect yet stall if its flywheel — onboarding, engagement, retention — is badly designed.",
    "A flywheel is a deliberately designed positive-feedback loop a platform engineers to grow: acquire → activate (first value) → engage (regular use) → retain (lock-in), with retention feeding back into acquisition. It differs from a network effect, which is natural (arising from users needing each other), whereas a flywheel is designed. The loop compounds — each turn cheaper and stronger — but needs critical mass (liquidity) to spin at all.",
    "flywheel · designed feedback loop · acquire/activate/engage/retain · natural (network effect) vs designed (flywheel)")

concept_understand("S12 · Concept 2 · [THEORY]","Switching Costs — the Five Types",
    "Switching costs are everything you'd lose or spend to move from one platform to another — and they are why you stay put. There are five types: financial (subscriptions, paid assets), learning/effort (relearning a new tool), data/asset loss (photos, files, history), network/social loss (friends, followers, ratings), and psychological/habit. The higher these are, the more locked in you are.",
    ["Financial: money lost — non-refundable subscriptions, paid content, transfer fees.",
     "Learning/effort: the time to relearn a new interface and reconfigure everything.",
     "Data/asset loss: chat history, photos, files, saved preferences you can't take with you.",
     "Network/social & psychological: losing your contacts/followers, and simple habit."],
    None,"Five switching costs: financial · learning · data/asset · network/social · psychological/habit.",
    "~7 min. Walk through WhatsApp: leaving means losing groups (network), chat history (data), and relearning (effort) — three at once.")
add_table_slide("S12 · Concept 2 · examples","The five switching costs — Nepal examples & how platforms raise them",
    ["Switching cost","What you'd lose","Nepal example","How a platform raises it"],
    [["Financial","Money paid / owed","Daraz wallet balance, vouchers","Prepaid balances, reward points"],
     ["Learning / effort","Time to relearn","Getting used to a new bank app","Deep features that take time to master"],
     ["Data / asset","Saved data & history","eSewa payment history, saved billers","Store your data in-platform, hard to export"],
     ["Network / social","Your connections","WhatsApp groups, contacts","Make your social graph the product"],
     ["Psychological / habit","Comfort & routine","Your default wallet 'muscle memory'","Defaults, streaks, daily nudges"]],
    per_page=5,widths=[1.6,1.8,2.4,2.7],fs=10.5,
    note="Switching costs are usually MORE than money — losing your WhatsApp groups (network) or eSewa history (data) can matter more than any fee. Platforms deliberately stack several types.")
concept_apply("S12 · Concept 2 · [THEORY]","Switching Costs",
    "Leaving eSewa isn't hard technically — but you'd re-add every bank account, lose your saved billers and payment history, re-learn another app, and give up any balance or reward points. Those are financial, data, learning, and habit costs stacked together. None is huge alone, but combined they make you shrug and stay — which is precisely the platform's intent.",
    "\"I stay with a service because it's the best.\" Often you stay because LEAVING is costly — data, contacts, habit, money — not because the alternative is worse. Recognising engineered switching costs helps you (and future customers you serve) make deliberate choices instead of default ones.",
    "Switching costs are everything a user would lose or spend to move to another platform, and they explain inertia. There are five types: financial (subscriptions, balances, fees), learning/effort (relearning a new tool), data/asset loss (history, photos, files, preferences), network/social loss (contacts, followers, ratings), and psychological/habit. The higher and more numerous these costs, the stronger the lock-in — and platforms deliberately stack several types.",
    "switching costs · financial · learning/effort · data/asset · network/social · psychological/habit · stacked = lock-in")

concept_understand("S12 · Concept 3 · [THEORY]","Engineered Lock-In, Walled Gardens & Multi-Homing",
    "Lock-in is the result when switching costs are high enough that users stay. Platforms engineer it: ecosystem bundling (Apple's devices + iCloud + iMessage), proprietary formats (WhatsApp backups that won't move to Signal), loyalty programs (Prime, reward points), seamless cross-device sync, and exclusive features. A tightly closed ecosystem is a walled garden. The opposite is multi-homing — using several platforms at once — which low switching costs enable and which weakens any single platform's grip.",
    ["Lock-in tactics: bundling, proprietary formats/data, loyalty rewards, sync, exclusive features.",
     "Walled garden: a closed ecosystem, smooth inside, hard to leave (Apple, Meta's apps).",
     "Multi-homing: users on several platforms at once (a driver on Pathao + InDrive) — weakens lock-in.",
     "Platforms fight multi-homing with loyalty, exclusives, and integration to keep users single-homed."],
    None,"Lock-in is engineered (bundling, formats, loyalty, sync); walled gardens deepen it; multi-homing weakens it.",
    "~7 min. Note the tension: users benefit from multi-homing (choice, competition); platforms fight it. Nepal: drivers multi-home across Pathao/InDrive.")
add_table_slide("S12 · Concept 3 · examples","How platforms engineer lock-in",
    ["Lock-in tactic","How it works","Example"],
    [["Ecosystem bundling","Many services only work well together","Apple: iPhone + iCloud + iMessage"],
     ["Proprietary format / data","Your data won't move elsewhere","WhatsApp backup can't import to Signal"],
     ["Loyalty / rewards","Points & perks you'd forfeit by leaving","Amazon Prime; Daraz vouchers"],
     ["Cross-device sync","Seamless only inside the ecosystem","Google Workspace across devices"],
     ["Exclusive features / content","Unique things unavailable elsewhere","Platform-only shows, filters, integrations"]],
    per_page=5,widths=[1.9,2.7,2.6],fs=11,
    note="Each tactic quietly raises a switching cost. A walled garden stacks them so the inside is frictionless and the exit is painful — the deliberate design behind 'I can't be bothered to switch'.")
concept_apply("S12 · Concept 3 · [THEORY]","Engineered Lock-In & Multi-Homing",
    "Nepali ride-share drivers often multi-home — running Pathao and InDrive together to catch more rides — because switching (or running both) costs them little. That multi-homing weakens each platform's grip, so platforms respond with driver loyalty bonuses, exclusive incentives, and integration (in-app payments, ratings) to make one platform the default. Apple, by contrast, is a walled garden most users never leave because everything is bundled.",
    "\"Lock-in just means the service is good enough that people stay.\" Lock-in is usually engineered, not earned — bundling, proprietary data, loyalty points, and exclusives raise the cost of leaving regardless of whether a rival is better. Multi-homing (using several at once) is the user's natural defence, which is exactly why platforms work to prevent it.",
    "Lock-in results when engineered switching costs keep users in place: platforms use ecosystem bundling (Apple), proprietary formats/data (WhatsApp backups), loyalty programs (Prime, vouchers), cross-device sync, and exclusive features. A tightly closed ecosystem is a walled garden. The opposite is multi-homing — using several platforms at once (drivers on Pathao + InDrive) — enabled by low switching costs, which weakens any single platform's grip; platforms fight it with loyalty, exclusives, and integration.",
    "lock-in · bundling · proprietary formats · loyalty · walled garden · multi-homing · single-homing")

add_activity("S12 — 'Trapped by design'  ·  ~5 min",
    ["Individually (1 min): name a service you'd like to leave but haven't.",
     "In pairs (2 min): identify which of the 5 switching costs keep you there, and any lock-in tactic used.",
     "Take 3–4 answers aloud (2 min); tally the most common switching cost.",
     "Close: notice how much lock-in is engineered, not accidental."],
    "Seeds: WhatsApp (network + data + habit), bank app (learning + data), Apple (bundling walled garden), Daraz (rewards). Reward naming the specific switching-cost type and the tactic.",
    "ACTIVITY [~5 min].")
add_quiz("S12 — Quick Check  ·  ~5 min",
    [("Q1.  The difference between a network effect and a flywheel is:","q"),
     ("a) none   b) ✅ a network effect is natural; a flywheel is a designed growth loop   c) size   d) only Amazon has flywheels","a"),
     ("     Why: the network effect is the force; the flywheel is the engineered machine that harnesses it.","o"),
     ("Q2.  Losing your WhatsApp groups and chat history if you left is which switching cost(s)?","q"),
     ("a) financial only   b) ✅ network/social + data/asset   c) learning only   d) none","a"),
     ("     Why: groups = network/social loss; chat history = data/asset loss — stacked switching costs.","o"),
     ("Discussion: name a service you'd leave but haven't — which switching costs trap you?","o")],
    "QUIZ [~5 min]. Nail flywheel-vs-network-effect and the five switching-cost types.")
add_summary("S12 · Summary  ·  [~2 min]",
    ["Flywheel = a DESIGNED growth loop (acquire→activate→engage→retain); a network effect is the NATURAL force it harnesses.",
     "Five switching costs — financial, learning, data/asset, network/social, psychological — stack into lock-in.",
     "Platforms engineer lock-in (bundling, formats, loyalty, sync, exclusives) & fight multi-homing; walled gardens deepen it."],
    "Lock-in decides whether a platform keeps the users it wins — and as a consumer it explains your own inertia. As a future builder, designing (ethical) switching costs is how you retain customers; as a regulator, reducing them (data portability) is how you restore competition.",
    "S13 — when network effects + scale + lock-in combine: how digital monopolies form.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S13
add_divider("Session 13 · Lecture hour 5 (of 7)","Formation of Monopolies in the Digital Economy",
    "Once everyone is on the platform, everyone HAS to be on the platform. In ordinary markets several firms share the pie; in digital markets the leader often takes almost all of it — 'winner-take-most'. Google has ~90% of search, WhatsApp is near-universal in Nepal. Why do digital markets tip toward one giant so much more than shops or factories do?",
    "OPENING HOOK [~5 min]. Contrast a street of many tea shops with search (one giant). Agenda: winner-take-most & tipping → the six forces → market types (incl. buyer power) & entry barriers.")

concept_understand("S13 · Concept 1 · [THEORY]","Winner-Take-Most & the Tipping Point",
    "A digital monopoly rarely means 100% control; it means 'winner-take-most' — the leader captures the bulk of the market, a small rival survives, and the rest fade. This happens because of increasing returns: the bigger a platform gets, the better and cheaper it becomes, attracting still more users. Past a tipping point, one platform becomes effectively unstoppable and users pile onto it.",
    ["Winner-take-most: leader takes the majority; one small competitor lingers; others die.",
     "Increasing returns: more users → better/cheaper product → even more users (S10 + S11 combined).",
     "Tipping point: the moment the market 'tips' to one platform and reversal becomes very hard.",
     "Not every market tips — where multi-homing is easy and effects are weak, several can coexist."],
    "s13_tipping.png","Winner-take-most: past the tipping point, increasing returns pile users onto the leader.",
    "~7 min. Use the tipping S-curve. Stress the nuance: markets tip when effects + scale + lock-in are strong; otherwise they stay contested.")
add_table_slide("S13 · Concept 1 · comparison","When a market tips vs stays contested",
    ["Factor","Tips to one winner","Stays contested (several survive)"],
    [["Network effects","Strong (value needs everyone)","Weak or local"],
     ["Switching costs","High (hard to leave)","Low (easy to switch)"],
     ["Multi-homing","Rare (users pick one)","Common (users use several)"],
     ["Differentiation","Little — one 'best' network","High — niches for different needs"],
     ["Example","Search (Google), messaging (WhatsApp)","Food delivery, ride-hailing (often several)"]],
    per_page=5,widths=[1.8,2.6,2.7],fs=11,
    note="Tipping is not inevitable: ride-hailing and food delivery often support several players because multi-homing is easy and needs are local. Knowing when a market tips is a strategic and regulatory question.")
concept_apply("S13 · Concept 1 · [THEORY]","Winner-Take-Most & Tipping",
    "Nepal's messaging market tipped: WhatsApp and Viber competed, but as more contacts settled on WhatsApp its value rose for everyone until it 'won most' and Viber faded — high network effects, high switching costs, little reason to multi-home. Ride-hailing has NOT fully tipped: Pathao and InDrive coexist because drivers and riders happily multi-home and needs are local. Same country, different tipping outcomes.",
    "\"Every digital market ends in one monopoly.\" Only markets with strong network effects, high switching costs, and little multi-homing tip to one winner (search, messaging). Where multi-homing is easy and needs differ (ride-hailing, food delivery), several players persist. Tipping is a tendency, not a law.",
    "A digital monopoly usually means 'winner-take-most' — the leader captures the bulk of the market, a small rival survives, and the rest fade — driven by increasing returns (more users → a better, cheaper product → more users). Past a tipping point one platform becomes effectively unstoppable. But not every market tips: where network effects are weak, switching costs low, and multi-homing easy, several platforms coexist (ride-hailing, food delivery).",
    "winner-take-most · increasing returns · tipping point · not every market tips · multi-homing keeps markets contested")

concept_understand("S13 · Concept 2 · [THEORY]","The Six Forces Behind Digital Monopolies",
    "Six reinforcing forces push digital markets toward monopoly: network effects (more users → more value), economies of scale (near-zero marginal cost → cheaper per user with size), economies of scope (one infrastructure/dataset serves many products), data advantage (more users → more data → better product), low/zero marginal cost, and high switching costs. Each strengthens the others, so a lead compounds into dominance.",
    ["Network effects + data advantage: users and data both make the product better, attracting more users.",
     "Economies of scale + low marginal cost: the biggest is cheapest to run per user.",
     "Economies of scope: reuse one login/dataset/infrastructure across many services (Google, Amazon).",
     "High switching costs (S12): once ahead, the leader is hard to dislodge — the forces lock together."],
    None,"Six forces: network effects · scale · scope · data advantage · low marginal cost · switching costs.",
    "~8 min. These are the whole unit converging — S10 (network effects), S11 (scale/marginal cost), S12 (switching costs) plus scope and data. They reinforce each other.")
add_table_slide("S13 · Concept 2 · scaffolding","The six forces — how each pushes toward monopoly",
    ["Force","How it drives dominance","Example"],
    [["Network effects","More users make the product more valuable","WhatsApp, Facebook"],
     ["Economies of scale","Near-zero marginal cost → cheaper with size","Google serving billions of searches"],
     ["Economies of scope","One infrastructure/dataset → many products","Google: search, maps, mail, ads"],
     ["Data advantage","More users → more data → better product","TikTok's feed; Google's ranking"],
     ["Low / zero marginal cost","Serving one more user is ~free","Any software copied infinitely"],
     ["High switching costs","Users can't easily leave","Ecosystem lock-in (S12)"]],
    per_page=6,widths=[1.9,2.7,2.4],fs=10.5,
    note="No single force is decisive — it's their COMBINATION and mutual reinforcement that turns a lead into a moat. This is why digital markets concentrate far more than traditional ones.")
concept_apply("S13 · Concept 2 · [THEORY]","The Six Forces",
    "Google is the six forces in one company: network effects (more searchers + more advertisers), scale (serving billions cheaply), scope (search, maps, mail, Android, ads on one infrastructure), a data advantage (every query improves ranking), near-zero marginal cost, and switching costs (defaults, integration). Each force feeds the others, which is why its ~90% search share is so durable — no single rival can match all six at once.",
    "\"A digital monopoly wins simply by being the best or cheapest product.\" It wins because six structural forces compound a lead into a moat — network effects, scale, scope, data, near-zero cost, and switching costs — not merely product quality. A slightly better rival still can't overcome all six, which is why dominance persists.",
    "Six reinforcing forces push digital markets toward monopoly: network effects (more users → more value), economies of scale (near-zero marginal cost → cheaper with size), economies of scope (one infrastructure/dataset serves many products), data advantage (more users → more data → better product), low/zero marginal cost, and high switching costs. Their combination and mutual reinforcement — not any single one — turns an early lead into a durable moat, which is why digital markets concentrate far more than traditional ones.",
    "six forces · network effects · economies of scale · economies of scope · data advantage · marginal cost · switching costs")

concept_understand("S13 · Concept 3 · [THEORY]","Market Types & Entry Barriers",
    "Markets differ by how many sellers — and buyers — hold power. Seller-side: monopoly (one seller), oligopoly (a few — Apple & Samsung), monopolistic competition (many, differentiated). Buyer-side matters too: monopsony (one dominant buyer — Amazon in some markets), oligopsony (a few big buyers — Google/Meta/Amazon buying most digital ads). Digital leaders are protected by high entry barriers: huge server/talent cost, un-replicable data, entrenched habits, ecosystem dependence, and compliance cost.",
    ["Monopoly / oligopoly / monopolistic competition = few→many SELLERS with market power.",
     "Monopsony / oligopsony = one / a few dominant BUYERS with power (often overlooked).",
     "Entry barriers: server & talent cost, data that can't be copied, user habits, ecosystem lock-in.",
     "High barriers mean even well-funded challengers struggle to enter — protecting the incumbent."],
    None,"Seller power: monopoly→oligopoly→monopolistic competition. Buyer power: monopsony/oligopsony. Barriers guard leaders.",
    "~7 min. Monopsony is the fresh idea — Amazon as the dominant BUYER squeezing sellers; ad-space bought mostly by Google/Meta. Barriers explain why incumbents stay.")
add_table_slide("S13 · Concept 3 · comparison","Market types — seller power and buyer power",
    ["Market type","Definition","Example"],
    [["Monopoly","One dominant seller, no real substitute","Google in search; Meta in social"],
     ["Oligopoly","A few sellers dominate","Apple & Samsung (smartphones)"],
     ["Monopolistic competition","Many sellers, differentiated products","Fast food; many small apps"],
     ["Monopsony","One dominant BUYER","Amazon in some e-book/supplier markets"],
     ["Oligopsony","A few dominant buyers","Google/Meta/Amazon buying digital ad space"]],
    per_page=5,widths=[1.9,2.6,2.6],fs=11,
    note="Digital power isn't only about selling: a platform can dominate as the main BUYER (monopsony/oligopsony), squeezing suppliers, sellers, or content creators who have nowhere else to go.")
concept_apply("S13 · Concept 3 · [THEORY]","Market Types & Entry Barriers",
    "Amazon can act as a monopsony: for many small sellers it is the main route to customers, so it can dictate fees and terms — buyer power, not just seller power. And entry barriers keep challengers out: a new search engine would need billions in servers, decades of ranking data it cannot copy, and users who won't change defaults. In Nepal, a new wallet faces the barrier of Fonepay/eSewa's entrenched merchant network.",
    "\"Market power only means charging buyers high prices (monopoly).\" Power also runs the other way: a dominant BUYER (monopsony/oligopsony) squeezes sellers, suppliers, or creators. Amazon over small sellers and the ad duopoly over publishers are buyer-power cases — and entry barriers are what let either kind of power persist.",
    "Markets differ by seller power — monopoly (one seller), oligopoly (a few, e.g. Apple & Samsung), monopolistic competition (many differentiated) — and by buyer power — monopsony (one dominant buyer, e.g. Amazon over some suppliers) and oligopsony (a few, e.g. Google/Meta/Amazon buying most digital ads). Digital leaders are shielded by high entry barriers: server/talent cost, un-replicable data, user habits, ecosystem dependence, and compliance cost — which is why incumbents persist.",
    "monopoly · oligopoly · monopolistic competition · monopsony · oligopsony · entry barriers · un-replicable data")

add_activity("S13 — 'Will it tip?'  ·  ~5 min",
    ["In pairs (3 min): pick a Nepali digital market (payments, ride-hailing, e-commerce, messaging).",
     "Decide if it will tip to one winner or stay contested — using network effects, switching costs, multi-homing.",
     "Name which of the six forces is strongest there.",
     "Take 3–4 answers aloud (2 min); compare predictions."],
    "Good reasoning: messaging/payments tend to tip (strong effects, high switching, low multi-homing); ride-hailing/food stay contested (easy multi-homing, local needs). Reward using the tip-vs-contested factors explicitly.",
    "ACTIVITY [~5 min].")
add_quiz("S13 — Quick Check  ·  ~5 min",
    [("Q1.  'Winner-take-most' in digital markets is driven mainly by:","q"),
     ("a) advertising   b) ✅ increasing returns — network effects, scale & lock-in compounding   c) luck   d) government","a"),
     ("     Why: the more a platform grows, the better/cheaper it gets, attracting more users — increasing returns.","o"),
     ("Q2.  Amazon dictating terms to small sellers who depend on it is an example of:","q"),
     ("a) monopoly (seller power)   b) ✅ monopsony (buyer power)   c) oligopoly   d) competition","a"),
     ("     Why: Amazon is the dominant BUYER/gateway for those sellers — buyer-side market power (monopsony).","o"),
     ("Discussion: pick a Nepali digital market — will it tip to one winner or stay contested? Why?","o")],
    "QUIZ [~5 min]. Reinforce increasing returns, the six forces, and buyer-side power (monopsony).")
add_summary("S13 · Summary  ·  [~2 min]",
    ["Digital monopoly = 'winner-take-most' via increasing returns; past a tipping point the leader is hard to beat.",
     "Six reinforcing forces: network effects, economies of scale, economies of scope, data advantage, low marginal cost, switching costs.",
     "Market power runs both ways (monopoly…monopsony); high entry barriers (data, habits, ecosystem) protect incumbents."],
    "This explains why Nepal's digital markets tend to have one dominant player per category — and why challengers struggle. Knowing which markets tip and why is essential whether you're building a challenger, advising an incumbent, or regulating either.",
    "S14 — the flip side: the risks of digital monopolies, and the tools used to check them.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S14
add_divider("Session 14 · Lecture hour 6 (of 7)","Monopoly Risks, Regulation & the Counter-Narrative",
    "A monopoly that gives you free search and cheap next-day delivery — where's the harm? And if the product is 'free', how does a regulator even prove you were hurt? Digital monopolies pose real risks, but they are uniquely hard to regulate — and, as PickMe and India's ONDC show, not always as permanent as they look.",
    "OPENING HOOK [~5 min]. Complicate the 'free = harmless' intuition. Agenda: the risks → why regulation is hard + the tools → the counter-narrative (monopolies aren't inevitable).")

concept_understand("S14 · Concept 1 · [THEORY]","The Risks of Digital Monopolies",
    "Dominance brings real harms even when prices look low or free: less competition can mean slower innovation; concentrated data raises privacy risk; the platform can control prices and terms (Apple's ~30% App Store cut); algorithms can be biased or self-preferencing; and the incumbent can copy or acquire rivals to remove competition (Instagram Stories cloning Snapchat; Reels cloning TikTok). 'Free to use' does not mean 'no cost to society'.",
    ["Less innovation: with no serious rival, the incumbent can coast.",
     "Data & privacy: one firm holding vast personal data is a concentration risk.",
     "Price/terms control: gatekeepers set fees and rules others must accept (30% app tax).",
     "Killing competition: copying features or acquiring threats (buy-or-bury)."],
    None,"Risks: less innovation · privacy/data concentration · price & terms control · biased algorithms · copying/killing rivals.",
    "~7 min. The '30% tax' and 'buy-or-bury' are concrete harms behind 'but it's free'. Consumer welfare isn't only price.")
add_table_slide("S14 · Concept 1 · comparison","Digital monopolies — the benefits vs the risks",
    ["Benefit (why users like them)","Risk (the hidden cost)","Consequence if unchecked"],
    [["Free or cheap services","Less competition → slower innovation","Users get a frozen, stagnant product"],
     ["Convenient all-in-one ecosystem","Data & privacy concentration","One breach/misuse affects everyone"],
     ["Reliable, well-funded platform","Price/terms control (30% app tax)","Higher costs passed to sellers & users"],
     ["Personalized, 'smart' service","Biased / self-preferencing algorithms","Rivals buried; unfair rankings"],
     ["One place everyone is","Copying or acquiring rivals","Fewer choices; innovation deterred"]],
    per_page=5,widths=[2.3,2.4,2.5],fs=10.5,
    note="The trap is that the benefits are visible and immediate (free, convenient) while the costs are hidden and long-term (less innovation, privacy risk, control) — which is why monopoly harm is so easy to underestimate.")
concept_apply("S14 · Concept 1 · [THEORY]","The Risks of Digital Monopolies",
    "Apple's ~30% cut on App Store purchases is a monopoly-risk case: developers (including any Nepali app maker) must accept the fee and rules because there is no other way onto iPhones — the gatekeeper controls price and terms. Meta cloning Snapchat's Stories and TikTok's Reels shows the 'copy to kill' risk: a dominant platform can neutralise a smaller innovator's advantage, deterring the next challenger.",
    "\"If a service is free or cheap, a monopoly can't be harming me.\" Harm shows up as less innovation, concentrated data/privacy risk, gatekeeper fees passed on to you, and rivals being copied or bought out. Consumer welfare is more than today's price — it includes tomorrow's choices and innovation.",
    "Digital monopolies bring real harms even at low or zero prices: less competition can slow innovation; concentrated data raises privacy risk; gatekeepers control prices and terms (Apple's ~30% App Store cut); algorithms can be biased or self-preferencing; and incumbents can copy or acquire rivals to remove competition (Stories, Reels). The benefits are visible and immediate while the costs are hidden and long-term, so monopoly harm is easily underestimated.",
    "monopoly risks · less innovation · data/privacy concentration · gatekeeper price control · self-preferencing · copy-or-acquire")

concept_understand("S14 · Concept 2 · [THEORY]","Why Regulation Is Hard — and the Tools",
    "Digital monopolies are hard to regulate: many products are 'free', so traditional 'did prices rise?' tests fail; markets move faster than law; and data ownership rules are unclear. Regulators have adapted with new tools: data portability (take your data with you), interoperability (platforms must work together), fines for abuse, and, in extreme cases, breaking companies up — seen in the EU's Digital Markets Act and GDPR and US FTC cases against Amazon and Google.",
    ["The 'free' problem: no price rise to point to, yet harm (data, innovation) is real.",
     "Speed & data: law lags fast markets; who owns/controls data is contested.",
     "Tools: data portability + interoperability lower switching costs and open competition.",
     "Harder tools: fines for anti-competitive behaviour; structural break-ups as a last resort."],
    None,"Hard because products are 'free', markets move fast, data rules unclear. Tools: portability, interoperability, fines, break-up.",
    "~7 min. Data portability & interoperability directly attack the switching costs (S12) that create lock-in — regulation targeting the mechanism, not just the outcome.")
add_table_slide("S14 · Concept 2 · scaffolding","Tools to regulate digital monopolies",
    ["Regulatory tool","What it does","Real case"],
    [["Data portability","Let users take their data to a rival","GDPR (EU) data-portability right"],
     ["Interoperability","Force platforms to work together","EU Digital Markets Act (messaging, app stores)"],
     ["Fines for abuse","Penalise anti-competitive behaviour","EU fines on Google (search, Android)"],
     ["Antitrust cases","Challenge dominance in court","US FTC vs Amazon; cases vs Google"],
     ["Break-up (last resort)","Split a firm into competing parts","Proposed in some US/EU debates"]],
    per_page=5,widths=[1.9,2.7,2.6],fs=11,
    note="Portability and interoperability are the modern favourites because they lower switching costs (S12) and let competition return WITHOUT breaking the platform up — attacking the lock-in mechanism directly.")
concept_apply("S14 · Concept 2 · [THEORY]","Why Regulation Is Hard — and the Tools",
    "QR interoperability in Nepal (from Unit 1) is exactly this kind of tool: by requiring that any wallet can pay any merchant's QR, NRB lowered switching costs and stopped any single wallet from locking up merchants — competition by design. Internationally, the EU's Digital Markets Act forces gatekeepers to allow interoperability and portability, tackling lock-in without waiting to prove a price rise that never happens with 'free' products.",
    "\"You can't regulate a free product — there's no harm to measure.\" Regulators shifted from 'did prices rise?' to targeting the MECHANISMS of dominance: portability and interoperability lower switching costs, fines punish abuse, and break-up is a last resort. Harm to innovation and data is addressed even when the price is zero.",
    "Digital monopolies are hard to regulate because many products are free (defeating price-based tests), markets move faster than law, and data-ownership rules are unclear. Regulators use adapted tools: data portability (users take their data to rivals), interoperability (platforms must work together), fines for anti-competitive abuse, antitrust cases, and structural break-up as a last resort — seen in the EU Digital Markets Act, GDPR, and US FTC actions. Portability and interoperability directly lower the switching costs that create lock-in.",
    "regulation is hard (free products, speed, data) · data portability · interoperability · fines · break-up · DMA/GDPR/FTC")

concept_understand("S14 · Concept 3 · [THEORY] [EXAMPLE]","The Counter-Narrative: Monopolies Aren't Inevitable",
    "Dominance is powerful but not permanent, and size is not the only way to win. PickMe (Sri Lanka) beat Uber locally by being cheaper, more reliable, and better adapted — relevance over scale. India's ONDC, UPI, and Aadhaar build open public digital infrastructure that lets small players compete with Amazon/Flipkart. And history is littered with fallen giants: MySpace, Nokia, Orkut. Local relevance, open standards, and shifting user needs can all break a monopoly.",
    ["Local relevance beats size: PickMe out-served Uber in Sri Lanka by fitting the local market.",
     "Open infrastructure: India's ONDC/UPI/Aadhaar let many small players share network effects.",
     "Giants fall: MySpace → Facebook, Nokia → smartphones — dominance decays when needs shift.",
     "Policy can engineer contestability (interoperability, open standards) on purpose."],
    None,"Not inevitable: local relevance (PickMe), open infra (ONDC/UPI), and shifting needs topple giants (MySpace, Nokia).",
    "~7 min. This balances the whole unit's winner-take-all story — a hopeful, South-Asia-relevant close. ONDC ties back to regulation-as-design.")
add_table_slide("S14 · Concept 3 · examples","'Inevitable monopoly?' — the counter-cases",
    ["Case","What happened","Lesson"],
    [["PickMe (Sri Lanka)","Beat Uber locally on price, reliability, local fit","Relevance can beat sheer size"],
     ["India ONDC","Open network vs Amazon/Flipkart dominance","Open infrastructure restores competition"],
     ["UPI / Aadhaar (India)","Shared public rails many apps build on","'Government as platform' spreads network effects"],
     ["MySpace → Facebook","Dominant social network overtaken","Lead-in-hand is not permanent"],
     ["Nokia → smartphones","Market leader missed a platform shift","Dominance decays when user needs shift"]],
    per_page=5,widths=[1.9,2.7,2.5],fs=11,
    note="The winner-take-most tendency (S13) is real but not destiny. Local relevance, open public infrastructure, and shifting needs are the three main ways monopolies are broken — a hopeful counterweight to inevitability.")
concept_apply("S14 · Concept 3 · [THEORY] [EXAMPLE]","The Counter-Narrative",
    "PickMe shows a Nepali lesson too: a local platform that understands local roads, prices, and payment habits can beat a global giant that treats every city the same — Pathao and InDrive coexist with no global monopoly precisely because local relevance matters. India's ONDC and UPI go further, building open rails so many small businesses share network effects instead of one platform hoarding them — a model Nepal's own digital-public-infrastructure debate is watching.",
    "\"Once a digital monopoly forms, it's permanent and unbeatable.\" History says otherwise — MySpace, Nokia, and Orkut all fell. Local relevance (PickMe), open public infrastructure (ONDC/UPI), and shifting user needs regularly topple or contain giants. Dominance is powerful but contestable, especially by design.",
    "Digital dominance is powerful but neither permanent nor the only path to success. PickMe (Sri Lanka) beat Uber locally through price, reliability, and local fit — relevance over scale. India's ONDC, UPI, and Aadhaar build open public digital infrastructure that lets small players share network effects against Amazon/Flipkart. Fallen giants (MySpace, Nokia, Orkut) show dominance decays when needs shift. Local relevance, open standards, and changing needs all break monopolies — and policy can engineer contestability deliberately.",
    "not inevitable · PickMe (relevance>size) · ONDC/UPI/Aadhaar (open infra) · fallen giants · contestability by design")

add_activity("S14 — 'Regulate or leave alone?'  ·  ~5 min",
    ["In pairs (3 min): pick a dominant platform. Should a regulator act, and if so, which tool?",
     "Name the specific risk you're addressing and the tool (portability, interoperability, fine, break-up).",
     "Take 3–4 answers aloud (2 min); debate whether the harm outweighs the convenience.",
     "Close: the best answers target a mechanism (lock-in via portability), not just 'break them up'."],
    "Reward precise pairing of risk→tool: e.g. lock-in → data portability/interoperability; self-preferencing → antitrust; privacy concentration → data rules. Note that heavy-handed rules can also reduce useful scale — it's a trade-off.",
    "ACTIVITY [~5 min].")
add_quiz("S14 — Quick Check  ·  ~5 min",
    [("Q1.  Regulating digital monopolies is hard mainly because:","q"),
     ("a) they're small   b) ✅ products are often 'free' (no price rise to prove), markets move fast, data rules unclear   c) no laws exist   d) users don't care","a"),
     ("     Why: the classic 'did prices rise?' test fails when the product is free, though data/innovation harms are real.","o"),
     ("Q2.  Data portability and interoperability work by:","q"),
     ("a) raising prices   b) ✅ lowering switching costs so competition can return   c) banning platforms   d) adding ads","a"),
     ("     Why: they attack the lock-in mechanism (S12) directly, letting users move and rivals interconnect.","o"),
     ("Discussion: pick a dominant platform — should a regulator act, and with which tool?","o")],
    "QUIZ [~5 min]. Tie regulation tools back to switching costs (S12) and end on the not-inevitable counter-narrative.")
add_summary("S14 · Summary  ·  [~2 min]",
    ["Monopoly risks: less innovation, data/privacy concentration, gatekeeper price control, biased algorithms, copying/killing rivals — even when 'free'.",
     "Regulation is hard (free products, speed, data); tools: data portability, interoperability, fines, break-up (DMA, GDPR, FTC).",
     "Not inevitable: local relevance (PickMe), open infrastructure (ONDC/UPI), and shifting needs (MySpace, Nokia) break monopolies."],
    "As citizens you feel monopoly power in the fees and choices you get; as future builders and policymakers you'll decide whether to exploit, resist, or regulate it. QR interoperability shows Nepal already using these tools — the debate is live here, not just abroad.",
    "S15 — zooming out: how do we MEASURE how digital a country is? The DAI and OECD DGI.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S15
add_divider("Session 15 · Lecture hour 7 (of 7) — CLOSES UNIT 2","Measuring Digital Adoption: DAI & the OECD DGI",
    "Estonia runs 99% of its government services online; in much of Nepal you still queue with photocopies and cash. Everyone says 'go digital' — but how do we actually MEASURE how digital a country is, compare countries fairly, and see where Nepal truly stands? That's what digital-adoption indexes do.",
    "OPENING HOOK [~5 min]. Contrast Estonia's e-government with a Nepali government queue. Agenda: what digital adoption means + the World Bank DAI (3 pillars) → the OECD DGI (6 dimensions) → Nepal's position.")

concept_understand("S15 · Concept 1 · [THEORY]","Digital Adoption & the World Bank DAI",
    "Digital adoption is the effective USE of digital tools in daily life, business, and government — not merely their availability. The World Bank's Digital Adoption Index (DAI) measures it across three pillars: People (internet, smartphones, social media, digital payments), Business (cloud, e-commerce, digital accounting, automation), and Government (e-services, digital ID, tax filing, open data). It lets countries be compared and gaps identified.",
    ["Adoption ≠ access: owning a smartphone isn't adoption; USING it to transact is.",
     "Three DAI pillars: People, Business, Government — each with concrete indicators.",
     "Used by the World Bank, UN, OECD, IMF, ITU to compare digital readiness across countries.",
     "Caveat: the DAI is a framework; the last official World Bank DAI dataset is from 2016."],
    "s15_dai_pillars.png","DAI = adoption (effective USE) across 3 pillars: People · Business · Government.",
    "~7 min. Use the DAI pillar graphic. Stress adoption = usage, not access — a country can have phones but low adoption.")
add_table_slide("S15 · Concept 1 · scaffolding","The DAI's three pillars — indicators & Nepal's status",
    ["Pillar","Example indicators","Nepal status","Why"],
    [["People","Internet, smartphones, social media, payments","Moderate–High","High social/TikTok use; eSewa/Khalti growing; uneven internet quality"],
     ["Business","Cloud, e-commerce, digital accounting, automation","Low–Moderate","Digital accounting rare; e-commerce rising but informal"],
     ["Government","E-services, digital ID, tax filing, open data","Early stage","Nagarik App & online passport exist; systems not integrated"]],
    per_page=3,widths=[1.4,2.8,1.6,3.0],fs=10.5,
    note="Nepal's pattern is common for developing economies: citizens (People) adopt fastest, businesses lag, and government is slowest — the reverse of leaders like Estonia. Adoption is uneven across the three pillars.")
concept_apply("S15 · Concept 1 · [THEORY]","Digital Adoption & the DAI",
    "Nepal scores relatively well on the People pillar — high social-media use and fast-growing wallets like eSewa, Khalti, and Fonepay — but lags on Business (few SMEs use cloud accounting) and Government (services exist as apps but aren't integrated; paperwork still dominates). The DAI makes this uneven picture visible and comparable, so policymakers can target the weak pillar rather than assume 'we have phones, so we're digital'.",
    "\"If people own smartphones, the country has high digital adoption.\" Adoption is about effective USE, not ownership — and it varies by pillar. Nepal's citizens adopt fast while its businesses and government lag, so a single 'we're online' claim hides exactly where the real gaps (and opportunities) are.",
    "Digital adoption is the effective use of digital tools in daily life, business, and government — not mere availability. The World Bank's Digital Adoption Index (DAI) measures it across three pillars — People (internet, smartphones, social media, payments), Business (cloud, e-commerce, digital accounting, automation), and Government (e-services, digital ID, tax, open data) — enabling cross-country comparison and gap-spotting. Nepal is strongest on People, weaker on Business, and early-stage on Government.",
    "digital adoption = effective use · World Bank DAI · People / Business / Government pillars · Nepal uneven by pillar")

concept_understand("S15 · Concept 2 · [THEORY]","The OECD Digital Government Index (DGI)",
    "The OECD Digital Government Index (DGI) measures how modern, efficient, and citizen-focused a government's digital services are — going beyond access to quality and maturity. It has six dimensions: user-centricity (built around people), digital-by-design (born digital, not paper copied), data-driven public sector, proactiveness (government acts before you ask), government-as-a-platform (shared ID/payments/cloud), and open-by-default (transparent, open data).",
    ["User-centricity: simple, fast, mobile-friendly services (UAE's one-app government).",
     "Digital-by-design & government-as-a-platform: shared rails like India's Aadhaar/UPI, Estonia's X-Road.",
     "Proactiveness: Denmark auto-sends child benefits after a birth is registered — no application needed.",
     "Open-by-default: government data public by default (UK open-data portal, COVID dashboards)."],
    None,"OECD DGI = 6 dimensions of digital-government maturity: user-centric · digital-by-design · data-driven · proactive · gov-as-platform · open.",
    "~8 min. This is the syllabus's 'OECD digital-adoption government index'. Contrast DGI (government maturity/quality) with DAI (broad adoption across society).")
add_table_slide("S15 · Concept 2 · scaffolding","The OECD DGI — six dimensions with country examples",
    ["Dimension","What it means","Country example"],
    [["User-centricity","Services built around people, not bureaucracy","UAE: ~90% services on one app"],
     ["Digital by design","Born digital, not paper scanned to PDF","IndiaStack: Aadhaar + eKYC + UPI"],
     ["Data-driven public sector","Use data to decide & predict","Singapore: data-tuned bus frequency"],
     ["Proactiveness","Government acts before you ask","Denmark: auto child benefits after birth"],
     ["Government as a platform","Shared ID, payments, cloud rails","India UPI; Estonia X-Road"],
     ["Open by default","Transparent, public open data","UK open-data portal; gov APIs"]],
    per_page=6,widths=[1.9,2.6,2.5],fs=10.5,
    note="The DGI measures the QUALITY and maturity of digital government, not just whether services exist. 'Digital by design' vs merely scanning paper forms into PDFs is the distinction Nepal most needs to make.")
concept_apply("S15 · Concept 2 · [THEORY]","The OECD DGI",
    "Nepal's online passport and Nagarik App are real progress on access, but on the DGI they'd score low on 'digital by design' and 'government as a platform': services are often digital copies of paper processes, run on separate systems that don't share one identity or payment rail. Estonia's X-Road (all agencies interconnected) and India's Aadhaar/UPI (shared public rails) are what higher DGI maturity looks like — the target Nepal is moving toward.",
    "\"Putting government forms online is digital government.\" That's the lowest rung. The DGI's higher bar is digital-by-design (rebuilt digitally, not paper scanned), shared platforms (one ID/payment), proactiveness, and openness. A PDF of an old form on a website is access, not digital-government maturity.",
    "The OECD Digital Government Index (DGI) measures how modern, efficient, and citizen-focused a government's digital services are — quality and maturity, beyond access. Its six dimensions are user-centricity, digital-by-design (born digital, not paper copied), data-driven public sector, proactiveness (acting before asked), government-as-a-platform (shared ID/payments/cloud), and open-by-default (transparent open data). Leaders (Estonia's X-Road, India's Aadhaar/UPI, Denmark's proactive benefits) show what high maturity looks like.",
    "OECD DGI · user-centricity · digital-by-design · data-driven · proactiveness · government-as-platform · open-by-default")

concept_understand("S15 · Concept 3 · [THEORY]","DAI vs DGI, and Reading Nepal's Position",
    "The two indexes answer different questions. The DAI asks 'how much does the whole SOCIETY (people, business, government) use digital tools?' The DGI asks, more narrowly and deeply, 'how mature and citizen-focused is the GOVERNMENT's digital service?' Read together for Nepal: society-wide adoption is led by people and lagged by government; and government digital maturity is early-stage — the same message from two angles.",
    ["DAI = breadth of adoption across society (people + business + government).",
     "DGI = depth/maturity of one actor — digital government specifically.",
     "For Nepal both point the same way: strong citizen uptake, weak government maturity.",
     "Caveat: treat scores as indicative — DAI data is dated (2016) and indexes simplify reality."],
    None,"DAI = society-wide adoption (breadth); DGI = digital-government maturity (depth). Nepal: strong people, weak government.",
    "~6 min. Close the unit by connecting adoption gaps back to the fundamentals: weak business/government adoption limits the very network effects and platforms the unit studied.")
add_table_slide("S15 · Concept 3 · comparison","DAI vs OECD DGI — what each measures",
    ["Question","World Bank DAI","OECD DGI"],
    [["Measures","Adoption across society","Maturity of digital government"],
     ["Scope","People + Business + Government","Government services only"],
     ["Depth","Breadth of usage","Quality & citizen-focus"],
     ["Key question","'How digital is the country?'","'How good is digital government?'"],
     ["Nepal read","People strong, business/govt lag","Early stage (access, not by-design)"]],
    per_page=5,widths=[1.8,2.6,2.6],fs=11,
    note="Use them together: the DAI locates WHERE adoption is weak (Nepal: business & government), and the DGI explains HOW to deepen the government side (digital-by-design, shared platforms). Both say Nepal's government is the lagging pillar.")
concept_apply("S15 · Concept 3 · [THEORY]","DAI vs DGI & Nepal's Position",
    "Put together, the indexes give Nepal a clear diagnosis: citizens have adopted digital fast (wallets, social media), but businesses and — most of all — government lag, and what government digital exists is access-level, not digital-by-design. That weak government/business adoption also caps the platforms and network effects from earlier in this unit: fewer businesses online means thinner marketplaces. The fix (per the DGI) is shared public rails and rebuilt-digital services — India's UPI/ONDC direction.",
    "\"A single number tells you how digital a country is.\" No one index captures it: the DAI shows society-wide breadth, the DGI shows government depth, and both simplify (and the DAI data is dated). Read together they diagnose Nepal precisely — strong citizens, lagging government — better than any single score.",
    "The DAI and DGI answer different questions: the DAI measures adoption across the whole society (people, business, government — breadth), while the DGI measures the maturity and citizen-focus of digital government specifically (depth). For Nepal both point the same way — strong citizen uptake, lagging business and (especially) government, with government digital still access-level rather than digital-by-design. Weak business/government adoption also limits the platforms and network effects studied earlier in this unit.",
    "DAI (breadth, society) vs DGI (depth, government) · read together · Nepal: strong people, lagging government · indexes simplify")

add_activity("S15 — 'Rate Nepal, then fix a pillar'  ·  ~5 min",
    ["In pairs (3 min): rate Nepal High/Medium/Low on each DAI pillar (People, Business, Government) with a reason.",
     "Pick the weakest pillar and propose one concrete fix (borrow from Estonia or India).",
     "Take 3–4 answers aloud (2 min); compare ratings.",
     "Close: the government pillar is usually rated weakest — link to the DGI's 'digital-by-design'."],
    "Expected: People Medium–High, Business Low–Moderate, Government Early/Low. Good fixes: a shared digital ID + payment rail (like Aadhaar/UPI), digital-by-design services (not scanned PDFs), open data. Reward concrete, borrowed-best-practice answers.",
    "ACTIVITY [~5 min].")
add_quiz("S15 — Quick Check  ·  ~5 min",
    [("Q1.  The World Bank DAI measures adoption across which three pillars?","q"),
     ("a) rich/middle/poor   b) ✅ People, Business, Government   c) phones/PCs/servers   d) urban/rural/remote","a"),
     ("     Why: the DAI's three pillars are People, Business, and Government — each with its own indicators.","o"),
     ("Q2.  A government service that is a scanned PDF of an old paper form scores LOW on the DGI's:","q"),
     ("a) openness   b) ✅ 'digital by design'   c) fines   d) network effect","a"),
     ("     Why: digital-by-design means rebuilt digitally, not paper copied — a scanned form is access, not maturity.","o"),
     ("Discussion: rate Nepal on the three DAI pillars and propose a fix for the weakest.","o")],
    "QUIZ [~5 min]. Cement the DAI pillars, the DGI 'digital-by-design' idea, and Nepal's uneven position.")
add_summary("S15 · Summary  ·  [~2 min]",
    ["Digital adoption = effective USE, not access; the World Bank DAI measures it across People, Business, Government.",
     "The OECD DGI measures digital-GOVERNMENT maturity across 6 dimensions (user-centric, digital-by-design, data-driven, proactive, gov-as-platform, open).",
     "Nepal: strong on People, lagging on Business & Government — the same diagnosis from both indexes."],
    "These indexes are how governments, the World Bank, and investors judge a country's digital readiness — and where Nepal ranks shapes real policy and investment. Knowing what they measure lets you read those judgements critically and see exactly which gap to close.",
    "Next unit — Unit 3: Digital Markets, Strategy & Innovation (competition & co-opetition, the layered internet model, digital business & value-creation models).",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 2 · Cheat Sheet","One-page revision reference",
    [("Platforms (S9)","Pipe = firm makes & sells value (one way); platform = connects groups, users create value (many ways). MSP = 2+ interdependent groups, solves matching. Value via: lower transaction cost, matching, trust, tools, network value."),
     ("Network effects (S10)","Value rises as more users join → positive feedback (best-connected wins). 4 types: direct/same-side, indirect/cross-side, data, standard. Limits: congestion, spam, toxicity, surge — can reverse. Network ≠ viral."),
     ("Two-sided pricing (S11)","Charge the money side, subsidise the side that attracts it (cross-subsidy) — 'free' has a payer. High fixed + ~0 marginal cost → average cost falls with scale. Chicken-and-egg: subsidise/seed/exclusive/freemium/incentives → critical mass."),
     ("Lock-in (S12)","Flywheel = designed loop (acquire→activate→engage→retain); network effect = natural. 5 switching costs: financial, learning, data/asset, network/social, psychological. Lock-in engineered via bundling, formats, loyalty, sync, exclusives. Multi-homing weakens it."),
     ("Monopolies (S13–S14)","Winner-take-most via increasing returns; tips past a point (not always). 6 forces: network effects, scale, scope, data, low marginal cost, switching costs. Market types incl. monopsony. Risks: less innovation, privacy, price control, copying. Tools: portability, interoperability, fines, break-up. Not inevitable (PickMe, ONDC, MySpace)."),
     ("Adoption indexes (S15)","Adoption = effective USE. World Bank DAI: 3 pillars (People/Business/Government). OECD DGI: 6 dimensions of digital-government maturity (user-centric, digital-by-design, data-driven, proactive, gov-as-platform, open). Nepal: strong People, lagging Business & Government.")])

add_glossary("Unit 2 · Glossary","Key terms — quick reference",
    [("Pipe (linear) business","a firm that makes and sells its own value, one-way to customers."),
     ("Platform business","a business that connects groups so they create value for each other."),
     ("Multi-sided platform (MSP)","a model linking 2+ interdependent user groups via matching."),
     ("Transaction cost","the cost of search, negotiation & enforcement in a trade."),
     ("Network effect","a product becomes more valuable as more people use it."),
     ("Positive feedback loop","more users → more value → more users."),
     ("Direct (same-side) effect","value from more users of the same group (WhatsApp)."),
     ("Indirect (cross-side) effect","value from more users on the other side (riders↔drivers)."),
     ("Data network effect","usage → data → a better product → more users."),
     ("Standard/technology effect","a standard grows more valuable as it dominates (QR, USB-C)."),
     ("Viral effect","fast spread via sharing; not necessarily lasting value."),
     ("Negative network effect","more users REDUCE value (congestion, spam, toxicity)."),
     ("Two-sided pricing","charging one side while subsidising another."),
     ("Money side / subsidy side","the side that pays / the side kept free to attract it."),
     ("Cross-subsidy","subsidising the side that attracts the paying side."),
     ("Marginal cost","the cost of serving one more user (near-zero for digital)."),
     ("Economies of scale","average cost per user falls as the platform grows."),
     ("Economies of scope","one infrastructure/dataset serves many products."),
     ("Chicken-and-egg problem","neither side of a platform will join before the other."),
     ("Critical mass / liquidity","enough participants that the network effect self-sustains."),
     ("Flywheel","a designed positive-feedback loop (acquire→activate→engage→retain)."),
     ("Switching cost","what a user loses/spends to move to another platform."),
     ("Lock-in","high switching costs that keep users from leaving."),
     ("Walled garden","a closed ecosystem, smooth inside, hard to leave."),
     ("Multi-homing","using several competing platforms at once."),
     ("Winner-take-most","the leader captures most of the market; rivals fade."),
     ("Tipping point","when a market tips decisively to one platform."),
     ("Data advantage","more users → more data → a better product."),
     ("Monopoly / oligopoly","one / a few dominant sellers."),
     ("Monopsony / oligopsony","one / a few dominant BUYERS with market power."),
     ("Entry barrier","what makes it hard for a new competitor to enter."),
     ("Data portability","the right to take your data to a rival service."),
     ("Interoperability","requiring platforms/standards to work together."),
     ("Digital adoption","the effective USE of digital tools (not just access)."),
     ("World Bank DAI","Digital Adoption Index — People, Business, Government pillars."),
     ("OECD DGI","Digital Government Index — 6 dimensions of gov digital maturity."),
     ("Digital by design","services built digitally from the start, not paper copied.")])

# ============= CONSOLIDATED END-OF-UNIT QUIZ =============
add_divider("Unit 2 · Revision","Consolidated end-of-unit quiz",
    "Twelve MCQs across the whole unit (answers shown), then short-answer, applied-case, and discussion questions to work from the concept slides and Unit2_material.md.",
    "Use as a 15–20 min in-class quiz or take-home review. (No genuine IT 250 past-paper exists — built from the syllabus + the in-lecture recap activity.)")
add_quiz("Section A — Multiple choice (answers shown)",
    [("1.  A platform business differs from a pipe in that   →  ✅ users create the value for each other","a"),
     ("2.  A multi-sided platform connects   →  ✅ 2+ interdependent groups (solves matching)","a"),
     ("3.  Riders-attract-drivers-attract-riders is a   →  ✅ indirect / cross-side network effect","a"),
     ("4.  TikTok's feed improving with use is a   →  ✅ data network effect","a"),
     ("5.  Google is free to users because   →  ✅ advertisers (money side) pay for their attention","a"),
     ("6.  As a digital platform scales, average cost per user   →  ✅ falls (near-zero marginal cost)","a"),
     ("7.  Neither side joining first is the   →  ✅ chicken-and-egg problem","a"),
     ("8.  A flywheel differs from a network effect in that it is   →  ✅ designed, not natural","a"),
     ("9.  Losing chat history + groups if you leave = which switching costs   →  ✅ data/asset + network/social","a"),
     ("10.  'Winner-take-most' is driven by   →  ✅ increasing returns (network effects + scale + lock-in)","a"),
     ("11.  Amazon dictating terms to dependent sellers is   →  ✅ monopsony (buyer power)","a"),
     ("12.  The OECD DGI measures   →  ✅ digital-government maturity (6 dimensions)","a")],
    "Consolidated quiz Section A.",compact=True)
add_quiz("Sections B–D — short answer, applied case & discussion",
    [("Section B — Short answer","q"),
     ("13. Define a multi-sided platform + name 2 value-creation mechanisms.   14. Name the 4 network-effect types with an example each.   15. Explain cross-subsidy with one example.","o"),
     ("16. List the 6 forces behind digital monopolies.   17. Name the DAI's 3 pillars and the OECD DGI.","o"),
     ("Section C — Applied case","q"),
     ("18. Choose ONE Nepali platform (Pathao / eSewa / Daraz / Foodmandu) and analyse it on: network effect · lock-in · switching cost · monopoly risk.","o"),
     ("19. Assess Nepal on the DAI's three pillars (People / Business / Government) and justify each rating.","o"),
     ("Section D — Discussion","q"),
     ("20. 'Are digital monopolies inevitable?' Argue using tipping/winner-take-most vs the PickMe/ONDC counter-cases.","o")],
    "Consolidated quiz Sections B–D. Model answers on the concept slides and in Unit2_material.md.",compact=True)

# ---- close ----
add_title("End of Unit 2  ·  IT 250",
          "S9–S15 complete: multi-sided platforms · network effects & positive feedback · two-sided pricing (who pays/who's subsidised) · "
          "lock-in, switching costs & the flywheel · formation of monopolies (the six forces) · risks & regulation · measuring digital adoption (DAI & OECD DGI)",
          "Built to COURSE_MATERIAL_STANDARD.md incl. the §7A depth rule · comparison & concrete-example tables throughout · "
          "self-contained, PDF-safe, Nepal-localised · Next: Unit 3 — Digital Markets, Strategy & Innovation.")

_add_page_numbers()
save("IT250_Unit2.pptx")
