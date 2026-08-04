#!/usr/bin/env python3
"""IT246 (sixth) Unit 9 deck — Cyber Law in the Context of Nepal (S45–S48) — the FINAL
unit of the course. Built to COURSE_MATERIAL_STANDARD.md INCLUDING the §7A depth rule:
every confusable set is a comparison table, every 'X vs not-X' a concrete-example table,
claims get scaffolding tables — each on its OWN slide, paginated, never squeezed.
Self-contained & PDF-safe. Imports deckkit.py. Diagrams in images/.

⚠️ LEGAL-ACCURACY CAUTION (reused from Unit 2 S10 framing): ETA 2063 (2008) is older and
Nepal's cyber-law landscape has evolved (amendments / proposed IT bills). ALL section
numbers, penalty figures, and dates below are ILLUSTRATIVE of the framework and the debate,
NOT settled current law — every slide that cites specifics carries a 'verify current law
before relying on specifics' caution. Present contested provisions (e.g. Section ~47) as
both protection AND free-speech concern, never one-sided.
Run: python3 build_unit9_pptx.py -> IT246_Unit9.pptx
"""
from deckkit import *

VERIFY = "⚠️ Legal specifics (section numbers, penalties, dates) are ILLUSTRATIVE of the framework and its debate — verify against the current official Nepali text (Nepal Law Commission / Gazette) before relying on them."

# Custom roadmap — deckkit's add_roadmap hardcodes a 'S1–S5' label, wrong for S45–S48.
def unit9_roadmap(done, todo):
    s=prs.slides.add_slide(BLANK); _bg(s,WHITE); _header(s,"Unit 9 — Roadmap","Where each session fits (S45–S48)")
    _card(s,0.7,1.8,5.85,4.55,TEAL,TEAL_T,"✅  THIS UNIT  ·  S45–S48","\n".join(done),body_sz=14)
    _card(s,6.78,1.8,5.85,4.55,GREY,LIGHT,"🎓  COURSE STATUS","\n".join(todo),body_sz=14)
    return s

# ============================================================
#                        BUILD
# ============================================================
add_title("Unit 9 — Cyber Law in the Context of Nepal",
          "IT 246: IT Ethics & Cybersecurity  ·  BIM 6th Semester  ·  Sessions S45–S48  ·  the FINAL unit",
          "Self-contained slides with depth: every concept grounded in comparison & concrete-example TABLES "
          "(Nepal-localised) — no abstraction without instances. Legal specifics are ILLUSTRATIVE — verify current law. Exports to PDF with nothing lost.")

add_outcomes("Unit 9 — Learning Outcomes","cyber law in Nepal  ·  s45–s48",
    "By the end of this unit, you will be able to:",
    ["Explain what cyber law is, why Nepal needs it, and the legal perspective on cybercrime (S45)",
     "Identify the main types of cybercrime recognised under Nepali law and who investigates them (S45)",
     "Describe the key provisions of the Electronic Transaction Act (ETA) 2063 — e-records, digital signatures, offences (S46)",
     "Explain the Electronic Transaction Rules, the Controller & Certifying Authorities, and Nepal's IT Policy (S47)",
     "Explain information-security policy concepts — and synthesise the whole course for exam, lab & project prep (S48)"],
    "This is Unit 9 of IT 246 — the course's closing unit. It turns the ethics, security and forensics of Units 1–8 toward the LAW that governs the digital world in Nepal, then zooms out to tie all nine units together.")

unit9_roadmap(
    ["S45  Legal perspective of cybercrime (cyber law · Cyber Bureau)",
     "S46  Electronic Transaction Act (ETA) 2063",
     "S47  Electronic Transaction Rules · Controller/CAs · IT Policy",
     "S48  Information security & policies + COURSE REVIEW — closes the course"],
    ["Units 1–4  Ethics (should)",
     "Units 5–7  Cybersecurity (protect)",
     "Unit 8   Digital forensics (investigate)",
     "Unit 9   Cyber law (govern & punish) — YOU ARE HERE",
     "🎓  After S48: the full IT 246 course is COMPLETE."])

# ============================================================ S45
add_divider("Session 45 · Lecture hour 1 (of 4)","Cyber Law in Nepal · Legal Perspective of Cybercrime",
    "Someone makes a fake Facebook/TikTok account in your name, posts defamatory photos, and demands money. Which police unit handles this in Nepal, and under which law — there was no 'internet' in the old paper-era Muluki Ain?",
    "OPENING HOOK [~5 min]. Draw out that old law, written for the paper world, cannot reach digital acts. Agenda: what cyber law is → why Nepal needs it → target vs tool → the Cyber Bureau path.")

# ---- S45 C1
concept_understand("S45 · Concept 1 · [THEORY]","What Is Cyber Law",
    "Cyber law (cyberspace law) is the body of law governing computers, networks, the internet, and electronic transactions. It fills the gap where traditional law — written for the physical, paper world — cannot reach digital acts: online identity, anonymity, electronic evidence, and cross-border jurisdiction.",
    ["Traditional law assumes a physical place, paper records, and a known person — the internet breaks all three.",
     "Cyber law gives electronic records/signatures legal validity AND criminalises computer offences.",
     "Global models: India's IT Act 2000; the Budapest Convention on Cybercrime.",
     "Nepal's primary cyber law is the Electronic Transaction Act (ETA) 2063 (2008) — also called the 'Cyber Law'."],
    "s45_timeline.png","Cyber law = traffic rules for a brand-new road where the cars (data) move fast and cross borders.",
    "~8 min. Before ~2004 Nepal had NO statute for electronic records. Keep dates as 'illustrative — verify'. Land: old law can't reach digital acts, so a new law was needed.")
add_comparison_table("S45 · Concept 1 · comparison","Why old (paper-world) law can't reach digital acts",
    ["Dimension","Traditional (paper-world) law","Why it fails online → cyber law's fix"],
    [["Identity","Assumes a known, physical person","Fake profiles & anonymity → rules for electronic identity"],
     ["Evidence","Paper documents, wet-ink signatures","Data, logs, e-records → legal recognition of e-evidence"],
     ["Location / jurisdiction","A crime happens in one place","Acts cross borders instantly → cross-border provisions"],
     ["The record","Physical, hard to copy","Digital, copied infinitely → integrity & signature rules"],
     ["The act","Named in the statute (theft, forgery)","'Hacking', 'source-code damage' didn't exist → new offences"],
     ["Speed & scale","One act, limited reach","One post reaches millions → new harms to regulate"]],
    per_page=6,widths=[1.7,2.6,2.9],fs=11,
    note="Cyber law exists precisely because paper-era law assumed a physical person, place, and record — none of which hold online. "+VERIFY)
concept_apply("S45 · Concept 1 · [THEORY]","What Is Cyber Law",
    "Before the ETA 2063, a Nepali court had no statute making an emailed contract or a digitally signed document legally valid, and no clear offence for 'hacking'. The ETA became Nepal's primary cyber law — enabling e-transactions AND criminalising computer offences — the legal foundation for eSewa, mobile banking, and e-government.",
    "\"Nepal has a dedicated 'Cyber Crime Act'.\" No — Nepal regulates cybercrime mainly through the ETA 2063 (an e-transactions law that ALSO criminalises computer offences), plus provisions in other laws (defamation, the Criminal Code 2074, the Privacy Act 2075). There is no single stand-alone 'Cyber Crime Act'.",
    "Cyber law is the body of law governing computers, networks, the internet, and electronic transactions; it fills the gap where paper-era law cannot reach digital acts (identity, anonymity, e-evidence, cross-border jurisdiction). Nepal's primary cyber law is the ETA 2063 (2008), which both gives e-records/e-signatures legal validity and criminalises computer offences — not a stand-alone 'Cyber Crime Act'.",
    "cyber law · ETA 2063 · fills the paper-law gap · jurisdiction/evidence/identity · not a stand-alone 'Cyber Crime Act'")

# ---- S45 C2
concept_understand("S45 · Concept 2 · [THEORY]","Why Nepal Needs Cyber Law",
    "Nepal needs cyber law because daily life has gone digital: e-banking, e-commerce, e-governance, and social media. Two jobs follow: (1) give electronic records and digital signatures legal validity so they can be trusted and enforced, and (2) punish digital crime that old law could not name.",
    ["e-banking / wallets (eSewa, Khalti, mobile banking) need a law that makes a digital transaction binding.",
     "e-governance (online PAN, Nagarik App, e-services) needs digitally signed records to count in law.",
     "e-commerce (Daraz, online contracts) needs an emailed/e-signed agreement to be enforceable.",
     "Rising online crime (fraud, fake profiles, defamation) needs offences and a body to investigate."],
    None,"No cyber law = a digital signature is 'just a picture' and a hacker breaks no named law.",
    "~7 min. Mini-case: a contract signed & emailed as a PDF — enforceable in a Nepali court? ETA answer: yes, e-records can carry legal recognition.")
add_examples_table("S45 · Concept 2 · concrete examples","Digital services in Nepal — what each needs from cyber law",
    ["Digital service (Nepal)","What it needs from cyber law","Consequence if there were NO law"],
    [["eSewa / Khalti wallet payment","A digital transaction that is legally binding","A disputed payment has no legal standing"],
     ["Mobile / internet banking transfer","Electronic records accepted as proof","Bank & customer can't prove what happened"],
     ["Online PAN / Nagarik App e-service","Digitally signed records that count in law","Citizens still forced to use paper & queues"],
     ["Emailed & e-signed business contract","Recognition of e-signatures = enforceable","'It was only an email' — unenforceable deal"],
     ["Daraz / online purchase","Consumer & transaction rules online","No remedy for online fraud or non-delivery"],
     ["Fake profile impersonating you","A named offence + a body to investigate","Impersonation & harassment go unpunished"]],
    per_page=6,widths=[2.3,2.6,2.6],fs=11,
    note="Every one of these services in Nepal rests on a law that makes digital records/signatures valid AND punishes digital crime — that is exactly why the ETA was enacted.")
concept_apply("S45 · Concept 2 · [THEORY]","Why Nepal Needs Cyber Law",
    "When you top up via eSewa, log into mobile banking, get a digital PAN, or accept online terms, the ETA 2063 is what makes that digital act legally binding. As Nepal digitised banking, government services, and commerce, a law was needed so a digital signature/record carries the same weight as ink on paper — and so digital crime has consequences.",
    "\"Going digital is just about convenience/technology, not law.\" Every digital transaction needs a legal backbone: without a law giving e-records and e-signatures validity, an online contract or payment can't be trusted or enforced, and a hacker or fraudster breaks no named offence. Law is what makes 'digital' trustworthy.",
    "Nepal needs cyber law because e-banking, e-commerce, e-governance and social media have made digital acts central to daily life. Cyber law does two jobs: it gives electronic records and digital signatures the same legal validity as paper (so they can be trusted and enforced), and it criminalises digital crime that paper-era law could not name — the exact rationale behind the ETA 2063.",
    "why cyber law · legal validity of e-records/signatures · e-banking/e-gov/e-commerce · punish digital crime")

# ---- S45 C3
concept_understand("S45 · Concept 3 · [THEORY]","Cybercrime: Computer as Target vs Tool",
    "A cybercrime is an offence in which a computer or network is either the TARGET (attacked) or the TOOL (used to commit the crime). This split is the cleanest way to classify the offences Nepali law recognises — and it decides how the act is understood.",
    ["TARGET crimes: the computer is the victim — hacking/unauthorised access, source-code damage, data theft, DoS.",
     "TOOL crimes: the computer is the weapon against a person — online fraud, cyber-defamation, harassment, fake profiles.",
     "Nepal recognises both, mainly under the ETA plus the Criminal Code 2074 and Privacy Act 2075.",
     "Fake social-media accounts & cyber-defamation are the single largest category the Cyber Bureau handles."],
    "s45_targettool.png","Target = the computer is the victim. Tool = the computer is the weapon.",
    "~8 min. Mini-case: a student edits a friend's photo to humiliate them — which type, and which body investigates? (Tool crime; Cyber Bureau.)")
add_examples_table("S45 · Concept 3 · concrete examples","Cybercrimes recognised in Nepal — target or tool, and the response",
    ["Cybercrime (Nepal example)","Target or tool?","Typical legal response / consequence"],
    [["Unauthorised access / hacking a server","Target","ETA computer-offence; investigated by Cyber Bureau"],
     ["Deleting or altering computer source code","Target","ETA offence — damage to computer source code"],
     ["Stealing a customer database (data breach)","Target","ETA + Privacy Act 2075; breach of confidentiality"],
     ["Online payment / wallet fraud","Tool","Fraud offence; Cyber Bureau traces the money trail"],
     ["Fake profile impersonating a person","Tool","Impersonation/defamation complaint under the ETA"],
     ["Defamatory or obscene post targeting someone","Tool","ETA e-publication offence — but free-speech debate (S46)"]],
    per_page=6,widths=[2.7,1.5,3.0],fs=11,
    note="If the computer is the victim it's a TARGET crime; if it's the weapon against a person, a TOOL crime. "+VERIFY)
concept_apply("S45 · Concept 3 · [THEORY]","Cybercrime: Computer as Target vs Tool",
    "Fake social-media accounts and cyber-defamation are, by volume, the single largest category the Nepal Police Cyber Bureau (established 2018, Bhotahiti, Kathmandu) handles — classic TOOL crimes where the computer is a weapon against a person. Hacking a bank server, by contrast, is a TARGET crime where the computer itself is the victim.",
    "\"Cybercrime just means hacking.\" Hacking is only the TARGET half. Most real Nepali cases are TOOL crimes — fraud, fake profiles, defamation, harassment — where the computer is the weapon, not the victim. Classifying an incident as target vs tool is the first step to naming the right offence.",
    "A cybercrime is an offence where a computer/network is the TARGET (attacked — hacking, source-code damage, data theft, DoS) or the TOOL (used against a person — online fraud, cyber-defamation, harassment, fake profiles). Nepal recognises both, mainly under the ETA plus the Criminal Code 2074 and Privacy Act 2075; fake profiles and cyber-defamation are the largest category the Cyber Bureau handles.",
    "cybercrime · target vs tool · hacking/data theft vs fraud/defamation · Cyber Bureau (2018) · ETA + related laws")

# ---- S45 C4
concept_understand("S45 · Concept 4 · [THEORY]","Reporting Cybercrime · The Cyber Bureau Path",
    "When you are impersonated, harassed, hacked, or defrauded online in Nepal, there is a defined path: preserve evidence, file a complaint with the Nepal Police Cyber Bureau (or local police), and the case is investigated and prosecuted under the ETA. Knowing this path is practical citizenship — the analogy: cyber law needs a new 'traffic police' for a new road.",
    ["Step 1 — preserve evidence: screenshots, URLs, account names, dates (don't just delete and rage-quit).",
     "Step 2 — file the complaint: the Cyber Bureau (Bhotahiti, Kathmandu) or your local police station.",
     "Step 3 — investigation: the Bureau traces accounts, IPs, and money trails and gathers proof.",
     "Step 4 — prosecution: the case proceeds under the ETA through the courts / IT Tribunal."],
    "s45_complaintflow.png","Evidence first, then the Cyber Bureau — panic-deleting the proof is the classic mistake.",
    "~7 min. Emphasise evidence-first. Venue/procedure specifics are illustrative — tell students to verify the current reporting channel and law.")
add_examples_table("S45 · Concept 4 · concrete examples","What to do — real incidents and the reporting response",
    ["Incident (Nepal)","What YOU should do first","Where it goes / outcome"],
    [["Someone opens a fake account in your name","Screenshot the profile, URL, and posts","Complaint to Cyber Bureau → impersonation case"],
     ["You are defrauded in an online payment","Save transaction IDs, chats, receipts","Cyber Bureau traces the money trail"],
     ["A private photo is shared to harass you","Preserve evidence; do NOT retaliate","Harassment complaint under the ETA"],
     ["Your email/social account is hacked","Record the breach details & recover access","Unauthorised-access (target) offence"],
     ["A defamatory post targets you","Keep the post/URL before it's deleted","Complaint filed — but note the free-speech debate"],
     ["A business database is breached","Log the breach; notify affected people","ETA + Privacy Act 2075 investigation"]],
    per_page=6,widths=[2.6,2.5,2.7],fs=11,
    note="The single biggest practical mistake is destroying the evidence. Preserve it, then report to the Cyber Bureau. "+VERIFY)
concept_apply("S45 · Concept 4 · [THEORY]","Reporting Cybercrime · The Cyber Bureau Path",
    "A friend finds a fake TikTok account in their name posting defamatory photos and demanding money. The right move: screenshot everything (profile, URL, posts, dates), then file a complaint with the Cyber Bureau — which can trace the account and pursue it under the ETA. What you must NOT do is angrily delete the messages, tipping off the offender and destroying the proof.",
    "\"Nothing can be done about online abuse in Nepal / I should handle it myself.\" There IS a channel — the Cyber Bureau — and a law (the ETA). The mistake is destroying evidence or retaliating. Preserve proof, don't engage the offender, and report; vigilante 'hacking back' is itself an offence.",
    "If you are impersonated, harassed, hacked, or defrauded online in Nepal, the path is: preserve evidence (screenshots, URLs, dates), file a complaint with the Nepal Police Cyber Bureau (est. 2018, Bhotahiti) or local police, after which the case is investigated and prosecuted under the ETA through the courts / IT Tribunal. Knowing this path is practical citizenship; the biggest error is destroying evidence.",
    "reporting path · preserve evidence first · Cyber Bureau · ETA prosecution · courts / IT Tribunal · don't retaliate")

add_activity("S45 — 'Which body, which law?'  ·  ~5 min",
    ["In pairs (2 min): pick one online-harm scenario (fake profile, hacked account, online fraud, defamatory post).",
     "Decide: is it a TARGET or TOOL crime, who investigates it, and what's your evidence-first first step?",
     "Take 3–4 answers aloud (3 min); classify each on the target/tool grid.",
     "Close: nearly all everyday Nepali cases are TOOL crimes handled by the Cyber Bureau under the ETA."],
    "Seeds: fake TikTok/Facebook account (tool); a hacked email (target); wallet fraud (tool); a defamatory comment (tool — flag the free-speech debate). Reward evidence-first thinking.",
    "ACTIVITY [~5 min].")
add_quiz("S45 — Quick Check  ·  ~5 min",
    [("Q1.  Nepal's PRIMARY cyber law is:","q"),
     ("a) a dedicated Cyber Crime Act   b) ✅ the Electronic Transaction Act (ETA) 2063   c) the Muluki Ain   d) the IT Policy","a"),
     ("     Why: Nepal regulates cybercrime mainly through the ETA 2063 (an e-transactions law that also criminalises computer offences).","o"),
     ("Q2.  A crime where the computer is the TOOL (not the target) is best illustrated by:","q"),
     ("a) hacking a server   b) a DoS attack   c) ✅ online fraud / cyber-defamation   d) source-code damage","a"),
     ("     Why: tool crimes use the computer as a weapon against a person; target crimes attack the computer itself.","o"),
     ("Discussion: give one concrete reason old Nepali law couldn't handle cybercrime — identity, evidence, or jurisdiction.","o")],
    "QUIZ [~5 min]. Draw out the target/tool split and that the ETA — not a stand-alone 'Cyber Crime Act' — is the primary law.")
add_summary("S45 · Summary  ·  [~2 min]",
    ["Cyber law governs the digital world where paper-era law (identity, evidence, jurisdiction) cannot reach.",
     "Nepal's main cyber law is the ETA 2063 — it validates e-records/signatures AND criminalises computer offences.",
     "Cybercrime = computer as target or tool; report via the Cyber Bureau (est. 2018), evidence first."],
    "If you are ever impersonated, harassed, or defrauded online in Nepal, you now know the channel (Cyber Bureau) and the law (ETA) — and that preserving evidence, not retaliating, is the right first move. That is practical citizenship.",
    "S46 — inside the ETA 2063: its two halves, digital signatures, and the debated offences chapter.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S46
add_divider("Session 46 · Lecture hour 2 (of 4)","Electronic Transaction Act (ETA) 2063",
    "What turns a typed-and-emailed agreement into something a Nepali court will enforce — and what turns a curious 'let me just try this login' into a crime with jail time? The same law: the ETA 2063.",
    "OPENING HOOK [~5 min]. The ETA is the heart of Nepal's cyber law. Agenda: what the ETA is (two halves) → e-records & digital signatures → offences & penalties (with the free-speech debate). Keep all figures 'illustrative — verify'.")

# ---- S46 C1
concept_understand("S46 · Concept 1 · [THEORY]","What the ETA 2063 Is & Its Purpose",
    "The Electronic Transaction Act 2063 (2008 AD) is Nepal's primary cyber law. It has TWO halves: most of it ENABLES the digital economy (legal recognition of electronic records and digital signatures, e-commerce, e-governance); one chapter PUNISHES computer-related offences. It is organised in chapters, from e-records and digital signatures to the Controller, service-provider liability, offences, and the IT Tribunal.",
    ["Enacted 2063 BS (2008 AD); designed to enable e-commerce/e-governance AND deter digital crime.",
     "Enable half: e-records, digital-signature validity, dispatch/receipt of records, certificates, the Controller & CAs.",
     "Punish half: the offences-and-penalties chapter (only one part of the whole Act).",
     "In design it mirrors the UNCITRAL Model Law on E-Commerce and India's IT Act."],
    "s46_twohalves.png","The ETA is a two-sided coin: mostly it ENABLES the digital economy; one chapter PUNISHES.",
    "~8 min. Confirm the exact chapter/section structure against the official text. Land the misconception fix: the ETA is not 'only about cybercrime'.")
add_examples_table("S46 · Concept 1 · concrete examples","The ETA's two halves — what each part actually does",
    ["Provision area (illustrative)","ENABLE or PUNISH?","What it does in practice (Nepal)"],
    [["Legal recognition of electronic records","Enable","An e-record can count as evidence like paper"],
     ["Validity of digital signatures","Enable","A digitally signed doc is legally binding"],
     ["Dispatch & receipt of e-records","Enable","Fixes when/where an e-message legally 'arrives'"],
     ["Digital-signature certificates, Controller & CAs","Enable","Sets up the PKI trust system (S47)"],
     ["Unauthorised access / source-code damage","Punish","Named computer offences with penalties"],
     ["Illegal / obscene electronic publication","Punish","The debated offences (esp. Section ~47) — see C3"]],
    per_page=6,widths=[2.7,1.5,3.0],fs=11,
    note="Most of the ETA ENABLES the digital economy; the offences chapter is one part. Provision areas are illustrative of the structure. "+VERIFY)
concept_apply("S46 · Concept 1 · [THEORY]","What the ETA 2063 Is & Its Purpose",
    "The ETA is why eSewa payments, bank e-statements, and digitally signed government forms carry legal weight in Nepal — the 'enable' half at work. The same Act also names hacking and illegal e-publication as offences — the 'punish' half. Both halves come from one law enacted in 2063 BS (2008 AD).",
    "\"The ETA is only about cybercrime / punishment.\" Most of the Act is about ENABLING e-commerce and e-governance — giving electronic records and signatures legal validity. The offences-and-penalties chapter is only one part. Reading the ETA as a pure 'crime law' misses its main purpose.",
    "The ETA 2063 (2008) is Nepal's primary cyber law, with two halves: most of it ENABLES the digital economy (legal recognition of electronic records and digital signatures, e-commerce, e-governance, the Controller & CAs), while one chapter PUNISHES computer offences. Organised in chapters and modelled on the UNCITRAL Model Law and India's IT Act, it is far more than a 'cybercrime law'.",
    "ETA 2063 (2008) · enable + punish · e-records & signatures · offences chapter · UNCITRAL / India IT Act model")

# ---- S46 C2
concept_understand("S46 · Concept 2 · [THEORY]","Electronic Records & Digital Signatures",
    "The ETA gives an electronic record and a digital signature the same legal validity as paper and a handwritten signature. A digital signature uses asymmetric (public/private key) cryptography: the signer signs with a PRIVATE key, and anyone can verify with the matching PUBLIC key — delivering authentication, integrity, and non-repudiation.",
    ["Legal recognition: an e-record/e-signature can be as binding as ink on paper.",
     "Mechanism: sign with the private key (secret); verify with the public key (shared).",
     "Authentication (WHO signed) + Integrity (NOT altered) + Non-repudiation (can't deny it later).",
     "In Nepal, digital signatures are issued under a PKI framework for banking & government use (S47)."],
    "s46_digsig.png","A digital signature is a wax seal that also fingerprints the message — change one word and the seal breaks.",
    "~8 min. Mini-case: a vendor denies sending a purchase-order email — how does a digital signature establish non-repudiation? (Only their private key could have signed it.)")
add_examples_table("S46 · Concept 2 · concrete examples","Paper world vs electronic equivalent — and the property it gives",
    ["Paper-world thing","Electronic equivalent (ETA)","Security property it provides"],
    [["Handwritten signature","Digital signature (private key)","Authentication — proves who signed"],
     ["Sealed, unaltered document","Hash-protected signed record","Integrity — proves it was not changed"],
     ["'I never signed that' denial fails","Only your private key could sign","Non-repudiation — signer can't deny it"],
     ["Notarised / certified copy","Digital-signature certificate (from a CA)","Trust — a licensed CA vouches for identity"],
     ["Posting a letter (proof of sending)","Dispatch/receipt rules for e-records","Certainty of when a message legally 'arrived'"],
     ["Paper contract in a court file","Electronic record admitted as evidence","Legal recognition — e-record counts in law"]],
    per_page=6,widths=[2.4,2.6,2.8],fs=11,
    note="A digital signature does what a wet-ink signature does — and more (integrity + non-repudiation via cryptography). "+VERIFY)
concept_apply("S46 · Concept 2 · [THEORY]","Electronic Records & Digital Signatures",
    "A vendor emails a signed purchase order, then denies sending it. Because the order was digitally signed with the vendor's PRIVATE key, anyone can verify it with the vendor's PUBLIC key — establishing non-repudiation: only the vendor could have produced that signature. This is exactly why Nepali banks and government e-services accept digitally signed documents.",
    "\"A scanned image of my signature = a digital signature.\" A scanned signature is just a picture — anyone can copy-paste it and it proves nothing. A true digital signature is cryptographic: it binds a specific signer to a specific unaltered document and cannot be forged or reused, which is what gives it legal weight under the ETA.",
    "Under the ETA, an electronic record and a digital signature carry the same legal validity as paper and a handwritten signature. A digital signature uses asymmetric cryptography — sign with the private key, verify with the public key — providing authentication (who signed), integrity (not altered), and non-repudiation (cannot be denied). This is the legal-and-technical backbone of trusted e-transactions in Nepal.",
    "digital signature · asymmetric keys (private signs / public verifies) · authentication · integrity · non-repudiation")

# ---- S46 C3
concept_understand("S46 · Concept 3 · [THEORY] [EXAMPLE]","Offences & Penalties — and the Free-Speech Debate",
    "The ETA's offences chapter criminalises acts such as unauthorised access ('hacking'), damage to computer source code, illegal/obscene/defamatory electronic publication, breach of confidentiality/privacy, and computer fraud and forgery. Penalties are commonly cited as fines up to about Rs. 200,000 and/or imprisonment up to about 5 years for several core offences. All figures are ILLUSTRATIVE — verify the exact section numbers and amounts.",
    ["Core offences: hacking, source-code damage, illegal e-publication, privacy breach, computer fraud/forgery.",
     "Commonly cited penalties: ~Rs. 200,000 fine and/or up to ~5 years' jail (VERIFY exact figures).",
     "The much-cited 'Section ~47' on illegal electronic publication is the most applied — and most criticised.",
     "Live debate: critics call the wording vague/over-broad and a threat to free speech; supporters see it as protection against real online harm."],
    None,"Same law: it makes your e-signature binding AND can make a careless post a criminal matter.",
    "~8 min. Reuse the Unit 2 S10 framing: present BOTH sides (protection vs free-speech chill). State section numbers/penalties as 'illustrative — verify current law', never as settled fact.")
add_examples_table("S46 · Concept 3 · offence → provision → penalty","ETA offences — provision, illustrative penalty, and consequence",
    ["Offence (Nepal)","Provision (illustrative)","Illustrative penalty → consequence"],
    [["Unauthorised access / hacking","ETA computer-offence section","~Fine and/or jail → criminal record"],
     ["Damage / alteration of source code","ETA source-code section","~Fine and/or imprisonment → liability for damage"],
     ["Illegal / obscene / defamatory e-publication","Section ~47 (most-cited)","~Up to Rs. 200,000 and/or ~5 yrs → the debated one"],
     ["Breach of confidentiality / privacy","ETA + Privacy Act 2075","~Fine and/or jail → data-protection liability"],
     ["Computer fraud & forgery","ETA fraud/forgery section","~Fine and/or jail → restitution + record"],
     ["False statement to obtain a certificate","ETA certificate section","~Penalty → certificate void, prosecution"]],
    per_page=6,widths=[2.6,2.0,3.0],fs=10.5,
    note="Section numbers & penalty figures are ILLUSTRATIVE of the framework, frequently misquoted. "+VERIFY)
concept_apply("S46 · Concept 3 · [THEORY] [EXAMPLE]","Offences & Penalties — and the Free-Speech Debate",
    "In Nepal, individuals have been arrested over Facebook/TikTok posts and comments under the ETA's electronic-publication offence (often cited as 'Section ~47'). Present both sides: supporters say it curbs genuine online harm (defamation, obscenity, fraud); critics argue the wording is vague and over-broad and has been used to silence legitimate criticism — a core reason behind reform/replacement proposals. Verify the current law before relying on specifics.",
    "\"The ETA clearly and precisely defines online defamation and obscenity.\" Critics argue 'Section ~47' is vague and over-broad, which is exactly why it is contested and why reform is proposed. Treat the specific section number and penalty as 'illustrative — verify'; teach the CONCEPT and the debate, not a memorised figure as settled current law.",
    "The ETA's offences chapter criminalises hacking, source-code damage, illegal/obscene/defamatory e-publication, privacy breach, and computer fraud/forgery, with penalties commonly cited as fines up to ~Rs. 200,000 and/or up to ~5 years' jail (verify). The most-applied and most-criticised provision (often 'Section ~47') on electronic publication raises a genuine free-speech vs online-harm tension — present both sides, and verify current law before citing specifics.",
    "offences chapter · Section ~47 (illustrative) · penalties (verify) · free-speech vs online-harm debate · reform proposed")

add_activity("S46 — 'Protection or over-reach?'  ·  ~5 min",
    ["In pairs (2 min): should posting a defamatory comment online be treated more seriously than saying it in person? Argue using the ETA.",
     "List one reason the e-publication offence PROTECTS people, and one reason it risks free speech.",
     "Take 3–4 answers aloud (3 min); keep both sides on the board.",
     "Close: the honest position holds BOTH truths — real online harm is real, and vague law can chill speech."],
    "Reward both-sides reasoning (Unit 2 S10 style). Remind students that specific section numbers/penalties are illustrative — the debate and concept matter more than a memorised figure. Verify current law.",
    "ACTIVITY [~5 min].")
add_quiz("S46 — Quick Check  ·  ~5 min",
    [("Q1.  A digital signature primarily provides authentication, integrity, and:","q"),
     ("a) encryption speed   b) ✅ non-repudiation   c) anonymity   d) lower cost","a"),
     ("     Why: only the signer's private key could produce it, so the signer cannot later deny signing.","o"),
     ("Q2.  The most frequently applied and criticised ETA provision (often used for social-media posts) is:","q"),
     ("a) the digital-signature section   b) ✅ the electronic-publication offence ('Section ~47' — verify)   c) the Controller section   d) the IT Tribunal","a"),
     ("     Why: the e-publication offence is the most-used and most-debated part — treat the exact number as 'verify current law'.","o"),
     ("Discussion: should an online defamatory comment be treated more seriously than the same words in person? Argue via the ETA.","o")],
    "QUIZ [~5 min]. Reinforce non-repudiation and the two-sided free-speech debate. Section numbers are illustrative — verify.")
add_summary("S46 · Summary  ·  [~2 min]",
    ["The ETA 2063 has two halves: it ENABLES the digital economy AND PUNISHES computer offences.",
     "Digital signatures give authentication, integrity, and non-repudiation — legal validity for e-records.",
     "The offences chapter (esp. the debated 'Section ~47') carries fines + jail and raises a free-speech tension (verify specifics)."],
    "Every time you e-sign a document, use mobile banking, or accept online terms in Nepal, the ETA makes that binding — and the same law can make a careless post a criminal matter. Understanding both halves is understanding your own digital rights and risks.",
    "S47 — the Rules that operationalise the Act (ETR), the Controller & CAs, and Nepal's IT Policy.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S47
add_divider("Session 47 · Lecture hour 3 (of 4)","Electronic Transaction Rules · Controller & CAs · IT Policy",
    "An Act says 'digital signatures are legal' — but WHO actually issues them, WHO checks the issuer is trustworthy, and WHAT national plan pushes Nepal toward a digital economy? That's the Rules, the Controller, and the Policy.",
    "OPENING HOOK [~5 min]. From law on paper to a working system. Agenda: the ETR (procedures) → the Controller & CAs (PKI) → the IT Policy (national goals). Confirm rule numbers/policy version before delivery.")

# ---- S47 C1
concept_understand("S47 · Concept 1 · [THEORY]","Electronic Transaction Rules (ETR)",
    "The Electronic Transaction Rules (commonly cited as ETR 2064 BS) are subordinate legislation made under the ETA that spell out the PROCEDURES — how the Act is actually implemented. Where the Act states the principle ('digital signatures are legal'), the Rules state the mechanics: how Certifying Authorities are licensed, how certificates are issued/suspended/revoked, the Controller's duties, standards, audit, and fees.",
    ["The Act is the parent law (passed by Parliament); the Rules are executive procedures made under it.",
     "Rules cover: licensing of CAs, certificate issue/suspend/revoke, Controller duties, standards/audit, fees.",
     "Rules are easier to amend than the Act — detail changes without re-passing the whole law.",
     "Confirm the exact year and rule numbers against the official text (commonly cited as ETR 2064)."],
    None,"The Act sets the principle; the Rules are the operating manual that makes it work.",
    "~7 min. Local example: the licensing requirements a Nepali entity must meet to operate as a CA under the Office of the Controller. Confirm year/rule numbers before delivery.")
add_comparison_table("S47 · Concept 1 · comparison","Act vs Rules — the parent law vs the procedures",
    ["Question","The Act (ETA)","The Rules (ETR)"],
    [["What is it?","The parent primary law","Subordinate procedures under the Act"],
     ["Who makes it?","Parliament (legislature)","The executive/government under the Act"],
     ["What does it do?","States principles & offences","Spells out the how-to (licensing, certificates, fees)"],
     ["How binding?","Primary legislation","Binding, but derives authority from the Act"],
     ["How easy to change?","Hard — needs Parliament","Easier — amended by the executive"],
     ["Example content","'Digital signatures are legally valid'","'How a CA is licensed and audited'"]],
    per_page=6,widths=[1.7,2.6,2.9],fs=11,
    note="Rules and the Act are NOT the same thing: the Act is the parent law; the Rules are the detailed procedures issued under it. "+VERIFY)
concept_apply("S47 · Concept 1 · [THEORY]","Electronic Transaction Rules (ETR)",
    "The ETA says a licensed Certifying Authority may issue digital-signature certificates. The ETR is what actually spells out HOW a Nepali entity becomes a licensed CA — the application, the standards it must meet, audits, and fees, plus how a certificate is suspended or revoked. Without the Rules, the Act's principle would have no working machinery.",
    "\"Rules and the Act are the same thing.\" They are different in kind: the Act is the parent law passed by Parliament (principles and offences); the Rules are detailed procedures issued by the executive under the Act, and are easier to amend. Confusing the two is a classic exam mistake.",
    "The Electronic Transaction Rules (commonly ETR 2064) are subordinate legislation under the ETA that specify the PROCEDURES to implement the Act: licensing of Certifying Authorities, issuing/suspending/revoking digital-signature certificates, the Controller's duties, standards, audit, and fees. The Act (Parliament) states principles; the Rules (executive) operationalise them and are easier to amend.",
    "ETR 2064 · subordinate legislation · procedures under the Act · CA licensing & certificates · Act ≠ Rules")

# ---- S47 C2
concept_understand("S47 · Concept 2 · [THEORY]","The Controller & Certifying Authorities (PKI in Nepal)",
    "The Office of the Controller of Certification (OCC, the 'Controller'), under the Ministry of Communication and Information Technology, is the government body that LICENSES and SUPERVISES Certifying Authorities (CAs). CAs, in turn, issue digital-signature certificates to the public. Together they form Nepal's PKI trust hierarchy: Controller (root) → licensed CAs → end-user certificates.",
    ["Controller = root authority: licenses CAs, sets standards, audits, can suspend/revoke.",
     "Certifying Authorities = licensed bodies that issue certificates after verifying identity.",
     "End users (citizens, banks, businesses) hold certificates used to sign and verify.",
     "Trust flows DOWN the chain — a certificate is only as trustworthy as the CA and Controller above it."],
    "s47_pki.png","Controller → CAs → users: trust flows down a chain, like a notary system for the digital world.",
    "~8 min. Mini-case: a CA issues a certificate without verifying identity and it's used in fraud — the Controller's supervisory/audit role is exactly what should catch and sanction that.")
add_examples_table("S47 · Concept 2 · scaffolding","The PKI trust chain — who does what",
    ["Role in the chain","Who / where (Nepal)","What they do → why it matters"],
    [["Controller (root authority)","Office of the Controller of Certification (under MoCIT)","Licenses & supervises CAs → sets the root of trust"],
     ["Certifying Authority (CA)","Licensed bodies under the Controller","Issue certificates after verifying identity"],
     ["Certificate","Issued to an end user","Binds a public key to a verified identity"],
     ["Subscriber / end user","Citizen, bank, business","Signs documents with their private key"],
     ["Relying party","Anyone verifying a signature","Trusts the signature via the chain above"],
     ["Audit / revocation","Controller's supervisory power","Catches a CA that issues certificates carelessly"]],
    per_page=6,widths=[1.9,2.6,2.9],fs=11,
    note="Trust flows down: Controller → CA → certificate → user. A certificate is only as trustworthy as the chain that issued it. "+VERIFY)
concept_apply("S47 · Concept 2 · [THEORY]","The Controller & Certifying Authorities",
    "When a Nepali bank or taxpayer uses a digital signature, the certificate traces back through a licensed CA to the Office of the Controller of Certification. If a CA issued a certificate without properly verifying identity and it was used in fraud, the Controller's supervisory and audit role is what should detect it, sanction the CA, and revoke the certificate — that oversight is what makes the whole system trustworthy.",
    "\"Any website or company can just hand out legally valid digital certificates.\" In Nepal, only CAs LICENSED and SUPERVISED by the Controller can issue legally recognised certificates. The Controller is the root of trust; an unlicensed 'certificate' has no legal standing. That supervised chain is the entire point of PKI.",
    "The Office of the Controller of Certification (the Controller, under MoCIT) licenses and supervises Certifying Authorities, which issue digital-signature certificates to the public. This forms Nepal's PKI trust hierarchy — Controller (root) → licensed CAs → end-user certificates — where trust flows down the chain and the Controller's audit/revocation power keeps CAs honest.",
    "Controller (OCC) · Certifying Authorities · PKI trust hierarchy · licenses & supervises · root of trust · MoCIT")

# ---- S47 C3
concept_understand("S47 · Concept 3 · [THEORY]","The IT Policy of Nepal",
    "Nepal's IT Policy is a national policy document setting the government's VISION and GOALS for ICT development — not a law, but a strategic framework. Its goals typically include building ICT infrastructure, expanding e-governance, growing the IT industry/exports and jobs, promoting digital literacy and inclusion, and improving information security. It is direction, not a binding legal mechanism.",
    ["A policy sets DIRECTION and GOALS; it does not itself punish or bind like a law.",
     "Typical goals: infrastructure, e-governance, IT industry/exports & jobs, digital literacy, security.",
     "Versions/framings evolve — e.g. IT Policy 2072 and 'Digital Nepal Framework' ambitions (confirm current version).",
     "The chain: Policy sets the destination; the Act + Rules provide the binding legal road."],
    None,"IT Policy = the destination on the map; the ETA is the road law; the ETR + Controller keep the road usable.",
    "~7 min. Discussion seed: name one IT Policy goal Nepal has progressed on and one it hasn't, from daily life. Confirm which policy version is current for teaching.")
add_comparison_table("S47 · Concept 3 · comparison","Act vs Rules vs Policy — the three, side by side",
    ["Question","Act (ETA)","Rules (ETR)","Policy (IT Policy)"],
    [["Who makes it?","Parliament","Executive (under the Act)","Government (as strategy)"],
     ["Legally binding?","Yes — primary law","Yes — under the Act","No — a direction/vision"],
     ["What it does","States principles & offences","Spells out procedures","Sets national goals & vision"],
     ["Can it punish?","Yes (offences chapter)","Enforces procedures","No — it guides, not punishes"],
     ["Example","'E-signatures are valid'","'How a CA is licensed'","'Make Nepal an IT/knowledge hub'"]],
    per_page=5,widths=[1.5,2.2,2.2,2.4],fs=10.5,
    note="A classic exam trap: the IT Policy is NOT binding law. Policy directs; the Act + Rules bind. "+VERIFY)
concept_apply("S47 · Concept 3 · [THEORY]","The IT Policy of Nepal",
    "When you obtain a digital-signature certificate for tax, banking, or e-government, it traces through a licensed CA to the Controller — that's the Act + Rules at work. WHICH digital services exist for you at all, though, is shaped by national IT Policy goals (e-governance, digital literacy, the 'Digital Nepal' ambition). Policy decides the direction; law makes each step binding.",
    "\"The IT Policy is legally binding like the ETA.\" It is not. Policy sets direction and goals; laws (the ETA) and rules (the ETR) provide the binding legal mechanism. Citing the IT Policy as if it could criminalise or enforce is a common and costly mistake.",
    "Nepal's IT Policy is a national strategic framework setting the government's vision and goals for ICT — infrastructure, e-governance, IT industry/exports, digital literacy and inclusion, and information security (e.g. IT Policy 2072 / 'Digital Nepal' ambitions). Crucially it is NOT binding law: policy sets direction, while the Act and Rules provide the binding legal mechanism.",
    "IT Policy · strategic framework (not law) · e-gov/infrastructure/literacy goals · Digital Nepal · policy directs, law binds")

add_activity("S47 — 'Act, Rule, or Policy?'  ·  ~5 min",
    ["In pairs (2 min): sort five statements into Act / Rules / Policy (e.g. 'e-signatures are valid'; 'how a CA is licensed'; 'make Nepal an IT hub').",
     "For each, say WHO makes it and whether it is legally binding.",
     "Take 3–4 answers aloud (3 min).",
     "Close: only the Act & Rules are binding; the Policy sets goals — this is a favourite exam distinction."],
    "Answers: 'e-signatures valid' = Act; 'how a CA is licensed' = Rules; 'make Nepal an IT hub / digital literacy' = Policy. Reward correct who-makes-it + binding reasoning.",
    "ACTIVITY [~5 min].")
add_quiz("S47 — Quick Check  ·  ~5 min",
    [("Q1.  In Nepal, the body that LICENSES and SUPERVISES Certifying Authorities is the:","q"),
     ("a) a private CA   b) ✅ Office of the Controller of Certification   c) the Cyber Bureau   d) the IT Tribunal","a"),
     ("     Why: the Controller is the root of the PKI trust chain — it licenses/supervises CAs, which issue certificates.","o"),
     ("Q2.  Which is a STRATEGIC FRAMEWORK rather than binding law?","q"),
     ("a) the ETA   b) the ETR   c) ✅ the IT Policy of Nepal   d) the Criminal Code","a"),
     ("     Why: the IT Policy sets national goals/direction; the Act and Rules are the binding legal mechanism.","o"),
     ("Discussion: name one IT Policy goal Nepal has progressed on, and one it has not — with evidence from daily life.","o")],
    "QUIZ [~5 min]. Nail the Act/Rules/Policy distinction and the Controller's role in PKI.")
add_summary("S47 · Summary  ·  [~2 min]",
    ["The ETR are procedures implementing the ETA — licensing of CAs, certificates, the Controller's duties.",
     "The Controller (OCC) licenses & supervises CAs in Nepal's PKI trust chain (Controller → CAs → users).",
     "The IT Policy sets non-binding national digital goals; the Act + Rules are what actually bind."],
    "When you get a digital-signature certificate for tax, banking, or e-government, it traces through a licensed CA to the Controller — and national IT Policy goals shape which digital services exist for you at all. This is the machinery behind Nepal's digital life.",
    "S48 — information-security policies, then a full course review and exam/project prep to close IT 246.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S48
add_divider("Session 48 · Lecture hour 4 (of 4) — CLOSES UNIT 9 & THE COURSE","Information Security & Policies · Course Review & Wrap-up",
    "Laws punish crime AFTER it happens — but a good security POLICY tries to stop it before. As we close the course: how does an organization (or you) actually write the rules that keep data safe — and how do all 9 units fit together?",
    "OPENING HOOK [~5 min]. Part new theory (infosec policies), part course-wide synthesis + exam/project prep. Agenda: CIA triad → security policy → where law meets policy → the whole course as one arc.")

# ---- S48 C1
concept_understand("S48 · Concept 1 · [THEORY]","Information Security & the CIA Triad",
    "Information security is protecting information's Confidentiality, Integrity, and Availability — the CIA triad. Confidentiality = only authorised people see the data; Integrity = the data is accurate and unaltered; Availability = the data is there when needed. Lose any one corner and the information is not secure. This ties Units 5–7 (cybersecurity, personal security, social engineering) to the legal/policy controls here.",
    ["Confidentiality — keep data secret from the unauthorised (encryption, access control).",
     "Integrity — keep data accurate & unaltered (hashing, change control, backups).",
     "Availability — keep data & services reachable when needed (redundancy, uptime).",
     "Law punishes AFTER a breach; security protects the triad BEFORE — the two work together."],
    "s48_cia.png","Confidentiality, Integrity, Availability — lose any one corner and the data isn't secure.",
    "~7 min. Local example: a Nepali bank's customer-data protection duties and NRB/regulatory IT-security expectations. Link back to Units 5–7 explicitly.")
add_examples_table("S48 · Concept 1 · concrete examples","The CIA triad — what each protects and the threat if lost",
    ["CIA element","What it protects (Nepal example)","Threat / consequence if lost"],
    [["Confidentiality","A bank's customer KYC data stays private","Data leak → privacy breach, ETA/Privacy Act liability"],
     ["Integrity","An account balance is accurate & unaltered","Tampered records → fraud, wrong decisions"],
     ["Availability","eSewa/mobile banking works when needed","Downtime/DoS → customers locked out, lost trust"],
     ["Confidentiality","Exam results seen only by the right office","Premature leak → unfairness, reputational harm"],
     ["Integrity","A digitally signed contract not modified","Silent alteration → disputes, non-repudiation lost"],
     ["Availability","A hospital system reachable in an emergency","Outage → direct risk to patient care"]],
    per_page=6,widths=[1.7,2.9,2.7],fs=11,
    note="Security means protecting ALL THREE at once — confidentiality, integrity, AND availability. A system can 'work' yet still fail the triad.")
concept_apply("S48 · Concept 1 · [THEORY]","Information Security & the CIA Triad",
    "A Nepali bank must keep customer data confidential (privacy), accurate (integrity), and reachable (availability) — and NRB/regulatory IT-security expectations push exactly this. Units 5–7 taught the attacks (malware, weak passwords, social engineering); the CIA triad is the frame those defences protect, and Unit 9's law is what governs it when it fails.",
    "\"Security just means keeping data secret (confidentiality).\" Confidentiality is only one corner. A system that keeps data secret but lets it be silently altered (integrity failure) or knocked offline during a festival rush (availability failure) is still insecure. Real security protects all three corners of the triad together.",
    "Information security protects the Confidentiality, Integrity, and Availability of information — the CIA triad. Confidentiality restricts who sees data, integrity keeps it accurate and unaltered, and availability keeps it reachable when needed; losing any one corner means the information is not secure. It ties the attacks studied in Units 5–7 to the legal and policy controls of Unit 9.",
    "information security · CIA triad · confidentiality / integrity / availability · protect all three · links Units 5–7")

# ---- S48 C2
concept_understand("S48 · Concept 2 · [THEORY]","Information Security Policy (ISP)",
    "An information security policy is a documented set of rules governing how an organization protects its information assets. It sits at the top of a hierarchy — POLICY (the rule & intent) → STANDARDS (measurable requirements) → PROCEDURES (step-by-step how-to) → GUIDELINES (advisory). Security is governance + people + process, not only firewalls.",
    ["Typical components: acceptable-use, access-control & password, data classification, incident response, BYOD, backup/retention.",
     "Hierarchy: policy states WHAT & WHY; standards make it measurable; procedures say HOW.",
     "It aligns with Nepal's Privacy Act 2075 / data-protection expectations and the ETA (verify current status).",
     "Good policy reduces both breaches AND legal liability — it operationalises protection."],
    "s48_policyhierarchy.png","Policy → Standard → Procedure → Guideline: from 'protect our data' down to 'here's how to reset a password'.",
    "~8 min. Mini-case: an employee uses a personal USB / shares a password — which policy should have prevented it, and what's the incident-response step?")
add_examples_table("S48 · Concept 2 · concrete examples","Information-security policy components — and the threat each stops",
    ["Policy component","What it governs","Threat it stops (Nepal example)"],
    [["Acceptable-use policy (AUP)","How staff may use company systems","Misuse, shadow IT, risky browsing"],
     ["Access control & password policy","Who can access what; strong passwords","Weak/shared passwords → account takeover"],
     ["Data classification","How data is labelled & handled","Sensitive KYC data treated carelessly"],
     ["Incident response","Steps when a breach occurs","Slow, chaotic reaction that worsens a breach"],
     ["BYOD policy","Personal devices on the network","An infected personal phone/USB spreads malware"],
     ["Backup & retention","How data is backed up & kept","Ransomware/data loss with no recovery"]],
    per_page=6,widths=[2.1,2.6,2.7],fs=11,
    note="Security is governance + people + process, not only firewalls — user behaviour and written policy matter as much as technology.")
concept_apply("S48 · Concept 2 · [THEORY]","Information Security Policy (ISP)",
    "An employee plugs in a personal USB and shares a password 'to save time'. A BYOD/acceptable-use policy plus an access-control & password policy should have prevented it; if malware got in, the incident-response procedure defines the steps (contain, eradicate, recover, report). This is where Unit 9's law meets daily practice — good policy reduces both the breach and the legal liability.",
    "\"Security is only a technical / IT-team problem.\" It is governance + people + process. Firewalls don't stop an employee sharing a password or losing an unencrypted laptop — policy, training, and user behaviour do. Most breaches exploit people and process gaps, not just technology.",
    "An information security policy is a documented set of rules for protecting an organization's information assets, structured as policy → standards → procedures → guidelines and covering acceptable use, access control/passwords, data classification, incident response, BYOD, and backup/retention. It aligns with Nepal's Privacy Act 2075 and the ETA, and treats security as governance + people + process, not only technology.",
    "information security policy · policy→standard→procedure → guideline · AUP · access/incident/BYOD/backup · people + process")

# ---- S48 C3
concept_understand("S48 · Concept 3 · [THEORY]","Where Law Meets Policy",
    "Law and policy play different, complementary roles. The ETA CRIMINALISES wrongdoing (punishment after harm); the IT Policy DIRECTS national digital goals; and information-security policies OPERATIONALISE protection inside organizations (stopping harm before it happens). Good internal policy reduces both breaches and legal liability — it is where the law lands in daily practice.",
    ["ETA (law) — criminalises: acts after harm has occurred, with penalties.",
     "IT Policy (strategy) — directs: sets national goals, non-binding.",
     "Security policy (organizational) — operationalises: prevents harm inside the org, before it happens.",
     "Together: prevention (policy) + deterrence/punishment (law) + direction (national policy)."],
    None,"Law punishes after; policy protects before; national policy points the way — three layers, one goal.",
    "~5 min. Land the synthesis: the ETA criminalises, the IT Policy directs, and infosec policy operationalises — a good policy reduces breaches AND legal liability.")
add_comparison_table("S48 · Concept 3 · comparison","Law vs national policy vs organizational security policy",
    ["Layer","Role","When it acts","Nepal example"],
    [["ETA (cyber law)","Criminalises & punishes","AFTER harm occurs","Prosecuting a hacker or fraudster"],
     ["IT Policy (national)","Directs & sets goals","Ongoing strategy","'Digital Nepal' e-governance ambition"],
     ["Security policy (org)","Operationalises protection","BEFORE harm occurs","A bank's AUP, password & incident policy"],
     ["Together","Prevent + deter + direct","All the time","Fewer breaches AND less legal liability"]],
    per_page=4,widths=[1.9,2.2,1.9,2.5],fs=11,
    note="The ETA criminalises, the IT Policy directs, and information-security policies operationalise protection — good policy reduces both breaches AND legal liability.")
concept_apply("S48 · Concept 3 · [THEORY]","Where Law Meets Policy",
    "A Nepali bank's information-security policy (prevention) keeps customer data safe day-to-day; if a breach still happens, the ETA and Privacy Act 2075 (law) govern the consequences; and the national IT Policy (direction) shaped the digital services that existed to protect in the first place. As a professional you operate inside all three layers at once.",
    "\"Once there's a law, we don't need internal policy\" — OR — \"policy is enough, the law is irrelevant.\" Neither is true. Law punishes after the fact and deters; policy prevents before the fact and reduces liability. You need prevention (policy) AND deterrence (law) — they are complementary layers, not substitutes.",
    "Law and policy are complementary: the ETA criminalises wrongdoing (punishment after harm), the national IT Policy directs digital goals, and organizational information-security policies operationalise protection (stopping harm before it happens). Good internal policy reduces both breaches and legal liability, so a professional works within all three layers — prevention, deterrence, and direction — at once.",
    "law vs policy · criminalise / direct / operationalise · prevention + deterrence · reduces breach + liability")

# ---- S48 Part B: Course-wide review
add_divider("Session 48 · Part B — COURSE-WIDE REVIEW","The Whole Course as One Arc — all 9 units",
    "Step back and see IT 246 as one connected story: ethics (should) → security (protect) → forensics (investigate) → law (govern & punish), with Nepal context binding Units 8–9.",
    "COURSE SYNTHESIS. Walk the arc on the diagram, then the 9-unit table. This is the mental map students should carry into the exam.")
concept_understand("S48 · Review · [SYNTHESIS]","IT 246 — the through-line of all nine units",
    "The whole course forms one connected arc: ETHICS says what you SHOULD do (Units 1–4), SECURITY protects systems (Units 5–7), FORENSICS investigates when defence fails (Unit 8), and LAW governs and punishes (Unit 9). Nepal context binds the last two: the Cyber Bureau investigates, the ETA prosecutes. Seeing the arc — not nine disconnected topics — is what makes the material stick.",
    ["Ethics (U1–U4): ethics vs law, professional duties, IP, software/organizational ethics.",
     "Security (U5–U7): cybersecurity fundamentals, personal security, social engineering.",
     "Forensics (U8): investigating incidents, evidence handling, cyber forensics in Nepal.",
     "Law (U9): the ETA, ETR, Controller/CAs, IT Policy, information-security policy — this unit."],
    "s48_coursemap.png","Ethics (should) → Security (protect) → Forensics (investigate) → Law (govern & punish).",
    "COURSE SYNTHESIS. Present the arc as ONE story; the Nepal thread (Cyber Bureau, ETA) binds Units 8–9. Encourage students to redraw this map from memory.")
add_examples_table("S48 · Review · the 9 units","IT 246 on a page — each unit, its focus, and the through-line",
    ["Unit","Focus","Key concepts to revise"],
    [["U1 Overview of Ethics","Ethics vs law, CSR","Ethical decision framework, why IT ethics is distinct"],
     ["U2 Ethics for IT Workers/Users","Professionalism, privacy","Codes, anonymity, social-networking harms"],
     ["U3 Intellectual Property","Protecting creations","Copyright, patent, trade secrets, plagiarism, cybersquatting"],
     ["U4 Software Dev & IT Orgs","How software is built","Quality, outsourcing, whistle-blowing, green computing"],
     ["U5 Fundamentals of Cybersecurity","Cyberspace & attacks","Attack types, attacker 'hats', risks mitigated"],
     ["U6 Personal Cybersecurity","Protecting yourself","Posture, devices/IoT, passwords, work-from-home"],
     ["U7 Social Engineering & Cyber Terror","Exploiting trust","Countermeasures, cyber-terrorism effects"],
     ["U8 Digital Forensics","Investigating incidents","Stages, evidence handling, mobile & cyber forensics in Nepal"],
     ["U9 Cyber Law in Nepal","Governing the digital world","ETA 2063, ETR, Controller/CAs, IT Policy, infosec policy"]],
    per_page=9,widths=[2.2,2.3,3.0],fs=10.5,
    note="The through-line: ethics (should) → security (protect) → forensics (investigate) → law (govern & punish). Nepal context binds Units 8–9.")

# ---- S48 Part C: Exam prep
add_examples_table("S48 · Part C — Exam prep","Likely question shapes, how to answer, and high-yield topics",
    ["Question shape","Answer technique","High-yield topic"],
    [["Definition (ethics, IP types, CIA)","Define → explain → Nepal example","U1 framework · U3 IP · CIA triad"],
     ["Compare/contrast","Use a comparison table structure","Act vs Rules vs Policy; ethics vs law; hat colours"],
     ["Applied Nepal case","Classify → cite the concept → steps","Classify a cybercrime; forensic chain of custody"],
     ["'Explain provisions of the ETA'","Two halves → key offences → note 'verify'","ETA 2063; Controller's role"],
     ["Attack/defence taxonomy","Name → mechanism → countermeasure","U5 attack types; U7 social engineering"],
     ["Discussion / argue both sides","State both, then a reasoned view","Section ~47: protection vs free speech"]],
    per_page=6,widths=[2.4,2.6,2.5],fs=10.5,
    note="Answer technique: define → explain → Nepal example → diagram where useful. PITFALLS: confusing Act/Rules/Policy; misquoting ETA section numbers (learn the CONCEPT, cite 'Section ~47 — verify'); treating IT Policy as binding law.")

# ---- S48 Part D: Project/lab presentation structure
add_activity("S48 · Part D — Project / lab presentation skeleton  ·  ~5 min",
    ["1. Problem / threat & objective — what you set out to do and why it matters.",
     "2. Tool / method used — ethically, in a lab/sandbox (scanning, sniffing, SQLi/XSS, phishing via SET, password cracking, firewall config, incident response).",
     "3. Findings / demo — what you discovered, shown clearly.",
     "4. Mitigation & relevant Nepal law/policy — the fix, tied to the ETA / infosec policy.",
     "5. Ethics & legal note — authorization, scope, responsible disclosure."],
    "EVERY offensive technique must be tied back to AUTHORIZATION and the ETA. 'Doing it in your own lab for a class' vs 'doing it to a real system' is the line between learning and a crime — make students state that line explicitly.",
    "PROJECT STRUCTURE [~5 min].")

add_quiz("S48 — Quick Check  ·  ~5 min",
    [("Q1.  The CIA triad stands for Confidentiality, Integrity, and:","q"),
     ("a) Authentication   b) Authorization   c) ✅ Availability   d) Auditing","a"),
     ("     Why: the three pillars of information security are Confidentiality, Integrity, and Availability.","o"),
     ("Q2.  A document stating how staff may use company systems is a(n):","q"),
     ("a) firewall   b) ✅ acceptable-use / information-security policy   c) digital signature   d) IT Policy of Nepal","a"),
     ("     Why: an AUP is an organizational security policy; the national IT Policy is a different, non-binding thing.","o"),
     ("Discussion: write one rule you'd put in your college's information-security policy — and say which threat it stops.","o")],
    "QUIZ [~5 min]. Keep it light — the main assessment is the course review and end-of-unit quiz. Draw out 'security = people + process, not just tech'.")
add_summary("S48 · Summary  ·  [~2 min]",
    ["Information-security policies operationalise protection: CIA triad → policy → standards → procedures.",
     "The 9 units form one arc — ethics (should) → security (protect) → forensics (investigate) → law (govern & punish).",
     "Exam = concepts + Nepal examples + applied cases; lab projects must always be framed within authorization and the ETA."],
    "This synthesis IS your professional posture: as a BIM graduate you will make ethical calls, secure systems, respond to incidents, and stay within Nepali law — all at once. The whole course was preparation for that single, integrated judgement.",
    "The End-of-Unit Quiz below, then final revision — and that completes IT 246.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 9 · Cheat Sheet","One-page revision reference",
    [("Cyber law & cybercrime (S45)","Cyber law fills the gap paper-law can't reach (identity/evidence/jurisdiction). Nepal's primary cyber law = ETA 2063 (NOT a stand-alone Cyber Crime Act). Cybercrime = computer as TARGET (hacking, data theft) or TOOL (fraud, defamation). Report to the Cyber Bureau (2018) — evidence first."),
     ("ETA 2063 (S46)","Two halves: ENABLE (e-records + digital-signature validity, e-commerce/e-gov) + PUNISH (offences chapter). Digital signature = private key signs / public key verifies → authentication + integrity + non-repudiation. Section ~47 (e-publication) = most-cited & debated. Figures ILLUSTRATIVE — verify."),
     ("ETR & Controller (S47)","ETR 2064 = procedures under the Act (CA licensing, certificates, fees). Controller (OCC, under MoCIT) licenses & supervises CAs → PKI chain: Controller → CAs → user certificates. Act = Parliament (binding); Rules = executive (binding); differ in kind."),
     ("IT Policy (S47)","National strategic framework — infrastructure, e-gov, IT industry/exports, digital literacy, security ('Digital Nepal'). NOT binding law. Policy directs; the Act + Rules bind. Classic exam trap: don't call it law."),
     ("Information security (S48)","CIA triad = Confidentiality + Integrity + Availability (lose one = insecure). Security policy hierarchy: policy → standards → procedures → guidelines. Components: AUP, access/password, data classification, incident response, BYOD, backup. Security = governance + people + process."),
     ("Law meets policy + arc (S48)","ETA criminalises (after), IT Policy directs, security policy operationalises (before). Course arc: ethics → security → forensics → law. Labs: every technique tied to AUTHORIZATION + the ETA.")])

add_glossary("Unit 9 · Glossary","Key terms — quick reference",
    [("Cyber law","the body of law governing computers, networks, the internet, and e-transactions."),
     ("ETA 2063","the Electronic Transaction Act (2008) — Nepal's primary cyber law."),
     ("ETR 2064","the Electronic Transaction Rules — procedures made under the ETA."),
     ("Cybercrime","an offence where a computer/network is the target or the tool."),
     ("Target vs tool crime","the computer is the victim (hacking) vs the weapon (fraud, defamation)."),
     ("Cyber Bureau","the Nepal Police cybercrime unit (est. 2018, Bhotahiti, Kathmandu)."),
     ("Electronic record","digital data given legal recognition equal to paper under the ETA."),
     ("Digital signature","a cryptographic signature: private key signs, public key verifies."),
     ("Asymmetric cryptography","a public/private key pair used to sign and verify."),
     ("Non-repudiation","the signer cannot later deny having signed."),
     ("Section ~47 (illustrative)","the most-applied & criticised e-publication offence — verify."),
     ("Controller (OCC)","the Office of the Controller of Certification — licenses & supervises CAs."),
     ("Certifying Authority (CA)","a licensed body that issues digital-signature certificates."),
     ("PKI","public-key infrastructure — the Controller → CA → user trust chain."),
     ("IT Tribunal","the ETA body for adjudicating certain electronic-transaction disputes."),
     ("IT Policy of Nepal","a non-binding national strategic framework for ICT development."),
     ("Act vs Rules vs Policy","Act (Parliament, binding) · Rules (executive, binding) · Policy (direction, non-binding)."),
     ("Privacy Act 2075","Nepal's data-privacy law, complementing the ETA (verify current status)."),
     ("CIA triad","Confidentiality, Integrity, Availability — the pillars of information security."),
     ("Information security policy","documented rules for protecting an organization's information assets."),
     ("Policy→standard→procedure","policy (what/why) → standard (measurable) → procedure (how-to)."),
     ("Acceptable-use policy (AUP)","rules on how staff may use company systems."),
     ("Incident response","the defined steps taken when a security breach occurs.")])

# ============= CONSOLIDATED END-OF-UNIT QUIZ =============
add_divider("Unit 9 · Revision","Consolidated end-of-unit quiz",
    "Ten MCQs across the whole unit (answers shown), then short-answer, applied-case, and discussion questions to work from the concept slides and Unit9_material.md.",
    "Use as a 15–20 min in-class quiz or take-home review. ⚠️ Mark all ETA/ETR section numbers & penalty figures as 'verify against official text' in the answer key.")
add_quiz("Section A — Multiple choice (answers shown)",
    [("1.  Nepal's primary cyber law is   →  ✅ the Electronic Transaction Act (ETA) 2063","a"),
     ("2.  A cybercrime where the computer is the TOOL is   →  ✅ online fraud / cyber-defamation","a"),
     ("3.  The Nepali body that investigates cybercrime is   →  ✅ the Nepal Police Cyber Bureau","a"),
     ("4.  What gives an electronic record legal validity in Nepal   →  ✅ the ETA 2063","a"),
     ("5.  A digital signature primarily provides   →  ✅ authentication, integrity, and non-repudiation","a"),
     ("6.  The most-applied & criticised ETA provision is   →  ✅ the e-publication offence ('Section ~47' — verify)","a"),
     ("7.  Act vs Rules vs Policy: the non-binding one is   →  ✅ the IT Policy of Nepal","a"),
     ("8.  The body that licenses & supervises CAs is   →  ✅ the Office of the Controller of Certification","a"),
     ("9.  The CIA triad stands for   →  ✅ Confidentiality, Integrity, Availability","a"),
     ("10.  'The IT Policy is binding law like the ETA' is   →  ✅ FALSE (policy directs; the Act + Rules bind)","a")],
    "Consolidated quiz Section A. ⚠️ Section numbers/penalties are illustrative — verify current law.",compact=True)
add_quiz("Sections B–D — short answer, applied case & discussion",
    [("Section B — Short answer","q"),
     ("11. Define cyber law and give one reason Nepal needs it.   12. List 4 cybercrimes recognised under Nepali law.   13. State the two main purposes of the ETA 2063.","o"),
     ("14. Explain the role of the Controller and Certifying Authorities.   15. List 4 components of an information-security policy.","o"),
     ("Section C — Applied case","q"),
     ("16. A person is impersonated on social media in Nepal and defamed — outline which body investigates, which provision applies (cite as 'verify'), and the steps.","o"),
     ("17. Classify four given scenarios as target/tool cybercrime and name the likely ETA-related response.","o"),
     ("Section D — Discussion","q"),
     ("18. 'Section 47 of the ETA: necessary protection against online harm, or a threat to free speech?' Argue BOTH sides with Nepal examples.","o")],
    "Consolidated quiz Sections B–D. Model answers on the concept slides and in Unit9_material.md. ⚠️ Verify all legal figures against the official text before finalising the answer key.",compact=True)

# ---- warm closing (final unit of the course) ----
add_title("End of Unit 9 — and the End of IT 246  🎓",
          "S45–S48 complete: cyber law & the Cyber Bureau · the ETA 2063 · the ETR, Controller & CAs · the IT Policy · information security & policies — and a full course synthesis.",
          "Congratulations — you have completed IT 246: IT Ethics & Cybersecurity. Across nine units you learned to reason ethically, protect systems, "
          "investigate incidents, and stay within Nepali law — one integrated professional judgement. Carry it well. (Legal specifics herein are illustrative — always verify current law.)")

_add_page_numbers()
save("IT246_Unit9.pptx")
