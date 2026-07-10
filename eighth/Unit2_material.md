# IT 250 — Unit 2: Fundamentals of the Digital Economy
### Full Lecturer-Ready Session Material (S9–S15)

**Program:** BIM, 8th Semester · **Unit weight:** 7 lecture hours
**Sessions:** S9–S15 (50 min each) · **Local context:** Nepal / South Asia
**Format:** Markdown — source of truth; the built deck is `IT250_Unit2.pptx`, regenerated via `build_unit2_pptx.py` (imports `deckkit.py`). Built to **COURSE_MATERIAL_STANDARD.md** — self-contained, PDF-safe, and carrying the **§7A depth tables** (every confusable set → a comparison table; every "X vs not-X" idea → a concrete-example table). Localised to Nepal's digital economy. Continues session numbering from Unit 1 (S1–S8).

> **How to read this file.** This is written to **carry a full 50 minutes on its own.** Each session
> has **minute markers** `[~X min]`, the actual **explanation to deliver** (prose, not just bullets),
> a **worked Nepal example**, a **common misconception + correction**, a **🎯 exam-ready answer**, an
> embedded **§7A depth table**, a **timed in-class activity**, and lecturer cue cards in `> 🎙️` blocks.
> `[SLIDE]` marks slide-ready blocks; `🖼️` marks diagram cues. Pace tags: `[THEORY] [EXAMPLE]
> [ACTIVITY] [QUIZ]`. Total per session: **5 + 35 + 5 + 3 + 2 = 50 min.** The 21 depth tables below are
> the SAME ones generated in `build_unit2_pptx.py`, so this source and the deck stay in sync.

> ⚠️ **Exam-alignment note.** **No genuine IT 250 past-paper was available** (see Unit 1 — the only
> question-paper artifact in the repo is school-level English/Social-Studies, not this course).
> Therefore every **🎯 exam-ready answer** and the end-of-unit quiz are derived from the **syllabus
> wording + the concept slides + the strong in-lecture recap artifacts** — especially the L7 "analyse
> a platform on 4 concepts (network effect · lock-in · switching cost · monopoly risk)" activity and
> its summary rating table, the most exam-ready item in the unit. Treat the framings as strong model
> answers, and update them if a real IT 250 paper surfaces.

> 📌 **Scope decisions locked for this unit.** (1) **S11 absorbs the platform ECONOMICS deferred from
> Unit 1 S1** — two-sided pricing, cross-subsidy (the money side vs the subsidy side), and the
> quantitative zero-marginal-cost / economies-of-scale story that Unit 1 taught only intuitively.
> (2) **The syllabus's "OECD digital adoption government index" is taught as the OECD Digital
> Government Index (DGI)** — this matches the syllabus wording and the old material. If an examiner
> means the UN E-Government Development Index (EGDI), that is not in the source material and would be
> added separately. (3) **Nepal policy DEPTH is still held for Unit 6** (Digitalization — the
> Nepalese Perspective); regulation here (S14) stays at the concept-and-tools level, using NRB's QR
> interoperability as the local anchor.

---

## Unit 2 — Learning Outcomes
By the end of this unit, students will be able to:
1. **Distinguish a platform business** from a traditional (pipe) business and **define a multi-sided platform** (S9).
2. **Explain network effects** — direct, indirect/cross-side, data, and standard — and **positive feedback**, including their limits (negative network effects) (S10).
3. **Explain two-sided market pricing** — cross-subsidy, the money side vs the subsidy side, and why one side is often free — plus zero marginal cost and the chicken-and-egg launch problem (S11).
4. **Explain lock-in and switching costs** (five types), how platforms engineer them, the **flywheel**, and **multi-homing** (S12).
5. **Explain how digital monopolies form** (the six forces, tipping, winner-take-most), their **risks**, and how they are **regulated** (S13–S14).
6. **Describe how digital adoption is measured** — the World Bank **DAI** (3 pillars) and the OECD **DGI** (6 dimensions) — and **assess Nepal's position** (S15).

> This is Unit 2 of IT 250 — the **engine room** of the course. Unit 1 defined the digital and
> knowledge economies and the 4IR; Unit 2 opens the hood and explains **WHY platforms win**, how value
> and prices really work in two-sided markets (the economics deferred from Unit 1), how dominance
> forms, and how the tools to check it work. It feeds directly into Unit 3 (digital markets &
> strategy), Unit 4 (digital transformation & currencies), Unit 5 (economics of information), and
> Unit 6 (digitalization — the Nepalese perspective).

---
---

# S9 — Multi-Sided Platforms: Pipes vs Platforms
**Lecture hour 1 of 7 (Unit 2) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"They own nothing — and they're worth the most"**

> **Deliver (≈2 min):** Read the paradox out loud. "**Daraz owns almost no products. Pathao owns no
> taxis. Airbnb owns no hotels.** Yet each is worth more than the firms that own everything they sell.
> How does a company that **MAKES nothing** become so valuable?"
>
> **Run a quick reaction (≈3 min):** Take a few answers. Most students say "because it's online" or
> "it's an app." Hold that — you will show the answer is a **business model**, not a website. Land the
> agenda: **pipe vs platform → what a multi-sided platform is → how platforms create value.**

> 🎙️ Speaker note: Don't resolve the paradox yet — the point is to surface that the value comes from
> connecting others, not from producing. Agenda on the board: pipe vs platform → MSP → value creation.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Pipe (Linear) vs Platform Business `[THEORY]` `[~7 min]`

[SLIDE] **A pipe MAKES the value; a platform CONNECTS the people who make it**

> **Deliver:** Give the distinction and write it on the board. **A pipe (linear) business creates a
> product or service and sells it to customers — value flows one way, Business → Customer. A platform
> business instead connects two or more groups and lets them create value for each other — value flows
> in many directions.** The platform does not make all the value; it makes the interactions possible.
> Then make three moves:
> - A **pipe** produces the value itself (Netflix originals, a software licence, a factory's goods).
> - A **platform** produces the **marketplace**; its **users** produce the value for each other.
> - A pipe grows by **making/selling more units**; a platform grows by **adding more participants** —
>   and because its "suppliers" are its users, it can scale without making the goods itself.

- 🇳🇵 **Local example (walk through it):** **Foodmandu makes no food and owns no kitchens.** It connects
  restaurants, riders, and hungry customers, and takes a cut of the interactions it enables — that is a
  platform. A traditional restaurant that cooks and sells its own meals is a **pipe.** Foodmandu can add
  a thousand restaurants without building a single kitchen; the restaurant can only grow by cooking more.
  **That is the structural difference** between the two models in one Kathmandu example.

> ❌ **Common misconception:** *"A platform is just a website or a middleman."*
> ✅ **Correction — say it out loud:** "A website is a **channel**; a platform is a **business model**
> where value is created by users interacting, not by the firm producing. The firm builds and governs
> the marketplace — matching, trust, tools — it does **not** make the goods. That is exactly why it
> scales."

> 🖼️ Visual: `s9_pipe_platform.png` — a **pipe** (Business → Customer, one arrow) beside a **platform**
> (users ↔ platform ↔ users, many arrows), labelled "MAKES value" vs "CONNECTS groups."

> 🎯 **Exam-ready answer:** "A pipe (linear) business creates a product or service and sells it to
> customers, with value flowing one way (business → customer) and growth coming from making/selling more
> units. A platform business connects two or more groups and enables them to create value for each other,
> with value flowing in many directions and growth coming from adding participants. The most valuable
> digital firms are platforms because their **users, not the firm, do the producing** — so they scale
> without making the goods themselves."

> 🎙️ Speaker note: ~7 min. Use the diagram. The key shift is that a platform's suppliers are its users,
> so it scales without making the goods itself.

**📊 Depth table — Pipe business vs platform business**

| Question | Pipe (linear) business | Platform business |
|---|---|---|
| Who creates the value? | The firm itself | The users, for each other |
| Direction of value | One way: business → customer | Many ways: user ↔ platform ↔ user |
| How it grows | Make/sell more units | Add more participants |
| Main asset | Products, factories, inventory | The network of users & the matching |
| Cost of one more unit | Real (materials, labour) | Near-zero (a new listing/user) |
| Nepal example | A shop selling its own goods | Daraz, Pathao, Hamrobazar, Foodmandu |

*ℹ️ The platform's genius is that its 'suppliers' are its users — so it can scale to millions of listings or rides without ever making a product itself.*

#### Concept 2 — What a Multi-Sided Platform Is `[THEORY]` `[~7 min]`

[SLIDE] **Connects 2+ interdependent groups and solves their matching problem**

> **Deliver:** Give the definition. **A multi-sided platform (MSP) is a business model that connects two
> or more interdependent user groups to enable interactions and create value.** It solves a **matching
> problem** — buyers↔sellers, riders↔drivers, creators↔audiences — where each side needs the other. Its
> defining trait: **the value to any one side rises as more participants join the other side.** Then
> teach:
> - **Interdependent groups:** sellers are useless without buyers; drivers are useless without riders.
> - The platform solves the **matching problem** (who connects with whom, at what price).
> - **Five features:** facilitation (not production), 2+ groups, interaction-based value, low marginal
>   cost, scalability.
> - **"Sides" can be more than two:** Daraz has buyers, sellers, advertisers, and delivery partners.

- 🇳🇵 **Local example (name the sides):** **eSewa is a multi-sided platform.** It links **users** who
  want to pay, **merchants** who want to be paid, **banks** that hold the money, and **billers** (NEA,
  water, ISPs) who want collection. None of these sides is useful to eSewa alone — the value is in
  **matching them** so a payment flows instantly. Add more merchants and the wallet is more useful to
  users; add more users and it is more useful to merchants. That mutual pull is the MSP in action.

> ❌ **Common misconception:** *"A multi-sided platform is just a company with many customers."*
> ✅ **Correction:** "The difference is **interdependence** — the groups need **each other**, and the
> platform's job is to **match** them. A supermarket has many customers but **one side**; eSewa's users
> and merchants are **two interdependent sides** whose value to each other the platform creates."

> 🎯 **Exam-ready answer:** "A multi-sided platform (MSP) is a business model connecting two or more
> **interdependent** user groups to enable interactions and create value, solving a **matching problem**
> (buyers↔sellers, riders↔drivers, creators↔audiences) where each side needs the other. Its five features
> are **facilitation (not production), two-or-more groups, interaction-based value, low marginal cost,
> and scalability** — and the value to any side **rises as the other side grows.**"

> 🎙️ Speaker note: ~7 min. Stress interdependence and the "matching problem." Have students name the
> sides of eSewa (users, banks, merchants, billers) before revealing the table.

**📊 Depth table — Multi-sided platforms — the sides they connect**

| Platform | Side A | Side B (and more) | The matching problem solved |
|---|---|---|---|
| Pathao | Riders/passengers | Drivers (+ restaurants for Food) | Who gives whom a ride, at what price |
| Daraz | Buyers | Sellers (+ advertisers, couriers) | Which product from which seller |
| eSewa / Fonepay | Users/payers | Merchants, banks, billers | Who pays whom, settled instantly |
| Foodmandu | Hungry customers | Restaurants (+ delivery riders) | Which meal, cooked & delivered by whom |
| Hamrobazar | Buyers | Individual sellers | Matching second-hand supply & demand |
| YouTube | Viewers | Creators (+ advertisers) | Which video for which viewer |

*ℹ️ Notice the interdependence in every row: each side is worthless to the platform without the other. Getting BOTH sides on board at once is the 'chicken-and-egg' problem (S11).*

#### Concept 3 — How Platforms Create Value `[THEORY]` `[~7 min]`

[SLIDE] **Five ways to add value while making nothing yourself**

> **Deliver:** Name the five mechanisms. **Platforms create value in five ways, even though they make
> nothing themselves:** they **reduce transaction costs** (search, negotiation, enforcement), **match
> efficiently** using data and algorithms, **build trust** through reputation systems (ratings, reviews,
> verification), **provide tools and infrastructure** (payments, logistics, dashboards), and create
> **network value** (each user makes the platform more useful). Walk them:
> - **Reduce transaction costs:** finding and trusting a stranger to transact with becomes cheap.
> - **Efficient matching:** algorithms pair the right buyer/seller, rider/driver faster than any market
>   square.
> - **Trust:** ratings, reviews, verification, and dispute resolution let strangers transact safely.
> - **Tools + network value:** payment gateways, tracking, and the sheer number of users add value.
>
> Note that this is how the platform **earns its cut** — via commissions, ads, or subscriptions.

- 🇳🇵 **Local example (walk through one purchase):** On **Hamrobazar** you buy a used phone from a
  **stranger you'll never meet** — something risky in a newspaper classified — because ratings, reviews,
  and the platform's dispute process create **trust.** **Daraz** reduces your **search cost** (no visiting
  ten shops), **matches** you to sellers, handles **payment and returns** (tools), and is more useful
  because millions already use it (**network value**). That is **all five mechanisms in one purchase.**

> ❌ **Common misconception:** *"Platforms just take a commission for doing nothing."*
> ✅ **Correction:** "They capture value because they **remove real friction** — search cost, matching,
> trust, payments, logistics — that buyers and sellers **could not remove alone.** The commission is the
> **price of the friction they eliminate**, not a toll for nothing."

> 🧠 **Memory hook:** *"Cost, Match, Trust, Tools, Network"* — the five ways a platform earns its cut
> without making the product.

> 🎯 **Exam-ready answer:** "Platforms create value in five ways despite making nothing themselves:
> reducing **transaction costs** (search, negotiation, enforcement), enabling **efficient matching**
> (data/algorithms), building **trust** (ratings, reviews, verification, dispute resolution), providing
> **tools and infrastructure** (payments, logistics, dashboards), and creating **network value** (each
> user makes the platform more useful). They capture a share of this value through **commissions,
> advertising, or subscriptions.**"

> 🎙️ Speaker note: ~7 min. Trust is the underrated one — ratings let you buy from a stranger on
> Hamrobazar you'd never trust offline.

**📊 Depth table — The five ways platforms create value — with Nepal examples**

| Value mechanism | What it does | Nepal example |
|---|---|---|
| Reduce transaction costs | Cuts search, negotiation, enforcement effort | Daraz: find & buy without visiting shops |
| Efficient matching | Algorithms pair the right two sides fast | Pathao matches nearest driver to rider |
| Trust / reputation | Ratings, reviews, verification, disputes | Hamrobazar seller ratings; Daraz returns |
| Tools & infrastructure | Payments, logistics, tracking, dashboards | eSewa payment gateway; Foodmandu tracking |
| Network value | More users → more useful for everyone | Fonepay: accepted almost everywhere |

*ℹ️ A platform earns its cut by removing friction (cost, matching, trust) that individuals could not remove alone. This is the value it captures via commissions, ads, or subscriptions.*

#### 🛠 ACTIVITY — "Name the sides" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Pick a Nepali platform and list every side it connects**

> **Run it:** In pairs (2 min) students pick a Nepali platform (eSewa, Pathao, Daraz, Foodmandu,
> Hamrobazar) and **list every distinct SIDE it connects**, plus **the matching problem it solves.** They
> then **name which of the 5 value mechanisms it relies on most.** Take 3 answers aloud (3 min) and
> **check each named at least two interdependent sides.**

> 🎙️ Speaker note: Good answer for **Daraz** — buyers, sellers, advertisers, couriers; matching
> product↔buyer; relies on trust (ratings/returns) + reduced transaction cost. Reward spotting **more than
> two sides** and the interdependence.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** The key difference between a pipe and a platform business is:
a) size  b) ✅ **who creates the value — the firm (pipe) vs the users, for each other (platform)**  c) profit  d) age
*(Why: a pipe produces and sells value; a platform enables users to create value for each other.)*

**MCQ 2.** A multi-sided platform's defining feature is that its user groups are:
a) unrelated  b) all buyers  c) ✅ **interdependent — each side needs the other**  d) employees
*(Why: sellers are useless without buyers and vice versa; the platform's job is to match interdependent sides.)*

**Discussion prompt:** *Name a Nepali platform and every side it connects.*

> 🎙️ Speaker note: Cement "users create the value" and interdependence — the foundation for network
> effects (S10).

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** almost every fast-growing Nepali digital business — eSewa, Pathao, Daraz,
Foodmandu — is a **platform, not a pipe.** Understanding the model explains **why they scale so fast**
and **where their money comes from**, which you will need whether you build one, work for one, or compete
with one. The habit of asking "who are the sides, and what value does the platform add between them?" is
exactly how a product manager or founder spots an opportunity.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. A **pipe** business MAKES & sells value one way; a **platform** CONNECTS groups so **users create value** for each other.
2. A **multi-sided platform** links **2+ interdependent groups** and solves a **matching problem**; value rises as each side grows.
3. Platforms create value **five ways:** lower transaction costs, matching, trust, tools/infrastructure, network value.

**Next session (S10):** the force that makes platforms win — **network effects and positive feedback.**

---
---

# S10 — Network Effects & Positive Feedback
**Lecture hour 2 of 7 (Unit 2) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Why don't we use 20 messaging apps?"**

> **Deliver (≈2 min):** Ask the room. "Why don't we juggle **20 messaging apps**? Why did **WhatsApp
> take over Nepal** while **Viber quietly faded**? WhatsApp isn't twenty times better as software — but
> its **USERS are.** The value isn't only in the app; it's in **who else is on it.**"
>
> **Run the question (≈3 min):** Ask which messaging app everyone uses, and why. Take a few answers.
> Land the theme: **this is the single most important force in the digital economy.** Agenda: **network
> effects & positive feedback → the four types → the limits (negative network effects).**

> 🎙️ Speaker note: Draw out that everyone uses the app their contacts use — the value is in the network.
> Agenda on the board.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Network Effects & the Positive Feedback Loop `[THEORY]` `[~7 min]`

[SLIDE] **More users → more value → more users**

> **Deliver:** Give the definition. **A network effect exists when a product becomes more valuable as
> more people use it.** One fax machine is useless; a million are essential. This creates a **positive
> feedback loop:** more users → more value → attracts more users → more value. Because digital goods
> scale cheaply, this loop can run **explosively.** Then teach:
> - The **value is in the network**, not just the product — a phone nobody else has is worthless.
> - **Positive feedback:** success breeds success (users → value → more users).
> - **Metcalfe intuition:** 2 users = 1 link, 5 users = 10 links — value rises **faster** than user count
>   because it tracks the number of possible **connections.**
> - **Digital + low marginal cost** lets the loop spin fast, unlike physical networks (roads, rail).

- 🇳🇵 **Local example (walk through it):** **WhatsApp won Nepal** not by being the best-engineered app
  but because **everyone's family, college group, and workplace is already on it** — each new user made
  it **more useful to the rest.** Viber and others faced the reverse: fewer contacts meant less value, so
  users drifted to where the network was. **The positive feedback loop rewarded the platform that got
  ahead first**, not the one with the best features.

> ❌ **Common misconception:** *"The best app always wins."*
> ✅ **Correction:** "In network markets the **best-CONNECTED** app wins, not necessarily the best-built
> one. A technically superior messenger with few of your contacts is **less useful to you** than a
> plainer one where everyone already is — **value lives in the network**, not only the features."

> 🖼️ Visual: `s10_networkloop.png` — a loop diagram: **more users → more value → more users**, labelled
> "positive feedback."

> 🎯 **Exam-ready answer:** "A network effect exists when a product becomes **more valuable as more people
> use it**, creating a **positive feedback loop** (more users → more value → more users). A rough
> intuition from **Metcalfe** is that value rises with the number of **possible connections**, faster than
> the raw user count. Because digital goods scale at **low marginal cost**, the loop can run explosively —
> which is why the **best-connected** platform, not always the best-built one, tends to win."

> 🎙️ Speaker note: ~7 min. Use the loop diagram. The fax/phone example makes "value is in the network"
> concrete before the four types.

**📊 Depth table — Network effect vs viral effect — often confused**

| Question | Network effect | Viral effect |
|---|---|---|
| What happens | Product gets more USEFUL as users join | Content SPREADS fast via sharing |
| Does it add lasting value? | Yes — each user improves the product | Not necessarily — a meme fades |
| Time horizon | Long-term competitive advantage | Often a short-lived spike |
| Example | WhatsApp more useful as friends join | A viral TikTok clip or forwarded joke |
| Can you have one without the other? | Yes — a useful tool few share | Yes — viral content on a weak platform |

*ℹ️ Going viral is not the same as a network effect: virality is fast spread; a network effect is durable added value. Google+ went viral on launch but had no lasting network effect and died.*

#### Concept 2 — The Four Types of Network Effect `[THEORY]` `[~8 min]`

[SLIDE] **Direct · indirect (cross-side) · data · standard**

> **Deliver:** Name the four kinds and how each grows value. **Network effects come in four kinds.**
> - **Direct (same-side):** more users of the **same** type add value — WhatsApp, Facebook, online games.
> - **Indirect (cross-side):** more users on **one** side attract the **other** — Uber/Pathao
>   riders↔drivers, app developers↔users.
> - **Data:** more users → more **data** → a **better product** → more users — Google Maps, TikTok.
> - **Standard/technology:** a **technical standard** grows more valuable as it **dominates** — Fonepay
>   QR, USB-C, GSM, PDF.
>
> Deliver the key point: a platform often has **several at once**, and knowing **which type** tells you
> **how it defends its lead.**

- 🇳🇵 **Local example (walk two of them):** **TikTok** shows the **data** network effect vividly — every
  swipe, watch-time, and replay **trains its algorithm**, so the feed gets more addictive the more you
  (and everyone) use it: a better product that attracts more users who generate more data. **Fonepay**
  shows the **standard** effect: once most Nepali merchants display a Fonepay QR, **every wallet wants to
  work with it** and every user expects it — the standard's **dominance is its value.**

> ❌ **Common misconception:** *"All network effects are the same 'more users = better' idea."*
> ✅ **Correction:** "They differ in **HOW** value grows: same-side (friends), cross-side (the other
> group), data (a smarter product), or a standard (adoption itself). **Knowing the type matters** — a
> data effect is defended by **data**, a standard effect by **ubiquity.**"

> 🎯 **Exam-ready answer:** "Network effects come in four types: **direct/same-side** (more users of the
> same group add value — WhatsApp), **indirect/cross-side** (more users on one side attract the other —
> Pathao riders↔drivers), **data** (usage generates data that makes the product smarter — TikTok, Google
> Maps), and **standard/technology** (a standard grows more valuable as it dominates — Fonepay QR, USB-C).
> A platform often has several at once, and the **type determines how it defends its lead.**"

> 🎙️ Speaker note: ~8 min. Use the comparison table. TikTok is the clearest DATA network effect — every
> swipe trains the feed.

**📊 Depth table — The four types of network effect**

| Type | How value grows | Nepal / global example |
|---|---|---|
| Direct (same-side) | More users of the SAME group add value | WhatsApp, Facebook, online games |
| Indirect (cross-side) | More users on one side attract the other | Pathao riders↔drivers; app stores |
| Data | Usage → data → smarter product → users | TikTok feed; Google Maps traffic |
| Standard / technology | A standard grows more valuable as it dominates | Fonepay QR; USB-C; GSM; PDF |

*ℹ️ Many platforms have several at once: Daraz has indirect (buyers↔sellers) AND data (recommendations) effects. Identifying which type is at work tells you how the platform defends its lead.*

#### Concept 3 — The Limits: Negative Network Effects `[THEORY]` `[~6 min]`

[SLIDE] **More users can HURT — and the loop can reverse**

> **Deliver:** Puncture the "growth is destiny" story. **Network effects are not infinite or always
> positive.** Beyond some point, more users can **REDUCE** value — **congestion** (a video call that lags
> at peak), **spam and low-quality content**, **toxicity**, or **price surges** that anger users. Walk
> them:
> - **Congestion:** too many users strain capacity (peak-time app slowdowns).
> - **Quality dilution:** too many low-quality sellers/posts crowd out the good ones.
> - **Toxicity & noise:** unmoderated growth drives good users away.
> - **The loop can reverse:** users leaving makes a platform less valuable, **accelerating decline** —
>   as with **Google+** and **Clubhouse.**

- 🇳🇵 **Local example (both edges at once):** **Pathao at rush hour shows both edges.** Normally more
  drivers mean **shorter waits** (positive); but when demand spikes, **surge pricing and long waits
  frustrate riders** (negative). A **marketplace flooded with low-quality or scam sellers** becomes harder
  to trust, driving good buyers away. Platforms spend heavily on **moderation, capacity, and quality
  control** precisely to keep the loop positive.

> ❌ **Common misconception:** *"Network effects mean a platform's growth is unstoppable."*
> ✅ **Correction:** "Growth can **dilute quality, congest capacity, or turn toxic** — and the loop can
> **reverse** when users leave (Google+, Clubhouse). Network effects are powerful but must be **managed**;
> they are **not** a guarantee of permanent dominance."

> 🧠 **Memory hook:** *the crowded restaurant* — popular is good until it's so crowded the service
> collapses and regulars leave. That tipping-into-negative is a negative network effect.

> 🎯 **Exam-ready answer:** "Network effects have limits and can turn negative: beyond a point more users
> can reduce value through **congestion** (peak lag), **quality dilution** (too many low-quality
> sellers/posts), **toxicity**, or anger-inducing **surge pricing.** Failure cases like **Google+** and
> **Clubhouse** show the positive feedback loop can **stall or reverse** when users leave. Platforms
> actively manage growth — moderation, capacity, quality control — to keep the effect positive."

> 🎙️ Speaker note: ~6 min. Balance the winner-take-all story: Clubhouse grew fast then collapsed when the
> novelty and network thinned. Growth isn't destiny.

**📊 Depth table — Positive vs negative network effects**

| Situation | Positive network effect | Negative network effect (too many / wrong users) |
|---|---|---|
| Messaging app | More friends → more useful | (few negatives — scales well) |
| Ride-hailing at peak | More drivers → shorter waits | Too many riders → surge pricing, long waits |
| Marketplace | More sellers → more choice | Too many low-quality sellers → hard to trust |
| Social feed | More friends → more relevant | Too many ads/spam → users leave |
| Video calls | More contacts reachable | Peak congestion → lag, dropped calls |

*ℹ️ The same growth that creates value can, unmanaged, destroy it. Platforms invest in moderation, capacity, and quality control precisely to keep the network effect positive.*

#### 🛠 ACTIVITY — "Which effect, and could it reverse?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Identify the network-effect type — then how it could turn negative**

> **Run it:** In pairs (2 min) students pick a platform and **identify which of the 4 network-effect types
> it relies on.** They then **name one way its network effect could turn NEGATIVE.** Take 3–4 answers
> aloud (3 min), **classifying each effect type on the board.** Close: "Strong platforms actively defend
> against the negative side."

> 🎙️ Speaker note: Seeds — TikTok (data; negative = toxic/low-quality flood), Pathao (indirect; negative
> = surge), Daraz (indirect+data; negative = scam sellers), WhatsApp (direct; negative = spam/forwarded
> misinformation).

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** Uber/Pathao's riders-attract-drivers-attract-riders is which type?
a) direct  b) ✅ **indirect / cross-side**  c) data  d) standard
*(Why: value on one side (riders) grows the other side (drivers) — a cross-side (indirect) network effect.)*

**MCQ 2.** Going viral is the same as a network effect:
a) true  b) ✅ **false — viral = fast spread; network effect = lasting added value**  c) only for TikTok  d) only offline
*(Why: a meme spreads (viral) without making the platform more useful; a network effect durably adds value.)*

**Discussion prompt:** *Name a Nepali platform's network-effect type and one way it could turn negative.*

> 🎙️ Speaker note: Drill the four types and the viral-vs-network distinction — both common confusions.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** network effects explain why **one Nepali platform in each category tends to
dominate** — one big wallet, one big messenger, one big marketplace — and why a **better-built challenger
still struggles.** If you launch a platform, **engineering a network effect** (and defending its positive
side against congestion, spam, and toxicity) is the whole game. If you invest or work in one, spotting
whether a real network effect exists tells you whether the lead is defensible.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Network effect** = a product gets more valuable as more use it → **positive feedback loop** (best-connected wins).
2. **Four types:** direct (same-side), indirect (cross-side), data, standard/technology — **often combined.**
3. **Limits:** more users can HURT (congestion, spam, toxicity, surge); the loop **can reverse** — growth must be **managed.**

**Next session (S11):** the economics Unit 1 promised — in a **two-sided market, who actually pays, and who gets it free?**

---
---

# S11 — Two-Sided Pricing: Who Pays, Who's Subsidised ⭐
**Lecture hour 3 of 7 (Unit 2) · 50 minutes · fills the platform ECONOMICS deferred from Unit 1 S1**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"If it's free, how is Google worth trillions?"**

> **Deliver (≈2 min):** List the free things. "**Google Search is free. TikTok is free. Adobe Reader is
> free. Facebook is free.** So **who pays the enormous bills?** Someone always does — and the genius of a
> platform is **charging the RIGHT side while giving the other side away.**"
>
> **Run the question (≈3 min):** Ask "if it's free, how is Google worth trillions?" Take a few answers.
> Land the theme: **this is the real economics behind 'free' — and the economics Unit 1 deferred to
> here.** Agenda: **the money side vs the subsidy side → zero marginal cost & scale → the chicken-and-egg
> launch problem.**

> 🎙️ Speaker note: This is the deferred-economics session (from Unit 1 S1). Make cross-subsidy and
> falling average cost land. Agenda on the board.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — The Money Side and the Subsidy Side `[THEORY]` `[~8 min]`

[SLIDE] **Charge the money side; subsidise the side that attracts it**

> **Deliver:** Give the definition. **In a two-sided market a platform charges one group (the money side)
> and subsidises the other (the subsidy side) — often giving it away free.** This is **cross-subsidy:**
> you subsidise the side that **attracts** the side that pays. Google gives search to users free because
> their **attention** is what advertisers (the money side) pay for. **The free side is bait, not
> charity.** Then teach:
> - **Money side:** the group that pays — advertisers, sellers, creators, premium users.
> - **Subsidy side:** the group kept free/cheap because it **attracts** the money side — users, readers.
> - Which side pays is a **DESIGN choice:** charge where **willingness-to-pay** is highest.
> - Get it **wrong** (charge the side you should subsidise) and the **network never forms.**

- 🇳🇵 **Local example (walk through it):** **Daraz** lets you browse and search for **free**, and charges
  **sellers** a commission. Why that way round? **Buyers are the scarce, valuable side** — sellers will
  happily pay to reach a crowd of ready buyers, but **buyers would leave if charged to shop.**
  Subsidising buyers **builds the crowd**; charging sellers **monetises it.** If Daraz charged buyers an
  entry fee, the crowd — and therefore the sellers — would vanish.

> ❌ **Common misconception:** *"A free service must be losing money or doing charity."*
> ✅ **Correction:** "Free-to-you usually means **you are the bait, not the customer:** the platform
> monetises your **attention or data** via the paying side (advertisers, sellers). Understanding this
> reveals **who the real customer is** — and why 'free' products still answer to someone."

> 🖼️ Visual: `s11_crosssubsidy.png` — two sides with the platform between them: **subsidy side (free,
> attracts) → platform → money side (pays)**, arrows showing the cross-subsidy.

> 🎯 **Exam-ready answer:** "In a two-sided market a platform charges one group (the **money side**) and
> subsidises another (the **subsidy side**), often giving it away free — a **cross-subsidy** where you
> subsidise the side that attracts the paying side. Which side pays is a **deliberate design choice:**
> charge where willingness-to-pay is highest, subsidise where presence is most valuable to the other side.
> Google users are free because **advertisers pay for their attention**; Daraz buyers are free because
> **sellers pay to reach them.**"

> 🎙️ Speaker note: ~8 min. Use the cross-subsidy diagram. Hammer: the free side is **bait** — it is
> monetised **indirectly** through the paying side.

**📊 Depth table — Who's free, who pays — two-sided pricing in practice**

| Platform | Subsidy side (free/cheap) | Money side (pays) | Why this split |
|---|---|---|---|
| Google Search | Users (search free) | Advertisers | Users' attention is what advertisers buy |
| Daraz | Buyers (browse free) | Sellers (commission) | Buyers attract sellers who will pay to reach them |
| Facebook / TikTok | Users (free) | Advertisers | Engagement/data is sold to advertisers |
| Adobe Reader / PDF | Readers (free) | Creators (pay for Acrobat) | Free readers make the paid format worth buying |
| Credit / QR (Visa, Fonepay) | Cardholders/payers | Merchants (fees) | Shoppers attract merchants who pay to accept |
| Newspapers (classic) | Readers (cheap) | Advertisers | Readership is sold to advertisers |

*ℹ️ The pattern: subsidise the side whose presence is most valuable to the other side, and charge the side willing to pay to reach them. 'Free to users' almost always means 'someone else is the customer'.*

#### Concept 2 — Zero Marginal Cost & Economies of Scale `[THEORY]` `[~7 min]`

[SLIDE] **High fixed cost + ~0 marginal cost → average cost falls with scale**

> **Deliver:** Give the cost structure. **Digital platforms have high fixed costs (build the software,
> the network) but a near-zero marginal cost — serving one more user costs almost nothing.** So as users
> grow, the fixed cost is **spread over more people** and the **average cost per user keeps falling.**
> This is why platforms chase scale relentlessly and why a giant can undercut any small rival. Walk it:
> - **Fixed cost:** large, one-time (engineering, infrastructure) — paid whether you have 1 user or 1M.
> - **Marginal cost:** cost of ONE more user — near zero for digital goods (a copy, a login).
> - **Average cost falls with scale:** fixed cost ÷ more users → cheaper per user.
> - **Consequence:** bigger platforms are **cheaper to run per user** — a structural advantage over small
>   rivals. (This is the **mechanism** behind Unit 1's intuitive "scalability" claim.)

- 🇳🇵 **Local example (walk through it):** It cost **eSewa** a great deal to build its platform, banking
  integrations, and security — but processing **your next transaction costs almost nothing.** So the more
  Nepalis use eSewa, the **lower its cost per user** and the more it can spend improving the app. A new
  wallet with few users carries **the same kind of fixed costs spread over far fewer people**, so its
  per-user cost is **higher** — a structural disadvantage before it even competes on features.

> ❌ **Common misconception:** *"Scale just means more customers."*
> ✅ **Correction:** "For digital platforms, scale changes the **ECONOMICS:** because marginal cost is
> near zero, **average cost per user falls as you grow**, so the leader gets **cheaper to run** than
> challengers. Scale is not just more revenue — it is a **widening cost advantage** that helps **tip
> markets** (S13)."

> 🎯 **Exam-ready answer:** "Digital platforms have **high fixed costs** (build the software and network)
> but **near-zero marginal cost** (serving one more user costs almost nothing), so **average cost per user
> falls** as the user base grows — **economies of scale.** This is the mechanism behind Unit 1's
> 'scalability': the largest platform has the **lowest per-user cost**, letting it invest more and undercut
> smaller rivals, which is also a force pushing digital markets toward **concentration.**"

> 🎙️ Speaker note: ~7 min. Contrast with a physical business (each extra unit costs materials). This is
> the mechanism behind Unit 1's "scalability" claim.

**📊 Depth table — Cost structure — traditional (pipe) vs digital platform**

| Cost question | Traditional / physical business | Digital platform |
|---|---|---|
| Cost of one more unit/user | Real & repeated (materials, labour) | Near zero (a copy, a new account) |
| Main cost | Variable (rises with output) | Fixed (build once, up front) |
| Average cost as you grow | Roughly flat or rises | Falls — fixed cost spread thinner |
| Limit to scale | Capacity, materials, geography | Very high — software copies freely |
| Who can undercut whom | Similar-cost rivals compete | The biggest has the lowest per-user cost |

*ℹ️ Near-zero marginal cost is the engine of digital scale — and a driver of monopoly (S13): the largest platform has the lowest cost per user, so it can invest more, charge less, and pull further ahead.*

#### Concept 3 — The Chicken-and-Egg Problem `[THEORY]` `[~7 min]`

[SLIDE] **Neither side comes first — five ways to break the deadlock**

> **Deliver:** Name the launch trap. **Every new platform faces a chicken-and-egg problem: buyers won't
> come without sellers, and sellers won't come without buyers — neither side wants to be first.**
> Platforms solve it with **deliberate strategies.** Walk the five:
> - **Subsidise one side:** pay or manually recruit the harder side first (drivers, sellers).
> - **Seed supply/inventory:** build the initial supply yourself.
> - **Exclusive partners:** sign a few big draws so users have a reason to come.
> - **Freemium / zero commission:** waive fees at launch to remove the barrier.
> - **Incentives / referrals:** reward users for bringing others.
>
> The target of all five is the same: reach **critical mass** (liquidity), after which the **network
> effect (S10) takes over on its own** and subsidies can be dialled back.

- 🇳🇵 **Local example (walk through it):** When **Pathao launched**, riders wouldn't open an app with **no
  nearby drivers**, and drivers wouldn't join with **no riders.** Pathao broke the deadlock by
  **subsidising the supply side** — bonuses and incentives to get enough drivers on the road that waits
  were short — which **drew riders**, whose demand then **drew more drivers.** Once it hit **critical
  mass** in a city, the network effect **sustained itself** and the incentives could shrink.

> ❌ **Common misconception:** *"Build a great app and users will come."*
> ✅ **Correction:** "A platform launches **empty and useless** — the hard part is the **cold start**, not
> the code. Without a deliberate strategy to **seed one side** and reach critical mass, even a superb
> platform **dies waiting** for the other side to show up first."

> 🎯 **Exam-ready answer:** "Every new platform faces a **chicken-and-egg problem:** neither side
> (buyers/sellers, riders/drivers) will join before the other. Platforms solve it deliberately —
> **subsidise one side, seed supply/inventory manually, sign exclusive early partners, waive fees
> (freemium/zero commission), and use incentives/referrals** — all aimed at reaching **critical mass
> (liquidity)**, after which the network effect becomes **self-sustaining** and subsidies can be reduced."

> 🎙️ Speaker note: ~7 min. Tie to liquidity: below critical mass the platform is dead; the launch
> strategies exist to reach it. Pathao subsidising early drivers is the local example.

**📊 Depth table — Solving chicken-and-egg — five launch strategies**

| Strategy | What the platform does | Example |
|---|---|---|
| Subsidise one side | Pay/reward the harder side to join first | Pathao bonuses for early drivers |
| Seed supply manually | Build initial inventory yourself | Amazon stocking its own goods early |
| Exclusive partners | Sign a few big draws for early users | A platform signing a popular brand first |
| Freemium / zero commission | Waive fees to remove the barrier | No seller commission at launch |
| Incentives / referrals | Reward users for bringing others | Sign-up cashback; refer-a-friend credit |

*ℹ️ All five aim at the same target: reach critical mass (liquidity) fast, so the network effect becomes self-sustaining and the subsidies can be dialled back.*

#### 🛠 ACTIVITY — "Design the price" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Choose the free side and the paying side for a new Nepali platform**

> **Run it:** In pairs (3 min) students are launching a new Nepali platform (tutoring, farm produce, home
> services). They **decide which side is FREE and which PAYS — and justify using cross-subsidy.** They
> then **name one chicken-and-egg launch move** they'd make first. Take 3–4 answers aloud (2 min) and
> **check the paying side is the one with willingness-to-pay.**

> 🎙️ Speaker note: Good reasoning — subsidise the scarce/valuable side (e.g. students free, tutors pay a
> cut; or buyers free, farmers pay commission), and **seed the hard side first.** Reward answers that name
> **WHO attracts WHOM.**

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** Google Search is free to users because:
a) it is charity  b) ✅ **users are the subsidy side; advertisers (money side) pay for their attention**  c) it loses money  d) the government funds it
*(Why: cross-subsidy — subsidise the side (users) that attracts the paying side (advertisers).)*

**MCQ 2.** "Near-zero marginal cost" means, as a platform grows, its average cost per user:
a) rises  b) stays flat  c) ✅ **falls (fixed cost spread over more users)**  d) becomes negative
*(Why: high fixed + ~0 marginal cost → the bigger the base, the cheaper per user — economies of scale.)*

**Discussion prompt:** *For a new Nepali platform, which side would you make free and why?*

> 🎙️ Speaker note: This is the deferred-economics session — make sure cross-subsidy and falling average
> cost land.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** this is the **money logic of every 'free' app you use** — and the playbook
you'd need to launch one. Knowing **who the real customer is** (the money side) and **how to beat the
cold start** separates a platform that scales from one that dies empty. It also lets you read the news
critically: when a service is "free," you now know to ask **who is paying, and with what** — attention,
data, or a commission on the other side.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Two-sided pricing:** charge the **money side**, subsidise the side that **attracts** it (cross-subsidy) — **'free' has a payer.**
2. **High fixed + near-zero marginal cost** → average cost per user **falls with scale** → the biggest platform is **cheapest per user.**
3. **Chicken-and-egg:** neither side comes first; solve with **subsidies, seeding, exclusives, freemium, incentives** → critical mass.

**Next session (S12):** once users are in, how platforms **keep** them — **lock-in, switching costs, and the flywheel.**

---
---

# S12 — Lock-In, Switching Costs & the Flywheel
**Lecture hour 4 of 7 (Unit 2) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"You've thought about leaving — and you're still there"**

> **Deliver (≈2 min):** Make it personal. "You've **half-thought about leaving eSewa, or WhatsApp, or
> your bank's app** — for months — and you're **still there.** That's **not laziness; it's engineered.**
> Platforms deliberately **raise the cost of leaving** until staying feels easier than switching."
>
> **Run the question (≈3 min):** Ask who has considered switching a service and didn't — **why not?**
> Take a few answers. Land the theme: **staying is designed, not accidental.** Agenda: **the flywheel
> (designed feedback) → the five switching costs → how platforms engineer lock-in.**

> 🎙️ Speaker note: Draw out that "I couldn't be bothered" is exactly the engineered switching cost at
> work. Agenda on the board.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — The Flywheel: a Designed Feedback Loop `[THEORY]` `[~7 min]`

[SLIDE] **Acquire → activate → engage → retain (and retention feeds acquisition)**

> **Deliver:** Define it. **A flywheel is a deliberately designed positive-feedback loop that a platform
> engineers to grow:** acquire users → **activate** them (first real value) → **engage** them (regular
> use) → **retain** them (lock-in), and retention feeds back into acquisition. The key distinction
> students must own: **a network effect is NATURAL (it arises from users needing each other); a flywheel
> is DESIGNED (the company builds the loop on purpose).** Walk it:
> - **Acquire → Activate → Engage → Retain** — then retention (referrals, reputation) feeds acquisition.
> - **Network effect = natural byproduct** of users; **flywheel = engineered strategy** to spin faster.
> - The loop **compounds** — each turn is cheaper and stronger than the last (Amazon's classic flywheel).
> - Below **liquidity** (supply meets demand fast) the flywheel **won't spin** — it needs critical mass
>   first (S11).

- 🇳🇵 **Local example (walk through it):** **Amazon's flywheel is the classic case:** lower prices attract
  more customers, more customers attract more sellers, more sellers mean more selection and scale, which
  **lowers costs and prices again.** Each turn strengthens the next. **Daraz runs a similar loop in
  Nepal** — more buyers draw more sellers, whose competition and variety draw more buyers. The company
  **designs and tunes** this loop; it does not just hope for it.

> ❌ **Common misconception:** *"A network effect and a flywheel are the same thing."*
> ✅ **Correction:** "A **network effect** is a **natural force** (value rises with users); a **flywheel**
> is the **deliberate business machine** built to harness it (acquire → activate → engage → retain). A
> platform can enjoy a network effect yet **stall** if its flywheel — onboarding, engagement, retention —
> is badly designed."

> 🖼️ Visual: `s12_flywheel.png` — a circular loop: **acquire → activate → engage → retain →** (arrow back
> to acquire), labelled "designed feedback loop."

> 🎯 **Exam-ready answer:** "A flywheel is a **deliberately designed** positive-feedback loop a platform
> engineers to grow: **acquire → activate (first value) → engage (regular use) → retain (lock-in)**, with
> retention feeding back into acquisition. It differs from a **network effect**, which is **natural**
> (arising from users needing each other), whereas a **flywheel is designed.** The loop compounds — each
> turn cheaper and stronger — but needs **critical mass (liquidity)** to spin at all."

> 🎙️ Speaker note: ~7 min. Use the flywheel diagram. The natural-vs-designed contrast is the exam point;
> the flywheel is how firms operationalise the network effect.

**📊 Depth table — Network effect vs flywheel — natural vs designed**

| Question | Network effect | Flywheel |
|---|---|---|
| What is it? | Value rises as more users join | A designed loop that compounds growth |
| Natural or designed? | Natural — emerges from users needing each other | Designed — the company engineers it |
| Focus | The value of the network | The growth process (acquire→retain) |
| Example | WhatsApp more useful with more contacts | Amazon: low price → traffic → sellers → lower price |
| Relationship | The force… | …the machine built to harness the force |

*ℹ️ They work together: the network effect is the physics; the flywheel is the engine a company builds to exploit it. A platform can have a network effect but a poorly-designed flywheel (and stall).*

#### Concept 2 — Switching Costs — the Five Types `[THEORY]` `[~7 min]`

[SLIDE] **Financial · learning · data/asset · network/social · psychological**

> **Deliver:** Define the set. **Switching costs are everything you'd lose or spend to move from one
> platform to another — and they are why you stay put.** There are **five types:**
> - **Financial:** money lost — non-refundable subscriptions, paid content, transfer fees, balances.
> - **Learning/effort:** the time to relearn a new interface and reconfigure everything.
> - **Data/asset loss:** chat history, photos, files, saved preferences you can't take with you.
> - **Network/social loss:** losing your contacts, followers, groups, ratings.
> - **Psychological/habit:** comfort, routine, and simple inertia.
>
> Deliver the key point: **the higher and more numerous these costs, the more locked in you are — and
> platforms deliberately stack several types.**

- 🇳🇵 **Local example (walk through it):** **Leaving eSewa isn't hard technically** — but you'd **re-add
  every bank account, lose your saved billers and payment history, re-learn another app, and give up any
  balance or reward points.** Those are **financial, data, learning, and habit** costs stacked together.
  None is huge alone, but combined they make you **shrug and stay** — which is precisely the platform's
  intent.

> ❌ **Common misconception:** *"I stay with a service because it's the best."*
> ✅ **Correction:** "Often you stay because **LEAVING is costly** — data, contacts, habit, money — **not**
> because the alternative is worse. Recognising **engineered switching costs** helps you (and future
> customers you serve) make **deliberate choices** instead of default ones."

> 🧠 **Memory hook:** *the WhatsApp trap* — leaving means losing your **groups** (network), your **chat
> history** (data), and **relearning** a new app (effort) — three switching costs at once.

> 🎯 **Exam-ready answer:** "Switching costs are everything a user would **lose or spend** to move to
> another platform, and they explain inertia. There are five types: **financial** (subscriptions,
> balances, fees), **learning/effort** (relearning a new tool), **data/asset loss** (history, photos,
> files, preferences), **network/social loss** (contacts, followers, ratings), and
> **psychological/habit.** The higher and more numerous these costs, the stronger the **lock-in** — and
> platforms deliberately **stack** several types."

> 🎙️ Speaker note: ~7 min. Walk through WhatsApp: leaving means losing groups (network), chat history
> (data), and relearning (effort) — three at once.

**📊 Depth table — The five switching costs — Nepal examples & how platforms raise them**

| Switching cost | What you'd lose | Nepal example | How a platform raises it |
|---|---|---|---|
| Financial | Money paid / owed | Daraz wallet balance, vouchers | Prepaid balances, reward points |
| Learning / effort | Time to relearn | Getting used to a new bank app | Deep features that take time to master |
| Data / asset | Saved data & history | eSewa payment history, saved billers | Store your data in-platform, hard to export |
| Network / social | Your connections | WhatsApp groups, contacts | Make your social graph the product |
| Psychological / habit | Comfort & routine | Your default wallet 'muscle memory' | Defaults, streaks, daily nudges |

*ℹ️ Switching costs are usually MORE than money — losing your WhatsApp groups (network) or eSewa history (data) can matter more than any fee. Platforms deliberately stack several types.*

#### Concept 3 — Engineered Lock-In, Walled Gardens & Multi-Homing `[THEORY]` `[~7 min]`

[SLIDE] **Lock-in is engineered; multi-homing is the user's defence**

> **Deliver:** Connect the pieces. **Lock-in is the result when switching costs are high enough that users
> stay.** Platforms **engineer it:** ecosystem bundling (Apple's devices + iCloud + iMessage), proprietary
> formats (WhatsApp backups that won't move to Signal), loyalty programs (Prime, reward points), seamless
> cross-device sync, and exclusive features. A tightly closed ecosystem is a **walled garden.** The
> opposite is **multi-homing** — using several platforms at once — which **low switching costs enable** and
> which **weakens any single platform's grip.** Walk it:
> - **Lock-in tactics:** bundling, proprietary formats/data, loyalty rewards, sync, exclusive features.
> - **Walled garden:** a closed ecosystem, smooth inside, hard to leave (Apple, Meta's apps).
> - **Multi-homing:** users on several platforms at once (a driver on Pathao + InDrive) — weakens lock-in.
> - Platforms **fight multi-homing** with loyalty, exclusives, and integration to keep users
>   **single-homed.**

- 🇳🇵 **Local example (walk through it):** **Nepali ride-share drivers often multi-home** — running
  **Pathao and InDrive together** to catch more rides — because switching (or running both) costs them
  little. That multi-homing **weakens each platform's grip**, so platforms respond with **driver loyalty
  bonuses, exclusive incentives, and integration** (in-app payments, ratings) to make one platform the
  default. **Apple, by contrast, is a walled garden** most users never leave because everything is
  bundled.

> ❌ **Common misconception:** *"Lock-in just means the service is good enough that people stay."*
> ✅ **Correction:** "Lock-in is usually **engineered, not earned** — bundling, proprietary data, loyalty
> points, and exclusives raise the **cost of leaving** regardless of whether a rival is better.
> **Multi-homing** (using several at once) is the user's natural **defence**, which is exactly why
> platforms work to **prevent** it."

> 🎯 **Exam-ready answer:** "Lock-in results when **engineered switching costs** keep users in place:
> platforms use **ecosystem bundling** (Apple), **proprietary formats/data** (WhatsApp backups), **loyalty
> programs** (Prime, vouchers), **cross-device sync**, and **exclusive features.** A tightly closed
> ecosystem is a **walled garden.** The opposite is **multi-homing** — using several platforms at once
> (drivers on Pathao + InDrive) — enabled by low switching costs, which **weakens** any single platform's
> grip; platforms fight it with loyalty, exclusives, and integration."

> 🎙️ Speaker note: ~7 min. Note the tension: users benefit from multi-homing (choice, competition);
> platforms fight it. Nepal: drivers multi-home across Pathao/InDrive.

**📊 Depth table — How platforms engineer lock-in**

| Lock-in tactic | How it works | Example |
|---|---|---|
| Ecosystem bundling | Many services only work well together | Apple: iPhone + iCloud + iMessage |
| Proprietary format / data | Your data won't move elsewhere | WhatsApp backup can't import to Signal |
| Loyalty / rewards | Points & perks you'd forfeit by leaving | Amazon Prime; Daraz vouchers |
| Cross-device sync | Seamless only inside the ecosystem | Google Workspace across devices |
| Exclusive features / content | Unique things unavailable elsewhere | Platform-only shows, filters, integrations |

*ℹ️ Each tactic quietly raises a switching cost. A walled garden stacks them so the inside is frictionless and the exit is painful — the deliberate design behind 'I can't be bothered to switch'.*

#### 🛠 ACTIVITY — "Trapped by design" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Name a service you'd leave but haven't — which costs trap you?**

> **Run it:** Individually (1 min) each student names **a service they'd like to leave but haven't.** In
> pairs (2 min) they **identify which of the 5 switching costs keep them there, and any lock-in tactic
> used.** Take 3–4 answers aloud (2 min) and **tally the most common switching cost.** Close: "Notice how
> much lock-in is **engineered, not accidental.**"

> 🎙️ Speaker note: Seeds — WhatsApp (network + data + habit), bank app (learning + data), Apple (bundling
> walled garden), Daraz (rewards). Reward naming the **specific switching-cost type and the tactic.**

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** The difference between a network effect and a flywheel is:
a) none  b) ✅ **a network effect is natural; a flywheel is a designed growth loop**  c) size  d) only Amazon has flywheels
*(Why: the network effect is the force; the flywheel is the engineered machine that harnesses it.)*

**MCQ 2.** Losing your WhatsApp groups and chat history if you left is which switching cost(s)?
a) financial only  b) ✅ **network/social + data/asset**  c) learning only  d) none
*(Why: groups = network/social loss; chat history = data/asset loss — stacked switching costs.)*

**Discussion prompt:** *Name a service you'd leave but haven't — which switching costs trap you?*

> 🎙️ Speaker note: Nail flywheel-vs-network-effect and the five switching-cost types.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** lock-in decides whether a platform **keeps the users it wins** — and as a
consumer it explains your **own inertia.** As a future builder, designing **(ethical) switching costs** is
how you retain customers; as a regulator, **reducing** them (data portability, interoperability — S14) is
how you **restore competition.** The same mechanism looks like good retention from one seat and unfair
lock-in from another — which is why the next two sessions turn to monopoly and its regulation.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. A **flywheel** is a **DESIGNED** growth loop (acquire→activate→engage→retain); a **network effect** is the **NATURAL** force it harnesses.
2. **Five switching costs** — financial, learning, data/asset, network/social, psychological — **stack** into **lock-in.**
3. Platforms **engineer lock-in** (bundling, formats, loyalty, sync, exclusives) & fight **multi-homing**; **walled gardens** deepen it.

**Next session (S13):** when network effects + scale + lock-in combine — **how digital monopolies form.**

---
---

# S13 — Formation of Monopolies in the Digital Economy
**Lecture hour 5 of 7 (Unit 2) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"The leader doesn't just win — it takes almost all"**

> **Deliver (≈2 min):** State the puzzle. "Once everyone is on the platform, **everyone HAS to be on the
> platform.** In ordinary markets several firms share the pie; in digital markets the leader often takes
> **almost all** of it — 'winner-take-most'. **Google has ~90% of search; WhatsApp is near-universal in
> Nepal.**"
>
> **Run the question (≈3 min):** Contrast a street of many tea shops with search (one giant). "**Why do
> digital markets tip toward one giant** so much more than shops or factories do?" Take a few answers.
> Agenda: **winner-take-most & tipping → the six forces → market types (incl. buyer power) & entry
> barriers.**

> 🎙️ Speaker note: The tea-shops-vs-search contrast frames the session. This is where S10, S11, and S12
> converge. Agenda on the board.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Winner-Take-Most & the Tipping Point `[THEORY]` `[~7 min]`

[SLIDE] **Increasing returns → past a tipping point, users pile onto the leader**

> **Deliver:** Give the definition. **A digital monopoly rarely means 100% control; it means
> 'winner-take-most' — the leader captures the bulk of the market, a small rival survives, and the rest
> fade.** This happens because of **increasing returns:** the bigger a platform gets, the **better and
> cheaper** it becomes, attracting still more users. Past a **tipping point**, one platform becomes
> effectively unstoppable. Walk it:
> - **Winner-take-most:** leader takes the majority; one small competitor lingers; others die.
> - **Increasing returns:** more users → better/cheaper product → even more users (**S10 + S11
>   combined**).
> - **Tipping point:** the moment the market 'tips' to one platform and reversal becomes very hard.
> - **Not every market tips** — where multi-homing is easy and effects are weak, several can coexist.

- 🇳🇵 **Local example (two outcomes, one country):** **Nepal's messaging market tipped** — WhatsApp and
  Viber competed, but as more contacts settled on WhatsApp its value **rose for everyone** until it "won
  most" and Viber faded (high network effects, high switching costs, little reason to multi-home).
  **Ride-hailing has NOT fully tipped** — **Pathao and InDrive coexist** because drivers and riders
  happily multi-home and needs are local. **Same country, different tipping outcomes** — which is exactly
  the nuance to teach.

> ❌ **Common misconception:** *"Every digital market ends in one monopoly."*
> ✅ **Correction:** "Only markets with **strong network effects, high switching costs, and little
> multi-homing** tip to one winner (search, messaging). Where **multi-homing is easy and needs differ**
> (ride-hailing, food delivery), several players persist. **Tipping is a tendency, not a law.**"

> 🖼️ Visual: `s13_tipping.png` — an S-curve: share of one platform rising slowly, then sharply past the
> **tipping point**, flattening near dominance.

> 🎯 **Exam-ready answer:** "A digital monopoly usually means **'winner-take-most'** — the leader captures
> the bulk of the market, a small rival survives, and the rest fade — driven by **increasing returns**
> (more users → a better, cheaper product → more users). Past a **tipping point** one platform becomes
> effectively unstoppable. But **not every market tips:** where network effects are weak, switching costs
> low, and multi-homing easy, several platforms coexist (ride-hailing, food delivery)."

> 🎙️ Speaker note: ~7 min. Use the tipping S-curve. Stress the nuance: markets tip when effects + scale +
> lock-in are strong; otherwise they stay contested.

**📊 Depth table — When a market tips vs stays contested**

| Factor | Tips to one winner | Stays contested (several survive) |
|---|---|---|
| Network effects | Strong (value needs everyone) | Weak or local |
| Switching costs | High (hard to leave) | Low (easy to switch) |
| Multi-homing | Rare (users pick one) | Common (users use several) |
| Differentiation | Little — one 'best' network | High — niches for different needs |
| Example | Search (Google), messaging (WhatsApp) | Food delivery, ride-hailing (often several) |

*ℹ️ Tipping is not inevitable: ride-hailing and food delivery often support several players because multi-homing is easy and needs are local. Knowing when a market tips is a strategic and regulatory question.*

#### Concept 2 — The Six Forces Behind Digital Monopolies `[THEORY]` `[~8 min]`

[SLIDE] **Six reinforcing forces turn a lead into a moat**

> **Deliver:** Name the six and stress that they **reinforce each other.** **Six forces push digital
> markets toward monopoly:** network effects (more users → more value), economies of scale (near-zero
> marginal cost → cheaper per user with size), economies of scope (one infrastructure/dataset serves many
> products), data advantage (more users → more data → better product), low/zero marginal cost, and high
> switching costs. Walk them:
> - **Network effects + data advantage:** users and data both make the product better, attracting more
>   users.
> - **Economies of scale + low marginal cost:** the biggest is cheapest to run per user.
> - **Economies of scope:** reuse one login/dataset/infrastructure across many services (Google, Amazon).
> - **High switching costs (S12):** once ahead, the leader is hard to dislodge — the forces **lock
>   together.**
>
> The key insight: **no single force is decisive — it's their COMBINATION and mutual reinforcement that
> turns a lead into a moat.** This is why digital markets concentrate far more than traditional ones.

- 🇳🇵 **Local example (all six in one firm):** **Google is the six forces in one company:** network
  effects (more searchers + more advertisers), scale (serving billions cheaply), scope (search, maps,
  mail, Android, ads on one infrastructure), a data advantage (every query improves ranking), near-zero
  marginal cost, and switching costs (defaults, integration). **Each force feeds the others**, which is
  why its ~90% search share is so durable — **no single rival can match all six at once.** (A Nepali
  parallel: Fonepay/eSewa combine network effects, scale, and switching costs in payments.)

> ❌ **Common misconception:** *"A digital monopoly wins simply by being the best or cheapest product."*
> ✅ **Correction:** "It wins because **six structural forces compound a lead into a moat** — network
> effects, scale, scope, data, near-zero cost, and switching costs — **not merely product quality.** A
> slightly better rival still **can't overcome all six**, which is why dominance persists."

> 🎯 **Exam-ready answer:** "Six reinforcing forces push digital markets toward monopoly: **network
> effects** (more users → more value), **economies of scale** (near-zero marginal cost → cheaper with
> size), **economies of scope** (one infrastructure/dataset serves many products), **data advantage**
> (more users → more data → better product), **low/zero marginal cost**, and **high switching costs.**
> Their **combination and mutual reinforcement** — not any single one — turns an early lead into a durable
> **moat**, which is why digital markets concentrate far more than traditional ones."

> 🎙️ Speaker note: ~8 min. These are the whole unit converging — S10 (network effects), S11
> (scale/marginal cost), S12 (switching costs) plus scope and data. They reinforce each other.

**📊 Depth table — The six forces — how each pushes toward monopoly**

| Force | How it drives dominance | Example |
|---|---|---|
| Network effects | More users make the product more valuable | WhatsApp, Facebook |
| Economies of scale | Near-zero marginal cost → cheaper with size | Google serving billions of searches |
| Economies of scope | One infrastructure/dataset → many products | Google: search, maps, mail, ads |
| Data advantage | More users → more data → better product | TikTok's feed; Google's ranking |
| Low / zero marginal cost | Serving one more user is ~free | Any software copied infinitely |
| High switching costs | Users can't easily leave | Ecosystem lock-in (S12) |

*ℹ️ No single force is decisive — it's their COMBINATION and mutual reinforcement that turns a lead into a moat. This is why digital markets concentrate far more than traditional ones.*

#### Concept 3 — Market Types & Entry Barriers `[THEORY]` `[~7 min]`

[SLIDE] **Seller power (monopoly…) and buyer power (monopsony) — guarded by entry barriers**

> **Deliver:** Widen the lens to buyer power. **Markets differ by how many sellers — and buyers — hold
> power.** On the **seller side:** monopoly (one seller), oligopoly (a few — Apple & Samsung),
> monopolistic competition (many, differentiated). On the **buyer side** (often overlooked): **monopsony**
> (one dominant buyer — Amazon in some markets), **oligopsony** (a few big buyers — Google/Meta/Amazon
> buying most digital ads). Digital leaders are protected by **high entry barriers:** huge server/talent
> cost, un-replicable data, entrenched habits, ecosystem dependence, and compliance cost. Walk it:
> - Monopoly / oligopoly / monopolistic competition = few→many **SELLERS** with market power.
> - Monopsony / oligopsony = one / a few dominant **BUYERS** with power.
> - **Entry barriers:** server & talent cost, data that can't be copied, user habits, ecosystem lock-in.
> - High barriers mean even **well-funded challengers struggle to enter** — protecting the incumbent.

- 🇳🇵 **Local example (buyer power + barriers):** **Amazon can act as a monopsony:** for many small
  sellers it is the **main route to customers**, so it can dictate fees and terms — **buyer power**, not
  just seller power. And **entry barriers** keep challengers out: a new search engine would need billions
  in servers, decades of ranking data it **cannot copy**, and users who won't change defaults. **In
  Nepal, a new wallet faces the barrier of Fonepay/eSewa's entrenched merchant network** — even a great
  app struggles when every merchant already displays a rival's QR.

> ❌ **Common misconception:** *"Market power only means charging buyers high prices (monopoly)."*
> ✅ **Correction:** "Power also runs the **other way:** a dominant **BUYER** (monopsony/oligopsony)
> squeezes **sellers, suppliers, or creators.** Amazon over small sellers and the ad duopoly over
> publishers are **buyer-power** cases — and **entry barriers** are what let either kind of power persist."

> 🎯 **Exam-ready answer:** "Markets differ by **seller power** — monopoly (one seller), oligopoly (a
> few, e.g. Apple & Samsung), monopolistic competition (many differentiated) — and by **buyer power** —
> **monopsony** (one dominant buyer, e.g. Amazon over some suppliers) and **oligopsony** (a few, e.g.
> Google/Meta/Amazon buying most digital ads). Digital leaders are shielded by **high entry barriers:**
> server/talent cost, un-replicable data, user habits, ecosystem dependence, and compliance cost — which
> is why incumbents persist."

> 🎙️ Speaker note: ~7 min. Monopsony is the fresh idea — Amazon as the dominant BUYER squeezing sellers;
> ad-space bought mostly by Google/Meta. Barriers explain why incumbents stay.

**📊 Depth table — Market types — seller power and buyer power**

| Market type | Definition | Example |
|---|---|---|
| Monopoly | One dominant seller, no real substitute | Google in search; Meta in social |
| Oligopoly | A few sellers dominate | Apple & Samsung (smartphones) |
| Monopolistic competition | Many sellers, differentiated products | Fast food; many small apps |
| Monopsony | One dominant BUYER | Amazon in some e-book/supplier markets |
| Oligopsony | A few dominant buyers | Google/Meta/Amazon buying digital ad space |

*ℹ️ Digital power isn't only about selling: a platform can dominate as the main BUYER (monopsony/oligopsony), squeezing suppliers, sellers, or content creators who have nowhere else to go.*

#### 🛠 ACTIVITY — "Will it tip?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Predict whether a Nepali market tips to one winner or stays contested**

> **Run it:** In pairs (3 min) students pick a Nepali digital market (payments, ride-hailing, e-commerce,
> messaging) and **decide if it will tip to one winner or stay contested** — using network effects,
> switching costs, and multi-homing. They **name which of the six forces is strongest** there. Take 3–4
> answers aloud (2 min) and **compare predictions.**

> 🎙️ Speaker note: Good reasoning — messaging/payments tend to tip (strong effects, high switching, low
> multi-homing); ride-hailing/food stay contested (easy multi-homing, local needs). Reward using the
> tip-vs-contested factors explicitly.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** "Winner-take-most" in digital markets is driven mainly by:
a) advertising  b) ✅ **increasing returns — network effects, scale & lock-in compounding**  c) luck  d) government
*(Why: the more a platform grows, the better/cheaper it gets, attracting more users — increasing returns.)*

**MCQ 2.** Amazon dictating terms to small sellers who depend on it is an example of:
a) monopoly (seller power)  b) ✅ **monopsony (buyer power)**  c) oligopoly  d) competition
*(Why: Amazon is the dominant BUYER/gateway for those sellers — buyer-side market power (monopsony).)*

**Discussion prompt:** *Pick a Nepali digital market — will it tip to one winner or stay contested? Why?*

> 🎙️ Speaker note: Reinforce increasing returns, the six forces, and buyer-side power (monopsony).

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** it explains why **Nepal's digital markets tend to have one dominant player per
category** — and why challengers struggle. Knowing **which markets tip and why** is essential whether
you're **building a challenger** (attack a market that hasn't tipped, or find a niche), **advising an
incumbent** (defend the moat), or **regulating either** (a tipped market may need intervention). The next
session takes the regulator's seat.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Digital monopoly = 'winner-take-most'** via **increasing returns**; past a **tipping point** the leader is hard to beat (but not every market tips).
2. **Six reinforcing forces:** network effects, economies of scale, economies of scope, data advantage, low marginal cost, switching costs.
3. **Market power runs both ways** (monopoly…monopsony); **high entry barriers** (data, habits, ecosystem) protect incumbents.

**Next session (S14):** the flip side — the **risks** of digital monopolies, and the **tools** used to check them.

---
---

# S14 — Monopoly Risks, Regulation & the Counter-Narrative
**Lecture hour 6 of 7 (Unit 2) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"If it's free, where's the harm — and how would you even prove it?"**

> **Deliver (≈2 min):** Complicate the easy view. "A monopoly that gives you **free search and cheap
> next-day delivery** — **where's the harm?** And if the product is **'free'**, how does a regulator even
> **prove you were hurt?**"
>
> **Run the question (≈3 min):** Take a few answers. Land the theme: **digital monopolies pose real
> risks, but they are uniquely hard to regulate — and, as PickMe and ONDC show, not always as permanent
> as they look.** Agenda: **the risks → why regulation is hard + the tools → the counter-narrative
> (monopolies aren't inevitable).**

> 🎙️ Speaker note: Kill the "free = harmless" intuition in the hook — the harm is hidden and long-term.
> Agenda on the board.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — The Risks of Digital Monopolies `[THEORY]` `[~7 min]`

[SLIDE] **'Free to use' does not mean 'no cost to society'**

> **Deliver:** List the harms honestly. **Dominance brings real harms even when prices look low or
> free:** less competition can mean **slower innovation**; concentrated data raises **privacy risk**; the
> platform can **control prices and terms** (Apple's ~30% App Store cut); algorithms can be **biased or
> self-preferencing**; and the incumbent can **copy or acquire rivals** to remove competition (Instagram
> Stories cloning Snapchat; Reels cloning TikTok). Walk them:
> - **Less innovation:** with no serious rival, the incumbent can **coast.**
> - **Data & privacy:** one firm holding vast personal data is a **concentration risk.**
> - **Price/terms control:** gatekeepers set fees and rules others must accept (30% app tax).
> - **Killing competition:** copying features or acquiring threats (**buy-or-bury**).
>
> Deliver the trap: **the benefits are visible and immediate (free, convenient) while the costs are
> hidden and long-term (less innovation, privacy risk, control)** — which is why monopoly harm is so easy
> to underestimate.

- 🇳🇵 **Local example (concrete harms):** **Apple's ~30% cut** on App Store purchases is a monopoly-risk
  case — developers (**including any Nepali app maker**) must accept the fee and rules because there is
  **no other way onto iPhones**: the gatekeeper controls price and terms. **Meta cloning Snapchat's
  Stories and TikTok's Reels** shows the **'copy to kill' risk:** a dominant platform can neutralise a
  smaller innovator's advantage, **deterring the next challenger** — including a would-be Nepali one.

> ❌ **Common misconception:** *"If a service is free or cheap, a monopoly can't be harming me."*
> ✅ **Correction:** "Harm shows up as **less innovation, concentrated data/privacy risk, gatekeeper fees
> passed on to you, and rivals being copied or bought out.** **Consumer welfare is more than today's
> price** — it includes **tomorrow's choices and innovation.**"

> 🎯 **Exam-ready answer:** "Digital monopolies bring real harms even at low or zero prices: **less
> competition** can slow innovation; **concentrated data** raises privacy risk; **gatekeepers control
> prices and terms** (Apple's ~30% App Store cut); algorithms can be **biased or self-preferencing**; and
> incumbents can **copy or acquire rivals** to remove competition (Stories, Reels). The benefits are
> **visible and immediate** while the costs are **hidden and long-term**, so monopoly harm is easily
> underestimated."

> 🎙️ Speaker note: ~7 min. The '30% tax' and 'buy-or-bury' are concrete harms behind "but it's free."
> Consumer welfare isn't only price.

**📊 Depth table — Digital monopolies — the benefits vs the risks**

| Benefit (why users like them) | Risk (the hidden cost) | Consequence if unchecked |
|---|---|---|
| Free or cheap services | Less competition → slower innovation | Users get a frozen, stagnant product |
| Convenient all-in-one ecosystem | Data & privacy concentration | One breach/misuse affects everyone |
| Reliable, well-funded platform | Price/terms control (30% app tax) | Higher costs passed to sellers & users |
| Personalized, 'smart' service | Biased / self-preferencing algorithms | Rivals buried; unfair rankings |
| One place everyone is | Copying or acquiring rivals | Fewer choices; innovation deterred |

*ℹ️ The trap is that the benefits are visible and immediate (free, convenient) while the costs are hidden and long-term (less innovation, privacy risk, control) — which is why monopoly harm is so easy to underestimate.*

#### Concept 2 — Why Regulation Is Hard — and the Tools `[THEORY]` `[~7 min]`

[SLIDE] **'Free' defeats the old test — so regulators attack the mechanism**

> **Deliver:** Explain the difficulty, then the tools. **Digital monopolies are hard to regulate:** many
> products are **'free'**, so the traditional "did prices rise?" test fails; markets **move faster than
> law**; and **data ownership rules are unclear.** Regulators have adapted with **new tools:** **data
> portability** (take your data with you), **interoperability** (platforms must work together), **fines**
> for abuse, and, in extreme cases, **breaking companies up** — seen in the EU's **Digital Markets Act**
> and **GDPR** and US **FTC** cases against Amazon and Google. Walk it:
> - The **'free' problem:** no price rise to point to, yet harm (data, innovation) is real.
> - **Speed & data:** law lags fast markets; who owns/controls data is contested.
> - **Tools:** **data portability + interoperability** lower switching costs and open competition.
> - **Harder tools:** **fines** for anti-competitive behaviour; structural **break-ups** as a last resort.

- 🇳🇵 **Local example (a tool Nepal already uses):** **QR interoperability in Nepal** (from Unit 1) is
  exactly this kind of tool: by requiring that **any wallet can pay any merchant's QR**, **NRB lowered
  switching costs** and stopped any single wallet from **locking up merchants** — competition by design.
  Internationally, the **EU's Digital Markets Act** forces gatekeepers to allow interoperability and
  portability, tackling lock-in **without waiting to prove a price rise** that never happens with 'free'
  products.

> ❌ **Common misconception:** *"You can't regulate a free product — there's no harm to measure."*
> ✅ **Correction:** "Regulators shifted from **'did prices rise?'** to targeting the **MECHANISMS** of
> dominance: **portability and interoperability lower switching costs, fines punish abuse, and break-up is
> a last resort.** Harm to **innovation and data** is addressed **even when the price is zero.**"

> 🎯 **Exam-ready answer:** "Digital monopolies are hard to regulate because many products are **free**
> (defeating price-based tests), markets **move faster than law**, and **data-ownership rules are
> unclear.** Regulators use adapted tools: **data portability** (users take their data to rivals),
> **interoperability** (platforms must work together), **fines** for anti-competitive abuse, **antitrust
> cases**, and structural **break-up** as a last resort — seen in the EU Digital Markets Act, GDPR, and US
> FTC actions. Portability and interoperability directly **lower the switching costs that create
> lock-in.**"

> 🎙️ Speaker note: ~7 min. Data portability & interoperability directly attack the switching costs (S12)
> that create lock-in — regulation targeting the mechanism, not just the outcome.

**📊 Depth table — Tools to regulate digital monopolies**

| Regulatory tool | What it does | Real case |
|---|---|---|
| Data portability | Let users take their data to a rival | GDPR (EU) data-portability right |
| Interoperability | Force platforms to work together | EU Digital Markets Act (messaging, app stores) |
| Fines for abuse | Penalise anti-competitive behaviour | EU fines on Google (search, Android) |
| Antitrust cases | Challenge dominance in court | US FTC vs Amazon; cases vs Google |
| Break-up (last resort) | Split a firm into competing parts | Proposed in some US/EU debates |

*ℹ️ Portability and interoperability are the modern favourites because they lower switching costs (S12) and let competition return WITHOUT breaking the platform up — attacking the lock-in mechanism directly.*

#### Concept 3 — The Counter-Narrative: Monopolies Aren't Inevitable `[THEORY]` `[EXAMPLE]` `[~7 min]`

[SLIDE] **Local relevance, open infrastructure, and shifting needs topple giants**

> **Deliver:** Balance the whole unit. **Dominance is powerful but not permanent, and size is not the only
> way to win.** **PickMe (Sri Lanka) beat Uber locally** by being cheaper, more reliable, and better
> adapted — **relevance over scale.** India's **ONDC, UPI, and Aadhaar** build **open public digital
> infrastructure** that lets small players compete with Amazon/Flipkart. And history is littered with
> **fallen giants:** MySpace, Nokia, Orkut. Walk it:
> - **Local relevance beats size:** PickMe out-served Uber in Sri Lanka by fitting the local market.
> - **Open infrastructure:** India's ONDC/UPI/Aadhaar let many small players **share** network effects.
> - **Giants fall:** MySpace → Facebook, Nokia → smartphones — dominance **decays when needs shift.**
> - **Policy can engineer contestability** (interoperability, open standards) **on purpose.**

- 🇳🇵 **Local example (the Nepali lesson):** **PickMe shows a Nepali lesson too** — a local platform that
  understands **local roads, prices, and payment habits** can beat a global giant that treats every city
  the same. **Pathao and InDrive coexist with no global monopoly** precisely because local relevance
  matters. India's **ONDC and UPI** go further, building **open rails** so many small businesses **share**
  network effects instead of one platform hoarding them — a model **Nepal's own digital-public-
  infrastructure debate is watching.**

> ❌ **Common misconception:** *"Once a digital monopoly forms, it's permanent and unbeatable."*
> ✅ **Correction:** "History says otherwise — **MySpace, Nokia, and Orkut** all fell. **Local relevance**
> (PickMe), **open public infrastructure** (ONDC/UPI), and **shifting user needs** regularly topple or
> contain giants. Dominance is **powerful but contestable**, especially **by design.**"

> 🎯 **Exam-ready answer:** "Digital dominance is powerful but **neither permanent nor the only path** to
> success. **PickMe (Sri Lanka)** beat Uber locally through price, reliability, and local fit — **relevance
> over scale.** India's **ONDC, UPI, and Aadhaar** build **open public digital infrastructure** that lets
> small players **share** network effects against Amazon/Flipkart. **Fallen giants (MySpace, Nokia,
> Orkut)** show dominance decays when needs shift. Local relevance, open standards, and changing needs all
> break monopolies — and **policy can engineer contestability deliberately.**"

> 🎙️ Speaker note: ~7 min. This balances the whole unit's winner-take-all story — a hopeful, South-Asia-
> relevant close. ONDC ties back to regulation-as-design.

**📊 Depth table — 'Inevitable monopoly?' — the counter-cases**

| Case | What happened | Lesson |
|---|---|---|
| PickMe (Sri Lanka) | Beat Uber locally on price, reliability, local fit | Relevance can beat sheer size |
| India ONDC | Open network vs Amazon/Flipkart dominance | Open infrastructure restores competition |
| UPI / Aadhaar (India) | Shared public rails many apps build on | 'Government as platform' spreads network effects |
| MySpace → Facebook | Dominant social network overtaken | Lead-in-hand is not permanent |
| Nokia → smartphones | Market leader missed a platform shift | Dominance decays when user needs shift |

*ℹ️ The winner-take-most tendency (S13) is real but not destiny. Local relevance, open public infrastructure, and shifting needs are the three main ways monopolies are broken — a hopeful counterweight to inevitability.*

#### 🛠 ACTIVITY — "Regulate or leave alone?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Pick a dominant platform — should a regulator act, and with which tool?**

> **Run it:** In pairs (3 min) students pick a dominant platform and decide: **should a regulator act, and
> if so, which tool?** They **name the specific risk** they're addressing and the **tool** (portability,
> interoperability, fine, break-up). Take 3–4 answers aloud (2 min) and **debate whether the harm
> outweighs the convenience.** Close: "The best answers **target a mechanism** (lock-in via portability),
> not just 'break them up'."

> 🎙️ Speaker note: Reward precise pairing of **risk→tool:** lock-in → data portability/interoperability;
> self-preferencing → antitrust; privacy concentration → data rules. Note that heavy-handed rules can also
> reduce useful scale — it's a trade-off.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** Regulating digital monopolies is hard mainly because:
a) they're small  b) ✅ **products are often 'free' (no price rise to prove), markets move fast, data rules unclear**  c) no laws exist  d) users don't care
*(Why: the classic 'did prices rise?' test fails when the product is free, though data/innovation harms are real.)*

**MCQ 2.** Data portability and interoperability work by:
a) raising prices  b) ✅ **lowering switching costs so competition can return**  c) banning platforms  d) adding ads
*(Why: they attack the lock-in mechanism (S12) directly, letting users move and rivals interconnect.)*

**Discussion prompt:** *Pick a dominant platform — should a regulator act, and with which tool?*

> 🎙️ Speaker note: Tie regulation tools back to switching costs (S12) and end on the not-inevitable
> counter-narrative.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** as **citizens** you feel monopoly power in the **fees and choices** you get; as
future **builders and policymakers** you'll decide whether to **exploit, resist, or regulate** it. **QR
interoperability shows Nepal already using these tools** — the debate is **live here, not just abroad.**
Understanding that dominance is contestable (PickMe, ONDC) keeps you from either fatalism ("giants always
win") or naïveté ("markets fix themselves").

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Monopoly risks:** less innovation, data/privacy concentration, gatekeeper price control, biased algorithms, copying/killing rivals — **even when 'free'.**
2. **Regulation is hard** (free products, speed, data); tools: **data portability, interoperability, fines, break-up** (DMA, GDPR, FTC).
3. **Not inevitable:** local relevance (**PickMe**), open infrastructure (**ONDC/UPI**), and shifting needs (**MySpace, Nokia**) break monopolies.

**Next session (S15):** zooming out — how do we **MEASURE** how digital a country is? The **DAI and OECD DGI.**

---
---

# S15 — Measuring Digital Adoption: DAI & the OECD DGI
**Lecture hour 7 of 7 (Unit 2) · 50 minutes · CLOSES UNIT 2**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Estonia runs 99% of government online; in Nepal you queue with photocopies"**

> **Deliver (≈2 min):** Draw the contrast. "**Estonia runs 99% of its government services online;** in
> much of Nepal you still **queue with photocopies and cash.** Everyone says **'go digital'** — but how do
> we actually **MEASURE** how digital a country is, **compare** countries fairly, and see **where Nepal
> truly stands?**"
>
> **Run the question (≈3 min):** Take a few answers. Land the theme: **that's what digital-adoption
> indexes do.** Agenda: **what digital adoption means + the World Bank DAI (3 pillars) → the OECD DGI (6
> dimensions) → Nepal's position.**

> 🎙️ Speaker note: Contrast Estonia's e-government with a Nepali government queue. Stress adoption =
> **usage**, not access. Agenda on the board; flag that this **closes Unit 2.**

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Digital Adoption & the World Bank DAI `[THEORY]` `[~7 min]`

[SLIDE] **Adoption = effective USE, measured across three pillars**

> **Deliver:** Give the definition. **Digital adoption is the effective USE of digital tools in daily
> life, business, and government — not merely their availability.** The **World Bank's Digital Adoption
> Index (DAI)** measures it across **three pillars:** **People** (internet, smartphones, social media,
> digital payments), **Business** (cloud, e-commerce, digital accounting, automation), and **Government**
> (e-services, digital ID, tax filing, open data). It lets countries be **compared** and gaps
> **identified.** Walk it:
> - **Adoption ≠ access:** owning a smartphone isn't adoption; **USING** it to transact is.
> - **Three DAI pillars:** People, Business, Government — each with concrete indicators.
> - Used by the **World Bank, UN, OECD, IMF, ITU** to compare digital readiness across countries.
> - **Caveat:** the DAI is a framework; the **last official World Bank DAI dataset is from 2016** — treat
>   scores as indicative.

- 🇳🇵 **Local example (walk the uneven picture):** **Nepal scores relatively well on the People pillar** —
  high social-media use and fast-growing wallets like **eSewa, Khalti, and Fonepay** — but **lags on
  Business** (few SMEs use cloud accounting) and **Government** (services exist as apps but aren't
  integrated; paperwork still dominates). The DAI makes this **uneven picture visible and comparable**, so
  policymakers can **target the weak pillar** rather than assume "we have phones, so we're digital."

> ❌ **Common misconception:** *"If people own smartphones, the country has high digital adoption."*
> ✅ **Correction:** "Adoption is about **effective USE, not ownership** — and it varies **by pillar.**
> Nepal's **citizens adopt fast** while its **businesses and government lag**, so a single 'we're online'
> claim **hides exactly where the real gaps (and opportunities) are.**"

> 🖼️ Visual: `s15_dai_pillars.png` — three pillars (People / Business / Government) with Nepal's status
> shaded under each (People high, Business low–moderate, Government early-stage).

> 🎯 **Exam-ready answer:** "Digital adoption is the **effective use** of digital tools in daily life,
> business, and government — **not mere availability.** The **World Bank's Digital Adoption Index (DAI)**
> measures it across three pillars — **People** (internet, smartphones, social media, payments),
> **Business** (cloud, e-commerce, digital accounting, automation), and **Government** (e-services, digital
> ID, tax, open data) — enabling cross-country comparison and gap-spotting. **Nepal is strongest on
> People, weaker on Business, and early-stage on Government.**"

> 🎙️ Speaker note: ~7 min. Use the DAI pillar graphic. Stress adoption = usage, not access — a country
> can have phones but low adoption.

**📊 Depth table — The DAI's three pillars — indicators & Nepal's status**

| Pillar | Example indicators | Nepal status | Why |
|---|---|---|---|
| People | Internet, smartphones, social media, payments | Moderate–High | High social/TikTok use; eSewa/Khalti growing; uneven internet quality |
| Business | Cloud, e-commerce, digital accounting, automation | Low–Moderate | Digital accounting rare; e-commerce rising but informal |
| Government | E-services, digital ID, tax filing, open data | Early stage | Nagarik App & online passport exist; systems not integrated |

*ℹ️ Nepal's pattern is common for developing economies: citizens (People) adopt fastest, businesses lag, and government is slowest — the reverse of leaders like Estonia. Adoption is uneven across the three pillars.*

#### Concept 2 — The OECD Digital Government Index (DGI) `[THEORY]` `[~8 min]`

[SLIDE] **Six dimensions of digital-government MATURITY — not just access**

> **Deliver:** Give the definition and attribution. **The OECD Digital Government Index (DGI) measures how
> modern, efficient, and citizen-focused a government's digital services are — going beyond access to
> quality and maturity.** It has **six dimensions:** **user-centricity** (built around people),
> **digital-by-design** (born digital, not paper copied), **data-driven** public sector, **proactiveness**
> (government acts before you ask), **government-as-a-platform** (shared ID/payments/cloud), and
> **open-by-default** (transparent, open data). Walk key ones:
> - **User-centricity:** simple, fast, mobile-friendly services (UAE's one-app government).
> - **Digital-by-design & government-as-a-platform:** shared rails like India's Aadhaar/UPI, Estonia's
>   X-Road.
> - **Proactiveness:** Denmark **auto-sends child benefits** after a birth is registered — no application
>   needed.
> - **Open-by-default:** government data public by default (UK open-data portal, COVID dashboards).
>
> Flag the terminology: **this is the syllabus's "OECD digital-adoption government index."**

- 🇳🇵 **Local example (walk the gap):** **Nepal's online passport and Nagarik App are real progress on
  access** — but on the DGI they'd score **low on 'digital by design' and 'government as a platform':**
  services are often **digital copies of paper processes**, run on **separate systems that don't share one
  identity or payment rail.** **Estonia's X-Road** (all agencies interconnected) and **India's Aadhaar/
  UPI** (shared public rails) are what **higher DGI maturity looks like** — the target Nepal is moving
  toward.

> ❌ **Common misconception:** *"Putting government forms online is digital government."*
> ✅ **Correction:** "That's the **lowest rung.** The DGI's higher bar is **digital-by-design** (rebuilt
> digitally, not paper scanned), **shared platforms** (one ID/payment), **proactiveness**, and
> **openness.** A **PDF of an old form on a website is access, not digital-government maturity.**"

> 🎯 **Exam-ready answer:** "The **OECD Digital Government Index (DGI)** measures how modern, efficient,
> and citizen-focused a government's digital services are — **quality and maturity, beyond access.** Its
> six dimensions are **user-centricity, digital-by-design** (born digital, not paper copied),
> **data-driven** public sector, **proactiveness** (acting before asked), **government-as-a-platform**
> (shared ID/payments/cloud), and **open-by-default** (transparent open data). Leaders (Estonia's X-Road,
> India's Aadhaar/UPI, Denmark's proactive benefits) show what **high maturity looks like.**"

> 🎙️ Speaker note: ~8 min. This is the syllabus's 'OECD digital-adoption government index'. Contrast DGI
> (government maturity/quality) with DAI (broad adoption across society).

**📊 Depth table — The OECD DGI — six dimensions with country examples**

| Dimension | What it means | Country example |
|---|---|---|
| User-centricity | Services built around people, not bureaucracy | UAE: ~90% services on one app |
| Digital by design | Born digital, not paper scanned to PDF | IndiaStack: Aadhaar + eKYC + UPI |
| Data-driven public sector | Use data to decide & predict | Singapore: data-tuned bus frequency |
| Proactiveness | Government acts before you ask | Denmark: auto child benefits after birth |
| Government as a platform | Shared ID, payments, cloud rails | India UPI; Estonia X-Road |
| Open by default | Transparent, public open data | UK open-data portal; gov APIs |

*ℹ️ The DGI measures the QUALITY and maturity of digital government, not just whether services exist. 'Digital by design' vs merely scanning paper forms into PDFs is the distinction Nepal most needs to make.*

#### Concept 3 — DAI vs DGI, and Reading Nepal's Position `[THEORY]` `[~6 min]`

[SLIDE] **DAI = breadth across society; DGI = depth of government**

> **Deliver:** Distinguish the two indexes, then read Nepal. **The two indexes answer different
> questions.** The **DAI** asks "how much does the whole **SOCIETY** (people, business, government) use
> digital tools?" The **DGI** asks, more narrowly and deeply, "how **mature and citizen-focused** is the
> **GOVERNMENT's** digital service?" Read together for Nepal: **society-wide adoption is led by people and
> lagged by government; and government digital maturity is early-stage** — the same message from two
> angles. Walk it:
> - **DAI = breadth** of adoption across society (people + business + government).
> - **DGI = depth/maturity** of one actor — digital government specifically.
> - For Nepal, **both point the same way:** strong citizen uptake, weak government maturity.
> - **Caveat:** treat scores as **indicative** — DAI data is dated (2016) and **indexes simplify
>   reality.**

- 🇳🇵 **Local example (the diagnosis):** Put together, the indexes give Nepal a **clear diagnosis:**
  citizens have **adopted digital fast** (wallets, social media), but **businesses and — most of all —
  government lag**, and what government digital exists is **access-level, not digital-by-design.** That
  weak government/business adoption also **caps the platforms and network effects** from earlier in this
  unit: **fewer businesses online means thinner marketplaces.** The fix (per the DGI) is **shared public
  rails and rebuilt-digital services** — India's UPI/ONDC direction.

> ❌ **Common misconception:** *"A single number tells you how digital a country is."*
> ✅ **Correction:** "No one index captures it: the **DAI shows society-wide breadth**, the **DGI shows
> government depth**, and **both simplify** (and the DAI data is dated). Read **together** they diagnose
> Nepal precisely — **strong citizens, lagging government** — better than any single score."

> 🎯 **Exam-ready answer:** "The **DAI and DGI answer different questions:** the **DAI** measures
> **adoption across the whole society** (people, business, government — **breadth**), while the **DGI**
> measures the **maturity and citizen-focus of digital government** specifically (**depth**). For Nepal
> both point the same way — **strong citizen uptake, lagging business and (especially) government**, with
> government digital still **access-level rather than digital-by-design.** Weak business/government
> adoption also **limits the platforms and network effects** studied earlier in this unit."

> 🎙️ Speaker note: ~6 min. Close the unit by connecting adoption gaps back to the fundamentals: weak
> business/government adoption limits the very network effects and platforms the unit studied.

**📊 Depth table — DAI vs OECD DGI — what each measures**

| Question | World Bank DAI | OECD DGI |
|---|---|---|
| Measures | Adoption across society | Maturity of digital government |
| Scope | People + Business + Government | Government services only |
| Depth | Breadth of usage | Quality & citizen-focus |
| Key question | 'How digital is the country?' | 'How good is digital government?' |
| Nepal read | People strong, business/govt lag | Early stage (access, not by-design) |

*ℹ️ Use them together: the DAI locates WHERE adoption is weak (Nepal: business & government), and the DGI explains HOW to deepen the government side (digital-by-design, shared platforms). Both say Nepal's government is the lagging pillar.*

#### 🛠 ACTIVITY — "Rate Nepal, then fix a pillar" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Rate Nepal on each DAI pillar, then propose a fix for the weakest**

> **Run it:** In pairs (3 min) students **rate Nepal High/Medium/Low on each DAI pillar** (People,
> Business, Government) with a reason. They **pick the weakest pillar and propose one concrete fix**
> (borrow from Estonia or India). Take 3–4 answers aloud (2 min) and **compare ratings.** Close: "The
> **government pillar** is usually rated weakest — link to the DGI's **'digital-by-design'.**"

> 🎙️ Speaker note: Expected — People Medium–High, Business Low–Moderate, Government Early/Low. Good fixes:
> a shared **digital ID + payment rail** (like Aadhaar/UPI), **digital-by-design services** (not scanned
> PDFs), **open data.** Reward concrete, borrowed-best-practice answers.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** The World Bank DAI measures adoption across which three pillars?
a) rich/middle/poor  b) ✅ **People, Business, Government**  c) phones/PCs/servers  d) urban/rural/remote
*(Why: the DAI's three pillars are People, Business, and Government — each with its own indicators.)*

**MCQ 2.** A government service that is a scanned PDF of an old paper form scores LOW on the DGI's:
a) openness  b) ✅ **'digital by design'**  c) fines  d) network effect
*(Why: digital-by-design means rebuilt digitally, not paper copied — a scanned form is access, not maturity.)*

**Discussion prompt:** *Rate Nepal on the three DAI pillars and propose a fix for the weakest.*

> 🎙️ Speaker note: Cement the DAI pillars, the DGI 'digital-by-design' idea, and Nepal's uneven position.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** these indexes are how **governments, the World Bank, and investors judge a
country's digital readiness** — and where Nepal ranks shapes **real policy and investment.** Knowing what
they measure lets you **read those judgements critically** and see **exactly which gap to close** — for
Nepal, the business and government pillars. It also closes the unit's arc: the platforms and network
effects you studied need **businesses and government online** to reach full strength.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Digital adoption = effective USE, not access;** the World Bank **DAI** measures it across **People, Business, Government.**
2. The **OECD DGI** measures **digital-GOVERNMENT maturity** across **6 dimensions** (user-centric, digital-by-design, data-driven, proactive, gov-as-platform, open).
3. **Nepal:** strong on **People**, lagging on **Business & Government** — the same diagnosis from **both** indexes.

**Next unit (Unit 3):** **Digital Markets, Strategy & Innovation** — competition & co-opetition, the layered internet model, and digital business & value-creation models.

---
---

# 📄 UNIT 2 — CHEAT SHEET
*One-page revision reference — what to read the night before the exam.*

| Topic | The compressed essentials |
|---|---|
| **Platforms (S9)** | **Pipe** = firm makes & sells value (one way); **platform** = connects groups, users create value (many ways). **MSP** = 2+ interdependent groups, solves matching. Value via: lower transaction cost, matching, trust, tools, network value. |
| **Network effects (S10)** | Value rises as more users join → **positive feedback** (best-connected wins). **4 types:** direct/same-side, indirect/cross-side, data, standard. **Limits:** congestion, spam, toxicity, surge — can reverse. **Network ≠ viral.** |
| **Two-sided pricing (S11)** | Charge the **money side**, subsidise the side that attracts it (**cross-subsidy**) — 'free' has a payer. **High fixed + ~0 marginal cost** → average cost falls with scale. **Chicken-and-egg:** subsidise/seed/exclusive/freemium/incentives → critical mass. |
| **Lock-in (S12)** | **Flywheel** = designed loop (acquire→activate→engage→retain); **network effect** = natural. **5 switching costs:** financial, learning, data/asset, network/social, psychological. Lock-in engineered via bundling, formats, loyalty, sync, exclusives. **Multi-homing** weakens it. |
| **Monopolies (S13–S14)** | **Winner-take-most** via increasing returns; **tips** past a point (not always). **6 forces:** network effects, scale, scope, data, low marginal cost, switching costs. Market types incl. **monopsony.** **Risks:** less innovation, privacy, price control, copying. **Tools:** portability, interoperability, fines, break-up. **Not inevitable** (PickMe, ONDC, MySpace). |
| **Adoption indexes (S15)** | Adoption = effective **USE.** **World Bank DAI:** 3 pillars (People/Business/Government). **OECD DGI:** 6 dimensions of digital-government maturity (user-centric, digital-by-design, data-driven, proactive, gov-as-platform, open). **Nepal:** strong People, lagging Business & Government. |

---

# 📖 UNIT 2 — GLOSSARY
*Key terms — quick reference.*

| Term | Definition |
|---|---|
| **Pipe (linear) business** | A firm that makes and sells its own value, one-way to customers. |
| **Platform business** | A business that connects groups so they create value for each other. |
| **Multi-sided platform (MSP)** | A model linking 2+ interdependent user groups via matching. |
| **Transaction cost** | The cost of search, negotiation & enforcement in a trade. |
| **Network effect** | A product becomes more valuable as more people use it. |
| **Positive feedback loop** | More users → more value → more users. |
| **Direct (same-side) effect** | Value from more users of the same group (WhatsApp). |
| **Indirect (cross-side) effect** | Value from more users on the other side (riders↔drivers). |
| **Data network effect** | Usage → data → a better product → more users. |
| **Standard/technology effect** | A standard grows more valuable as it dominates (QR, USB-C). |
| **Viral effect** | Fast spread via sharing; not necessarily lasting value. |
| **Negative network effect** | More users REDUCE value (congestion, spam, toxicity). |
| **Two-sided pricing** | Charging one side while subsidising another. |
| **Money side / subsidy side** | The side that pays / the side kept free to attract it. |
| **Cross-subsidy** | Subsidising the side that attracts the paying side. |
| **Marginal cost** | The cost of serving one more user (near-zero for digital). |
| **Economies of scale** | Average cost per user falls as the platform grows. |
| **Economies of scope** | One infrastructure/dataset serves many products. |
| **Chicken-and-egg problem** | Neither side of a platform will join before the other. |
| **Critical mass / liquidity** | Enough participants that the network effect self-sustains. |
| **Flywheel** | A designed positive-feedback loop (acquire→activate→engage→retain). |
| **Switching cost** | What a user loses/spends to move to another platform. |
| **Lock-in** | High switching costs that keep users from leaving. |
| **Walled garden** | A closed ecosystem, smooth inside, hard to leave. |
| **Multi-homing** | Using several competing platforms at once. |
| **Winner-take-most** | The leader captures most of the market; rivals fade. |
| **Tipping point** | When a market tips decisively to one platform. |
| **Data advantage** | More users → more data → a better product. |
| **Monopoly / oligopoly** | One / a few dominant sellers. |
| **Monopsony / oligopsony** | One / a few dominant BUYERS with market power. |
| **Entry barrier** | What makes it hard for a new competitor to enter. |
| **Data portability** | The right to take your data to a rival service. |
| **Interoperability** | Requiring platforms/standards to work together. |
| **Digital adoption** | The effective USE of digital tools (not just access). |
| **World Bank DAI** | Digital Adoption Index — People, Business, Government pillars. |
| **OECD DGI** | Digital Government Index — 6 dimensions of gov digital maturity. |
| **Digital by design** | Services built digitally from the start, not paper copied. |

---

# 📋 UNIT 2 — END-OF-UNIT QUIZ
*Use as a 15–20 min in-class quiz or a take-home review. Answer key at the end.*
*(Note: no genuine IT 250 past-paper was available — these are built from the syllabus, the concept slides, and the in-lecture recap activity.)*

### Section A — Multiple Choice (1 mark each)
1. A platform business differs from a pipe in that:
   a) it is bigger  b) it is more profitable  c) ✅ users create the value for each other  d) it is newer
2. A multi-sided platform connects:
   a) ✅ 2+ interdependent groups (solves matching)  b) many buyers  c) employees  d) one supplier
3. Riders-attract-drivers-attract-riders is a:
   a) direct effect  b) data effect  c) standard effect  d) ✅ indirect / cross-side network effect
4. TikTok's feed improving with use is a:
   a) ✅ data network effect  b) direct effect  c) viral effect  d) standard effect
5. Google is free to users because:
   a) it is charity  b) it loses money  c) ✅ advertisers (money side) pay for their attention  d) governments fund it
6. As a digital platform scales, average cost per user:
   a) rises  b) stays flat  c) turns negative  d) ✅ falls (near-zero marginal cost)
7. Neither side joining first is the:
   a) network effect  b) ✅ chicken-and-egg problem  c) flywheel  d) walled garden
8. A flywheel differs from a network effect in that it is:
   a) ✅ designed, not natural  b) natural  c) only for Amazon  d) about size
9. Losing chat history + groups if you leave = which switching costs:
   a) financial only  b) learning only  c) ✅ data/asset + network/social  d) none
10. "Winner-take-most" is driven by:
    a) advertising  b) ✅ increasing returns (network effects + scale + lock-in)  c) luck  d) government
11. Amazon dictating terms to dependent sellers is:
    a) monopoly (seller power)  b) oligopoly  c) competition  d) ✅ monopsony (buyer power)
12. The OECD DGI measures:
    a) internet speed  b) phone ownership  c) ✅ digital-government maturity (6 dimensions)  d) GDP

### Section B — Short Answer (2 marks each)
13. **Define a multi-sided platform** and name **two** value-creation mechanisms.
14. **Name the four network-effect types**, with **one example each**.
15. Explain **cross-subsidy** with **one example**.
16. **List the six forces** behind digital monopolies.
17. Name the **three DAI pillars** and state what the **OECD DGI** measures.

### Section C — Applied Case (3 marks each)
18. **Choose ONE Nepali platform** (Pathao / eSewa / Daraz / Foodmandu) and analyse it on: **network effect · lock-in · switching cost · monopoly risk.**
19. **Assess Nepal on the DAI's three pillars** (People / Business / Government) and **justify each rating.**

### Section D — Discussion (open-ended)
20. "**Are digital monopolies inevitable?**" Argue using **tipping / winner-take-most** vs the **PickMe / ONDC** counter-cases, and state your own position.

---

### ✅ Answer Key (Section A)
1-c · 2-a · 3-d · 4-a · 5-c · 6-d · 7-b · 8-a · 9-c · 10-b · 11-d · 12-c

> **Sections B–D: grade on key terms.** **Q13** — MSP = connects 2+ interdependent groups to enable
> interactions/solve matching; any two of: reduce transaction costs, efficient matching, trust/reputation,
> tools/infrastructure, network value. **Q14** — direct/same-side (WhatsApp), indirect/cross-side (Pathao
> riders↔drivers), data (TikTok/Google Maps), standard/technology (Fonepay QR/USB-C). **Q15** — cross-
> subsidy = subsidise the side that attracts the paying side; e.g. Google users free (subsidy side),
> advertisers pay (money side); or Daraz buyers free, sellers pay. **Q16** — network effects, economies of
> scale, economies of scope, data advantage, low/zero marginal cost, high switching costs. **Q17** — DAI
> pillars: People, Business, Government; DGI measures digital-government maturity/quality (6 dimensions).
> **Q18** — for the chosen platform, name a real network-effect type, a lock-in / switching-cost example,
> and a monopoly risk (e.g. Pathao: indirect network effect; multi-homing weakens lock-in; switching cost
> = habit/ratings; monopoly risk = surge/data). **Q19** — People Moderate–High (wallets, social media),
> Business Low–Moderate (little cloud accounting/e-commerce), Government Early-stage (apps exist, not
> integrated), each with a reason. **Q20** — reward using the tipping / six-forces argument for
> "inevitable" AND the PickMe/ONDC/MySpace counter-cases for "not inevitable," ending with a reasoned
> position (dominance is a tendency, contestable by local relevance and open infrastructure).

---

## ✅ Unit 2 complete (full lecturer-ready depth)
The deck is built: **IT250_Unit2.pptx** — diagram-rich, self-contained, and PDF-safe, carrying all
**21 §7A depth tables** (comparison, concrete-example, and scaffolding types) across 7 sessions and 21
concepts, plus **6 diagrams** (pipe-vs-platform, cross-side network loop, two-sided cross-subsidy,
flywheel loop, tipping-point curve, DAI three-pillar + Nepal status). This Markdown source carries those
**same 21 depth tables inline** under each concept, so the source of truth and the deck stay in sync.
Regenerated via `build_unit2_pptx.py` (imports `deckkit.py`). Built to **COURSE_MATERIAL_STANDARD.md**,
Nepal-localised throughout. **Next: Unit 3 — Digital Markets, Strategy & Innovation.**
