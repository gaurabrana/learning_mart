# IT 250 — Unit 3: Digital Markets, Strategy & Innovation
### Full Lecturer-Ready Session Material (S16–S25)

**Program:** BIM, 8th Semester · **Unit weight:** 10 lecture hours
**Sessions:** S16–S25 (50 min each) · **Local context:** Nepal / South Asia
**Format:** Markdown — source of truth; the built deck is `IT250_Unit3.pptx`, regenerated via `build_unit3_pptx.py` (imports `deckkit.py`). Built to **COURSE_MATERIAL_STANDARD.md** — self-contained, PDF-safe, and carrying the **§7A depth tables** (every confusable set → a comparison table; every "X vs not-X" idea → a concrete-example table with ≥6 Nepal-localised rows). Localised to Nepal's digital economy. Continues session numbering from Unit 2 (S9–S15).

> **How to read this file.** This is written to **carry a full 50 minutes on its own.** Each session
> has the actual **explanation to deliver** (prose, not just bullets), a **worked Nepal example**, a
> **common misconception + correction**, a **🎯 exam-ready answer**, the embedded **§7A depth table(s)**,
> a **timed in-class activity**, and lecturer cue cards in `> 🎙️` blocks. `[SLIDE]` marks slide-ready
> blocks; `🖼️` marks diagram cues. Pace tags: `[THEORY] [EXAMPLE] [ACTIVITY] [QUIZ]`.
> Total per session: **5 + 35 + 5 + 3 + 2 = 50 min.** The 31 depth tables below are the SAME ones
> generated in `build_unit3_pptx.py`, so this source and the deck stay in sync.

> ⚠️ **Exam-alignment note.** **No genuine IT 250 past-paper was available.** Every **🎯 exam-ready
> answer** and the end-of-unit quiz are derived from the **syllabus wording + the concept slides + the
> in-lecture prompts**. Treat the framings as strong model answers, and update them if a real IT 250
> paper surfaces.

> 📌 **Scope decisions locked for this unit.** (1) This unit **builds on Unit 2** — network effects,
> two-sided markets, and tipping are **cross-referenced, not re-derived.** (2) Fresh academic frameworks
> the old lecture PDFs omit are added lightly for rigor: **Porter's Five Forces** (S17), the
> **Brandenburger–Nalebuff Value-Net** for co-opetition (S19), **disruptive innovation** (Christensen,
> S21), and the classic **Stabell–Fjeldstad value chain / value shop / value network** (S23).
> (3) "**Strategy**" is in the unit title (lecture hours 9–10) though not one of the six syllabus
> bullets, so it gets a dedicated closing session, **S25**, which also integrates all dimensions.

---

## Unit 3 — Learning Outcomes
By the end of this unit, students will be able to:
1. **Describe digital markets** — their four characteristics, five components, and five types (S16).
2. **Distinguish competition, cooperation & co-opetition**, and explain why digital markets reward cooperation (S17–S19).
3. **Explain the layered internet model** (infrastructure/platform/application) and why layer control confers power (S20).
4. **Define digital innovation**, its types and enablers, and distinguish innovation from invention (sustaining vs disruptive) (S21).
5. **Compare digital business models** (the 10) and **value-creation models** (incl. value chain/shop/network) (S22–S23).
6. **Explain how digital markets are modelled** — pricing, dynamic pricing, two-sided markets, tipping (S24).
7. **Explain digital strategy** — value capture, ecosystem strategy, control points — and integrate all dimensions (S25).

> This is Unit 3 of IT 250. Unit 2 opened the **engine room** (why platforms win). Unit 3 zooms out to
> the **market**: how digital firms compete AND cooperate, how the internet is layered, how they
> innovate, the business and value models they run on, and the **strategy** that ties it together. It
> feeds Unit 4 (digital transformation & currencies), Unit 5 (economics of information), and Unit 6
> (digitalization — the Nepalese perspective).

---
---

# S16 — Introduction to Digital Markets
**Lecture hour 1 of 10 (Unit 3) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] **"The market that never closed and you never left"**

> **Deliver (≈2 min):** "Fifty years ago a *market* was a physical place — Asan Bazaar, a shop, a mandi —
> where you went, haggled, and carried goods home. Today you buy a phone on **Daraz** at midnight, pay
> with **eSewa**, and a rider brings it tomorrow. The market never closed and you never left home."
>
> **Run the question (≈3 min):** "What exactly IS a digital market, and how is it different from the
> bazaar?" Agenda: what a digital market is + its 4 characteristics → the 5 components → the 5 types.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — What a Digital Market Is + 4 Characteristics `[THEORY]` `[~7 min]`
[SLIDE] **Buyers + sellers meeting online — speed, scale, network effects, low marginal cost**

> **Deliver:** **A digital market is an online space where buyers and sellers discover each other, agree a
> price, and transact — matched, priced, and settled electronically instead of in a physical place.**
> Four characteristics set it apart: **SPEED** (near-instant search and transactions, 24/7), **SCALE**
> (reach beyond geography), **NETWORK EFFECTS** (more users make it more valuable — from Unit 2), and
> **LOW MARGINAL COST** (serving one more buyer costs almost nothing).

- 🇳🇵 **Local example:** **Daraz** — at midnight you search thousands of products (speed), from sellers
  across Nepal you'd never reach on foot (scale), on a platform more useful because millions already shop
  there (network effect), and Daraz adds your order at almost no extra cost (low marginal cost). Asan
  Bazaar has none of these four at once — that is the leap from bazaar to platform.

> ❌ **Misconception:** *"A digital market is just a shop with a website."*
> ✅ **Correction:** "A website is a shopfront. A digital market is where independent buyers and sellers
> actually **meet, match, price, and settle online** — with speed, geography-free scale, network effects,
> and near-zero marginal cost. Those four traits, not the web address, make it a market."

> 🖼️ Visual: `s16_digital_market.png` — buyers ↔ digital market ↔ sellers, resting on the 5 components.

> 🎯 **Exam-ready answer:** "A digital market is an online space where buyers and sellers discover each
> other, agree a price, and transact electronically rather than in a physical place. Four characteristics
> distinguish it: **speed** (instant, 24/7), **scale** (beyond geography), **network effects** (more users
> add value), and **low marginal cost** (serving one more user is almost free)."

**📊 Depth table — Traditional market vs digital market**

| Dimension | Traditional market | Digital market |
|---|---|---|
| Where it happens | A physical place (shop, bazaar) | An online platform (app/website) |
| Hours & speed | Opening hours; slow search | 24/7; near-instant search & pay |
| Reach | Local, limited by geography | National/global, geography-free |
| Cost of one more sale | Real (space, stock, staff) | Near-zero (a listing, a login) |
| Information | Scarce; you must ask around | Abundant: prices, reviews, ratings |
| Value with more users | Roughly flat | Rises (network effects) |

*ℹ️ The four characteristics — speed, scale, network effects, low marginal cost — are exactly the columns where a digital market pulls away from the bazaar. They are why online markets grow so fast.*

#### Concept 2 — The 5 Components of a Digital Market `[THEORY]` `[~7 min]`
[SLIDE] **Platform · payments · logistics · data & analytics · support/trust**

> **Deliver:** A digital market runs on **five components** working together. (1) The **PLATFORM** hosts
> the marketplace and matches sides. (2) **PAYMENTS** move money safely (wallets, gateways, banks).
> (3) **LOGISTICS** deliver goods (couriers, tracking, warehouses). (4) **DATA & ANALYTICS** power search,
> recommendations, pricing, and fraud checks. (5) **SUPPORT & TRUST** (ratings, returns, help desks,
> dispute resolution) keep strangers transacting. A missing component breaks the market.

- 🇳🇵 **Local example:** When you order on **Daraz**, all five fire — the platform lists and matches,
  Khalti/eSewa or cash-on-delivery handles payment, a Pathao/Aramex rider delivers, data decides what you
  saw and flags fraud, and ratings + a return policy give you confidence. Remove one — delivery fails
  outside the valley — and the market stops working there.

> ❌ **Misconception:** *"The platform IS the digital market."*
> ✅ **Correction:** "The platform is only one of five components. Payments, logistics, data, and trust are
> equally load-bearing. In Nepal, logistics (last-mile delivery) and trust (fake products) — not the app —
> are usually what limit growth."

> 🎯 **Exam-ready answer:** "A digital market runs on five components: platform (hosts & matches), payments
> (eSewa/Khalti/Fonepay), logistics (couriers, tracking), data & analytics (search, recommendations,
> pricing, fraud), and support & trust (ratings, returns, disputes). It is only as strong as its weakest
> component — in Nepal usually logistics or trust."

**📊 Depth table — The 5 components — with Nepal examples**

| Component | What it does | Nepal example |
|---|---|---|
| Platform | Hosts listings, search & matching | Daraz app, Foodmandu, Hamrobazar |
| Payments | Moves money safely | eSewa, Khalti, Fonepay, ConnectIPS |
| Logistics | Delivers goods, tracks orders | Pathao/Aramex couriers, Daraz hubs |
| Data & analytics | Search, recommendations, pricing, fraud | Daraz recommendations; surge pricing |
| Support & trust | Ratings, returns, help, disputes | Seller ratings, return policy, call centre |

*ℹ️ A digital market is only as strong as its weakest component. In Nepal, payments and platforms are mature, but logistics (last-mile outside cities) and trust (fake products) are the common weak links.*

#### Concept 3 — The 5 Types of Digital Market `[THEORY]` `[~7 min]`
[SLIDE] **B2C · B2B · C2C · C2B · P2P**

> **Deliver:** Digital markets are classified by **WHO transacts with WHOM.** **B2C** (business→consumer:
> Daraz, Netflix). **B2B** (business→business: cloud, wholesale). **C2C** (consumer→consumer: Hamrobazar,
> Facebook Marketplace). **C2B** (consumer→business: a freelancer on Fiverr, a creator). **P2P**
> (peers share/exchange directly: Airbnb, InDrive). A single platform can span types — Daraz is mainly B2C
> but its marketplace sellers add C2C/B2B.

- 🇳🇵 **Local example:** **Hamrobazar is C2C** — ordinary Nepalis buy and sell used goods to each other,
  with the platform providing the meeting place and trust tools. **Daraz** is mainly B2C but becomes
  C2C/B2B where independent sellers list. A Nepali designer selling gigs on Fiverr is **C2B**. Naming the
  type tells you instantly who the paying customer is.

> ❌ **Misconception:** *"All e-commerce is B2C."*
> ✅ **Correction:** "B2C is only one of five types. C2C (Hamrobazar), C2B (freelancers), B2B (cloud/
> wholesale), and P2P (Airbnb/InDrive) are all digital markets with different customers and money flows."

> 🎯 **Exam-ready answer:** "Digital markets are classified by who transacts with whom: B2C, B2B, C2C, C2B,
> and P2P. Many platforms are hybrids (Daraz is B2C for its own stock, C2C/B2B for third-party sellers), so
> identify the dominant relationship first."

**📊 Depth table — The 5 types of digital market — Nepal & global**

| Type | Who → who | Example |
|---|---|---|
| B2C | Business sells to consumers | Daraz, Foodmandu, Netflix, Sastodeal |
| B2B | Business sells to business | AWS/cloud, wholesale portals, SaaS tools |
| C2C | Consumer sells to consumer | Hamrobazar, Facebook Marketplace, eBay |
| C2B | Consumer sells to business | Freelancers on Fiverr/Upwork; stock photos |
| P2P | Peers share/exchange directly | Airbnb (rooms), InDrive, ride/asset sharing |

*ℹ️ The type tells you who the customer is and how money flows. Many real platforms are hybrids — Daraz is B2C for its own stock and C2C/B2B for third-party sellers — so name the DOMINANT relationship first.*

#### 🛠 ACTIVITY — "Classify the market" `[ACTIVITY]` `[~5 min]`
> **Run it:** In pairs (2 min) pick 3 Nepali digital services; for each name its **type** and the 5
> components it relies on, flagging any weak component. Take 3 answers aloud (3 min).

> 🎙️ Good answers: Daraz = B2C (weak: logistics + trust); Hamrobazar = C2C (weak: trust/escrow);
> Foodmandu = B2C (weak: rider logistics at peak). Reward the DOMINANT type + a real weak component.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`
**MCQ 1.** Which is NOT one of the four characteristics of a digital market?
a) speed  b) scale  c) ✅ **high marginal cost per user**  d) network effects
*(Why: digital markets have LOW, near-zero marginal cost — the opposite of high.)*

**MCQ 2.** People buying and selling used phones to each other on Hamrobazar is:
a) B2C  b) ✅ **C2C (consumer-to-consumer)**  c) B2B  d) C2B
*(Why: both sides are consumers; the platform only provides the meeting place and trust.)*

**Discussion prompt:** *Pick a Nepali platform — name its type and its weakest of the 5 components.*

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** every Nepali digital business you use is one of these types running on these
five components. Spotting the type and the weak component is exactly how a founder finds a gap (better
rural logistics) or how you assess where a platform is fragile.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. A digital market matches buyers & sellers online; 4 traits: **speed, scale, network effects, low marginal cost.**
2. It runs on **5 components** (platform, payments, logistics, data & analytics, support/trust) — only as strong as the weakest.
3. **Five types** by who-sells-to-whom: **B2C, B2B, C2C, C2B, P2P** — many platforms are hybrids.

**Next session (S17):** how digital markets **compete** — and winner-take-most.

---
---

# S17 — Competition in Digital Markets
**Lecture hour 2 of 10 (Unit 3) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] **"Ten rice shops vs one search engine"**

> **Deliver (≈2 min):** "In Asan, ten shops sell the same rice and compete on price and a friendly smile.
> Online, one search engine has ~90% of the world and one messenger owns Nepal. Why does online
> competition so often end with ONE big winner, when the bazaar keeps many sellers alive?"
>
> **Run (≈3 min):** Agenda: traditional vs digital competition (+ a light Porter's Five Forces) →
> winner-take-most & dominance → effects on consumers & startups.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Traditional vs Digital Competition `[THEORY]` `[~8 min]`
[SLIDE] **From price/place/quality to data, network, speed, UX — global & concentrated**

> **Deliver:** Traditional firms compete mainly on **price, location, and product quality** within a local
> area. Digital firms compete on **data, network size, speed of innovation, ecosystem, and user
> experience** — often globally and at near-zero marginal cost. A useful lens is **Porter's Five Forces**
> (rivalry, new entrants, buyer power, supplier power, substitutes): online, low entry cost raises the
> threat of new entrants, but network effects and data raise the barriers protecting the leader — so
> competition is **fiercer AND more concentrated.**

- 🇳🇵 **Local example:** Two Kathmandu grocery shops compete on price and location. **Daraz vs a new
  e-commerce startup** is different — Daraz competes with data (it knows what you buy), a huge seller
  network, faster feature updates, and switching costs (saved cards, order history). The startup can copy
  the app in months but cannot copy Daraz's network or data, so digital competition concentrates.

> ❌ **Misconception:** *"Online competition is just offline competition with a website."*
> ✅ **Correction:** "The BASIS changes — from price/location to data, network size, speed, and UX, at
> global scale and near-zero marginal cost. Porter's five forces still apply, but network effects and data
> tilt them toward whoever leads — so digital markets concentrate far more than the bazaar."

> 🎯 **Exam-ready answer:** "Traditional firms compete on price, location, and quality locally; digital
> firms compete on data, network size, speed, ecosystem, and user experience, usually globally and at
> near-zero marginal cost. Porter's Five Forces still apply, but easy entry raises the entrant threat
> while network effects and data raise the incumbent's moat — making competition both fiercer and more
> concentrated."

**📊 Depth table — Traditional competition vs digital competition**

| Dimension | Traditional competition | Digital competition |
|---|---|---|
| Basis | Price, location, product quality | Data, network size, UX, speed of innovation |
| Reach | Local / regional | National / global |
| Speed | Slow (months to react) | Fast (features ship in days) |
| Cost of growth | High (each unit costs) | Low (near-zero marginal cost) |
| Switching cost for buyer | Low (walk to next shop) | Often high (data, habit, network) |
| Role of data | Minor | Central — a competitive weapon |
| Typical outcome | Many firms coexist | Winner-take-most (one dominant) |

*ℹ️ Same five Porter forces, different strengths: online entry is cheap (more entrants) yet network effects and data build high moats (fewer survive) — which is why digital competition is both fiercer and more concentrated.*

**📊 Depth table — Porter's Five Forces — the digital twist**

| Force | What it asks | Digital twist (example) |
|---|---|---|
| Rivalry among firms | How intense is competition? | Fierce but often winner-take-most (search) |
| Threat of new entrants | How easy to enter? | Easy to start, hard to scale vs network effects |
| Buyer power | Can buyers push back? | High — reviews & one-click switching (small items) |
| Supplier power | Can suppliers squeeze you? | Sellers depend on the platform (low power) |
| Threat of substitutes | Is there another way? | Many apps substitute (super-apps absorb them) |

*ℹ️ Porter's framework still works as a checklist, but network effects, data, and low marginal cost bend every force toward the incumbent once a platform gets ahead — the moat, not the smile, wins online.*

#### Concept 2 — Winner-Take-Most & Platform Dominance `[THEORY]` `[~7 min]`
[SLIDE] **Increasing returns tip many markets to one leader — but not all**

> **Deliver:** In many digital markets, competition ends in **winner-take-most** — the leader captures the
> bulk, one small rival survives, and the rest fade. This is the same mechanism as **Unit 2's tipping:**
> network effects + economies of scale + switching costs create **increasing returns**, so being slightly
> ahead compounds into dominance. But **not every market tips** — where multi-homing is easy and needs are
> local (ride-hailing, food delivery), several players coexist.

- 🇳🇵 **Local example:** Nepal's **messaging** market tipped to WhatsApp — once contacts settled there its
  value rose for everyone and Viber faded (high network effects, high switching cost, little multi-homing).
  **Ride-hailing** has NOT tipped: Pathao and InDrive coexist because drivers and riders happily run both
  apps and needs are local. Same economy, opposite outcomes.

> ❌ **Misconception:** *"Every digital market ends in one monopoly."*
> ✅ **Correction:** "Only markets with strong network effects, high switching costs, and little
> multi-homing tip to one winner (search, messaging). Where multi-homing is easy and needs differ
> (ride-hailing, food), several persist. Tipping is a tendency, not a law."

> 🎯 **Exam-ready answer:** "Digital competition often ends in winner-take-most — the leader takes the bulk,
> a small rival survives — driven by increasing returns (network effects + scale + switching costs, from
> Unit 2). Past a tipping point the leader is hard to beat. But where multi-homing is easy and needs local,
> several coexist. WhatsApp tipped in Nepal; ride-hailing did not."

**📊 Depth table — Nepali digital markets — tipped vs contested**

| Market | Leader(s) | Tipped or contested? | Why |
|---|---|---|---|
| Search | Google | Tipped (global) | Strong data + habit; no reason to multi-home |
| Messaging | WhatsApp/Viber | Tipped to WhatsApp | Contacts settled on one; high switching cost |
| Digital wallet | eSewa, Khalti | Concentrating | Network + merchant lock-in, but 2-3 survive |
| Ride-hailing | Pathao, InDrive | Contested | Easy multi-homing; local, low switching cost |
| Food delivery | Foodmandu, Pathao | Contested | Restaurants & riders multi-home; local needs |
| E-commerce | Daraz | Leading, not sole | Scale + data lead, but niche sellers persist |

*ℹ️ Same country, different outcomes: search and messaging tip to one winner (strong effects, high switching); ride-hailing and food delivery stay contested (easy multi-homing, local needs). Knowing which is a strategic and regulatory question.*

#### Concept 3 — Effects on Consumers & Startups `[THEORY]` `[~6 min]`
[SLIDE] **Cheaper & better early, fewer choices after tipping; easy launch, hard scale**

> **Deliver:** Digital competition is **double-edged.** For **CONSUMERS**, early competition brings lower
> prices, more choice, better service — but once a market tips, dominance can mean fewer choices, data
> harvesting, and gatekeeper-set terms. For **STARTUPS**, low entry cost makes launching easy but scaling
> against an incumbent's network effects and data is brutally hard. Result: many launch, few reach critical
> mass.

- 🇳🇵 **Local example:** Nepal's **wallet war** gave consumers cashbacks and free transfers while eSewa and
  Khalti fought. But a new wallet startup faces the trap: launching an app is cheap, pulling users off the
  incumbent's merchant network is nearly impossible. So many Nepali startups don't fight head-on — they
  integrate (build on Fonepay rails) or serve a niche the giant ignores (the S18 logic).

> ❌ **Misconception:** *"Competition is always good for consumers, always bad for big firms."*
> ✅ **Correction:** "Competition helps consumers EARLY (price, choice), but a tipped market can reduce
> choice and set terms. And low entry cost flatters startups — the hard part is scaling against the moat,
> not launching. Dominance is double-edged for both sides."

> 🎯 **Exam-ready answer:** "Digital competition is double-edged. Consumers gain lower prices, more choice,
> and better service while competition is fierce, but a tipped market brings fewer alternatives, data
> harvesting, and gatekeeper terms. Startups find it cheap to launch but hard to scale against network
> effects and data — so most cannot reach critical mass, and many cooperate or find niches instead (S18)."

**📊 Depth table — Dominance: effect on consumers vs startups**

| Aspect | Effect on consumers | Effect on startups |
|---|---|---|
| Early competition | Lower prices, more choice | Easy, cheap to launch |
| After tipping | Fewer alternatives, lock-in | Hard to scale vs incumbent moat |
| Data | Personalised service… | …but incumbent's data edge is un-catchable |
| Innovation | Fast at first, can stall later | Must find a niche the giant ignores |
| Prices/terms | Gatekeeper can raise fees/terms | Commissions & platform rules squeeze margins |

*ℹ️ The same dominance that once delivered cheap, convenient service can later reduce choice and squeeze the small players who depend on the platform — which is exactly why Nepali startups so often COOPERATE rather than fight head-on (S18).*

#### 🛠 ACTIVITY — "Will it tip, and who wins?" `[ACTIVITY]` `[~5 min]`
> **Run it:** In pairs (3 min) pick a Nepali market; decide tip-or-contested using network effects,
> switching cost, multi-homing; name one effect on consumers and one on a startup entrant. Take 3–4
> answers (2 min).

> 🎙️ Messaging/search tip (strong effects, high switching); ride-hailing/food stay contested (easy
> multi-homing). Consumers gain early then risk lock-in; startups launch easily but struggle to scale.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`
**MCQ 1.** Compared with a bazaar, digital competition is mainly fought on:
a) rent & smiles  b) ✅ **data, network size, speed & user experience**  c) shop location  d) shouting
*(Why: online the basis shifts from price/location to data, network, speed, UX — often global.)*

**MCQ 2.** Ride-hailing in Nepal stays contested (Pathao + InDrive) mainly because:
a) weak apps  b) ✅ **easy multi-homing & local needs**  c) no network effects at all  d) government rule
*(Why: drivers/riders run both apps and needs are local, so the market does not tip to one.)*

**Discussion prompt:** *Name a Nepali market that tipped and one that stayed contested — why?*

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** it explains why Nepal tends to get one dominant player per category and why
challengers struggle — and it sets up the surprising survival strategy of the next three sessions: in
digital markets, firms often **cooperate** with rivals rather than only fight them.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. Digital competition shifts the basis to **data, network size, speed & UX** — global, near-zero marginal cost.
2. **Winner-take-most** via increasing returns (Unit 2 tipping) — but easy multi-homing & local needs keep some markets contested.
3. Double-edged: consumers gain early then risk lock-in; startups launch easily but struggle to scale vs the moat.

**Next session (S18):** the counter-move — **cooperation** in digital markets, and "grow the pie first."

---
---

# S18 — Cooperation in Digital Markets
**Lecture hour 3 of 10 (Unit 3) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] **"Rivals sharing the very pipes they compete on"**

> **Deliver (≈2 min):** "eSewa and Khalti are rivals — yet both settle through the same NCHL/ConnectIPS
> rails, and any wallet can scan a Fonepay QR. Rivals sharing the very pipes they compete on sounds mad in
> the bazaar. Online it is normal, even necessary."
>
> **Run (≈3 min):** Agenda: what cooperation is + why digital encourages it → the 5 reasons ("grow the pie
> first") → the 3 forms.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — What Cooperation Is + Why Digital Encourages It `[THEORY]` `[~7 min]`
[SLIDE] **Create value together — via modularity, APIs, network effects & convenience**

> **Deliver:** **Cooperation is when firms work together — sharing infrastructure, standards, data, or
> customers — to create value they could not create alone.** Digital markets encourage it more than
> traditional ones for four reasons: **MODULARITY** (products are interchangeable parts that must
> interconnect), **APIs** (software makes plugging systems together cheap), **NETWORK EFFECTS** (a shared
> standard grows everyone's value), and **CONVENIENCE** (users want one seamless experience).

- 🇳🇵 **Local example:** Nepal's banks jointly built and fund **NCHL/ConnectIPS** — shared rails no single
  bank would build alone. Because payments are modular and API-connected, and a common standard is worth
  more to everyone (network effect), rivals cooperate on the plumbing. **QR interoperability** is the
  clearest case: eSewa, Khalti, and banks agreed a common QR so any customer can pay any merchant.

> ❌ **Misconception:** *"Cooperating with a competitor is always a mistake."*
> ✅ **Correction:** "In digital markets, shared standards and rails enlarge the whole market via network
> effects, and modular/API architecture makes interconnection cheap. Firms cooperate on the infrastructure
> (pipes) while still competing on the product (app and customers)."

> 🎯 **Exam-ready answer:** "Cooperation is firms working together — sharing infrastructure, standards,
> data, or customers — to create value none could alone. Digital markets encourage it because of modularity,
> APIs, network effects, and convenience. Nepal's banks cooperating on ConnectIPS and QR interoperability
> shows the logic."

**📊 Depth table — Why digital markets encourage cooperation — cause → effect**

| Driver | Why it pushes firms to cooperate | Nepal example |
|---|---|---|
| Modularity | Products are parts that must interconnect | Wallet + bank + biller must link up |
| APIs | Plugging systems together is cheap & fast | eSewa integrating a bank via API |
| Network effects | A shared standard grows everyone's value | QR interoperability (any wallet, any QR) |
| Convenience | Users want one seamless experience | Pay any biller from one wallet app |
| Cost sharing | Building rails alone is too expensive | Banks jointly funding NCHL/ConnectIPS |

*ℹ️ In the bazaar, helping a rival is loss. Online, shared standards and rails make the WHOLE market bigger and cheaper to serve — so cooperating on the plumbing while competing on the product is rational.*

#### Concept 2 — The 5 Reasons to Cooperate ("Grow the Pie First") `[THEORY]` `[~7 min]`
[SLIDE] **Grow the market · share cost/risk · access capabilities · set standards · speed & reach**

> **Deliver:** Firms cooperate for five concrete reasons: (1) **GROW THE MARKET** — a bigger cashless pie
> helps every wallet before they fight for slices; (2) **SHARE COST & RISK** — build rails no one can afford
> alone; (3) **ACCESS CAPABILITIES** — borrow a partner's logistics, licence, or user base; (4) **SET
> STANDARDS** — agree a common format so the market interoperates; (5) **SPEED & REACH** — enter or scale
> faster together. The mindset: **"grow the pie first, then compete for slices."**

- 🇳🇵 **Local example:** **Daraz** doesn't own a fleet — it partners with **Pathao/Aramex** (accessing a
  capability) rather than building logistics alone. Nepali wallets jointly promote "go cashless" (growing
  the market) and co-fund shared rails (sharing cost & risk). In a small market like Nepal, cooperation is
  often the only way any player reaches scale.

> ❌ **Misconception:** *"Firms only cooperate when they're weak."*
> ✅ **Correction:** "Cooperation is deliberate strategy for the strong too: grow the total market, share
> cost, borrow capabilities, set standards, move faster. Enlarging the market first often beats fighting
> over today's small one."

> 🎯 **Exam-ready answer:** "Firms cooperate to grow the market, share cost and risk, access capabilities,
> set standards, and gain speed and reach — 'grow the pie first, then compete for slices.' In a small market
> like Nepal, cooperation is often survival, not luxury."

**📊 Depth table — The 5 reasons to cooperate — with payoff**

| Reason | What the firm gains | Nepal example |
|---|---|---|
| Grow the market | A bigger total pie for all | Wallets pushing 'go cashless' together |
| Share cost & risk | Afford what none could alone | Banks co-funding NCHL/ConnectIPS |
| Access capabilities | Borrow a partner's strength | Daraz using Pathao/Aramex for delivery |
| Set standards | An interoperable market | Common QR standard across wallets |
| Speed & reach | Enter/scale faster | A bank + fintech co-launching a product |

*ℹ️ Each reason is a payoff: cooperation is not charity but strategy. 'Grow the pie first, then compete for slices' — in a small market like Nepal, cooperation is often the only way any player reaches scale.*

#### Concept 3 — The 3 Forms of Cooperation `[THEORY]` `[~7 min]`
[SLIDE] **Joint platforms · partnerships · service integration**

> **Deliver:** Cooperation takes three main forms. (1) **JOINT PLATFORMS / shared infrastructure** — rivals
> build or use common rails (NCHL, ConnectIPS, SWIFT, a shared QR). (2) **PARTNERSHIPS** — combine strengths
> through co-branding, logistics deals, or joint marketing. (3) **SERVICE INTEGRATION** — one service embeds
> another for a seamless experience (pay a utility bill inside a wallet; log in with Google). The forms
> stack.

- 🇳🇵 **Local example:** **eSewa** lets you pay NEA bills and Ncell top-ups inside the app (service
  integration); **Daraz** partners with Pathao/Aramex (logistics partnership); every wallet plugs into
  **NCHL/ConnectIPS** (joint platform). Often all three stack while firms still compete for the customer.

> ❌ **Misconception:** *"Cooperation means merging or becoming friends."*
> ✅ **Correction:** "It has three concrete forms — joint platforms, partnerships, service integration —
> none requiring a merger. Firms stay independent rivals while cooperating on specific layers — the setup
> for co-opetition (S19)."

> 🎯 **Exam-ready answer:** "Cooperation takes three forms: joint platforms/shared infrastructure (NCHL,
> ConnectIPS, SWIFT, shared QR), partnerships (co-branding, logistics, marketing — Daraz + a courier), and
> service integration (embedding one service in another — bill payment in a wallet, 'login with Google').
> The forms stack while firms stay independent."

**📊 Depth table — The 3 forms of cooperation — Nepal examples**

| Form | How it works | Nepal / global example |
|---|---|---|
| Joint platform | Rivals share common rails/standards | NCHL, ConnectIPS, SWIFT, shared QR |
| Partnership (logistics) | Combine delivery strengths | Daraz + Pathao/Aramex couriers |
| Partnership (co-brand) | Two brands launch together | Bank + fintech co-branded card/wallet |
| Partnership (marketing) | Joint campaigns/cashback | Wallet + merchant festival offers |
| Service integration | Embed one service in another | Pay NEA/water bills inside eSewa/Khalti |
| Service integration | Single sign-on / embedded pay | 'Login with Google'; in-app Fonepay |

*ℹ️ These forms explain HOW Nepali firms cooperate in practice — and they set up S19: when firms cooperate on the rails (upstream) while competing for customers (downstream), that is co-opetition.*

#### 🛠 ACTIVITY — "Design a cooperation" `[ACTIVITY]` `[~5 min]`
> **Run it:** In pairs (3 min): you run a small Nepali fintech. Pick a rival/partner, choose the **form**
> and a **reason**, and state what you'd still compete on. Take 3–4 answers (2 min).

> 🎙️ Good answer: integrate with ConnectIPS (joint platform) to share cost & grow the market, partner with
> a courier for reach — but still compete on app UX and cashback. Reward FORM + REASON + what stays
> competitive (the S19 hook).

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`
**MCQ 1.** Nepali banks jointly building and funding ConnectIPS is cooperation via:
a) a price war  b) ✅ **a joint platform (shared rails)**  c) an acquisition  d) advertising
*(Why: rivals share common payment infrastructure none would build alone.)*

**MCQ 2.** "Grow the pie first, then compete for slices" means:
a) never compete  b) ✅ **enlarge the whole market together before fighting for share**  c) merge  d) cut prices
*(Why: cooperation expands total demand first; firms compete for the bigger market after.)*

**Discussion prompt:** *Name a Nepali cooperation and its form (joint platform / partnership / integration).*

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** in a small market like Nepal, cooperation is often the only route to scale —
which is why rivals share rails like ConnectIPS while still fighting for customers. That exact combination
is the subject of the next session.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Cooperation** = creating value together; digital encourages it via **modularity, APIs, network effects, convenience.**
2. Five reasons: grow the market, share cost/risk, access capabilities, set standards, speed & reach (**"grow the pie first"**).
3. Three forms: **joint platforms, partnerships, service integration.**

**Next session (S19):** the paradox resolved — **co-opetition.**

---
---

# S19 — Co-opetition: Cooperate + Compete at Once
**Lecture hour 4 of 10 (Unit 3) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] **"eSewa and Nabil need each other — and fight over the same money"**

> **Deliver (≈2 min):** "eSewa and Nabil Bank need each other — the wallet needs the bank's accounts, the
> bank wants the wallet's reach — yet both chase the same customer's money. They cooperate and compete at
> the same time, with the same firm."
>
> **Run (≈3 min):** Agenda: co-opetition = cooperate upstream + compete downstream (+ the Value-Net) → why
> it's so common → benefits & risks.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Co-opetition = Cooperate Upstream, Compete Downstream `[THEORY]` `[~8 min]`
[SLIDE] **Cooperate on the pipes; compete for the customer**

> **Deliver:** **Co-opetition is cooperating and competing with the same firm at the same time.** The
> pattern is **UPSTREAM cooperation** (shared technology, infrastructure, and standards — the "pipes") and
> **DOWNSTREAM competition** (for customers, brand, and price — the "product"). **Brandenburger &
> Nalebuff's Value-Net** names the players around a firm: customers, suppliers, competitors, and
> **complementors** — and shows a rival can be a complementor upstream while a competitor downstream.

- 🇳🇵 **Local example:** **eSewa and Nabil Bank co-opete** — upstream they cooperate (eSewa needs Nabil's
  rails and accounts; both use ConnectIPS) while downstream they compete for the same customer's wallet
  share. Globally, **Samsung** sells **Apple** the screens and chips for iPhones (upstream) while battling
  Apple in phone sales (downstream). Cooperate on the pipes, compete for the customer.

> ❌ **Misconception:** *"You either compete with a firm or cooperate — not both."*
> ✅ **Correction:** "Co-opetition is doing both at once with the SAME firm: cooperate upstream on shared
> tech/rails/standards, compete downstream for customers and brand. The Value-Net shows a rival can be a
> complementor (grows the pie) and a competitor (splits it) simultaneously."

> 🖼️ Visual: `s19_coopetition.png` — an upstream "cooperate" band and a downstream "compete" band around two firms.

> 🎯 **Exam-ready answer:** "Co-opetition is cooperating and competing with the same firm at once: cooperate
> UPSTREAM on shared technology, infrastructure, and standards (the pipes), and compete DOWNSTREAM for
> customers, brand, and price (the product). The Value-Net names customers, suppliers, competitors, and
> complementors — a rival can be a complementor upstream and a competitor downstream (eSewa & Nabil;
> Samsung & Apple)."

**📊 Depth table — Cooperate upstream vs compete downstream**

| Case | Cooperate UPSTREAM (shared) | Compete DOWNSTREAM (for customers) |
|---|---|---|
| eSewa & Khalti | Same ConnectIPS/QR rails | App UX, cashback, merchant deals |
| Daraz & Pathao | Share delivery logistics | Pathao's own Foodmandu-style services |
| Banks & ConnectIPS | Shared clearing/settlement | Interest rates, branches, own apps |
| Apple & Samsung | Samsung supplies Apple chips/screens | Compete fiercely in phone sales |
| Airlines (codeshare) | Share routes & booking systems | Compete on price & loyalty |
| Google & Apple | Google pays to be default on iPhone | Android vs iOS ecosystems compete |

*ℹ️ The consistent split: cooperate on the expensive shared 'pipes' (rails, chips, routes) that grow the whole market, then compete on the 'product' the customer actually chooses. That is co-opetition in one line.*

#### Concept 2 — Why Co-opetition Is So Common Online `[THEORY]` `[~6 min]`
[SLIDE] **Layered, modular products — no one owns the whole stack; ecosystems win**

> **Deliver:** Co-opetition is common because products are **LAYERED and MODULAR:** no single firm owns the
> whole stack (device, OS, network, payment, app), so firms must interconnect at some layers even while
> competing at others. **Ecosystems, not lone products, win** — a firm that cooperates to enrich a shared
> platform captures more value than one that walls itself off. Network effects reward shared standards, and
> specialisation means everyone depends on partners' pieces.

- 🇳🇵 **Local example:** A Nepali wallet cannot function alone — it needs banks (accounts), telecoms
  (data/SMS), device makers (phones), and merchants, none of which it owns. So it cooperates across the
  stack while competing for daily use. Globally, Apple's **App Store** thrives because it lets even rival
  developers build on it — the ecosystem enriched by complementors beats a walled-off product.

> ❌ **Misconception:** *"Firms should own their whole stack to avoid depending on rivals."*
> ✅ **Correction:** "In layered digital markets no one can own device + OS + network + payment + app, and a
> rich ecosystem beats an isolated product. Interconnection is unavoidable, so cooperating at some layers
> while competing at others is the rational default."

> 🎯 **Exam-ready answer:** "Co-opetition is common because digital products are layered and modular — no
> firm owns the whole stack, so interconnection is unavoidable. Ecosystems beat isolated products;
> cooperating to enrich a shared platform (with complementors, even rivals) captures more value. Network
> effects reward shared standards, and specialisation makes every firm depend on partners' pieces."

**📊 Depth table — Why co-opetition happens — the forces**

| Force | Why it drives co-opetition | Example |
|---|---|---|
| Layered products | No one owns the whole stack | Wallet needs bank + network + device |
| Ecosystem advantage | Rich shared platform beats isolation | App stores enrich iOS/Android |
| Standards & network effects | Shared interface grows all value | QR standard adopted by all wallets |
| Specialisation | Each firm best at one layer | Daraz retails; Pathao delivers |

*ℹ️ Because digital products are stacks of layers owned by different firms, interconnection is unavoidable — so rivals cooperate at some layers while competing at others. Co-opetition is the natural shape of a layered market (S20).*

#### Concept 3 — Benefits & Risks of Co-opetition `[THEORY]` `[~7 min]`
[SLIDE] **Bigger market, shared cost, speed, scale — vs dependency, power imbalance, lock-in, leakage**

> **Deliver:** Co-opetition's **benefits:** it grows the whole market, shares cost and risk, speeds
> innovation, and lets small firms reach scale via shared rails. Its **risks:** **DEPENDENCY** (you rely on
> a rival's infrastructure), **POWER IMBALANCE** (the bigger partner sets terms), **LOCK-IN** (hard to leave
> a shared standard), and knowledge/data **LEAKAGE.** The skill is deciding which layers to share (the
> pipes) and which to guard (data, the customer relationship).

- 🇳🇵 **Local example:** A small Nepali wallet gains huge benefit from shared **ConnectIPS/QR** rails —
  instant national reach it could never build alone. But the risk is **dependency and power imbalance:** it
  relies on banks that also run their own apps and could change terms or fees. Its skill is cooperating on
  the shared rails while guarding its own customer data and app experience.

> ❌ **Misconception:** *"Co-opetition is win-win with no downside."*
> ✅ **Correction:** "Cooperating with a rival creates dependency, power imbalance, lock-in, and data
> leakage — the partner can squeeze or out-learn you. The benefits are real, but so are the risks; the skill
> is choosing which layers to share and which to protect."

> 🎯 **Exam-ready answer:** "Co-opetition's benefits: grow the whole market, share cost and risk, speed
> innovation, give small firms scale via shared rails. Its risks: dependency on a rival's infrastructure,
> power imbalance, lock-in to a shared standard, and data/knowledge leakage. The skill is deciding which
> layers to cooperate on (the pipes) and which to guard (data, the customer relationship)."

**📊 Depth table — Co-opetition — benefits vs risks**

| Dimension | Benefit | Risk |
|---|---|---|
| Market size | Grows the whole pie | Rival grows too — you may lose share |
| Cost & risk | Shared, so affordable | Dependency on a rival's infrastructure |
| Innovation | Faster via shared standards | Lock-in to a standard you can't leave |
| Bargaining | Small firm gains scale | Power imbalance — big partner sets terms |
| Information | Learn from the partner | Data/knowledge leaks to the rival |

*ℹ️ Every benefit has a shadow risk. The strategic question is WHICH layers to share (the expensive pipes) and WHICH to guard (your data and the customer relationship — the control points of S25).*

#### 🛠 ACTIVITY — "Split the layers" `[ACTIVITY]` `[~5 min]`
> **Run it:** In pairs (3 min) pick two Nepali rivals; list upstream cooperation vs downstream competition;
> name one benefit and one risk for the smaller firm. Take 3–4 answers (2 min).

> 🎙️ eSewa & Khalti: cooperate on ConnectIPS/QR (upstream), compete on UX & cashback (downstream); benefit
> = national reach cheaply, risk = dependency on bank rails. Reward the explicit split + one benefit/risk.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`
**MCQ 1.** Co-opetition typically means firms:
a) compete on everything  b) cooperate on everything  c) merge  d) ✅ **cooperate upstream (tech/rails) and compete downstream (customers)**
*(Why: shared infrastructure/standards upstream; competition for customers and brand downstream.)*

**MCQ 2.** A key RISK of co-opetition for a small firm is:
a) lower costs  b) ✅ **dependency & power imbalance vs the larger partner**  c) more customers  d) faster innovation
*(Why: relying on a rival's rails creates dependency; the bigger partner can set terms.)*

**Discussion prompt:** *Name a Nepali co-opetition and split its upstream cooperation vs downstream competition.*

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** co-opetition is how Nepal's small digital firms survive giants — sharing rails to
reach scale while guarding the customer. Deciding which layers to share and which to protect is a strategic
choice we formalise as "control points" in S25.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Co-opetition** = cooperate + compete with the same firm: cooperate UPSTREAM (tech/rails/standards), compete DOWNSTREAM (customers/brand). Value-Net adds complementors.
2. Common online because products are **layered/modular** — no one owns the whole stack; ecosystems beat isolated products.
3. Benefits (bigger market, shared cost, speed, scale) come with risks (**dependency, power imbalance, lock-in, data leakage**).

**Next session (S20):** why "upstream/downstream" exist at all — the **layered internet model.**

---
---

# S20 — The Layered Internet Model
**Lecture hour 5 of 10 (Unit 3) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] **"You see the top; the power sits at the bottom"**

> **Deliver (≈2 min):** "When you watch a video on Foodmandu's app, you touch an APPLICATION — but under it
> sits a PLATFORM (Android, cloud), and under that the INFRASTRUCTURE (Ncell's network, data centres,
> fibre). You see the top; the power often sits at the bottom."
>
> **Run (≈3 min):** Agenda: the 3 layers (+ user) → value flows bottom-up → power: control lower = power
> over higher.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — The Three Layers (+ the User) `[THEORY]` `[~7 min]`
[SLIDE] **Infrastructure → Platform → Application → User**

> **Deliver:** The layered internet model (a **business/economic** view, *not* the technical OSI/TCP-IP
> stack) has three layers plus the user. **INFRASTRUCTURE** — the technical base: fibre, data centres,
> connectivity, devices, cloud (NTC/Ncell, AWS). **PLATFORM** — the capability layer: operating systems,
> payment rails, cloud services, app stores (Android/iOS, eSewa/Fonepay, AWS). **APPLICATION** — the
> experience layer: the apps people use (Daraz, Foodmandu, Netflix). The **USER** sits on top.

- 🇳🇵 **Local example:** Trace a **Foodmandu** order — you use the APPLICATION (the app), which runs on a
  PLATFORM (Android/iOS, cloud, a payment rail like Khalti/Fonepay), which sits on INFRASTRUCTURE
  (Ncell/NTC data, servers, fibre). You, the USER, see only the top. Netflix is identical.

> ❌ **Misconception:** *"The internet is one flat thing."* / *"This is the OSI model."*
> ✅ **Correction:** "It is a STACK — infrastructure (base), platform (capability), application (experience),
> user on top. And this is the ECONOMIC layered model, not the technical 7-layer OSI/TCP-IP stack students
> often confuse it with; the business layers are about who owns value and power, not protocols."

> 🖼️ Visual: `s20_layers.png` — the stacked layers with value-up and power-down arrows.

> 🎯 **Exam-ready answer:** "The layered internet model (business view, distinct from OSI) has three layers
> plus the user: infrastructure (technical base — fibre, data centres, cloud), platform (capability — OS,
> payment rails, cloud services, app stores), and application (experience — the apps people use). The user
> consumes the experience; every digital service can be read down through all three."

**📊 Depth table — The 3 layers — role, global vs Nepal example**

| Layer | Role | Global example | Nepal example |
|---|---|---|---|
| Infrastructure | Technical base: network, data centre, device | AWS, Google fibre, cables | NTC/Ncell, data centres, ISPs |
| Platform | Capability: OS, payment rails, cloud, app store | Android/iOS, AWS, Visa | eSewa/Fonepay, ConnectIPS, Android |
| Application | Experience: the app users open | Netflix, Uber, Amazon app | Daraz, Foodmandu, Pathao app |
| User | Consumes the experience | People, firms, government | Nepali consumers & businesses |

*ℹ️ Read any digital service top-to-bottom and you'll find all three layers. Note Nepal mostly owns the APPLICATION layer while depending on foreign PLATFORM and INFRASTRUCTURE (Android, AWS) — the structural-dependence point of Concept 3.*

#### Concept 2 — Value Flows Bottom-Up `[THEORY]` `[~7 min]`
[SLIDE] **Technical → capability → experience**

> **Deliver:** Value is built from the bottom up: each layer adds value to the one below. Infrastructure
> provides raw **TECHNICAL** capability (bandwidth, compute, connectivity). The platform turns that into
> usable **CAPABILITY** (an OS, a payment rail, cloud services others build on). The application turns
> capability into **EXPERIENCE** (a service the user enjoys). Raw fibre → cloud compute → a streaming app →
> a movie night.

- 🇳🇵 **Local example:** Your **bank's app** (application) gives you the EXPERIENCE of transferring money in
  seconds. That rests on ConnectIPS and core-banking CAPABILITY (platform), which rests on data centres and
  the bank network's TECHNICAL capacity (infrastructure). Netflix is identical: AWS fibre → AWS/Android
  services → the Netflix app.

> ❌ **Misconception:** *"The app creates all the value."*
> ✅ **Correction:** "The app only delivers the EXPERIENCE; the value beneath — capability from the platform,
> technical capacity from infrastructure — makes the experience possible. Value flows bottom-up; the visible
> top sits on invisible value from below."

> 🎯 **Exam-ready answer:** "Value flows bottom-up: infrastructure gives technical value, the platform turns
> it into capability value (usable services others build on), the application turns capability into
> experience value. Raw fibre becomes cloud compute becomes a streaming app becomes a movie night —
> technical to capability to experience."

**📊 Depth table — Value type by layer — a worked trace**

| Layer | Value type | Banking example | Netflix example |
|---|---|---|---|
| Infrastructure | Technical (compute, network) | Data centre, bank network | AWS servers, global fibre |
| Platform | Capability (usable service) | ConnectIPS rails, core banking | AWS services, Android/iOS |
| Application | Experience (what user enjoys) | Your bank's mobile app | Netflix app & recommendations |
| User | Consumption | You transfer money in seconds | You watch a film instantly |

*ℹ️ Trace any service down and value climbs back up: technical capacity becomes a usable platform becomes an experience. The user sees only the experience but relies on every layer beneath.*

#### Concept 3 — Layer Power: Control Lower = Power Over Higher `[THEORY]` `[~7 min]`
[SLIDE] **Value flows up, but power flows down**

> **Deliver:** While value flows UP, **power flows DOWN:** whoever controls a lower layer holds power over
> everything above it. An app depends on the platform (app-store rules, payment cut); the platform depends
> on infrastructure. **Apple's App Store** can take ~30% from any app; a cloud provider can raise prices on
> everyone hosted on it. This is why Nepal's **structural dependence** matters: Nepali firms own the
> APPLICATION layer but rent the PLATFORM and INFRASTRUCTURE (Android, AWS) — so foreign firms hold power
> over local apps.

- 🇳🇵 **Local example:** A Nepali app maker owns the APPLICATION but rents everything below — ships through
  Apple/Google's app stores (which take a cut/set rules), hosts on AWS/foreign cloud (which sets prices),
  runs on Android/iOS. Power over a local app sits with foreign platform and infrastructure owners; the
  App Store's ~30% cut is felt by any Nepali developer.

> ❌ **Misconception:** *"The app on top is the most powerful part."*
> ✅ **Correction:** "Value flows up but POWER flows down: the platform and infrastructure beneath set the
> terms (app-store cut, cloud pricing, OS rules). The visible top layer is often the least powerful — which
> is why Nepal owning apps but renting the layers beneath leaves real power abroad."

> 🎯 **Exam-ready answer:** "Value flows up, but power flows down: whoever controls a lower layer holds power
> over everything above it (an app depends on the platform's app-store rules and ~30% cut; the platform
> depends on infrastructure/cloud pricing). Owning the platform or infrastructure is the deepest moat. Nepal
> owns the application layer but rents platform and infrastructure, so foreign firms hold power over Nepali
> apps."

**📊 Depth table — Benefits of layered architecture (and the power it hides)**

| Benefit | What it enables | But note the power |
|---|---|---|
| Specialisation | Each firm masters one layer | Layer owners set terms for others |
| Modularity / reuse | Build apps fast on shared platforms | App depends on platform's rules |
| Innovation at the top | Anyone can launch an app | Platform can copy or tax the app |
| Scalability | Cloud scales apps instantly | Cloud provider controls pricing |
| Lower entry cost | No need to build infra | Deep dependence on infra/platform owner |

*ℹ️ Layering is hugely beneficial — it lets a Nepali startup launch an app without building fibre or a cloud. But every benefit comes with dependence: whoever owns the layer you build on holds power over you (the App Store's 30%).*

#### 🛠 ACTIVITY — "Trace the stack" `[ACTIVITY]` `[~5 min]`
> **Run it:** In pairs (3 min) pick a Nepali service; name what sits at each layer; identify which layers
> are Nepali vs foreign and where power sits. Take 3–4 answers (2 min).

> 🎙️ Daraz: app = Daraz; platform = Android/iOS + cloud + Fonepay rails; infrastructure = NTC/Ncell +
> foreign cloud + devices. Nepal owns the app; platform/infra largely foreign → power sits abroad.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`
**MCQ 1.** Cloud, data centres, connectivity and devices belong to which layer?
a) application  b) ✅ **infrastructure**  c) user  d) payment
*(Why: infrastructure is the technical base — networks, data centres, devices, cloud.)*

**MCQ 2.** "Control of a lower layer gives power over higher layers" is shown by:
a) users choosing apps  b) ✅ **an app store taking a ~30% cut from every app**  c) fast internet  d) free apps
*(Why: the platform beneath the app sets terms the app must accept — power flows down.)*

**Discussion prompt:** *For a Nepali service, which layers are local and which foreign — where's the power?*

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** the layered model explains WHY co-opetition happens (S19) and where real power
lives — and it sets up S25's control points. For Nepal it's a strategic warning: owning apps while renting
the layers beneath leaves power (and profit) abroad.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. Three layers (+ user): **infrastructure** (technical base), **platform** (capability), **application** (experience) — the business, not OSI, view.
2. **Value flows bottom-up:** technical → capability → experience; each layer adds to the one below.
3. **Power flows top-down:** control a lower layer and you hold power over higher ones — Nepal owns apps but rents platform & infrastructure.

**Next session (S21):** what drives NEW value — **digital innovation**, and innovation vs invention.

---
---

# S21 — Digital Innovation
**Lecture hour 6 of 10 (Unit 3) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] **"eSewa invented nothing — yet changed how millions pay"**

> **Deliver (≈2 min):** "eSewa didn't invent the internet, smartphones, or QR codes — yet it changed how
> millions of Nepalis pay. Meanwhile brilliant inventions sit unused in labs. What's the difference between
> INVENTING and INNOVATING — and why do cheap, 'good-enough' newcomers topple better-funded incumbents?"
>
> **Run (≈3 min):** Agenda: definition + innovation ≠ invention + sustaining vs disruptive → the 6 types →
> enablers, process & Nepal challenges.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Innovation ≠ Invention; Sustaining vs Disruptive `[THEORY]` `[~8 min]`
[SLIDE] **Value, not just new tech — and low-end disruption that rises to overtake**

> **Deliver:** **Digital innovation is creating new value — in products, processes, services, or business
> models — using digital technology.** Crucially, **INNOVATION ≠ INVENTION:** invention creates a new
> technology; innovation turns an idea into **VALUE people actually use.** It also comes in two strategic
> kinds: **SUSTAINING** (improving an existing product for existing customers — a better camera each year)
> and **DISRUPTIVE** (a cheaper, simpler, 'good-enough' offering that enters at the low end and rises to
> overtake incumbents — Christensen).

- 🇳🇵 **Local example:** **eSewa** invented nothing technically — QR, internet, phones existed — but it
  INNOVATED by turning them into a payment service millions use. It was also **DISRUPTIVE:** a simpler,
  cheaper alternative to bank queues that began with small top-ups and bills, then climbed to serious
  payments. Banks did sustaining innovation (better branch apps) and were caught off guard.

> ❌ **Misconception:** *"Innovation means inventing brand-new technology."*
> ✅ **Correction:** "Innovation is creating VALUE people use, often reusing existing tech in a new context
> or business model — eSewa invented nothing but changed everything. The dangerous kind is disruptive: a
> cheap, 'good-enough' entrant that looks unthreatening until it climbs and overtakes."

> 🖼️ Visual: `s21_innovation.png` — the sustaining vs disruptive trajectory curve.

> 🎯 **Exam-ready answer:** "Digital innovation is creating new value with digital tech. Innovation ≠
> invention: invention creates a technology, innovation turns an idea into value people use. It is either
> sustaining (improving for existing customers) or disruptive (a cheaper, 'good-enough' entrant that starts
> low and rises to overtake incumbents — Christensen). eSewa is both an innovation and a disruptor."

**📊 Depth table — Sustaining vs disruptive innovation**

| Dimension | Sustaining innovation | Disruptive innovation |
|---|---|---|
| Aim | Improve for existing customers | Serve overlooked / new customers |
| Starting point | Better than current product | Simpler, cheaper, 'good enough' |
| Who does it | Usually incumbents | Usually new entrants |
| Price | Same or higher | Lower / more accessible |
| Trajectory | Steady improvement | Enters low, then climbs to overtake |
| Example | Yearly phone camera upgrade | eSewa vs bank queues; Netflix vs cable |

*ℹ️ Incumbents win at sustaining innovation but are blindsided by disruption because the newcomer looks too cheap/basic to matter — until it climbs. This is why 'good enough & cheap' beats 'better & pricey' in digital markets.*

#### Concept 2 — The Six Types of Digital Innovation `[THEORY]` `[~7 min]`
[SLIDE] **Product · process · business-model · service · marketing · organizational**

> **Deliver:** Digital innovation shows up in six types. **PRODUCT** (a new/improved offering). **PROCESS**
> (a better way of working — automated warehousing). **BUSINESS-MODEL** (a new way to create/capture value —
> subscription instead of sale). **SERVICE** (a new service experience — streaming, online support).
> **MARKETING** (new ways to reach customers — social, influencer). **ORGANIZATIONAL** (new internal
> structure/culture — agile, remote). The most powerful digital shifts are usually business-model
> innovations, not just product ones.

- 🇳🇵 **Local example:** **Daraz** shows several types — automated warehousing (process), app features
  (product), a marketplace-commission model (business-model), returns/buyer protection (service), festival
  cashback (marketing), agile teams (organizational). The biggest lever was the marketplace **business
  model**, not any single feature. Netflix likewise won on its subscription business model.

> ❌ **Misconception:** *"Innovation just means new products/features."*
> ✅ **Correction:** "Product is only one of six types — process, business-model, service, marketing, and
> organizational matter too, and business-model innovation often reshapes whole industries (subscription,
> platform)."

> 🎯 **Exam-ready answer:** "Digital innovation appears in six types: product, process, business-model,
> service, marketing, and organizational. Firms often innovate on several at once, but the most powerful
> shifts are usually business-model innovations (subscription, platform, freemium) rather than single
> product features."

**📊 Depth table — The 6 types of digital innovation — Nepal & global**

| Type | What changes | Example |
|---|---|---|
| Product | A new/improved offering | Smart devices; a new app feature |
| Process | A better way of working | Daraz automated warehousing; e-invoicing |
| Business-model | New way to create/capture value | Netflix subscription; eSewa wallet model |
| Service | A new service experience | Online banking; streaming; e-tickets |
| Marketing | New ways to reach customers | TikTok/influencer marketing; app cashback |
| Organizational | New internal structure/culture | Agile teams; remote work; digital HR |

*ℹ️ A single company often innovates on several types at once. The type that reshapes an industry is usually business-model innovation (S22) — changing HOW value is earned, not just WHAT is sold.*

#### Concept 3 — Enablers, the Process & Nepal's Challenges `[THEORY]` `[~7 min]`
[SLIDE] **AI/IoT/cloud/big data/AR/VR · ideation→MVP→scale · Nepal challenges**

> **Deliver:** Six technologies enable most digital innovation: **AI, IoT, cloud, big data, AR, VR.** The
> innovation **PROCESS** runs **ideation → MVP → scale.** But innovation faces challenges — especially in
> Nepal: limited funding/VC, small market size, talent and skills gaps (brain-drain), weak digital
> infrastructure outside cities, regulatory uncertainty, and low digital/financial literacy. **Innovation is
> about CONTEXT, not just technology.**

- 🇳🇵 **Local example:** A Nepali **agri-tech** startup might use cloud + big data + mobile (enablers) to
  connect farmers to buyers — ideation (farmers get poor prices) → MVP (a simple SMS/app price service in
  one district) → scale. But it hits Nepal's challenges: thin funding, low rural connectivity, digital
  literacy. Winners fit the CONTEXT — a lightweight, SMS-friendly, cash-aware design beats a data-heavy app
  copied from abroad.

> ❌ **Misconception:** *"With the right technology, any innovation will succeed."*
> ✅ **Correction:** "Technology is only the enabler; success depends on CONTEXT — funding, market size,
> talent, infrastructure, regulation, literacy. In Nepal a 'lower-tech' solution that fits local realities
> often beats a sophisticated one copied from Silicon Valley."

> 🎯 **Exam-ready answer:** "Enablers: AI, IoT, cloud, big data, AR, VR. Process: ideation → MVP → scale.
> Challenges (sharpened in Nepal): funding, small market, talent/brain-drain, weak rural infrastructure,
> regulatory uncertainty, low literacy. Innovation is about context, not just technology — Nepal's fintech
> and agri-tech win by fitting local realities."

**📊 Depth table — Innovation challenges — general vs Nepal-specific**

| Challenge | General | Nepal-specific angle |
|---|---|---|
| Funding | Scaling needs capital | Thin VC/angel ecosystem; hard to raise |
| Market size | Need enough users | Small population; low per-capita spend |
| Talent | Skilled builders scarce | Brain-drain of engineers abroad |
| Infrastructure | Reliable connectivity/power | Weak rural internet & power outages |
| Regulation | Rules lag innovation | Unclear fintech/data rules; slow approvals |
| Literacy | Users must adopt | Low digital/financial literacy outside cities |

*ℹ️ Nepal's fintech (eSewa/Khalti) and agri-tech successes worked by fitting the LOCAL context — solving a real Nepali problem cheaply — rather than importing a Silicon Valley model. Innovation is context, not just technology.*

#### 🛠 ACTIVITY — "Pitch a Nepali innovation" `[ACTIVITY]` `[~5 min]`
> **Run it:** In pairs (3 min) propose one digital innovation for a real Nepali problem; name its TYPE,
> ENABLER tech, and whether it's sustaining or disruptive; name the biggest local CHALLENGE. Take 3–4
> answers (2 min).

> 🎙️ Good pitch: SMS crop-price service = service + business-model innovation, enabler = cloud/big data,
> disruptive, biggest challenge = rural literacy/connectivity. Reward context-fit over tech sophistication.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`
**MCQ 1.** "Innovation is not invention" means innovation is about:
a) ✅ **creating value people use from an idea, not just inventing the tech**  b) patents only  c) pure lab research  d) copying rivals
*(Why: invention creates a technology; innovation turns it into value people actually use.)*

**MCQ 2.** A cheaper, 'good-enough' newcomer that enters low and rises to overtake incumbents is:
a) sustaining innovation  b) ✅ **disruptive innovation**  c) invention  d) marketing innovation
*(Why: disruptive innovation enters at the low end and climbs to displace better, pricier incumbents.)*

**Discussion prompt:** *Name a Nepali innovation — its type, and whether it is sustaining or disruptive.*

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** innovation is how a Nepali startup can beat a giant without out-spending it — by
fitting the local context and disrupting from below. The most powerful kind, business-model innovation, is
exactly the next session.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. Digital innovation = creating value with digital tech; **innovation ≠ invention.** Sustaining improves; disruptive enters cheap & rises.
2. **Six types:** product, process, business-model, service, marketing, organizational — business-model matters most.
3. Enablers **AI/IoT/cloud/big data/AR/VR**; process **ideation → MVP → scale**; Nepal challenges make **CONTEXT** decisive.

**Next session (S22):** the innovation that reshapes markets — **digital business models** and the value triad.

---
---

# S22 — Digital Business Models
**Lecture hour 7 of 10 (Unit 3) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] **"Same internet, wildly different ways to make money"**

> **Deliver (≈2 min):** "Netflix charges a flat monthly fee; Google is free but sells ads; Daraz takes a cut
> of each sale; Spotify gives you free-with-ads or paid. Same internet, wildly different ways to make money.
> A business model answers one question: how do you CREATE, DELIVER, and CAPTURE value?"
>
> **Run (≈3 min):** Agenda: the value triad → the 10 model types (part 1) → the 10 model types (part 2) +
> hybrids.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — The Value Triad: Create, Deliver, Capture `[THEORY]` `[~7 min]`
[SLIDE] **Create (proposition) + deliver (channels) + capture (revenue)**

> **Deliver:** A business model describes how a firm **creates, delivers, and captures** value. **CREATE:**
> what problem you solve and for whom (the value proposition). **DELIVER:** how you get it to customers
> (channels, platform, logistics). **CAPTURE:** how you make money (the revenue mechanism — subscription,
> commission, ads). Digital firms often find create and deliver easy but must think hard about **capture** —
> which is why 'free' products (Unit 2) still need a money side.

- 🇳🇵 **Local example:** **Foodmandu** CREATES value by getting restaurant meals to busy customers, DELIVERS
  via its app + rider network with live tracking, and CAPTURES through a commission per order plus a delivery
  fee. Netflix creates with content, delivers via streaming, captures via a flat subscription.

> ❌ **Misconception:** *"A business model is just how a company makes money."*
> ✅ **Correction:** "Making money is only the CAPTURE part. A full model also covers how value is CREATED
> (the proposition) and DELIVERED (channels/platform). Two firms can create/deliver the same value yet
> capture it differently — capture is where models diverge."

> 🎯 **Exam-ready answer:** "A business model describes how a firm creates value (the proposition), delivers
> it (channels, platform, logistics), and captures it (the revenue mechanism — subscription, commission,
> ads). Digital firms often find create and deliver easy but must design capture carefully — which is why
> even 'free' products need a money side (Unit 2)."

**📊 Depth table — The value triad — with a Nepal example**

| Element | The question | Foodmandu example |
|---|---|---|
| Create value | What problem, for whom? | Get restaurant food to busy customers |
| Deliver value | How does it reach the user? | App + rider network + live tracking |
| Capture value | How is money made? | Commission per order + delivery fee |

*ℹ️ Every business model answers these three. Most digital firms find create and deliver relatively easy (software scales); the hard, distinctive choice is CAPTURE — which revenue mechanism, and from which side (Unit 2).*

#### Concept 2 — The 10 Business Models — Part 1 `[THEORY]` `[~7 min]`
[SLIDE] **Platform · subscription · freemium · sharing/access · marketplace**

> **Deliver:** Digital firms mostly use ten model types; part 1 covers five. (1) **PLATFORM** — connect
> groups and take a cut (Daraz, Pathao). (2) **SUBSCRIPTION** — recurring fee for ongoing access (Netflix,
> Spotify Premium). (3) **FREEMIUM** — free base tier, pay to upgrade (Spotify, Zoom). (4) **SHARING/ACCESS**
> — pay to use, not own, an asset (Airbnb, ride sharing). (5) **MARKETPLACE** — match many buyers and
> sellers for commission (Hamrobazar, eBay).

- 🇳🇵 **Local example:** Daraz runs a PLATFORM/MARKETPLACE model (commission), a gym app might use
  SUBSCRIPTION, a learning app uses FREEMIUM (free lessons, pay to unlock), and InDrive uses a SHARING model
  (pay to use a ride, not own the car). Each solves value capture differently.

> ❌ **Misconception:** *"Every online business just sells things (e-commerce)."*
> ✅ **Correction:** "E-commerce is only one of ten models. Platform, subscription, freemium, sharing, and
> marketplace capture value differently — via commission, recurring fees, upsell, or access — and most
> successful firms combine several."

> 🎯 **Exam-ready answer:** "Part 1 of the ten models: platform (connect groups, take a cut — Daraz),
> subscription (recurring fee — Netflix), freemium (free base, pay to upgrade — Spotify), sharing/access
> (pay to use, not own — Airbnb), and marketplace (commission on matched trades — Hamrobazar). Each captures
> value through a different mechanism."

*(The full 10-model table is shown once, under Concept 3 below.)*

#### Concept 3 — The 10 Business Models — Part 2 + Hybrids `[THEORY]` `[~7 min]`
[SLIDE] **Advertising · e-commerce · ecosystem · usage/on-demand · experience (+ hybrids)**

> **Deliver:** Part 2 covers the other five, plus hybrids. (6) **ADVERTISING** — give a service free, sell
> user attention (Google, Meta, TikTok). (7) **E-COMMERCE** — sell goods online for a margin (Sastodeal,
> brand stores). (8) **ECOSYSTEM** — bundle many services so users stay (Apple, Google). (9)
> **USAGE/ON-DEMAND** — pay per use or API call (AWS pay-as-you-go). (10) **EXPERIENCE** — charge for a
> premium experience (Netflix originals). Most real firms are **HYBRIDS**, and **DATA-MONETIZATION** (selling
> insights/targeting) underlies the advertising models.

- 🇳🇵 **Local example:** **Google** gives search free and captures value via ADVERTISING (Unit 2's money
  side), while also running an ECOSYSTEM (Android, Maps, Gmail) and USAGE-based cloud — a hybrid. In Nepal,
  **Daraz** is a hybrid too: MARKETPLACE (commission) + ADVERTISING (sellers pay for placement) +
  E-COMMERCE (its own stock).

> ❌ **Misconception:** *"Each company has exactly one business model."*
> ✅ **Correction:** "Most successful digital firms are HYBRIDS — marketplace + advertising + e-commerce, or
> advertising + ecosystem + cloud. Advertising models are really data-monetization (Unit 2's subsidy side).
> Describe a firm by its MIX, not one label."

> 🎯 **Exam-ready answer:** "Part 2: advertising (free service, sell attention — Google), e-commerce (margin
> on goods — Sastodeal), ecosystem (bundle to lock in — Apple), usage/on-demand (pay per use/API — AWS), and
> experience (premium experience — Netflix originals). Most real firms are hybrids (Daraz = marketplace + ads
> + e-commerce), and data-monetization underlies the advertising models — the subsidy-side logic of Unit 2."

**📊 Depth table — The 10 digital business models — revenue mechanism & example**

| Model | How it captures value | Example (Nepal / global) |
|---|---|---|
| Platform | Commission/fee on interactions | Pathao, Daraz / Uber, Airbnb |
| Subscription | Recurring fee for access | Netflix, Spotify Premium, SaaS |
| Freemium | Free base, pay to upgrade | Spotify free/paid, Zoom, LinkedIn |
| Sharing / access | Pay to use, not own | Airbnb, InDrive, asset sharing |
| Marketplace | Commission on matched trades | Hamrobazar, eBay, Etsy |
| Advertising | Sell user attention to advertisers | Google, Meta, YouTube, TikTok |
| E-commerce | Margin on goods sold online | Sastodeal, Amazon retail, brand stores |
| Ecosystem | Lock-in across bundled services | Apple, Google, Amazon ecosystems |
| Usage / on-demand | Pay per use / API call | AWS pay-as-you-go, cloud, SMS API |
| Experience | Charge for a premium experience | Netflix originals, events, premium UX |

*ℹ️ Read the middle column: models differ mainly in HOW they capture value. Most real firms are HYBRIDS — Daraz combines marketplace + advertising + e-commerce; Google combines advertising + ecosystem + usage (cloud). Data-monetization underlies the ad models.*

**📊 Depth table — How digital lowers entry barriers (why so many models exist)**

| Barrier lowered | How digital lowers it | Effect |
|---|---|---|
| Physical assets | Cloud rents compute; no factory needed | Start with little capital |
| Distribution | App stores & internet reach all | Global reach from day one |
| Inventory | Marketplace lists others' stock | Sell without owning goods |
| Marketing | Social/targeted ads are cheap | Reach niche customers cheaply |
| Payments | Wallets/gateways plug in | Collect money instantly |

*ℹ️ Because digital slashes the cost of assets, distribution, inventory, marketing, and payments, almost anyone can launch a business model — which is why so many models coexist and why competition is easy to START but hard to WIN (S17).*

#### 🛠 ACTIVITY — "Name the model(s)" `[ACTIVITY]` `[~5 min]`
> **Run it:** In pairs (3 min) pick 3 firms; name each firm's model(s) and capture mechanism; spot at least
> one HYBRID. Take 3–4 answers (2 min).

> 🎙️ Netflix = subscription + experience; Daraz = marketplace + advertising + e-commerce (hybrid);
> Spotify = freemium + subscription + advertising. Reward the capture mechanism + a hybrid.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`
**MCQ 1.** Netflix charging a flat monthly fee for access is which model?
a) freemium  b) marketplace  c) ✅ **subscription**  d) advertising
*(Why: a recurring fee for ongoing access is the subscription model.)*

**MCQ 2.** Google giving search free and earning from ads is capturing value via:
a) subscription  b) ✅ **advertising (selling user attention)**  c) e-commerce  d) usage fees
*(Why: the advertising model gives the service free and monetises attention/data — Unit 2's money side.)*

**Discussion prompt:** *Name a Nepali hybrid firm and the two-plus models it combines.*

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** knowing the models lets you read any digital firm's money logic and design your
own — the single most powerful innovation lever (S21). But a business model (how you EARN) is not the same
as how value is GENERATED — the next session's distinction.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. A business model = how you **CREATE + DELIVER + CAPTURE** value; capture is the key design choice.
2. **Ten models:** platform, subscription, freemium, sharing, marketplace, advertising, e-commerce, ecosystem, usage/on-demand, experience.
3. Most real firms are **HYBRIDS**; digital lowers entry barriers so many models coexist.

**Next session (S23):** how value is actually generated — **value-creation models** and chain/shop/network.

---
---

# S23 — Value-Creation Models
**Lecture hour 8 of 10 (Unit 3) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] **"Factory, hospital, Pathao — three different ways to create value"**

> **Deliver (≈2 min):** "A factory MAKES value by turning materials into products. A hospital SOLVES a
> problem to create value. Pathao creates value by CONNECTING riders and drivers — it builds nothing and
> solves no single problem, yet creates huge value. Three fundamentally different ways to create value.
> Which one is a digital platform?"
>
> **Run (≈3 min):** Agenda: value creation vs capture + chain/shop/network → the 7 digital value-creation
> models → orchestration + Inputs→Process→Outputs→Impact.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Value Creation vs Capture; Chain, Shop, Network `[THEORY]` `[~8 min]`
[SLIDE] **Chain (make) · shop (solve) · network (connect) — platforms are networks**

> **Deliver:** Value **CREATION** is how a firm generates value; value **CAPTURE** (the business model, S22)
> is how it earns money from that value — two different questions. **Stabell & Fjeldstad's** classic
> framework gives three ways to CREATE value: the **VALUE CHAIN** (transform inputs into outputs — a
> factory), the **VALUE SHOP** (solve a customer's unique problem — a hospital, law firm, IT consultancy),
> and the **VALUE NETWORK** (connect members so they create value for each other — a bank, telecom, or
> platform).

- 🇳🇵 **Local example:** A Nepali handset assembler is a value **CHAIN** (inputs → phones). A Kathmandu
  hospital or audit firm is a value **SHOP** (diagnose and solve each client's problem). **Pathao and eSewa
  are value NETWORKS** — they create value by connecting members, and that value grows with network size.
  How each captures value (its business model) is a separate question: Pathao's network is captured via
  commission.

> ❌ **Misconception:** *"Every business creates value the same way."*
> ✅ **Correction:** "There are three distinct configurations: chain (make things), shop (solve problems),
> network (connect people). And value CREATION (how value is generated) is not value CAPTURE (how money is
> earned, S22). A firm can create value as a network yet capture it via commission, ads, or subscription."

> 🖼️ Visual: `s23_value_creation.png` — chain, shop, and network side by side.

> 🎯 **Exam-ready answer:** "Value creation is how value is generated; value capture (the business model) is
> how money is earned. Stabell & Fjeldstad give three creation configurations: value chain (transform inputs
> to outputs — factory), value shop (diagnose and solve a unique problem — hospital, consultancy), and value
> network (connect members — bank, telecom, platform). Most digital platforms are value networks, whose
> value grows with network size."

**📊 Depth table — Value chain vs value shop vs value network**

| Dimension | Value chain | Value shop | Value network |
|---|---|---|---|
| Logic | Transform inputs → outputs | Diagnose & solve a problem | Connect members to each other |
| Shape | Sequential / linear | Cyclical / iterative | Mediating / hub |
| Key activity | Production | Problem-solving | Matching & facilitation |
| Value driver | Efficiency, scale | Expertise, solution quality | Size of the network |
| Example | Factory, handset maker | Hospital, law/audit, IT consult | Bank, telecom, Pathao, marketplace |

*ℹ️ Most digital platforms are value NETWORKS: their value grows with the number of connected members (network effects, Unit 2), not with production efficiency (chain) or expertise (shop). Naming the configuration tells you what drives the firm's value.*

#### Concept 2 — The 7 Digital Value-Creation Models `[THEORY]` `[~7 min]`
[SLIDE] **Platform/ecosystem · data-driven · data-monetization · advertising · multi-stakeholder · experience · value-loop**

> **Deliver:** Beyond the classic three, digital markets create value in seven observed ways: (1)
> **PLATFORM/ECOSYSTEM** (connect and orchestrate participants); (2) **DATA-DRIVEN** (usage data → a better
> product); (3) **DATA-MONETIZATION** (sell insights/targeting); (4) **ADVERTISING/ATTENTION** (monetise
> engagement); (5) **MULTI-STAKEHOLDER** (value for several groups at once); (6) **EXPERIENCE** (a superior,
> personalised experience); (7) **VALUE-LOOP** (a self-reinforcing feedback loop — Unit 2's flywheel). These
> are digital specialisations of the value-network logic.

- 🇳🇵 **Local example:** **eSewa** creates value as a MULTI-STAKEHOLDER platform (users, merchants, banks,
  billers all gain) and a PLATFORM/ECOSYSTEM. **TikTok** creates value as DATA-DRIVEN (every swipe improves
  the feed), ADVERTISING/ATTENTION, and a VALUE-LOOP (use → better feed → more use). Firms combine several.

> ❌ **Misconception:** *"Digital firms all create value the same way (they just connect people)."*
> ✅ **Correction:** "Connecting is the base, but digital value creation specialises into seven forms —
> data-driven, data-monetization, advertising, multi-stakeholder, experience, value-loop, platform/
> ecosystem. Most firms combine several, and the value-loop is Unit 2's flywheel reappearing as value
> creation."

> 🎯 **Exam-ready answer:** "Digital markets create value in seven ways: platform/ecosystem, data-driven,
> data-monetization, advertising/attention, multi-stakeholder, experience, and value-loop (Unit 2's
> flywheel). These are digital specialisations of the value-network logic; firms usually combine several."

**📊 Depth table — The 7 digital value-creation models — examples**

| Model | How value is created | Example |
|---|---|---|
| Platform / ecosystem | Orchestrate many participants | Pathao, Daraz, Apple ecosystem |
| Data-driven | Usage data → better product | Google Maps, TikTok feed |
| Data-monetization | Sell insights / targeting | Ad networks, analytics firms |
| Advertising / attention | Monetise engagement | Meta, YouTube, TikTok |
| Multi-stakeholder | Value for several groups at once | eSewa (users/merchants/banks) |
| Experience | Superior, personalised experience | Netflix, Spotify personalisation |
| Value-loop | Self-reinforcing feedback loop | Amazon flywheel; TikTok use→feed |

*ℹ️ These seven overlap and combine — they are digital specialisations of the value-NETWORK logic. Several depend on data and network size (the forces from Unit 2), and the value-loop is the flywheel by another name.*

#### Concept 3 — Orchestration & Inputs→Process→Outputs→Impact `[THEORY]` `[~7 min]`
[SLIDE] **Platforms ENABLE value they don't produce — mapped IPOI**

> **Deliver:** A platform does not produce value directly — it **ORCHESTRATES** it: setting the rules,
> matching participants, ensuring trust, and steering the ecosystem so members create value for each other
> ("Uber doesn't drive cars — it orchestrates value creation"). Any value-creation process maps as **Inputs
> → Process → Outputs → Impact:** what goes in (participants, data), what the platform does (match, govern),
> what comes out (transactions, experiences), and the wider impact (jobs, market growth, financial
> inclusion).

- 🇳🇵 **Local example:** **Pathao** orchestrates rather than produces — it sets fares and rules, matches
  riders to drivers, ensures trust via ratings; the drivers create the rides. Mapped: Inputs (drivers,
  riders, data) → Process (match, price, govern) → Outputs (completed rides, ratings) → Impact (driver
  incomes, urban mobility, less idle capacity). Value CREATION (a network, orchestrated); its business model
  (S22) is how it CAPTURES that value — commission.

> ❌ **Misconception:** *"A platform produces its service like a factory."*
> ✅ **Correction:** "A platform ORCHESTRATES value it doesn't produce — it sets rules, matches, and ensures
> trust while members create the value. And don't confuse value creation (a network here) with the business
> model (commission). Both are chosen deliberately."

> 🎯 **Exam-ready answer:** "A platform orchestrates value rather than producing it — it sets rules, matches
> participants, ensures trust, and steers the ecosystem so members create value for each other. Any flow maps
> as Inputs → Process → Outputs → Impact. Value creation (how value is generated) stays distinct from the
> business model (how it is captured, S22)."

**📊 Depth table — Business model vs value-creation model (disambiguation)**

| Question | Business model (S22) | Value-creation model (S23) |
|---|---|---|
| Asks | How do you EARN money? | How is value GENERATED? |
| Focus | Revenue / capture mechanism | Configuration of value activities |
| Example labels | Subscription, ads, commission | Chain, shop, network; the 7 digital |
| Pathao | Commission (platform model) | Value network (connect riders/drivers) |
| Relationship | How you capture the value… | …the value you created here |

*ℹ️ Keep them distinct: value CREATION is how value is generated (chain/shop/network + the 7); the business model is how that value is CAPTURED as revenue (S22). A firm chooses both — Pathao creates as a network, captures via commission.*

#### 🛠 ACTIVITY — "Chain, shop, or network?" `[ACTIVITY]` `[~5 min]`
> **Run it:** In pairs (3 min) classify a factory, a hospital, a bank, and Pathao as chain/shop/network;
> map the network one as IPOI; state its business model to show creation ≠ capture. Take 3–4 answers (2 min).

> 🎙️ Factory = chain, hospital = shop, bank & Pathao = network. Pathao IPOI: inputs (riders/drivers/data) →
> process (match/price) → outputs (rides) → impact (incomes, mobility); captures via commission.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`
**MCQ 1.** A hospital or IT consultancy that diagnoses and solves a client's problem is a:
a) value chain  b) ✅ **value shop**  c) value network  d) value pipe
*(Why: the value shop creates value by solving a unique problem, iteratively.)*

**MCQ 2.** A business model and a value-creation model differ in that the business model answers:
a) how value is generated  b) ✅ **how you EARN money (capture)**  c) the logo  d) the tax rate
*(Why: value creation = how value is generated; business model = how that value is captured.)*

**Discussion prompt:** *Classify a Nepali firm as chain/shop/network and name its business model.*

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** separating how value is created from how it's captured is what lets you design a
platform deliberately — create as a network, capture via the right model. Next we make the market itself
DYNAMIC.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. Value **creation** (how value is generated) ≠ value **capture** (how money is earned). Classic configs: chain (make), shop (solve), network (connect).
2. **Seven digital value-creation models** specialise the network logic (platform/ecosystem, data-driven, data-monetization, advertising, multi-stakeholder, experience, value-loop).
3. Platforms **ORCHESTRATE** value they don't produce; map it as **Inputs → Process → Outputs → Impact.**

**Next session (S24):** putting it in motion — **modelling digital markets**, static vs dynamic.

---
---

# S24 — Modelling Digital Markets
**Lecture hour 9 of 10 (Unit 3) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] **"A snapshot vs a motion picture"**

> **Deliver (≈2 min):** "A business model is a snapshot — how a firm earns today. But markets MOVE: users
> sign up, convert, stay, or churn; prices rise at peak and fall off-peak; a market tips to one winner. To
> run or predict a digital market you need a MODEL of how it behaves over time, not just a snapshot."
>
> **Run (≈3 min):** Agenda: business model (static) vs market model (dynamic) → pricing as a lever + dynamic
> pricing → two-sided balance & tipping (cross-ref Unit 2).

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Business Model (Static) vs Market Model (Dynamic) `[THEORY]` `[~7 min]`
[SLIDE] **Static snapshot vs dynamic adoption/conversion/retention/churn**

> **Deliver:** A business model is largely **STATIC** — how a firm creates, delivers, and captures value at
> a point in time (S22). A **market model is DYNAMIC** — how the market behaves and evolves over time: how
> users are **ACQUIRED**, how many **CONVERT** (free→paid, visitor→buyer), how many are **RETAINED**, and
> how many **CHURN** (leave). Modelling these flows lets a firm predict growth, spot when a market will tip,
> and test 'what-if' pricing decisions.

- 🇳🇵 **Local example:** A Nepali **streaming startup's** BUSINESS MODEL might be freemium. Its MARKET
  MODEL asks: how many users acquired per month, what fraction convert to paid, how many stay, how many
  churn? The business model can look great yet fail if churn outpaces acquisition. You need both — the
  snapshot and the motion picture.

> ❌ **Misconception:** *"If the business model is sound, the firm will succeed."*
> ✅ **Correction:** "A sound business model can still fail if the market DYNAMICS are bad — high churn, low
> conversion, slow adoption. The market model captures that motion (acquire/convert/retain/churn) which the
> static business model cannot."

> 🎯 **Exam-ready answer:** "A business model is static (how a firm earns now); a market model is dynamic
> (adoption, conversion, retention, churn over time). Modelling these flows predicts growth, anticipates
> tipping, and tests pricing decisions. A freemium business model only works if its market model — conversion
> vs churn — adds up."

**📊 Depth table — Business model vs market model**

| Dimension | Business model (static) | Market model (dynamic) |
|---|---|---|
| Question | How does the firm earn? | How does the market behave over time? |
| Time | A snapshot | Evolution / motion |
| Key variables | Value proposition, revenue | Adoption, conversion, retention, churn |
| Use | Describe the firm | Predict growth & tipping; test decisions |
| Example | Freemium (free + paid tiers) | How many free users convert & stay per month |

*ℹ️ You need BOTH: the business model says how a freemium app earns; the market model predicts how many free users will convert and how fast churn erodes them — which decides whether the business model actually works at scale.*

#### Concept 2 — Pricing as a Lever; Dynamic & Algorithmic Pricing `[THEORY]` `[~7 min]`
[SLIDE] **Subscription · freemium · loss-leader · penetration · dynamic/surge**

> **Deliver:** Price is the most powerful **LEVER** in a market model — small changes swing adoption,
> conversion, and churn. Strategies: fixed **subscription**, **freemium**, **loss-leader** (sell below cost
> to win the market), **penetration** (low to grow fast), and **DYNAMIC/ALGORITHMIC pricing** — prices that
> change automatically with demand, time, or user data (surge). Dynamic pricing maximises revenue and
> balances supply/demand, but can anger users and raise fairness concerns.

- 🇳🇵 **Local example:** **Pathao** uses DYNAMIC (surge) pricing — when rush-hour demand exceeds available
  drivers, fares rise automatically to attract more drivers and ration rides. It balances supply and demand
  and lifts revenue, but riders resent paying more in the rain (a fairness tension). A new wallet instead
  uses PENETRATION pricing (heavy cashback) to win users fast.

> ❌ **Misconception:** *"Dynamic pricing is just greed / random price hikes."*
> ✅ **Correction:** "Surge pricing is an algorithmic balancing tool — it raises price when demand exceeds
> supply to attract more supply and ration scarce capacity. It is efficient and often necessary, though it
> can feel unfair; the design challenge is transparency."

> 🎯 **Exam-ready answer:** "Price is the key lever in a market model. Strategies include subscription,
> freemium, loss-leader, penetration, and dynamic/algorithmic pricing (prices auto-adjust to demand, time,
> or data — surge). Dynamic pricing maximises revenue and balances supply and demand (Pathao at peak) but
> can anger users and raise fairness concerns."

**📊 Depth table — Pricing strategies — how they work & examples**

| Strategy | How it works | Example |
|---|---|---|
| Subscription | Flat recurring fee | Netflix, Spotify Premium |
| Freemium | Free base, pay to upgrade | Spotify, Zoom, LinkedIn |
| Loss-leader | Sell below cost to win market | Launch discounts; free delivery deals |
| Penetration | Low price to grow fast | New wallet's heavy cashback |
| Dynamic / surge | Auto-adjust to demand/time | Pathao peak fares; airline seats |
| Algorithmic | Price set by data/algorithm | E-commerce price changes by demand |

*ℹ️ Pricing is the fastest lever in the market model: a loss-leader launch buys adoption, freemium buys reach, surge balances supply. Dynamic/algorithmic pricing is efficient but can feel unfair — a real tension for Pathao at peak.*

#### Concept 3 — Two-Sided Balance & Tipping (cross-ref Unit 2) `[THEORY]` `[~6 min]`
[SLIDE] **Model both sides; watch for tipping**

> **Deliver:** Modelling a digital market must handle its **two-sided nature** (Unit 2 S11): the platform
> decides who to **SUBSIDISE** and who to **CHARGE**, and must keep both sides in balance — too few drivers
> and riders leave; too few riders and drivers leave. The model also predicts **TIPPING:** strong network
> effects and switching costs can tip the market to one winner (winner-take-most, Unit 2 S13). Good market
> models track both sides' growth and watch for the tipping point.

- 🇳🇵 **Local example:** **Pathao's** market model must balance two sides — subsidise/attract enough drivers
  (bonuses, fair fares) or riders wait and leave; keep fares acceptable or riders leave and drivers idle. It
  also watches tipping — if it locks in enough drivers and riders in a city, the market could tip its way.
  **Gillette's razor-and-blades** and **credit cards** show the same two-sided logic long before the
  internet.

> ❌ **Misconception:** *"Two-sided pricing and tipping are new internet ideas."*
> ✅ **Correction:** "Razor-and-blades (Gillette) and credit cards ran two-sided pricing for decades; digital
> just runs it dynamically and at scale. In a market model these are VARIABLES — who to subsidise, whether
> the market will tip — not fresh theory; they're Unit 2 applied dynamically."

> 🎯 **Exam-ready answer:** "A market model must handle two-sidedness (Unit 2 S11): decide whom to subsidise
> and whom to charge, and keep both sides balanced. It also predicts tipping — strong network effects and
> switching costs can tip the market to one winner (Unit 2 S13). Credit cards and Gillette's razor-and-blades
> show two-sided pricing predates the internet; digital runs it dynamically."

**📊 Depth table — Two-sided pricing cases — who subsidises whom**

| Case | Subsidised side | Paying side | Why |
|---|---|---|---|
| Credit card | Cardholders (rewards) | Merchants (fees) | Shoppers attract merchants who pay to accept |
| Adobe (PDF/Reader) | Readers (free) | Creators (pay for Acrobat) | Free readers make the paid tool worth buying |
| Pathao | Riders (low fares off-peak) | Riders at peak / commission | Balance demand; drivers earn, platform takes cut |
| Gillette (razor-blade) | Buyers (cheap razor) | Buyers (pricey blades) | Cheap razor locks in profitable blade sales |
| Google | Users (free search) | Advertisers | Users' attention is sold to advertisers |
| Console gaming | Gamers (cheap console) | Game publishers (licence fees) | Cheap console builds base; games earn |

*ℹ️ The razor-and-blades and credit-card cases show two-sided pricing predates the internet — but digital markets run it dynamically. Modelling WHO subsidises WHOM, and keeping both sides balanced, is central to any market model (Unit 2 S11).*

#### 🛠 ACTIVITY — "Model the market" `[ACTIVITY]` `[~5 min]`
> **Run it:** In pairs (3 min) pick a Nepali platform; state its business model (static) AND its
> market-model variables (adoption/conversion/retention/churn); choose a pricing strategy and predict
> tip-or-contested. Take 3–4 answers (2 min).

> 🎙️ Streaming app: business model = freemium; market model = acquire via ads, ~5% convert, watch churn;
> pricing = penetration then subscription; likely contested (easy multi-homing).

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`
**MCQ 1.** A business model describes how you EARN; a market model describes:
a) the logo  b) the office  c) ✅ **how the market behaves over time (adoption, churn, tipping)**  d) the tax rate
*(Why: the market model is dynamic — acquisition, conversion, retention, churn, and tipping over time.)*

**MCQ 2.** Pathao raising fares automatically at peak demand is:
a) freemium  b) a subsidy  c) loss-leader  d) ✅ **dynamic (surge) pricing**
*(Why: prices auto-adjust to demand/time — dynamic/algorithmic (surge) pricing.)*

**Discussion prompt:** *For a Nepali platform, name its market-model variables and one pricing lever.*

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** modelling the market in motion is how a firm predicts growth, prices smartly, and
spots tipping before rivals — the analytical core of digital strategy. The final session ties everything
together.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Business model = static** (how you earn); **market model = dynamic** (adoption, conversion, retention, churn) — you need both.
2. **Price is the key lever:** subscription, freemium, loss-leader, penetration, dynamic/surge — efficient but with a fairness tension.
3. Model both sides (subsidise/charge, keep balanced) and watch for **tipping** — Unit 2 S11 & S13 applied dynamically.

**Next session (S25):** the capstone — **strategy, control points & the integrated framework.**

---
---

# S25 — Strategy & Integration (closes Unit 3)
**Lecture hour 10 of 10 (Unit 3) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] **"Who keeps the profit?"**

> **Deliver (≈2 min):** "You now know how digital markets compete, cooperate, layer, innovate, earn, create
> value, and move. Strategy ties them together — and its hardest part is not creating or capturing value,
> but DEFENDING it. Why can two firms create the same value, yet one keeps the profit and the other loses
> it? The answer is control points."
>
> **Run (≈3 min):** Agenda: strategy = create + capture + DEFEND + control points → strategy trade-offs →
> the integrated framework applied to Pathao + trends & Nepal.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Strategy = Create + Capture + Defend; Control Points `[THEORY]` `[~8 min]`
[SLIDE] **Defend value through control points: data, algorithms, standards, user relationships**

> **Deliver:** Digital strategy has three jobs: **CREATE** value (S23), **CAPTURE** it (S22), and — the
> hardest — **DEFEND** it against imitation and rivals. Value is defended through **STRATEGIC CONTROL
> POINTS:** the chokepoints others must pass through, which confer lasting power. The four main ones are
> **DATA** (who owns the user data), **ALGORITHMS** (who runs the matching/ranking), **STANDARDS** (the
> format others must adopt), and **USER RELATIONSHIPS** (who owns the customer). "Whoever controls the
> control point controls the market."

- 🇳🇵 **Local example:** **Pathao's** real defence is its control points — the DATA on riders/drivers and
  city demand, the ALGORITHM that dispatches efficiently, and the USER RELATIONSHIP with everyday riders. A
  rival can copy the app (create the same value) but not instantly copy Pathao's data, dispatch quality, or
  user base. Globally, **Apple** defends via the App Store standard and the customer relationship (the ~30%
  cut).

> ❌ **Misconception:** *"If you create value, you'll automatically keep the profit."*
> ✅ **Correction:** "Value that isn't DEFENDED is competed away — rivals copy it. Profit is kept by holding
> a control point (data, algorithms, standards, or the customer relationship) others must pass through.
> Strategy is create + capture + DEFEND, and defending is the part firms most neglect."

> 🖼️ Visual: `s25_control_points.png` — the four control points around a central chokepoint.

> 🎯 **Exam-ready answer:** "Digital strategy has three jobs: create value, capture it, and defend it against
> imitation — the hardest. Value is defended through strategic control points — chokepoints others must pass
> through — the four main ones being data, algorithms, standards, and user relationships. 'Whoever controls
> the control point controls the market' (Pathao's data/dispatch/users; Apple's App Store)."

**📊 Depth table — Strategic control points — who controls, and how**

| Control point | Why it confers power | Who holds it (example) |
|---|---|---|
| Data | Un-copyable user data → better product | Google, Meta, Amazon |
| Algorithms | Owns the matching/ranking/feed | TikTok feed; Uber/Pathao dispatch |
| Standards | Others must adopt the format | Visa, Fonepay QR, Windows, USB-C |
| User relationship | Owns the customer & the demand | Apple, Amazon, the bank's app |
| App store / gateway | Others must pass through to reach users | Apple/Google Play (~30% cut) |
| Infrastructure / cloud | Everyone builds on it, pays rent | AWS, foreign cloud (Nepal depends) |

*ℹ️ Two firms can create the same value; the one holding a control point (data, algorithm, standard, or the customer) keeps the profit. For Nepal, the warning from S20 repeats: control points (cloud, app stores) sit largely abroad.*

#### Concept 2 — Strategy Trade-Offs `[THEORY]` `[~7 min]`
[SLIDE] **Growth vs profit · openness vs control · scale vs focus**

> **Deliver:** Digital strategy is a series of **trade-offs**, not a single best answer. **GROWTH vs
> PROFIT:** chase share now (subsidise, burn cash) or profit today? **OPENNESS vs CONTROL:** an open platform
> grows faster but you control less; a closed one controls more but grows slower. Also **scale vs focus,
> cooperation vs competition, short-term revenue vs long-term trust.** Amazon chose growth and cross-subsidy
> for years; a focused Nepali startup may choose profit and a niche.

- 🇳🇵 **Local example:** **Amazon** chose GROWTH over PROFIT for years — cross-subsidising, reinvesting,
  thin margins — a strategy only deep capital allows. **Daraz** pursued SCALE and data. But a small Nepali
  startup usually cannot out-spend giants, so it should choose **FOCUS over scale** and **profit/trust over
  growth-at-all-costs** — win one niche deeply rather than fight everywhere.

> ❌ **Misconception:** *"There is one winning digital strategy (just grow fast like Amazon)."*
> ✅ **Correction:** "Growth-at-all-costs suits firms with deep capital and tipping markets; it bankrupts a
> small player in a contested one. Strategy is trade-offs — growth vs profit, openness vs control, scale vs
> focus — and the right choice depends on the market and your resources. For most Nepali startups, focus
> beats scale."

> 🎯 **Exam-ready answer:** "Digital strategy is a set of trade-offs, not one best answer: growth vs profit,
> openness vs control, scale vs focus, cooperation vs competition, short-term revenue vs long-term trust. No
> choice is universally right — it depends on the market and the firm's position. Amazon chose growth and
> cross-subsidy for years; a focused Nepali startup usually wins by choosing profit and a niche."

**📊 Depth table — Strategy trade-offs — the two sides**

| Trade-off | Choose one side… | …or the other |
|---|---|---|
| Growth vs profit | Growth: subsidise, win share now | Profit: earn today, grow slower |
| Openness vs control | Open: grow fast, control less | Closed: control more, grow slower |
| Scale vs focus | Scale: go broad, many markets | Focus: one niche done best |
| Cooperate vs compete | Cooperate: grow the pie (co-opetition) | Compete: fight for the whole slice |
| Short vs long term | Short: revenue now | Long: build trust, monetise later |

*ℹ️ There is no universally right choice — the answer depends on the market, the firm's resources, and its position. Amazon chose growth/openness for years; a small Nepali startup usually wins by choosing focus and long-term trust.*

#### Concept 3 — The Integrated Framework + Trends + Nepal `[THEORY]` `[~7 min]`
[SLIDE] **Value creation + business model + market model + strategy — Nepal: focus, not scale**

> **Deliver:** Everything in this unit fits one integrated framework: a digital firm chooses a
> **VALUE-CREATION** model (S23), a **BUSINESS** model to capture it (S22), operates in a **MARKET** model it
> must manage (S24), and defends it all with **STRATEGY** and control points (S25) — while competing,
> cooperating, and co-opeting (S17–S19) across a layered internet (S20) through innovation (S21). Emerging
> trends (**AI, blockchain, IoT**) and regulation will reshape all four. For Nepal, the strategic lesson is
> **"focus, not scale"** — win a niche, fit the local context, build trust.

- 🇳🇵 **Local example:** Read **Pathao** across the four dimensions — it CREATES value as a network (S23),
  CAPTURES it via commission (S22), operates a two-sided, surge-priced, contested MARKET (S24), and DEFENDS
  it with data, its dispatch algorithm, and local user relationships (S25) — competing with InDrive while
  co-opeting with banks. Its winning strategy is focus, not scale — own the local market giants
  underprioritise.

> ❌ **Misconception:** *"The four topics — value, business model, market, strategy — are separate."*
> ✅ **Correction:** "They are one integrated system: value creation feeds the business model, which plays
> out in a market model, all defended by strategy and control points, on top of the layered internet and
> driven by innovation. Analysing a firm on ALL four at once is the point of Unit 3."

> 🎯 **Exam-ready answer:** "One integrated framework ties the unit together: a firm chooses a value-creation
> model (S23), a business model to capture it (S22), operates in a market model it must manage (S24), and
> defends it with strategy and control points (S25) — while competing, cooperating, and co-opeting across a
> layered internet via innovation. Trends (AI, blockchain, IoT) and regulation reshape all four. Nepal's
> lesson: focus, not scale."

**📊 Depth table — The integrated framework applied to Pathao (4 dimensions)**

| Dimension | What it asks | Pathao |
|---|---|---|
| Value creation (S23) | How is value generated? | Value NETWORK — connects riders & drivers |
| Business model (S22) | How is value captured? | Platform/commission per ride (+ Food) |
| Market model (S24) | How does the market behave? | Two-sided; surge pricing; contested (multi-homing) |
| Strategy (S25) | How is value defended? | Data, dispatch algorithm, user relationship; focus on Nepal |

*ℹ️ This one table IS the unit: any digital firm can be read across the four dimensions — how it creates value, captures it, behaves as a market, and defends it. Pathao's edge is local focus + control points, not out-spending global giants.*

#### 🛠 ACTIVITY — "Integrate a Nepali platform" `[ACTIVITY]` `[~5 min]`
> **Run it:** In pairs (4 min) pick a Nepali platform (not Pathao); map it across ALL FOUR dimensions; name
> its strongest control point and one strategy trade-off. Take 3–4 answers (1 min). This rehearses the
> integration exam question directly.

> 🎙️ eSewa: creation = multi-stakeholder network; business model = platform/commission + float; market =
> two-sided, concentrating; strategy = control points (merchant network, data, user relationship),
> trade-off = openness vs control. Reward all four dimensions + a named control point.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`
**MCQ 1.** Controlling the data, algorithms, or standards others must pass through is holding a:
a) ✅ **strategic control point**  b) a patent  c) a subsidy  d) a pipe
*(Why: a control point is a chokepoint others must pass through — it defends value and confers power.)*

**MCQ 2.** For most Nepali startups facing global giants, the wisest strategy is usually:
a) out-spend them on scale  b) ✅ **focus on a niche and fit local context**  c) copy them exactly  d) avoid digital
*(Why: small players can't win a spending war; 'focus, not scale' wins a niche giants underprioritise.)*

**Discussion prompt:** *Map any Nepali platform across value creation, business model, market model, strategy.*

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** it closes Unit 3: you can now analyse ANY digital firm across all four dimensions
and judge how it competes, cooperates, and defends its value — the exact skill the integration exam question
tests, and the skill a founder or analyst uses in the real Nepali market.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. Digital strategy = **create + capture + DEFEND** value; defence comes from **control points** (data, algorithms, standards, user relationships).
2. Strategy is **trade-offs:** growth vs profit, openness vs control, scale vs focus — no universally right answer.
3. **Integrated framework:** value creation + business model + market model + strategy, on competition/co-opetition, layers & innovation. **Nepal: focus, not scale.**

**Next unit (Unit 4):** Digital Transformation & Currencies — how organisations and money themselves go digital.

---
---

# 📄 UNIT 3 — CHEAT SHEET
*One-page revision reference — what to read the night before the exam.*

| Topic | The compressed essentials |
|---|---|
| **Digital markets (S16)** | Online space matching buyers & sellers. **4 traits:** speed, scale, network effects, LOW marginal cost. **5 components:** platform, payments, logistics, data & analytics, support/trust. **5 types:** B2C, B2B, C2C, C2B, P2P. |
| **Competition & cooperation (S17–S18)** | Digital competes on data, network, speed, UX (Porter's 5 forces bent by network effects) → winner-take-most, but multi-homing keeps some contested. Cooperation ('grow the pie first'): 5 reasons; 3 forms = joint platforms, partnerships, service integration. |
| **Co-opetition & layers (S19–S20)** | Co-opetition = cooperate UPSTREAM (tech/rails/standards) + compete DOWNSTREAM (customers); Value-Net adds complementors. Layered internet: infrastructure → platform → application (+user); value flows UP, power flows DOWN (control lower = power over higher). |
| **Innovation & business models (S21–S22)** | Innovation ≠ invention (value, not just tech); sustaining vs disruptive; 6 types; enablers AI/IoT/cloud/big data/AR/VR; ideation→MVP→scale. Value triad: create/deliver/capture. 10 models (platform, subscription, freemium, sharing, marketplace, advertising, e-commerce, ecosystem, usage, experience) — hybrids normal. |
| **Value creation & market model (S23–S24)** | Creation ≠ capture. Chain (make) / shop (solve) / network (connect); platforms = networks; 7 digital models; orchestration; Inputs→Process→Outputs→Impact. Business model (static) vs market model (dynamic: adoption/conversion/retention/churn). Pricing lever incl. dynamic/surge; two-sided balance & tipping. |
| **Strategy & integration (S25)** | Strategy = create + capture + DEFEND. Control points: data, algorithms, standards, user relationships. Trade-offs: growth vs profit, openness vs control, scale vs focus. Integrated framework = value creation + business model + market model + strategy. Nepal: focus, not scale. |

---

# 📖 UNIT 3 — GLOSSARY
*Key terms — quick reference.*

| Term | Definition |
|---|---|
| **Digital market** | An online space where buyers & sellers match, price & transact. |
| **Marginal cost** | Cost of serving one more user — near-zero for digital markets. |
| **Digital market types** | B2C, B2B, C2C, C2B, P2P — classified by who sells to whom. |
| **Winner-take-most** | The leading platform captures the bulk of the market. |
| **Multi-homing** | Users/suppliers using several competing platforms at once. |
| **Porter's Five Forces** | Rivalry, entrants, buyer power, supplier power, substitutes. |
| **Cooperation** | Firms working together to create value none could alone. |
| **Joint platform** | Rivals sharing common rails/standards (ConnectIPS, SWIFT). |
| **Service integration** | Embedding one service inside another for seamlessness. |
| **Co-opetition** | Cooperating & competing with the same firm at once. |
| **Upstream / downstream** | Shared tech/rails (upstream) vs customers/brand (downstream). |
| **Value-Net** | Customers, suppliers, competitors & complementors around a firm. |
| **Complementor** | A firm whose product makes yours more valuable. |
| **Layered internet model** | Infrastructure → platform → application (+ user), business view. |
| **Layer power** | Control of a lower layer confers power over higher layers. |
| **Digital innovation** | Creating new value with digital tech (product, process, model…). |
| **Innovation vs invention** | Value people use (innovation) vs a new technology (invention). |
| **Sustaining innovation** | Improving a product for existing customers. |
| **Disruptive innovation** | Cheap, 'good-enough' entry that rises to overtake incumbents. |
| **Business model** | How a firm creates, delivers & captures value. |
| **Value triad** | Create + deliver + capture value. |
| **Freemium** | Free base tier, pay to upgrade. |
| **Ecosystem model** | Bundling services to lock users in. |
| **Value creation** | How a firm generates value (vs capture = how it earns). |
| **Value chain / shop / network** | Make / solve a problem / connect members (Stabell–Fjeldstad). |
| **Orchestration** | A platform enabling value it does not itself produce. |
| **Inputs→Process→Outputs→Impact** | A map of any value-creation flow end to end. |
| **Market model** | Dynamic view: adoption, conversion, retention, churn over time. |
| **Dynamic / surge pricing** | Prices that auto-adjust to demand, time, or data. |
| **Two-sided balance** | Keeping both platform sides growing (subsidise/charge). |
| **Strategic control point** | A chokepoint (data, algorithm, standard, customer) that defends value. |
| **Focus, not scale** | Nepal strategy: win a niche & fit local context, don't out-spend giants. |

---

# 📋 UNIT 3 — END-OF-UNIT QUIZ
*Use as a 15–20 min in-class quiz or a take-home review. Answer key at the end.*
*(Note: no genuine IT 250 past-paper was available — these are built from the syllabus and the concept slides.)*

### Section A — Multiple Choice (1 mark each · correct letter varies)
1. A defining characteristic of a digital market is:
   a) high marginal cost per user  b) ✅ near-zero marginal cost & network effects  c) fixed local reach  d) slow price changes
2. "Winner-take-most" means:
   a) all firms share equally  b) the newest firm wins  c) ✅ the leading platform captures the bulk of the market  d) government picks the winner
3. Two banks jointly running ConnectIPS is cooperation via:
   a) ✅ a joint platform  b) a price war  c) an acquisition  d) advertising
4. Co-opetition typically means firms:
   a) compete on everything  b) cooperate on everything  c) merge  d) ✅ cooperate upstream (tech) & compete downstream (customers)
5. Cloud, data-centres & connectivity belong to which layer?
   a) application  b) ✅ infrastructure  c) user  d) payment
6. "Innovation is not invention" means innovation is about:
   a) ✅ creating value people use, not just inventing tech  b) patents only  c) pure research  d) copying
7. A cheap, "good-enough" entrant that rises to overtake incumbents is:
   a) sustaining innovation  b) ✅ disruptive innovation  c) invention  d) marketing innovation
8. Netflix charging a flat monthly fee is which business model?
   a) freemium  b) marketplace  c) ✅ subscription  d) advertising
9. A hospital or consultancy that diagnoses & solves a problem is a:
   a) value chain  b) ✅ value shop  c) value network  d) value pipe
10. A business model shows how you EARN; a market model shows:
    a) the logo  b) the office  c) ✅ how the market behaves over time (adoption, churn, tipping)  d) the tax rate
11. Pathao raising fares automatically at peak demand is:
    a) freemium  b) a subsidy  c) loss-leader  d) ✅ dynamic (surge) pricing
12. Controlling data/algorithms/standards others must pass through is holding a:
    a) ✅ strategic control point  b) a patent  c) a subsidy  d) a pipe

### Section B — Short Answer (2 marks each)
13. **Define co-opetition** and give a Nepali example.
14. **Name the three internet layers** and the direction value flows.
15. **Name three digital business-model types.**
16. Explain **value chain vs value shop vs value network.**
17. What is a **strategic control point**? Name two.

### Section C — Applied Case (3 marks each)
18. **Map Pathao across ALL FOUR dimensions:** value creation · business model · market model · strategy (the integration question).
19. Explain a **Nepali co-opetition case** (eSewa + Nabil, or Daraz + Pathao): what is shared upstream, what is competed downstream?

### Section D — Discussion (open-ended)
20. "**Is Pathao's dominance good for Nepal? Should digital platforms be regulated? Can Nepali startups compete — focus or scale?**" Argue using the unit's concepts and state your own position.

---

### ✅ Answer Key (Section A)
**1-b · 2-c · 3-a · 4-d · 5-b · 6-a · 7-b · 8-c · 9-b · 10-c · 11-d · 12-a**
*(Note the correct answer deliberately varies its position across questions — a, b, c, and d all appear.)*

> **Sections B–D: grade on key terms.** **Q13** — co-opetition = cooperating & competing with the same firm
> at once (cooperate upstream on tech/rails, compete downstream for customers); e.g. eSewa & Nabil, or two
> wallets sharing ConnectIPS while competing on cashback. **Q14** — infrastructure → platform → application
> (+ user); value flows UP (technical → capability → experience), power flows DOWN. **Q15** — any three of:
> platform, subscription, freemium, sharing, marketplace, advertising, e-commerce, ecosystem, usage/on-demand,
> experience. **Q16** — chain = transform inputs→outputs (factory); shop = diagnose & solve a problem
> (hospital, consultancy); network = connect members (bank, telecom, platform). **Q17** — a control point is
> a chokepoint others must pass through that defends value; any two of data, algorithms, standards, user
> relationships (also app store/gateway, infrastructure). **Q18** — Pathao: creation = value network
> (riders↔drivers); business model = platform/commission; market model = two-sided, surge-priced, contested
> (multi-homing); strategy = defend via data/dispatch algorithm/user relationship, focus on Nepal. **Q19** —
> name what is shared upstream (rails/standards, e.g. ConnectIPS/QR) and what is competed downstream (app UX,
> cashback, customers); one benefit + one risk. **Q20** — reward using tipping/winner-take-most, control
> points, and the growth-vs-focus trade-off, ending with a reasoned position (dominance is a tendency,
> contestable; regulation via portability/interoperability; Nepali startups usually win by focus, not scale).

---

## ✅ Unit 3 complete (full lecturer-ready depth)
The deck is built: **IT250_Unit3.pptx** — diagram-rich, self-contained, and PDF-safe, carrying all
**31 §7A depth tables** (comparison, concrete-example, and scaffolding types) across 10 sessions and 30
concepts, plus **6 diagrams** (digital-market ecosystem, co-opetition upstream/downstream, the layered
internet model, sustaining-vs-disruptive innovation, value chain/shop/network, strategic control points).
This Markdown source carries those **same 31 depth tables inline** under each concept, so the source of
truth and the deck stay in sync. Regenerated via `build_unit3_pptx.py` (imports `deckkit.py`). Built to
**COURSE_MATERIAL_STANDARD.md**, Nepal-localised throughout, and building directly on Unit 2 (network
effects, two-sided markets, tipping cross-referenced). **Next: Unit 4 — Digital Transformation & Currencies.**
