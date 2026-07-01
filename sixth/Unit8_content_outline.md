# Unit 8 — Digital Forensics · Content Outline

**7 LHs → 7 sessions (S38–S44) · 50 min each**
This is the *content map* — what will fill each slot before we generate full material.
Local examples use Nepal / South Asia (Nepal Police Cyber Bureau, Nepali court cases, mobile-phone evidence). Review and tell me what to swap.
Recurring themes across the whole unit: **chain of custody** and **evidence integrity** (hashing, write blockers, documentation).

> Template per session (from the guide):
> Opening hook (5m) → Content sections (35m) → Check for understanding (5m) →
> Real-life application (3m) → Summary & takeaways (2m), with speaker notes + visual cues.

---

## Unit 8 learning outcomes (what students can do after S38–S44)
1. Define digital forensics and explain how the field grew from "computer forensics," including its core principles.
2. Describe the staged forensic process (identification → preservation → collection → examination → analysis → reporting).
3. Explain what counts as digital evidence and describe a forensic lab's setup and tool categories.
4. Explain chain of custody and the techniques that protect evidence integrity (write blockers, hashing, sealed storage).
5. Describe — conceptually — how deleted data is recovered through disk imaging and file carving.
6. Explain mobile forensics: how phone evidence is extracted, its challenges, and app-data sources.
7. Explain the legal admissibility of digital evidence and the state of cyber forensics in Nepal.

---

## S38 — Introduction · From Computer Forensics to Digital Forensics

**Hook:** "A suspect's laptop is seized in a fraud case. An officer 'just opens it to check' — and the case collapses in court. One click destroyed the evidence. How can looking at a file *break* it?" → why forensics is a discipline, not casual snooping.

**Concepts & how each will be filled:**

1. **What is digital forensics**
   - Definition: the scientific process of identifying, preserving, analysing and presenting digital evidence in a way that is legally admissible.
   - Theory: forensics = applying science to legal questions; "digital" = any device storing/transmitting data.
   - Global example: the BTK killer caught via metadata in a Word document on a floppy disk.
   - Local example: Nepal Police Cyber Bureau (Cyber Bureau, established 2018, Bhotahity) analysing seized devices in online-fraud and social-media abuse cases.
   - Misconception: *"Forensics is just data recovery / IT support."* Correction: the goal is court-admissible proof, not just retrieving files.

2. **From computer forensics to digital forensics**
   - Definition: the field broadened from desktop hard disks to phones, cloud, IoT, network traffic and vehicles.
   - Theory: "computer forensics" (1980s–90s, single PC) → "digital forensics" (multi-device, networked, cloud, mobile-dominant today).
   - Local example: Nepali cases now hinge more on Facebook/TikTok/WhatsApp and mobile phones than on desktop PCs.
   - Mini case: "An old textbook says 'image the hard drive.' The suspect only owns a smartphone — what changed?"

3. **Core principles**
   - Don't alter the original; work on copies; document everything; maintain chain of custody; ensure repeatability.
   - Theory: ACPO-style principles — actions taken should not change the data; if originals must be accessed, the person must be competent and explain why.
   - Fun element: analogy — a digital crime scene is like a sandy beach footprint; walking over it to "look closer" destroys the very thing you came to capture.

**Check for understanding:**
- MCQ1: The defining goal of digital forensics is…? → producing legally admissible evidence ✅
- MCQ2: "Computer forensics" grew into "digital forensics" mainly because…? → evidence now lives on phones, cloud and networks, not just PCs ✅
- Discussion: "Why is 'just take a quick look at the file' one of the most dangerous things an investigator can do?"

**Real-life application:** anyone in IT may someday hold a device that is evidence — knowing not to touch it can make or break a case (and your own liability).

**Summary:** (1) digital forensics = science + law applied to digital evidence; (2) the field expanded far beyond the single PC; (3) preserve the original, work on copies. **Next:** the staged forensic process.

**Visual cues:** timeline "computer forensics → digital forensics"; principle list as a "DO NOT ALTER" sign over a hard drive.

---

## S39 — Stages of Digital Forensics

**Hook:** "Two investigators find the same incriminating photo on a phone. One follows a documented process; the other 'just found it.' Only one will hold up in court. Why?" → process is what makes evidence trustworthy.

**Concepts & how each will be filled:**

1. **The forensic process model**
   - Definition: a repeatable, documented sequence from scene to courtroom.
   - Theory: identification → preservation → collection → examination → analysis → reporting (NIST/standard model).
   - Global example: NIST SP 800-86 phases (collection, examination, analysis, reporting).
   - Misconception: *"Analysis is the main step; the rest is paperwork."* Correction: preservation and chain of custody are what make the analysis usable at all.

2. **Walking the stages**
   - Identification (what devices/data matter) → Preservation (isolate, prevent change, e.g. airplane mode/Faraday) → Collection (image/seize) → Examination (extract relevant data) → Analysis (interpret, reconstruct events) → Reporting (clear, defensible, for non-technical judges).
   - Local example: a Cyber Bureau workflow for a cyberbullying complaint — identify the account/phone, preserve by isolating the device, image it, examine messages, analyse the timeline, report for the prosecutor.
   - Mini case: "Investigators skip preservation and let the phone keep syncing — overnight, the cloud deletes the key chat. What stage failed?"

3. **Integrity & chain of custody run through every stage**
   - Documentation, hashing at collection, sealed evidence bags, custody log.
   - Fun element: analogy — like a relay race baton: every handoff is recorded, and dropping it (a gap in custody) disqualifies the team.

**Check for understanding:**
- MCQ1: Which is the correct order? → identification → preservation → collection → examination → analysis → reporting ✅
- MCQ2: The forensic report must be written primarily for…? → a non-technical audience such as a judge/lawyer ✅
- Discussion: "Which single stage, if skipped, most often destroys a case — and why?"

**Real-life application:** the same disciplined-process thinking applies to incident response in any company breach, not just police work.

**Summary:** (1) forensics follows a fixed, documented sequence; (2) preservation protects everything downstream; (3) integrity and custody thread through all six stages. **Next:** what actually counts as digital evidence, and the lab that handles it.

**Visual cues:** 6-stage horizontal pipeline with "chain of custody" as a band running under all stages.

---

## S40 — Role of Digital Evidence · Methods and the Forensic Lab

**Hook:** "A deleted message, a GPS log, a thumbnail cache, a router log — which of these convicted someone? All of them have. What turns ordinary data into *evidence*?" → defining and handling digital evidence.

**Concepts & how each will be filled:**

1. **What counts as digital evidence**
   - Definition: any data stored or transmitted in digital form that can support or refute a fact in a case.
   - Theory: types — files/documents, metadata, logs, chats/email, images/video, location data, deleted/residual data; properties of good evidence (admissible, authentic, complete, reliable, believable).
   - Global example: location/cell-tower and search-history evidence in major criminal trials.
   - Local example: chat screenshots, call detail records (CDRs) from NTC/Ncell, and mobile photos/metadata used in Nepali fraud and harassment cases.
   - Misconception: *"A screenshot is solid proof."* Correction: screenshots are easily faked and lack metadata — they are weak unless backed by a forensically extracted original.

2. **Methods & tools overview**
   - Definition: standard techniques (imaging, hashing, keyword search, timeline/artifact analysis) and tool categories.
   - Theory: imaging tools, write blockers, analysis suites (e.g. Autopsy/Sleuth Kit — open source; EnCase, FTK — commercial), mobile tools (e.g. Cellebrite) — introduced by category, not deep use.
   - Mini case: "A team has only free tools (Autopsy) and a tight budget — can they still do valid forensics?" (Yes — methodology matters more than brand.)

3. **The forensic lab**
   - Definition: a controlled environment ensuring integrity, security and accreditation.
   - Theory: physical security, access control, evidence storage/lockers, isolated/air-gapped analysis machines, documentation, ideally accreditation (ISO 17025).
   - Local example: the Nepal Police Cyber Bureau lab; constraints faced by district-level investigations that lack lab access.
   - Fun element: analogy — a forensic lab is a "clean room for truth": just as a hospital lab avoids contaminating a blood sample, the forensic lab avoids contaminating the data.

**Check for understanding:**
- MCQ1: Which property is NOT required of good digital evidence? → that it be encrypted ✅
- MCQ2: A bare screenshot is considered weak evidence mainly because…? → it can be faked and lacks original metadata ✅
- Discussion: "Why might a free tool like Autopsy be just as admissible as expensive commercial software?"

**Real-life application:** understanding evidence quality helps you, as a future IT professional, log and preserve data correctly when something goes wrong on your systems.

**Visual cues:** "types of digital evidence" mind map; forensic-lab floor-plan sketch (locked evidence store, isolated workstation, entry log).

---

## S41 — Collecting, Seizing and Protecting Evidence

**Hook:** "A phone is seized still switched on, screen unlocked, connected to Wi-Fi. Do you turn it off? Leave it on? Either choice can destroy evidence. What's the rule?" → controlled collection and protection.

**Concepts & how each will be filled:**

1. **Chain of custody (the unit's spine)**
   - Definition: the documented, unbroken record of who handled evidence, when, why and how — from seizure to court.
   - Theory: every transfer logged; sealed, labelled evidence bags; custody form; any gap = challengeable in court.
   - Global example: evidence thrown out because a custody gap could not be explained.
   - Local example: Cyber Bureau seizure procedure — device tagged, sealed, logged before transport; weaknesses when officers without training seize phones at a local thana.
   - Misconception: *"Chain of custody is just bureaucratic paperwork."* Correction: it is the proof the evidence wasn't tampered with — without it, even perfect data is worthless.

2. **Seizing devices correctly**
   - Definition: capturing a device in a state that preserves its data.
   - Theory: photograph the scene/screen; decide power-on vs power-off (live data in RAM vs remote-wipe risk); isolate from networks (Faraday bag, airplane mode) to stop remote wiping/syncing; record everything.
   - Mini case: "An officer powers down a running laptop with full-disk encryption — the disk re-locks and the password is unknown. What was lost?" (Live-acquisition opportunity.)

3. **Protecting evidence integrity: write blockers & hashing**
   - Definition: write blocker = hardware/software that allows reading a drive but blocks any write; hashing = a digital fingerprint (MD5/SHA-256) proving data is unchanged.
   - Theory: hash the original at collection, hash the copy — matching hashes prove the image is identical and untouched; write blockers ensure the original is never modified during imaging.
   - Local example: in a Nepali court, an expert showing identical SHA-256 hashes to demonstrate the analysed copy equals the seized original.
   - Fun element: analogy — a hash is like a tamper-evident seal on a medicine bottle; if even one byte changes, the seal (hash) visibly breaks.

**Check for understanding:**
- MCQ1: The purpose of a write blocker is to…? → allow reading a drive while preventing any change to it ✅
- MCQ2: Identical hash values of the original and the copy prove that…? → the copy is an exact, unaltered duplicate ✅
- Discussion: "A seized phone is left connected to the internet 'just for a minute.' List everything that could go wrong."

**Real-life application:** the same hashing idea verifies downloads and backups you use daily — and a custody mindset protects you when you handle sensitive company data.

**Summary:** (1) chain of custody is the proof of integrity, not mere paperwork; (2) seize devices without altering them (isolate networks, decide power carefully); (3) write blockers + hashing guarantee the original is untouched. **Next:** how investigators recover data that someone tried to delete.

**Visual cues:** chain-of-custody form mock-up; "write blocker" diagram (one-way arrow drive→analyst); before/after hash match graphic.

---

## S42 — Recovering Data (conceptual)

**Hook:** "A suspect 'deletes everything' and empties the recycle bin, confident it's gone. Investigators recover it in an hour. Where was it hiding?" → deletion ≠ erasure.

**Concepts & how each will be filled:**

1. **Why "deleted" isn't gone**
   - Definition: deleting usually removes the pointer/index entry, not the actual data, which stays until overwritten.
   - Theory: file system marks space as "free"; until reused, the bytes remain recoverable. (Note: SSD TRIM and full-disk encryption complicate this — a useful nuance.)
   - Global example: criminal cases solved by recovering "deleted" emails and images.
   - Misconception: *"Emptying the recycle bin / formatting permanently destroys data."* Correction: a quick format and delete leave most data recoverable; only overwriting/secure wipe truly destroys it.

2. **Disk imaging (forensic copy)**
   - Definition: a bit-for-bit copy of an entire drive, including slack and unallocated space.
   - Theory: image first (with write blocker, then hash), then analyse the image — never the original; logical copy vs full physical image.
   - Local example: imaging a seized hard disk/USB in a Nepali financial-fraud investigation so the original stays sealed.
   - Mini case: "Why image the *whole* disk, including 'empty' space, instead of just copying the visible files?"

3. **File carving**
   - Definition: reconstructing files from raw data using file signatures (headers/footers) when the file-system metadata is gone.
   - Theory: e.g. a JPEG always starts with a known header; carving scans unallocated space for these signatures to rebuild files without relying on the index.
   - Fun element: analogy — file carving is like reassembling a shredded document by recognising the edges and patterns, even though the labelled folder it came from is missing.

**Check for understanding:**
- MCQ1: When a file is "deleted," what usually happens? → the pointer is removed but the data remains until overwritten ✅
- MCQ2: File carving recovers files by…? → recognising file signatures in raw data, without the file-system index ✅
- Discussion: "If deletion rarely erases data, how should *you* properly dispose of an old laptop or phone?"

**Real-life application:** this is why selling a phone after a factory reset can still leak your photos — and why secure wiping matters before disposal.

**Summary:** (1) deletion removes the pointer, not the data; (2) always work from a hashed disk image, never the original; (3) file carving rebuilds files from signatures. **Next:** the device at the centre of most Nepali cases — the mobile phone.

**Visual cues:** "delete = remove label, keep box" diagram; JPEG header/footer carving illustration; bit-for-bit imaging arrow with hash check.

---

## S43 — Mobile Forensics

**Hook:** "Your phone knows where you slept, who you texted at 2am, what you searched, and which photos you 'deleted.' In most Nepali cyber cases today, the phone *is* the crime scene. How do investigators get evidence out of it — legally?" → mobile forensics.

**Concepts & how each will be filled:**

1. **Why mobile forensics is its own discipline**
   - Definition: extracting and analysing evidence from smartphones, tablets, SIMs and their apps.
   - Theory: phones are always-on, networked, encrypted, OS-locked, and store rich data (location, messages, app data, media, call logs).
   - Local example: most Nepal Police Cyber Bureau complaints (online fraud, harassment, blackmail, fake profiles) center on mobile phones and apps like Facebook, Messenger, TikTok, WhatsApp, Viber, eSewa/Khalti.
   - Misconception: *"A factory reset wipes the phone clean."* Correction: resets and "deleted" chats can still leave recoverable traces, and cloud backups may persist.

2. **Extraction methods & app data**
   - Definition: levels of extraction — manual (scrolling/photographing), logical (APIs/backups), file-system, and physical (full image).
   - Theory: more invasive = more data but harder; key sources — chat/app databases (often SQLite), call logs, location history, media metadata, cloud-synced data.
   - Mini case: "A suspect deleted a WhatsApp chat, but the app's local database still holds fragments and the cloud backup has the rest — how many places must the investigator check?"

3. **Challenges & integrity**
   - Definition: obstacles unique to mobile — encryption, lock screens, constant connectivity (remote wipe), OS/version diversity, rapid app changes.
   - Theory: isolate immediately (Faraday bag/airplane mode), document, hash extractions, maintain chain of custody just as with disks.
   - Fun element: analogy — a smartphone is a diary that writes itself and locks itself; forensics is about reading it without it noticing — or destroying — the page.

**Check for understanding:**
- MCQ1: Which extraction type generally yields the most data? → physical (full image) ✅
- MCQ2: A seized phone is placed in a Faraday bag primarily to…? → block all signals so it can't be remotely wiped or synced ✅
- Discussion: "Where, besides the phone itself, might 'deleted' chat evidence still exist?"

**Real-life application:** understanding what your phone stores (and how recoverable it is) directly shapes how you protect your own privacy and dispose of old devices.

**Summary:** (1) phones are today's primary crime scene and a discipline of their own; (2) extraction ranges from manual to full physical, with app databases and cloud as key sources; (3) the same integrity rules — isolate, hash, custody — still apply. **Next:** the legal side, and where Nepal stands on cyber forensics.

**Visual cues:** extraction-levels pyramid (manual→logical→file system→physical); phone "data sources" radial map; Faraday bag icon.

---

## S44 — Legal Aspects of Digital Forensics · Cyber Forensics in Nepal (closes Unit 8)

**Hook:** "Investigators recover damning evidence — but the judge rules it inadmissible because of how it was handled. The criminal walks free. In Nepal, who is even allowed to do this work, and under which law?" → law decides whether good forensics matters.

**Concepts & how each will be filled:**

1. **Legal admissibility of digital evidence**
   - Definition: the conditions under which a court will accept digital evidence.
   - Theory: relevance, authenticity, integrity (chain of custody + hashing), proper authorisation (search warrant/legal seizure), and expert testimony; how mishandling makes evidence inadmissible.
   - Global example: evidence excluded due to broken chain of custody or unlawful seizure.
   - Misconception: *"If the evidence is true, the court must accept it."* Correction: even genuine evidence is rejected if illegally obtained or improperly handled.

2. **The legal framework in Nepal**
   - Definition: the laws that recognise and govern electronic evidence in Nepal.
   - Theory: Electronic Transaction Act (ETA) 2063 (2008) — recognises electronic records/evidence and defines cyber offences; Evidence Act provisions; courts' acceptance of electronic records. (Forward link to Unit 9 on cyber law.)
   - Local example: cybercrime complaints prosecuted via the Cyber Bureau under the ETA; ongoing debate about a dedicated, modern cybercrime/data-protection law.
   - Mini case: "A complainant brings only WhatsApp screenshots to the Cyber Bureau — what additional steps are needed before this becomes court-ready evidence?"

3. **Cyber forensics in Nepal — state & challenges**
   - Definition: the current capacity, institutions and gaps in Nepal's digital forensics.
   - Theory/practice: Nepal Police Cyber Bureau as the central body; rising caseload (online fraud, social-media abuse, financial scams); challenges — limited trained personnel, tools/lab capacity, backlog, dependence on foreign platforms for data, evolving legal framework.
   - Fun element: analogy — Nepal's cyber forensics is a small fire brigade facing a fast-growing city: the principles are sound, but capacity must scale with the digital population.

**Check for understanding:**
- MCQ1: Genuine evidence can still be rejected by a court if…? → it was illegally obtained or improperly handled (broken chain of custody) ✅
- MCQ2: In Nepal, electronic records are primarily recognised as evidence under the…? → Electronic Transaction Act (ETA), 2063 ✅
- Discussion: "Should Nepal create a dedicated cybercrime and digital-evidence law beyond the ETA? Argue both sides."

**Real-life application:** as a BIM graduate you may file or face a cyber complaint — knowing what makes evidence admissible (and the Cyber Bureau's role) is directly practical.

**Summary:** (1) admissibility needs legality + authenticity + integrity, not just truth; (2) Nepal relies mainly on the ETA 2063 and the Police Cyber Bureau; (3) capacity must grow with rising cybercrime. **Next unit:** Cyber Law in the context of Nepal — the ETA, Electronic Transaction Rules, and IT/security policy in depth.

**Visual cues:** "admissibility checklist" graphic (relevant ✓ authentic ✓ integrity ✓ legally obtained ✓); Nepal cyber-forensics ecosystem diagram (complaint → Cyber Bureau → lab → court under ETA).

---

## 📋 Unit 8 — End-of-Unit Quiz (added per your preference)

**Section A — MCQ (10):** definition/goal of digital forensics; computer→digital forensics shift; order of the six stages; properties of good evidence; purpose of a write blocker; meaning of matching hashes; what "deleted" really means; file carving; best mobile extraction type; ETA 2063 as basis for electronic evidence in Nepal.
**Section B — Short answer (5):** define chain of custody and why it matters; list and explain the six forensic stages; explain why a bare screenshot is weak evidence; explain how hashing proves integrity; name the central cyber-forensics body in Nepal and two challenges it faces.
**Section C — Applied case (2):** (i) given a Nepal-context phone-seizure scenario, list the correct steps to preserve integrity and chain of custody; (ii) explain why a piece of genuine but mishandled evidence would be ruled inadmissible.
**Section D — Discussion (1):** "Should Nepal invest in a dedicated digital-forensics law and lab capacity beyond the current ETA and Cyber Bureau? Argue both sides."
*(Full questions + answer key generated with the material.)*

---

## Open questions before I generate Unit 8 material
1. Keep the Nepali examples above (Cyber Bureau, ETA 2063, NTC/Ncell CDRs, eSewa/Khalti, Facebook/TikTok/WhatsApp cases)?
2. For tools (S40), keep it category-level only, or name specific tools (Autopsy, EnCase, FTK, Cellebrite) for student awareness?
3. For data recovery & mobile (S42–S43), keep it conceptual as specified, or add light hands-on framing to tie into the lab work?
4. Same as Unit 1: keep 2-MCQ + discussion per session **and** the end-of-unit quiz?
