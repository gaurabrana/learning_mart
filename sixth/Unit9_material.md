# IT 246 — Unit 9: Cyber Law in the Context of Nepal
### Full Lecturer-Ready Session Material (S45–S48) · THE FINAL UNIT OF THE COURSE

**Program:** BIM, 6th Semester · **Unit weight:** 4 lecture hours
**Sessions:** S45–S48 (50 min each) · **Local context:** Nepal / South Asia
**Format:** Markdown — source of truth; the built deck is `IT246_Unit9.pptx` (68 slides), regenerated via `build_unit9_pptx.py` (imports `deckkit.py`), with diagrams from `build_unit9_images.py`.

> **How to read this file.** This is written to **carry a full 50 minutes on its own.** Each
> session has **minute markers** `[~X min]`, the actual **explanation to deliver** (prose, not just
> bullets), **worked examples**, a **timed in-class activity**, and lecturer cue cards in
> `> 🎙️` blocks. `[SLIDE]` marks slide-ready blocks; `🖼️` marks diagram cues. Pace tags:
> `[THEORY] [EXAMPLE] [ACTIVITY] [QUIZ]`. Total per session: **5 + 35 + 5 + 3 + 2 = 50 min.**

> ⚠️ **ACCURACY NOTE — READ BEFORE TEACHING.** All legal specifics below — **section numbers,
> chapter references, penalty amounts, fine/imprisonment figures, and dates** — are **ILLUSTRATIVE
> of the framework and the debate**, drawn from the Electronic Transaction Act 2063 (2008) and
> Electronic Transaction Rules 2064 as commonly taught. **Verify every section number and penalty
> against the current official Nepali text (Nepal Law Commission / Gazette) before delivery**,
> because (a) figures are easy to misquote and (b) Nepal has had repeated proposals to replace/amend
> the ETA (IT Bill / IT Management Bill). Where a figure appears, treat it as **"confirm exact value."**
> Teach the **concept and the debate**, not a memorised number as settled current law. (This mirrors
> the careful framing used in Unit 2, S10.)

---

## Unit 9 — Learning Outcomes
By the end of this unit, students will be able to:
1. Explain what cyber law is, why Nepal needs it, and the legal perspective on cybercrime.
2. Identify the main types of cybercrime recognised under Nepali law and who investigates them.
3. Describe the key provisions of the ETA 2063 — legal recognition of electronic records, digital signatures, offences and penalties.
4. Explain the Electronic Transaction Rules, the role of the Controller and Certifying Authorities, and the goals of Nepal's IT Policy.
5. Explain information-security policy concepts — and synthesise the whole course for exam, lab, and project preparation.

---
---

# S45 — Cyber Law in Nepal · Legal Perspective of Cybercrime
**Lecture hour 1 of 4 (Unit 9) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Which unit, which law?"**

> **Deliver (≈2 min):** Put the students in the seat. "Someone makes a **fake Facebook/TikTok
> account in your name**, posts **defamatory photos**, and **demands money.**"
>
> **Run the question (≈3 min):** "**Which police unit** handles this in Nepal, and under **which
> law** — there was no 'internet' in the old **paper-era Muluki Ain**?" Take a few answers. Most
> students don't know there is a dedicated body. Land the theme: traditional law was **written for
> the physical, paper world** and simply **cannot reach digital acts** — so a country needs a **new
> kind of law**. Agenda: **what cyber law is → why Nepal needs it → target vs tool → the Cyber
> Bureau path.**

> 🎙️ Speaker note: Don't resolve it in the hook — the point is to surface that old law can't reach
> digital acts. Keep all dates "illustrative — verify current law."

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — What Is Cyber Law `[THEORY]` `[~8 min]`

[SLIDE] **Traffic rules for a brand-new road**

> **Deliver:** Give the definition. **Cyber law (cyberspace law) is the body of law governing
> computers, networks, the internet, and electronic transactions.** Its purpose is to **fill the gap
> where traditional law — written for the paper world — cannot reach digital acts**: online
> identity, anonymity, electronic evidence, and cross-border jurisdiction. Explain the two jobs it
> does: it **gives electronic records/signatures legal validity** AND **criminalises computer
> offences**. Global models to name: **India's IT Act 2000** and the **Budapest Convention on
> Cybercrime**. Land Nepal's answer: the **Electronic Transaction Act (ETA) 2063 (2008)** — also
> called the "Cyber Law" — is Nepal's primary cyber law.

- 🌍 **Global example:** India's **IT Act 2000**; the **Budapest Convention** as an international model.
- 🇳🇵 **Local example (walk the timeline):** before roughly **2004**, Nepal had **no statute** for
  electronic records. The **ETA 2063 (2008)** became Nepal's primary cyber law, followed by the
  **Rules (ETR 2064)**, the **Cyber Bureau (2018)**, and **ongoing reform proposals.**

> ❌ **Common misconception:** *"Nepal has a dedicated 'Cyber Crime Act.'"*
> ✅ **Correction:** "Nepal regulates cybercrime **mainly through the ETA 2063** — an e-transactions
> law that **also** criminalises computer offences — plus provisions in **other laws** (defamation,
> the **Criminal Code 2074**, the **Privacy Act 2075**). There is **no** single stand-alone 'Cyber
> Crime Act.'"

> 🍿 **Fun analogy:** "Cyber law is **traffic law for a brand-new kind of road** — the cars (data)
> move fast and cross borders, so you need **new rules and a new traffic police** (the Cyber Bureau)."

> 🖼️ Visual: a **timeline** — no-law era → ETA 2063 → ETR 2064 → Cyber Bureau 2018 → reform proposals.

> 🎙️ Speaker note: Land that old law can't reach digital acts, so a new law was needed. Dates are
> "illustrative — verify."

**📊 Depth table — Why old (paper-world) law can't reach digital acts**

| Dimension | Traditional (paper-world) law | Why it fails online → cyber law's fix |
|---|---|---|
| Identity | Assumes a known, physical person | Fake profiles & anonymity → rules for electronic identity |
| Evidence | Paper documents, wet-ink signatures | Data, logs, e-records → legal recognition of e-evidence |
| Location / jurisdiction | A crime happens in one place | Acts cross borders instantly → cross-border provisions |
| The record | Physical, hard to copy | Digital, copied infinitely → integrity & signature rules |
| The act | Named in the statute (theft, forgery) | 'Hacking', 'source-code damage' didn't exist → new offences |
| Speed & scale | One act, limited reach | One post reaches millions → new harms to regulate |

*ℹ️ Cyber law exists precisely because paper-era law assumed a physical person, place, and record — none of which hold online. ⚠️ Verify current legal specifics against the official text.*


#### Concept 2 — Why Nepal Needs Cyber Law `[THEORY]` `[~9 min]`

[SLIDE] **From convenience to legal backbone**

> **Deliver:** Explain the driver. **Nepal needs cyber law because daily life has gone digital** —
> **e-banking, e-commerce, e-governance, and social media.** Two jobs follow: (1) **give electronic
> records and digital signatures legal validity** so they can be **trusted and enforced**, and (2)
> **punish digital crime** that old law could not name. Walk through the systems students use every
> day — **eSewa/Khalti, mobile banking, online PAN, the Nagarik App, Daraz** — and show that each
> **needs a law** that makes a digital signature/record **legally binding.**

- 🇳🇵 **Local example:** the rise of **mobile banking, eSewa/Khalti wallets, and online government
  services** (online PAN, Nagarik App) — **all** need a law that makes a digital signature/record
  **legally binding.**
- 🇳🇵 **Mini case (work it, ≈2 min):** a **contract signed and emailed as a PDF** — is it
  **enforceable** in a Nepali court? Draw out the **ETA answer**: **electronic records can have legal
  recognition**, so yes — that is exactly the gap the ETA fills.

> ❌ **Misconception:** *"Going digital is just about convenience/technology, not law."*
> ✅ **Correction:** "Every digital transaction needs a **legal backbone.** Without a law giving
> e-records and e-signatures validity, an **online contract or payment can't be trusted or
> enforced**, and a **hacker or fraudster breaks no named offence.** Law is what makes 'digital'
> **trustworthy.**"

> 🎙️ Speaker note: Anchor on services students use daily. The recurring lesson: no cyber law = a
> digital signature is "just a picture" and a hacker breaks no named law.

**📊 Depth table — Digital services in Nepal — what each needs from cyber law**

| Digital service (Nepal) | What it needs from cyber law | Consequence if there were NO law |
|---|---|---|
| eSewa / Khalti wallet payment | A digital transaction that is legally binding | A disputed payment has no legal standing |
| Mobile / internet banking transfer | Electronic records accepted as proof | Bank & customer can't prove what happened |
| Online PAN / Nagarik App e-service | Digitally signed records that count in law | Citizens still forced to use paper & queues |
| Emailed & e-signed business contract | Recognition of e-signatures = enforceable | 'It was only an email' — unenforceable deal |
| Daraz / online purchase | Consumer & transaction rules online | No remedy for online fraud or non-delivery |
| Fake profile impersonating you | A named offence + a body to investigate | Impersonation & harassment go unpunished |

*ℹ️ Every one of these services in Nepal rests on a law that makes digital records/signatures valid AND punishes digital crime — that is exactly why the ETA was enacted.*


#### Concept 3 — Cybercrime: Computer as Target vs Tool `[THEORY]` `[~9 min]`

[SLIDE] **Target = victim; Tool = weapon**

> **Deliver:** Define it. **A cybercrime is an offence in which a computer or network is either the
> TARGET (attacked) or the TOOL (used to commit the crime).** This split is the **cleanest way to
> classify** the offences Nepali law recognises:
> - **TARGET crimes** — the computer is the **victim**: **unauthorised access/hacking, damage to
>   source code, data theft, denial-of-service.**
> - **TOOL crimes** — the computer is the **weapon against a person**: **online fraud,
>   cyber-defamation, harassment/cyberbullying, fake profiles/identity theft.**
>
> Nepal recognises **both**, mainly under the **ETA** plus the **Criminal Code 2074** and **Privacy
> Act 2075.** Land the practical fact: **fake social-media accounts and cyber-defamation are the
> single largest category** the **Nepal Police Cyber Bureau** handles.

- 🇳🇵 **Local example:** **fake social-media accounts and "cyber defamation" cases** are the single
  largest category handled by the **Nepal Police Cyber Bureau** (established **2018**, Bhotahiti,
  Kathmandu).
- 🇳🇵 **Mini case (work it):** a **student edits a friend's photo and posts it to humiliate them** —
  **which type** of cybercrime, and **which body** investigates? (A **tool** crime; the **Cyber
  Bureau**.)

> ❌ **Misconception:** *"Cybercrime just means hacking."*
> ✅ **Correction:** "Hacking is only the **TARGET** half. **Most real Nepali cases are TOOL crimes**
> — fraud, fake profiles, defamation, harassment — where the computer is the **weapon**, not the
> victim. Classifying an incident as **target vs tool** is the first step to naming the right offence."

> 🖼️ Visual: a **target-vs-tool grid** — hacking/data theft on one side, fraud/defamation on the other.

> 🎙️ Speaker note: The target/tool split is the backbone of this session. Keep flagging that the
> defamation examples carry a **free-speech debate** (developed in S46).

**📊 Depth table — Cybercrimes recognised in Nepal — target or tool, and the response**

| Cybercrime (Nepal example) | Target or tool? | Typical legal response / consequence |
|---|---|---|
| Unauthorised access / hacking a server | Target | ETA computer-offence; investigated by Cyber Bureau |
| Deleting or altering computer source code | Target | ETA offence — damage to computer source code |
| Stealing a customer database (data breach) | Target | ETA + Privacy Act 2075; breach of confidentiality |
| Online payment / wallet fraud | Tool | Fraud offence; Cyber Bureau traces the money trail |
| Fake profile impersonating a person | Tool | Impersonation/defamation complaint under the ETA |
| Defamatory or obscene post targeting someone | Tool | ETA e-publication offence — but free-speech debate (S46) |

*ℹ️ If the computer is the victim it's a TARGET crime; if it's the weapon against a person, a TOOL crime. ⚠️ Verify current legal specifics against the official text.*


#### Concept 4 — Reporting Cybercrime · The Cyber Bureau Path `[THEORY]` `[~8 min]`

[SLIDE] **Evidence first, then the Cyber Bureau**

> **Deliver:** Make it practical. **When you are impersonated, harassed, hacked, or defrauded online
> in Nepal, there is a defined path:** preserve evidence → file a complaint with the **Nepal Police
> Cyber Bureau** (or local police) → investigation → prosecution under the **ETA** through the
> **courts / IT Tribunal.** Walk the steps:
> - **Step 1 — preserve EVIDENCE:** screenshots, URLs, account names, dates. **Do not** panic-delete.
> - **Step 2 — file the complaint:** the **Cyber Bureau (Bhotahiti, Kathmandu)** or your local police.
> - **Step 3 — investigation:** the Bureau **traces accounts, IPs, and money trails.**
> - **Step 4 — prosecution:** the case proceeds under the **ETA** through the **courts / IT Tribunal.**
>
> Land it: **knowing this path is practical citizenship.**

- 🇳🇵 **Local example:** the **Cyber Bureau** is the go-to body; for many towns the **local police**
  are the first point of contact, who then coordinate with the Bureau.
- 🇳🇵 **Mini case:** a friend finds a **fake TikTok account** in their name — the right move is
  **screenshot everything first**, then **report**; the wrong move is to **angrily delete** and tip
  off the offender.

> ❌ **Misconception:** *"Nothing can be done about online abuse in Nepal / I should handle it myself."*
> ✅ **Correction:** "There **is** a channel (the Cyber Bureau) and a **law** (the ETA). The mistake
> is **destroying evidence** or **retaliating.** Preserve proof, don't engage the offender, and
> report — vigilante **'hacking back' is itself an offence.**"

> 🖼️ Visual: the **complaint/enforcement flow** — incident → evidence → complaint → investigation →
> prosecution.

> 🎙️ Speaker note: Emphasise **evidence-first.** Venue/procedure specifics are illustrative — tell
> students to **verify the current reporting channel and law.**

**📊 Depth table — What to do — real incidents and the reporting response**

| Incident (Nepal) | What YOU should do first | Where it goes / outcome |
|---|---|---|
| Someone opens a fake account in your name | Screenshot the profile, URL, and posts | Complaint to Cyber Bureau → impersonation case |
| You are defrauded in an online payment | Save transaction IDs, chats, receipts | Cyber Bureau traces the money trail |
| A private photo is shared to harass you | Preserve evidence; do NOT retaliate | Harassment complaint under the ETA |
| Your email/social account is hacked | Record the breach details & recover access | Unauthorised-access (target) offence |
| A defamatory post targets you | Keep the post/URL before it's deleted | Complaint filed — but note the free-speech debate |
| A business database is breached | Log the breach; notify affected people | ETA + Privacy Act 2075 investigation |

*ℹ️ The single biggest practical mistake is destroying the evidence. Preserve it, then report to the Cyber Bureau. ⚠️ Verify current specifics.*

#### 🛠 ACTIVITY — "Which body, which law?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Classify an online-harm scenario**

> **Run it:** In pairs (2 min), each pair picks **one online-harm scenario** (fake profile, hacked
> account, online fraud, defamatory post). They decide: **target or tool?** **who investigates?**
> and their **evidence-first first step.** Take **3–4 answers aloud** (3 min) and classify each on
> the **target/tool grid.** Seeds: **fake TikTok/Facebook account** (tool); a **hacked email**
> (target); **wallet fraud** (tool); a **defamatory comment** (tool — flag the free-speech debate).
> Close: "Nearly all everyday Nepali cases are **TOOL crimes** handled by the **Cyber Bureau** under
> the **ETA.**"

> 🎙️ Speaker note: Reward **evidence-first** thinking and correct target/tool classification.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** Nepal's PRIMARY cyber law is:
a) a dedicated Cyber Crime Act b) ✅ **the Electronic Transaction Act (ETA) 2063** c) the Muluki Ain d) the IT Policy

**MCQ 2.** A crime where the computer is the TOOL (not the target) is best illustrated by:
a) hacking a server b) a DoS attack c) ✅ **online fraud / cyber-defamation** d) source-code damage

**Discussion prompt:** *Give one concrete reason old Nepali law couldn't handle cybercrime — identity, evidence, or jurisdiction.*

> 🎙️ Speaker note: Draw out the target/tool split and that the **ETA** — not a stand-alone "Cyber
> Crime Act" — is the primary law.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** if you are ever **impersonated, harassed, or defrauded online in Nepal**,
you now know the **channel** (Cyber Bureau) and the **law** (ETA) — and that **preserving evidence,
not retaliating**, is the right first move. That is **practical citizenship**, not an abstraction.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Cyber law governs the digital world** where paper-era law (identity, evidence, jurisdiction) **cannot reach.**
2. **Nepal's main cyber law is the ETA 2063** — it validates e-records/signatures AND criminalises computer offences.
3. **Cybercrime = computer as target or tool**; report via the **Cyber Bureau** (est. 2018), **evidence first.**

**Next session (S46):** inside the ETA 2063 — its two halves, digital signatures, and the debated offences chapter.

---
---

# S46 — Electronic Transaction Act (ETA) 2063
**Lecture hour 2 of 4 (Unit 9) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Same law: enable and punish"**

> **Deliver (≈2 min):** Pose the paired question. "**What turns a typed-and-emailed agreement into
> something a Nepali court will enforce** — and **what turns a curious 'let me just try this login'
> into a crime with jail time?**"
>
> **Run it (≈3 min):** Reveal — "**The same law: the ETA 2063.**" This is the **heart of Nepal's
> cyber law.** Agenda: **what the ETA is (two halves) → e-records & digital signatures → offences &
> penalties (with the free-speech debate).** Remind the class up front that **all figures are
> 'illustrative — verify current law.'**

> 🎙️ Speaker note: Set the "two halves" frame in the hook — most students think the ETA is only
> about crime. Keep all section numbers/penalties as "illustrative — verify."

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — What the ETA 2063 Is & Its Purpose `[THEORY]` `[~11 min]`

[SLIDE] **A two-sided coin — enable AND punish**

> **Deliver:** Define it. **The Electronic Transaction Act 2063 (2008 AD) is Nepal's primary cyber
> law.** It has **TWO halves**: most of it **ENABLES the digital economy** (legal recognition of
> electronic records and digital signatures, e-commerce, e-governance); **one chapter PUNISHES**
> computer-related offences. It is **organised in chapters** — from e-records and digital signatures,
> to dispatch/receipt, certificates, the **Controller & Certifying Authorities**, network
> service-provider liability, **offences & penalties**, and the **IT Tribunal.** *(Confirm the exact
> chapter/section structure against the official text.)* In design it **mirrors the UNCITRAL Model
> Law on E-Commerce** and **India's IT Act.**

- 🌍 **Global example:** the ETA's design mirrors the **UNCITRAL Model Law** and **India's IT Act.**
- 🇳🇵 **Local example:** the ETA is **why eSewa payments, bank e-statements, and digitally signed
  government forms carry legal weight** — the "enable" half; and it **names hacking and illegal
  e-publication as offences** — the "punish" half.

> ❌ **Common misconception:** *"The ETA is only about cybercrime / punishment."*
> ✅ **Correction:** "**Most of the Act is about ENABLING e-commerce and e-governance** — giving
> electronic records and signatures **legal validity.** The **offences-and-penalties chapter is only
> one part.** Reading the ETA as a pure 'crime law' misses its main purpose."

> 🖼️ Visual: the **ETA "two halves"** diagram — ENABLE (most of the Act) | PUNISH (one chapter).

> 🎙️ Speaker note: Confirm chapter/section structure before delivery. Land the misconception fix hard.

**📊 Depth table — The ETA's two halves — what each part actually does**

| Provision area (illustrative) | ENABLE or PUNISH? | What it does in practice (Nepal) |
|---|---|---|
| Legal recognition of electronic records | Enable | An e-record can count as evidence like paper |
| Validity of digital signatures | Enable | A digitally signed doc is legally binding |
| Dispatch & receipt of e-records | Enable | Fixes when/where an e-message legally 'arrives' |
| Digital-signature certificates, Controller & CAs | Enable | Sets up the PKI trust system (S47) |
| Unauthorised access / source-code damage | Punish | Named computer offences with penalties |
| Illegal / obscene electronic publication | Punish | The debated offences (esp. Section ~47) — see C3 |

*ℹ️ Most of the ETA ENABLES the digital economy; the offences chapter is one part. Provision areas are illustrative of the structure. ⚠️ Verify against the official text.*


#### Concept 2 — Electronic Records & Digital Signatures `[THEORY]` `[~12 min]`

[SLIDE] **Private key signs, public key verifies**

> **Deliver:** Give the definition. **The ETA gives an electronic record and a digital signature the
> same legal validity as paper and a handwritten signature.** Then teach the mechanism: a **digital
> signature uses asymmetric (public/private key) cryptography** — the signer **signs with a PRIVATE
> key**, and anyone can **verify with the matching PUBLIC key.** The three functions students must
> memorise: **authentication** (WHO signed), **integrity** (NOT altered), and **non-repudiation**
> (can't deny it later). In Nepal these are issued under a **PKI framework** for banking and
> government use (developed in S47).

- 🇳🇵 **Local example:** **digital signatures issued under Nepal's PKI framework** for secure
  government/banking transactions; government e-services accepting **digitally signed documents.**
- 🇳🇵 **Mini case (work it, ≈2 min):** a **vendor denies sending a purchase-order email** — how does
  a digital signature establish **non-repudiation?** Draw it out: **only their private key could have
  produced that signature**, so they cannot credibly deny it.

> ❌ **Misconception:** *"A scanned image of my signature = a digital signature."*
> ✅ **Correction:** "A scanned signature is **just a picture** — anyone can copy-paste it and it
> **proves nothing.** A **true digital signature is cryptographic**: it **binds a specific signer to
> a specific unaltered document** and cannot be forged or reused, which is what gives it **legal
> weight** under the ETA."

> 🍿 **Fun analogy:** "A digital signature is like a **wax seal that also fingerprints the message** —
> **change one word and the seal breaks.**"

> 🖼️ Visual: the **digital-signature flow** — private key signs → public key verifies → authentication,
> integrity, non-repudiation.

> 🎙️ Speaker note: Hammer the three properties. Use the purchase-order case for non-repudiation.

**📊 Depth table — Paper world vs electronic equivalent — and the property it gives**

| Paper-world thing | Electronic equivalent (ETA) | Security property it provides |
|---|---|---|
| Handwritten signature | Digital signature (private key) | Authentication — proves who signed |
| Sealed, unaltered document | Hash-protected signed record | Integrity — proves it was not changed |
| 'I never signed that' denial fails | Only your private key could sign | Non-repudiation — signer can't deny it |
| Notarised / certified copy | Digital-signature certificate (from a CA) | Trust — a licensed CA vouches for identity |
| Posting a letter (proof of sending) | Dispatch/receipt rules for e-records | Certainty of when a message legally 'arrived' |
| Paper contract in a court file | Electronic record admitted as evidence | Legal recognition — e-record counts in law |

*ℹ️ A digital signature does what a wet-ink signature does — and more (integrity + non-repudiation via cryptography). ⚠️ Verify legal specifics.*


#### Concept 3 — Offences & Penalties — and the Free-Speech Debate `[THEORY]` `[EXAMPLE]` `[~12 min]`

[SLIDE] **The debated chapter — protection vs free speech**

> **Deliver:** Define the scope. **The ETA's offences chapter criminalises** acts such as
> **unauthorised access ('hacking'), damage to computer source code, illegal/obscene/defamatory
> electronic publication, breach of confidentiality/privacy, and computer fraud and forgery.**
> Penalties are **commonly cited** as **fines up to about Rs. 200,000 and/or imprisonment up to about
> 5 years** for several core offences. **⚠️ All figures are ILLUSTRATIVE — verify the exact section
> numbers and amounts; they are frequently misquoted.** Then deliver the debate carefully (mirroring
> Unit 2, S10): the much-cited **"Section ~47"** on illegal electronic publication has been the
> **most-applied** and the **most-criticised** provision — **present both sides.**

- 🇳🇵 **Local example (both sides):** individuals in Nepal have been **arrested over Facebook/TikTok
  posts or comments** under the ETA's electronic-publication offence. **Supporters** argue it **curbs
  genuine online harm** (defamation, obscenity, fraud); **critics** argue the **wording is vague and
  over-broad** and has been used to **silence legitimate criticism** — a core reason behind
  reform/replacement proposals.
- 🇳🇵 **Mini case (real-context):** discuss a case where someone is arrested for a comment — hold the
  **tension between curbing online harm and protecting free expression.**

> ❌ **Misconception:** *"The ETA clearly and precisely defines online defamation and obscenity."*
> ✅ **Correction:** "Critics argue **'Section ~47' is vague and over-broad**, which is exactly why it
> is **contested** and why **reform is proposed.** Treat the specific **section number and penalty as
> 'illustrative — verify'**; teach the **CONCEPT and the debate**, not a memorised figure as **settled
> current law.**"

> 🍿 **Fun analogy:** "A digital signature is a **wax seal** — but this **offences chapter is the
> police at the other end of the same road**: the **same law** that makes your e-signature binding can
> make a **careless post a criminal matter.**"

> 🖼️ Visual: an **offence → provision → penalty** table (the depth table below), each row marked
> "verify."

> 🎙️ Speaker note: **Present BOTH sides** (protection vs free-speech chill). State section
> numbers/penalties as **"illustrative — verify current law,"** never as settled fact. This is the
> single most sensitive slide in the unit.

**📊 Depth table — ETA offences — provision, illustrative penalty, and consequence**

| Offence (Nepal) | Provision (illustrative) | Illustrative penalty → consequence |
|---|---|---|
| Unauthorised access / hacking | ETA computer-offence section | ~Fine and/or jail → criminal record |
| Damage / alteration of source code | ETA source-code section | ~Fine and/or imprisonment → liability for damage |
| Illegal / obscene / defamatory e-publication | Section ~47 (most-cited) | ~Up to Rs. 200,000 and/or ~5 yrs → the debated one |
| Breach of confidentiality / privacy | ETA + Privacy Act 2075 | ~Fine and/or jail → data-protection liability |
| Computer fraud & forgery | ETA fraud/forgery section | ~Fine and/or jail → restitution + record |
| False statement to obtain a certificate | ETA certificate section | ~Penalty → certificate void, prosecution |

*ℹ️ ⚠️ Section numbers & penalty figures are ILLUSTRATIVE of the framework, frequently misquoted. Verify against the current official Nepali text before relying on them.*

#### 🛠 ACTIVITY — "Protection or over-reach?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Argue both sides of the e-publication offence**

> **Run it:** In pairs (2 min): **should posting a defamatory comment online be treated more
> seriously than saying it in person?** Argue **using the ETA.** Each pair lists **one reason the
> e-publication offence PROTECTS people**, and **one reason it risks free speech.** Take **3–4
> answers aloud** (3 min); keep **both sides on the board.** Close: "The **honest position holds BOTH
> truths** — real online harm is real, and vague law can chill speech."

> 🎙️ Speaker note: Reward both-sides reasoning (Unit 2 S10 style). Remind students that specific
> section numbers/penalties are **illustrative** — the **debate and concept** matter more than a
> memorised figure. **Verify current law.**

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** A digital signature primarily provides authentication, integrity, and:
a) encryption speed b) ✅ **non-repudiation** c) anonymity d) lower cost

**MCQ 2.** The most frequently applied and criticised ETA provision (often used for social-media posts) is:
a) the digital-signature section b) ✅ **the electronic-publication offence ('Section ~47' — verify)** c) the Controller section d) the IT Tribunal

**Discussion prompt:** *Should an online defamatory comment be treated more seriously than the same words in person? Argue via the ETA.*

> 🎙️ Speaker note: Reinforce non-repudiation and the **two-sided** free-speech debate. Section
> numbers are illustrative — verify.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** every time you **e-sign a document, use mobile banking, or accept online
T&Cs** in Nepal, the **ETA makes that legally binding** — and the **same law can make a careless post
a criminal matter.** Understanding **both halves** is understanding your own **digital rights and
risks.**

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **The ETA 2063 has two halves:** it **ENABLES** the digital economy AND **PUNISHES** computer offences.
2. **Digital signatures give authentication, integrity, and non-repudiation** — legal validity for e-records.
3. **The offences chapter** (esp. the debated **"Section ~47"**) carries **fines + jail** and raises a **free-speech tension** (verify specifics).

**Next session (S47):** the **Rules** that operationalise the Act (ETR), the **Controller & CAs**, and Nepal's **IT Policy.**

---
---

# S47 — Electronic Transaction Rules · Controller & CAs · IT Policy
**Lecture hour 3 of 4 (Unit 9) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Who issues them, who checks them, what's the plan?"**

> **Deliver (≈2 min):** Set up the gap. "An **Act** says '**digital signatures are legal**' — but
> **WHO actually issues them, WHO checks the issuer is trustworthy, and WHAT national plan pushes
> Nepal toward a digital economy?**"
>
> **Run it (≈3 min):** Reveal — "That's the **Rules, the Controller, and the Policy** — the move
> **from law on paper to a working system.**" Agenda: **the ETR (procedures) → the Controller & CAs
> (PKI) → the IT Policy (national goals).** Note: **confirm rule numbers/policy version before
> delivery.**

> 🎙️ Speaker note: The theme is **law on paper → working machinery.** Confirm ETR year/rule numbers
> and the current IT Policy version before teaching specifics.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Electronic Transaction Rules (ETR) `[THEORY]` `[~11 min]`

[SLIDE] **The operating manual for the Act**

> **Deliver:** Define it. **The Electronic Transaction Rules (commonly cited as ETR 2064 BS) are
> subordinate legislation made under the ETA that spell out the PROCEDURES** — how the Act is
> actually **implemented.** Where the **Act states the principle** ('digital signatures are legal'),
> the **Rules state the mechanics**: how **Certifying Authorities are licensed**, how **certificates
> are issued/suspended/revoked**, the **Controller's duties**, **standards, audit, and fees.** Make
> the parent/child relationship explicit: the **Act** is the parent law **(passed by Parliament)**;
> the **Rules** are **executive procedures** made under it, and are **easier to amend.** *(Confirm the
> exact year and rule numbers.)*

- 🇳🇵 **Local example:** the **licensing requirements** a Nepali entity must meet to **operate as a
  Certifying Authority** under the **Office of the Controller** — application, standards, audits, fees.

> ❌ **Misconception:** *"Rules and the Act are the same thing."*
> ✅ **Correction:** "They are **different in kind**: the **Act** is the **parent law passed by
> Parliament** (principles and offences); the **Rules** are **detailed procedures issued by the
> executive** under the Act, and are **easier to amend.** Confusing the two is a classic exam mistake."

> 🖼️ Visual: an **Act vs Rules** comparison (who makes it / binding / how easy to change / example).

> 🎙️ Speaker note: Confirm year/rule numbers. Land: the Act sets the principle; the Rules are the
> operating manual.

**📊 Depth table — Act vs Rules — the parent law vs the procedures**

| Question | The Act (ETA) | The Rules (ETR) |
|---|---|---|
| What is it? | The parent primary law | Subordinate procedures under the Act |
| Who makes it? | Parliament (legislature) | The executive/government under the Act |
| What does it do? | States principles & offences | Spells out the how-to (licensing, certificates, fees) |
| How binding? | Primary legislation | Binding, but derives authority from the Act |
| How easy to change? | Hard — needs Parliament | Easier — amended by the executive |
| Example content | 'Digital signatures are legally valid' | 'How a CA is licensed and audited' |

*ℹ️ Rules and the Act are NOT the same thing: the Act is the parent law; the Rules are the detailed procedures issued under it. ⚠️ Verify specifics.*


#### Concept 2 — The Controller & Certifying Authorities (PKI in Nepal) `[THEORY]` `[~12 min]`

[SLIDE] **Controller → CAs → user certificates**

> **Deliver:** Define the bodies. **The Office of the Controller of Certification (OCC, the
> "Controller"), under the Ministry of Communication and Information Technology (MoCIT), is the
> government body that LICENSES and SUPERVISES Certifying Authorities (CAs).** CAs, in turn, **issue
> digital-signature certificates to the public.** Together they form Nepal's **PKI trust hierarchy:
> Controller (root) → licensed CAs → end-user certificates.** Explain that **trust flows DOWN** the
> chain — a certificate is only as trustworthy as the **CA and Controller above it.**

- 🇳🇵 **Local example:** the **Office of the Controller of Certification** (under **MoCIT**) and the
  **rollout of licensed CAs** to enable legally valid digital signatures in Nepal.
- 🇳🇵 **Mini case (work it):** a **CA issues a certificate without verifying identity**, and it's
  **used in fraud** — what is the **Controller's supervisory/audit role?** Draw out that the
  Controller's **audit and revocation powers** are what should **detect it, sanction the CA, and
  revoke the certificate.**

> ❌ **Misconception:** *"Any website or company can just hand out legally valid digital certificates."*
> ✅ **Correction:** "In Nepal, **only CAs LICENSED and SUPERVISED by the Controller** can issue
> **legally recognised** certificates. The **Controller is the root of trust**; an **unlicensed
> 'certificate' has no legal standing.** That **supervised chain** is the entire point of PKI."

> 🖼️ Visual: the **PKI trust pyramid** — Controller → CAs → user certificates.

> 🎙️ Speaker note: Land "trust flows down the chain." The Controller's audit/revocation power is what
> keeps CAs honest.

**📊 Depth table — The PKI trust chain — who does what**

| Role in the chain | Who / where (Nepal) | What they do → why it matters |
|---|---|---|
| Controller (root authority) | Office of the Controller of Certification (under MoCIT) | Licenses & supervises CAs → sets the root of trust |
| Certifying Authority (CA) | Licensed bodies under the Controller | Issue certificates after verifying identity |
| Certificate | Issued to an end user | Binds a public key to a verified identity |
| Subscriber / end user | Citizen, bank, business | Signs documents with their private key |
| Relying party | Anyone verifying a signature | Trusts the signature via the chain above |
| Audit / revocation | Controller's supervisory power | Catches a CA that issues certificates carelessly |

*ℹ️ Trust flows down: Controller → CA → certificate → user. A certificate is only as trustworthy as the chain that issued it. ⚠️ Verify specifics.*


#### Concept 3 — The IT Policy of Nepal `[THEORY]` `[~9 min]`

[SLIDE] **The destination on the map — not the road law**

> **Deliver:** Define it. **Nepal's IT Policy is a national policy document setting the government's
> VISION and GOALS for ICT development — not a law, but a strategic framework.** Its goals typically
> include **building ICT infrastructure, expanding e-governance, growing the IT industry/exports and
> jobs, promoting digital literacy and inclusion, and improving information security.** It is
> **direction, not a binding legal mechanism.** *(Confirm which policy version is current for
> teaching — e.g. the IT Policy 2072 and the "Digital Nepal Framework" ambitions.)*

- 🇳🇵 **Local example:** **IT Policy goals** — e.g. the **IT Policy 2072 / "Digital Nepal Framework"**
  ambitions: **bridging the digital divide, e-government services, making Nepal a knowledge/IT hub.**
  *(Confirm the current version.)*

> ❌ **Misconception:** *"The IT Policy is legally binding like the ETA."*
> ✅ **Correction:** "It is **not.** **Policy sets direction and goals; laws (the ETA) and rules (the
> ETR) provide the binding legal mechanism.** Citing the IT Policy as if it could **criminalise or
> enforce** is a common and costly mistake."

> 🍿 **Fun analogy:** "The **IT Policy** is the **destination on the map** (where Nepal wants to go
> digitally), the **ETA** is the **road law**, and the **ETR + Controller** are the **licensing office
> and traffic police** that keep the road usable."

> 🖼️ Visual: the **Act vs Rules vs Policy** three-way comparison (who makes it / binding? / what it
> does / example).

> 🎙️ Speaker note: Confirm the current policy version. The exam trap is treating the IT Policy as
> binding law — hammer that it directs, it does not bind.

**📊 Depth table — Act vs Rules vs Policy — the three, side by side**

| Question | Act (ETA) | Rules (ETR) | Policy (IT Policy) |
|---|---|---|---|
| Who makes it? | Parliament | Executive (under the Act) | Government (as strategy) |
| Legally binding? | Yes — primary law | Yes — under the Act | No — a direction/vision |
| What it does | States principles & offences | Spells out procedures | Sets national goals & vision |
| Can it punish? | Yes (offences chapter) | Enforces procedures | No — it guides, not punishes |
| Example | 'E-signatures are valid' | 'How a CA is licensed' | 'Make Nepal an IT/knowledge hub' |

*ℹ️ A classic exam trap: the IT Policy is NOT binding law. Policy directs; the Act + Rules bind. ⚠️ Verify specifics against the official text.*

#### 🛠 ACTIVITY — "Act, Rule, or Policy?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Sort the statements**

> **Run it:** In pairs (2 min), sort **five statements** into **Act / Rules / Policy** (e.g.
> '**e-signatures are valid**'; '**how a CA is licensed**'; '**make Nepal an IT hub**'). For each,
> say **WHO makes it** and **whether it is legally binding.** Take **3–4 answers aloud** (3 min).
> Close: "**Only the Act & Rules are binding; the Policy sets goals** — this is a favourite exam
> distinction." Answers: 'e-signatures valid' = **Act**; 'how a CA is licensed' = **Rules**; 'make
> Nepal an IT hub / digital literacy' = **Policy.**

> 🎙️ Speaker note: Reward correct **who-makes-it + binding** reasoning.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** In Nepal, the body that LICENSES and SUPERVISES Certifying Authorities is the:
a) a private CA b) ✅ **Office of the Controller of Certification** c) the Cyber Bureau d) the IT Tribunal

**MCQ 2.** Which is a STRATEGIC FRAMEWORK rather than binding law?
a) the ETA b) the ETR c) ✅ **the IT Policy of Nepal** d) the Criminal Code

**Discussion prompt:** *Name one IT Policy goal Nepal has progressed on, and one it has not — with evidence from daily life.*

> 🎙️ Speaker note: Nail the **Act/Rules/Policy** distinction and the **Controller's** role in PKI.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** when you **obtain a digital-signature certificate** (for tax, banking, or
e-government), it **traces back through a licensed CA to the Controller** — and **national IT Policy
goals shape which digital services exist for you at all.** This is the **machinery behind Nepal's
digital life.**

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **The ETR are procedures implementing the ETA** — licensing of CAs, certificates, the Controller's duties.
2. **The Controller (OCC) licenses & supervises CAs** in Nepal's **PKI trust chain** (Controller → CAs → users).
3. **The IT Policy sets non-binding national digital goals**; the **Act + Rules** are what actually **bind.**

**Next session (S48):** information-security policies, then a **full course review and exam/project prep** to close IT 246.

---
---

# S48 — Information Security & Policies · Course Review & Wrap-up
**Lecture hour 4 of 4 (Unit 9) · 50 minutes — CLOSES UNIT 9 & THE COURSE**

> **Adapted session:** part **new theory** (information-security policies), part **course-wide
> synthesis + exam/project prep.** The end-of-session quiz slot is complemented by a **course review
> structure** and **exam guidance** (the formal end-of-unit quiz still appears below).

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Law punishes after; policy protects before"**

> **Deliver (≈2 min):** Reframe the whole course. "**Laws punish crime AFTER it happens** — but a
> good security **POLICY tries to stop it before.**"
>
> **Run it (≈3 min):** "As we **close the course**: how does an organization (or **you**) actually
> **write the rules that keep data safe** — and how do **all 9 units fit together?**" Agenda: **CIA
> triad → security policy → where law meets policy → the whole course as one arc.**

> 🎙️ Speaker note: This session is **new content + synthesis.** Keep the new theory **compact** so
> there is time for the course review and exam/project prep.

---

### 📚 PART A — CONTENT `[~20 min]`

#### Concept 1 — Information Security & the CIA Triad `[THEORY]` `[~7 min]`

[SLIDE] **Confidentiality · Integrity · Availability**

> **Deliver:** Define it. **Information security is protecting information's Confidentiality,
> Integrity, and Availability — the CIA triad.** **Confidentiality** = only authorised people see
> the data; **Integrity** = the data is accurate and unaltered; **Availability** = the data is there
> when needed. **Lose any one corner and the information is not secure.** Explicitly **link back**:
> this ties **Unit 5 (cybersecurity), Unit 6 (personal security), Unit 7 (social engineering)** to
> the **legal/policy controls** here. And the through-line to Unit 9: **law punishes AFTER a breach;
> security protects the triad BEFORE.**

- 🇳🇵 **Local example:** a **Nepali bank's customer-data protection obligations**; **NRB/regulatory
  IT-security expectations** push exactly the CIA triad.

> ❌ **Misconception:** *"Security just means keeping data secret (confidentiality)."*
> ✅ **Correction:** "Confidentiality is **only one corner.** A system that keeps data secret but lets
> it be **silently altered** (integrity failure) or **knocked offline** during a festival rush
> (availability failure) is **still insecure.** Real security protects **all three corners together.**"

> 🖼️ Visual: the **CIA triad triangle.**

> 🎙️ Speaker note: Link back to Units 5–7 explicitly — those taught the attacks; CIA is the frame the
> defences protect.

**📊 Depth table — The CIA triad — what each protects and the threat if lost**

| CIA element | What it protects (Nepal example) | Threat / consequence if lost |
|---|---|---|
| Confidentiality | A bank's customer KYC data stays private | Data leak → privacy breach, ETA/Privacy Act liability |
| Integrity | An account balance is accurate & unaltered | Tampered records → fraud, wrong decisions |
| Availability | eSewa/mobile banking works when needed | Downtime/DoS → customers locked out, lost trust |
| Confidentiality | Exam results seen only by the right office | Premature leak → unfairness, reputational harm |
| Integrity | A digitally signed contract not modified | Silent alteration → disputes, non-repudiation lost |
| Availability | A hospital system reachable in an emergency | Outage → direct risk to patient care |

*ℹ️ Security means protecting ALL THREE at once — confidentiality, integrity, AND availability. A system can 'work' yet still fail the triad.*


#### Concept 2 — Information Security Policy (ISP) `[THEORY]` `[~7 min]`

[SLIDE] **Policy → Standard → Procedure → Guideline**

> **Deliver:** Define it. **An information security policy is a documented set of rules governing how
> an organization protects its information assets.** Teach the **hierarchy**: **POLICY** (the rule &
> intent) → **STANDARDS** (measurable requirements) → **PROCEDURES** (step-by-step how-to) →
> **GUIDELINES** (advisory). List the **typical components**: **acceptable-use, access-control &
> password, data classification, incident response, BYOD, backup/retention.** Land the governance
> point: **security is governance + people + process, not only firewalls.** It **aligns with Nepal's
> Privacy Act 2075 / data-protection expectations and the ETA** *(verify current status).*

- 🇳🇵 **Local example:** an organization's **acceptable-use and password policy**; **alignment with
  Nepal's Privacy Act 2075 / data-protection expectations** and the **ETA.** *(Verify current
  data-protection status.)*
- 🇳🇵 **Mini case:** an **employee uses a personal USB / shares a password** — **which policy** should
  have prevented it (BYOD/AUP + access-control/password), and **what's the incident-response step?**

> ❌ **Misconception:** *"Security is only a technical/IT-team problem."*
> ✅ **Correction:** "It is **governance + people + process.** **Firewalls don't stop an employee
> sharing a password** or losing an unencrypted laptop — **policy, training, and user behaviour do.**
> **Most breaches exploit people and process gaps**, not just technology."

> 🖼️ Visual: the **policy → standard → procedure → guideline** hierarchy.

> 🎙️ Speaker note: Use the USB/password mini-case to show the policy that should have prevented it
> and the incident-response step.

**📊 Depth table — Information-security policy components — and the threat each stops**

| Policy component | What it governs | Threat it stops (Nepal example) |
|---|---|---|
| Acceptable-use policy (AUP) | How staff may use company systems | Misuse, shadow IT, risky browsing |
| Access control & password policy | Who can access what; strong passwords | Weak/shared passwords → account takeover |
| Data classification | How data is labelled & handled | Sensitive KYC data treated carelessly |
| Incident response | Steps when a breach occurs | Slow, chaotic reaction that worsens a breach |
| BYOD policy | Personal devices on the network | An infected personal phone/USB spreads malware |
| Backup & retention | How data is backed up & kept | Ransomware/data loss with no recovery |

*ℹ️ Security is governance + people + process, not only firewalls — user behaviour and written policy matter as much as technology.*


#### Concept 3 — Where Law Meets Policy `[THEORY]` `[~6 min]`

[SLIDE] **Criminalise · Direct · Operationalise**

> **Deliver:** Tie the layers together. **Law and policy play different, complementary roles:**
> - The **ETA CRIMINALISES** wrongdoing — punishment **after** harm, with penalties.
> - The **IT Policy DIRECTS** national digital goals — non-binding **direction.**
> - **Information-security policies OPERATIONALISE** protection **inside organizations** — stopping
>   harm **before** it happens.
>
> Land the synthesis: **good internal policy reduces both breaches AND legal liability** — it is
> where the **law lands in daily practice.** Together they give **prevention (policy) + deterrence/
> punishment (law) + direction (national policy).**

- 🇳🇵 **Local example:** a **Nepali bank's security policy** keeps data safe day-to-day; if a breach
  happens, the **ETA + Privacy Act 2075** govern the consequences; the **national IT Policy** shaped
  which digital services existed to protect in the first place.

> ❌ **Misconception:** *"Once there's a law, we don't need internal policy"* — OR — *"policy is
> enough, the law is irrelevant."*
> ✅ **Correction:** "**Neither is true.** Law **punishes after** the fact and **deters**; policy
> **prevents before** the fact and **reduces liability.** You need **prevention (policy) AND
> deterrence (law)** — they are **complementary layers, not substitutes.**"

> 🎙️ Speaker note: This is the bridge from the whole unit into the course synthesis: the ETA
> criminalises, the IT Policy directs, and infosec policy operationalises.

**📊 Depth table — Law vs national policy vs organizational security policy**

| Layer | Role | When it acts | Nepal example |
|---|---|---|---|
| ETA (cyber law) | Criminalises & punishes | AFTER harm occurs | Prosecuting a hacker or fraudster |
| IT Policy (national) | Directs & sets goals | Ongoing strategy | 'Digital Nepal' e-governance ambition |
| Security policy (org) | Operationalises protection | BEFORE harm occurs | A bank's AUP, password & incident policy |
| Together | Prevent + deter + direct | All the time | Fewer breaches AND less legal liability |

*ℹ️ The ETA criminalises, the IT Policy directs, and information-security policies operationalise protection — good policy reduces both breaches AND legal liability.*

---

### 📚 PART B — COURSE-WIDE REVIEW (synthesis of all 9 units) `[~10 min]`

[SLIDE] **The whole course as one arc**

> **Deliver:** Present the course as **one connected story**, not nine disconnected topics: **ETHICS
> (should) → SECURITY (protect) → FORENSICS (investigate) → LAW (govern & punish)**, with **Nepal
> context binding Units 8–9** (the Cyber Bureau investigates, the ETA prosecutes). Walk the map, then
> the 9-unit table. Encourage students to **redraw this arc from memory** — it is the mental map they
> carry into the exam.

- **Unit 1 — Overview of Ethics:** ethics vs law, CSR, ethical decision-making, why IT ethics is distinct.
- **Unit 2 — Ethics for IT Workers & Users:** professionalism, privacy/anonymity, social-networking ethics.
- **Unit 3 — Intellectual Property:** copyright, patent, trade secrets, plagiarism, cybersquatting.
- **Unit 4 — Software Dev Ethics & IT Organizations:** software quality, outsourcing, whistle-blowing, green computing.
- **Unit 5 — Fundamentals of Cybersecurity:** cyberspace, attack types, attacker "hats," risks mitigated.
- **Unit 6 — Personal Cybersecurity:** posture, devices/IoT, passwords, work-from-home security.
- **Unit 7 — Social Engineering & Cyber Terrorism:** trust exploitation, countermeasures, cyber-terrorism effects.
- **Unit 8 — Digital Forensics:** stages, evidence handling, mobile forensics, cyber forensics in Nepal.
- **Unit 9 — Cyber Law in Nepal:** ETA 2063, ETR, Controller/CAs, IT Policy, infosec policies.

> **The through-line:** *ethics (should) → security (protect) → forensics (investigate) → law (govern
> & punish)* — one connected arc, with **Nepal context binding Units 8–9.**

> 🖼️ Visual: a **course-on-a-page** map — all 9 units as a connected arc.

**📊 Depth table — IT 246 on a page — each unit, its focus, and the through-line**

| Unit | Focus | Key concepts to revise |
|---|---|---|
| U1 Overview of Ethics | Ethics vs law, CSR | Ethical decision framework, why IT ethics is distinct |
| U2 Ethics for IT Workers/Users | Professionalism, privacy | Codes, anonymity, social-networking harms |
| U3 Intellectual Property | Protecting creations | Copyright, patent, trade secrets, plagiarism, cybersquatting |
| U4 Software Dev & IT Orgs | How software is built | Quality, outsourcing, whistle-blowing, green computing |
| U5 Fundamentals of Cybersecurity | Cyberspace & attacks | Attack types, attacker 'hats', risks mitigated |
| U6 Personal Cybersecurity | Protecting yourself | Posture, devices/IoT, passwords, work-from-home |
| U7 Social Engineering & Cyber Terror | Exploiting trust | Countermeasures, cyber-terrorism effects |
| U8 Digital Forensics | Investigating incidents | Stages, evidence handling, mobile & cyber forensics in Nepal |
| U9 Cyber Law in Nepal | Governing the digital world | ETA 2063, ETR, Controller/CAs, IT Policy, infosec policy |

*ℹ️ The through-line: ethics (should) → security (protect) → forensics (investigate) → law (govern & punish). Nepal context binds Units 8–9.*

---

### 📚 PART C — EXAM PREPARATION GUIDANCE `[~5 min]`

> **Deliver:** Give students the **shapes** exam questions take and the **technique** for each.
> - **Likely question shapes:** definitions (ethics, IP types, CIA), compare/contrast (Act vs Rules
>   vs Policy; ethics vs law; white/grey/black hat), applied cases (analyse a Nepal cyber incident;
>   classify a cybercrime), and "explain provisions of the ETA / role of the Controller."
> - **High-yield topics:** Unit 1 decision framework, Unit 3 IP distinctions, Unit 5 attack taxonomy,
>   Unit 8 forensic stages + chain of custody, Unit 9 ETA provisions & Cyber Bureau.
> - **Answer technique:** **define → explain → Nepal example → diagram** where useful; for case
>   questions use the **Unit 1 five-step ethical process.**
> - **Common pitfalls:** confusing **Act/Rules/Policy**; **misquoting ETA section numbers/penalties**
>   (learn the **concept**, cite section as "Section ~47 — verify"); treating the **IT Policy as
>   binding law.**

**📊 Depth table — Likely question shapes, how to answer, and high-yield topics**

| Question shape | Answer technique | High-yield topic |
|---|---|---|
| Definition (ethics, IP types, CIA) | Define → explain → Nepal example | U1 framework · U3 IP · CIA triad |
| Compare/contrast | Use a comparison table structure | Act vs Rules vs Policy; ethics vs law; hat colours |
| Applied Nepal case | Classify → cite the concept → steps | Classify a cybercrime; forensic chain of custody |
| 'Explain provisions of the ETA' | Two halves → key offences → note 'verify' | ETA 2063; Controller's role |
| Attack/defence taxonomy | Name → mechanism → countermeasure | U5 attack types; U7 social engineering |
| Discussion / argue both sides | State both, then a reasoned view | Section ~47: protection vs free speech |

*ℹ️ Answer technique: define → explain → Nepal example → diagram. PITFALLS: confusing Act/Rules/Policy; misquoting ETA section numbers (learn the CONCEPT, cite 'Section ~47 — verify'); treating IT Policy as binding law.*

---

### 🛠 PART D — PROJECT / LAB PRESENTATION STRUCTURE `[ACTIVITY]` `[~5 min]`

[SLIDE] **The project/lab presentation skeleton**

> **Deliver / run it:** Give the skeleton the students should use to present lab/project work (lab
> themes: **network scanning, sniffing, web-app vulnerabilities (SQLi, XSS), phishing via the Social
> Engineering Toolkit, password cracking, firewall config, incident response**):
> 1. **Problem/threat & objective** — what you set out to do and why it matters.
> 2. **Tool/method used** — **ethically, in a lab/sandbox.**
> 3. **Findings/demo** — what you discovered, shown clearly.
> 4. **Mitigation & relevant Nepal law/policy** — the fix, tied to the **ETA / infosec policy.**
> 5. **Ethics & legal note** — **authorization, scope, responsible disclosure.**
>
> Emphasise the line: **every offensive technique must be tied back to AUTHORIZATION and the ETA** —
> "**doing it for a class on your own lab**" vs "**doing it to a real system**" is the line between
> **learning and a crime.**

> 🎙️ Speaker note: Make students **state the authorization line explicitly.** This is the ethical
> capstone of the whole course.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`
*(kept light — the main assessment is the course review above + the end-of-unit quiz below)*

**MCQ 1.** The CIA triad stands for Confidentiality, Integrity, and:
a) Authentication b) Authorization c) ✅ **Availability** d) Auditing

**MCQ 2.** A document stating how staff may use company systems is a(n):
a) firewall b) ✅ **acceptable-use / information-security policy** c) digital signature d) IT Policy of Nepal

**Discussion prompt:** *Write one rule you'd put in your college's information-security policy and say which threat it stops.*

> 🎙️ Speaker note: Draw out "security = **people + process**, not just tech."

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** the synthesis is your **actual professional posture**: as a **BIM
graduate** you will **make ethical calls, secure systems, respond to incidents, and stay within
Nepali law — all at once.** The whole course was preparation for that single, integrated judgement.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Information-security policies operationalise protection:** CIA triad → policy → standards → procedures.
2. **The 9 units form one arc** — ethics (should) → security (protect) → forensics (investigate) → law (govern & punish).
3. **Exam = concepts + Nepal examples + applied cases;** lab projects must always be framed within **authorization and the ETA.**

**Next:** the **End-of-Unit Quiz** below, then final revision — and that **completes IT 246.**

---
---

## 📋 Unit 9 — End-of-Unit Quiz

> ⚠️ Mark all ETA/ETR **section numbers and penalty figures** as **"verify against official text"** in
> the answer key.

### Section A — Multiple Choice (answers shown)
1. Nepal's primary cyber law is → ✅ **the Electronic Transaction Act (ETA) 2063**
2. A cybercrime where the computer is the TOOL is → ✅ **online fraud / cyber-defamation**
3. The Nepali body that investigates cybercrime is → ✅ **the Nepal Police Cyber Bureau**
4. What gives an electronic record legal validity in Nepal → ✅ **the ETA 2063**
5. A digital signature primarily provides → ✅ **authentication, integrity, and non-repudiation**
6. The most-applied & criticised ETA provision is → ✅ **the e-publication offence ('Section ~47' — verify)**
7. Act vs Rules vs Policy: the non-binding one is → ✅ **the IT Policy of Nepal**
8. The body that licenses & supervises CAs is → ✅ **the Office of the Controller of Certification**
9. The CIA triad stands for → ✅ **Confidentiality, Integrity, Availability**
10. "The IT Policy is binding law like the ETA" is → ✅ **FALSE (policy directs; the Act + Rules bind)**

### Section B — Short Answer (5)
11. Define cyber law and give one reason Nepal needs it.
12. List 4 cybercrimes recognised under Nepali law.
13. State the two main purposes of the ETA 2063.
14. Explain the role of the Controller and Certifying Authorities.
15. List 4 components of an information-security policy.

### Section C — Applied Case (2)
16. A person is impersonated on social media in Nepal and defamed — outline which body investigates, which provision applies (cite as "verify"), and the steps.
17. Classify four given scenarios as target/tool cybercrime and name the likely ETA-related response.

### Section D — Discussion (1)
18. *"Section 47 of the ETA: necessary protection against online harm, or a threat to free speech? Argue both sides with Nepal examples."*

> *(Full model answers are on the concept slides and in this file. ⚠️ Verify all legal figures against the official text before finalising the answer key.)*

---

## Unit 9 · Cheat Sheet (one-page revision)

- **Cyber law & cybercrime (S45):** Cyber law fills the gap paper-law can't reach (identity/evidence/jurisdiction). Nepal's primary cyber law = **ETA 2063** (NOT a stand-alone Cyber Crime Act). Cybercrime = computer as **TARGET** (hacking, data theft) or **TOOL** (fraud, defamation). Report to the **Cyber Bureau** (2018) — **evidence first.**
- **ETA 2063 (S46):** Two halves — **ENABLE** (e-records + digital-signature validity) + **PUNISH** (offences chapter). Digital signature = private key signs / public key verifies → **authentication + integrity + non-repudiation.** "Section ~47" (e-publication) = most-cited & debated. **Figures illustrative — verify.**
- **ETR & Controller (S47):** **ETR 2064** = procedures under the Act (CA licensing, certificates, fees). **Controller (OCC, under MoCIT)** licenses & supervises CAs → PKI chain: **Controller → CAs → user certificates.** Act = Parliament (binding); Rules = executive (binding); differ in kind.
- **IT Policy (S47):** National strategic framework — infrastructure, e-gov, IT exports, digital literacy, security ("Digital Nepal"). **NOT binding law.** Policy directs; the Act + Rules bind.
- **Information security (S48):** **CIA triad** = Confidentiality + Integrity + Availability (lose one = insecure). Policy hierarchy: policy → standards → procedures → guidelines. Components: AUP, access/password, data classification, incident response, BYOD, backup. Security = **governance + people + process.**
- **Law meets policy + arc (S48):** ETA **criminalises** (after), IT Policy **directs**, security policy **operationalises** (before). Course arc: **ethics → security → forensics → law.** Labs: every technique tied to **AUTHORIZATION + the ETA.**

---

## Unit 9 · Glossary (key terms)

- **Cyber law** — the body of law governing computers, networks, the internet, and e-transactions.
- **ETA 2063** — the Electronic Transaction Act (2008) — Nepal's primary cyber law.
- **ETR 2064** — the Electronic Transaction Rules — procedures made under the ETA.
- **Cybercrime** — an offence where a computer/network is the target or the tool.
- **Target vs tool crime** — the computer is the victim (hacking) vs the weapon (fraud, defamation).
- **Cyber Bureau** — the Nepal Police cybercrime unit (est. 2018, Bhotahiti, Kathmandu).
- **Electronic record** — digital data given legal recognition equal to paper under the ETA.
- **Digital signature** — a cryptographic signature: private key signs, public key verifies.
- **Asymmetric cryptography** — a public/private key pair used to sign and verify.
- **Non-repudiation** — the signer cannot later deny having signed.
- **Section ~47 (illustrative)** — the most-applied & criticised e-publication offence — verify.
- **Controller (OCC)** — the Office of the Controller of Certification — licenses & supervises CAs.
- **Certifying Authority (CA)** — a licensed body that issues digital-signature certificates.
- **PKI** — public-key infrastructure — the Controller → CA → user trust chain.
- **IT Tribunal** — the ETA body for adjudicating certain electronic-transaction disputes.
- **IT Policy of Nepal** — a non-binding national strategic framework for ICT development.
- **Act vs Rules vs Policy** — Act (Parliament, binding) · Rules (executive, binding) · Policy (direction, non-binding).
- **Privacy Act 2075** — Nepal's data-privacy law, complementing the ETA (verify current status).
- **CIA triad** — Confidentiality, Integrity, Availability — the pillars of information security.
- **Information security policy** — documented rules for protecting an organization's information assets.
- **Policy → standard → procedure** — policy (what/why) → standard (measurable) → procedure (how-to).
- **Acceptable-use policy (AUP)** — rules on how staff may use company systems.
- **Incident response** — the defined steps taken when a security breach occurs.

---

*End of Unit 9 — and the end of IT 246. Congratulations to the cohort: across nine units you learned
to reason ethically, protect systems, investigate incidents, and stay within Nepali law — one
integrated professional judgement. ⚠️ All legal specifics in this file are illustrative of the
framework and its debate — always verify the current official Nepali text before relying on them.*
