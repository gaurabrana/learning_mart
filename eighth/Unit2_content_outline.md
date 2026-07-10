# Unit 2 — Fundamentals of Digital Economy · Content Outline

**IT 250 Digital Economy · 7 LHs → 7 sessions (S9–S15) · 50 min each**
The **syllabus is the backbone**; the instructor's old lecture PDFs/PPTX are cross-mapped below (§0).
Local examples use Nepal / South Asia. Continues session numbering from Unit 1 (S1–S8).

> ⚠️ **Exam-alignment note:** no genuine IT 250 past-paper exists (see Unit 1). 🎯 answers are driven
> by the syllabus + the strong in-lecture recap artifacts (esp. the L7 "analyse a platform on 4 concepts"
> activity and its summary rating table — the most exam-ready item in the unit).

---

## §0. SYLLABUS ↔ OLD-MATERIAL MAPPING

Sources: **L1** Fundamentals & MSPs · **L2** Network Effects · **L3** Flywheels/Scaling/Lock-in (pptx) ·
**L4** Formation of Monopolies · **L5** Measuring Digital Adoption (indexes) · **L7** Recap.

| # | Syllabus topic | ✅ MATCH (reuse) | ⚠️ GAP (build fresh) | ➕ BONUS (beyond syllabus, keep) |
|---|---|---|---|---|
| 1 | **Multi-sided platforms: network effects & positive feedback** | **Very strong.** L1+L2: platform-vs-pipe business, MSP definition, 5 features, 5 value-creation mechanisms, revenue models, 4 types of network effect (direct / indirect-cross-side / data / standard), positive-feedback loop, negative network effects. Rich Nepal examples (eSewa, Khalti, Fonepay, Daraz, Pathao, Foodmandu, Hamrobazar). | **The two-sided PRICING economics Unit 1 deferred here** — cross-subsidy (money side vs subsidy side, why one side is free), Metcalfe-style "value ∝ users", quantitative zero-marginal-cost. Asserted but never modeled. | Flywheel framework (acquire→activate→engage→retain); "network effect vs flywheel" (natural vs designed); chicken-and-egg + 5 solutions; failure cases (Google+, Clubhouse). |
| 2 | **Lock-in and switching costs** | **Strong (L3).** 5 switching-cost types (financial, learning, data/asset, network, psychological); 5 lock-in tactics; walled gardens; multi-homing; liquidity. Nepal case cards (Pathao, eSewa, Daraz, Foodmandu) in L7. | Switching cost as a monetary **entry barrier**; a §7A consequence table (none exists yet). | Multi-flywheel platforms (Amazon); cold/warm/hot-start curve; lock-in case studies (Airbnb, Uber, OpenAI). |
| 3 | **Formation of monopolies in the digital economy** | **Very strong (L4).** Digital "winner-take-most" monopoly; 6 forces (network effects, economies of scale, economies of scope, data advantage, low marginal cost, switching costs); tipping point; entry barriers; market types incl. **monopsony/oligopsony**; risks; antitrust cases (EU DMA/GDPR, FTC); govt tools. | The **mechanism** of tipping / increasing returns (when markets tip vs support multi-homing) — asserted via "party" analogy, not modeled. | PickMe (Sri Lanka) beating Uber = "relevance > size"; India ONDC/UPI/Aadhaar as an anti-monopoly policy alternative; MySpace death case. |
| 4 | **Digital adoption index + OECD digital-adoption/e-gov index** | **Good, conceptual (L5).** World Bank **DAI** 3 pillars (People/Business/Government); **OECD DGI** all 6 dimensions (user-centricity, digital-by-design, data-driven, proactiveness, gov-as-platform, open-by-default) with examples; explicit Nepal status per pillar. | **No quantitative data** — no scores, weights, or country rankings (last WB DAI is 2016 — flag currency). Nepal position is qualitative only. | Estonia (X-Road, 99% online), IndiaStack, UAE/Singapore/Denmark proactiveness examples. |

**➕ Cross-cutting bonus:** the L7 recap **"analyse a platform on 4 concepts (network effect · lock-in · switching cost · monopoly risk)"** activity + its worked answers and summary rating table (Pathao/TikTok/eSewa/WhatsApp/Daraz/Foodmandu) → becomes the unit's capstone activity + a master comparison table.

**Two flags / open questions (proceeding with the noted default):**
1. **Which "e-government index"?** Syllabus says "OECD digital adoption government index." The material covers the **OECD Digital Government Index (DGI)** — I'll teach that (matches the syllabus wording). If the examiner means the **UN E-Government Development Index (EGDI)**, that's NOT in the old material and I'd add it — tell me if so.
2. **Terminology fix carried into the build:** an old L3 slide mislabels an Amazon example as "Uber" — corrected in the new deck.

**Locked decisions inherited from Unit 1:** Nepal policy DEPTH → Unit 6; generous slides / full §7A depth; localise to Nepal; no real past-paper (syllabus-derived 🎯). This unit ALSO absorbs the platform economics deferred from Unit 1 S1 (→ new session S11).

---

## Unit 2 learning outcomes (after S9–S15)
1. Distinguish a **platform** business from a traditional (pipe) business and define a **multi-sided platform**.
2. Explain **network effects** (direct, indirect/cross-side, data, standard) and **positive feedback**, incl. their limits (negative network effects).
3. Explain **two-sided market pricing** — cross-subsidy, the money side vs the subsidy side, and why one side is often free.
4. Explain **lock-in and switching costs** (five types), how platforms engineer them, and multi-homing.
5. Explain how **digital monopolies form** (the six forces, tipping, winner-take-most), their risks, and how they are regulated.
6. Describe how digital adoption is measured — the World Bank **DAI** (3 pillars) and the OECD **DGI** (6 dimensions) — and assess Nepal's position.

---

## S9 — Multi-Sided Platforms: Pipes vs Platforms
**Hook:** "Daraz owns almost no products, Pathao owns no taxis, Airbnb owns no hotels — yet they're worth more than firms that own everything. How does a company that MAKES nothing create so much value?"
**Concepts:** (1) Pipe (linear) vs platform business — value flows one way vs many ways; (2) Multi-sided platform definition — connects 2+ interdependent user groups, solves a matching problem, value rises with participants; (3) 5 features (facilitation not production, 2+ groups, interaction-based value, low marginal cost, scalability); (4) How platforms create value — reduce transaction costs, matching, trust/reputation, tools/infrastructure, network value; (5) Misconception: "a platform is just a website/middleman."
**§7A tables:** pipe vs platform (comparison); 5 value-creation mechanisms × Nepal example; MSP examples × the sides they connect (≥6 rows).
**Visual:** pipe-vs-platform diagram. **Image:** `s9_pipe_platform.png`.

## S10 — Network Effects & Positive Feedback
**Hook:** "Why don't we use 20 messaging apps? Why did WhatsApp win in Nepal while Viber faded? The app isn't 20× better — its USERS are."
**Concepts:** (1) Network effect — value grows as more users join; (2) 4 types — direct/same-side (WhatsApp), indirect/cross-side (Uber riders↔drivers), data (Google Maps, TikTok), standard/technology (Fonepay QR, USB-C); (3) Positive feedback loop (users→value→more users); Metcalfe intuition (value ∝ connections); (4) Negative network effects & limits — congestion, spam, toxicity, surge anger; (5) Network vs viral effects; (6) Misconception: "more users always = more value."
**§7A tables:** 4 types of network effect (comparison, + Nepal example); positive vs negative network effects (examples); network effect vs viral effect.
**Visual:** cross-side network-effect loop. **Image:** `s10_networkloop.png`.

## S11 — Two-Sided Market Economics: Who Pays, Who's Subsidised  ⭐ (fills Unit 1's deferred economics)
**Hook:** "Google Search is free, TikTok is free, Adobe Reader is free — so who pays the bill? Someone always does. Platforms are the art of charging the RIGHT side."
**Concepts:** (1) Two-sided pricing — the **money side** vs the **subsidy side**; why platforms deliberately make one side free/cheap; (2) Cross-subsidy logic — subsidise the side that attracts the valuable side (users free, advertisers pay; readers free, creators pay); (3) Zero marginal cost, quantitatively — high fixed cost, ~0 cost per extra user → average cost falls with scale (the scale economics from Unit 1 S1, now with the mechanism); (4) The chicken-and-egg problem + 5 launch strategies (subsidise a side, seed inventory, exclusive partners, freemium/no-commission, incentives); (5) Misconception: "the free side is the platform's charity / the platform loses money on it."
**§7A tables:** money side vs subsidy side (≥6 platforms → who's free, who pays, why); chicken-and-egg solutions × example; fixed vs marginal cost (traditional vs digital, scaffolding).
**Visual:** two-sided cross-subsidy diagram. **Image:** `s11_crosssubsidy.png`.

## S12 — Lock-In, Switching Costs & the Flywheel
**Hook:** "You've thought about leaving eSewa or WhatsApp for months — and haven't. It's not laziness; it's engineered. Meet the switching cost."
**Concepts:** (1) The flywheel — a DESIGNED positive-feedback loop (acquire→activate→engage→retain); network effect (natural) vs flywheel (designed); (2) Switching costs — 5 types (financial, learning/effort, data/asset, network/social, psychological/habit); (3) How platforms engineer lock-in — ecosystem bundling, proprietary formats, loyalty programs, cross-device sync, exclusive features; walled gardens; (4) Multi-homing & liquidity — when switching costs are low, flywheels weaken; (5) Misconception: "lock-in is just good service."
**§7A tables:** network effect vs flywheel (comparison); 5 switching-cost types × Nepal example × how a platform raises it; lock-in tactic × platform (examples).
**Visual:** the flywheel loop. **Image:** `s12_flywheel.png`.

## S13 — Formation of Monopolies in the Digital Economy
**Hook:** "Once everyone's on the platform, everyone HAS to be on the platform. In digital markets the leader doesn't just win — it often takes (almost) all. Why?"
**Concepts:** (1) Digital monopoly = "winner-take-most" (not 100% control); (2) The 6 forces — network effects, economies of scale, economies of scope, data advantage, low/zero marginal cost, high switching costs; (3) Tipping point & increasing returns — when a market tips vs when it supports multi-homing; (4) Entry barriers (server/talent cost, un-replicable data, habits, ecosystem dependence, compliance); (5) Market types — monopoly / oligopoly / monopolistic competition / **monopsony / oligopsony** (buyer power: Amazon, YouTube, ad-space buyers); (6) Misconception: "digital monopolies win purely by being best/cheapest."
**§7A tables:** the 6 forces × how each pushes toward monopoly × example; market types (comparison, incl. monopsony); winner-take-most vs contestable market (when does it tip?).
**Visual:** tipping-point / winner-take-most curve. **Image:** `s13_tipping.png`.

## S14 — Monopoly Risks, Regulation & the Counter-Narrative
**Hook:** "A monopoly that gives you free search and cheap delivery — what's the harm? And if Google's 'free', how does a regulator even prove you were hurt?"
**Concepts:** (1) Risks — less innovation, privacy/data concentration, price control (Apple's 30% tax), biased algorithms, copying/killing rivals (Stories→Reels); (2) Why regulating digital monopolies is hard — "free" products, fast markets, unclear data ownership; (3) Government tools — data portability, interoperability, fines, break-ups; real cases (EU Digital Markets Act, GDPR, US FTC vs Amazon/Google); (4) The counter-narrative — **PickMe (Sri Lanka) beat Uber on relevance not size**; India's **ONDC/UPI/Aadhaar** as open alternatives to platform dominance; (5) Misconception: "digital monopolies are permanent/unbeatable" (MySpace, Nokia).
**§7A tables:** monopoly benefit vs risk (two-sided, consequence column); regulatory tool × what it does × real case; "inevitable monopoly?" — counter-cases (examples).
**Visual:** none new (uses tables). *(reuse s13 if needed)*

## S15 — Measuring Digital Adoption: DAI & the OECD DGI
**Hook:** "Estonia runs 99% of government online; in Nepal you still queue with photocopies. How do we MEASURE how digital a country really is — and where does Nepal actually stand?"
**Concepts:** (1) Digital adoption = effective USAGE, not just access; (2) World Bank **Digital Adoption Index (DAI)** — 3 pillars: People, Business, Government (indicators each); (3) OECD **Digital Government Index (DGI)** — 6 dimensions (user-centricity, digital-by-design, data-driven, proactiveness, government-as-platform, open-by-default) with country examples; (4) Nepal's status — People: moderate–high; Business: low–moderate; Government: early-stage — with why; (5) Misconception: "having the technology = adoption."
**§7A tables:** DAI 3 pillars × indicators × Nepal status; OECD DGI 6 dimensions × meaning × country example; DAI vs DGI (what each measures).
**Visual:** DAI 3-pillar + Nepal status graphic. **Image:** `s15_dai_pillars.png`.

---

## 📋 Unit 2 — End-of-Unit Quiz
**A — MCQ (12):** pipe vs platform; MSP definition; the 4 network-effect types; positive feedback; money side vs subsidy side; chicken-and-egg; the 5 switching-cost types; flywheel vs network effect; the 6 monopoly forces; monopsony; a regulatory tool; DAI's 3 pillars / DGI's dimensions.
**B — Short answer (5):** define a multi-sided platform; name & give an example of each network-effect type; explain cross-subsidy with one example; list the 6 forces behind digital monopolies; name the 3 DAI pillars and the OECD DGI.
**C — Applied (2):** (i) the L7 capstone — analyse ONE Nepali platform (Pathao/eSewa/Daraz/Foodmandu) on network effect + lock-in + switching cost + monopoly risk; (ii) assess Nepal on the DAI's 3 pillars.
**D — Discussion (1):** "Are digital monopolies inevitable? Argue using tipping vs PickMe/ONDC counter-cases."

## Open questions before/while building
1. **OECD DGI vs UN EGDI** — proceeding with **OECD DGI** (matches syllabus wording + old material). Confirm or redirect.
2. 7 sessions (S9–S15) OK? (Platforms/network effects get 3 sessions incl. the deferred economics; monopolies 2; lock-in 1; indexes 1 — matches material density.)
