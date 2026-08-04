# IT 246 — Unit 8: Digital Forensics
### Full Lecturer-Ready Session Material (S38–S44)

**Program:** BIM, 6th Semester · **Unit weight:** 7 lecture hours
**Sessions:** S38–S44 (50 min each) · **Local context:** Nepal / South Asia
**Format:** Markdown — source of truth; the built deck is `IT246_Unit8.pptx` (100 slides), regenerated via `build_unit8_pptx.py` (imports `deckkit.py`); diagrams via `build_unit8_images.py`.

> **How to read this file.** This is written to **carry a full 50 minutes on its own.** Each
> session has **minute markers** `[~X min]`, the actual **explanation to deliver** (prose, not just
> bullets), **worked examples**, a **timed in-class activity**, and lecturer cue cards in
> `> 🎙️` blocks. `[SLIDE]` marks slide-ready blocks; `🖼️` marks diagram cues. Pace tags:
> `[THEORY] [EXAMPLE] [ACTIVITY] [QUIZ]`. Total per session: **5 + 35 + 5 + 3 + 2 = 50 min.**
> **Recurring spine of the whole unit: chain of custody and evidence integrity** (hashing, write
> blockers, documentation) — return to it in every session.

---

## Unit 8 — Learning Outcomes
By the end of this unit, students will be able to:
1. Define digital forensics and explain how the field grew from "computer forensics," including its core principles.
2. Describe the staged forensic process (identification → preservation → collection → examination → analysis → reporting).
3. Explain what counts as digital evidence and describe a forensic lab's setup and tool categories.
4. Explain chain of custody and the techniques that protect evidence integrity (write blockers, hashing, sealed storage).
5. Describe — conceptually — how deleted data is recovered through disk imaging and file carving.
6. Explain mobile forensics: how phone evidence is extracted, its challenges, and app-data sources.
7. Explain the legal admissibility of digital evidence and the state of cyber forensics in Nepal.

---
---

# S38 — Introduction · From Computer Forensics to Digital Forensics
**Lecture hour 1 of 7 (Unit 4) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"One click destroyed the evidence"**

> **Deliver (≈2 min):** A suspect's **laptop is seized in a fraud case.** An officer **"just opens it
> to check"** — and the **case collapses in court.** One click destroyed the evidence.
>
> **Run a quick reaction (≈3 min):** "How can **looking at a file BREAK it?**" Take a few answers.
> Most students assume forensics is "recovering files" or "IT support." Land the surprise: forensics is
> a **disciplined science**, not casual snooping — and merely opening a file **changes** it. Today:
> **what digital forensics is → how the field grew → the core principles.**

> 🎙️ Speaker note: Don't resolve "how did looking break it" yet — that's Concept 3. The hook exists to
> shake the "forensics = data recovery" reflex. Agenda on the board.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — What Is Digital Forensics `[THEORY]` `[~10 min]`

[SLIDE] **Science applied to law — the goal is admissible proof**

> **Deliver:** Give the definition and write it on the board. **Digital forensics is the scientific
> process of identifying, preserving, analysing and presenting digital evidence in a way that is legally
> admissible.** Break the phrase: **forensics = applying science to legal questions**; **"digital" = any
> device that stores or transmits data.** Hammer the key move: the **goal is court-admissible proof —
> not just retrieving a file.** It uses a **repeatable, documented, scientific method** so the result
> can be **defended** under challenge.

- 🌍 **Global example:** the **BTK killer** was caught via **metadata in a Word document** on a floppy
  disk — the hidden data, not the visible text, cracked the case.
- 🇳🇵 **Local example:** the **Nepal Police Cyber Bureau** (established **2018, Bhotahity, Kathmandu**)
  analyses **seized devices** in online-fraud and social-media-abuse cases — preserving, hashing and
  documenting so the evidence survives a courtroom challenge.

> ❌ **Common misconception:** *"Forensics is just data recovery / IT support."*
> ✅ **Correction — say it out loud:** "The **goal is legally admissible proof**, not simply retrieving
> files. Casual recovery that **alters the original** or **skips documentation** destroys the evidential
> value even when the data is found."

> 🎙️ Speaker note: Keep returning to the phrase **science + law → admissible proof.** That frame governs
> the whole unit.

**📊 Depth table — Data recovery vs digital forensics — same file, different discipline**

| Dimension | Plain data recovery | Digital forensics |
|---|---|---|
| Goal | Get the file back | Court-admissible proof |
| Original | May write to / repair it | Never alter — work on a hashed copy |
| Documentation | Optional | Every step logged (chain of custody) |
| Method | Whatever works | Repeatable, defensible, scientific |
| Output | The recovered data | A report a judge can rely on |
| Who uses it | IT support | Cyber Bureau, courts, investigators |

*ℹ️ Forensics is NOT 'IT support that finds files'. The extra discipline — no alteration, full documentation, repeatability — is exactly what makes the result usable in court.*


#### Concept 2 — From Computer Forensics to Digital Forensics `[THEORY]` `[~10 min]`

[SLIDE] **From one PC to phones, cloud, IoT and networks**

> **Deliver:** Tell the history. **"Computer forensics" (1980s–90s)** meant a **single PC, one hard
> disk**, seized and imaged in a lab. Then **networks, email and servers** added **remote and volatile**
> evidence. Today evidence is **mostly on phones and apps**, with **cloud copies elsewhere**, and new
> sources keep arriving — **IoT devices, smart TVs, cars, wearables.** The field broadened into
> **"digital forensics": multi-device, networked, cloud-connected, and mobile-dominant.**

- 🇳🇵 **Local example:** **Nepali cases now hinge far more on Facebook / TikTok / WhatsApp / Viber and
  mobile phones** than on desktop PCs. A single seized smartphone can hold **chats, location history,
  wallet transactions and cloud-linked backups** — the crime scene moved into the pocket.
- 🇳🇵 **Mini case (work it, ≈2 min):** "An old textbook says **'image the hard drive.'** The suspect
  only owns a **smartphone** — what changed?" Draw it out: the **device landscape** did; the method
  must follow the data.

> ❌ **Common misconception:** *"Digital forensics just means examining a computer's hard drive."*
> ✅ **Correction:** "That was the **1990s.** Evidence now lives on **phones, in the cloud, and across
> networks and IoT** — an investigator who only knows disk imaging **misses most of the evidence.**"

> 🖼️ Visual: an **evolution timeline** — computer forensics (single PC) → networks/servers →
> mobile-dominant + cloud → IoT/vehicles.

> 🎙️ Speaker note: Land that **"image the hard drive" is no longer the default.** Follow the data
> wherever it now lives.

**📊 Depth table — How the evidence source shifted — old assumption vs today (Nepal)**

| Case type | Old assumption (computer era) | Today's reality (digital era) |
|---|---|---|
| Online fraud | Desktop PC with account files | eSewa/Khalti + phone + bank app data |
| Harassment / abuse | Emails on a work PC | Facebook, Messenger, TikTok, WhatsApp chats |
| Blackmail / sextortion | Local image files on a disk | Phone gallery + cloud backup + chat apps |
| Financial scam | Spreadsheet on one computer | Mobile wallets, SMS OTPs, CDRs from NTC/Ncell |
| Fake profile / defamation | A single machine's browser history | Social-media accounts hosted abroad (cloud) |
| Data theft by an insider | USB copied at a desk | Cloud sync, personal phone, webmail |

*ℹ️ In Nepal most cases now hinge on phones, apps and cloud — not desktop PCs. 'Image the hard drive' is no longer the default; the investigator must follow the data wherever it now lives.*


#### Concept 3 — Core Principles of Digital Forensics `[THEORY]` `[~10 min]`

[SLIDE] **Don't alter · work on copies · document · custody · repeatability**

> **Deliver:** State the **core principles**: **don't alter the original; work on copies; document
> everything; maintain chain of custody; ensure repeatability.** These echo the **ACPO-style
> principles**: actions taken **must not change the data**; if originals **must** be accessed, the
> person must be **competent** and able to **explain why.** Walk the four operational rules:
> - **Principle 1:** no action should change the evidence (the golden rule).
> - **Principle 2:** if you must access the original, be competent and **record why.**
> - **Principle 3:** keep an **audit trail** — another expert could **repeat your steps.**
> - **Principle 4:** the **lead investigator is responsible** for compliance throughout.

- 🇳🇵 **Local example:** when the Cyber Bureau seizes a phone in a fraud case, an officer who **"just
  opens the gallery to check"** has already **changed timestamps and access records** — violating
  principle 1. The correct move is to **isolate, image, and analyse a hashed copy**, logging every step.

> ❌ **Common misconception:** *"Taking a quick look at the file can't hurt."*
> ✅ **Correction:** "**Opening a file changes access times, can trigger syncs, and breaks the 'don't
> alter the original' principle** — one of the most dangerous things an investigator can do. Look only at
> a **forensic copy**, never the seized original."

> 🍿 **Fun analogy (deliver it):** "A digital crime scene is a **footprint in sand** — **walking over it
> to 'look closer' destroys the very thing you came to capture.** Looking can be destroying."

> 🎙️ Speaker note: These principles are **not bureaucracy** — each keeps the evidence trustworthy.
> Break one and even damning evidence can be **thrown out.**

**📊 Depth table — The core principles — what each means and why it matters**

| Principle | What it means in practice | Why it matters |
|---|---|---|
| Don't alter the original | Use write blockers; never open files on the seized device | A changed byte makes the evidence challengeable |
| Work on copies | Image the device; analyse the hashed image | The sealed original stays pristine for court |
| Document everything | Log who, what, when, why for every action | Undocumented steps can't be defended |
| Chain of custody | Record every handoff of the evidence | A gap suggests possible tampering |
| Repeatability | Another expert can redo your steps & agree | Science, not opinion — this is what convinces a court |
| Competence | Only trained people touch originals | An untrained click can destroy a case |

*ℹ️ These principles are not bureaucracy — each one exists to keep the evidence trustworthy and defensible. Break one and even genuine, damning evidence can be thrown out.*

#### 🛠 ACTIVITY — "Why is a quick look dangerous?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **What changes the moment you open a file?**

> **Run it:** In pairs (2 min), an officer wants to **"just open one file"** on a seized laptop.
> Students list **everything that could change on the device** the moment a file is opened. Take **3–4
> answers aloud** (3 min) and connect each to a **broken core principle.** Seeds: **last-accessed
> timestamps change; auto-sync / cloud upload triggers; antivirus/OS writes; 'recent files' updates; the
> disk hash changes.** Close: **"looking can be destroying — image first, then examine the copy."**

> 🎙️ Speaker note: Each seed breaks **"don't alter the original"** and hands the defence a challenge.
> Reward students who name the principle, not just the symptom.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** The defining goal of digital forensics is:
a) recover deleted files b) ✅ **produce legally admissible evidence** c) fix the device d) back up data

**MCQ 2.** "Computer forensics" grew into "digital forensics" mainly because:
a) PCs got faster b) ✅ **evidence now lives on phones, cloud and networks, not just PCs** c) laws changed d) disks shrank

**Discussion prompt:** *Why is "just take a quick look at the file" one of the most dangerous things an investigator can do?*

> 🎙️ Speaker note: Draw out that opening a file **alters the original** and breaks admissibility — the
> whole discipline is built to prevent exactly that.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** **anyone in IT may one day hold a device that is evidence** — a colleague's
laptop in an HR investigation, a server after a breach, a phone in a dispute. **Knowing not to touch
it — to isolate it and hand it over properly — can make or break a case** and protect **your own
liability.** The instinct to "just check" is exactly the instinct forensics trains out of you.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Digital forensics = science + law** applied to digital evidence; the goal is **legally admissible proof.**
2. The field **expanded far beyond the single PC** — phones, cloud, networks and IoT dominate today.
3. **Core principles:** preserve the original, work on **hashed copies**, document, keep custody, stay repeatable.

**Next session (S39):** the **staged forensic process** that turns a scene into courtroom-ready evidence.

---
---

# S39 — Stages of Digital Forensics
**Lecture hour 2 of 7 (Unit 4) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"One found it; one 'just found it'"**

> **Deliver (≈2 min):** **Two investigators find the same incriminating photo** on a phone. One
> **follows a documented process**; the other **"just found it."** Only one will **hold up in court.**
>
> **Run the question (≈3 min):** "Why?" Take answers. Land it: **process is what makes evidence
> trustworthy** — a photo with no documented, repeatable chain behind it is just an assertion. Today:
> **the process model → walking the six stages → integrity & custody through all of them.**

> 🎙️ Speaker note: The theme is that a **fixed, documented sequence** is what separates evidence from a
> claim. Agenda on the board.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — The Forensic Process Model `[THEORY]` `[~8 min]`

[SLIDE] **A fixed, documented pipeline: scene → courtroom**

> **Deliver:** Define it. **The forensic process is a repeatable, documented sequence from scene to
> courtroom: identification → preservation → collection → examination → analysis → reporting.** It
> follows standard models such as **NIST SP 800-86** (collection, examination, analysis, reporting).
> Stress: it is a **fixed, ordered sequence** — not "poke around and see." Each stage has a **defined
> purpose** and hands a **clean result** to the next, so **different investigators reach the same,
> defensible result.** **Preservation and custody are what make the later analysis usable at all.**

- 🇳🇵 **Local example (preview):** the Cyber Bureau follows this pipeline on every case — the workflow
  is walked in detail in Concept 2.

> ❌ **Common misconception:** *"Analysis is the real work; the rest is just paperwork."*
> ✅ **Correction:** "**Preservation and chain of custody are what make the analysis usable at all** —
> brilliant analysis of **contaminated** evidence is **worthless** in court. The 'paperwork' **is** the
> admissibility."

> 🖼️ Visual: the **six-stage pipeline** with a **chain-of-custody band** running under all stages.

> 🎙️ Speaker note: The order is **deliberate, not decorative.** Stress that the **report** is written
> for a **non-technical judge**, not another engineer.

**📊 Depth table — The six stages — purpose and output of each**

| Stage | What happens | Output handed on |
|---|---|---|
| Identify | Find which devices/accounts/data matter | A list of evidence sources |
| Preserve | Isolate & prevent any change (airplane mode/Faraday) | An unaltered, protected source |
| Collect | Image/seize the evidence; hash it | A verified forensic copy |
| Examine | Extract the relevant data from the copy | Filtered, relevant data |
| Analyse | Interpret it; reconstruct the timeline of events | A reasoned account of what happened |
| Report | Explain it clearly for a non-technical judge | A defensible written report |

*ℹ️ Analysis grabs the attention, but preservation and collection are what make it admissible. The report must convince a judge or lawyer — not another engineer.*


#### Concept 2 — Walking the Stages `[THEORY]` `[~8 min]`

[SLIDE] **Each stage feeds the next — skip one and the rest is poisoned**

> **Deliver:** Walk the pipeline concretely. **Identification** (what devices/data matter) →
> **Preservation** (isolate, prevent change) → **Collection** (image/seize) → **Examination** (extract
> relevant data) → **Analysis** (interpret, reconstruct events) → **Reporting** (clear, defensible, for
> non-technical readers). Key moves: **identify before you touch**; **preserve immediately** (airplane
> mode / Faraday bag stops remote wiping and syncing); **collect by imaging and hashing**, then examine
> and analyse **only the copy.** A **skipped stage silently poisons everything after it.**

- 🇳🇵 **Local example:** a **Cyber Bureau workflow for a cyberbullying complaint** — **identify** the
  account/phone, **preserve** by isolating the device, **image** it, **examine** the messages, **analyse**
  the timeline, and **report** for the prosecutor.
- 🇳🇵 **Mini case (work it, ≈2 min):** "Investigators **skip preservation** and let the phone keep
  **syncing** — overnight, the cloud **deletes the key chat.** What stage failed?" (**Preservation.**)

> ❌ **Common misconception:** *"We can always go back and re-collect if we miss something."*
> ✅ **Correction:** "**Volatile evidence** (RAM, live syncs, cloud-deletable chats) can vanish
> **permanently within minutes.** Preservation is a **one-shot chance** — you cannot re-collect what has
> been overwritten or wiped."

> 🎙️ Speaker note: Errors **compound downstream.** A preservation failure **can't be fixed** by
> brilliant analysis — that's why it's the case-ending stage.

**📊 Depth table — What goes wrong when a stage is skipped (Nepal cases)**

| Stage skipped / done badly | What happens | Consequence (verdict) |
|---|---|---|
| Identification | Miss the suspect's second phone | Key evidence never collected — case weakened |
| Preservation | Phone left online; cloud deletes the chat overnight | Irreplaceable evidence lost — preservation failed |
| Collection | Copy files by hand instead of imaging | No hash, no slack space — challengeable & incomplete |
| Examination | Analyst wades through everything unfiltered | Slow, error-prone; may miss the relevant data |
| Analysis | Report a chat with no timeline/context | A judge can't see what actually happened |
| Reporting | Hand the court a raw technical dump | Non-technical judge can't use it — impact lost |

*ℹ️ Errors compound downstream: a preservation failure can't be fixed by brilliant analysis. The single most case-ending skip is usually preservation — lost data can't be re-collected.*


#### Concept 3 — Integrity & Chain of Custody Run Through Every Stage `[THEORY]` `[~7 min]`

[SLIDE] **Integrity is a band under all stages, not a final checkbox**

> **Deliver:** Make the spine explicit. **Chain of custody and integrity thread through all six
> stages:** **documentation, hashing at collection, sealed evidence bags, and a custody log.** Every
> **handoff is recorded**; any **gap** becomes a **challenge in court.** Integrity is **not a stage — it
> is a band under all stages.** Operationally: **hash at collection** and **re-hash later** to prove
> nothing changed; **seal and label** evidence; **store in a locked, access-controlled place**; **log
> every transfer** (who, when, why, how). **A single unexplained gap can make the whole exhibit
> inadmissible.**

- 🇳🇵 **Local example:** in a Nepali fraud case, the Cyber Bureau **tags and seals** the phone, **hashes
  the image at collection**, **logs every handoff** to the lab and back, and **cites those hashes in the
  report.** If challenged, the expert can show the analysed copy **still matches the seized original
  bit-for-bit.**

> ❌ **Common misconception:** *"Chain of custody is just bureaucratic paperwork."*
> ✅ **Correction:** "It is the **proof the evidence wasn't tampered with** — without it, even perfect
> data is **worthless** in court. The **log and the hashes** are what let the evidence be **believed at
> all.**"

> 🍿 **Fun analogy (deliver it):** "Chain of custody is a **relay-race baton** — **every handoff is
> recorded**, and **dropping it (a gap in custody) disqualifies the team.**"

> 🎙️ Speaker note: Integrity is **continuous**, not a **final checkbox.** The custody log **plus**
> matching hashes are what let an expert **testify credibly.**

**📊 Depth table — How integrity is maintained at each stage**

| Stage | Integrity action taken | Why it protects the case |
|---|---|---|
| Preservation | Seal in a labelled, tamper-evident bag | Proves no one accessed it in transit |
| Collection | Compute a SHA-256 hash of the image | Later re-hash proves the copy is unchanged |
| Storage | Lock in an access-controlled evidence locker | Limits who could have tampered |
| Every handoff | Sign the custody log (who/when/why/how) | No gap for the defence to exploit |
| Examination | Work only on the hashed copy, never the original | The sealed original stays court-ready |
| Reporting | Cite hashes & custody log in the report | Shows the court the evidence is trustworthy |

*ℹ️ Integrity is continuous, not a final checkbox. The custody log plus matching hashes are what let an expert testify, credibly, that the evidence is exactly what was seized.*

#### 🛠 ACTIVITY — "Order the stages" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Put the six stages in order — and say what each produces**

> **Run it:** In pairs (2 min), give students the **six stages shuffled** to put in the **correct
> order**, writing **one sentence per stage** on what it **produces** for the next. Take answers aloud (3
> min); **fix any that swap collection/examination.** Correct order: **identify → preserve → collect →
> examine → analyse → report.** Close: point to the **one stage that, if skipped, most often destroys a
> case — preservation.**

> 🎙️ Speaker note: The common error is **merging collection and examination.** Draw out that
> **preservation** is the **one-shot, case-ending** stage.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** Which is the correct order of the forensic process?
a) collect→identify→report b) ✅ **identify→preserve→collect→examine→analyse→report** c) analyse→collect→report d) report→collect

**MCQ 2.** The forensic report must be written primarily for:
a) other engineers b) ✅ **a non-technical audience such as a judge/lawyer** c) the suspect d) the media

**Discussion prompt:** *Which single stage, if skipped, most often destroys a case — and why?*

> 🎙️ Speaker note: Land that **preservation** is usually the case-ending skip — **lost volatile
> evidence cannot be re-collected.**

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** the **same disciplined-process thinking applies to incident response in any
company breach**, not just police work. When your systems are hacked, a **clean, documented process** —
identify what's affected, preserve logs before they rotate, collect images, analyse, report — is what
turns a panicked mess into a **defensible account** for management, insurers, and possibly a court.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. Forensics follows a **fixed, documented sequence:** identify → preserve → collect → examine → analyse → report.
2. **Preservation protects everything downstream**; a **skipped stage silently poisons** the rest.
3. **Integrity and chain of custody thread through all six stages** — a continuous band, not a final checkbox.

**Next session (S40):** what actually counts as **digital evidence**, and the **lab** that handles it.

---
---

# S40 — Role of Digital Evidence · Methods and the Forensic Lab
**Lecture hour 3 of 7 (Unit 4) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Which of these convicted someone? All of them."**

> **Deliver (≈2 min):** "**A deleted message, a GPS log, a thumbnail cache, a router log** — which of
> these **convicted someone?** **All of them have.**"
>
> **Run the question (≈3 min):** "**What turns ordinary data into evidence?**" Take answers. Land that
> **evidence is defined by its properties and its handling**, not by how dramatic it looks. Today: **what
> counts as digital evidence → methods & tools → the forensic lab.**

> 🎙️ Speaker note: The point of the hook is that **the humble log/cache is often the decisive
> evidence** — and that what makes it "evidence" is admissibility, not drama.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — What Counts as Digital Evidence `[THEORY]` `[~10 min]`

[SLIDE] **Data that supports/refutes a fact — with five properties**

> **Deliver:** Define it. **Digital evidence is any data stored or transmitted in digital form that can
> support or refute a fact in a case.** List the **types** — files/documents, metadata, logs,
> chats/email, images/video, location data, deleted/residual data. Then the **five properties of good
> evidence: admissible, authentic, complete, reliable, believable.** Stress two things: evidence can be
> **visible (a chat) or hidden (metadata, a thumbnail cache, a log)**; and **encryption is NOT a required
> property** — it's how you **protect** evidence, not what **makes** it evidence.

- 🌍 **Global example:** **location / cell-tower and search-history evidence** has been decisive in major
  criminal trials.
- 🇳🇵 **Local example:** **chat screenshots, call detail records (CDRs) from NTC/Ncell, and mobile
  photos/metadata** are used in Nepali fraud and harassment cases — but only the **forensically extracted
  originals** carry the authenticity a court needs. **A CDR from the telco is far stronger than a phone
  screenshot.**

> ❌ **Common misconception:** *"A screenshot is solid proof."*
> ✅ **Correction:** "**Screenshots are easily faked and lack metadata**, so they are **weak** on their
> own. They become strong only when **backed by a forensically extracted original** (the actual message
> record, with metadata and a chain of custody)."

> 🖼️ Visual: a **"types of digital evidence" map** radiating from a central node.

> 🎙️ Speaker note: Much of the **strongest evidence is hidden** (metadata, logs, deleted residue) — the
> reason imaging captures the **whole device**, not just the visible screen.

**📊 Depth table — Types of digital evidence — where it lives and what it proves**

| Type | Where it lives | What it can prove (Nepal example) |
|---|---|---|
| Files / documents | Disk, phone, cloud | A forged invoice in a fraud case |
| Metadata | Inside the file (author, timestamps, GPS) | When/where a photo was really taken |
| Logs | System, router, server, app | Which account logged in, and when |
| Chats / email | App databases, mail servers | A blackmail or harassment conversation |
| Location / GPS | Phone, app history, CDRs (NTC/Ncell) | A suspect's movements at a key time |
| Deleted / residual | Slack & unallocated space | Data a suspect tried to destroy |

*ℹ️ Much of the strongest evidence is hidden (metadata, logs, deleted residue) — not the obvious visible file. That is why forensic imaging captures the whole device, not just what's on screen.*


#### Concept 2 — Methods & Tools Overview `[THEORY]` `[~10 min]`

[SLIDE] **Method over brand — a free tool used well is valid**

> **Deliver:** Name the **standard methods** — **imaging, hashing, keyword search, and timeline/artifact
> analysis** — and the **tool categories**: **imaging tools, write blockers, analysis suites, and mobile
> tools.** Introduce tools **by category, not deep use:** **Autopsy / The Sleuth Kit** (open source);
> **EnCase, FTK** (commercial analysis suites); **Cellebrite** (mobile). Land the key point: **the
> methodology matters far more than the brand** — a **valid method with a free tool beats a sloppy method
> with an expensive one.**

- 🇳🇵 **Mini case (work it, ≈2 min):** "A team has **only free tools (Autopsy)** and a **tight budget** —
  can they still do **valid** forensics?" (**Yes** — **methodology** matters more than brand;
  admissibility rests on write-blocked imaging, hashing, documentation, repeatability.)

> ❌ **Common misconception:** *"Real forensics needs expensive commercial software."*
> ✅ **Correction:** "**Admissibility depends on sound, documented, repeatable methodology** — not the
> price of the tool. A **free tool used with discipline** is **just as admissible** as a costly one used
> sloppily."

> 🎙️ Speaker note: Know the tools **by category.** A court cares that the **method** is sound and
> repeatable, not which brand's logo is on the screen.

**📊 Depth table — Forensic tool → what it is used for**

| Tool / category | What it does | Open / commercial |
|---|---|---|
| Write blocker | Read a drive while blocking any write | Hardware or software |
| Imaging tool (dd, FTK Imager) | Make a bit-for-bit forensic copy | Free & commercial |
| Autopsy / The Sleuth Kit | Analyse disk images, timelines, carving | Open source (free) |
| EnCase | Commercial analysis suite, court-tested | Commercial |
| FTK | Commercial analysis & indexing suite | Commercial |
| Cellebrite / mobile kit | Extract data from phones & SIMs | Commercial |

*ℹ️ Know these by CATEGORY, not deep operation. A court cares that the method is sound, documented and repeatable — not which brand's logo is on the tool.*


#### Concept 3 — The Forensic Lab `[THEORY]` `[~7 min]`

[SLIDE] **A "clean room for truth"**

> **Deliver:** Define it. **A forensic lab is a controlled environment ensuring integrity, security and
> accreditation.** It needs **physical security, access control, evidence storage/lockers, isolated
> (air-gapped) analysis machines, thorough documentation, and ideally accreditation such as ISO/IEC
> 17025.** Explain each: access control narrows **who could contaminate**; locked lockers keep exhibits
> **sealed and logged**; **air-gapped** machines stop **malware, remote wiping, and contamination**;
> accreditation **signals the lab's results are trustworthy.**

- 🇳🇵 **Local example:** the **Nepal Police Cyber Bureau** runs the **central forensic lab**; many
  **district-level investigations lack lab access** entirely — a real capacity gap that pushes work back
  to the Bureau and **slows cases.**

> ❌ **Common misconception:** *"Any IT technician with a good PC can do forensic analysis."*
> ✅ **Correction:** "Without a **controlled lab** — access control, sealed storage, air-gapped machines,
> accreditation — the evidence can be **contaminated or challenged.** The **environment is part of the
> integrity**, not an optional extra."

> 🍿 **Fun analogy (deliver it):** "A forensic lab is a **'clean room for truth'**: just as a **hospital
> lab avoids contaminating a blood sample**, the forensic lab **avoids contaminating the data.**"

> 🖼️ Visual: a **forensic-lab floor-plan** sketch — locked evidence store, isolated workstation, entry
> log.

> 🎙️ Speaker note: Contrast the **Cyber Bureau lab** with a **district thana** that has **no lab access
> at all** — the capacity gap is the real Nepali constraint.

**📊 Depth table — What a forensic lab needs — and why**

| Lab feature | What it provides | Why it matters |
|---|---|---|
| Physical security | Locked, monitored premises | Stops unauthorised access to evidence |
| Access control | Only trained staff enter | Narrows who could contaminate/tamper |
| Evidence lockers | Sealed, logged storage | Preserves chain of custody |
| Air-gapped machines | Analysis PCs off the network | No malware, remote wipe, or contamination |
| Documentation | Full records of every action | Repeatability & defensibility |
| ISO/IEC 17025 | Accreditation of competence | Court trust in the lab's results |

*ℹ️ Nepal's Cyber Bureau runs the central lab; many district-level investigations lack lab access entirely — a real capacity gap that pushes work back to the Bureau and slows cases.*

#### 🛠 ACTIVITY — "Screenshot vs extracted original" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Why is a screenshot weak — and what does extraction add?**

> **Run it:** In pairs (2 min), a complainant brings a **chat screenshot.** Students list **why it is
> weak evidence** on its own, then list **what a forensic extraction adds** that a screenshot lacks. Take
> **3–4 answers aloud** (3 min). Close: **name the five properties of good evidence and check the
> screenshot against them.** Screenshot weaknesses: **easily edited, no metadata, no proof of source/time,
> no chain of custody.** Extraction adds the **original record, metadata, hashes and a custody log** —
> moving it from "believable maybe" to **authentic/reliable.**

> 🎙️ Speaker note: Tie every weakness to a **property** it fails (authentic, reliable). The lesson: the
> extraction and custody **supply** the properties the screenshot lacks.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** Which property is NOT required of good digital evidence?
a) authentic b) complete c) reliable d) ✅ **that it be encrypted**

**MCQ 2.** A bare screenshot is considered weak evidence mainly because:
a) it's too large b) ✅ **it can be faked and lacks original metadata** c) it's in colour d) courts ban images

**Discussion prompt:** *Why might a free tool like Autopsy be just as admissible as expensive commercial software?*

> 🎙️ Speaker note: Land that **admissibility rests on method** (imaging, hashing, documentation,
> repeatability), **not** on the tool's brand or price.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** understanding **evidence quality** helps **you, as a future IT professional,
log and preserve data correctly** when something goes wrong on your own systems. The **good logs you set
up today** are the **evidence you'll need tomorrow** — and knowing that a **screenshot is weak** stops
you from relying on flimsy proof in an incident.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Digital evidence** = data that supports/refutes a fact; **good evidence** is admissible, authentic, complete, reliable, believable.
2. **Methods** (imaging, hashing, keyword search, timeline analysis) and **tools** matter **by category** — **method beats brand.**
3. A **forensic lab** (access control, sealed storage, air-gapped machines, accreditation) keeps evidence **uncontaminated.**

**Next session (S41):** how to **collect, seize and protect** evidence without altering it.

---
---

# S41 — Collecting, Seizing and Protecting Evidence
**Lecture hour 4 of 7 (Unit 4) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"On? Off? Either choice can destroy evidence."**

> **Deliver (≈2 min):** "A phone is seized **still switched on, screen unlocked, connected to Wi-Fi.**
> Do you **turn it off? Leave it on?** **Either choice can destroy evidence.**"
>
> **Run the question (≈3 min):** "**What's the rule?**" Take answers. Hold the tension — this session is
> the **unit's spine: integrity.** Today: **chain of custody → seizing devices correctly (order of
> volatility) → write blockers & hashing.**

> 🎙️ Speaker note: Don't resolve the on/off dilemma yet — it's Concept 2 (**isolate first**, then decide
> deliberately). Agenda on the board.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Chain of Custody — the Unit's Spine `[THEORY]` `[~10 min]`

[SLIDE] **An unbroken, logged handoff from seizure to court**

> **Deliver:** Define it. **Chain of custody is the documented, unbroken record of who handled evidence,
> when, why and how — from seizure to court.** Mechanics: **every transfer is logged; evidence is sealed
> in labelled tamper-evident bags with a custody form; any gap becomes a challenge in court.** The
> **custody form travels with the exhibit** through the whole journey, and an **unexplained gap** lets the
> defence argue the evidence was **tampered with.**

- 🌍 **Global example:** evidence **thrown out** because a **custody gap could not be explained.**
- 🇳🇵 **Local example:** the Cyber Bureau **tags, seals and logs** a device before transport. The
  **weakness appears earlier** — an **untrained officer at a local thana** who **seizes a phone without
  tagging or logging it** creates a **custody gap** that can sink an otherwise strong case.

> ❌ **Common misconception:** *"Chain of custody is just bureaucratic paperwork."*
> ✅ **Correction:** "It is the **proof the evidence wasn't tampered with** — without it, **even perfect
> data is worthless.** A single **unexplained gap** can make **damning evidence inadmissible.**"

> 🖼️ Visual: a **chain-of-custody handoff chain** — seizure → transport → lab intake → analyst →
> storage → court, each recording **who / when / why / how.**

> 🎙️ Speaker note: The relay-baton idea from S39 returns here — **every handoff signed.** A **complete
> log is the proof of integrity.**

**📊 Depth table — A chain-of-custody log — what each entry records**

| Log field | What it captures | Why the court needs it |
|---|---|---|
| Who | Every person who held the exhibit | Names each link in the chain |
| When | Date & time of each transfer | Shows no unexplained time gaps |
| Why | Reason for the handoff | Justifies each access to the evidence |
| How | Sealed bag, hash, transport method | Proves it couldn't be altered in transit |
| Seal / label | Tamper-evident bag & unique ID | Any broken seal is immediately visible |
| Signature | Sign-off at each handoff | Makes each person accountable |

*ℹ️ A complete log is the proof of integrity. In Nepal, untrained officers seizing phones at a local thana without tagging/sealing/logging is a common weakness that hands the defence an easy challenge.*


#### Concept 2 — Seizing Devices Correctly (Order of Volatility) `[THEORY]` `[~8 min]`

[SLIDE] **Photograph · isolate · capture the most fragile data first**

> **Deliver:** Define it. **Seizing correctly means capturing a device in a state that preserves its
> data.** The moves: **photograph the scene and screen**; **decide power-on vs power-off** (live RAM data
> vs remote-wipe risk); **isolate from networks (Faraday bag / airplane mode)** to stop remote wiping and
> syncing; and follow the **order of volatility — capture the most fragile data first.** Volatility order:
> **RAM and live connections vanish first → disk survives longer → backups longest.** **Power-off can
> re-lock an encrypted disk; power-on risks a remote wipe — decide deliberately.**

- 🇳🇵 **Mini case (work it, ≈2 min):** "An officer **powers down a running laptop with full-disk
  encryption** — the disk **re-locks** and the **password is unknown.** What was lost?" (**The
  live-acquisition opportunity** — capturing the decrypted data and RAM while it was unlocked.)

> ❌ **Common misconception:** *"Always switch a seized device off to be safe."*
> ✅ **Correction:** "**Powering down destroys volatile RAM evidence and can re-lock an encrypted disk**
> you'll never get back into. Power decisions must be **deliberate** — **isolate from networks first**
> (Faraday/airplane mode), then choose based on **encryption and what's running.**"

> 🖼️ Visual: an **order-of-volatility ladder** — CPU cache → RAM → network state → disk → backups —
> with "collect in this order."

> 🎙️ Speaker note: The on/off answer to the hook: **isolate first**, then decide power state based on
> **encryption** and **live data.** Never power down reflexively.

**📊 Depth table — Seizure decisions — what's at stake either way**

| Situation at the scene | Wrong move | Right move (why) |
|---|---|---|
| Laptop on, full-disk encryption unlocked | Power it off → disk re-locks | Live-acquire RAM/keys first, then image |
| Phone on, connected to Wi-Fi | Leave it online | Airplane mode / Faraday bag → stop remote wipe |
| Suspect's screen shows an open app | Close it 'to be tidy' | Photograph it first — that state is evidence |
| Running processes / network connections | Ignore (grab disk only) | Capture RAM first — most volatile |
| Device warm, possibly syncing to cloud | Wait and finish paperwork | Isolate now — cloud may delete the chat |
| USB/SD card in the device | Forget it | Log, seize and image it too |

*ℹ️ Order of volatility: RAM and live network state vanish first, disk survives longer, backups longest. Powering down first can destroy live evidence AND re-lock an encrypted disk — decide power state deliberately.*


#### Concept 3 — Protecting Integrity — Write Blockers & Hashing `[THEORY]` `[~8 min]`

[SLIDE] **A one-way valve and a tamper-evident seal**

> **Deliver:** Define both. **A write blocker is hardware/software that lets you read a drive but blocks
> any write to it.** **Hashing (MD5/SHA-256) is a digital fingerprint proving data is unchanged.** The
> workflow: **hash the original at collection and hash the copy — matching hashes prove the image is an
> identical, untouched duplicate**, while the **write blocker guarantees the original is never modified
> during imaging.** Land it: **change one byte and the hash changes visibly — tampering is detectable.**

- 🇳🇵 **Local example:** in a **Nepali court**, a forensic expert **demonstrates identical SHA-256
  hashes** for the seized original and the analysed copy — **visual proof** the copy is an **exact,
  unaltered duplicate.** A write blocker ensured the original was **never written to** while that image
  was made.

> ❌ **Common misconception:** *"If the analyst is careful, hashing and write blockers aren't really
> needed."*
> ✅ **Correction:** "**Care is not proof.** Only a **write blocker** guarantees the original wasn't
> altered, and only a **matching hash** proves it to a court — **'trust me, I was careful' is not
> defensible evidence.**"

> 🍿 **Fun analogy (deliver it):** "A hash is like a **tamper-evident seal on a medicine bottle** — if
> even **one byte changes**, the **seal (hash) visibly breaks.**"

> 🖼️ Visual: a **write-blocker** diagram (one-way arrow drive→analyst) plus a **before/after hash-match**
> graphic.

> 🎙️ Speaker note: They **work together** — the write blocker **prevents** alteration during imaging; the
> hash **proves** the copy still equals the original. **Neither alone is enough.**

**📊 Depth table — Write blocker vs hashing — two different integrity guards**

| Question | Write blocker | Hashing (MD5/SHA-256) |
|---|---|---|
| What it is | Hardware/software that blocks writes | A mathematical fingerprint of the data |
| When used | During imaging of the original | At collection, then re-checked later |
| Protects against | Accidentally altering the original | Undetected change to the copy |
| Proves | The original was never written to | The copy is identical, bit-for-bit |
| Analogy | A one-way valve | A tamper-evident seal on a bottle |
| If it fails | The original could be altered | A mismatch flags tampering/corruption |

*ℹ️ They work together: the write blocker prevents alteration during imaging; the hash proves, afterwards and in court, that the copy still equals the original. Neither alone is enough.*

#### 🛠 ACTIVITY — "A minute online — what could go wrong?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **A seized phone left online 'just for a minute'**

> **Run it:** In pairs (2 min), a seized phone is **left connected to the internet "just for a
> minute."** Students **list everything that could go wrong** in that minute. Take **3–4 answers aloud**
> (3 min) and **sort them** into **remote-wipe, sync/delete, and tamper.** Close: **"this is exactly why
> isolation (Faraday / airplane mode) is the first protective step."** Seeds: **remote wipe triggered;
> cloud deletes/edits a chat; new messages overwrite old ones; location updates; someone signs the
> account out** — each **irreversible.**

> 🎙️ Speaker note: Every seed is **irreversible** — the reason to **isolate immediately** at seizure.
> Connect back to Concept 2's order of volatility.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** The purpose of a write blocker is to:
a) speed up copying b) ✅ **allow reading a drive while preventing any change to it** c) encrypt the disk d) delete data

**MCQ 2.** Identical hash values of the original and the copy prove that:
a) the data is encrypted b) ✅ **the copy is an exact, unaltered duplicate** c) the drive is empty d) nothing

**Discussion prompt:** *A seized phone is left connected to the internet "just for a minute." List everything that could go wrong.*

> 🎙️ Speaker note: Draw out that **isolation is the first protective step** and that **write blocker +
> hash together** are the **technical proof of integrity.**

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** the **same hashing idea verifies the downloads and backups you use daily**
(a checksum that confirms a file wasn't corrupted or swapped), and a **custody mindset** protects **you**
whenever you handle **sensitive company data** — logging who touched what, and keeping originals
untouched, is exactly the habit that keeps you defensible if a dispute arises.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Chain of custody is the proof of integrity** — an unbroken, logged handoff — **not mere paperwork.**
2. **Seize devices without altering them:** photograph, **isolate networks**, follow order of volatility, decide power carefully.
3. **Write blockers + hashing** guarantee and **prove** the original is **untouched** and the copy is **identical.**

**Next session (S42):** how investigators **recover data** that someone tried to delete.

---
---

# S42 — Recovering Data (conceptual)
**Lecture hour 5 of 7 (Unit 4) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Deleted everything — recovered in an hour"**

> **Deliver (≈2 min):** "A suspect **'deletes everything'** and **empties the recycle bin**, confident
> it's gone. Investigators **recover it in an hour.**"
>
> **Run the question (≈3 min):** "**Where was it hiding?**" Take answers. Land the theme: **deletion ≠
> erasure.** Today: **why 'deleted' isn't gone → disk imaging → file carving.**

> 🎙️ Speaker note: Most students believe deleting/emptying-the-bin erases data. **Hold the surprise** —
> resolve it in Concept 1.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Why "Deleted" Isn't Gone `[THEORY]` `[~10 min]`

[SLIDE] **Delete removes the label, not the box**

> **Deliver:** Explain the mechanism. **Deleting a file usually removes the pointer/index entry, not the
> actual data — the bytes stay until overwritten.** The file system just **marks that space as "free"**;
> until it's **reused**, the data **remains recoverable.** So a **quick format or empty-recycle-bin leaves
> most data recoverable**; **only overwriting or a secure wipe truly destroys it.** Add the nuance: **SSD
> TRIM and full-disk encryption complicate recovery** — a useful real-world caveat.

- 🌍 **Global example:** criminal cases solved by **recovering "deleted" emails and images.**
- 🇳🇵 **Local relevance:** in Nepali cases, suspects who "delete everything" are **routinely undone** —
  until the space is overwritten, the bytes remain. The **same fact** means a **resold, factory-reset
  phone can still leak the previous owner's photos.**

> ❌ **Common misconception:** *"Emptying the recycle bin / formatting permanently destroys data."*
> ✅ **Correction:** "A **quick format and a delete leave most data recoverable** — **only overwriting,
> secure-wiping, or destroying the disk (or its encryption key) truly erases it.**"

> 🍿 **Fun analogy (deliver it):** "'Delete' **removes the label from the box, not the box** — the data
> **stays until something overwrites it.**"

> 🖼️ Visual: a **"delete = remove label, keep box"** diagram.

> 🎙️ Speaker note: This is the **misconception-first** concept — state the wrong belief loudly, then
> correct it with the pointer-vs-data mechanism.

**📊 Depth table — Does this really destroy the data? (Nepal / IT)**

| Action taken | Really destroyed? | Why (verdict) |
|---|---|---|
| Delete a file & empty the recycle bin | No | Only the pointer is gone; bytes remain |
| Quick format a USB drive | No | Rebuilds the index; most data still recoverable |
| Factory reset an old phone (then sell it) | Often no | Traces + cloud backup can remain → data leak |
| Overwrite the whole drive (secure wipe) | Yes | Every byte is replaced — nothing to recover |
| Physically destroy / shred the disk | Yes | No medium left to read |
| Full-disk encryption + destroy the key | Effectively yes | Data is unreadable without the key |

*ℹ️ 'Deleted' and 'formatted' are recoverable; only overwriting, secure-wipe, physical destruction, or discarding the encryption key truly destroys data. This is why a factory-reset resold phone can still leak your photos.*


#### Concept 2 — Disk Imaging (Forensic Copy) `[THEORY]` `[~10 min]`

[SLIDE] **A bit-for-bit copy — then analyse the copy, never the original**

> **Deliver:** Define it. **A disk image is a bit-for-bit copy of an entire drive — including slack and
> unallocated space, not just the visible files.** Workflow: **image first (with a write blocker, then
> hash), then analyse the image — never the original.** Distinguish **physical image** (copies **every
> sector**, incl. the "empty" space where deleted data hides) from a **logical copy** (only chosen
> files/folders). Land it: **imaging the whole disk is what makes deleted-data recovery possible.**

- 🇳🇵 **Local example:** imaging a **seized hard disk / USB in a Nepali financial-fraud investigation**
  so the **original stays sealed** and all analysis runs on the **hashed copy.**
- 🇳🇵 **Mini case (work it, ≈2 min):** "Why image the **whole** disk, including 'empty' space, instead of
  just copying the visible files?" (Because **deleted/residual data lives in slack and unallocated
  space** — exactly what a file copy would **miss** — and only a **whole-disk hash** proves integrity.)

> ❌ **Common misconception:** *"Just copy the important files off the disk — that's enough."*
> ✅ **Correction:** "Copying only **visible files** misses **deleted data** in slack/unallocated space
> and produces **no whole-disk hash.** A forensic **physical image** captures everything **and** proves
> integrity; a file copy doesn't."

> 🖼️ Visual: a **bit-for-bit imaging** diagram showing visible/free/slack/unallocated regions all copied,
> with a **hash check.**

> 🎙️ Speaker note: Physical **image first, keep the original sealed.** A logical copy is fine for quick
> **triage** only — never as the evidential copy.

**📊 Depth table — Physical image vs logical copy — and why forensics prefers the image**

| Dimension | Physical (bit-for-bit) image | Logical copy |
|---|---|---|
| What it captures | Every sector, incl. slack & unallocated | Only chosen files/folders |
| Deleted data | Preserved (recoverable) | Lost — not copied |
| Hash verification | Whole-disk hash proves integrity | Weaker — misses hidden areas |
| Size / effort | Large, slower | Small, quick |
| Forensic value | High — the standard for evidence | Limited — triage only |
| Nepal example | Image a seized fraud-case hard disk/USB | Grab a few named files for a quick check |

*ℹ️ Forensics prefers the physical image because deleted/residual data lives in slack and unallocated space — exactly what a logical copy of 'visible files' would miss. Image first, keep the original sealed.*


#### Concept 3 — File Carving `[THEORY]` `[~7 min]`

[SLIDE] **Rebuild files by signature — no index needed**

> **Deliver:** Define it. **File carving reconstructs files from raw data using file signatures
> (headers/footers) when the file-system metadata is gone.** Example: a **JPEG always starts with a known
> header (FF D8) and ends with a known footer (FF D9)**; carving **scans unallocated space for these
> signatures** to **rebuild files without relying on the index.** It works **precisely when 'delete' or a
> format has removed the index but left the bytes behind** — which is how deleted photos and documents are
> recovered.

- 🇳🇵 **Local relevance:** when a suspect deletes photos and the **file-system index no longer lists
  them**, an analyst **carves the unallocated space** of the disk image — scanning for **JPEG headers/
  footers** — and rebuilds the images **without any index.**

> ❌ **Common misconception:** *"If the file isn't in the index, it's gone."*
> ✅ **Correction:** "**File carving recovers files by recognising their signatures in raw data**, with
> **no reliance on the file-system index** — so data can be rebuilt **even after the index entry is
> deleted**, as long as the **bytes aren't overwritten.**"

> 🍿 **Fun analogy (deliver it):** "File carving is like **reassembling a shredded document by
> recognising the edges and patterns**, even though the **labelled folder it came from is missing.**"

> 🖼️ Visual: a **JPEG header/footer carving** illustration — raw bytes with the FF D8 / FF D9 markers
> highlighted.

> 🎙️ Speaker note: The key idea: carving relies on **content signatures, not the index** — that's why it
> works when the index is gone.

**📊 Depth table — File carving — signatures rebuild files without an index**

| File type | Signature clue | What carving recovers |
|---|---|---|
| JPEG image | Header FF D8 … footer FF D9 | Deleted photos from unallocated space |
| PNG image | Header 89 50 4E 47 | Deleted screenshots/graphics |
| PDF document | Header %PDF … trailer %%EOF | Deleted documents/receipts |
| ZIP / Office file | Header PK\x03\x04 | Deleted archives & docx/xlsx |
| MP4 video | 'ftyp' box near the start | Deleted video clips |
| No index needed | Scans raw bytes for signatures | Files the file system no longer lists |

*ℹ️ Carving relies on content signatures, not the file-system index — so it works precisely when 'delete' or a format has removed the index but left the bytes behind.*

#### 🛠 ACTIVITY — "Dispose of your old device" `[ACTIVITY]` `[~5 min]`

[SLIDE] **If deletion rarely erases data, how do you dispose safely?**

> **Run it:** In pairs (2 min): **if deletion rarely erases data, how should you properly dispose of an
> old laptop or phone?** Students list the **steps that would actually stop data being recovered.** Take
> **3–4 answers aloud** (3 min) and **rank them** from **weak (delete)** to **strong (destroy /
> encrypt+wipe).** Close: connect to **Unit 2 privacy** — a **resold factory-reset phone can still leak
> photos.** Strong answers: **full secure-wipe/overwrite**, or **full-disk encryption then wipe/destroy
> the key**, or **physical destruction** for sensitive media. Weak: delete, empty bin, quick format,
> plain factory reset.

> 🎙️ Speaker note: Always **wipe BEFORE resale/disposal.** Reward answers that distinguish "the data is
> gone" from "the label is gone."

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** When a file is "deleted," what usually happens?
a) bytes are overwritten instantly b) ✅ **the pointer is removed but the data remains until overwritten** c) the disk shrinks d) nothing at all

**MCQ 2.** File carving recovers files by:
a) reading the index b) ✅ **recognising file signatures in raw data, without the file-system index** c) asking the OS d) decrypting them

**Discussion prompt:** *If deletion rarely erases data, how should you properly dispose of an old laptop or phone?*

> 🎙️ Speaker note: Land **deletion ≠ erasure** and connect to **privacy** — secure-wipe or destroy
> before disposal, **never** just delete or factory-reset.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** this is **why selling a phone after a factory reset can still leak your
photos** — and why **secure-wiping** (or **destroying the encryption key**) matters **before you dispose
of any device.** The recovery techniques investigators use are the **same techniques a buyer of your old
phone could use** on your leftover data.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Deletion removes the pointer, not the data** — "deleted" and "formatted" stay recoverable until **overwritten.**
2. Always work from a **hashed, bit-for-bit disk image** (incl. slack/unallocated), **never the original.**
3. **File carving** rebuilds files from their **header/footer signatures**, without the file-system index.

**Next session (S43):** the device at the centre of most Nepali cases — the **mobile phone.**

---
---

# S43 — Mobile Forensics
**Lecture hour 6 of 7 (Unit 4) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"The phone IS the crime scene"**

> **Deliver (≈2 min):** "**Your phone knows where you slept, who you texted at 2am, what you searched,
> and which photos you 'deleted.'** In most Nepali cyber cases today, **the phone IS the crime scene.**"
>
> **Run the question (≈3 min):** "How do investigators **get evidence out of it — legally?**" Take
> answers. Today: **why mobile is its own discipline → extraction methods & app data → challenges &
> integrity.**

> 🎙️ Speaker note: Make it personal — students' **own phones** hold exactly this data. That's the hook
> for privacy relevance later.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Why Mobile Forensics Is Its Own Discipline `[THEORY]` `[~10 min]`

[SLIDE] **A diary that writes and locks itself**

> **Deliver:** Define it. **Mobile forensics is extracting and analysing evidence from smartphones,
> tablets, SIMs and their apps.** Explain **why it's distinct:** phones are **always-on, networked,
> encrypted, OS-locked**, and store **extraordinarily rich data — location, messages, app data, media and
> call logs.** Each property makes mobile **harder than disk forensics**: constant **remote-wipe/sync
> risk**, getting **in** is often the hardest part, and **new OS versions/apps break yesterday's
> techniques.**

- 🇳🇵 **Local example:** **most Nepal Police Cyber Bureau complaints** — **online fraud, harassment,
  blackmail, fake profiles** — centre on **mobile phones and apps** like **Facebook, Messenger, TikTok,
  WhatsApp, Viber, eSewa/Khalti.** A single phone holds **chats, location, media and wallet data.**

> ❌ **Common misconception:** *"A factory reset wipes the phone clean."*
> ✅ **Correction:** "**Resets and 'deleted' chats can still leave recoverable traces**, and **cloud
> backups may persist** entirely — so a reset is **not a guarantee** the data is gone, for investigators
> or for **your own privacy.**"

> 🍿 **Fun analogy (deliver it):** "A smartphone is a **diary that writes itself and locks itself** —
> forensics is about **reading it without it noticing — or destroying — the page.**"

> 🎙️ Speaker note: Land that the **phone, not a PC, is the crime scene today** in Nepal.

**📊 Depth table — Nepali cyber complaints — the phone as the crime scene**

| Complaint type (Nepal) | Where the evidence lives | What the phone reveals |
|---|---|---|
| Online fraud / scam | eSewa/Khalti, SMS OTPs, bank app | Transactions, payee, timing |
| Harassment / cyberbullying | Messenger, WhatsApp, Viber, TikTok | The abusive messages & who sent them |
| Blackmail / sextortion | Gallery, chat apps, cloud backup | Images, threats, contact history |
| Fake profile / impersonation | Facebook/Instagram app + logins | Account access, device linkage |
| Financial dispute | Call logs + CDRs (NTC/Ncell) | Who contacted whom, and when |
| Location alibi | Maps/app location history | Where the phone was at a key time |

*ℹ️ Most Nepal Police Cyber Bureau complaints centre on mobile phones and apps (Facebook, Messenger, TikTok, WhatsApp, Viber, eSewa/Khalti) — the phone, not a PC, is the crime scene today.*


#### Concept 2 — Extraction Methods & App Data `[THEORY]` `[~10 min]`

[SLIDE] **Manual → logical → file-system → physical (more data, harder)**

> **Deliver:** Teach the **levels of extraction** as a ladder: **manual** (scrolling/photographing) →
> **logical** (via APIs/backups) → **file-system** → **physical** (a full image). The rule: **more
> invasive = more data but harder.** Name the **key sources:** **chat/app databases (often SQLite), call
> logs, location history, media metadata, and cloud-synced data.** Land it: **app data often lives in
> SQLite databases; cloud backups may hold the rest.**

- 🇳🇵 **Mini case (work it, ≈2 min):** "A suspect **deleted a WhatsApp chat**, but the app's **local
  SQLite database still holds fragments** and the **cloud backup has the rest** — **how many places must
  the investigator check?**" (At least three: **device storage, the app database, and (lawfully) the
  cloud backup** — because "deleted from the chat view" rarely means deleted everywhere.)

> ❌ **Common misconception:** *"If it's deleted in the app, it's gone from the phone."*
> ✅ **Correction:** "App data lives in **local SQLite databases** and often **syncs to a cloud backup**,
> so **fragments and full copies commonly survive** a chat 'deletion.' An investigator (and a
> privacy-conscious user) must think about **every place the data was copied to.**"

> 🖼️ Visual: an **extraction-levels pyramid** — manual → logical → file system → physical — with "more
> data / more invasive" downward.

> 🎙️ Speaker note: The **more invasive the level, the more data** — but the **harder** (encryption,
> locks, access). Cloud access needs **lawful authorisation.**

**📊 Depth table — The four extraction levels — data vs difficulty**

| Level | How it works | Data yield / trade-off |
|---|---|---|
| Manual | Scroll & photograph the screen | Least data; quick but alters the device |
| Logical | Via device APIs / backups | Moderate; less invasive, may miss deleted data |
| File-system | Pull app databases & system files | More — reaches SQLite chat databases |
| Physical | Full bit-for-bit image of storage | Most data (incl. deleted); hardest, needs access |
| App databases | Read SQLite chat/app stores | Fragments of 'deleted' chats |
| Cloud-synced | Lawfully obtain the backup | What the phone itself no longer holds |

*ℹ️ The rule: the more invasive the level, the more data — but the harder it is (encryption, locks, access). Deleted chat evidence often survives in the app's SQLite database AND in the cloud backup.*


#### Concept 3 — Challenges & Integrity in Mobile Forensics `[THEORY]` `[~7 min]`

[SLIDE] **New obstacles, same integrity rules**

> **Deliver:** List the **obstacles unique to mobile:** **encryption, lock screens, constant connectivity
> (remote-wipe risk), OS/version diversity, and rapid app changes.** Then land the payoff: **the integrity
> rules are unchanged** — **isolate immediately (Faraday bag / airplane mode), document, hash extractions,
> and maintain chain of custody just as with disks.** If anything, the **remote-wipe risk makes immediate
> isolation more urgent** than with a disk.

- 🇳🇵 **Local example:** a **seized phone in Kathmandu is placed in a Faraday bag the moment it's
  collected** — blocking all signals so it **can't be remotely wiped or synced** — then **documented, its
  extraction hashed, and every handoff logged.** The **obstacles are new; the rules are those from S41.**

> ❌ **Common misconception:** *"Mobile evidence is so messy that strict integrity rules don't really
> apply."*
> ✅ **Correction:** "They apply **fully** — **isolate, document, hash, keep custody** — **precisely
> because** phones are **volatile and connected.** The remote-wipe risk makes **immediate isolation more
> urgent**, not less."

> 🍿 **Fun analogy (callback):** the **Faraday bag** from S41 returns — the phone is a **live radio**;
> **isolation is the airlock** that stops the outside world reaching in to destroy the evidence.

> 🎙️ Speaker note: Mobile is **harder technically** but the **integrity discipline is identical** to
> disk forensics. Integrity gets **no mobile exemption.**

**📊 Depth table — Mobile-specific challenges — and the integrity response**

| Challenge | Why it's hard on mobile | Integrity response |
|---|---|---|
| Encryption | Data unreadable without the key | Live-acquire while unlocked; lawful access |
| Lock screen | Can't get in without the passcode | Isolate; document; use lawful means |
| Constant connectivity | Remote wipe / cloud sync risk | Faraday bag / airplane mode immediately |
| OS / version diversity | No single technique fits all | Document tool & method used; repeatability |
| Rapid app changes | Yesterday's method breaks | Validate the tool; note versions |
| Rich, mixed data | Easy to alter or miss | Hash extractions; work on copies; custody log |

*ℹ️ The obstacles are new but the discipline is the same as disk forensics: isolate first, document everything, hash the extraction, and keep an unbroken chain of custody. Integrity does not get a mobile exemption.*

#### 🛠 ACTIVITY — "Where else does the chat live?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Besides the phone, where can 'deleted' chat evidence survive?**

> **Run it:** In pairs (2 min): **besides the phone itself, where might "deleted" chat evidence still
> exist?** Students list **every place** a WhatsApp/Messenger message could be recovered from. Take **3–4
> answers aloud** (3 min); **mark which need lawful authorisation** to access. Close: connect to privacy —
> **the same copies that help investigators can leak YOUR data.** Seeds: **local app SQLite database,
> device backup, cloud backup (Google/iCloud), the other party's phone, the platform's servers, and
> SMS/notification logs.**

> 🎙️ Speaker note: Accessing **cloud/platform data lawfully needs proper authorisation** — flag the legal
> gate that Concept 2 raised.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** Which extraction type generally yields the MOST data?
a) manual b) logical c) file-system d) ✅ **physical (full image)**

**MCQ 2.** A seized phone is placed in a Faraday bag primarily to:
a) charge it b) ✅ **block all signals so it can't be remotely wiped or synced** c) unlock it d) hash it

**Discussion prompt:** *Where, besides the phone itself, might "deleted" chat evidence still exist?*

> 🎙️ Speaker note: Land the **extraction-level trade-off** (more data = harder) and that **isolation is
> the first, urgent step** on any seized phone.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** understanding **what your phone stores — and how recoverable it is —**
directly shapes **how you protect your own privacy** and **how you dispose of old devices.** The chat you
"deleted," the location history you forgot, the cloud backup you never checked — all of it is
recoverable, which is a warning for **your** data as much as a tool for an investigator.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Phones are today's primary crime scene** and a **discipline of their own** (always-on, encrypted, data-rich).
2. **Extraction ranges from manual → logical → file-system → physical**, with **app SQLite databases & cloud** as key sources.
3. The **same integrity rules still apply:** **isolate (Faraday bag), document, hash, and keep chain of custody.**

**Next session (S44):** the **legal** side — admissibility, the **ETA 2063**, and where **Nepal** stands.

---
---

# S44 — Legal Aspects of Digital Forensics · Cyber Forensics in Nepal (closes Unit 8)
**Lecture hour 7 of 7 (Unit 4) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Damning evidence — ruled inadmissible — the criminal walks free"**

> **Deliver (≈2 min):** "Investigators **recover damning evidence** — but the judge rules it
> **inadmissible because of how it was handled.** **The criminal walks free.**"
>
> **Run the question (≈3 min):** "In Nepal, **who is even allowed to do this work, and under which
> law?**" Take answers. Land it: **law decides whether good forensics matters.** Today: **legal
> admissibility → Nepal's legal framework (ETA 2063) → the state of cyber forensics in Nepal.**

> 🎙️ Speaker note: Hold the sting of the hook — **perfect forensics is wasted if the law rejects it.**
> Agenda on the board.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Legal Admissibility of Digital Evidence `[THEORY]` `[~10 min]`

[SLIDE] **Truth isn't enough — it must be lawful, authentic and intact**

> **Deliver:** Define it. **Admissibility is the set of conditions under which a court will accept digital
> evidence:** **relevance, authenticity, integrity (chain of custody + hashing), proper authorisation (a
> search warrant / lawful seizure), and expert testimony.** Land the ethical/legal core: **mishandling —
> even of genuine evidence — makes it inadmissible.** Walk the conditions: it must be **relevant** (bear on
> a fact), **authentic & integral** (proven unaltered via custody log and hashes), **lawfully obtained** (a
> valid warrant, not an illegal search), and **explained by a competent expert** the court can question.

- 🌍 **Global example:** evidence **excluded due to a broken chain of custody or unlawful seizure.**
- 🇳🇵 **Local relevance:** a Cyber Bureau case where the **seizure lacked proper authorisation**, or the
  **custody chain has an unexplained gap**, can see **genuine evidence excluded** — and the **accused
  walks free.**

> ❌ **Common misconception:** *"If the evidence is true, the court must accept it."*
> ✅ **Correction:** "Even **genuine evidence is rejected if illegally obtained or improperly handled** —
> a **broken chain of custody** or a **warrantless seizure** can exclude it entirely. **Lawful process is
> as essential as the truth of the data.**"

> 🖼️ Visual: an **admissibility checklist** — relevant ✓ authentic ✓ integrity ✓ legally obtained ✓.

> 🎙️ Speaker note: This is the **misconception-first** concept — "true ≠ admissible." **Every box must be
> ticked at once.**

**📊 Depth table — The admissibility checklist — every box must be ticked**

| Condition | What it requires | If it fails |
|---|---|---|
| Relevance | Bears on a fact in the case | Excluded as irrelevant |
| Authenticity | Proven to be what it claims to be | Weight collapses; may be rejected |
| Integrity | Chain of custody + matching hashes | Challenged as possibly tampered |
| Lawful authorisation | Search warrant / lawful seizure | Excluded — 'fruit of unlawful search' |
| Expert testimony | A competent expert explains it | Court can't rely on it |
| Handling | Correct process throughout | Mishandling sinks even true evidence |

*ℹ️ Every condition must hold at once. A single failure — an unlawful seizure, a custody gap, a hash mismatch — can make genuine, damning evidence inadmissible. Truth alone is never sufficient.*


#### Concept 2 — The Legal Framework in Nepal `[THEORY]` `[~10 min]`

[SLIDE] **ETA 2063 (2008) — the backbone of e-evidence in Nepal**

> **Deliver:** Name the law. Nepal's electronic evidence is governed mainly by the **Electronic
> Transaction Act (ETA) 2063 (2008)**, which **recognises electronic records/evidence and defines cyber
> offences**, alongside **Evidence Act provisions** and the **courts' growing acceptance of electronic
> records.** Cybercrime complaints are **prosecuted via the Cyber Bureau under the ETA.** Flag the live
> debate: there is an **ongoing push for a dedicated, modern cybercrime / data-protection law** (a forward
> link to **Unit 9** on cyber law).

- 🇳🇵 **Mini case (work it, ≈2 min):** "A complainant brings **only WhatsApp screenshots** to the Cyber
  Bureau — **what additional steps are needed** before this becomes **court-ready evidence?**"
  (**Forensic extraction of the original messages with metadata, hashing, a chain-of-custody record, and
  lawful authorisation** — turning weak screenshots into **authenticated, admissible** evidence.)

> ❌ **Common misconception:** *"The ETA 2063 automatically makes any electronic file valid evidence in
> court."*
> ✅ **Correction:** "The ETA **recognises** electronic records, but the evidence still has to be
> **authentic, intact, and lawfully obtained.** **Screenshots alone don't clear that bar; forensic
> extraction and custody do.**"

> 🖼️ Visual: a **Nepal legal-framework** panel — ETA 2063, Evidence Act, Cyber Bureau, courts.

> 🎙️ Speaker note: The ETA is the **backbone** but **predates today's mobile/cloud reality** — hence the
> push for a **modern law** (Unit 9).

**📊 Depth table — Nepal's legal handles on digital evidence**

| Instrument / body | Role | Note |
|---|---|---|
| ETA 2063 (2008) | Recognises e-records; defines cyber offences | The main legal basis for e-evidence |
| Evidence Act provisions | Support acceptance of electronic records | Used alongside the ETA |
| Nepal Police Cyber Bureau | Investigates & prosecutes cybercrime | Central body (est. 2018) |
| Courts | Accept electronic records as evidence | Practice still maturing |
| Warrant / lawful seizure | Authorises collection | Required for admissibility |
| Proposed modern law | Dedicated cybercrime/data-protection | Still debated (Unit 9) |

*ℹ️ The ETA 2063 is the backbone but predates today's mobile/cloud reality — hence the ongoing push for a dedicated, modern cybercrime and data-protection law, explored in Unit 9.*


#### Concept 3 — Cyber Forensics in Nepal — State & Challenges `[THEORY]` `[~7 min]`

[SLIDE] **Sound principles, but capacity must scale**

> **Deliver:** Describe the landscape. Nepal's cyber forensics **centres on the Nepal Police Cyber
> Bureau** as the central body, facing a **rising caseload** (online fraud, social-media abuse, financial
> scams) against real **constraints**: **limited trained personnel, tool/lab capacity, backlog, dependence
> on foreign platforms for data, and an evolving legal framework.** Land the honest picture: **the
> principles are sound; the constraint is capacity.**

- 🇳🇵 **Local example:** the Cyber Bureau handles a **fast-rising caseload** with **limited trained
  staff**, **constrained lab capacity**, a **growing backlog**, and **slow, dependent cross-border access**
  to data on **Facebook / Google** — all under an **ageing ETA 2063.** The **framework works; capacity is
  the bottleneck.**

> ❌ **Common misconception:** *"Nepal can't do real cyber forensics."*
> ✅ **Correction:** "It **can and does** — the Cyber Bureau **applies sound principles daily.** The real
> issue is **capacity** (people, labs, law, foreign-data access) that must **scale with the rising
> caseload**, not a lack of valid methodology."

> 🍿 **Fun analogy (deliver it):** "Nepal's cyber forensics is a **small fire brigade facing a
> fast-growing city:** the **principles are sound**, but **capacity must scale with the digital
> population.**"

> 🖼️ Visual: a **Nepal cyber-forensics ecosystem** diagram — complaint → Cyber Bureau → lab → court under
> ETA — with the **admissibility checklist.**

> 🎙️ Speaker note: Be **fair and honest** — praise the sound principles, name the **capacity gaps** (few
> experts, limited labs, backlog, foreign-data dependence, ageing law).

**📊 Depth table — Cyber forensics in Nepal — strengths and gaps**

| Area | Current state | Challenge / gap |
|---|---|---|
| Central body | Cyber Bureau investigates cybercrime | Overloaded; district reach is limited |
| Caseload | Rising fast (fraud, abuse, scams) | Backlog grows faster than capacity |
| Personnel | A trained core team exists | Too few trained forensic experts |
| Lab / tools | Central lab at the Bureau | Limited lab capacity beyond it |
| Foreign data | Evidence on Facebook/Google etc. | Slow, dependent cross-border access |
| Legal framework | ETA 2063 in force | Ageing; modern law still debated |

*ℹ️ The principles are sound; the constraint is capacity. Like a small fire brigade facing a fast-growing city, Nepal's cyber forensics must scale personnel, labs and law with the rising digital caseload.*

#### 🛠 ACTIVITY — "Screenshots to court-ready" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Turn WhatsApp screenshots into admissible evidence**

> **Run it:** In pairs (2 min): a complainant brings **only WhatsApp screenshots** to the Cyber Bureau.
> Students list the **steps needed to turn them into court-ready, admissible evidence under the ETA
> 2063**, then **check each step against the admissibility checklist.** Take **3–4 answers aloud** (3 min).
> Steps: **forensic extraction of the original messages + metadata, hashing, a chain-of-custody record,
> lawful authorisation/warrant, and expert testimony.** Close: debate briefly — **should Nepal create a
> dedicated cybercrime / data-evidence law beyond the ETA?**

> 🎙️ Speaker note: **Screenshots alone fail authenticity/integrity;** the **extraction and custody
> supply them.** Use the debate to preview **Unit 9.**

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** Genuine evidence can still be rejected by a court if:
a) it's too detailed b) ✅ **it was illegally obtained or improperly handled (broken chain of custody)** c) it's digital d) it's on a phone

**MCQ 2.** In Nepal, electronic records are primarily recognised as evidence under the:
a) Muluki Ain b) ✅ **Electronic Transaction Act (ETA), 2063** c) Companies Act d) no law

**Discussion prompt:** *Should Nepal create a dedicated cybercrime and digital-evidence law beyond the ETA? Argue both sides.*

> 🎙️ Speaker note: Land that **admissibility needs legality + authenticity + integrity**, and that the
> **ETA 2063 is Nepal's main (but ageing) legal basis.**

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** as a **BIM graduate you may one day file or face a cyber complaint** — a scam,
a harassment case, a data dispute. **Knowing what makes evidence admissible** (lawful seizure,
authenticity, integrity, custody) **and the Cyber Bureau's role** is **directly practical** for
protecting **yourself and others** — you'll know to preserve, not "check," and to demand extraction over
screenshots.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Admissibility needs legality + authenticity + integrity, not just truth** — mishandled evidence is **excluded.**
2. Nepal relies mainly on the **ETA 2063 (2008)** and the **Nepal Police Cyber Bureau** for electronic evidence.
3. The **principles are sound**, but **capacity (people, labs, law) must grow** with the rising cybercrime caseload.

**Next unit (Unit 9):** **Cyber Law in the context of Nepal** — the ETA, Electronic Transaction Rules, and IT/security policy in depth.

---
---

# 📋 UNIT 8 — END-OF-UNIT QUIZ
*Use as a 15–20 min in-class quiz or a take-home review. Answer key at the end.*

### Section A — Multiple Choice (1 mark each)
1. The defining goal of digital forensics is:
   a) recover deleted files  b) ✅ producing legally admissible evidence  c) fix the device  d) back up data
2. "Computer forensics" grew into "digital forensics" mainly because:
   a) PCs got faster  b) ✅ evidence now lives on phones, cloud and networks, not just PCs  c) laws changed  d) disks shrank
3. The correct order of the forensic process is:
   a) collect→identify→report  b) ✅ identify→preserve→collect→examine→analyse→report  c) analyse→collect→report  d) report→collect
4. Which property is NOT required of good digital evidence?
   a) authentic  b) complete  c) reliable  d) ✅ that it be encrypted
5. The purpose of a write blocker is to:
   a) speed up copying  b) ✅ allow reading a drive while preventing any change to it  c) encrypt the disk  d) delete data
6. Identical hash values of the original and the copy prove that:
   a) the data is encrypted  b) ✅ the copy is an exact, unaltered duplicate  c) the drive is empty  d) nothing
7. When a file is "deleted," what usually happens?
   a) bytes are overwritten instantly  b) ✅ the pointer is removed but data remains until overwritten  c) the disk shrinks  d) nothing
8. File carving recovers files by:
   a) reading the index  b) ✅ recognising file signatures in raw data, without the file-system index  c) asking the OS  d) decrypting them
9. Which extraction type generally yields the most data?
   a) manual  b) logical  c) file-system  d) ✅ physical (full image)
10. In Nepal, electronic records are primarily recognised as evidence under the:
    a) Muluki Ain  b) ✅ Electronic Transaction Act (ETA), 2063  c) Companies Act  d) no law

### Section B — Short Answer (2 marks each)
11. Define **chain of custody** and explain **why it matters**.
12. List and explain the **six forensic stages** (in order).
13. Explain **why a bare screenshot is weak evidence** (and what makes it strong).
14. Explain **how hashing proves integrity** (and the role of the write blocker).
15. Name the **central cyber-forensics body in Nepal** and **two challenges** it faces.

### Section C — Applied Case (3 marks each)
16. Given a **Nepal-context phone-seizure scenario** (a suspect's unlocked, connected phone), list the **correct steps to preserve integrity and chain of custody.**
17. Explain **why a piece of genuine but mishandled evidence would be ruled inadmissible** in a Nepali court.

### Section D — Discussion (open-ended)
18. "**Should Nepal invest in a dedicated digital-forensics law and lab capacity beyond the current ETA and Cyber Bureau?**" Argue **both sides**, then state your own position.

---

### ✅ Answer Key (Section A)
1-b · 2-b · 3-b · 4-d · 5-b · 6-b · 7-b · 8-b · 9-d · 10-b

> **Sections B–D: grade on key terms.** Q11 must give the *documented, unbroken record of who handled
> evidence, when, why and how* + that it is the **proof of integrity** (a gap = challengeable). Q12 must
> list **identify → preserve → collect → examine → analyse → report** with one line each, noting
> preservation protects everything downstream and the report is for a non-technical judge. Q13 must note
> screenshots are **easily faked and lack metadata/custody**, made strong by a **forensically extracted
> original.** Q14 must explain that **matching hashes (MD5/SHA-256) prove the copy is bit-for-bit
> identical** and that a **write blocker** stops the original being altered during imaging. Q15 —
> **Nepal Police Cyber Bureau** + any two of: few trained experts, limited lab/tool capacity, backlog,
> dependence on foreign platforms for data, ageing legal framework. Q16 must include **photograph the
> scene/screen, isolate the network (Faraday/airplane mode), decide power deliberately, image + hash,
> seal & label, and log every handoff.** Q17 must state that **illegally obtained (no warrant) or
> mishandled (broken custody / no hashing)** evidence is **excluded regardless of truth.** Q18 — reward
> weighing **both sides** (a modern law + more labs/experts/faster foreign-data access vs cost,
> priorities, and building on the existing ETA/Cyber Bureau), not a one-sided slogan.

---

## ✅ Unit 8 complete (full lecturer-ready depth)
The deck is built: **IT246_Unit8.pptx** (100 slides) — diagram-rich, self-contained, and PDF-safe,
carrying all **21 §7A depth tables** (comparison, concrete-example, and scaffolding) and **10 diagrams**
(evolution timeline; the six-stage process with a chain-of-custody band; the digital-evidence map; the
chain-of-custody handoff chain; the order-of-volatility ladder; write-blocker + hash match; bit-for-bit
disk imaging; JPEG file carving; the mobile extraction-level pyramid; and the Nepal cyber-forensics
ecosystem + admissibility checklist). This Markdown source carries those **same 21 depth tables inline**
under each concept, so the source of truth and the deck stay in sync. **Chain of custody and evidence
integrity** run through every session, and every example is localised to Nepal (ETA 2063, Nepal Police
Cyber Bureau, NTC/Ncell CDRs, eSewa/Khalti, Facebook/TikTok/WhatsApp).
