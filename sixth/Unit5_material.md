# IT 246 — Unit 5: Fundamentals of Cybersecurity
### Full Lecturer-Ready Session Material (S22–S27)

**Program:** BIM, 6th Semester · **Unit weight:** 6 lecture hours
**Sessions:** S22–S27 (50 min each) · **Local context:** Nepal / South Asia
**Format:** Markdown — source of truth; the built deck is `IT246_Unit5.pptx` (94 slides), regenerated via `build_unit5_pptx.py` (imports `deckkit.py`).

> **Framing note (read to the class on day one of this unit).** This is a **defensive / awareness**
> unit. Every attack is described **only so you can recognise and defend against it** — there are **no
> exploit or attack-execution recipes** anywhere in this material. The goal is a citizen and future IT
> professional who can name the trick *and* the defence.

> **How to read this file.** This is written to **carry a full 50 minutes on its own.** Each session
> has **minute markers** `[~X min]`, the actual **explanation to deliver** (prose, not just bullets),
> **worked examples**, a **timed in-class activity**, and lecturer cue cards in `> 🎙️` blocks.
> `[SLIDE]` marks slide-ready blocks; `🖼️` marks diagram cues. Pace tags: `[THEORY] [EXAMPLE]
> [ACTIVITY] [QUIZ]`. Total per session: **5 + 35 + 5 + 3 + 2 = 50 min.**

---

## Unit 5 — Learning Outcomes
By the end of this unit, students will be able to:
1. Define cyberspace and cybersecurity, and explain the CIA triad as the core security objective.
2. Explain how technological change, economic-model shifts, and outsourcing reshape the threat landscape.
3. Express risk as threat × vulnerability × impact and use it to prioritise defences.
4. Recognise common cyberattacks (malware, phishing, DoS, poisoned web services) and the defences against them.
5. Explain ARP/DNS poisoning and man-in-the-middle conceptually, and name the countermeasures.
6. Classify cyberattackers by motive and "hat" (white/grey/black, script kiddies, hacktivists, state actors, insiders).

---
---

# S22 — Introduction to Cyberspace & Cybersecurity · the CIA Triad
**Lecture hour 1 of 6 (Unit 5) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Where does it all live — and safe from what?"**

> **Deliver (≈2 min):** Read it slowly. "Your **eSewa balance**, your **exam results** on a college
> portal, the **NEA billing system**, the **army's email** — all live in the same 'place' that **doesn't
> physically exist.**"
>
> **Run the question (≈3 min):** "**Who is responsible for keeping it safe — and safe *from what
> exactly*?**" Take a few answers. Most say "the internet" or "hackers." Land the theme: today we give
> that 'place' a name (**cyberspace**), define what protecting it means (**cybersecurity**), and give
> 'secure' a precise meaning (**the CIA triad**).

> 🎙️ Speaker note: Don't resolve it yet — the point is to show 'the internet' is only part of the
> picture and 'secure' needs a precise definition. Agenda on the board: cyberspace → cybersecurity →
> CIA triad.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — What Is Cyberspace `[THEORY]` `[~10 min]`

[SLIDE] **A domain, like land, sea, air, and space**

> **Deliver:** Define it and write it on the board. **Cyberspace is the interconnected digital
> environment of networks, systems, data, and the people and devices using them.** The key move:
> **it is NOT just "the internet" or "the websites I visit."** It includes **private and bank
> networks, the cloud, OT/ICS** (the industrial control software running a power grid or water plant),
> and **mobile**. Militaries treat it as the **"fifth domain"** of conflict, after land, sea, air, and
> space.

- 🌍 **Global example:** NATO and modern militaries formally treat **cyberspace as the fifth domain**
  of operations — a place where conflict happens, just like land, sea, air, and space.
- 🇳🇵 **Local example:** Nepal's cyberspace is growing fast — the **National ID** system,
  **eSewa / Khalti** wallets, the **Nagarik App**, online banking, and **e-governance portals** — plus
  the **NEA grid / billing software** you never see but which is just as much a part of it.

> ❌ **Common misconception:** *"Cyberspace = the websites I visit."*
> ✅ **Correction — say it out loud:** "It includes **back-end systems, infrastructure (OT/ICS), the
> cloud, and offline-connected devices** too. Protecting cyberspace means protecting the **plumbing you
> never see**, not just the pages on your screen."

> 🖼️ Visual: the **five domains** (land / sea / air / space / **cyber**), plus a grid of what cyberspace
> *includes* — public internet, private networks, cloud, mobile apps, OT/ICS, connected devices.

> 🎙️ Speaker note: Kill the "cyberspace = my browser tabs" reflex early. Point at **NEA billing / OT**
> and the **Nagarik App** as parts of the same domain that all need protecting.

**📊 Depth table — Is this part of cyberspace? — beyond 'the websites I visit'**

| Real thing (Nepal / IT) | Part of cyberspace? | Why (verdict) |
|---|---|---|
| The websites you browse | Yes | The visible surface — but only a slice of the whole |
| A bank's back-end customer database | Yes | Private systems are cyberspace even if you never see them |
| NEA grid / billing control software (OT/ICS) | Yes | Operational technology is a critical, often-forgotten part |
| The Nagarik App on your phone | Yes | Mobile apps + their cloud back-ends are all in the domain |
| A smart CCTV / IoT sensor in an office | Yes | Connected devices are entry points into cyberspace |
| A paper land-record ledger in a cupboard | No | Not digital / not connected — outside cyberspace (until digitised) |

*ℹ️ 'Cyberspace = the websites I visit' is the misconception. It includes back-end systems, infrastructure (OT/ICS), cloud, and offline-connected devices — a whole domain like land/sea/air.*

#### Concept 2 — What Is Cybersecurity `[THEORY]` `[~10 min]`

[SLIDE] **People + process + technology**

> **Deliver:** Define it. **Cybersecurity is the practice of protecting systems, networks, and data
> from unauthorised access, harm, or disruption.** Then bust the "cybersecurity = antivirus" reflex: it
> rests on **three pillars — people, process, and technology** — and it is a **defensive discipline,
> not a product.**
> - **People** — trained staff and users who don't click the phishing link or share the OTP.
> - **Process** — policies, patching schedules, incident response, backups, access rules.
> - **Technology** — firewalls, antivirus/EDR, encryption, MFA (tools, not the whole answer).
>
> Land the rule: **the weakest of the three pillars decides how secure you really are.**

- 🇳🇵 **Local example:** **NPCERT** (Nepal's national Computer Emergency Response Team) coordinates
  incident response; **banks run dedicated security teams** under **NRB cyber-resilience guidance.**
- 🇳🇵 **Mini case (work it, ≈2 min):** "A college server is reachable from the internet with a
  **default admin password** — is the **threat** the password, the **exposure**, or **both**?" Draw it
  out: **both.** The default password is a **vulnerability** (a process failure), the internet
  reachability is the **exposure**, and someone scanning for it is the **threat**. Security fixes the
  process and the exposure — it doesn't just blame one thing.

> ❌ **Misconception:** *"Cybersecurity just means installing antivirus."*
> ✅ **Correction:** "Antivirus is one piece of the **technology** pillar. Real security is **people +
> process + technology together** — a trained user, a patching policy, *and* a firewall — and it's a
> **continuous discipline**, not a one-time purchase."

> 🎙️ Speaker note: Keep returning to the **weakest-pillar** rule. Antivirus can't save you from an
> untrained clerk (people) or a missing patch policy (process).

**📊 Depth table — People + process + technology — and what fails without each**

| Pillar | What it is | If this pillar is weak (Nepal / IT) |
|---|---|---|
| People | Trained, aware staff and users | A clerk shares an OTP → account drained despite good tech |
| Process | Policies, patching, backups, response | No patch schedule → a known flaw stays open for months |
| Technology | Firewalls, antivirus/EDR, MFA, encryption | No MFA → one stolen password = full access |
| People + process | Trained staff following a set drill | No incident plan → a breach turns into a public disaster |
| Process + tech | Backups that are actually tested | Untested backup fails on restore → ransomware wins |
| All three | A defensive discipline, not a product | 'We bought antivirus, so we're secure' → false confidence |

*ℹ️ Security is only as strong as the weakest pillar. Antivirus alone (technology) cannot save you from an untrained clerk (people) or a missing patch policy (process).*

#### Concept 3 — The CIA Triad `[THEORY]` `[~9 min]`

[SLIDE] **Confidentiality · Integrity · Availability**

> **Deliver:** This is the most important vocabulary in the whole course — write all three on the board
> and keep them there. **The CIA triad is the three goals every security control serves:**
> - **Confidentiality (C)** — data is kept **secret / access-controlled** (encryption, access control).
> - **Integrity (I)** — data stays **unchanged and trustworthy** (hashing, audit logs, checks).
> - **Availability (A)** — the system is **usable when needed** (backups, redundancy, capacity).
>
> Every attack **breaks at least one leg**, and there are **trade-offs**: locking a system down hard
> (C) can hurt Availability. Security is a **balance of all three.**

- 🌍 **Global mapping:** **ransomware** breaks **Availability**; a **leaked database** breaks
  **Confidentiality**; a **tampered exam result** breaks **Integrity.**
- 🇳🇵 **Local example:** a **DDoS knocking a Nepali bank's e-banking offline** = **Availability**;
  **altered land-records data** = **Integrity**; a **leaked KYC / customer database** =
  **Confidentiality.**

> ❌ **Misconception:** *"Security just means keeping secrets (Confidentiality)."*
> ✅ **Correction:** "An **always-down or easily-tampered** system is insecure **even if nothing ever
> leaks.** Integrity and Availability matter just as much."

> 🍿 **Fun analogy (deliver it):** "The CIA triad is a **three-legged stool** — **saw off any leg and
> you fall over.** You need all three at once."

> 🖼️ Visual: the **CIA triangle** with one Nepal example per corner (eSewa balance not leaked / land
> records not altered / e-banking stays online).

> 🎙️ Speaker note: Map each Nepal incident to a leg — DDoS = A, leaked DB = C, altered result = I.
> Keep returning to the stool. Some attacks (ransomware with data theft) break more than one leg.

**📊 Depth table — Confidentiality vs Integrity vs Availability**

| Dimension | Confidentiality (C) | Integrity (I) | Availability (A) |
|---|---|---|---|
| Goal | Keep data secret | Keep data correct & trusted | Keep the service usable |
| Broken when… | Data is leaked/read | Data is secretly altered | Service is knocked offline |
| Typical control | Encryption, access control | Hashing, audit logs, checks | Backups, redundancy, capacity |
| Nepal example (broken) | eSewa/KYC database leaks | Land-record data is altered | e-banking down in a DDoS |
| Attack that hits it | Data theft / spyware | Tampering / defacement | DoS / ransomware lockout |

*ℹ️ Every control ultimately serves one or more of C, I, A. A system that never leaks (C) but is always down (A) or tamper-prone (I) is still insecure — you need all three.*

**📊 Depth table — Which CIA goal does each incident violate?**

| Incident (Nepal / global) | CIA goal violated | Why (verdict) |
|---|---|---|
| Ransomware locks a hospital's files | Availability | Legitimate users can't reach data when needed |
| A leaked eSewa/KYC customer database | Confidentiality | Secret data is now readable by outsiders |
| An exam result changed on a college portal | Integrity | Data is no longer trustworthy / unaltered |
| DDoS takes a bank's e-banking offline | Availability | Service is unusable during the attack |
| Land-record values quietly altered | Integrity | Records look official but are wrong |
| Spyware silently copies your messages | Confidentiality | Private data is read without permission |
| Ransomware that also steals data first | Confidentiality + Availability | Two legs broken at once — data stolen AND locked |

*ℹ️ Naming the violated leg is the vocabulary every security job, audit, and NRB bank inspection uses. Some attacks (ransomware with exfiltration) break more than one leg.*

#### 🛠 ACTIVITY — "Rank C, I, A for your result portal" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Which leg matters most — and why?**

> **Run it:** In pairs (2 min), for the **college result portal**, rank **C, I, and A** by importance
> and justify — what's the worst thing that could happen to each? Take **3–4 answers aloud** (3 min).
> Teams will disagree — that's the point. Land it: for a **result portal, Integrity usually tops**
> (a changed grade is catastrophic); for **e-banking, all three are critical**; for a **KYC store,
> Confidentiality** leads. **The ranking depends on the asset.**

> 🎙️ Speaker note: There is no single 'right' order — the answer depends on the system. Reward pairs
> who justify with a concrete worst-case per leg.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** A ransomware attack that locks files mainly violates:
a) Confidentiality b) Integrity c) ✅ **Availability** d) none

**MCQ 2.** Ensuring data has not been secretly altered is:
a) Confidentiality b) ✅ **Integrity** c) Availability d) authentication

**Discussion prompt:** *For your college result portal, rank C, I, and A by importance — and justify.*

> 🎙️ Speaker note: Draw out that 'secure' means **all three legs**, not just secrecy — and that the
> ranking **depends on the system.**

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** the **CIA triad is the vocabulary you'll use for the rest of this course and
in every real security job.** Every **audit, penetration test, and NRB bank inspection** is ultimately
checking **C, I, and A.** Learn to **name the leg an incident breaks** and you can reason about *any*
attack you meet.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Cyberspace** = the whole connected digital domain (networks, systems, data, people) — **not just the websites you visit.**
2. **Cybersecurity** = **people + process + technology**; a defensive discipline, not just antivirus (the **weakest pillar** wins).
3. The **CIA triad** — Confidentiality, Integrity, Availability — is the **goal every control serves**; every attack breaks a leg.

**Next session (S23):** the **forces** — technology, economics, outsourcing — that keep reshaping this landscape.

---
---

# S23 — Key Development Areas: Technology · Economics · Outsourcing
**Lecture hour 2 of 6 (Unit 5) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Did the shop get a security team too?"**

> **Deliver (≈2 min):** "Ten years ago a **Nepali shop kept cash in a drawer.** Today it takes **QR
> payments**, stores **customer numbers in the cloud**, and runs on a **phone.**"
>
> **Run the question (≈3 min):** "**Did the shop get a security team too?**" Take a few answers. Land
> it: each convenience **added an entry point** but almost **never added a defender.** Today: **why the
> attack surface keeps exploding** — technology → economics → outsourcing.

> 🎙️ Speaker note: The theme is that convenience quietly adds *doors*. Agenda on the board: technology
> growth → economic-model shifts → outsourcing & supply chain.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Technological Changes Expand the Attack Surface `[THEORY]` `[~8 min]`

[SLIDE] **More devices, data, entry points = bigger attack surface**

> **Deliver:** Define the key term. **The attack surface is the sum of all the points where an attacker
> could try to get in.** Each new technology — **cloud, mobile, IoT, AI, remote work** — adds **new
> devices, data, and entry points**, so it **grows the attack surface.** And the crucial lag: **new
> features usually arrive before their security does.**

- 🌍 **Global example:** **billions of IoT devices** shipped with **weak default passwords** became
  **botnet fuel** (e.g. the Mirai botnet powered massive DDoS attacks).
- 🇳🇵 **Local example:** the explosion of **QR payments (fonepay)**, the **Nagarik App**, **smart
  CCTV**, and cheap **IoT** in Nepali homes and offices — each a new door.

> ❌ **Misconception:** *"New technology is automatically more secure."*
> ✅ **Correction:** "Usually the **opposite** — new features arrive first and their security hardening
> comes **later** (or never for cheap IoT). Adopting a technology **without** adding its defence
> quietly **grows your attack surface.**"

> 🖼️ Visual: a **growing attack-surface** graphic — 2010 (a till + one PC, few entry points) vs 2026
> (QR pay, cloud DB, app, CCTV, staff phones, IoT — many entry points).

> 🎙️ Speaker note: Contrast 2010 with 2026 concretely. Every convenience listed is *also a door*.

**📊 Depth table — New technology → the new attack surface it adds (Nepal)**

| New technology adopted | New entry point it adds | Defence to add with it |
|---|---|---|
| QR payments (fonepay) at a shop | Fake QR / payment-redirect risk | Verify payee name; staff training; reconcile daily |
| Customer data moved to the cloud | Data now reachable over the internet | Access control, encryption, MFA on the console |
| Smart CCTV / IoT in the office | Cheap devices with weak defaults | Change defaults, segregate on their own network, patch |
| Staff use personal phones for work | Lost/compromised phone = data leak | Screen lock, remote wipe, keep work data separate |
| Remote / work-from-home setup | Home Wi-Fi and PCs you don't control | VPN, endpoint protection, secure config policy |
| An AI chatbot handling queries | New data flows + prompt-abuse risk | Limit data it sees; monitor; validate its outputs |

*ℹ️ Each row PAIRS the new tech with the defence it demands. New features arrive before their security — so the habit is: adopt a technology, add its defence in the same breath.*

#### Concept 2 — Economic Model Shifts: Cybercrime as a Business `[THEORY]` `[~8 min]`

[SLIDE] **Crime went pro — attacks are now rented**

> **Deliver:** **Cybercrime and IT itself have become businesses, and that changes who attacks and
> why.** Three shifts:
> - **SaaS / cloud** moves data onto third-party platforms you don't own — a new dependency and target.
> - **"Cybercrime-as-a-Service" / Ransomware-as-a-Service (RaaS)** lets **low-skill criminals RENT**
>   ready-made attack tools — lowering the skill needed to attack.
> - **Data itself becomes a commodity** — stolen cards, credentials, and KYC sold **in bulk.**

- 🌍 **Global example:** **ransomware gangs operate like companies** — some even run a **"customer
  support" desk** to help victims pay the ransom.
- 🇳🇵 **Local example:** stolen **card / eSewa / bank credentials** are sold in bulk, and
  **pre-packaged phishing kits** are aimed specifically at **Nepali users** (fake bank-KYC, fake wallet
  rewards).
- 🇳🇵 **Mini case:** "Why does a **low-skill criminal in 2026** pose **more risk** than one in 2010?"
  Answer: **rented, ready-made tools** — they don't need to build anything.

> ❌ **Misconception:** *"Only a genius hacker could attack us, and we're too small to bother with."*
> ✅ **Correction:** "RaaS and rented phishing kits mean a **low-skill criminal can run a powerful
> attack cheaply and at scale** — **small, local targets are attacked precisely because they're easy
> and numerous.**"

> 🎙️ Speaker note: The defensive point — 'we're too small/unskilled a target' is **false**. The tools
> are rented, not built, so attacks are cheap and scalable.

**📊 Depth table — The attacker economy — 2010 vs 2026**

| Dimension | ~2010 attacker | 2026 attacker |
|---|---|---|
| Skill needed | High — had to build tools | Low — rents ready-made kits (RaaS) |
| Where data lives | On-premise servers | Cloud / SaaS platforms (new target) |
| Business model | Lone hobbyist / vandal | Organised gangs with 'customer support' |
| What's for sale | Little | Stolen cards, credentials, KYC in bulk |
| Nepal impact | Rare, opportunistic | Pre-packaged phishing kits target local users |

*ℹ️ The shift matters for defence: attacks are now cheap, scalable, and require little skill — so 'we're too small/unskilled a target for real hackers' is false. The tools are rented, not built.*

#### Concept 3 — Outsourcing & the Supply Chain `[THEORY]` `[~7 min]`

[SLIDE] **A vendor's breach is your breach**

> **Deliver:** **Relying on third-party vendors and contractors introduces THEIR risk into YOUR
> system** — this is **supply-chain risk.** Third-party access, shared credentials, and managed
> services **extend your trust boundary outside your own walls.** And the chain is **deep**: you trust
> your vendor, *and* your vendor's sub-vendors. The rule to remember: **you outsource the WORK, but you
> keep the ACCOUNTABILITY** for protecting your data.

- 🌍 **Global example:** **supply-chain attacks** — a **poisoned software update** from a trusted
  vendor reaching **thousands of customers at once** — show how deep and dangerous the chain is.
- 🇳🇵 **Local example:** **Nepali banks and government offices** routinely **outsource software
  development or hosting** to outside vendors. If that vendor is breached, **the bank's customers** are
  the ones harmed — and the **bank's name** is on the incident.

> ❌ **Misconception:** *"If we outsource IT, we outsource the risk too."*
> ✅ **Correction:** "You outsource the **work**, not the **accountability.** Regulators, customers, and
> the public still hold **YOU** responsible — so vendor security must be **contracted, audited, and
> monitored**, not assumed."

> 🍿 **Fun analogy:** "Outsourcing is **giving a spare house key to a contractor** — convenient, but now
> **their carelessness is your break-in.**"

> 🖼️ Visual: a **supply-chain trust chain** (you → vendor → vendor's sub-vendor) with a **breach arrow
> travelling back** to you.

> 🎙️ Speaker note: Tie to Unit 4's outsourcing ethics — **the duty of care travels with the data.**

**📊 Depth table — Outsourcing scenario → the risk it inherits (Nepal)**

| Outsourcing scenario | Risk inherited | Defence / control |
|---|---|---|
| Bank outsources app development to a vendor | Vendor's insecure code ships into the bank | Security requirements in contract; code review; testing |
| Government hosts a portal with a third party | Host's breach exposes citizen data | Data-protection clauses; audits; encryption |
| Vendor gets remote access to maintain a system | A stolen vendor credential = access to you | Least privilege, MFA, time-limited access, logging |
| Shared admin password given to a contractor | No accountability if it leaks | Unique named accounts; revoke on exit |
| Managed service (SaaS) holds your data | Depend on their uptime & security | Review their certifications; a backup you control |
| Vendor uses its own sub-vendor (deep chain) | Risk you can't even see | Require vendors to vet their sub-vendors |

*ℹ️ The duty of care travels with the data (echoing Unit 4's outsourcing ethics). You outsource the work, not the accountability — a vendor's carelessness is your customers' breach.*

#### 🛠 ACTIVITY — "One new tech, one new risk" `[ACTIVITY]` `[~5 min]`

[SLIDE] **What did your family adopt — and what came with it?**

> **Run it:** In pairs (2 min), name **one new technology** your family or workplace adopted recently;
> list the **new risk** it brought and **one defence.** Take **3–4 answers aloud** (3 min) and sort
> them into **technology / economics / outsourcing** drivers. Close: "Notice **almost nobody added a
> defender** when they added the technology — that's the whole point."

> 🎙️ Speaker note: Seeds — QR payments (fake-QR), smart TV/CCTV (weak default), online banking
> (phishing), records moved to the cloud (access control). Reward a **concrete, matching defence.**

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** The "attack surface" grows mainly because:
a) hackers get smarter b) ✅ **more devices, data, and entry points are added** c) laws change d) prices fall

**MCQ 2.** "Ransomware-as-a-Service" matters because it:
a) is legal b) protects victims c) ✅ **lets low-skill attackers rent powerful tools** d) needs no internet

**Discussion prompt:** *Name one new technology your family adopted recently — what new risk came with it?*

> 🎙️ Speaker note: Draw out — convenience adds doors; crime is now a cheap rented service; outsourcing
> keeps the accountability with you.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** when you **propose a new system at work** — a cloud service, a vendor, an
app — you'll be **expected to ask** *"what new risk does this add, and who now has access to our
data?"* This session **is that habit**: adopt a capability and its **defence together**, never one
without the other.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **New technology** (cloud, mobile, IoT, AI, remote work) **grows the attack surface** — features arrive before their security.
2. **Cybercrime and IT became business models**: RaaS/phishing kits let **low-skill attackers rent power**; **data is a traded commodity.**
3. **Outsourcing extends your trust boundary** — a vendor's breach is **your** breach; you outsource the **work**, not the **accountability.**

**Next session (S24):** turning all this into **measurable risk**, so you can decide what to fix first.

---
---

# S24 — Risks Cybersecurity Mitigates · Risk = Threat × Vulnerability × Impact
**Lecture hour 3 of 6 (Unit 5) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Same virus, two very different nights of sleep"**

> **Deliver (≈2 min):** "**Two laptops.** One holds **wedding photos** with **no internet**; one holds
> a **bank's customer database online.** The **same 'virus' lands on both.**"
>
> **Run the question (≈3 min):** "**Which one keeps you up at night — and can you now say *why*,
> precisely?**" Take answers. Land it: the **same threat** carries **very different risk**, because risk
> is about **more than the threat** — it's threat **and** vulnerability **and** impact.

> 🎙️ Speaker note: The point is to show risk ≠ threat. Agenda: threat vs vulnerability vs asset → the
> risk formula → what security actually mitigates.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Threats, Vulnerabilities & Assets `[THEORY]` `[~8 min]`

[SLIDE] **Three words people confuse**

> **Deliver:** Write all three and their chain on the board.
> - **Threat** = something that **could** cause harm (a worm, a phisher, a flood).
> - **Vulnerability** = a **weakness** it can exploit (unpatched software, a weak password).
> - **Asset** = what has **value** and is being protected (data, money, a service, reputation).
>
> The chain: **a threat actor + a threat exploits a vulnerability to harm an asset.** The key
> consequence: **with no vulnerability, the threat has nothing to land on** — which is *exactly* what
> patching achieves.

- 🌍 **Global example:** an **unpatched server** (vulnerability) + a **worm** (threat) = **mass
  compromise** (e.g. WannaCry).
- 🇳🇵 **Local example:** a **Nepali government site running outdated software** (vulnerability) is
  **repeatedly defaced** (threat realised), harming **citizens' trust** (the asset).

> ❌ **Misconception:** *"Threat and vulnerability are the same thing."*
> ✅ **Correction:** "A **flood is a threat**; **living in a basement is the vulnerability**; **your
> belongings are the asset.** You usually **can't remove the threat** (floods happen), but you **CAN
> remove the vulnerability** (patch, move upstairs) — that's what defence does."

> 🖼️ Visual: **threat actor → threat → exploits a vulnerability → harms an asset**, with a
> **"NO vulnerability ⇒ the threat can't land"** callout.

> 🎙️ Speaker note: Hammer the flood analogy. A threat with no matching vulnerability ≈ harmless.

**📊 Depth table — Threat vs Vulnerability vs Asset**

| Term | What it is | Everyday analogy | Nepal / IT example |
|---|---|---|---|
| Threat | Something that could cause harm | A flood | A worm; a phishing campaign |
| Vulnerability | A weakness it can exploit | Living in a basement | An unpatched government web server |
| Asset | What you're protecting | Your belongings | Citizen data; eSewa balances |
| Threat actor | Who is behind the threat | The storm / a burglar | A criminal gang; an insider |
| Exploit | Threat actually using the weakness | Water entering the basement | The worm compromising the server |

*ℹ️ 'Threat and vulnerability are the same thing' is the classic confusion. A flood (threat) only harms you if you live in a basement (vulnerability) — no weakness, no harm.*

#### Concept 2 — Risk = Threat × Vulnerability × Impact `[THEORY]` `[~9 min]`

[SLIDE] **The formula professionals prioritise with**

> **Deliver:** **Risk is the likelihood × consequence of a threat exploiting a vulnerability** —
> captured as **risk = threat × vulnerability × impact.** The crucial property: **you MULTIPLY, you
> don't add** — so if **any factor is near zero, the risk is low.**
> - **High threat + zero vulnerability ≈ low risk** (nothing to exploit).
> - **Small vulnerability + catastrophic impact ≈ high risk** (worth fixing first).
>
> This is **exactly how professionals prioritise** limited defence budget: rank risks by **likelihood ×
> impact** and defend the **top-right of the matrix first.**

- 🇳🇵 **Local example:** framing the **NIC ASIA SWIFT fraud** incident as **high-impact** (large funds
  moved) explains **why financial systems get the most defence budget** — the impact factor is enormous
  even when likelihood is low.
- 🇳🇵 **Mini case:** "Rank three risks for a campus by **impact**: (a) a **defaced public webpage**,
  (b) **leaked student grades**, (c) a **wiped payroll database.**" Draw out that **(b) and (c)
  outrank (a).**

> ❌ **Misconception:** *"The threat we hear about most is the one to fix first."*
> ✅ **Correction:** "Risk **multiplies** threat, vulnerability, **and** impact. A **loud but low-impact**
> threat can rank **below** a **quiet one with catastrophic impact.** **Fear ranks by headlines;
> professionals rank by likelihood × impact.**"

> 🖼️ Visual: a **risk matrix** (likelihood × impact) with a "risk = T × V × I" formula card.

> 🎙️ Speaker note: Work the campus ranking out loud, then map to the matrix. High-impact financial
> systems get the most defence budget for a reason.

**📊 Depth table — Scoring risk — same threat, different risk (Nepal)**

| Scenario | Threat × Vulnerability × Impact | Risk level (verdict) |
|---|---|---|
| Offline laptop of wedding photos, malware | High × Low (no net) × Low | Low — little to exploit, little lost |
| Online bank customer DB, same malware | High × Medium × Critical | High — huge impact if it lands |
| Defaced public webpage (no data lost) | High × Medium × Low | Medium — embarrassing, limited harm |
| Leaked student grades on a portal | Medium × Medium × High | High — privacy + trust damage |
| Wiped payroll database, no backup | Low × Medium × Critical | High — low odds, catastrophic loss |
| Old test server, no real data | Medium × High × Low | Low — weak, but nothing valuable on it |

*ℹ️ This is why financial systems get the most defence budget: not because they're attacked most, but because their IMPACT is critical. Rank by likelihood × impact and fix the top of the list first.*

#### Concept 3 — What Cybersecurity Actually Mitigates `[THEORY]` `[~8 min]`

[SLIDE] **Reduce risk to acceptable — never zero**

> **Deliver:** State the goal plainly. **Cybersecurity aims to reduce risk to an ACCEPTABLE level, not
> to reach zero.** You attack the formula from **three sides**:
> - **Reduce threat exposure** — don't expose services to the internet needlessly; filter, monitor.
> - **Reduce vulnerability** — patch, strong passwords + MFA, secure configuration.
> - **Reduce impact** — backups, network segmentation, encryption so a breach hurts less.
>
> Whatever is left after all controls is **residual risk** — the leftover you **consciously accept.**

> ❌ **Misconception:** *"Good security means zero risk."*
> ✅ **Correction:** "**Zero risk is impossible** — you manage it **down to acceptable.** Chasing zero
> **wastes budget** and creates **false confidence.**"

> 🍿 **Fun analogy:** "You can't make **crossing the road** risk-free — but a **zebra crossing + looking
> both ways** makes the risk **acceptable.** Same for systems."

> 🎙️ Speaker note: Keep the residual-risk idea explicit — pretending zero risk is achievable is itself
> a security failure.

**📊 Depth table — Each control → which risk factor it reduces**

| Control / practice | Reduces which factor? | Effect (verdict) |
|---|---|---|
| Patching software promptly | Vulnerability | Removes the weakness the threat needs |
| MFA on accounts | Vulnerability | A stolen password alone is no longer enough |
| Tested backups | Impact | Ransomware/wipe hurts far less — you restore |
| Network segmentation | Impact | A breach is contained to one segment |
| Not exposing a service to the internet | Threat exposure | Fewer attackers can even reach it |
| Staff phishing training | Vulnerability (human) | Fewer people click the lure in the first place |
| Encryption of stored data | Impact | A stolen database is unreadable to the thief |

*ℹ️ Defence works the formula from three sides: cut threat exposure, fix vulnerabilities, and limit impact. You can't zero any factor entirely — the leftover is residual risk you consciously accept.*

#### 🛠 ACTIVITY — "Threat, vulnerability, impact for your device" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Name all three for one device you own**

> **Run it:** In pairs (2 min), pick **one device you own**; name **one threat**, **one vulnerability**,
> and the **impact** if compromised. Take **3–4 answers aloud** (3 min); for each, suggest **one
> control** and **which factor it reduces.** Close: "Notice you can rarely remove the **threat** — but
> you can nearly always reduce the **vulnerability** or **impact.**"

> 🎙️ Speaker note: Seed — phone: threat theft/phishing; vulnerability no lock / reused password; impact
> eSewa + photos lost; controls: lock + MFA (vulnerability), backup (impact). Reward correct labelling.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** A weakness that an attack can exploit is a:
a) threat b) ✅ **vulnerability** c) asset d) risk

**MCQ 2.** In risk = threat × vulnerability × impact, patching a flaw mainly reduces the:
a) threat b) impact c) ✅ **vulnerability factor** d) asset value

**Discussion prompt:** *Pick one device you own — name one threat, one vulnerability, and the impact if compromised.*

> 🎙️ Speaker note: Draw out — risk multiplies three factors, and defence usually targets vulnerability
> and impact (not the threat itself).

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** **security budgets — and even exam-grade priorities — are set by risk, not
fear.** This formula is **exactly how professionals decide what to fix first.** Being able to say
*"this is low likelihood but critical impact, so it's a high risk"* is the **language of every risk
register and audit.**

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Threat ≠ vulnerability ≠ asset**: a threat could harm; a vulnerability is the weakness it exploits; the asset is what you protect.
2. **Risk = threat × vulnerability × impact** — factors **multiply**, so a near-zero factor means low risk; rank by **likelihood × impact.**
3. Security reduces risk to **ACCEPTABLE, never zero** — cut exposure, fix vulnerabilities, limit impact; **residual risk remains.**

**Next session (S25):** the **actual attacks** that exploit these vulnerabilities — how to recognise and defend against them.

---
---

# S25 — Common Cyberattacks & Poisoned Web Services (defensive view)
**Lecture hour 4 of 6 (Unit 5) · 50 minutes**

> **Defensive framing (say it again here):** every attack below is described **only to recognise and
> defend** against it. **No attack-execution steps.**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Both want one thing from you"**

> **Deliver (≈2 min):** "An **SMS** says '**Your eSewa/IME is blocked — verify here**' with a link. A
> **pop-up** says '**Your PC has 5 viruses, call this number.**' **Both want one thing from you.**"
>
> **Run the question (≈3 min):** "**Can you name the trick — AND the defence?**" Take answers. Land the
> agenda: **malware → phishing → DoS → poisoned web services**, each **paired with its defence.**

> 🎙️ Speaker note: Set the tone as recognise-and-defend. Agenda on the board with the four families.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Malware: Recognition & Defence `[THEORY]` `[~8 min]`

[SLIDE] **Different malware, overlapping defence**

> **Deliver:** **Malware is malicious software** — **viruses, worms, trojans, ransomware, spyware.**
> Each **behaves differently** (spreads / hides / locks / spies), but the **defences overlap.** Teach
> the behaviours to **recognise** them:
> - **Virus** attaches to files; **worm** spreads by itself; **trojan** hides in something you trust.
> - **Ransomware** locks/encrypts your files for money; **spyware** silently watches and steals.
>
> Warning signs: **sudden slowness, pop-ups, files renamed/locked, unknown processes.** Defences:
> **updates + antivirus/EDR + least privilege + tested backups + careful clicks.**

- 🌍 **Global example:** **WannaCry** ransomware spread worldwide through a **single unpatched Windows
  flaw** — a worm + ransomware combined.
- 🇳🇵 **Local example:** ransomware and malware have hit **Nepali businesses and government offices**,
  and **pirated / cracked software** is a common infection route (the 'free' download carries a trojan).

> ❌ **Misconception:** *"Antivirus alone keeps me safe."*
> ✅ **Correction:** "Antivirus is **one layer.** **Updates** (WannaCry was a missing patch), **tested
> backups** (your ransomware recovery), **least privilege**, and **careful clicks** matter just as much
> — and **pirated software often IS the malware.**"

> 🎙️ Speaker note: Keep it recognition + defence. The unglamorous truth: patch, EDR, least privilege,
> backups beat most malware.

**📊 Depth table — Malware types — behaviour, warning sign & defence**

| Type | How it behaves | Warning sign | Key defence |
|---|---|---|---|
| Virus | Attaches to a file; runs when opened | Files corrupted; odd errors | Antivirus; don't open unknown files |
| Worm | Self-spreads across the network | Network slow; devices infected fast | Patch promptly; segment the network |
| Trojan | Hides inside trusted-looking software | Unexpected behaviour after install | Install only from trusted sources |
| Ransomware | Encrypts files, demands payment | Files locked; ransom note | Tested offline backups; patch; least privilege |
| Spyware | Silently watches, steals data | Battery/data drain; strange activity | Anti-malware; app-permission hygiene |
| Adware / PUP | Floods pop-ups, bundles junk | Constant ads; new toolbars | Careful installs; avoid pirated software |

*ℹ️ Studied for RECOGNITION and DEFENCE only. Notice the defences overlap: updates, antivirus/EDR, least privilege, backups, and careful clicks beat most of them.*

#### Concept 2 — Phishing & Social-Lure Attacks: Recognition & Defence `[THEORY]` `[~9 min]`

[SLIDE] **Phishing hacks the human, not the computer**

> **Deliver:** **Phishing tricks a PERSON into giving credentials, money, or clicks via fake messages.**
> It **targets people, not machines**, so **no firewall fully stops it.** The **signs**: manufactured
> **urgency**, **mismatched or look-alike links**, requests for **OTP/PIN.** The **defences**: **verify
> out-of-band**, **never share an OTP**, use **MFA**, and **report.** Note **spear-phishing** —
> targeted, researched phishing that **fools experts too.**

- 🇳🇵 **Local example:** fake **"eSewa/Khalti reward,"** fake **bank-KYC SMS**, fake **Nepal Police /
  IRD fine** messages, and **look-alike bank URLs** (subtly misspelled).
- 🇳🇵 **Mini case:** "An email **'from your principal'** urgently asks you to **buy gift cards** — list
  **3 red flags.**" Answer: the **urgency**, the **unusual request**, and the **mismatched sender.**

> ❌ **Misconception:** *"Only careless people fall for phishing."*
> ✅ **Correction:** "Well-crafted, **targeted spear-phishing** (researched, personalised, well-timed)
> **fools experts and executives too.** The defence isn't 'be smart', it's a **habit**: pause on
> urgency, verify out-of-band, never share an OTP, and enable **MFA** so a stolen password alone fails."

> 🖼️ Visual: a "**spot-the-phish**" annotated SMS/email highlighting the red flags.

> 🎙️ Speaker note: Localise heavily — students have all received these. Reward naming the **red flag +
> the correct action.**

**📊 Depth table — Nepali phishing lures — the red flag & the defence**

| Lure (Nepal) | Red flag to spot | What you should do |
|---|---|---|
| 'Your eSewa/IME is blocked — verify here' | Urgency + a link asking to log in | Don't click; open the app yourself; report |
| 'You won a Khalti reward — claim now' | Too-good offer + urgency | Ignore; verify in the official app only |
| Fake bank-KYC SMS asking for OTP/PIN | Any request for OTP/PIN | Never share OTP/PIN — banks never ask |
| 'Nepal Police/IRD fine — pay via this link' | Threat + unofficial payment link | Verify through official channels, not the link |
| Look-alike bank URL (subtly misspelled) | Domain slightly wrong (e.g. rn for m) | Type the address yourself; check carefully |
| Email 'from the principal' wanting gift cards | Urgent, unusual request, odd sender | Verify by phone/in person out-of-band |

*ℹ️ Phishing targets the human, so the defence is behavioural: pause on urgency, verify out-of-band, never share OTP/PIN, enable MFA, and report. Well-crafted spear-phishing fools experts too.*

#### Concept 3 — Denial-of-Service (DoS / DDoS): Conceptual `[THEORY]` `[~8 min]`

[SLIDE] **Flood the service so real users can't get in**

> **Deliver (conceptual only):** **A Denial-of-Service attack overwhelms a service with traffic so
> legitimate users can't reach it** — it attacks **Availability.** A **DDoS** is **"distributed"**: the
> flood comes from **many machines (often a botnet) at once**, so you can't simply block one address.
> **There are no traffic-generation instructions here** — the point is recognising the **CIA goal hit
> (Availability)** and the **defences.**
>
> Defences (conceptual): **rate-limiting, CDNs / traffic-scrubbing services, spare capacity**, and
> **coordinating with your ISP and NPCERT** during a sustained attack — you can't absorb a large flood
> alone.

- 🇳🇵 **Local example:** **Nepali bank / government portals knocked offline** during **hacktivist
  campaigns** — nothing stolen or altered, but nobody can use the service.

> 🖼️ Visual: a **DoS flood** — many bots → an overwhelmed server → a legitimate user **blocked.**

> 🎙️ Speaker note: Strictly conceptual. Land that a DoS usually **steals nothing** — it attacks
> **uptime.** That's still serious (a bank offline during a festival is a real harm).

**📊 Depth table — Attack family → CIA goal it hits → defence**

| Attack family | CIA goal it mainly hits | Core defence (paired) |
|---|---|---|
| Malware / ransomware | Availability (+ Confidentiality) | Patch, EDR, least privilege, tested backups |
| Phishing | Confidentiality (stolen creds) | Verify out-of-band, MFA, training, report |
| DoS / DDoS | Availability | Rate-limiting, CDN/scrubbing, capacity, ISP/NPCERT |
| Poisoned / defaced website | Integrity (+ Availability) | Patching, input validation, WAF, monitoring |
| Data theft / spyware | Confidentiality | Encryption, access control, anti-malware |
| Tampering with records | Integrity | Hashing, audit logs, backups, access control |

*ℹ️ This is the map for the whole unit: name the CIA goal an attack hits, then reach for the paired defence. Every attack here is studied to defend against it.*

#### Concept 4 — Poisoned Web-Service & Web-Based Attacks: Recognition & Defence `[THEORY]` `[~7 min]`

[SLIDE] **Even a trusted, HTTPS site can be compromised**

> **Deliver:** **A poisoned web-service attack turns a trusted website or service into a delivery
> vehicle** — **drive-by downloads, malvertising, defacement, or injected malicious content.** The
> unsettling point: **a familiar, HTTPS site can be compromised.** Split the defences:
> - **User defences:** keep **browser/OS updated**, **ad/script hygiene**, **don't ignore warnings.**
> - **Site-owner defences (conceptual):** **input validation, patching, a Web Application Firewall (WAF).**

- 🇳🇵 **Local example:** **defacement of Nepali government websites**; **cloned / fake banking login
  pages** hosted on **poisoned or look-alike sites.**

> ❌ **Misconception:** *"A familiar / HTTPS site is always safe."*
> ✅ **Correction:** "**Trusted sites can be compromised**, and the **padlock only means the connection
> is encrypted** — **not** that the site is genuine or clean. A **cloned phishing site can show a
> padlock too.** Verify the **domain and certificate**; don't treat HTTPS as a safety guarantee."

> 🍿 **Fun analogy:** "A poisoned web service is a **tampered sample at a trusted store** — you trusted
> the **shop**, not the **tampering.**"

> 🎙️ Speaker note: The one-liner to leave them with — **padlock = encrypted, not trustworthy.**

**📊 Depth table — Web-based attack sign → what it is → defence**

| Sign / situation (Nepal) | What it likely is | Defence (paired) |
|---|---|---|
| Govt website shows an attacker's message | Defacement (Integrity hit) | Patching, input validation, WAF, monitoring |
| A trusted site suddenly pushes a download | Drive-by / compromised site | Keep browser/OS updated; don't run it |
| Ads on a normal site trigger scary pop-ups | Malvertising | Ad/script hygiene; ad-blocker; ignore the pop-up |
| A cloned bank login on a look-alike URL | Fake login (credential theft) | Check the domain + certificate; type the address |
| Padlock shown but the site feels wrong | HTTPS ≠ trustworthy | Padlock = encrypted only; verify identity too |
| Form input causes odd server behaviour | Possible injection | Site owner: validate/sanitise input; patch |

*ℹ️ The padlock means the connection is ENCRYPTED, not that the site is TRUSTWORTHY — a poisoned or cloned site can have HTTPS. Trusted sites can be compromised; keep software patched and heed warnings.*

#### 🛠 ACTIVITY — "Share a real scam message" `[ACTIVITY]` `[~5 min]`

[SLIDE] **The lure, the red flags, and what to do**

> **Run it:** In pairs (2 min), share a **real scam SMS/email** you or your family received; identify
> the **lure** and the **red flags.** Take **3–4 examples aloud** (3 min); for each, state **what the
> person should have done.** Close: "Almost every example uses **urgency + a link or an OTP request** —
> the same two tells."

> 🎙️ Speaker note: Expect fake wallet rewards, bank-KYC OTP requests, fake fines, look-alike URLs.
> Reward the **red flag + correct action** (verify out-of-band, never share OTP, report). Keep it
> defensive.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** A message creating urgency to make you click a fake link is:
a) malware b) ✅ **phishing** c) DoS d) a firewall

**MCQ 2.** A DoS attack primarily targets which CIA goal?
a) Confidentiality b) Integrity c) ✅ **Availability** d) authentication

**Discussion prompt:** *Share a real scam SMS/email — what was the lure, and what should the person have done?*

> 🎙️ Speaker note: Reinforce the drill — name the attack, name the CIA goal it hits, name the defence.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** these **four attack families cause the majority of real incidents in Nepal**
— recognising them is your **single highest-value skill** in this unit. If you can **name the trick and
the defence** for a scam SMS, you can protect **yourself, your family, and your future employer.**

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Malware** (virus/worm/trojan/ransomware/spyware) is beaten by **layered defence**: updates + antivirus/EDR + least privilege + backups.
2. **Phishing targets PEOPLE** with urgency and fake links — **verify out-of-band, never share OTP, use MFA, and report.**
3. **DoS attacks Availability** (capacity/filtering/ISP+NPCERT); **poisoned/HTTPS sites can be compromised** — the **padlock ≠ safe.**

**Next session (S26):** attacks that poison the **network** beneath all this — ARP, DNS, and man-in-the-middle.

---
---

# S26 — Network Infrastructure Poisoning · MITM (defensive view)
**Lecture hour 5 of 6 (Unit 5) · 50 minutes**

> **Defensive framing:** conceptual **recognition + countermeasures only** — **no execution steps.**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Or do you?"**

> **Deliver (≈2 min):** "You type **esewa.com.np** and hit your **real login**... **or do you?** What if
> the **'signpost' that points your browser to the right address** was **quietly swapped** — on
> **public café Wi-Fi?**"
>
> **Run the question (≈3 min):** Take a few reactions. Land the agenda: attacks on the **plumbing of
> the network** — **MITM → ARP poisoning → DNS poisoning → why infrastructure attacks are dangerous.**

> 🎙️ Speaker note: Frame as conceptual only. The recurring hero of this session is **encryption.**

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Man-in-the-Middle (MITM): the Idea `[THEORY]` `[~8 min]`

[SLIDE] **A secret relay between you and the server**

> **Deliver:** **In a man-in-the-middle attack, an attacker secretly sits between two parties and can
> READ or ALTER what passes.** Because it can **both eavesdrop and tamper**, MITM breaks
> **Confidentiality AND Integrity.** The classic setting is an **untrusted / public Wi-Fi** network.
> The **universal defence is encryption**: **HTTPS/TLS** and a **VPN**, plus **taking certificate
> warnings seriously.**

- 🌍 **Global example:** **rogue Wi-Fi hotspots** in **airports and cafés** intercepting **unencrypted
  traffic.**
- 🇳🇵 **Local example:** **open Wi-Fi at Kathmandu cafés, the airport, and campuses** is a real MITM
  risk for anyone **checking e-banking.**

> ❌ **Misconception:** *"Public Wi-Fi is fine if it has a password posted on the wall."*
> ✅ **Correction:** "A **shared, known password protects little** against someone **already on the same
> network.** The real protection is **end-to-end encryption (HTTPS/VPN)** and heeding certificate
> warnings — **not** whether the Wi-Fi itself asked for a password."

> 🖼️ Visual: **you — attacker — bank server**, with the attacker **reading/altering** in the middle,
> and a **defence band** (HTTPS/TLS + VPN + heed warnings).

> 🎙️ Speaker note: Encryption makes intercepted traffic **unreadable and un-alterable** — that's why
> it defeats MITM.

**📊 Depth table — Network-poisoning attacks — what each targets & its defence**

| Attack | What it targets | How you might notice | Key defence |
|---|---|---|---|
| MITM | Traffic between two parties | Certificate warnings; odd behaviour | HTTPS/TLS + VPN on untrusted Wi-Fi |
| ARP poisoning | The LOCAL network (LAN) | Hard to see; needs monitoring | Segmentation, DAI, encryption |
| DNS poisoning | Name→address lookup | Right name but cert warnings | DNSSEC, trusted resolver, HTTPS checks |
| Rogue Wi-Fi hotspot | Users on public Wi-Fi | Unexpected/duplicate network name | VPN; avoid sensitive logins on it |

*ℹ️ Conceptual recognition + countermeasures only. The through-line: encryption (HTTPS/VPN) and heeding warnings protect the USER even when the network beneath is compromised.*

#### Concept 2 — ARP Poisoning: What It Is `[THEORY]` `[~7 min]`

[SLIDE] **The LAN trusts address answers blindly**

> **Deliver (conceptual):** **ARP poisoning tricks devices on a LOCAL network into sending their
> traffic to the attacker by faking hardware-address mappings.** The root problem: **the local network
> trusts ARP answers blindly.** This enables **MITM on a LAN.** **There are no spoofing commands here**
> — we focus on the **defences**: **network segmentation, dynamic ARP inspection (DAI), encrypted
> traffic, monitoring.** And crucially: **even on a poisoned LAN, HTTPS/VPN keeps the diverted traffic
> unreadable.**

- 🇳🇵 **Mini case:** "On a **shared office LAN**, why does **encryption (HTTPS/VPN) still protect you**
  even if the LAN is poisoned?" Answer: the attacker sees **only encrypted, useless traffic.**

> 🖼️ Visual: a **switch + devices + gateway**, with an **attacker claiming to be the gateway** and
> traffic **diverted** — plus a **defence band.**

> 🎙️ Speaker note: Keep it conceptual. The reassuring point for users is that **encryption is the
> safety net** even on a compromised LAN.

**📊 Depth table — ARP-poisoning situations → the safe response**

| Situation (defensive framing) | Why it's a risk | Safe response / defence |
|---|---|---|
| Shared office LAN, sensitive logins | LAN trusts ARP replies blindly | Use HTTPS/VPN; segment the network |
| Guest devices on the same LAN as servers | A guest could divert traffic | Separate VLAN for guests |
| Traffic silently rerouted on the LAN | MITM enabled locally | Dynamic ARP inspection (DAI) on switches |
| No monitoring of the local network | Poisoning goes unnoticed | Monitor/alert on ARP anomalies |
| Plaintext (HTTP) service on the LAN | Readable if diverted | Enforce HTTPS/TLS internally too |
| Café/campus Wi-Fi with many strangers | Anyone may be on your segment | VPN; avoid banking on it |

*ℹ️ Framed for defence only — no spoofing steps. The universal user safety net is encryption: a poisoned LAN still can't read or alter HTTPS/VPN traffic.*

#### Concept 3 — DNS Poisoning / Spoofing: What It Is `[THEORY]` `[~8 min]`

[SLIDE] **The phonebook is tampered with**

> **Deliver (conceptual):** **DNS poisoning corrupts the "phonebook" that turns a domain name into an
> address**, so a **correct-looking name leads to a FAKE server.** **Forged or cached DNS answers** send
> users to **look-alike sites.** The **tell for a user is a certificate/security warning**: the **name
> can look right while the destination is wrong.** Defences: **DNSSEC, trusted resolvers**, and **HTTPS
> + certificate checks** (and heeding warnings).

- 🇳🇵 **Local example (threat + detection):** **redirecting users typing a Nepali bank's domain to a
  cloned phishing login** — the address bar shows the **right name**, but the server is **fake.** The
  fake server **can't present a valid certificate** for the real domain, so a **certificate warning**
  appears — that's the tell.

> ❌ **Misconception:** *"If the address bar shows the right name, the site must be real."*
> ✅ **Correction:** "**Poisoned DNS can show the right NAME while pointing at a fake server.** The
> reliable tell is the **certificate**: a fake server **can't present a valid one** for the real domain,
> so a **certificate warning means STOP** — don't type your password."

> 🍿 **Fun analogy:** "DNS poisoning is **tampering with the phone directory** so the **right name lists
> the wrong number.**"

> 🖼️ Visual: **you type esewa.com.np → poisoned phonebook → the FAKE look-alike** (with the real server
> greyed out), plus a **defence band.**

> 🎙️ Speaker note: The certificate warning is the **defence that catches** DNS poisoning — teach
> students to never click through it.

**📊 Depth table — DNS-poisoning signs → what's happening → defence**

| Sign the user sees | What's happening | Defence / safe response |
|---|---|---|
| Right name, but a certificate warning | Sent to a fake server | Stop; don't proceed; heed the warning |
| Bank login looks slightly 'off' | Possible cloned site via poisoned DNS | Close it; type the address; use the app |
| Redirected somewhere unexpected | Forged/cached DNS answer | Use a trusted resolver; check HTTPS cert |
| No padlock / invalid certificate | Fake server can't prove the name | Never enter credentials |
| Different result on mobile data vs Wi-Fi | One resolver may be poisoned | Compare; report to IT/NPCERT |
| Org-wide users hitting a fake site | Cache poisoning at the resolver | DNSSEC + secure resolver at the org level |

*ℹ️ Poisoned DNS shows the RIGHT name while pointing at a FAKE server — so the address bar alone isn't proof. The certificate warning is the tell; DNSSEC and trusted resolvers stop it at the infrastructure level.*

#### Concept 4 — Why Infrastructure Attacks Are Dangerous `[THEORY]` `[~5 min]`

[SLIDE] **Silent, below the app, many users at once**

> **Deliver:** **Attacks on the network's plumbing (ARP, DNS, MITM) are dangerous because they are
> SILENT and hit many users at once, below the application layer** — **the app looks normal while the
> traffic beneath is compromised.** The good news: **one small set of universal user defences works
> across all of them** — **encryption (HTTPS/VPN), heed security warnings, and avoid sensitive logins on
> untrusted networks.** Infrastructure owners add **DNSSEC, DAI, segmentation, and monitoring** on top.

> 🎙️ Speaker note: Tie the whole session together — **three different attacks, one repeated defence.**
> That's the takeaway students must leave with.

**📊 Depth table — One universal defence set → covers all infrastructure attacks**

| Universal user defence | Why it works | Covers |
|---|---|---|
| Use HTTPS/TLS everywhere | Encrypted traffic can't be read or altered | MITM, ARP, DNS (partially) |
| Use a VPN on untrusted Wi-Fi | Wraps all traffic in encryption | MITM, ARP, rogue hotspot |
| Heed certificate/security warnings | The tell that you're on a fake/relayed path | DNS poisoning, MITM |
| Avoid sensitive logins on public Wi-Fi | Removes the exposure entirely | MITM, rogue hotspot |
| Keep the device/browser updated | Closes flaws these attacks lean on | All |
| Owners: DNSSEC, DAI, segmentation, monitoring | Fix it at the infrastructure level | DNS, ARP, MITM |

*ℹ️ The unifying lesson of S26: three different plumbing attacks, ONE repeated user defence — encryption plus heeding warnings — with infrastructure owners hardening DNS/ARP/segmentation underneath.*

#### 🛠 ACTIVITY — "Café Wi-Fi and your e-banking" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Only café Wi-Fi is available — what do you do?**

> **Run it:** In pairs (2 min): you **must check e-banking** and **only café Wi-Fi** is available —
> **what do you do, and why?** List the **risks** (MITM, poisoned DNS) and the **defences.** Take **3–4
> answers aloud** (3 min); rank them **safest → riskiest.** Close: "Safest is **mobile data or wait**;
> if you must, use a **VPN + HTTPS** and **never ignore a certificate warning.**"

> 🎙️ Speaker note: Reward reasoning about **WHY encryption defeats MITM/DNS poisoning**, not just the
> rule.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** An attacker secretly relaying/altering traffic between two parties is performing a:
a) DoS b) ✅ **man-in-the-middle attack** c) phishing d) defacement

**MCQ 2.** The best everyday user defence against MITM on public Wi-Fi is:
a) a longer password b) ✅ **use HTTPS/VPN encryption** c) turn off the screen lock d) delete cookies

**Discussion prompt:** *You must check e-banking and only café Wi-Fi is available — what do you do, and why?*

> 🎙️ Speaker note: Land the through-line — three plumbing attacks, one repeated defence (encryption +
> heeding certificate warnings).

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** as a **future IT manager** you'll set **café-Wi-Fi policy, VPN rules, and
HTTPS enforcement** — these concepts let you **justify those rules to a non-technical boss**
("*encryption is why a poisoned network still can't read our traffic*"). It's the **reasoning**, not
just the rule.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **MITM** = an attacker secretly relaying/altering traffic (breaks **Confidentiality AND Integrity**), common on **public Wi-Fi.**
2. **ARP poisoning** targets the **LOCAL network**; **DNS poisoning** targets **name lookups** (right name, fake server — the **cert warning is the tell**).
3. **Universal defence:** **encryption (HTTPS/VPN)** + **heed security warnings** + **avoid sensitive logins on untrusted networks.**

**Next session (S27):** **who** is behind all these attacks, and why — cyberattackers and their coloured hats.

---
---

# S27 — Cyberattackers and Their Coloured Hats
**Lecture hour 6 of 6 (Unit 5) · 50 minutes — CLOSES UNIT 5**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Criminal, hero, or just a job title?"**

> **Deliver (≈2 min):** "The **same skill** that breaks into a bank can also be **PAID by that bank** to
> break in **first** and **report it.**"
>
> **Run the question (≈3 min):** "So is a **'hacker' a criminal, a hero, or just a job title?**" Take
> answers. Land the theme: **MOTIVE and AUTHORISATION — not skill — define the hat.** Agenda: coloured
> hats → attacker types by motive → why classifying attackers shapes defence.

> 🎙️ Speaker note: The whole session reframes "hacker = criminal." Agenda on the board.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — The Coloured Hats `[THEORY]` `[~7 min]`

[SLIDE] **Authorisation + intent, not skill**

> **Deliver:** **Hackers are classified by INTENT and AUTHORISATION, not by skill.**
> - **White hat** — **authorised and ethical** (a penetration tester, a bug-bounty researcher). **Legal.**
> - **Black hat** — **malicious and illegal.**
> - **Grey hat** — **unauthorised but not (always) malicious** — **still illegal**, because they act
>   **without permission** even if they mean to help.
>
> The same **technical skill** sits behind all three; the hat is about **authorisation + intent.**

- 🌍 **Global example:** **bug-bounty researchers (white)** vs **ransomware operators (black)** — often
  the **same knowledge**, opposite purposes.
- 🇳🇵 **Local example:** Nepali **ethical-hacker / bug-bounty researchers** who **responsibly report
  flaws** in bank/government sites (white) vs attackers who **defaced them** (black).

> ❌ **Misconception:** *"All hackers are criminals."*
> ✅ **Correction:** "The hat is about **authorisation + intent, not skill** — **many hackers are paid
> defenders** (penetration testers, bug-bounty researchers) who **make systems safer.** Skill is
> neutral; **how and why** you use it decides the colour of the hat."

> 🖼️ Visual: a **hats spectrum** (white → grey → black) with **legal · invited / still illegal /
> criminal** labels.

> 🎙️ Speaker note: Stress that a **grey hat still acts illegally** — good intentions don't make it
> authorised.

**📊 Depth table — White vs Grey vs Black hat**

| Dimension | White hat | Grey hat | Black hat |
|---|---|---|---|
| Authorised? | Yes — invited | No | No |
| Intent | Improve security | Mixed / curious | Malicious / criminal |
| Legal? | Legal | Illegal (no permission) | Illegal |
| Typical activity | Pen-test, bug bounty | Unrequested probing, then report | Fraud, ransomware, theft |
| Nepal example | Reports a bank flaw responsibly | Finds a gov flaw uninvited | Defaces / steals data |

*ℹ️ It's about authorisation + intent, not skill. A grey hat may mean well but is still acting illegally by probing without permission — good intentions don't make it authorised.*

#### Concept 2 — Attacker Types by Motive `[THEORY]` `[~9 min]`

[SLIDE] **Motive predicts behaviour**

> **Deliver:** **Different attackers want different things, and motive predicts their behaviour.**
> - **Script kiddies** — **low skill**, use **others' tools**, chase **thrills/notoriety.**
> - **Hacktivists** — **politically/socially motivated** (defacements, leaks, DDoS).
> - **Cybercriminals / organised crime** — **money** (fraud, ransomware, data theft).
> - **State / nation-state actors ("APT")** — **espionage, sabotage, strategic advantage**; **well-resourced and persistent.**
> - **Insiders** — employees/contractors **misusing access** — **malicious OR simply negligent.**

- 🇳🇵 **Local example:** **hacktivist defacements** of Nepali government sites during **regional
  tensions**; **financially-motivated fraud** framed around the **NIC ASIA SWIFT-style** incident;
  **insider misuse** of access at an organisation.
- 🇳🇵 **Mini case:** "A site is **defaced with a political message** and **no money is stolen** — which
  attacker type, and what's their goal?" Answer: a **hacktivist**, whose goal is **attention, not
  profit.**

> ❌ **Misconception:** *"The biggest threat is always an outside genius hacker."*
> ✅ **Correction:** "In reality, **insiders and simple phishing cause a large share of real damage**,
> and much crime uses **rented, unsophisticated tools.** Ranking attackers by **Hollywood image**, not
> by **motive and likelihood**, **misdirects your defences.**"

> 🍿 **Fun analogy:** "Hats and types are like **jersey colours** — **same game**, but you **defend
> differently against each team.**"

> 🖼️ Visual: an **attacker-type table** graphic (type → motive → typical target → key defence).

> 🎙️ Speaker note: Localise each type. Stress that **insiders can be negligent**, not just malicious.

**📊 Depth table — Attacker types — motive, typical target & key defence**

| Attacker type | Motive | Typical target | Key defence |
|---|---|---|---|
| Script kiddie | Thrills, notoriety | Easy, exposed systems | Patch, basic hygiene, MFA |
| Hacktivist | Political / social message | Public gov / high-profile sites | DDoS defence, patching, monitoring |
| Cybercriminal / org. crime | Money | Banks, wallets, personal data | Fraud controls, backups, MFA, monitoring |
| State / nation-state (APT) | Espionage, sabotage | Government, critical infrastructure | Defence-in-depth, threat intel, segmentation |
| Insider (malicious) | Revenge, profit | Own employer's data/systems | Least privilege, logging, separation of duties |
| Insider (negligent) | (none — carelessness) | Accidental exposure | Training, DLP, access reviews |

*ℹ️ Motive predicts target, method, and persistence — so it shapes which defences you prioritise. Note insiders split into malicious AND negligent; both need trust + monitoring controls, not just firewalls.*

#### Concept 3 — Why Classifying Attackers Matters for Defence `[THEORY]` `[~5 min]`

[SLIDE] **Motive shapes where you spend defence**

> **Deliver:** **Motive predicts target, method, and persistence — so knowing WHO you face shapes your
> defence priorities.** A **bank fears organised crime and insiders** most; a **ministry fears state
> actors and hacktivists.** And **insiders need trust + monitoring controls** (least privilege,
> logging, separation of duties), **not just firewalls** — because they're **already inside.** The rule:
> **spend the budget where the real, likely threat is — not on the scariest headline.**

> ❌ **Misconception:** *"Just buy a firewall and you're safe from everyone."*
> ✅ **Correction:** "A firewall stops **outside network attacks** but does little against an **insider
> who already has access** or a **user tricked by phishing.** Different motives need different controls."

> 🎙️ Speaker note: Land that **insiders + phishing**, not a lone genius, cause much of the real damage.

**📊 Depth table — Organisation → top attacker to fear → defence priority (Nepal)**

| Organisation | Top attacker(s) to fear | Defence priority |
|---|---|---|
| Commercial bank | Organised crime + insiders | Fraud controls, least privilege, monitoring, MFA |
| Government ministry | State actors + hacktivists | Defence-in-depth, DDoS defence, threat intel |
| College / campus | Script kiddies + phishing | Patching, MFA, awareness training |
| Fintech / wallet (eSewa-like) | Cybercriminals + insiders | Fraud detection, segregation of duties, backups |
| Hospital | Ransomware crews | Tested backups, segmentation, patching |
| Telecom / ISP | State actors + DDoS crews | Infrastructure hardening, scrubbing, monitoring |

*ℹ️ Motive predicts target and method, so it sets defence priorities. Insiders need trust + monitoring controls (least privilege, logging), not just a firewall — they're already inside.*

#### 🛠 ACTIVITY — "Biggest real risk to a Nepali bank?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Rank the attacker types for a bank**

> **Run it:** In pairs (2 min): which **attacker type** is the biggest **REAL** risk to a **Nepali
> bank** — and **why?** Rank **organised crime, insiders, hacktivists, and state actors** for a bank
> specifically. Take **3–4 answers aloud** (3 min); tie each to the **defence it demands.** Close: "For
> a bank, **organised crime + insiders** usually top the list — and **insiders need monitoring, not just
> a firewall.**"

> 🎙️ Speaker note: Reward reasoning that links **MOTIVE → TARGET → DEFENCE.**

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** A hacker authorised to test a system to improve its security is a:
a) black hat b) grey hat c) ✅ **white hat** d) script kiddie

**MCQ 2.** An employee misusing legitimate access is an:
a) outsider b) ✅ **insider threat** c) hacktivist d) script kiddie

**Discussion prompt:** *Which attacker type is the biggest real risk to a Nepali bank — and why?*

> 🎙️ Speaker note: Land the two big corrections — the hat is **intent + authorisation, not skill**, and
> **insiders/phishing** cause much of the real damage.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** knowing **who** attacks and **why** lets you (and your future employer)
**spend defence budget where the real threats are**, instead of on fear. This **closes Unit 5**: you
now have the **CIA vocabulary**, the **risk formula**, the **attack/defence pairs**, and the **attacker
map.**

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Hats = intent + authorisation, not skill**: white (authorised/ethical), black (malicious/illegal), grey (unauthorised but not always malicious — still illegal).
2. **Attackers range** from **script kiddies** to **hacktivists, cybercriminals, state actors (APT)**, and **insiders** (malicious or negligent).
3. **Motive predicts target and method**, so it **shapes defence** — a bank fears **crime + insiders**; insiders need **trust + monitoring**, not just firewalls.

**Next unit:** from these fundamentals to **personal cybersecurity** — your own devices, accounts, and passwords.

---
---

# 📋 UNIT 5 — END-OF-UNIT QUIZ
*Use as a 15–20 min in-class quiz or a take-home review. All content stays defensive / conceptual — no attack-execution steps. Answer key at the end.*

### Section A — Multiple Choice (1 mark each)
1. Cyberspace is best described as:
   a) only the websites you visit  b) ✅ the whole connected digital domain (networks, systems, data, people)  c) only the internet  d) only social media
2. The three goals of the CIA triad are:
   a) control, identity, access  b) ✅ Confidentiality, Integrity, Availability  c) crime, incident, alert  d) cloud, IoT, AI
3. A ransomware attack that locks files mainly violates:
   a) Confidentiality  b) Integrity  c) ✅ Availability  d) none
4. Ensuring data has not been secretly altered is:
   a) Confidentiality  b) ✅ Integrity  c) Availability  d) authentication
5. The "attack surface" grows mainly because:
   a) hackers get smarter  b) ✅ more devices, data, and entry points are added  c) laws change  d) prices fall
6. "Ransomware-as-a-Service" matters because it:
   a) is legal  b) protects victims  c) ✅ lets low-skill attackers rent powerful tools  d) needs no internet
7. Risk is expressed as:
   a) threat + cost  b) ✅ threat × vulnerability × impact  c) number of attacks  d) team size
8. A weakness that an attack can exploit is a:
   a) threat  b) ✅ vulnerability  c) asset  d) risk
9. A message using urgency and a fake link is phishing; the best everyday defence against MITM on public Wi-Fi is:
   a) a longer password  b) ✅ HTTPS/VPN encryption  c) deleting cookies  d) hiding the SSID
10. A hacker authorised to test a system is a white hat; an employee misusing legitimate access is an:
    a) outsider  b) ✅ insider threat  c) hacktivist  d) script kiddie

### Section B — Short Answer (2 marks each)
11. Define **cybersecurity** and name its **three pillars** (people, process, technology).
12. Explain **each letter of the CIA triad** with **one Nepal example** each.
13. Explain **why outsourcing keeps accountability with you** even though the work is done by a vendor.
14. **State and explain** the risk formula (**risk = threat × vulnerability × impact**), including why it multiplies.
15. **List three defences against phishing.**

### Section C — Applied Case (3 marks each)
16. For a **Nepali bank or campus** scenario, **identify the asset, threat, vulnerability, and impact**, then **propose two controls** and say which risk factor each reduces.
17. Given a described incident — **a poisoned / cloned login page reached via the right-looking address** — **name the likely technique** and the **user-side defence** (and what tell would warn the user).

### Section D — Discussion (open-ended)
18. "**For a Nepali government ministry, rank these attacker types by real-world risk — hacktivists, organised crime, state actors, insiders — and justify your top two.**"

---

### ✅ Answer Key (Section A)
1-b · 2-b · 3-c · 4-b · 5-b · 6-c · 7-b · 8-b · 9-b · 10-b

> **Sections B–D: grade on key terms.** Q11 must give "protecting systems/networks/data from
> unauthorised access, harm, or disruption" + name **people, process, technology** (and ideally the
> weakest-pillar point). Q12 must map **C = secrecy** (e.g. eSewa/KYC not leaked), **I = unaltered**
> (e.g. land records/exam result), **A = usable** (e.g. e-banking online). Q13 must state **you
> outsource the work, not the accountability** — regulators/customers still hold you responsible; the
> duty of care travels with the data. Q14 must give **risk = threat × vulnerability × impact**, note it
> **multiplies** (a near-zero factor → low risk), and that it ranks defences by **likelihood ×
> impact.** Q15 — any three of: **verify out-of-band, never share OTP/PIN, enable MFA, check the
> domain/link, report, be wary of urgency.** Q16 — reward a coherent asset/threat/vulnerability/impact
> set + **two controls tied to the factor they reduce** (e.g. patching → vulnerability, backups →
> impact). Q17 must name **DNS poisoning (or a cloned/poisoned-site / phishing) attack** and the
> **user-side defence** — **check the certificate / heed the warning, type the address, use HTTPS**;
> the tell is a **certificate/security warning.** Q18 — reward students who tie **motive → target →
> defence** and justify **state actors + hacktivists** (or a defended alternative) as a ministry's top
> two, noting insiders need monitoring, not just firewalls.

---

## ✅ Unit 5 complete (full lecturer-ready depth)
The deck is built: **IT246_Unit5.pptx** (94 slides) — diagram-rich, self-contained, and PDF-safe,
carrying all **21 §7A depth tables** (comparison, concrete-example, scaffolding, and payoff) and **11
diagrams** (CIA triad, the five domains, attack-surface growth, supply-chain trust chain,
threat→vulnerability→asset chain, risk matrix, DoS flood, man-in-the-middle relay, DNS-phonebook
tampering, ARP-LAN trust, and the white→black hat spectrum). This Markdown source carries those **same
21 depth tables inline** under each concept, so the source of truth and the deck stay in sync. Every
attack is framed **for defence / awareness only** — there are **no attack-execution recipes** anywhere.
