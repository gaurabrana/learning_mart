#!/usr/bin/env python3
"""IT246 (sixth) Unit 2 deck — Ethics for IT Workers & Users (S6–S10), built to
COURSE_MATERIAL_STANDARD.md INCLUDING the §7A depth rule: every confusable set is a comparison
table, every 'X vs not-X' concept a concrete-example table, claims get scaffolding tables, plus
payoff/example tables — each table on its OWN slide, paginated, never squeezed. Generous slide
count by design. Self-contained & PDF-safe. Imports the shared toolkit deckkit.py.
Diagrams in images/. Run: python3 build_unit2_pptx.py -> IT246_Unit2.pptx
"""
from deckkit import *

# ============================================================
#                        BUILD
# ============================================================
add_title("Unit 2 — Ethics for IT Workers & IT Users",
          "IT 246: IT Ethics & Cybersecurity  ·  BIM 6th Semester  ·  Sessions S6–S10",
          "Self-contained slides with depth: every concept grounded in comparison & concrete-example TABLES "
          "(Nepal / IT localised) — no abstraction without instances. Exports to PDF with no information lost.")

add_outcomes("Unit 2 — Learning Outcomes","workers & users  ·  s6–s10",
    "By the end of this unit, you will be able to:",
    ["Identify the six relationships an IT worker manages and the ethical duty in each (S6)",
     "Explain how codes, certification, licensing & professional bodies encourage professionalism (S7)",
     "Describe acceptable use policies and the main IT-use issues — piracy, inappropriate use (S8)",
     "Explain key privacy, surveillance, and anonymity/identity issues in IT (S9)",
     "Recognise and reason about social-networking harms — cyberbullying, fake news, defamation (S10)"],
    "This is Unit 2 of IT 246. It applies Unit 1's reasoning (legal≠ethical, can-vs-should, decision traps) to the working IT professional and the everyday IT user.")

add_roadmap("Unit 2 — Roadmap","Where each session fits (S6–S10)",
    ["S6   The IT-worker relationship web (6 duties)",
     "S7   Professionalism: codes · certs · licensing · bodies",
     "S8   Ethical IT use: AUP · piracy · inappropriate use",
     "S9   Privacy · surveillance · anonymity · identity",
     "S10  Social-networking harms (closes Unit 2)"],
    ["Unit 3   Intellectual property (copyright, patents…)",
     "Unit 4   Whistle-blowing & professional dilemmas",
     "Units 5–8   Cybersecurity & digital forensics",
     "Unit 9   Cyber law in Nepal (ETA, Privacy Act)"])

# ============================================================ S6
add_divider("Session 6 · Lecture hour 1 (of 5)","Managing the IT Worker Relationship",
    "A vendor offers the bank's IT manager a 'free' iPhone the week before a Rs 2-crore tender. A developer quietly moonlights for a client's competitor on weekends. Nobody broke a law yet — so why does it already feel wrong? Because an IT worker doesn't serve one boss; they juggle many relationships that pull on their loyalty at once.",
    "OPENING HOOK [~5 min]. Run the two votes ('broken a law?' vs 'feels wrong?'); DON'T resolve the iPhone — hold it until Concept 4. Agenda: why IT workers face special pressure → employer → client → suppliers/peers/users/society.")

concept_understand("S6 · Concept 1 · [THEORY]","Why IT Workers Face Special Pressure — access = power = responsibility",
    "An IT worker designs, builds, maintains, or manages IT systems and the data inside them. What makes them ethically different is privileged access: a clerk sees their own desk; a database admin can see everyone's records. Access is power, and power is responsibility.",
    ["A developer holds the source code; a sysadmin holds root/admin rights; support can read your files 'to fix it'.",
     "Being technically able to read a balance or reset a password does NOT make it right to do so.",
     "Every relationship therefore comes with a built-in duty of care — a duty not to abuse the trust access represents.",
     "This is Unit 1's 'can vs should', now with real power behind the 'can'."],
    "s6_web.png","Access is power; power is responsibility — 'can' is not 'should'.",
    "~8 min. Keep the six-arrow web on screen all session. The gap between 'can' and 'should' is exactly where IT-worker ethics lives.")
add_table_slide("S6 · Concept 1 · scaffolding","Privileged access — what each role CAN do, and the duty it creates",
    ["IT role","What they can technically do","The duty their access creates"],
    [["Database administrator","Read/edit any record — every customer's balance, any citizen's KYC","View only what the job needs; never browse out of curiosity"],
     ["Developer","Hold the full source code and business logic","Not leak, sell, or reuse the employer's/client's code"],
     ["System administrator","Root rights — read anyone's email, reset any password","Not snoop on colleagues or executives; act only on authorised tasks"],
     ["Support technician","Open your files, install software, take remote control","Touch only what fixes the stated problem; keep what they see private"],
     ["Network administrator","See all traffic, block or log any user","Monitor per policy, not to spy on individuals"],
     ["Bank IT staffer (Nepal)","Look up any account — a neighbour's, a celebrity's, an ex's","Look only for a work reason; the system permits it, ethics forbids it"]],
    per_page=6,widths=[1.8,2.9,3.0],fs=11,
    note="Nothing on the right column is enforced by the system — the system GRANTS the access. Only trust and ethics stop the abuse.")
concept_apply("S6 · Concept 1 · [THEORY]","Why IT Workers Face Special Pressure",
    "A bank IT staffer with database access could view any customer's balance — your neighbour's, a celebrity's, an ex's. What stops them is not lack of permission (the system grants it); it is trust and ethics. Globally: a sysadmin abusing root to read executives' private emails — nothing technical stopped them, only ethics should have.",
    "\"IT is just a back-office technical job — ethics is for managers.\" Access IS power: the more you can technically do, the more responsibility you carry, whether or not you hold a manager's title. A junior with admin rights holds more trust than a senior manager without them.",
    "IT workers are ethically distinct because of privileged access to systems and data. Since access is power and power is responsibility, technical ability ('can') never settles what is right ('should'). Every relationship an IT worker has therefore carries a duty of care — a duty not to abuse the trust that access represents.",
    "IT worker · privileged access · duty of care · can vs should · access = power = responsibility")

concept_understand("S6 · Concept 2 · [THEORY] [EXAMPLE]","Relationship 1 — the Employer: loyalty & honesty",
    "The first arrow points to your employer. Two core duties: LOYALTY — protect the employer's assets and IP (source code, client lists, internal data); and HONESTY — be truthful about your work and your qualifications (this is where resume fraud lives).",
    ["Loyalty means not leaking, selling, or carrying the employer's IP out the door to your next job.",
     "Honesty starts before day one: claiming a certification you don't hold is a breach against your employer.",
     "Four pressure points strain this bond: conflicts of interest, resume fraud, software-license compliance (S8), whistle-blowing.",
     "Loyalty has a LIMIT — it does not extend to covering up harm (whistle-blowing is treated fully in Unit 4)."],
    None,"Loyalty protects the employer's assets; honesty protects the truth — but neither obliges you to hide harm.",
    "~9 min. If a student says 'the boss told me to', connect to Unit 1's blind-obedience trap — obedience does not erase personal accountability.")
add_table_slide("S6 · Concept 2 · scaffolding","Four pressure points on the employer relationship",
    ["Pressure point","What it looks like","Why it's an ethical problem"],
    [["Conflict of interest","A side interest that competes with the employer (moonlighting for a rival)","Your judgment now serves two masters; the employer can't trust your loyalty"],
     ["Resume fraud","Claiming a certification or skill you don't have","A breach of honesty before you even start — the employer relied on a lie"],
     ["Software-license compliance","Using unlicensed/pirated software on the job (see S8)","Legal liability for the firm AND you; 'orders' don't transfer the blame"],
     ["Whistle-blowing tension","The employer itself is doing wrong; do you stay loyal?","Loyalty has a limit — it never requires covering up harm (Unit 4)"]],
    per_page=4,widths=[1.9,3.0,2.9],fs=11.5,
    note="Loyalty and honesty are the duties; these four are where they get tested in a real job.")
concept_apply("S6 · Concept 2 · [THEORY] [EXAMPLE]","Relationship 1 — the Employer",
    "A Kathmandu IT-firm staffer copies client source code to reuse at a weekend side gig. The code isn't theirs — it belongs to the employer (and often contractually to the client). Reusing it is theft of IP, betraying TWO relationships at once, even though 'no one will notice' and 'I wrote it anyway'.",
    "\"If the boss orders it, it's on them.\" Your employer asks you to install pirated Office/AutoCAD on all machines to cut costs. Liability can fall on the company AND the individual who installed it — 'I was just following orders' is the blind-obedience trap and does not transfer responsibility off you.",
    "The IT worker owes the employer loyalty (protect assets and IP) and honesty (truthful work and qualifications). This is strained by conflicts of interest, resume fraud, license non-compliance, and the whistle-blowing tension. Loyalty is real but limited: it never extends to concealing harm, and obeying an order does not erase personal accountability.",
    "loyalty · honesty · IP protection · conflict of interest · resume fraud · loyalty has a limit")

concept_understand("S6 · Concept 3 · [THEORY]","Relationship 2 — the Client: duty beyond the contract",
    "The client is who you build for. Three professional duties: give HONEST technical advice, DELIVER what was promised, and DISCLOSE risks (don't hide that a system might fail, leak, or not scale). What makes this relationship ethically loaded is information asymmetry.",
    ["The client usually cannot judge technical quality — they can't read your code or spot a shortcut.",
     "They are forced to rely on your honesty, the way a patient must trust a doctor.",
     "When one party can't verify and the other can exploit that, ethics is the weaker party's only protection.",
     "So the duty is professional, not just contractual — the contract is a floor, not the ceiling (Unit 1)."],
    None,"When the client can't check your work, your ethics is the only thing protecting them.",
    "~8 min. Land 'information asymmetry' slowly — it's why a professional duty exists at all.")
add_table_slide("S6 · Concept 3 · scaffolding","Three duties to the client — and the failure when each is broken",
    ["Duty to the client","What it means","Failure example (Nepal / IT)"],
    [["Honest technical advice","Recommend what the client needs, not what pays you most","Selling an over-sized system a small NGO doesn't need"],
     ["Deliver what was promised","Build the agreed scope to the agreed quality","Marking a half-built e-gov module 'done' to trigger payment"],
     ["Disclose risks","Tell them what might fail, leak, or not scale","Hiding that the system can't handle election-day load"]],
    per_page=3,widths=[1.9,2.9,3.0],fs=12,
    note="All three exploit information asymmetry — the client literally cannot catch the breach until it's too late. That's what makes it a PROFESSIONAL duty.")
concept_apply("S6 · Concept 3 · [THEORY]","Relationship 2 — the Client",
    "A software vendor over-promises an e-governance module to a municipality, then quietly under-delivers. The municipality lacks the technical expertise to catch it until the system fails in production — months later, after payment. The asymmetry let the vendor sell air; good ethics here protects a party that literally cannot protect itself.",
    "\"If the contract doesn't ban it, it's fine.\" Professional duty goes beyond the contract's letter. The contract is a floor, not the limit of your responsibility (the Unit 1 'floor, not ceiling' idea). A loophole in the contract is not an ethical permission slip.",
    "The IT worker owes the client honest technical advice, delivery of what was promised, and disclosure of risks. Because of information asymmetry — the client usually cannot verify technical quality — the worker holds a professional duty like a doctor's, extending beyond the contract's letter. Ethics is the only protection the weaker party has.",
    "honest advice · deliver as promised · disclose risk · information asymmetry · contract is a floor")

concept_understand("S6 · Concept 4 · [THEORY] [EXAMPLE]","Relationships 3–6 — Suppliers, Peers, Users & Society",
    "The remaining four arrows share a theme: fairness to people who aren't your boss or your client. Suppliers — deal fairly, no bribery/kickbacks. Peers — mutual respect, no resume inflation or poaching trade secrets. Users — support and train them, don't exploit their lack of skill. Society — build safe systems, don't enable harm.",
    ["Resolve the hook: the 'free iPhone' is a bribe disguised as a gift — timed around a tender, meant to influence.",
     "The profession's reputation is shared: one fraud damages every IT worker's credibility.",
     "Don't bury a non-technical user in jargon to overcharge or scare them into an unneeded purchase.",
     "A system that leaks citizen data or powers a scam harms people who never agreed to anything."],
    None,"Gift or bribe? Public? Timed? Influences you? Fail any → it's a bribe.",
    "~5 min. Resolve the iPhone here. Deliver the pharmacist analogy: trusted with powerful 'medicine' that heals or harms depending on whose hand holds it.")
add_table_slide("S6 · Concept 4 · comparison","Gift vs Bribe — the three-question test",
    ["Test question","A genuine gift","A bribe"],
    [["Would it survive being made PUBLIC?","Yes — a logo pen at a conference is fine to disclose","No — you'd hide the 'free iPhone' from your boss"],
     ["Is it TIMED around a decision?","No — unrelated to any pending choice","Yes — arrives the week before the tender"],
     ["Could it INFLUENCE your judgment?","No — token value, no leverage","Yes — that's the entire point of giving it"]],
    per_page=3,widths=[2.3,2.6,2.6],fs=12,
    note="The iPhone fails all three → bribe. The logo pen passes all three → gift. In Nepal, festival ('Dashain') gifting is cultural — the test is what keeps a normal gift from becoming a bribe.")
add_table_slide("S6 · Concept 4 · scaffolding","The six relationships on one page — duty & a concrete Nepal risk",
    ["Relationship","Core duty","A concrete ethical risk (Nepal / IT)"],
    [["Employer","Loyalty + honesty; protect assets/IP","Copying source code to a personal side project"],
     ["Client","Honest advice; deliver; disclose risk","Hiding a security flaw to hit a deadline"],
     ["Suppliers","Deal fairly; no bribes/kickbacks","Accepting a vendor's pre-tender 'gift'"],
     ["Peers","Mutual respect; no poaching/inflation","Blaming a teammate to look better; stealing a rival's trade secrets"],
     ["Users","Support & train; don't exploit skill gaps","Burying a customer in jargon to overcharge"],
     ["Society","Build safe systems; don't enable harm","Shipping a system that leaks citizen data"]],
    per_page=6,widths=[1.4,2.4,3.4],fs=11,
    note="None of these risks required hacking — every one came from ordinary access plus a pull on your loyalty.")
concept_apply("S6 · Concept 4 · [THEORY] [EXAMPLE]","Relationships 3–6 — Suppliers, Peers, Users & Society",
    "Resolving the hook: the vendor's 'free iPhone' is a bribe, not a gift — it fails the three-question test (you'd hide it, it's timed around the tender, and it's meant to influence the Rs 2-crore decision). A logo pen at a conference passes all three and is a genuine gift.",
    "\"A gift is just good manners — accepting it is polite.\" A gift timed around a decision you control, that you'd hide, and that could sway you, is a bribe regardless of how it's wrapped. Cultural festival-gifting blurs the line, which is exactly why you apply the public/timed/influence test.",
    "Beyond employer and client, the IT worker owes suppliers fair dealing (no bribes), peers respect (no poaching or inflation), users honest support (no exploiting skill gaps), and society safe systems (no enabling harm). A gift becomes a bribe when it fails the public-timed-influence test. Like a pharmacist, the worker's ethics — not their skill — is the safeguard.",
    "fair dealing · bribery vs gift · trade secrets · don't exploit users · safe systems · pharmacist analogy")

add_activity("S6 — 'Map your own six arrows'  ·  ~5 min",
    ["In pairs (2 min): imagine you've just joined a Nepali bank's or fintech's IT team.",
     "For ANY THREE of the six relationships, write one concrete ethical risk you'd face in that role.",
     "Take 3–4 answers aloud (3 min) and place each on the relationship web on screen.",
     "Close: notice none required hacking — every risk came from ordinary access plus a pull on your loyalty."],
    "Seeds if a pair stalls: employer (copying code to a side project), client (hiding a security flaw to hit a deadline), peers (inflating a teammate's mistake to look better), supplier (a vendor's Dashain gift).",
    "ACTIVITY [~5 min].")
add_quiz("S6 — Quick Check  ·  ~5 min",
    [("Q1.  A supplier gifting an IT manager a phone right before a tender decision is best described as:","q"),
     ("a) good manners   b) ✅ a conflict of interest / bribery   c) a loyalty bonus   d) fair dealing","a"),
     ("     Why: it's timed around a decision, you'd hide it, and it's meant to influence — it fails the gift test.","o"),
     ("Q2.  The duty to give honest technical advice applies most directly to the:","q"),
     ("a) supplier   b) competitor   c) ✅ the client   d) regulator","a"),
     ("     Why: the client can't verify technical quality (information asymmetry), so they depend on your honesty.","o"),
     ("Discussion: which relationship is hardest for a junior IT worker in Nepal to manage honestly — and why?","o")],
    "QUIZ [~5 min]. Expect 'employer vs society' (pressure to install pirated software) and 'supplier' (festival gifts blur the bribe line).")
add_summary("S6 · Summary  ·  [~2 min]",
    ["IT workers manage six key relationships: employer, client, supplier, peers, users, society.",
     "Privileged access creates duties — it's about power, not just permission; 'can' ≠ 'should'.",
     "Loyalty, honesty, and no conflicts of interest run through all six; the contract is a floor, not the ceiling."],
    "Your first IT job hands you access and vendor contacts on day one — before anyone has tested your character. How you handle gifts, access, and honesty in those first weeks quietly sets your reputation for years, and in Nepal's small IT market, reputation travels fast between firms.",
    "S7 — how the profession itself encourages good behaviour: codes, certification, and licensing.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S7
add_divider("Session 7 · Lecture hour 2 (of 5)","Encouraging Professionalism of IT Workers",
    "A doctor swears an oath and can be struck off the NMC register. An engineer signs off on a bridge and answers to the NEC. But anyone can call themselves an 'IT professional' tomorrow — and an IT worker who ships dangerous, negligent software usually faces… nothing formal. There's often no licence to lose.",
    "OPENING HOOK [~5 min]. Take a show of hands on the two driving questions: is IT really a profession? Should it be regulated like medicine? Keep 'should IT be licensed?' alive as a thread to the CFU debate. Agenda: is IT a profession? → codes → certification → licensing → bodies.")

concept_understand("S7 · Concept 1 · [THEORY]","Is IT a 'Profession'? — the four-part test",
    "'Profession' doesn't just mean 'a serious job'. There's a four-part test: (1) specialized education, (2) a recognized body of knowledge, (3) a code of ethics, (4) self-regulation — the field can license and discipline its own members.",
    ["IT clearly has (1) degrees like this one, (2) documented shared expertise, and (3) codes (ACM, IEEE-CS).",
     "IT LACKS (4) universal licensing — you can build banking software tomorrow with no government permission.",
     "Verdict: IT partly qualifies — knowledge and codes, but not the self-regulation medicine and law have.",
     "That single gap is why IT's status as a 'profession' is genuinely debated, not just an exam phrase."],
    None,"Education ✓ knowledge ✓ code ✓ self-regulation ✗ — IT is a partial profession.",
    "~7 min. Professionalism is about standards and accountability, not just skill. A brilliant coder who hides bugs is skilled, not professional.")
add_table_slide("S7 · Concept 1 · comparison","The four-part profession test — IT vs medicine/engineering",
    ["Criterion","Medicine / Engineering","Information Technology"],
    [["Specialized education","Medical / engineering degree required","✅ Yes — IT degrees (like this BIM)"],
     ["Recognized body of knowledge","Established, documented, examined","✅ Yes — shared, documented expertise"],
     ["Code of ethics","Yes — enforced by the council","✅ Yes — ACM, IEEE-CS (voluntary)"],
     ["Self-regulation (licensing + discipline)","Yes — NMC / NEC can strike you off","❌ No universal licensing to lose"]],
    per_page=4,widths=[2.3,2.6,2.6],fs=11.5,
    note="IT scores 3 of 4. The missing self-regulation — no licence, no strike-off — is the whole reason 'is IT a profession?' is a live debate.")
concept_apply("S7 · Concept 1 · [THEORY]","Is IT a 'Profession'?",
    "In Nepal, doctors are licensed by the NMC and engineers by the NEC — you legally cannot practise without it. IT workers generally are NOT licensed: you can build banking software tomorrow with no government permission. That single fact is the heart of the 'is IT a profession?' debate.",
    "\"Anyone who fixes computers is an IT professional.\" Professionalism is about standards and accountability, not just technical skill. A brilliant coder who hides bugs and pads invoices is skilled, not professional — the title is earned by how you're held to account, not by what you can build.",
    "A profession has four marks: specialized education, a recognized body of knowledge, a code of ethics, and self-regulation (licensing + discipline). IT has the first three but lacks universal licensing, so it is a partial profession — which is precisely why its status is debated. Professionalism is defined by standards and accountability, not skill alone.",
    "four-part test · self-regulation · licensing · partial profession · standards over skill")

concept_understand("S7 · Concept 2 · [THEORY] [EXAMPLE]","Professional Codes of Ethics",
    "A code of ethics is a published set of principles members commit to upholding. The big two in IT are the ACM Code of Ethics and IEEE-CS. A code does four jobs: sets expectations, builds public trust, guides decisions, and provides a basis for discipline.",
    ["Sets expectations — turns 'be good' into specifics: 'avoid harm', 'respect privacy', 'be honest about limitations'.",
     "Builds public trust — outsiders can see what the field holds itself to.",
     "Guides decisions — when stuck, the code is a reference, not just your gut.",
     "Basis for discipline — membership/employment can be tied to it, giving it teeth even without a government licence."],
    None,"A code turns 'be good' into commitments you can be held to.",
    "~8 min. Connect to S6: this is the employer-vs-society tension again, now with a code to lean on — 'the code gives you language to say no professionally.'")
add_table_slide("S7 · Concept 2 · scaffolding","The four jobs a code of ethics does",
    ["Job of the code","What it achieves","Concrete example"],
    [["Sets expectations","Turns vague 'be good' into specific commitments","ACM: 'avoid harm', 'respect privacy', 'be honest about limitations'"],
     ["Builds public trust","Outsiders can see the standard the field holds itself to","Clients/outsourcing partners trust a firm that follows ACM norms"],
     ["Guides decisions","A reference when you're unsure, not just your gut","Asked to build hidden tracking → the code says object/disclose/refuse"],
     ["Basis for discipline","Membership or employment can be tied to it","Breach → lose membership or your job, even with no state licence"]],
    per_page=4,widths=[1.8,2.8,3.0],fs=11,
    note="A code has 'some teeth' without a government licence — the last row is how the field disciplines its own even though IT lacks NMC/NEC-style regulation.")
concept_apply("S7 · Concept 2 · [THEORY] [EXAMPLE]","Professional Codes of Ethics",
    "A developer is asked to build a hidden tracking feature users don't know about. The ACM principle 'avoid harm' applies: undisclosed tracking harms users' privacy and autonomy without consent → the code says object, disclose, or refuse. In Nepal, firms adopt internal codes modeled on ACM and rally around CAN (Computer Association of Nepal) because clients expect professional standards.",
    "\"A code of ethics is just words on a website.\" A code is only useful if you can APPLY it to a concrete ask — and it gives you professional language to refuse. Voluntary firms import ACM standards precisely because clients and outsourcing partners demand them; the code has real market teeth.",
    "A code of ethics is a published set of principles members commit to (ACM, IEEE-CS). It sets expectations, builds public trust, guides decisions, and provides a basis for discipline — giving the field some accountability even without government licensing. Its value shows when applied to a concrete ask, such as refusing to build undisclosed user tracking.",
    "code of ethics · ACM · IEEE-CS · avoid harm · CAN-Nepal · apply the code")

concept_understand("S7 · Concept 3 · [THEORY]","Certification — proof of a specific skill",
    "A certification is a vendor or industry credential proving a specific skill — CCNA, CISSP, CompTIA, AWS, PMP. Four defining traits, because students routinely over-trust certs: it signals competence, it is voluntary, it can become outdated, and it is NOT a licence.",
    ["Signals competence — a fast, trusted filter for employers scanning a CV.",
     "Voluntary — no law requires it; you choose to pursue it.",
     "Can become outdated — a 2015 cloud cert may be stale today; certs expire and renew.",
     "Not a licence — passing an exam grants no legal right to practise anything."],
    None,"A cert proves you CAN do the skill — not that you WILL do it ethically.",
    "~6 min. Nepali IT grads pursue CCNA/CEH to get a CV past a foreign client's first filter. Certification proves skill, not integrity.")
add_table_slide("S7 · Concept 3 · examples","Common IT certifications — what each proves & who issues it",
    ["Certification","What it proves","Issued by"],
    [["CCNA","Cisco networking fundamentals","Cisco (vendor)"],
     ["CISSP","Information-security management expertise","(ISC)² (industry body)"],
     ["CEH","Skill in ethical hacking / penetration testing","EC-Council (industry body)"],
     ["CompTIA A+","Core IT support / hardware & OS troubleshooting","CompTIA (industry body)"],
     ["AWS Certified","Building/operating on Amazon Web Services","Amazon (vendor)"],
     ["CISA / CISM","IT audit / security governance","ISACA (professional body)"]],
    per_page=6,widths=[1.5,3.2,2.3],fs=11.5,
    note="All are voluntary, expire over time, and prove SKILL — none grants a legal right to practise. CEH proves the skill to break into systems; whether it's used ethically is a separate question.")
concept_apply("S7 · Concept 3 · [THEORY]","Certification",
    "Nepali IT graduates pursue CCNA / CEH to compete for jobs and remote/outsourcing work — a cert is often what gets a Kathmandu graduate's CV past a foreign client's first filter. It signals a specific, verified skill to someone who has never met them.",
    "\"Certification = guaranteed ethical behaviour.\" Certification proves skill, not integrity. A Certified Ethical Hacker (CEH) has the skill to break into systems — whether they use it ethically is a separate question the certificate can't answer. A cert filters competence, never character.",
    "A certification is a voluntary vendor/industry credential proving a specific skill (CCNA, CISSP, CEH, AWS, PMP). It signals competence to employers, can expire and become outdated, and — crucially — is not a licence: it grants no legal right to practise and says nothing about integrity.",
    "certification · signals skill · voluntary · expires · not a licence · skill ≠ integrity")

concept_understand("S7 · Concept 4 · [THEORY]","Licensing & Professional Organizations",
    "A licence is government-granted permission to practise, legally enforced — its point is to protect the public in high-stakes fields where mistakes kill people. Professional organizations are the bodies that set standards, run certifications, publish codes, and represent members.",
    ["Licensing protects the public (medicine, structural engineering) but adds gatekeeping, fees, and slower entry.",
     "Live debate: should safety-critical software (medical devices, aviation, banking cores) need a licensed engineer?",
     "The bodies: ACM & IEEE-CS (global standards/codes), ISACA (audit/security), CAN-Nepal (advocacy/events/training).",
     "The map: organizations publish CODES and run CERTS; only GOVERNMENT runs LICENSING."],
    "s7_map.png","Bodies write codes & run certs; only government grants a licence.",
    "~9 min. Note the US 'Professional Engineer — Software' licence was created, then largely discontinued for lack of demand — shows how unsettled this is even in mature markets.")
add_table_slide("S7 · Concept 4 · comparison","Certification vs Licence vs Code vs Professional body — the confusable four",
    ["Mechanism","Who grants it","Legal force?","What it proves / does","Example"],
    [["Certification","A vendor or industry body","No — voluntary","You have a specific skill","CCNA, CISSP, AWS"],
     ["Licence","Government","Yes — legally enforced","Legal right to practise","NMC doctor reg., driving licence"],
     ["Code of ethics","A professional body","No — but can discipline members","Shared ethical commitments","ACM 'avoid harm'"],
     ["Professional body","(is itself the organization)","No — sets standards","Publishes codes, runs certs, advocates","ACM, IEEE-CS, ISACA, CAN-Nepal"]],
    per_page=4,widths=[1.5,1.9,1.7,2.5,2.0],fs=10.5,
    note="The test that separates them: WHO grants it, and does it have LEGAL FORCE? A driving licence is a licence (government, legal). CAN is a body (may run certs, isn't itself a cert).")
add_table_slide("S7 · Concept 4 · scaffolding","The professional bodies that keep IT professional",
    ["Body","Focus","What it runs / offers"],
    [["ACM","Global computing standards & ethics","The ACM Code of Ethics; conferences, digital library"],
     ["IEEE-CS","Computing/engineering standards","Standards, the software-engineering code (with ACM)"],
     ["ISACA","Governance, audit & security","The CISA and CISM certifications"],
     ["CAN (Computer Association of Nepal)","Nepal's IT community","Advocacy, events, training for local professionals"]],
    per_page=4,widths=[2.0,2.6,3.0],fs=11.5,
    note="Organizations publish the codes and run the certifications; government runs the licensing. That's the whole map of 'who keeps IT professional'.")
concept_apply("S7 · Concept 4 · [THEORY]","Licensing & Professional Organizations",
    "The US 'Professional Engineer (PE) — Software' licence was created and then largely discontinued for lack of demand — telling you how unsettled software licensing is even in mature markets. Meanwhile ACM/IEEE-CS write the codes, ISACA runs CISA/CISM, and CAN-Nepal advocates for the local community.",
    "\"Certification and licence are basically the same thing.\" They're not: a certification is voluntary and issued by a vendor/body to prove a skill; a licence is government-granted, legally enforced, and confers the right to practise. Ask 'who grants it, and does it have legal force?' to tell them apart every time.",
    "A licence is government-granted, legally enforced permission to practise, used to protect the public in high-stakes fields — but it adds gatekeeping and cost, which is why IT has resisted it. Professional organizations (ACM, IEEE-CS, ISACA, CAN-Nepal) set standards, publish codes, and run certifications. The map: bodies write codes and run certs; only government licenses.",
    "licence · legal force · protect the public · ACM/IEEE-CS/ISACA/CAN · bodies vs government")

add_activity("S7 — 'Cert, licence, or code?'  ·  ~5 min",
    ["In pairs (2 min): label each of six items as Certification / Licence / Code of Ethics / Professional Body.",
     "The six: (1) CCNA, (2) NMC doctor registration, (3) the ACM 'avoid harm' rule, (4) ISACA, (5) a driving licence, (6) CAN-Nepal.",
     "Take answers aloud (3 min) and resolve the two that trip people up.",
     "A driving licence is a LICENCE (government, legal force); CAN is a BODY (may run certs, isn't itself a cert)."],
    "The deliberate confusable is cert-vs-licence — keep returning to 'who grants it, and does it have legal force?' as the test. Answers: 1=cert, 2=licence, 3=code, 4=body, 5=licence, 6=body.",
    "ACTIVITY [~5 min].")
add_quiz("S7 — Quick Check  ·  ~5 min",
    [("Q1.  A government-granted, legally enforced permission to practise is:","q"),
     ("a) a certificate   b) ✅ a licence   c) a code of ethics   d) a degree","a"),
     ("     Why: only a licence is granted by government and carries legal force; the rest are voluntary.","o"),
     ("Q2.  ACM and IEEE-CS are examples of:","q"),
     ("a) certifications   b) laws   c) ✅ professional organizations (with codes of ethics)   d) employers","a"),
     ("     Why: they are bodies that publish codes and set standards — not certs, laws, or employers.","o"),
     ("Discussion: should IT workers in Nepal be licensed like engineers and doctors? Pick a side and argue it.","o")],
    "QUIZ [~5 min]. Reward the TRADE-OFF: for = safety-critical accountability; against = slows a fast field, raises barriers, hard to enforce across borders.")
add_summary("S7 · Summary  ·  [~2 min]",
    ["IT is a partial profession — it has knowledge and codes, but no universal licensing.",
     "Codes guide behaviour; certification proves a skill (not integrity); licensing has legal force.",
     "Professional bodies (ACM, IEEE-CS, ISACA, CAN-Nepal) set the standards and run the certs."],
    "Employers and outsourcing clients increasingly require certifications plus adherence to a code of conduct, which directly shape your hireability and pay. Knowing the difference between a cert (skill), a licence (legal force), and a code (commitment) lets you build a credential strategy on purpose instead of collecting random badges.",
    "S8 — turning from workers to users: keeping everyday IT use ethical.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S8
add_divider("Session 8 · Lecture hour 3 (of 5)","Encouraging Ethical Use of IT Resources among Users",
    "One shared office Wi-Fi password, three problems: someone torrents movies, another installs cracked Photoshop, a third runs a crypto miner on the server overnight. No outsider hacked anything — so whose problem is it? The threat came from inside, from ordinary users. The lesson in one line: users need rules, not just tools.",
    "OPENING HOOK [~5 min]. Frame it as an ethics + responsibility problem FIRST (security units 5–8 come later). Agenda: who is a 'user' → Acceptable Use Policy → software piracy → inappropriate use.")

concept_understand("S8 · Concept 1 · [THEORY]","Who Is an 'IT User' — and Why Their Behaviour Matters",
    "An IT user is anyone who uses an organization's IT resources — staff, students, customers, contractors, not just 'the IT department'. The key idea: most security and ethics incidents start with ordinary users, not hackers. This is the insider risk — usually not malicious, just careless.",
    ["Careless, everyday acts: a clicked phishing link, a reused password, a home USB, a cracked app 'to get work done'.",
     "If most harm starts inside, buying more security tools won't fix it — you must change user behaviour.",
     "That's what the rest of the session (AUP, anti-piracy, use norms) is actually for.",
     "Security is a shared duty, not a department."],
    "s8_insider.png","The danger isn't the hacker at the door — it's the user who props it open.",
    "~8 min. Resist calling it 'a security problem' — it's an ethics/responsibility problem first. The lab example: 100% insider damage, every student who installed something contributed.")
add_table_slide("S8 · Concept 1 · examples","The insider risk — careless (not malicious) acts that cause real harm",
    ["Everyday user action","The harm it causes","Who is affected"],
    [["Clicking a phishing link","Credentials stolen, malware installed","The whole organization's network"],
     ["Reusing one password everywhere","One leak unlocks every account","The user and everyone in shared systems"],
     ["Plugging in a personal USB","Malware jumps onto work machines","Colleagues, shared servers"],
     ["Installing a cracked app 'to get work done'","Malware + licence violation","The firm (legal + security)"],
     ["Installing games on a shared lab PC","Slows the machine, fills it with malware","The next class / every other student"],
     ["Sharing the Wi-Fi/server password freely","Untraceable misuse (torrents, mining)","The organization that owns the network"]],
    per_page=6,widths=[2.4,2.6,2.0],fs=11,
    note="None of these is a 'hacker' — the damage is 100% insider and usually careless, not malicious. That's why the fix is behaviour, not just tools.")
concept_apply("S8 · Concept 1 · [THEORY]","Who Is an 'IT User'",
    "A college computer lab where students install games and cracked software on shared PCs — slowing them, filling them with malware, ruining them for the next class. No hacker involved; the damage is 100% insider, and every student who installed something contributed to it.",
    "\"Only the IT department is responsible for misuse.\" Every user shares responsibility for safe, ethical use. The IT department locks the doors — but if you prop them open, that's on you. Because most incidents start inside, no amount of security tooling substitutes for responsible user behaviour.",
    "An IT user is anyone who uses an organization's IT resources, not just the IT department. Most security and ethics incidents begin with ordinary users — the insider risk — and are usually careless rather than malicious. Since harm starts inside, the remedy is changing user behaviour (AUPs, anti-piracy, use norms), because security is a shared duty, not a department.",
    "IT user · insider risk · careless not malicious · shared responsibility · behaviour over tools")

concept_understand("S8 · Concept 2 · [THEORY] [EXAMPLE]","Acceptable Use Policy (AUP)",
    "An AUP is a document stating what users may and may not do with the organization's IT resources. It defines four things: permitted use, prohibited use, monitoring, and consequences. What gives it ethical force is that users acknowledge/sign it.",
    ["Permitted — work tasks, reasonable limited personal use.",
     "Prohibited — piracy, personal USBs, offensive content, side businesses on company email.",
     "Monitoring — a clear statement the org MAY monitor use (this makes later monitoring fair; ties to S9).",
     "Consequences — warning → dismissal → legal action. The signature turns a vague expectation into informed consent."],
    None,"A signed AUP means you can never say 'I didn't know'.",
    "~8 min. Reward rules that name a CONSEQUENCE — students forget that an unenforced rule is just a suggestion (echoes Unit 1: enforcement beats the document).")
add_table_slide("S8 · Concept 2 · scaffolding","The four things every AUP defines",
    ["AUP element","What it states","Example clause"],
    [["Permitted use","What you may do","Work tasks; reasonable limited personal browsing"],
     ["Prohibited use","What you may not do","No piracy, no personal USBs, no side business on company email"],
     ["Monitoring","That the org may watch use","'Your email and web use may be monitored' (makes later monitoring fair)"],
     ["Consequences","What happens on breach","Warning → suspension → dismissal → legal action"]],
    per_page=4,widths=[1.6,2.4,3.4],fs=11.5,
    note="The signature is the ethical hinge: it converts a vague expectation into informed, consented agreement — 'I didn't know' stops being available.")
add_table_slide("S8 · Concept 2 · examples","A lab/office AUP — Allowed vs Prohibited",
    ["Allowed","Prohibited"],
    [["Using PCs for coursework and assignments","Installing cracked or unlicensed software"],
     ["Reasonable, brief personal use on a break","Torrenting movies or games on the network"],
     ["Saving work to approved storage","Plugging in personal USB drives without scanning"],
     ["Printing documents you need","Accessing offensive or illegal content"],
     ["Reporting a fault to IT","Running a side business on company email/resources"],
     ["Using licensed, provided applications","Crypto-mining or unauthorised background jobs"]],
    per_page=6,widths=[1,1],fs=12,
    note="This two-column card IS the AUP for most everyday cases — it draws the line in advance, before anyone can claim ambiguity.")
concept_apply("S8 · Concept 2 · [THEORY] [EXAMPLE]","Acceptable Use Policy (AUP)",
    "A bank or telecom (NTC / Ncell) staff AUP bans personal USB drives and unlicensed software; a university's IT-use policy is agreed to at enrolment. These are the same insider risks from Concept 1, now governed by a signed rule everyone has consented to.",
    "\"An AUP is just paperwork nobody reads.\" Its power is the signature: it converts a vague expectation into informed consent, so 'I didn't know' is gone. And an AUP with no named consequence is just a suggestion — enforcement, as in Unit 1, beats the document.",
    "An Acceptable Use Policy states what users may and may not do with IT resources, defining permitted use, prohibited use, monitoring, and consequences. Because users sign it, it becomes an informed, consented agreement — the basis for fair monitoring (S9) and for discipline. Its force depends on named consequences and real enforcement.",
    "AUP · permitted/prohibited · monitoring clause · consequences · signed = informed consent")

concept_understand("S8 · Concept 3 · [THEORY] [EXAMPLE]","Software Piracy",
    "Software piracy is copying, installing, or distributing software without a valid licence. Its forms: counterfeiting (selling fakes as genuine), unlicensed installs (one copy on ten machines, or a cracked version), and licence violation (a 5-seat licence used by 50 people). It is BOTH a legal and an ethical harm.",
    ["Legal harm — copyright infringement (full treatment in Unit 3, Intellectual Property).",
     "Ethical harm — you took the value of someone's work without paying: a fairness violation.",
     "Don't let it collapse into 'just illegal' — the ethics stands on its own even where enforcement is weak.",
     "'Everyone does it' is the Unit 1 normalization trap — name it as a trap, not an excuse."],
    None,"Piracy isn't just illegal — it's taking value you never paid for.",
    "~9 min. High piracy rates across Nepal/South Asia; offices on cracked Windows/Office. Make the dual-harm point: the wrong isn't profiting, it's using value you never paid for.")
add_table_slide("S8 · Concept 3 · comparison","Three forms of software piracy",
    ["Form","What it is","Example"],
    [["Counterfeiting","Selling fake copies as if genuine","A shop selling pirated Windows DVDs as 'original'"],
     ["Unlicensed install","One purchased copy on many machines, or a cracked version","Installing cracked AutoCAD across a whole office"],
     ["Licence violation","Exceeding what the licence permits","A 5-seat licence actually used by 50 staff"]],
    per_page=3,widths=[1.7,3.0,2.8],fs=12,
    note="All three are piracy even with no sale involved — the harm is USING value you never paid for, not profiting from it.")
concept_apply("S8 · Concept 3 · [THEORY] [EXAMPLE]","Software Piracy",
    "High software-piracy rates across Nepal / South Asia; countless offices running cracked Windows / Office; and the 'everyone does it' normalization — the Unit 1 trap where something stops feeling wrong because it's everywhere. Name it as a trap, not an excuse.",
    "\"It's only piracy if I sell it.\" Using an unlicensed copy is already a violation — no sale required. The wrong isn't profiting; it's using value you never paid for. Installing one cracked copy for yourself already crosses the line — like sneaking into a movie hall, you were never entitled to the seat.",
    "Software piracy is using, copying, or distributing software without a valid licence, in forms including counterfeiting, unlicensed installs, and licence violation. It is both a legal harm (copyright infringement — Unit 3) and an ethical one (taking the value of someone's work without paying). 'Everyone does it' is normalization, a decision trap, not a justification.",
    "software piracy · counterfeiting · unlicensed install · licence violation · legal + ethical harm · normalization")

concept_understand("S8 · Concept 4 · [THEORY]","Inappropriate Use of IT Resources",
    "Inappropriate use is using organizational resources for unauthorized, personal, or harmful purposes. Unlike piracy, the software may be perfectly licensed — the problem is the PURPOSE. The common thread: resources provided for work, diverted to non-work or harmful ends.",
    ["Examples: excessive personal browsing/streaming/gaming, accessing offensive content, a side business on company email, unauthorized apps.",
     "The line is usually about degree and impact, not a bright rule.",
     "A workable test: reasonableness + the AUP + impact on your work.",
     "A 30-second eSewa payment on a break is reasonable; streaming cricket all afternoon isn't."],
    None,"Right tools, wrong purpose — the AUP draws the line in advance.",
    "~5 min. Most real cases are about degree and impact, which is exactly why the AUP exists to draw the line before the situation arises.")
add_table_slide("S8 · Concept 4 · examples","Where's the line? — everyday office actions (Nepal AUP)",
    ["Action","Typical verdict","Why"],
    [["Charging your phone on the office PC","Depends","Trivial, but some AUPs restrict USB ports"],
     ["Installing a cracked PDF editor","Prohibited","Software piracy — a clear licence violation"],
     ["A quick eSewa / Khalti payment on a break","Allowed","Reasonable, brief, no impact on work"],
     ["Running a weekend freelance project on the work laptop","Prohibited","Resource misuse + IP conflict with the employer"],
     ["Plugging in a personal USB to print a file","Depends","Malware risk; often needs a scan or is banned outright"],
     ["Streaming cricket all afternoon","Prohibited","Excessive personal use — impacts work and bandwidth"]],
    per_page=6,widths=[3.0,1.4,2.6],fs=11,
    note="The 'depends' rows are exactly the ones an AUP must spell out in advance — ambiguity is where misuse hides. Test each with reasonableness + AUP + impact.")
concept_apply("S8 · Concept 4 · [THEORY]","Inappropriate Use of IT Resources",
    "A government-office computer used for personal Facebook and online shopping during work hours — a familiar sight, and a clean example of inappropriate use that isn't illegal but wastes public resources and time. Is a quick eSewa payment and a family message the same thing? The test is reasonableness + AUP + impact.",
    "\"If it's not illegal, using work resources for personal things is fine.\" Inappropriate use is usually legal — the wrong is diverting resources given for work to non-work or harmful ends. Most cases turn on degree and impact, which is why the AUP draws the line in advance rather than leaving it to each person's judgment.",
    "Inappropriate use is using organizational IT resources for unauthorized, personal, or harmful purposes — the software may be fully licensed; the problem is the purpose. Examples range from excessive personal browsing to side businesses on company email. The workable test is reasonableness + the AUP + impact on work, and the AUP exists to draw that line before the situation arises.",
    "inappropriate use · right tools wrong purpose · reasonableness + AUP + impact · degree and impact")

add_activity("S8 — 'Where's the line?'  ·  ~5 min",
    ["In pairs (2 min): sort five actions into Allowed / Prohibited / Depends for a typical Nepali office AUP.",
     "The five: (1) charging your phone on the office PC, (2) installing a cracked PDF editor, (3) a quick eSewa payment, (4) a weekend freelance project on the work laptop, (5) a personal USB to print a file.",
     "Take answers aloud (3 min).",
     "The point: the 'depends' cases are exactly what an AUP must spell out — ambiguity is where misuse hides."],
    "(2) is clearly prohibited (piracy); (4) is usually prohibited (resource + IP issues); (1), (3), (5) are the genuine 'depends' — push students to justify with reasonableness + impact.",
    "ACTIVITY [~5 min].")
add_quiz("S8 — Quick Check  ·  ~5 min",
    [("Q1.  The document defining what users may/may not do with IT resources is the:","q"),
     ("a) EULA   b) ✅ Acceptable Use Policy (AUP)   c) invoice   d) warranty","a"),
     ("     Why: the AUP is the signed rulebook of permitted/prohibited use, monitoring, and consequences.","o"),
     ("Q2.  Installing a cracked copy of Office for office work (not selling it) is:","q"),
     ("a) fine if unsold   b) ✅ software piracy   c) fair use   d) open source","a"),
     ("     Why: using an unlicensed copy is already piracy — no sale is required for the violation.","o"),
     ("Discussion: is software piracy in Nepal mainly an ethics, affordability, or enforcement problem?","o")],
    "QUIZ [~5 min]. Reward 'all three interacting': affordability tempts, weak enforcement removes deterrence, 'everyone does it' erodes ethics (Unit 1's situational view).")
add_summary("S8 · Summary  ·  [~2 min]",
    ["Users cause most incidents — the insider risk is real, and every user shares responsibility.",
     "AUPs set the rules everyone signs (permitted, prohibited, monitoring, consequences).",
     "Piracy (using unlicensed software) and inappropriate use (right tools, wrong purpose) are the two biggest user-ethics issues."],
    "On day one of any job you'll sign an AUP, and breaking it — through piracy or misuse — is one of the most common reasons people are fired or sued. It's rarely a dramatic hack that ends a career; it's a cracked install traced back to you, or company resources caught powering a side hustle.",
    "S9 — the user's flip side: their privacy and anonymity.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S9
add_divider("Session 9 · Lecture hour 4 (of 5)","Key Privacy and Anonymity Issues",
    "You fill a loan form at a bank. You hand your number to a SIM dealer. You scan a QR to enter a mall. A week later you're flooded with spam calls about loans you never asked for. Your data clearly travelled somewhere — so when did you consent to THIS?",
    "OPENING HOOK [~5 min]. Keep it personal — every student has had an unexplained spam call. Agenda: data privacy → surveillance → online anonymity → identity & identity theft.")

concept_understand("S9 · Concept 1 · [THEORY] [EXAMPLE]","Data Privacy — control over your personal data",
    "Data privacy is the right of individuals to control how their personal data is collected, used, and shared. The keyword is CONTROL: privacy isn't secrecy, it's who decides. Three operational principles: consent, purpose limitation, and data minimization.",
    ["Consent — data should be collected with your informed agreement, not silently.",
     "Purpose limitation — data collected for one reason (a loan) shouldn't be reused for another (marketing) without asking.",
     "Data minimization — collect only what you actually need; a SIM purchase doesn't need your blood group.",
     "When these fail, the harms are profiling (silent targeting) and fraud (leaked data enabling impersonation)."],
    "s9_trail.png","Privacy is about control, not secrecy — you close the curtains even with nothing to hide.",
    "~9 min. KYC data is among Nepal's richest datasets. Nepal's Individual Privacy Act 2075 (2018) recognises a legal right to privacy; reported leaks show the gap between law and enforcement.")
add_table_slide("S9 · Concept 1 · scaffolding","The three data-privacy principles — and what breaking each looks like",
    ["Principle","One-line meaning","Violation example (Nepal / IT)"],
    [["Consent","Collect data only with informed agreement","A SIM dealer selling your number to loan marketers"],
     ["Purpose limitation","Use data only for the reason it was collected","Loan-form data reused to target you with ads"],
     ["Data minimization","Collect only what you actually need","A mall QR form demanding your citizenship number"]],
    per_page=3,widths=[1.8,2.7,3.0],fs=12,
    note="Nepal's Individual Privacy Act 2075 recognises these rights; reported citizen-data leaks show the gap between a law existing and being enforced.")
concept_apply("S9 · Concept 1 · [THEORY] [EXAMPLE]","Data Privacy",
    "KYC data held by Nepali banks and telecoms is among the richest personal datasets in the country. Nepal's Individual Privacy Act, 2075 (2018) recognises a legal right to privacy of personal information — yet reported leaks of citizen data show the gap between having a law and enforcing it.",
    "\"I have nothing to hide, so privacy doesn't matter to me.\" Privacy is about control and power, not hiding wrongdoing. You lock your door not because you're doing something wrong inside, but because it's yours to control who enters. 'Nothing to hide' confuses secrecy with control — you still close the curtains.",
    "Data privacy is the right to control how your personal data is collected, used, and shared — control, not secrecy. It rests on consent (informed agreement), purpose limitation (use only for the collected reason), and data minimization (collect only what's needed). When these fail, the harms are profiling and fraud. Nepal's Individual Privacy Act 2075 gives legal backing, unevenly enforced.",
    "data privacy · control not secrecy · consent · purpose limitation · minimization · Individual Privacy Act 2075")

concept_understand("S9 · Concept 2 · [THEORY]","Surveillance — systematic monitoring",
    "Surveillance is the systematic monitoring of people's activities, communications, or location. 'Systematic' matters — a one-off glance isn't surveillance; a system that logs everyone, always, is. Its forms: workplace monitoring, CCTV, government surveillance, and app/location tracking.",
    ["The central tension is security vs privacy — more monitoring can mean more safety, but every increment costs privacy.",
     "There is no free lunch: the ethical work is deciding how much monitoring is PROPORTIONATE to the real risk.",
     "And whether people were TOLD — transparency + consent is the ethical lever.",
     "This is why the AUP's 'monitoring' clause from S8 exists: disclosure is what separates monitoring from spying."],
    "s9_seesaw.png","Every gain in security costs some privacy — the question is proportionality + disclosure.",
    "~8 min. Rising CCTV in Kathmandu; employer email/screen monitoring; SIM/biometric registration. Ask if each trade is proportionate.")
add_table_slide("S9 · Concept 2 · comparison","Same technology, different ethics — spying vs legitimate monitoring",
    ["Question","Secret surveillance (spying)","Legitimate monitoring"],
    [["Were people told in advance?","No — it's hidden","Yes — stated in a signed AUP (S8)"],
     ["Did they consent?","No","Yes — acknowledged the policy"],
     ["Is the scope proportionate?","Often excessive — everything, always","Limited to a stated, work-related purpose"],
     ["Ethical verdict","Violates privacy / autonomy","Fair — transparency + consent make it legitimate"]],
    per_page=4,widths=[2.0,2.5,2.5],fs=11.5,
    note="Keystroke logging + screenshots can be either — the SAME technology. Transparency and consent (the S8 AUP clause) are what shift it from spying to monitoring.")
concept_apply("S9 · Concept 2 · [THEORY]","Surveillance",
    "Rising CCTV across Kathmandu, employers monitoring staff email and screens, and SIM / biometric registration linking your identity to your activity — each trades some privacy for some claimed security. Your employer logging every keystroke and taking screenshots is ethical only once staff are told in advance and consent (the S8 AUP clause).",
    "\"If it improves security, more monitoring is always good.\" Every increment of monitoring costs privacy — there's no free lunch. The ethical test is proportionality (is this much watching justified by the actual risk?) and disclosure (were people told?). A disclosed policy is the difference between monitoring and spying.",
    "Surveillance is the systematic monitoring of activities, communications, or location (workplace, CCTV, government, app tracking). It sits on a security-vs-privacy trade-off: every gain in security costs privacy. What makes monitoring legitimate rather than spying is proportionality to the real risk plus transparency and consent — exactly why the AUP declares monitoring in advance.",
    "surveillance · systematic monitoring · security vs privacy · proportionality · transparency + consent")

concept_understand("S9 · Concept 3 · [THEORY]","Anonymity Online — a double-edged tool",
    "Anonymity is acting online without revealing your real identity. The whole point: it is neither good nor bad — it's a tool with two edges, and the same feature does both jobs.",
    ["It PROTECTS whistle-blowers exposing corruption, activists under pressure, and free speech for the vulnerable.",
     "It SHIELDS trolls, scammers, and criminals who use the same cover to harass and defraud.",
     "You can't simply ban or fully allow it — any rule that silences the troll also silences the whistle-blower.",
     "That's why real-name policies are so contested (the CFU debate)."],
    None,"The same mask that protects the whistle-blower shields the troll.",
    "~8 min. Anonymous Nepali pages exposing corruption vs anonymous pages spreading rumours — same tool, opposite uses, which is why it's hard to regulate.")
add_table_slide("S9 · Concept 3 · comparison","Anonymity — the same tool, two opposite edges",
    ["Anonymity...","Protective edge (good)","Harmful edge (bad)"],
    [["Who uses it","Whistle-blowers, activists, the vulnerable","Trolls, scammers, harassers"],
     ["What it enables","Exposing corruption; free speech under pressure","Harassment and fraud without consequence"],
     ["Nepal example","Pages exposing corruption safely","Pages spreading rumours and harassing people"],
     ["Why it can't be banned","Silencing the troll also silences the whistle-blower","Allowing it fully shields the criminal too"]],
    per_page=4,widths=[1.9,2.6,2.6],fs=11.5,
    note="Same tool, opposite uses — which is exactly why real-name registration is so contested (S9 CFU). Note: true anonymity is rare — IP logs, metadata, and device fingerprints leave a trail.")
concept_apply("S9 · Concept 3 · [THEORY]","Anonymity Online",
    "Anonymous Nepali Facebook / X pages exposing corruption (anonymity protecting public-interest speech) versus anonymous pages spreading rumours and harassment (anonymity shielding harm). Same tool, opposite uses — which is exactly why it's so hard to regulate.",
    "\"Online, I'm completely anonymous.\" IP logs, metadata, and device fingerprints make true anonymity rare — you almost always leave a trail, which is why people do get traced and arrested for anonymous posts. Feeling anonymous is not the same as being anonymous.",
    "Anonymity is acting online without revealing your real identity — a double-edged tool. The same feature protects whistle-blowers, activists, and free speech while shielding trolls, scammers, and criminals. It can be neither fully banned nor fully allowed, because any rule that silences the troll also silences the whistle-blower. And true anonymity is rare: logs and metadata leave a trail.",
    "anonymity · double-edged tool · whistle-blower vs troll · real-name debate · true anonymity is rare")

concept_understand("S9 · Concept 4 · [THEORY] [EXAMPLE]","Identity & Identity Theft — you are your data",
    "Online, your identity is the data that represents you — your name, citizenship number, bank/eSewa logins, biometrics. To a system you are not a person but a bundle of data fields, and whoever controls those fields can BE you. That's identity theft: fake profiles and stolen credentials.",
    ["Identity theft/impersonation happens through fake profiles and stolen credentials.",
     "The usual method is phishing — tricking you into handing over your own keys (previewed fully in Unit 7).",
     "In Nepal the most common attack is a phishing SMS posing as eSewa or a bank to steal your OTP.",
     "Your data is like your house key: easy to copy, and you don't notice until someone's already inside."],
    None,"You are a bundle of data fields — control them, or someone else becomes you.",
    "~5 min. Fake Facebook profiles impersonating public figures (reputation + fraud harm); phishing SMS posing as eSewa/bank to steal an OTP — the attack ordinary Nepalis actually face.")
add_table_slide("S9 · Concept 4 · examples","How identity gets stolen — method, Nepal example, defence",
    ["Method","How it works","Everyday defence"],
    [["Phishing SMS / call","Fake 'eSewa/bank' message tricks you into sharing an OTP","Never share an OTP; banks never ask for it"],
     ["Fake social profile","Impersonates you or a public figure to defraud contacts","Report it; verify before trusting a request"],
     ["Stolen credentials","A leaked/reused password unlocks your accounts","Unique passwords + two-factor authentication"],
     ["Data-leak reuse","Leaked KYC data used to impersonate you elsewhere","Minimise what you share; watch for misuse"]],
    per_page=4,widths=[1.7,3.0,2.6],fs=11.5,
    note="Phishing is the single most common entry point (full treatment in Unit 7). Nobody 'steals the house' — they copy the key (your data) and walk in the front door.")
concept_apply("S9 · Concept 4 · [THEORY] [EXAMPLE]","Identity & Identity Theft",
    "Fake Facebook profiles impersonating Nepali public figures (reputation + fraud harm); and phishing SMS posing as eSewa or a bank to steal your OTP — the single most common attack ordinary Nepalis actually face. The attacker doesn't need to hack a server; they just need you to hand over your key.",
    "\"Identity theft only happens to careless or rich people.\" Your personal data is like your house key — easy to copy, and you usually don't notice until someone is already inside. Anyone who shares an OTP once, or reuses a leaked password, is exposed; the attack targets ordinary people precisely because it's cheap and scalable.",
    "Online, identity is the data that represents you (name, citizenship number, logins, biometrics) — to a system you are a bundle of data fields, and whoever controls them can impersonate you. Identity theft uses fake profiles and stolen credentials, most often obtained via phishing. In Nepal, OTP-stealing phishing SMS posing as eSewa or a bank is the most common case.",
    "identity · you are your data · identity theft · impersonation · phishing · OTP · never share your key")

add_activity("S9 — 'Trace your data trail'  ·  ~5 min",
    ["In pairs (2 min): pick one routine action from this morning (SIM top-up, QR scan, eSewa login, TikTok post).",
     "Map: (a) what personal data you handed over, (b) who else might now have it, (c) whether you actually consented.",
     "Take 3 answers aloud (3 min) and plot each on the 'data trail' visual.",
     "Close: most of you couldn't fully answer (b) and (c) — and that uncertainty IS the privacy problem in one sentence."],
    "Use the hook's spam-call chain (form/SIM/QR → company → third parties → spam) as the model if a pair stalls. The point is that the trail is invisible and unconsented — that's the harm.",
    "ACTIVITY [~5 min].")
add_quiz("S9 — Quick Check  ·  ~5 min",
    [("Q1.  'Collect only the data you actually need' is the principle of:","q"),
     ("a) surveillance   b) ✅ data minimization   c) anonymity   d) profiling","a"),
     ("     Why: minimization limits collection to what's necessary — a SIM sale doesn't need your blood group.","o"),
     ("Q2.  Online anonymity is best described as:","q"),
     ("a) always good   b) always harmful   c) ✅ a double-edged tool   d) impossible","a"),
     ("     Why: the same cover protects whistle-blowers and shields trolls — it is neither wholly good nor bad.","o"),
     ("Discussion: should the government require real-name registration to post on social media?","o")],
    "QUIZ [~5 min]. Force the trade-off: for = less trolling/fake accounts; against = silences whistle-blowers, builds a dangerous ID database, easily evaded by real criminals.")
add_summary("S9 · Summary  ·  [~2 min]",
    ["Privacy = control over your data — built on consent, minimization, purpose limitation (not 'nothing to hide').",
     "Surveillance trades security for privacy; transparency and consent are what make monitoring legitimate.",
     "Anonymity cuts both ways; your identity is now the target, and phishing is the usual entry point."],
    "As a BIM graduate you'll handle customer data — KYC records, payment details, account logins. Mishandling it can break Nepal's Individual Privacy Act 2075 AND destroy customer trust, a business risk, not just a legal one. Consent, purpose limitation, and minimization are the design rules you'll build into the systems you ship.",
    "S10 — where privacy, anonymity, and harm collide most: social networking.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S10
add_divider("Session 10 · Lecture hour 5 (of 5) — CLOSES UNIT 2","Social Networking Ethical Issues",
    "A doctored screenshot of a Nepali celebrity goes viral on TikTok/Facebook before lunch. By evening a teenager is being mocked in her school group chat, and a 'breaking news' rumour has sparked a panic. How many servers were hacked? None. Ordinary people did all the damage, using the apps exactly as designed.",
    "OPENING HOOK [~5 min]. This session ties Unit 1 (scale/speed/permanence) and S9 (privacy/anonymity) into recognisable Nepali events. Agenda: why it's an ethics hotspot → cyberbullying/harassment → fake news → defamation.")

concept_understand("S10 · Concept 1 · [THEORY]","Why Social Networking Is an Ethics Hotspot",
    "Social networking = platforms where users create, share, and connect (Facebook, TikTok, Instagram, X, YouTube). Four amplifiers turn ordinary behaviour into outsized harm — these are the Unit 1 IT factors, now made personal: scale, speed, anonymity, virality.",
    ["Scale — one post reaches thousands instantly, not the few people in a room.",
     "Speed — it spreads before anyone can check or correct it.",
     "Anonymity — people say things they'd never say to your face (S9's double edge).",
     "Virality + the online bystander effect — the algorithm amplifies outrage, and in a crowd of thousands everyone assumes someone else will speak up, so no one does."],
    None,"Scale + speed + anonymity + virality turn one careless act into mass harm.",
    "~8 min. Nepal's very high Facebook/TikTok usage, where viral content shapes public opinion and elections. The harm grows in the silence of the bystanders.")
add_table_slide("S10 · Concept 1 · scaffolding","The four amplifiers — how a small act becomes mass harm",
    ["Amplifier","What it does","Everyday example"],
    [["Scale","One post reaches thousands, not a roomful","A rumour shared to a 50k-follower page"],
     ["Speed","Spreads before anyone can check or correct","A fake 'breaking news' clip trending in minutes"],
     ["Anonymity","People say what they'd never say to your face","Abusive comments from throwaway accounts"],
     ["Virality","The algorithm boosts the most emotional content","An outrage post pushed to millions of feeds"],
     ["Bystander effect","In a huge crowd, everyone assumes someone else will act","Thousands watch a pile-on; no one intervenes"]],
    per_page=5,widths=[1.5,2.8,2.7],fs=11.5,
    note="These are Unit 1's scale/speed/permanence factors, now personal. The harm grows in the silence — passive bystanders are part of the mechanism.")
concept_apply("S10 · Concept 1 · [THEORY]","Why Social Networking Is an Ethics Hotspot",
    "Nepal's very high Facebook / TikTok usage, where viral content shapes public opinion and even elections — a scale of influence that ordinary individuals now hold in their thumbs. One share button connects a careless act to thousands of strangers in minutes.",
    "\"It's just online — it isn't real / it doesn't count.\" Online harm has real legal, social, and psychological consequences — lost jobs, depression, arrests under the ETA. The screen is not a shield between the act and the harm; the amplifiers make the harm bigger, not less real.",
    "Social networking is an ethics hotspot because four amplifiers — scale, speed, anonymity, and virality — turn ordinary behaviour into outsized harm, compounded by the online bystander effect where everyone assumes someone else will intervene. These are Unit 1's IT factors made personal; online harm carries real legal, social, and psychological consequences.",
    "social networking · scale · speed · anonymity · virality · bystander effect · online harm is real")

concept_understand("S10 · Concept 2 · [THEORY] [EXAMPLE]","Cyberbullying & Online Harassment",
    "Cyberbullying/harassment is using digital tools to REPEATEDLY threaten, humiliate, or target a person. The word 'repeatedly' matters — a single rude comment is unkind; a pattern aimed at someone is harassment. Its forms: trolling, doxxing, group pile-ons, and gendered harassment.",
    ["Trolling — deliberately provoking to upset.",
     "Doxxing — publishing someone's private details to expose them to harm.",
     "Group pile-ons — many people targeting one, amplified by scale.",
     "Gendered harassment — aimed especially at women. The mental-health impact is severe: anxiety, withdrawal, in extreme cases self-harm."],
    None,"One rude comment is unkind; a repeated pattern aimed at a person is harassment.",
    "~8 min. Harassment of Nepali women and public figures in comment sections; ordinary school group-chat bullying — the same dynamic at national and classroom scale.")
add_table_slide("S10 · Concept 2 · examples","Forms of cyberbullying & harassment",
    ["Form","What it is","Example"],
    [["Trolling","Deliberately provoking to upset or derail","Posting inflammatory replies to bait a reaction"],
     ["Doxxing","Publishing private details to expose someone to harm","Leaking a person's home address and phone number"],
     ["Group pile-on","Many people targeting one, amplified by scale","A comment section swarming one individual"],
     ["Gendered harassment","Targeting aimed especially at women","Sexualised abuse of women public figures online"],
     ["Group-chat bullying","Repeated mocking in a shared chat","A class group chat mocking one classmate"],
     ["Threats / intimidation","Direct threats of harm","Menacing DMs meant to frighten a target"]],
    per_page=6,widths=[1.7,2.8,2.5],fs=11,
    note="The common thread is a REPEATED pattern aimed at a person — and the well-documented, severe mental-health impact (anxiety, withdrawal, self-harm).")
concept_apply("S10 · Concept 2 · [THEORY] [EXAMPLE]","Cyberbullying & Online Harassment",
    "Harassment of Nepali women and public figures in Facebook / TikTok comment sections, and ordinary school group-chat bullying — the same dynamic at national and classroom scale. Your friend group starts mocking a classmate in a shared chat and you say nothing: the online bystander effect means silence reads as agreement and fuels the pile-on.",
    "\"I just didn't join in, so I'm not part of it.\" Passive bystanders are part of the mechanism that makes pile-ons hurt — silence in a group chat reads as agreement. There's a duty to intervene, even at low cost: DM the target, name it as too far, or leave the chat.",
    "Cyberbullying/harassment is using digital tools to repeatedly threaten, humiliate, or target a person; the pattern (not a single comment) is what defines it. Forms include trolling, doxxing, group pile-ons, and gendered harassment, with severe mental-health impact. The online bystander effect makes silence complicit, creating a duty to intervene.",
    "cyberbullying · repeated targeting · trolling · doxxing · pile-on · gendered harassment · bystander duty")

concept_understand("S10 · Concept 3 · [THEORY]","Fake News & Misinformation",
    "The key distinction students conflate: MISinformation is false info spread carelessly (you believed it and shared without checking — no intent to deceive). DISinformation is false info spread deliberately to mislead (intent to deceive — propaganda, scams, coordinated campaigns).",
    ["The difference is INTENT — careless sharing vs deliberate deception.",
     "Why it spreads faster than truth: it exploits emotion (fear, outrage).",
     "It rides confirmation bias — we share what fits our existing beliefs.",
     "And engagement algorithms boost outrage because it keeps people scrolling. Truth is boring; outrage is viral."],
    "s10_verify.png","Mis- = careless, no intent; Dis- = deliberate deception. The difference is intent.",
    "~8 min. False earthquake/disaster rumours that trigger panic, fake health cures, election misinformation — each a careless share doing real damage.")
add_table_slide("S10 · Concept 3 · comparison","Misinformation vs Disinformation",
    ["Dimension","Misinformation","Disinformation"],
    [["Intent","None — believed it, shared carelessly","Deliberate — intent to deceive"],
     ["Typical source","An ordinary user who didn't check","Propagandists, scammers, coordinated campaigns"],
     ["Example (Nepal)","Forwarding a fake 'health cure' you trusted","A staged rumour to sway an election or scam money"],
     ["Are you responsible?","Yes — the share button is an act","Yes — and the intent makes it worse"]],
    per_page=4,widths=[1.8,2.6,2.6],fs=11.5,
    note="Both spread because they exploit emotion, ride confirmation bias, and are boosted by engagement algorithms — truth is boring, outrage is viral.")
concept_apply("S10 · Concept 3 · [THEORY]","Fake News & Misinformation",
    "False earthquake / disaster rumours that trigger panic, fake health cures, and election misinformation circulating on Nepali social media — each a case where a careless share did real damage to real people. The person who forwarded it 'just to warn friends' became the reason it reached thousands more.",
    "\"Sharing isn't creating it, so I'm not responsible.\" Forwarding unverified content spreads the harm — the share button is an act. You become a link in the chain that delivers the lie to a thousand more people. 'I only forwarded it' is not a defence; it's a description of how the harm scaled. A lie online is cheap to send, impossible to recall.",
    "Misinformation is false information shared carelessly (no intent to deceive); disinformation is false information spread deliberately to mislead — the difference is intent. Both outrun the truth because they exploit emotion, ride confirmation bias, and are boosted by engagement algorithms. Forwarding unverified content makes you a link in the chain: the share button is an ethical act.",
    "misinformation · disinformation · intent to deceive · confirmation bias · engagement algorithms · share button is an act")

concept_understand("S10 · Concept 4 · [THEORY] [EXAMPLE]","Defamation & Reputation Harm",
    "Defamation is a false statement, presented as fact, that damages someone's reputation. The dividing line: opinion/criticism is NOT defamation. 'I didn't like this café' is opinion; 'this café's owner is a thief' is a false statement of fact — that's what crosses into defamation. The test: fact vs opinion, and true vs false.",
    ["Opinion and honest criticism are protected — they aren't statements of fact that can be 'false'.",
     "Defamation requires a false statement OF FACT that harms reputation.",
     "In Nepal, online defamation can be treated as a cybercrime under the Electronic Transactions Act, 2063 (full law in Unit 9).",
     "Live tension: the same law has been criticised for chilling free speech."],
    "s10_spectrum.png","Opinion & criticism are protected; a false statement of fact is defamation.",
    "~5 min. VERIFY current cyber-law before teaching specifics — ETA 2063 is older and the landscape is evolving. Present 'arrests for Facebook posts' as illustrating the debate, not settled current law.")
add_table_slide("S10 · Concept 4 · examples","Opinion vs Criticism vs Defamation — classify the statement",
    ["Statement","Classification","Why / legal risk"],
    [["'I didn't enjoy this café's coffee.'","Opinion","Personal taste — not a factual claim; protected"],
     ["'This café's service is slow and overpriced.'","Criticism","Honest evaluation of experience; low risk"],
     ["'The owner of this café is a thief.'","Defamation","False statement of fact alleging a crime; high risk"],
     ["'I think shop X overcharges.'","Opinion","Framed as a personal view; lower risk"],
     ["'Shop X is a fraud that steals money.'","Defamation","False factual accusation of a crime; high risk"],
     ["Repeatedly posting a classmate's photo with insults","Harassment","Repeated targeting of a person (not defamation)"]],
    per_page=6,widths=[3.0,1.5,2.5],fs=11,
    note="⚠️ Verify the current legal position (ETA 2063 and later amendments) before teaching specifics. Rule of thumb: state experiences and opinions, not invented facts about people.")
concept_apply("S10 · Concept 4 · [THEORY] [EXAMPLE]","Defamation & Reputation Harm",
    "In Nepal, people have been arrested under the ETA for defamatory Facebook posts — alongside an ongoing public debate over free speech vs misuse of the law (critics argue it's been used to silence criticism, not just punish genuine lies). Present both sides. Compare 'I think shop X overcharges' (opinion) with 'Shop X is a fraud that steals money' (a false statement of fact — defamation risk).",
    "\"If I write it as my honest view, it can't be defamation.\" What matters is fact vs opinion and true vs false — dressing a false factual accusation as 'my view' doesn't protect you. But the reverse trap is real too: the ETA has been criticised for chilling legitimate criticism, so genuine opinion is not defamation. Verify current law before relying on specifics.",
    "Defamation is a false statement, presented as fact, that damages someone's reputation; opinion and honest criticism are excluded because they aren't falsifiable statements of fact. The test is fact-vs-opinion and true-vs-false. In Nepal online defamation can fall under the ETA 2063 (Unit 9), a law also criticised for chilling free speech — so verify the current position before teaching specifics.",
    "defamation · false statement of fact · opinion ≠ defamation · fact vs opinion · ETA 2063 · free-speech tension")

add_activity("S10 — 'Verify before you share'  ·  ~6 min",
    ["In pairs (2 min): take a plausible shocking headline (e.g. 'BREAKING: bank X collapses, withdraw your money now').",
     "Apply three pre-share checks: (1) who is the SOURCE, and is it credible? (2) is it REPORTED anywhere reputable, or only forwarded? (3) does it just TRIGGER emotion/urgency (a red flag)?",
     "Decide: share, hold, or report. Take 3 pairs aloud (4 min).",
     "Close by tying it to a real recent Nepali viral rumour — 'would these three checks have stopped it?'"],
    "The 'withdraw your money now' urgency is the tell — manufactured urgency is the single most common signature of disinformation and scams. Make students name it.",
    "ACTIVITY [~6 min].")
add_quiz("S10 — Quick Check  ·  ~5 min",
    [("Q1.  Deliberately spreading false information to mislead is:","q"),
     ("a) misinformation   b) ✅ disinformation   c) satire   d) opinion","a"),
     ("     Why: disinformation carries intent to deceive; misinformation is careless sharing without intent.","o"),
     ("Q2.  A false factual statement that damages someone's reputation is:","q"),
     ("a) criticism   b) opinion   c) ✅ defamation   d) anonymity","a"),
     ("     Why: defamation is a false statement of FACT — opinion and honest criticism are excluded.","o"),
     ("Discussion: before sharing a shocking post, what 2 checks should you do? Would they stop a recent rumour?","o")],
    "QUIZ [~5 min]. Expect 'check the source' and 'check a reputable outlet'. Push them to add 'does it just trigger emotion?' and apply it to a concrete recent rumour.")
add_summary("S10 · Summary  ·  [~2 min]",
    ["Social media scales everyday acts into big harm (scale + speed + anonymity + virality + bystander effect).",
     "The core issues are cyberbullying/harassment, fake news (mis- vs disinformation), and defamation (which excludes genuine opinion/criticism).",
     "Verify before you share — the share button is an ethical act with legal consequences."],
    "Your public posts are part of your professional reputation — recruiters check them before they interview you. And in Nepal, a careless defamatory or harassing post can lead to arrest under the ETA. A single bad share can cost you a job AND land you in a police station — which is why 'verify before you share' is a professional habit.",
    "Unit 3 — Intellectual Property: copyright, patents, trade secrets, trademarks, and IP misuse.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 2 · Cheat Sheet","One-page revision reference",
    [("IT-worker relationships (S6)","Six arrows: employer (loyalty/honesty), client (advice/disclose), suppliers (no bribes), peers (respect), users (support), society (safe systems). Access = power = responsibility."),
     ("Gift vs bribe test (S6)","Public? Timed around a decision? Could it influence you? Fail any → bribe."),
     ("Professionalism (S7)","IT = partial profession (has knowledge+codes, no licensing). Cert = skill (voluntary); licence = legal force (government); code = commitment; bodies = ACM/IEEE-CS/ISACA/CAN."),
     ("Ethical use (S8)","Insider risk = most incidents. AUP defines permitted/prohibited/monitoring/consequences (signed). Piracy = using unlicensed software; inappropriate use = right tools, wrong purpose."),
     ("Privacy & anonymity (S9)","Privacy = control (consent, purpose limitation, minimization). Surveillance = security vs privacy (needs proportionality + disclosure). Anonymity = double-edged. Identity theft via phishing."),
     ("Social networking (S10)","Amplifiers: scale/speed/anonymity/virality/bystander. Mis- (careless) vs dis-information (deliberate). Defamation = false statement of FACT; opinion/criticism excluded. Verify before you share.")])

add_glossary("Unit 2 · Glossary","Key terms — quick reference",
    [("IT worker","one who designs, builds, maintains, or manages IT systems and their data."),
     ("Privileged access","the technical ability to see/do far more than an ordinary user — creates a duty of care."),
     ("Conflict of interest","a competing interest that compromises loyalty to the employer."),
     ("Information asymmetry","the client can't judge technical quality, so must rely on the worker's honesty."),
     ("Gift vs bribe","a bribe fails the public / timed / influence test."),
     ("Profession (four-part test)","specialized education, body of knowledge, code of ethics, self-regulation."),
     ("Code of ethics","published principles members commit to (ACM, IEEE-CS)."),
     ("Certification","a voluntary credential proving a specific skill; not a licence."),
     ("Licence","government-granted, legally enforced right to practise."),
     ("Professional body","an organization that sets standards, runs certs, publishes codes (ACM, ISACA, CAN)."),
     ("IT user","anyone who uses an organization's IT resources."),
     ("Insider risk","most incidents start with ordinary users, usually careless not malicious."),
     ("AUP","Acceptable Use Policy — signed rules: permitted, prohibited, monitoring, consequences."),
     ("Software piracy","using/copying/distributing software without a valid licence."),
     ("Inappropriate use","using org resources for unauthorized, personal, or harmful purposes."),
     ("Data privacy","the right to control how your personal data is collected, used, shared."),
     ("Data minimization","collect only the data you actually need."),
     ("Surveillance","systematic monitoring of activity, communications, or location."),
     ("Anonymity","acting online without revealing your real identity — a double-edged tool."),
     ("Identity theft","impersonation via fake profiles or stolen credentials (often via phishing)."),
     ("Misinformation","false info shared carelessly, without intent to deceive."),
     ("Disinformation","false info spread deliberately to mislead."),
     ("Defamation","a false statement of fact that damages someone's reputation.")])

# ============= CONSOLIDATED END-OF-UNIT QUIZ =============
add_divider("Unit 2 · Revision","Consolidated end-of-unit quiz",
    "Twelve MCQs across the whole unit (answers shown), then short-answer, applied-case, and discussion questions to work from the concept slides and Unit2_material.md.",
    "Use as a 15–20 min in-class quiz or take-home review.")
add_quiz("Section A — Multiple choice (answers shown)",
    [("1.  Privileged access (admin rights, personal data) means an IT worker has extra   →  ✅ responsibility","a"),
     ("2.  A vendor's 'free iPhone' before a tender is best described as   →  ✅ a conflict of interest / bribery","a"),
     ("3.  The duty to give honest technical advice applies most directly to the   →  ✅ client","a"),
     ("4.  A government-granted, legally enforced permission to practise is   →  ✅ a licence","a"),
     ("5.  ACM and IEEE-CS are examples of   →  ✅ professional organizations","a"),
     ("6.  Certification mainly proves   →  ✅ a specific skill","a"),
     ("7.  The document defining what users may/may not do with IT resources is the   →  ✅ AUP","a"),
     ("8.  Installing a cracked copy of Office for office use (not selling) is   →  ✅ software piracy","a"),
     ("9.  'Collect only the data you actually need' is the principle of   →  ✅ data minimization","a"),
     ("10.  Online anonymity is best described as   →  ✅ a double-edged tool","a"),
     ("11.  Deliberately spreading false information to mislead is   →  ✅ disinformation","a"),
     ("12.  A false factual statement that harms someone's reputation is   →  ✅ defamation","a")],
    "Consolidated quiz Section A.",compact=True)
add_quiz("Sections B–D — short answer, applied case & discussion",
    [("Section B — Short answer","q"),
     ("13. List & explain three of the six IT-worker relationships + one risk each.   14. Differentiate certification vs licensing (who grants, legal force, what it proves).","o"),
     ("15. What four things does an AUP define?   16. Explain the 'I have nothing to hide' fallacy.   17. Distinguish misinformation, disinformation & defamation with one example each.","o"),
     ("Section C — Applied case","q"),
     ("18. Analyse the 'vendor gift before a tender' scenario with the Unit 1 5-step process: stakeholders, conflict, what the IT manager should do.","o"),
     ("19. Classify with reasons: (a) 'I didn't enjoy this café's coffee' (b) 'service is slow and overpriced' (c) 'the owner is a thief who poisons customers' (d) repeatedly posting a classmate's photo with insulting captions.","o"),
     ("Section D — Discussion","q"),
     ("20. 'IT workers in Nepal should be licensed like doctors and engineers.' Argue both sides, then state your own position.","o")],
    "Consolidated quiz Sections B–D. Model answers on the concept slides and in Unit2_material.md. Q19: (a)=opinion, (b)=criticism, (c)=defamation, (d)=harassment.",compact=True)

# ---- close ----
add_title("End of Unit 2  ·  IT 246",
          "S6–S10 complete: the IT-worker relationship web · professionalism (codes/certs/licensing/bodies) · ethical IT use (AUP, piracy, misuse) · privacy/surveillance/anonymity/identity · social-networking harms",
          "Built to COURSE_MATERIAL_STANDARD.md incl. the §7A depth rule · comparison & concrete-example tables throughout · "
          "self-contained, PDF-safe · Next: Unit 3 — Intellectual Property.")

_add_page_numbers()
save("IT246_Unit2.pptx")
