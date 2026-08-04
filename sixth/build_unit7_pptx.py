#!/usr/bin/env python3
"""IT246 (sixth) Unit 7 deck — Social Engineering and Cyber Terrorism (S33–S37), built to
COURSE_MATERIAL_STANDARD.md INCLUDING the §7A depth rule: every confusable set is a
comparison table, every 'X vs not-X' concept a concrete-example table (≥6 Nepal/IT-localised
rows + consequence/why), claims get scaffolding tables — each on its OWN slide, paginated,
never squeezed. Self-contained & PDF-safe. Imports deckkit.py. Diagrams in images/.
DEFENSIVE / awareness framing throughout: students learn to RECOGNISE and PREVENT attacks,
never to perform them; cyber terrorism is kept conceptual and responsible.
Run: python3 build_unit7_pptx.py -> IT246_Unit7.pptx
"""
from deckkit import *

# ============================================================
#                        FRONT MATTER
# ============================================================
add_title("Unit 7 — Social Engineering and Cyber Terrorism",
          "IT 246: IT Ethics & Cybersecurity  ·  BIM 6th Semester  ·  Sessions S33–S37",
          "Self-contained slides with depth: every concept grounded in comparison & concrete-example TABLES "
          "(Nepal / IT localised) — no abstraction without instances. DEFENSIVE / awareness framing only. "
          "Exports to PDF with no information lost.")

add_outcomes("Unit 7 — Learning Outcomes","social engineering & cyber terrorism  ·  s33–s37",
    "By the end of this unit, you will be able to:",
    ["Define social engineering and explain why humans are the 'weakest link' in security (S33)",
     "Recognise the psychological levers — trust, authority, reciprocity, urgency, fear — attackers exploit (S34)",
     "Identify the major attack types (phishing, vishing, smishing, pretexting, baiting, tailgating) and apply countermeasures (S35)",
     "Define cyber terrorism, distinguish it from cybercrime/hacktivism/warfare, and classify its types (S36)",
     "Explain its effects on critical infrastructure and how it is countered at personal, organizational & national levels (S37)"],
    "This is Unit 7 of IT 246. It shifts from attacking machines to attacking PEOPLE — the human layer of security — and then scales that up to attacks on a whole nation. Everything here is taught for DEFENCE: to recognise and prevent, never to perform.")

add_roadmap("Unit 7 — Roadmap","Where each session fits (S33–S37)",
    ["S33  Introduction to social engineering · why humans break first",
     "S34  The psychology — implications · building trust · exploiting it",
     "S35  Attack types (recognise) · countermeasures & prevention",
     "S36  Cyber terrorism · its types (vs crime/hacktivism/warfare)",
     "S37  Effects on infrastructure · countering it — closes the unit"],
    ["Unit 8   Digital forensics — investigating incidents after the fact",
     "Unit 9   Cyber law in Nepal (Electronic Transaction Act, Privacy Act)"])

# ============================================================ S33
add_divider("Session 33 · Lecture hour 1 (of 5)","Introduction to Social Engineering",
    "You can buy a Rs. 50,000 firewall, but if a polite caller says 'Namaste, I'm calling from your bank's head office' and you read out your OTP — the firewall never even gets a vote. Why do humans break before machines do?",
    "OPENING HOOK [~5 min]. People are the easiest system to 'hack'. Agenda: what social engineering is → why attackers use it → why humans are the weakest link. Keep it defensive — we learn to recognise, never to run, these tricks.")

concept_understand("S33 · Concept 1 · [THEORY]","What Is Social Engineering",
    "Social engineering = manipulating PEOPLE into giving up confidential information or access, instead of breaking technology directly. The attacker 'hacks the person, not the PC' — it targets human psychology (trust, helpfulness, fear), not code.",
    ["It bypasses the technology entirely: no firewall is defeated if a human opens the door.",
     "The 'system' being attacked is a person's judgement — persuasion and deception, not exploits.",
     "It works over any channel: a call, an SMS, an email, or a face-to-face visit.",
     "The tech (a fake page, a spoofed number) is only a prop; the con is the human manipulation."],
    "s33_human_firewall.png","Social engineering = hacking the person, not the PC.",
    "~7 min. Classic awareness scenario: an attacker impersonates the IT helpdesk to get an employee to reset a password. No code is broken — the human is persuaded. Keep the framing on recognising it.")
add_table_slide("S33 · Concept 1 · scaffolding","Hacking the machine vs hacking the person",
    ["Dimension","Technical attack (the machine)","Social engineering (the person)"],
    [["Target","Code, servers, encryption","A human's trust and judgement"],
     ["Method","Exploits, brute force, malware","Persuasion, deception, impersonation"],
     ["What it defeats","A weak system","A busy, polite, or fearful person"],
     ["Cost & skill","High — needs deep tech skill","Low — mostly a convincing story"],
     ["Nepal example","Cracking a bank's core system","Phoning a customer as 'bank security'"],
     ["Defence","Firewalls, patching, encryption","Awareness, verify-before-trust habits"]],
    per_page=6,widths=[1.5,2.7,2.8],fs=11,
    note="The whole point: social engineering routes AROUND the technology by targeting the person operating it. Defence is therefore human-first — awareness and habits, not just software.")
concept_apply("S33 · Concept 1 · [THEORY]","What Is Social Engineering",
    "A fake 'NTC / Ncell' SMS tells you your SIM will be blocked unless you 'verify' your details on a link; a caller claiming to be from your bank asks you to confirm the OTP just sent to your phone. No system was breached — the attacker simply persuaded a person to hand over the keys. Recognising this as manipulation, not a technical event, is the first defence.",
    "\"Social engineering is a technical hacking skill.\" It is mostly persuasion and deception; the technology is secondary. A scammer needs a convincing story far more than coding skill — which is exactly why anyone, not just 'techies', can be targeted and must stay alert.",
    "Social engineering is manipulating people into giving up confidential information or access, rather than defeating technology directly. It targets human psychology — trust, helpfulness, fear — so the attacker 'hacks the person, not the PC'. It works across calls, SMS, email, and in person, with the technology serving only as a prop for a human con.",
    "social engineering · hacking the person · manipulation not code · human layer · verify before trust")
add_table_slide("S33 · Concept 1 · concrete examples","Real Nepali social-engineering incidents — the con, not the code",
    ["Real case (Nepal / IT)","What the attacker actually did","Why it's social engineering (verdict)"],
    [["Fake 'NTC/Ncell' SIM-block SMS with a link","Scared the user into 'verifying' on a fake page","Persuasion + fear — no telecom system was breached"],
     ["'Bank head office' call asking for the OTP","Impersonated authority to extract the code","Targets the person's trust, not the bank's servers"],
     ["'IT helpdesk' asks a staffer to confirm a password","Used helpfulness + urgency to reset access","The human is the door; the network is untouched"],
     ["Fake eSewa 'account suspended' message","Rushed the victim to click and log in","Deception over a channel — the wallet wasn't hacked"],
     ["Caller uses your real name + branch (leaked list)","Manufactured legitimacy to lower your guard","Story-building, not code — sounds official"],
     ["'Daraz prize' claim asking for a 'fee'","Dangled a reward to get money/details","Greed lever — a con, not a technical exploit"]],
    per_page=6,widths=[2.6,2.6,2.7],fs=11,
    note="In every row the technology is untouched — the attacker persuaded a person. That is the signature of social engineering, and the reason awareness (not just software) is the defence.")

concept_understand("S33 · Concept 2 · [THEORY]","Why Attackers Use It (the need)","Social engineering is the path of LEAST resistance — cheaper, faster, and more reliable than defeating strong technical controls. Strong encryption and firewalls make direct attacks costly, so attackers pivot to the human.",
    ["Strong tech controls raise the cost of a direct attack — so the human becomes the cheap way in.",
     "High success rate, low cost, and hard to trace back to the attacker.",
     "No expensive tools needed — a phone and a convincing story can be enough.",
     "It scales: one message blasted to thousands needs only a few victims to pay off."],
    "s33_cost_success.png","Cheapest attack path: beat the person, not the encryption.",
    "~7 min. Frame with the quadrant: social engineering sits in 'low cost + high success'. That economics is exactly why it is so common — not because attackers can't hack machines, but because they don't need to.")
add_table_slide("S33 · Concept 2 · scaffolding","Why the human is the path of least resistance",
    ["Attack path","Cost / skill to the attacker","Success & traceability"],
    [["Breaking strong encryption","Very high — often infeasible","Low success; heavy effort wasted"],
     ["Finding a zero-day exploit","High — rare, expensive skill","Works, but costly and perishable"],
     ["Phoning a customer as 'bank security'","Very low — a phone + a script","High success; hard to trace"],
     ["Mass phishing SMS to thousands","Very low — one message, bulk send","A few victims still pays off"],
     ["Tricking a busy employee for a password","Low — a plausible story","Bypasses every technical control"]],
    per_page=5,widths=[2.6,2.5,2.7],fs=11,
    note="Attackers are economically rational: they pick the cheapest path with the highest payoff. When machines are hardened, that path runs straight through the person.")
concept_apply("S33 · Concept 2 · [THEORY]","Why Attackers Use It (the need)",
    "Instead of cracking a Nepali bank's systems — expensive, slow, and likely to fail — scammers simply phone customers pretending to be 'bank security'. It is far easier to fool a thousand customers than to breach one well-defended bank. The economics, not a lack of skill, is why the phone call beats the exploit.",
    "\"If the bank is secure, my money is safe.\" The bank's servers may be hardened, but YOU are the softer target. Attackers deliberately skip the strong wall and knock on the human door — so your own awareness is part of the bank's security, not separate from it.",
    "Attackers use social engineering because it is the path of least resistance: strong encryption and firewalls make direct attacks costly, so they pivot to the human, who is cheaper to fool. It offers high success, low cost, and is hard to trace, and it scales — one mass message needs only a few victims. It is chosen for economics, not for lack of technical skill.",
    "path of least resistance · low cost / high success · hard to trace · scales · economics of attack")

concept_understand("S33 · Concept 3 · [THEORY]","Why Humans Are the Weakest Link",
    "Humans are exploitable through predictable traits — helpfulness, obedience to authority, fear of consequences, curiosity, and trust in familiar brands — combined with low security awareness. Attackers don't break these traits; they USE them.",
    ["Helpfulness: we want to assist, so we comply with a reasonable-sounding request.",
     "Obedience to authority: a 'boss' or 'official' voice short-circuits our doubt.",
     "Fear & urgency: a threat ('account will be blocked') makes us act before thinking.",
     "Curiosity & trust in brands: a familiar logo or a 'you've won' message lowers the guard."],
    None,"Attackers don't break human traits — they exploit them.",
    "~8 min. Mini case: an office peon gets 'Sir, from IT — your email will be deleted today, just confirm your password.' It works on a busy, polite employee because helpfulness + authority + urgency all fire at once.")
add_table_slide("S33 · Concept 3 · concrete examples","Human trait → how it's exploited → how you defend",
    ["Human trait","How the attacker exploits it (Nepal)","Defence habit"],
    [["Helpfulness","'Just confirm your password so I can fix your email'","No one legitimate needs your password — refuse"],
     ["Obedience to authority","'I'm calling from the bank / the police'","Verify the identity via the official number yourself"],
     ["Fear of consequences","'A police case is filed unless you pay now'","Real authorities don't demand instant payment by phone"],
     ["Urgency / time pressure","'Your account blocks in 10 minutes'","Slow down — urgency is a red flag, not a reason"],
     ["Curiosity","'Open this to see who viewed your profile'","Don't open unexpected links/attachments"],
     ["Trust in familiar brands","Fake eSewa / Daraz logo and sender name","Check the real sender/URL; brands don't ask for OTP"]],
    per_page=6,widths=[1.9,3.0,2.6],fs=11,
    note="Each row is a normal, good human trait turned into an attack surface. Defence is not becoming rude or paranoid — it is a small verify-before-you-act habit for each trigger.")
concept_apply("S33 · Concept 3 · [THEORY]","Why Humans Are the Weakest Link",
    "A busy office employee gets a call: 'Sir, from the IT department — your email will be deleted today, just confirm your password.' It works because three levers fire together: authority (IT department), urgency (today), and helpfulness (the employee wants to cooperate). The strongest castle wall is useless if the gatekeeper opens the gate to anyone in the right uniform.",
    "\"Only careless or foolish people fall for scams.\" Smart, busy, polite people are exactly the target — the attack exploits normal good traits (helpfulness, respect for authority) under time pressure. Assuming 'it won't happen to me' is itself the vulnerability.",
    "Humans are the weakest link because attackers exploit predictable traits — helpfulness, obedience to authority, fear of consequences, curiosity, and trust in familiar brands — amplified by low awareness and time pressure. These are normal, positive human tendencies, so anyone can be targeted; the defence is a deliberate verify-before-acting habit for each trigger.",
    "weakest link · helpfulness · authority · fear/urgency · curiosity · brand trust · verify habit")

add_activity("S33 — 'Name the trick'  ·  ~5 min",
    ["In pairs (2 min): recall one suspicious call or SMS you or your family received (in Nepali).",
     "Write down the exact story it told and what it asked you to do.",
     "Name the human trait it was trying to exploit (helpfulness / authority / fear / curiosity / brand trust).",
     "Take 3–4 answers aloud (3 min); notice how often authority + urgency appear together."],
    "Seeds: NTC/Ncell SIM-block SMS, 'bank security' OTP call, Facebook/Daraz prize, eSewa 'account suspended'. Draw out that recognising the lever is the fastest early-warning sign — the goal is recognition, not any how-to.",
    "ACTIVITY [~5 min].")
add_quiz("S33 — Quick Check  ·  ~5 min",
    [("Q1.  Social engineering primarily attacks:","q"),
     ("a) firewalls   b) encryption   c) ✅ human psychology / people   d) hardware","a"),
     ("     Why: it manipulates a person into giving access — the technology is bypassed, not broken.","o"),
     ("Q2.  Attackers prefer social engineering mainly because it is:","q"),
     ("a) more technical   b) ✅ low-cost and high-success vs. beating strong tech controls   c) always legal   d) slower","a"),
     ("     Why: hardened machines make direct attacks costly, so the cheaper human path is chosen.","o"),
     ("Discussion: recall one suspicious call/SMS you or your family received — what trick was it using?","o")],
    "QUIZ [~5 min]. Reward students who name the specific lever (authority/urgency/fear) rather than just 'a scam'. Keep the tone defensive.")
add_summary("S33 · Summary  ·  [~2 min]",
    ["Social engineering = hacking PEOPLE, not machines — persuasion and deception over any channel.",
     "It's the cheapest, highest-success attack path, so attackers pivot to the human by choice.",
     "Humans are exploitable through helpfulness, authority, fear, curiosity, and brand trust — verify before you act."],
    "The most common way money is stolen from ordinary Nepalis online is not 'hacking' — it's a convincing phone call or message. Recognising this is your first and cheapest line of defence, for you and your family.",
    "S34 — the exact psychological levers attackers pull, and how the con is built.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S34
add_divider("Session 34 · Lecture hour 2 (of 5)","Implications · Building Trust · Exploiting the Relationship",
    "Why does a scammer spend 10 minutes being friendly before asking for anything? Because the ask only works after the trust. Today we reverse-engineer the manipulation — so you see it coming.",
    "OPENING HOOK [~5 min]. The psychology of the con, taught for DEFENCE. Agenda: what's really at stake → how trust is manufactured → how urgency and fear close the trap.")

concept_understand("S34 · Concept 1 · [THEORY]","Understanding the Implications",
    "A single successful manipulation rarely stays 'one account'. One leaked OTP or password can cascade into data loss, financial theft, identity theft, and reputational damage — because credentials are keys to a whole chain of linked accounts.",
    ["Credentials are keys, not doors: one unlocks email, which resets others.",
     "Email → bank → wallet → social accounts is a common chain reaction.",
     "The attacker then messages your contacts for more money, spreading the damage.",
     "Impact is delayed and wide — you often see it only after the chain has run."],
    "s34_chain.png","One leaked OTP is never 'just one account'.",
    "~7 min. Walk the chain: an OTP unlocks email; email resets the bank; the wallet balance goes; then the scammer poses as the victim to hit their contacts. Emphasise the cascade to counter the 'no big deal' reflex.")
add_table_slide("S34 · Concept 1 · scaffolding","One leaked credential — what it unlocks (the chain)",
    ["Step in the chain","What the attacker reaches","Why it cascades"],
    [["OTP / password shared","The first account (e.g. email)","The entry point to everything linked"],
     ["Email taken over","Password resets for other services","Most accounts recover via email"],
     ["Bank / eSewa / Khalti","Wallet balance & payment history","Direct financial theft"],
     ["Social accounts","Identity & the contact list","Enables the next round of scams"],
     ["Contacts messaged","Friends & family targeted next","Trust in YOUR name is now the weapon"]],
    per_page=5,widths=[2.1,2.7,2.6],fs=11,
    note="The damage is a chain, not a point. This is why 'it's just one OTP' is dangerous thinking — that one code is the first link that unlocks all the others.")
concept_apply("S34 · Concept 1 · [THEORY]","Understanding the Implications",
    "A victim who shares one OTP loses their eSewa / Khalti wallet balance — and then the attacker uses the hijacked account to message the victim's contacts asking for money, so the harm spreads to friends and family. What felt like 'one small code' became financial theft plus a reputational and social attack running through the victim's own name.",
    "\"It's just one password — no big deal.\" Credentials are keys to a whole chain of accounts: one leaked code can unlock email, then the bank, then social accounts, then your contacts. The impact is almost never limited to the single thing you first gave away.",
    "The implications of a single manipulation are rarely limited to one account: because credentials are keys to a chain of linked services, one leaked OTP or password can cascade into data loss, financial theft, identity theft, and reputational damage — and the attacker often exploits the victim's contacts next. The impact is wide and delayed, which is why every credential matters.",
    "chain reaction · credentials are keys · cascade · identity theft · reputational damage")

concept_understand("S34 · Concept 2 · [THEORY]","Building Trust — the levers",
    "Attackers manufacture trust using well-known influence principles (Cialdini-style) — authority, liking/rapport, social proof, and reciprocity. Taught here only to RECOGNISE them: the friendly, legitimate-sounding front is engineered, not genuine.",
    ["Authority: 'I'm from the bank / the police' — a title that short-circuits doubt.",
     "Liking / rapport: friendly small talk to make you comfortable before the ask.",
     "Social proof: 'everyone has already updated their KYC' — the herd nudge.",
     "Reciprocity: 'I've helped you fix this, now just confirm the code for me.'"],
    "s34_levers.png","Trust is manufactured — spot the lever behind the friendliness.",
    "~7 min. Present the six levers as a recognition tool, never a playbook. Point out attackers combine several at once (authority + social proof) and often use your real name/branch from a leaked list to sound legitimate.")
add_comparison_table("S34 · Concept 2 · comparison","The influence levers — recognise, don't use",
    ["Lever","How it sounds (Nepal)","The red flag it should raise"],
    [["Authority","'I'm calling from the bank / police / IT'","A title alone is not proof — verify independently"],
     ["Liking / rapport","Warm, friendly chat before any request","Unusual friendliness from a stranger who then asks"],
     ["Social proof","'Everyone has updated their KYC already'","'Everyone's doing it' is pressure, not a reason"],
     ["Reciprocity","'I helped you — now just confirm this code'","A small favour used to extract a bigger one"],
     ["Familiarity","Uses your real name, branch, or last digits","Scraped from a leaked list to fake legitimacy"],
     ["Consistency","'You already agreed, so just finish the step'","Manufactured momentum toward the real ask"]],
    per_page=6,widths=[1.7,2.8,2.8],fs=11,
    note="These are legitimate psychology principles turned into a con. You are learning them to DETECT them — the moment you can name the lever, its power drops.")
concept_apply("S34 · Concept 2 · [THEORY]","Building Trust — the levers",
    "A caller uses a real-sounding Nepali bank name, your actual branch, and your own name (scraped from a leaked customer list) to sound legitimate, then spoofs a sender name/logo that looks like the real institution. Every detail is engineered to manufacture trust — none of it proves who they are. The polished front is the attack, not evidence against it.",
    "\"If they know my name, my branch, and my bank, they must be genuine.\" That information is often scraped from leaked lists and is exactly how attackers manufacture legitimacy. Knowing your details proves nothing — always verify by contacting the institution through its official number yourself.",
    "Attackers build trust by exploiting influence principles — authority ('I'm from the bank'), liking/rapport, social proof ('everyone has updated their KYC'), and reciprocity ('I helped you, now help me') — often reinforced with your real name, branch, and spoofed logos scraped from leaked data. The trust is manufactured, so recognising the lever, not the friendly front, is the defence.",
    "authority · liking/rapport · social proof · reciprocity · spoofing · manufactured trust")

concept_understand("S34 · Concept 3 · [THEORY]","Exploiting the Relationship — the close",
    "Once trust exists, attackers add PRESSURE so the victim acts before thinking — urgency, fear, and scarcity. This is 'the close': the emotional squeeze that converts a friendly conversation into a harmful action.",
    ["Urgency: 'your account blocks in 10 minutes' — no time to verify.",
     "Fear: 'a police case has been filed against you' — panic overrides judgement.",
     "Scarcity: 'this lottery claim expires today' — act now or lose out.",
     "The friendly build-up is misdirection; the pressured ask is the actual trick."],
    "s34_cycle.png","Trust is the setup; urgency/fear is the close.",
    "~8 min. Mini case: a 'Facebook lottery' message — 'You've won Rs. 25 lakh, pay Rs. 5,000 processing fee to release it.' Have students name every trust + urgency + greed lever used. It's a magician's patter: friendly chatter, then the ask.")
add_table_slide("S34 · Concept 3 · concrete examples","Annotated scams — spot the levers and the close",
    ["Scam message (Nepal)","Levers used","The 'close' + safe response"],
    [["'You've won Rs. 25 lakh — pay Rs. 5,000 fee to release it'","Greed + authority + scarcity","Urgency to pay → never pay a fee to receive a 'prize'"],
     ["'Account blocks in 10 min — confirm your OTP now'","Authority + urgency","Time pressure → banks never ask for your OTP"],
     ["'Police case filed — settle immediately or be arrested'","Authority + fear","Threat of arrest → hang up, call the real police line"],
     ["'KYC expires today — verify on this link'","Social proof + urgency","Deadline → visit the bank/app directly, not the link"],
     ["'Parcel held at customs — pay Rs. 200 here'","Curiosity + urgency","Small ask → verify with the courier's official number"],
     ["'I'm your boss's assistant — approve this transfer fast'","Authority + rapport","Rushed approval → confirm with the boss on a known number"]],
    per_page=6,widths=[3.0,1.9,2.6],fs=11,
    note="In every case the emotion (greed, fear, urgency) is the tell. Naming the lever and refusing to be rushed is the single fastest way to defuse the close.")
concept_apply("S34 · Concept 3 · [THEORY]","Exploiting the Relationship — the close",
    "A 'Facebook lottery' message says: 'You've won Rs. 25 lakh — pay Rs. 5,000 processing fee to release it.' It stacks levers: authority (an official-looking win), greed (a huge prize), and scarcity/urgency ('claim expires today'). The friendly, exciting build-up is misdirection; the pressured 'pay the fee now' is the trick. Spotting the emotion it triggers stops it cold.",
    "\"A real urgent message means I must act immediately.\" Manufactured urgency is the attacker's main weapon — it exists precisely to stop you verifying. The correct response to pressure is to slow down: a genuine institution will not punish you for taking time to confirm through official channels.",
    "After building trust, attackers exploit the relationship by adding pressure — urgency ('blocks in 10 minutes'), fear ('a police case is filed'), and scarcity ('claim expires today') — so the victim acts before thinking. The friendly build-up is misdirection and the pressured ask is the close, so recognising the emotion a message is trying to trigger is the fastest way to catch the scam.",
    "the close · urgency · fear · scarcity · misdirection · spot the emotion")

add_activity("S34 — 'Which lever?'  ·  ~5 min",
    ["In pairs (2 min): take a scam call your aunt/uncle actually got (or a message above).",
     "Identify the trust-building tactic first (authority, liking, or social proof).",
     "Then identify the 'close' — the urgency, fear, or scarcity that pushed for action.",
     "Take 3–4 answers aloud (3 min); confirm the pattern: build trust, then squeeze."],
    "Draw out the two-phase structure: manufacture trust, then apply pressure. The strongest answers separate the trust phase from the close, and name the emotion each lever targets. Recognition only — no how-to.",
    "ACTIVITY [~5 min].")
add_quiz("S34 — Quick Check  ·  ~5 min",
    [("Q1.  'I'm calling from the police, act now or face arrest' combines:","q"),
     ("a) liking + scarcity   b) ✅ authority + fear/urgency   c) reciprocity only   d) social proof","a"),
     ("     Why: a title (authority) plus a threat that demands instant action (fear/urgency).","o"),
     ("Q2.  Why is leaking a single OTP serious?","q"),
     ("a) it isn't   b) ✅ it can unlock a chain of linked accounts   c) only if it's a bank OTP   d) it expires","a"),
     ("     Why: credentials are keys — one unlocks email, then bank, wallet, social, and your contacts.","o"),
     ("Discussion: in a scam call your family got, which trust tactic was used — authority, liking, or social proof?","o")],
    "QUIZ [~5 min]. Reward answers that separate the trust-building lever from the urgency/fear close. Emphasise: naming the emotion is the defence.")
add_summary("S34 · Summary  ·  [~2 min]",
    ["Impact chains far beyond one account — one leaked OTP can unlock email, bank, wallet, and your contacts.",
     "Attackers manufacture trust via authority, liking/rapport, social proof, and reciprocity — the friendly front is engineered.",
     "They exploit it with urgency, fear, and scarcity — the 'close' that makes you act before verifying."],
    "Spotting the EMOTION a message is trying to trigger — fear, greed, urgency — is the single fastest way to catch a scam before you react. The pause to name the lever is your protection.",
    "S35 — the named attack types, how to recognise each, and how to defend against them.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S35
add_divider("Session 35 · Lecture hour 3 (of 5)","Attack Types (Recognition) · Countermeasures & Prevention",
    "Phishing, vishing, smishing, pretexting, baiting, tailgating — six names, one goal: make YOU the door. Today you learn to recognise all six in the wild, and how to shut the door. Recognition only — no instructions to carry them out.",
    "OPENING HOOK [~5 min]. A field guide to spotting attacks, strictly defensive. Agenda: the six attack types (recognise) → organizational + technical countermeasures → personal prevention habits.")

concept_understand("S35 · Concept 1 · [THEORY]","The Major Attack Types (recognise them)",
    "The same con appears across channels under different names. You learn to RECOGNISE each — never to run it. Phishing (email), vishing (voice call), smishing (SMS), pretexting (invented backstory), baiting (a tempting lure), and tailgating (physical door-following).",
    ["Digital channels: phishing (email), smishing (SMS), vishing (a call) — same trick, different pipe.",
     "Human/physical: pretexting (a fake role/story), baiting (a 'free' download or dropped USB).",
     "Tailgating: following an authorised person through a secured door.",
     "Recognition cues repeat: mismatched URLs, urgent threats, requests for OTP/PIN, generic greetings."],
    "s35_taxonomy.png","Six names, one con — recognise the channel, refuse the ask.",
    "~8 min. Bust the 'phishing = only email' myth: it spans SMS, calls, QR codes, and social media. Keep every description at the recognition level — what a victim sees — with zero operational detail.")
add_comparison_table("S35 · Concept 1 · comparison","The six attack types — channel, recognition cue, example",
    ["Type","Channel","How you recognise it (Nepal example)"],
    [["Phishing","Email","Fake 'bank/college' email + link; mismatched URL, generic greeting"],
     ["Vishing","Voice call","'Bank officer' pressuring you to share the OTP/PIN just sent"],
     ["Smishing","SMS","'eSewa/bank suspended — click here'; 'Daraz prize'; 'parcel fee'"],
     ["Pretexting","Any (a story)","'I'm the new auditor / your boss's assistant' invented role"],
     ["Baiting","Download / USB","A 'free' movie/app, or a USB left in the canteen/parking"],
     ["Tailgating","Physical door","A stranger following staff through a secure door 'hands full'"]],
    per_page=6,widths=[1.5,1.6,3.9],fs=11,
    note="Phishing is NOT only email — smishing, vishing, QR codes, and social media all carry the same con. Recognising the channel plus the tell (urgency, a link, an OTP request) is enough to refuse.")
concept_apply("S35 · Concept 1 · [THEORY]","The Major Attack Types (recognise them)",
    "In Nepal right now: fake 'Nepal lottery / Daraz prize' SMS (smishing), a 'bank officer' call asking for the OTP just sent to you (vishing), and globally, package-delivery smishing waves and CEO-impersonation ('business email compromise') asking finance to wire money. Different names, one goal — make a person the door. Naming the type lets you instantly classify and reject it.",
    "\"Phishing only happens over email.\" It spans SMS (smishing), calls (vishing), QR codes, and social media. Guarding only your inbox leaves every other channel open — the con simply switches pipes to whichever one you trust more.",
    "The major social-engineering attack types are phishing (email), vishing (voice call), smishing (SMS), pretexting (an invented backstory), baiting (a tempting lure such as a 'free' download or dropped USB), and tailgating (following someone through a secure door). They share one goal — make the person the door — and recognisable tells (urgency, links, OTP requests), so classifying the type is the first step to rejecting it.",
    "phishing · vishing · smishing · pretexting · baiting · tailgating · same con, different channel")
add_examples_table("S35 · Concept 1 · concrete examples","Red flag → defence (the §7A field guide)",
    ["Attack (technique)","Red flag to spot","Defence / safe response","If you fall for it (consequence)"],
    [["Vishing — 'bank' OTP call","Anyone asking you to read out an OTP/PIN","Hang up; call the bank's official number yourself","Wallet/account drained within minutes"],
     ["Smishing — 'account suspended' SMS","A link + urgency in a text you didn't expect","Don't click; open the app/site directly","Credentials phished on a fake login page"],
     ["Phishing — fake bank/college email","Mismatched URL, generic 'Dear customer'","Hover the link; verify via official channel","Login stolen; inbox used to reset other accounts"],
     ["Baiting — 'free' download / dropped USB","Something too tempting or conveniently 'found'","Don't plug in / don't download; report it","Malware installed on your device or network"],
     ["Pretexting — 'new auditor' call","A stranger with a story wanting info/access","Verify the role with a known internal contact","Sensitive data handed to an outsider"],
     ["Tailgating — door-following","Someone without a badge following you in","Don't hold the door; direct them to reception","An intruder gains physical access to the office"]],
    per_page=6,widths=[2.2,2.6,2.8,2.4],fs=10,
    note="This is the core recognition table: spot the red flag, apply the defence, and note the consequence of NOT doing so. Every defence is a refusal or a verify — never an instruction to attack.")

concept_understand("S35 · Concept 2 · [THEORY]","Countermeasures — organizational + technical",
    "Defence is layered — combining people, process, and technology. No single control stops social engineering; they work together so a slip at one layer is caught by another.",
    ["People: security-awareness training and simulated-phishing drills.",
     "Process: verify-via-callback policy, least-privilege access, visitor badges & escort rules.",
     "Technology: MFA, email filtering, anti-spoofing (SPF/DKIM/DMARC — named at awareness level).",
     "Policy anchor: a bank publicly stating 'we will NEVER ask for your OTP/PIN'."],
    None,"People + process + technology — layered, because one control is never enough.",
    "~7 min. Keep MFA/SPF/DKIM/DMARC at the awareness level — students should know these exist and what they achieve, not configure them. The strongest cultural control is the 'we never ask for your OTP' rule.")
add_table_slide("S35 · Concept 2 · scaffolding","Countermeasures by layer — and what each stops",
    ["Layer","Measure","What it stops"],
    [["People","Awareness training + simulated-phishing drills","Staff recognise and report the lure"],
     ["Process","Verify-via-callback before acting on a request","Impersonation calls fail the check"],
     ["Process","Least-privilege access","A fooled account can reach less"],
     ["Process","Visitor badges & escort policy","Tailgating into secure areas"],
     ["Technology","Multi-factor authentication (MFA)","A stolen password alone can't log in"],
     ["Technology","Email filtering + anti-spoofing (SPF/DKIM/DMARC)","Many phishing/spoofed emails never arrive"]],
    per_page=6,widths=[1.5,3.1,2.4],fs=11,
    note="Defence-in-depth: each layer catches what the previous one missed. MFA, for example, means even a successfully phished password is not enough on its own.")
concept_apply("S35 · Concept 2 · [THEORY]","Countermeasures — organizational + technical",
    "A Nepali bank runs regular staff awareness sessions and simulated-phishing drills, enforces a verify-via-callback rule for sensitive requests, turns on MFA, and repeats one public message to customers: 'we will NEVER ask for your OTP/PIN.' No single measure is decisive; together they mean a slip at one layer is caught at another.",
    "\"We have MFA / a spam filter, so we're safe.\" One control is never enough — attackers adapt, and social engineering targets people, not just technology. Real defence layers people (training), process (callback, least privilege), and technology (MFA, filtering) so no single failure is fatal.",
    "Social-engineering countermeasures are layered across people, process, and technology: security-awareness training and simulated-phishing drills; verify-via-callback policies, least-privilege access, and visitor/escort rules; and MFA, email filtering, and anti-spoofing (SPF/DKIM/DMARC). Because no single control is enough, defence-in-depth ensures a slip at one layer is caught at another — anchored by the rule that a bank will never ask for your OTP.",
    "defence-in-depth · awareness training · verify-via-callback · least privilege · MFA · anti-spoofing")

concept_understand("S35 · Concept 3 · [THEORY]","Preventing Attacks — personal habits",
    "Personal prevention is a small set of habits that defeats most attacks: never share OTP/PIN/password; verify by calling the official number yourself; check links before clicking; slow down when rushed; and report suspicious messages.",
    ["Never share an OTP/PIN/password — with anyone, even 'the bank'.",
     "Verify independently: call the official number YOU look up, not the one you were given.",
     "Hover/check links and sender addresses before you act.",
     "Slow down when a message pushes urgency — and report it so others are warned."],
    "s35_stop_think_click.png","STOP · THINK · then CLICK — the pause is the protection.",
    "~8 min. Mini case: an SMS 'parcel held at customs, pay Rs. 200 here.' Walk the safe response — don't click, verify with the courier directly. Analogy: like looking both ways before crossing a road, the pause is the protection.")
add_examples_table("S35 · Concept 3 · concrete examples","Scam scenario → wrong reaction → safe response",
    ["Scenario (Nepal)","The wrong (unsafe) reaction","The safe response"],
    [["'Parcel held at customs — pay Rs. 200 here'","Click the link and pay to release it","Don't click; contact the courier's official number"],
     ["'Bank security' asks for the OTP just sent","Read out the code to 'confirm identity'","Refuse — banks never ask; hang up and call them"],
     ["'You won a prize — pay a small fee'","Pay the fee to claim the winnings","Ignore — real prizes never require an upfront fee"],
     ["Email: 'reset your password here now'","Click the in-email link and log in","Go to the site directly and check your account"],
     ["A found USB / 'free movie' download","Plug it in / download to see what it is","Don't; hand a found USB to IT, avoid the download"],
     ["'Your KYC expires today — verify now'","Rush to submit details on the link","Visit the branch or official app on your own"]],
    per_page=6,widths=[2.7,2.6,2.7],fs=11,
    note="The pattern is always the same: refuse, then verify independently. 'STOP, THINK, then CLICK' — the deliberate pause defeats the urgency the attacker depends on.")
concept_apply("S35 · Concept 3 · [THEORY]","Preventing Attacks — personal habits",
    "You get an SMS: 'parcel held at customs, pay Rs. 200 here.' The safe response: don't click the link, and verify directly with the courier's official number. Banks and wallets (eSewa, Khalti, NIC ASIA) repeatedly warn that they will never ask for your OTP — so any such request, however official it sounds, is the scam identifying itself.",
    "\"If a message looks official, it's safe to act on it.\" Logos, names, and official tone are trivial to fake. The safe habit ignores how it looks and instead verifies through a channel you control — the official number or app — before doing anything, especially anything urgent.",
    "Personal prevention rests on a few reliable habits: never share your OTP/PIN/password with anyone; verify independently by calling the official number you look up yourself; check links and senders before clicking; slow down whenever a message pushes urgency; and report suspicious messages. Captured as 'STOP, THINK, then CLICK', the deliberate pause defeats the urgency attacks depend on.",
    "never share OTP · verify independently · check links · slow down · report · STOP-THINK-CLICK")

add_activity("S35 — 'Spot the phish'  ·  ~5 min",
    ["In pairs (2 min): take the 'parcel held at customs, pay Rs. 200' SMS.",
     "List every red flag you can find (link, urgency, small fee, unexpected).",
     "Write the safe response step by step (don't click → verify with the courier directly).",
     "Take 3–4 answers aloud (3 min); which of the six attack types is it, and why?"],
    "It's smishing. Reward listing concrete red flags and a verify-first response. Discussion seed: which of the six types do you think is most common in Nepal now, and why? Keep it recognition + defence only.",
    "ACTIVITY [~5 min].")
add_quiz("S35 — Quick Check  ·  ~5 min",
    [("Q1.  A fraudulent phone call asking for your OTP is an example of:","q"),
     ("a) phishing   b) smishing   c) ✅ vishing   d) baiting","a"),
     ("     Why: vishing = voice; the OTP request over a call is the giveaway.","o"),
     ("Q2.  The single best rule against OTP fraud is:","q"),
     ("a) share it only with the bank   b) ✅ never share your OTP with anyone, even 'the bank'   c) share it if urgent   d) email it","a"),
     ("     Why: legitimate banks never ask for your OTP, so any such request is a scam.","o"),
     ("Discussion: which of the six attack types do you think is most common in Nepal right now, and why?","o")],
    "QUIZ [~5 min]. Reinforce the 'never share OTP' rule and channel-matching (call=vishing, SMS=smishing, email=phishing). Recognition and defence only.")
add_summary("S35 · Summary  ·  [~2 min]",
    ["Six recognisable attack types across channels: phishing, vishing, smishing, pretexting, baiting, tailgating.",
     "Countermeasures are layered — people (training), process (callback, least privilege), technology (MFA, filtering).",
     "Personal rule: verify independently, never share your OTP, slow down — STOP, THINK, then CLICK."],
    "Banks and wallets (eSewa, Khalti, NIC ASIA) repeatedly warn they will never ask for an OTP — knowing the attack names lets you instantly classify and reject the scam instead of freezing.",
    "S36 — when manipulation scales up to attacks on a whole nation: cyber terrorism.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S36
add_divider("Session 36 · Lecture hour 4 (of 5)","Cyber Terrorism · Types of Cyber Terrorism",
    "A teenager defacing a website for fun, an activist protesting online, and a group trying to shut down a country's power grid — all use computers, but only one is cyber terrorism. Where's the line?",
    "OPENING HOOK [~5 min]. Defining the term precisely and responsibly. Agenda: what cyber terrorism is → distinguishing it from crime/hacktivism/warfare → its types. Kept conceptual — no operational content.")

concept_understand("S36 · Concept 1 · [THEORY]","What Is Cyber Terrorism",
    "Cyber terrorism = the politically or ideologically motivated use of computers/networks to cause serious harm, fear, or disruption — especially to critical systems or the public. Three ingredients define it: intent, target, and severity.",
    ["Intent: political or ideological motivation — not profit.",
     "Target: often critical infrastructure or the public's sense of safety.",
     "Severity: real-world harm or genuine terror, not mere nuisance.",
     "All three together are what separate it from ordinary hacking or vandalism."],
    None,"Cyber terrorism = ideological INTENT + serious harm/fear, often vs. infrastructure.",
    "~7 min. Keep this conceptual and responsible. The awareness-level local example: defacement of Nepali government websites/public-service portals during regional tensions, used to spread fear or embarrassment. No methods discussed.")
add_table_slide("S36 · Concept 1 · scaffolding","The three ingredients of cyber terrorism",
    ["Ingredient","What it means","Why it matters"],
    [["Intent","Political / ideological motive (not money)","Separates terrorism from profit-driven crime"],
     ["Target","Critical systems or the public's safety","The aim is society-wide impact, not one victim"],
     ["Severity","Serious harm, fear, or disruption","Nuisance/vandalism alone doesn't qualify"],
     ["The public effect","Spreading terror or coercion","The 'terror' in cyber terrorism — fear is the goal"]],
    per_page=4,widths=[1.6,3.0,2.7],fs=11.5,
    note="Only when intent + target + severity line up do you have cyber terrorism. Missing the ideological intent makes it crime; missing the severity makes it vandalism.")
concept_apply("S36 · Concept 1 · [THEORY]","What Is Cyber Terrorism",
    "At an awareness level: defacement of Nepali government websites and attacks on public-service portals during periods of regional tension have been used to spread fear and embarrassment. Globally, attacks aimed at power grids and industrial control systems are intended to cause physical disruption. In each, the motive is ideological and the target is public — the signature of cyber terrorism, not ordinary crime.",
    "\"Any hacking is cyber terrorism.\" Most hacking is crime (for profit) or vandalism. Terrorism requires political/ideological intent PLUS an intent to terrorise or seriously harm — mislabelling a prank or a profit scam as 'terrorism' distorts both the threat and the correct response.",
    "Cyber terrorism is the politically or ideologically motivated use of computers or networks to cause serious harm, fear, or disruption — especially to critical infrastructure or the public. It is defined by three ingredients together: intent (political/ideological, not profit), target (critical systems or public safety), and severity (real harm or terror). All three are needed, which is what separates it from ordinary hacking.",
    "cyber terrorism · political/ideological intent · critical infrastructure · fear · intent + target + severity")

concept_understand("S36 · Concept 2 · [THEORY]","Distinguishing Related Terms",
    "Cybercrime, hacktivism, cyber warfare, and cyber terrorism overlap but are distinct — separated mainly by MOTIVE and ACTOR. Labelling an incident correctly changes the legal and response path entirely.",
    ["Cybercrime: motive is profit (e.g. a ransomware gang for money).",
     "Hacktivism: motive is protest or a message (e.g. a defacement to make a point).",
     "Cyber warfare: state-versus-state action as part of conflict.",
     "Cyber terrorism: ideological motive aiming to terrorise or seriously harm."],
    "s36_intent_target.png","Sort by motive: profit / protest / state-conflict / terror.",
    "~8 min. Mini case: classify three events — a ransomware gang for money, a protest-driven defacement, and an attempt to disable a national grid — into the right bucket. The exercise is classification, not method.")
add_comparison_table("S36 · Concept 2 · comparison","Cybercrime vs hacktivism vs cyber warfare vs cyber terrorism",
    ["Term","Primary motive","Typical actor","Example (awareness)"],
    [["Cybercrime","Profit / money","Criminals, fraud gangs","Ransomware gang; OTP/eSewa scams"],
     ["Hacktivism","Protest / a message","Activists","Website defacement to make a point"],
     ["Cyber warfare","State conflict","Nation-states","State-vs-state attacks in a conflict"],
     ["Cyber terrorism","Ideology + terror/harm","Ideologically driven groups","Attempt to disable a national grid to cause fear"],
     ["(shared trait)","All use computers","Overlapping tools","The tool is not what distinguishes them"]],
    per_page=5,widths=[1.7,2.0,1.9,3.0],fs=11,
    note="They share tools, so the tool never decides the label — MOTIVE and ACTOR do. Getting the label right changes the legal route and who responds (police vs national security).")
concept_apply("S36 · Concept 2 · [THEORY]","Distinguishing Related Terms",
    "Classify three events: a ransomware gang encrypting a company's files for money is cybercrime; a protest-driven defacement of a website carrying a political slogan is hacktivism; an attempt to disable a national power grid to spread fear is cyber terrorism (or cyber warfare if state-driven). Same tools, very different labels — because motive and actor, not the technology, decide.",
    "\"If it's illegal and uses a computer, it's cyber terrorism.\" Illegality and computers are common to all four categories. The distinguishing factors are motive (profit vs protest vs state conflict vs ideology-and-terror) and actor — which is exactly why careful classification matters.",
    "Cybercrime (profit), hacktivism (protest/message), cyber warfare (state-vs-state), and cyber terrorism (ideology plus intent to terrorise or seriously harm) overlap in tools but differ in motive and actor. Because they share technology, the tool never decides the label; motive and actor do. Correct classification is essential because it changes the legal and response path — police, regulator, or national security.",
    "cybercrime · hacktivism · cyber warfare · cyber terrorism · motive & actor decide · correct labelling")

concept_understand("S36 · Concept 3 · [THEORY]","Types of Cyber Terrorism",
    "Common categories used for AWARENESS: (a) attacks on critical infrastructure, (b) data destruction/manipulation of public records, (c) disruption/denial of essential services, (d) propaganda, recruitment & psychological operations / disinformation, and (e) financing via cyber means.",
    ["Critical-infrastructure attacks: power, water, telecom, finance, aviation.",
     "Data destruction / manipulation: corrupting or wiping public records.",
     "Service denial: large-scale disruption of services people depend on.",
     "Propaganda / psy-ops & financing: spreading fear, recruiting, and funding operations online."],
    "s36_types.png","Types span infrastructure, data, service-denial, propaganda, and financing.",
    "~8 min. Local awareness example: disinformation campaigns on social media during sensitive national events; threats to telecom/banking continuity in South Asia. Analogy: 'arson with a keyboard' — the goal is fear and damage, not theft.")
add_examples_table("S36 · Concept 3 · concrete examples","Types of cyber terrorism — example and intended effect",
    ["Type","Example (awareness level)","Intended effect"],
    [["Critical-infrastructure attack","Targeting power/water/telecom/finance/aviation","Physical disruption and public fear"],
     ["Data destruction / manipulation","Corrupting or wiping public records","Erode trust; damage governance"],
     ["Service denial (large-scale)","Disrupting essential online services","Freeze daily life and commerce"],
     ["Propaganda & psy-ops","Disinformation during sensitive national events","Spread fear, divide, and recruit"],
     ["Recruitment / radicalisation","Online content to recruit and radicalise","Grow the movement, normalise harm"],
     ["Financing via cyber means","Moving/raising funds online for operations","Fund and sustain the campaign"]],
    per_page=6,widths=[2.2,3.0,2.6],fs=11,
    note="These are awareness categories, not a manual — each names WHAT is targeted and WHY, so you can recognise and correctly report it. The common thread is fear and damage, not profit.")
concept_apply("S36 · Concept 3 · [THEORY]","Types of Cyber Terrorism",
    "In South Asia, awareness-level concerns include disinformation campaigns on social media during sensitive national events (propaganda/psy-ops) and threats to telecom and banking continuity (service denial / critical-infrastructure risk). Cyber terrorism is 'arson with a keyboard' — the aim is not to steal, but to cause fear and damage, whether to systems or to the public mind.",
    "\"Cyber terrorism only means blowing up power plants.\" Its types are broader — data destruction, large-scale service denial, and especially propaganda and disinformation that attack the public's mind. An information campaign that spreads fear can be as much a part of it as an infrastructure strike.",
    "The common types of cyber terrorism, used for awareness, are: attacks on critical infrastructure (power, water, telecom, finance, aviation); data destruction or manipulation of public records; disruption or denial of essential services; propaganda, recruitment, and psychological operations / disinformation; and financing via cyber means. All share the aim of fear and damage rather than profit — 'arson with a keyboard'.",
    "critical infrastructure · data destruction · service denial · propaganda/psy-ops · financing · fear not profit")

add_activity("S36 — 'Crime, hacktivism, or terrorism?'  ·  ~5 min",
    ["In pairs (2 min): take a website defacement of a government portal.",
     "Classify it using the three ingredients: intent, target, and severity.",
     "Decide — cybercrime, hacktivism, or cyber terrorism — and defend your choice.",
     "Take 3–4 answers aloud (3 min); note how motive and severity swing the label."],
    "There's no single 'right' label — reward reasoning with intent/target/severity. A pure protest message leans hacktivism; an ideological attempt to terrorise leans terrorism. The skill is correct classification, which sets the legal/response path.",
    "ACTIVITY [~5 min].")
add_quiz("S36 — Quick Check  ·  ~5 min",
    [("Q1.  What most distinguishes cyber terrorism from ordinary cybercrime?","q"),
     ("a) it uses a computer   b) it is illegal   c) ✅ political/ideological intent to cause fear or serious harm   d) it is online","a"),
     ("     Why: crime is profit-driven; terrorism adds ideological motive plus intent to terrorise/harm.","o"),
     ("Q2.  Spreading propaganda and disinformation to recruit and instill fear is which type?","q"),
     ("a) baiting   b) ✅ psychological operations / propaganda   c) phishing   d) ransomware","a"),
     ("     Why: psy-ops/propaganda targets the public mind — a recognised type of cyber terrorism.","o"),
     ("Discussion: is a defacement of a government portal cybercrime, hacktivism, or cyber terrorism? Defend it.","o")],
    "QUIZ [~5 min]. Reward correct use of intent/target/severity. Keep the discussion analytical and responsible — no methods, only classification.")
add_summary("S36 · Summary  ·  [~2 min]",
    ["Cyber terrorism = ideological/political INTENT + serious harm or fear, often aimed at critical infrastructure.",
     "It's distinct from cybercrime (profit), hacktivism (protest), and cyber warfare (state-vs-state) — motive & actor decide.",
     "Its types span infrastructure attacks, data destruction, service denial, propaganda/psy-ops, and financing."],
    "As future IT/business professionals you'll need to correctly LABEL incidents — mislabelling vandalism as 'terrorism' (or vice versa) changes the legal and response path entirely.",
    "S37 — what it does to real infrastructure, and how nations, organizations, and citizens counter it.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S37
add_divider("Session 37 · Lecture hour 5 (of 5) — CLOSES UNIT 7","Effects on Infrastructure · Countering Cyber Terrorism",
    "Imagine Kathmandu's power, the banking network, and mobile service all going dark for two days — no ATMs, no eSewa, no calls. Cyber terrorism's real damage isn't on a screen; it's in the streets.",
    "OPENING HOOK [~5 min]. Why critical infrastructure is the prize, and how we defend it. Agenda: cascading effects on infrastructure → layered countering (national/organizational/personal) → resilience & preparedness.")

concept_understand("S37 · Concept 1 · [THEORY]","Effects on Critical Infrastructure",
    "Critical infrastructure (CI) = the systems a society can't function without. An attack rarely stays contained: cascading (domino) effects spread from one system to the next, causing public panic and economic loss well beyond the first target.",
    ["Cascade: a power outage takes telecom down, which hits banking, hospitals, and water.",
     "The damage is physical and economic, not merely 'digital'.",
     "Dependence concentrates risk: a few telecom operators and wallets carry the whole economy.",
     "Attacks on government data centres also put citizens' records at risk."],
    "s37_cascade.png","CI attacks cascade — power → telecom → banking → hospitals → panic.",
    "~7 min. Local framing: Nepal's dependence on a few telecom operators and on eSewa/Khalti/connectIPS means an attack on national payment or telecom infrastructure could freeze daily commerce. Keep it about EFFECTS and resilience, not methods.")
add_examples_table("S37 · Concept 1 · concrete examples","Infrastructure attacked → cascade → real-world effect",
    ["If this is hit (Nepal)","The cascade it triggers","Real-world effect on people"],
    [["National power / load-dispatch","Telecom & data centres lose power","Blackout; comms and services go dark"],
     ["Telecom operators","Internet, calls, and OTP delivery fail","Wallets and banking become unusable"],
     ["Payment infra (eSewa/Khalti/connectIPS)","Digital commerce halts","Shops, salaries, remittances freeze"],
     ["Banking network","ATMs and transfers stop","People can't access their own money"],
     ["Government data centre","Citizen records exposed/altered","Identity risk; loss of trust in e-gov"],
     ["Aviation / hospital systems","Safety-critical operations disrupted","Direct risk to travel and to life"]],
    per_page=6,widths=[2.4,2.7,2.7],fs=11,
    note="The lesson is the CASCADE: one failure topples dependent systems. This is why CI protection matters far more than the size of any single target suggests.")
concept_apply("S37 · Concept 1 · [THEORY]","Effects on Critical Infrastructure",
    "Nepal's dependence on a few telecom operators and on digital wallets (eSewa, Khalti, connectIPS) means an attack on national payment or telecom infrastructure could freeze daily commerce — no OTPs, no transfers, no ATMs — while an attack on government data centres risks citizens' records. Globally, attacks on energy/utility control systems have caused regional blackouts. The harm lands in the streets, not just on a screen.",
    "\"Cyber attacks only cause online / digital damage.\" Attacks on industrial and control systems can cause physical, economic, and human harm — blackouts, frozen commerce, and risk to hospitals. The 'cyber' part is only the entry point; the damage is very much in the physical world.",
    "Cyber terrorism's effect on critical infrastructure is dangerous because of cascading (domino) effects: an attack on one system — power, telecom, payments, banking, or a government data centre — spreads to the systems that depend on it, causing public panic and economic loss. In Nepal, heavy dependence on a few telecom operators and digital wallets concentrates this risk, and the harm is physical and economic, not merely digital.",
    "critical infrastructure · cascading effects · physical & economic harm · concentrated dependence · not just digital")

concept_understand("S37 · Concept 2 · [THEORY]","Countering It — a layered defence",
    "Countering cyber terrorism is coordinated across three levels — national, organizational, and personal. No single level is sufficient; the base, the middle, and the top must all hold.",
    ["National: CERT/incident-response teams, CI-protection policy, intelligence sharing, legal frameworks, international cooperation.",
     "Organizational: network segmentation, monitoring/intrusion detection, incident-response & business-continuity/DR plans, drills, backups.",
     "Personal/citizen: awareness, reporting suspicious activity, and NOT amplifying disinformation or panic.",
     "Nepal's layer: NPCERT and government IT-security efforts, with cyber law (ties forward to Unit 9)."],
    "s37_defense_pyramid.png","Three layers — national + organizational + personal — all must hold.",
    "~8 min. Nepal specifics: NPCERT (national CERT), the Electronic Transaction Act's role in prosecution (forward link to Unit 9), and coordination among NRB, telecoms, and agencies. Citizens counter it partly by not amplifying disinformation.")
add_table_slide("S37 · Concept 2 · scaffolding","Countering cyber terrorism — by layer",
    ["Layer","Key measures","Nepal example"],
    [["National","CERT, CI-protection policy, intelligence sharing, cyber law, intl cooperation","NPCERT; the Electronic Transaction Act (Unit 9)"],
     ["National","Cross-agency coordination","NRB, telecoms, and government agencies together"],
     ["Organizational","Segmentation, monitoring/IDS, backups","Banks isolating and monitoring core systems"],
     ["Organizational","Incident-response + BCP/DR plans, drills","Tested continuity plans and regular rehearsals"],
     ["Personal / citizen","Awareness; report suspicious activity","Reporting scams/phishing to the bank/CERT"],
     ["Personal / citizen","Don't amplify disinformation/panic","Verifying before resharing during a crisis"]],
    per_page=6,widths=[1.7,3.1,2.4],fs=11,
    note="Defence is a stack: the national base (CERT, law), the organizational middle (segmentation, IR/BCP), and the personal tip (awareness, don't amplify). A gap at any level weakens the whole.")
concept_apply("S37 · Concept 2 · [THEORY]","Countering It — a layered defence",
    "In Nepal, NPCERT and government IT-security efforts sit at the national layer; cyber law (the Electronic Transaction Act — Unit 9) enables prosecution; and NRB, telecoms, and agencies coordinate response. Organizations add segmentation, monitoring, and tested incident-response/business-continuity plans, while citizens report suspicious activity and refuse to amplify disinformation. Each layer covers what the others can't.",
    "\"Cyber terrorism is only the government's problem.\" Defence needs all three layers — national policy and CERTs, organizational plans and monitoring, AND individual citizens who report suspicious activity and don't spread panic or disinformation. Leaving it entirely to 'the government' removes two of the three defensive layers.",
    "Countering cyber terrorism is layered across national, organizational, and personal levels: nationally, CERTs (NPCERT), critical-infrastructure protection, intelligence sharing, legal frameworks (the Electronic Transaction Act), and international cooperation; organizationally, segmentation, monitoring/IDS, incident-response and business-continuity/DR plans, drills, and backups; personally, awareness, reporting suspicious activity, and not amplifying disinformation. No single level is sufficient.",
    "national/CERT/NPCERT · organizational IR & BCP · personal awareness · cyber law · layered defence")

concept_understand("S37 · Concept 3 · [THEORY]","Resilience & Preparedness",
    "Resilience means ASSUMING attacks will happen and building the ability to keep operating and recover fast. Preparedness — backups, failover, tested plans, and coordination — decides whether an incident is a scare or a catastrophe.",
    ["Assume breach: plan for 'when', not 'if'.",
     "Continuity: backups and failover keep essential services running.",
     "Response: a tested incident-response plan and clear communication limit damage.",
     "Coordination: working with a CERT and partners speeds recovery."],
    "s37_ir_flow.png","Prepare → detect → contain → eradicate → recover → review.",
    "~8 min. Mini case: a national bank suffers a service-disrupting attack — walk the continuity steps (backups, failover, public communication, coordination with CERT). Analogy: like earthquake preparedness in Nepal — drills and a plan decide scare vs. catastrophe.")
add_examples_table("S37 · Concept 3 · concrete examples","A bank under a disruptive attack — resilience steps in order",
    ["Incident-response step","What the bank does","Why it limits the damage"],
    [["Prepare (before)","Backups, tested BCP/DR, staff drills","Ready to act — no improvising mid-crisis"],
     ["Detect","Monitoring/IDS flags the disruption","Faster detection means less spread"],
     ["Contain","Isolate affected systems; fail over","Stops the cascade to other services"],
     ["Eradicate","Remove the threat from the network","Prevents re-infection on recovery"],
     ["Recover","Restore service from clean backups","Gets customers back online safely"],
     ["Review & communicate","Learn, coordinate with NPCERT, inform the public","Prevents recurrence; limits panic"]],
    per_page=6,widths=[2.2,2.9,2.7],fs=11,
    note="Preparedness is the difference between a scare and a catastrophe: every step assumes the attack will come and is rehearsed before it does. Clear public communication limits panic — the attacker's real goal.")
concept_apply("S37 · Concept 3 · [THEORY]","Resilience & Preparedness",
    "A national bank suffers a service-disrupting attack. Because it prepared — backups, tested business-continuity plans, failover, and a rehearsed communication plan — it detects fast, contains the affected systems, recovers service from clean backups, coordinates with NPCERT, and keeps customers informed. The same attack against an unprepared bank would be a catastrophe; against a prepared one, a manageable scare.",
    "\"Good defence means never getting attacked.\" No defence is perfect, so hoping it won't happen is not a plan. Resilience assumes an incident will occur and invests in backups, failover, tested response, and coordination — so recovery is fast and the impact is contained.",
    "Resilience and preparedness mean assuming attacks will happen and building the ability to keep operating and recover fast — through backups, failover, tested incident-response and business-continuity plans, drills, clear communication, and coordination with a CERT. It follows the cycle prepare → detect → contain → eradicate → recover → review, and, like earthquake preparedness, it is what decides whether an incident is a scare or a catastrophe.",
    "resilience · assume breach · backups & failover · incident response · business continuity · CERT coordination")

add_activity("S37 — 'Defend one system'  ·  ~5 min",
    ["In pairs (2 min): pick the piece of Nepal's critical infrastructure that worries you most if attacked.",
     "Name the cascade you fear (what fails next if it goes down).",
     "Choose ONE defence to prioritise across the national/organizational/personal layers.",
     "Take 3–4 answers aloud (3 min); connect each defence to a layer of the pyramid."],
    "Seeds: telecom, national payments (eSewa/connectIPS), power, government data. Reward answers that name the cascade AND pick a concrete, layer-appropriate defence (e.g. backups + BCP at the org layer, NPCERT coordination at the national layer).",
    "ACTIVITY [~5 min].")
add_quiz("S37 — Quick Check  ·  ~5 min",
    [("Q1.  The most dangerous feature of an infrastructure attack is:","q"),
     ("a) it's online   b) ✅ cascading effects across dependent systems   c) it's slow   d) it's visible","a"),
     ("     Why: one failure topples the systems that depend on it — the domino effect multiplies harm.","o"),
     ("Q2.  A national team that coordinates response to major cyber incidents is a:","q"),
     ("a) ISP   b) firewall   c) ✅ CERT (Computer Emergency Response Team)   d) VPN","a"),
     ("     Why: a CERT (e.g. NPCERT) coordinates national incident response and intelligence sharing.","o"),
     ("Discussion: which piece of Nepal's critical infrastructure worries you most, and what one defence would you prioritise?","o")],
    "QUIZ [~5 min]. Draw out the cascade concept and the three defensive layers. Connect the CERT answer forward to Unit 9 (cyber law).")
add_summary("S37 · Summary  ·  [~2 min]",
    ["Infrastructure attacks cause cascading, real-world harm — power → telecom → banking → hospitals → panic.",
     "Countering needs three layers: national (CERT/NPCERT, law), organizational (segmentation, IR/BCP), and personal (awareness).",
     "Resilience & preparedness — assume breach, back up, drill, recover — beat hoping it won't happen."],
    "Organizations now expect employees to follow incident-response and business-continuity plans; understanding infrastructure resilience makes you valuable in any IT/management role and a responsible digital citizen.",
    "Next unit — Digital Forensics: how incidents are investigated after the fact.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 7 · Cheat Sheet","One-page revision reference",
    [("Social engineering (S33)","Hacking the PERSON, not the PC — persuasion/deception over any channel. Chosen because it's low-cost, high-success, hard to trace. Humans exploited via helpfulness, authority, fear, curiosity, brand trust."),
     ("The psychology (S34)","Impact CHAINS (one OTP → email → bank → wallet → contacts). Trust is manufactured: authority, liking, social proof, reciprocity. The close: urgency, fear, scarcity. Spot the emotion."),
     ("Attack types (S35)","Phishing (email), vishing (call), smishing (SMS), pretexting (story), baiting (lure), tailgating (door). Recognise the channel + tell; refuse the ask."),
     ("Countermeasures (S35)","Layered: people (training/drills), process (verify-callback, least privilege), tech (MFA, filtering, SPF/DKIM/DMARC). Personal: never share OTP; verify independently; STOP-THINK-CLICK."),
     ("Cyber terrorism (S36)","Ideological INTENT + serious harm/fear, often vs. critical infra. Distinct from crime (profit), hacktivism (protest), warfare (state). Types: infra, data destruction, service denial, propaganda, financing."),
     ("Effects & countering (S37)","CI attacks CASCADE (power→telecom→banking→hospitals). Counter across national (CERT/NPCERT, law), organizational (segmentation, IR/BCP), personal (awareness, don't amplify). Resilience = assume breach + recover fast.")])

add_glossary("Unit 7 · Glossary","Key terms — quick reference",
    [("Social engineering","manipulating people into giving up information or access, not breaking technology."),
     ("Weakest link","the human, exploited via helpfulness, authority, fear, curiosity, and brand trust."),
     ("Path of least resistance","the cheap, high-success human route attackers choose over hardened machines."),
     ("Chain reaction","one leaked credential unlocking a chain of linked accounts."),
     ("Authority (lever)","impersonating a bank/police/IT figure to short-circuit doubt."),
     ("Social proof","'everyone is doing it' pressure used to manufacture trust."),
     ("Reciprocity","a small 'favour' used to extract a bigger concession."),
     ("Urgency / the close","manufactured time pressure so the victim acts before verifying."),
     ("Phishing","fraudulent email with a link/attachment to steal logins or data."),
     ("Vishing","voice-call social engineering (e.g. asking for an OTP/PIN)."),
     ("Smishing","SMS-based social engineering (KYC/parcel/lottery links)."),
     ("Pretexting","using an invented backstory/role to extract information."),
     ("Baiting","dangling a tempting lure (a 'free' download or dropped USB)."),
     ("Tailgating","following an authorised person through a secure door."),
     ("MFA","multi-factor authentication — a stolen password alone can't log in."),
     ("SPF/DKIM/DMARC","email anti-spoofing standards (awareness level)."),
     ("STOP-THINK-CLICK","pause, verify, then act — the personal-prevention rule."),
     ("Cyber terrorism","ideologically motivated use of computers to cause serious harm or fear."),
     ("Hacktivism","hacking for protest or to send a message."),
     ("Cyber warfare","state-versus-state cyber action in a conflict."),
     ("Critical infrastructure (CI)","systems a society can't function without (power, telecom, finance…)."),
     ("Cascading effect","one system's failure toppling the systems that depend on it."),
     ("CERT / NPCERT","a (national) Computer Emergency Response Team; NPCERT is Nepal's."),
     ("Resilience","assuming attacks happen and being able to keep operating and recover fast."),
     ("Incident response","prepare → detect → contain → eradicate → recover → review.")])

# ============= CONSOLIDATED END-OF-UNIT QUIZ =============
add_divider("Unit 7 · Revision","Consolidated end-of-unit quiz",
    "Ten MCQs across the whole unit (answers shown), then short-answer, applied-case, and discussion questions to work from the concept slides and Unit7_material.md. All content stays at the recognition/defence level.",
    "Use as a 15–20 min in-class quiz or take-home review.")
add_quiz("Section A — Multiple choice (answers shown)",
    [("1.  Social engineering primarily attacks   →  ✅ human psychology / people","a"),
     ("2.  Why humans are the weakest link   →  ✅ helpfulness, authority, fear, curiosity, brand trust","a"),
     ("3.  Why attackers prefer social engineering   →  ✅ low cost + high success vs. beating strong tech","a"),
     ("4.  'I'm from the bank, act now' combines   →  ✅ authority + urgency/fear","a"),
     ("5.  A fraudulent phone call for your OTP is   →  ✅ vishing","a"),
     ("6.  The best rule against OTP fraud is   →  ✅ never share your OTP with anyone","a"),
     ("7.  Match by channel: SMS scam link is   →  ✅ smishing","a"),
     ("8.  What distinguishes cyber terrorism from cybercrime   →  ✅ political/ideological intent to cause fear/harm","a"),
     ("9.  A type of cyber terrorism   →  ✅ propaganda/psy-ops (or a critical-infrastructure attack)","a"),
     ("10. A national team coordinating cyber incident response is a   →  ✅ CERT (e.g. NPCERT)","a")],
    "Consolidated quiz Section A.",compact=True)
add_quiz("Sections B–D — short answer, applied case & discussion",
    [("Section B — Short answer","q"),
     ("11. Define social engineering.   12. List 4 reasons humans are exploited.   13. Name & explain 3 attack types.","o"),
     ("14. List 4 countermeasures (personal + organizational).   15. Define cyber terrorism and give two of its types.","o"),
     ("Section C — Applied case","q"),
     ("16. Given a Nepali scam SMS/call transcript: identify the attack type, the psychological levers, and the safe response.","o"),
     ("17. Given a national-infrastructure attack: describe the cascading effects and 3 countering measures across the national/organizational/personal layers.","o"),
     ("Section D — Discussion","q"),
     ("18. Is a politically motivated defacement of a Nepali government website 'cyber terrorism'? Argue both sides using intent, target, and severity.","o")],
    "Consolidated quiz Sections B–D. Model answers on the concept slides and in Unit7_material.md. All attack content stays at recognition/defence level.",compact=True)

# ---- close ----
add_title("End of Unit 7  ·  IT 246",
          "S33–S37 complete: social engineering & the human 'weakest link' · the psychology of the con · attack types & countermeasures · "
          "cyber terrorism & its types · effects on infrastructure & how we counter it",
          "Built to COURSE_MATERIAL_STANDARD.md incl. the §7A depth rule · comparison & concrete-example tables throughout · "
          "DEFENSIVE / awareness framing · self-contained, PDF-safe · Next: Unit 8 — Digital Forensics.")

_add_page_numbers()
save("IT246_Unit7.pptx")
