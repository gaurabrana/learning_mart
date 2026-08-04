#!/usr/bin/env python3
"""IT246 (sixth) Unit 6 deck — Personal Cybersecurity (S28–S32), built to
COURSE_MATERIAL_STANDARD.md INCLUDING the §7A depth rule: every confusable set is a
comparison table, every 'X vs not-X' concept a concrete-example table, claims get
scaffolding tables — each table on its OWN slide, paginated, never squeezed. Self-contained
& PDF-safe. Nepal-localised (eSewa/Khalti OTP scams, WorldLink/Vianet routers, Nagarik App,
Thamel/New Road snatching, second-hand market). Imports deckkit.py. Diagrams in images/.
Run: python3 build_unit6_pptx.py -> IT246_Unit6.pptx
"""
from deckkit import *

# ============================================================
#                        FRONT MATTER
# ============================================================
add_title("Unit 6 — Personal Cybersecurity",
          "IT 246: IT Ethics & Cybersecurity  ·  BIM 6th Semester  ·  Sessions S28–S32",
          "Self-contained slides with depth: every concept grounded in comparison & concrete-example TABLES "
          "(Nepal / IT localised) — weak-vs-strong practices, scam types, do/don't. Exports to PDF with no information lost.")

add_outcomes("Unit 6 — Learning Outcomes","personal cybersecurity  ·  s28–s32",
    "By the end of this unit, you will be able to:",
    ["Audit your home computer's security posture — updates, antivirus, backups, firewall — and fix the weak spots (S28)",
     "Harden your mobile phone and home IoT devices against permissions abuse, default passwords and insecure networks (S29)",
     "Apply physical-security habits against theft, shoulder-surfing and careless device disposal (S30)",
     "Configure a safer work-from-home setup: secured router, VPN, work/personal separation, safe video calls (S31)",
     "Secure your online accounts with strong unique passwords, a password manager and MFA, and respond to a breach (S32)"],
    "This is Unit 6 of IT 246. It turns Units 1–4's ethics and Unit 5's cybersecurity fundamentals into YOUR own daily defence — the device in your hand, the router in your room, and the accounts that hold your money and identity.")

add_roadmap("Unit 6 — Roadmap","Where each session fits (S28–S32)",
    ["S28  Your home computer: posture, patching, AV, backups, firewall",
     "S29  Mobile devices & Internet of Things (IoT)",
     "S30  Physical security: theft, shoulder-surfing, disposal",
     "S31  Cybersecurity when working from home",
     "S32  Securing your accounts & passwords — closes unit"],
    ["Unit 7   Social engineering & cyber terrorism",
     "Units 8–9   Digital forensics · Cyber law in Nepal (ETA)"])

# ============================================================ S28
add_divider("Session 28 · Lecture hour 1 (of 5)","Evaluating Your Cybersecurity Posture: Home Computer",
    "Your laptop has 47 pending updates, no backup, and an antivirus that expired in 2022 — but it 'feels fine.' If it got locked by ransomware tonight, what would you lose, and could you get it back?",
    "OPENING HOOK [~5 min]. Draw out that most personal security is basic hygiene nobody does. Agenda: what a security posture is → updates → antivirus → backups (3-2-1) → firewall.")

concept_understand("S28 · Concept 1 · [THEORY]","Security Posture — auditing yourself",
    "Your security posture is the overall state of how well your device and habits resist AND recover from threats. Audit it in layers: patch → protect → back up → contain. Risk = likelihood × impact — and a single laptop holds your photos, college files, and banking sessions.",
    ["Think in four layers, not one magic tool: patch, protect, back up, contain.",
     "Risk = likelihood × impact: low-effort attacks are very likely; the impact on one laptop is your whole digital life.",
     "Most attacks are automated and untargeted — they scan the internet and hit whoever is unpatched.",
     "A good posture assumes something WILL fail, and makes sure you can recover when it does."],
    "s28_posture.png","Posture = patch + protect + back up + contain — layers, not one wall.",
    "~8 min. Land the mindset shift: security is a posture you audit, not a product you buy. Keep returning to the four layers — they are the spine of the whole session.")
add_table_slide("S28 · Concept 1 · scaffolding","The four posture layers — what each one does",
    ["Layer","What it does","If you skip it (Nepal / IT)"],
    [["Patch","Closes known holes attackers already exploit","An unpatched laptop caught by an automated worm (WannaCry-style)"],
     ["Protect","Antivirus + firewall block malware & bad traffic","A 'PC cleaner' pop-up installs the very malware it claims to remove"],
     ["Back up","Recoverable copies survive ransomware/theft","Thesis files gone when a stolen laptop had the only copy"],
     ["Contain","Limits damage when one layer fails","One phished password unlocks everything because nothing was segmented"]],
    per_page=4,widths=[1.3,3.0,3.2],fs=11,
    note="No single layer is enough. Posture is the WHOLE stack — and the cheapest win is usually the layer you've been ignoring.")
concept_apply("S28 · Concept 1 · [THEORY]","Security Posture — auditing yourself",
    "A Pulchowk/BIM student's laptop was hit by ransomware days before thesis submission — no backup, files gone. Globally, WannaCry (2017) spread mostly to unpatched Windows machines. Neither victim was 'targeted': automated attacks simply found an unpatched, un-backed-up machine and took it.",
    "\"Hackers only target big companies, not me.\" Most attacks are automated and untargeted — they hit whoever is unpatched and un-backed-up, student or bank alike. You don't have to be interesting to be a victim; you only have to be reachable and unprotected.",
    "A security posture is the overall state of how well your device and habits resist and recover from threats, audited in four layers: patch (close known holes), protect (antivirus + firewall), back up (recoverable copies), and contain (limit damage when a layer fails). Risk = likelihood × impact, and because most attacks are automated and untargeted, everyone needs a posture — not just big organisations.",
    "security posture · patch/protect/back up/contain · risk = likelihood × impact · automated & untargeted attacks")

concept_understand("S28 · Concept 2 · [THEORY]","Updates & Patching",
    "A patch fixes a known security hole that attackers already know about. Turn on automatic updates for the OS, browser, and apps. 'End-of-life' software (e.g. Windows 7) never gets fixed again — every hole found after that stays open forever.",
    ["Once a patch is public, the hole it fixes is public too — unpatched machines become easy, known targets.",
     "Automatic updates for OS + browser + apps close holes without you having to remember.",
     "End-of-life software (no more updates) only gets more dangerous over time.",
     "Most updates are security fixes, not new features — 'later' means 'exposed until later'."],
    None,"A patch closes a door attackers already have the key to — apply it before they walk in.",
    "~6 min. The pirated-Windows point lands hard in Nepal: a cracked OS that can't update safely is a permanently open door, often shipping malware from day one.")
add_examples_table("S28 · Concept 2 · concrete examples","Patch or not? — real Nepali habits and their verdict",
    ["Habit / situation","Verdict","Why (consequence)"],
    [["Auto-updates ON for Windows + Chrome","Safe","Holes close automatically before attackers arrive"],
     ["'Remind me later' clicked for weeks","Weak","Every known hole stays open the whole time"],
     ["Pirated/cracked Windows that can't update","Dangerous","No safe patches + often ships bundled malware"],
     ["Still running Windows 7 / an old Android","Dangerous","End-of-life: new holes are never fixed again"],
     ["Ignoring app updates ('just new features')","Weak","Most updates are security fixes, not cosmetics"],
     ["Updating the OS but never the router firmware","Weak","The router is a computer too — it has holes as well"]],
    per_page=6,widths=[3.0,1.3,3.0],fs=11,
    note="Pirated/cracked software is common in Nepal and is the worst case: it usually cannot patch safely AND arrives with malware pre-installed.")
concept_apply("S28 · Concept 2 · [THEORY]","Updates & Patching",
    "Pirated/cracked Windows is common in Nepal and often can't update safely — and frequently ships with bundled malware from the crack itself. A genuine, auto-updating OS closes holes the moment a fix ships; the cracked copy leaves them open forever and may already be compromised before you type a password.",
    "\"Updates are just annoying new features I can skip.\" Most updates are security fixes for holes attackers already know about — 'skip' means 'stay exposed'. And end-of-life software (Windows 7) is not merely old; it is permanently unpatchable, so it only gets more dangerous.",
    "Patching applies vendor fixes for known security holes, which become public — and therefore easy to exploit — as soon as the patch ships. The defence is automatic updates for OS, browser, and apps, and retiring end-of-life software that no longer receives fixes. In Nepal, pirated/cracked software is the sharpest trap: it usually cannot patch safely and often ships with malware pre-installed.",
    "patch · known vulnerability · automatic updates · end-of-life software · pirated software risk")

concept_understand("S28 · Concept 3 · [THEORY]","Antivirus / Anti-Malware",
    "Antivirus (anti-malware) is software that detects and blocks malicious files and behaviour. Windows Defender is built in, free, and fine for most users. It works by real-time scanning (as files arrive) plus on-demand scans, using both known signatures and suspicious-behaviour detection.",
    ["Real-time scanning catches threats as they arrive; on-demand scans sweep what's already there.",
     "Signature detection catches known malware; behaviour detection flags new, unseen threats acting badly.",
     "One good, updated AV is enough — Windows Defender covers most home users for free.",
     "Running two real-time antivirus programs at once causes conflicts and slowdowns, not extra safety."],
    None,"One good, updated antivirus beats three fighting each other — and Defender is free.",
    "~6 min. The 'PC cleaner pop-up IS the malware' case is the teachable moment: unsolicited pop-up + urgency + 'pay to fix 5 viruses' are the red flags.")
add_examples_table("S28 · Concept 3 · concrete examples","Real antivirus / malware situations — spot the trap",
    ["Situation","Verdict","Why (the tell)"],
    [["Windows Defender on, kept updated","Safe","One good real-time AV is enough for most users"],
     ["Pop-up: 'Your PC has 5 viruses — pay to fix!'","Scam / malware","Unsolicited + urgency + pay-now = the malware itself"],
     ["A free 'PC cleaner' from a random pop-up","Dangerous","Installs the threat it claims to remove"],
     ["Installing 3 antiviruses 'to be extra safe'","Weak","They conflict and slow the PC — no extra safety"],
     ["Cracked 'premium' AV from a torrent","Dangerous","Cracks commonly carry trojans"],
     ["Ignoring AV alerts to keep working","Weak","Dismisses the one warning you actually got"]],
    per_page=6,widths=[3.0,1.4,3.0],fs=11,
    note="The strongest tell of fake-AV/scareware: it found you (a pop-up), rushes you, and asks for money. Real protection is quiet and already installed.")
concept_apply("S28 · Concept 3 · [THEORY]","Antivirus / Anti-Malware",
    "A pop-up screams 'Your PC has 5 viruses — download our cleaner to fix them!' The 'cleaner' IS the malware. The tells: it was unsolicited (a pop-up found you), it manufactured urgency, and it demanded payment. Meanwhile Windows Defender — already on, quietly updating — is doing the real job for free.",
    "\"I need to buy 3 antiviruses to be really safe.\" One good, updated AV is enough; multiple real-time scanners conflict, slow the machine, and can miss threats while fighting each other. More antivirus is not more security — it is more problems.",
    "Antivirus/anti-malware detects and blocks malicious files and behaviour via real-time and on-demand scans, using signature detection (known threats) and behaviour detection (new ones). One good, updated product — Windows Defender is free and enough for most home users — suffices; running several at once causes conflicts, not safety. Scareware pop-ups rushing you to 'pay to fix' viruses are themselves the malware.",
    "antivirus / anti-malware · real-time vs on-demand · signature vs behaviour · Windows Defender · scareware")

concept_understand("S28 · Concept 4 · [THEORY]","Backups — the 3-2-1 Rule",
    "A backup is a recoverable copy of your important data. The rule to memorise: 3 copies, on 2 different media types, with 1 kept offsite (or in the cloud). Ransomware, theft, and disk failure are all defeated by one clean, recent backup you can restore from.",
    ["3 copies means the original plus two backups — one failure never leaves you with zero.",
     "2 media types (e.g. the laptop disk + an external drive) so a single fault can't kill all copies.",
     "1 offsite/cloud copy survives theft, fire, or a power surge that takes the whole room.",
     "A backup you have never test-restored is a hope, not a backup — verify it works."],
    "s28_backup321.png","3 copies · 2 media · 1 offsite — the single habit that beats ransomware.",
    "~8 min. Localise it: cheap drives fail often and load-shedding surges kill hardware; a stolen laptop in a tempo takes everything with it. The offsite copy is what survives all three.")
add_table_slide("S28 · Concept 4 · scaffolding","What each part of 3-2-1 defeats",
    ["3-2-1 element","What it protects against","Nepal example"],
    [["3 copies","Any single copy being lost or corrupted","A file deleted or a drive that silently corrupts it"],
     ["2 media types","One type of hardware failing","A cheap external drive that dies after a year"],
     ["1 offsite / cloud","Theft, fire, or a whole-room disaster","Laptop snatched in a tempo — cloud copy survives"],
     ["A tested restore","A backup that turns out to be broken","Discovering on thesis day that the backup was empty"]],
    per_page=4,widths=[1.8,2.8,2.6],fs=11,
    note="Each part defeats a different disaster. Ransomware, theft, disk failure, and a load-shedding surge are ALL beaten by one recent, tested, offsite copy.")
concept_apply("S28 · Concept 4 · [THEORY]","Backups — the 3-2-1 Rule",
    "In Nepal, load-shedding surges and cheap drives fail often, and a stolen laptop in a tempo takes everything with it. A BIM student who kept the only copy of a thesis on one laptop lost it all to ransomware days before submission. A 3-2-1 setup — laptop + external drive + Google Drive — would have made it a shrug, not a catastrophe.",
    "\"Deleting files or having them on my laptop is basically a backup.\" One copy on one device is zero backups — theft, ransomware, or a dead disk wipes it out at once. A real backup is separate, on different media, and offsite, so no single event can reach all copies.",
    "A backup is a recoverable copy of important data, and the standard is 3-2-1: three copies, on two different media types, with one kept offsite or in the cloud — plus a tested restore. It defeats ransomware, theft, disk failure, and power surges because no single event can reach every copy. A backup that has never been test-restored is a hope, not a backup.",
    "backup · 3-2-1 rule · media types · offsite/cloud copy · tested restore · ransomware recovery")

concept_understand("S28 · Concept 5 · [THEORY]","Firewall Basics",
    "A firewall is a filter that controls which network traffic is allowed in and out. There are two kinds: a host firewall on your OS and a router firewall at your home gateway. The safe default is 'deny incoming by default' — and don't blindly click 'Allow' on every prompt.",
    ["A firewall decides what may connect to your machine and what your apps may connect out to.",
     "Host firewall (Windows/Mac, built in) protects the one device; router firewall protects the whole home.",
     "'Deny by default' for incoming means unrequested connections are blocked unless you allow them.",
     "Clicking 'Allow' on every pop-up defeats the point — allow only apps you actually trust and expect."],
    None,"A firewall is one wall of the castle, not the whole castle — keep the others too.",
    "~6 min. Bust the 'firewall = unhackable' myth: it blocks unwanted connections but does nothing against a phished password or a malicious download you invited in.")
add_examples_table("S28 · Concept 5 · concrete examples","Firewall decisions — allow or deny?",
    ["Prompt / situation","Right move","Why"],
    [["Windows Defender Firewall is ON by default","Keep it on","Blocks unrequested incoming connections"],
     ["Unknown app asks to accept incoming connections","Deny","If you didn't expect it, don't allow it"],
     ["Your known game/app needs a port to play online","Allow (that app)","Trusted, expected — allow narrowly"],
     ["A pop-up says 'disable firewall to speed up PC'","Ignore","No legitimate fix requires turning off the firewall"],
     ["Router admin panel on default password","Change it","An open gateway firewall is no firewall"],
     ["Assuming the firewall stops all malware","Wrong belief","It filters traffic; it can't stop a phished login"]],
    per_page=6,widths=[3.2,1.4,2.8],fs=11,
    note="A firewall controls connections; it does NOT stop malware you download or a password you hand over. It is one layer of the posture, not the whole thing.")
concept_apply("S28 · Concept 5 · [THEORY]","Firewall Basics",
    "Your home has two firewalls: the one built into Windows/Mac guarding your laptop, and the one in your WorldLink/Vianet router guarding the whole house. Both should stay on with 'deny incoming by default' — but if the router still uses the sticker admin password, that gateway firewall is wide open regardless.",
    "\"A firewall makes me unhackable.\" It's one wall, not the whole castle. A firewall blocks unrequested connections, but it can't stop malware you download, a phishing site you log into, or a scam call that talks you out of your OTP. It complements the other layers; it doesn't replace them.",
    "A firewall filters which network traffic is allowed in and out, at two levels: a host firewall on the OS (protects one device) and a router firewall at the home gateway (protects the network). The safe default is deny-incoming-by-default, allowing only trusted, expected apps rather than clicking 'Allow' on every prompt. It is one layer of a posture — it does not stop downloaded malware or a phished password.",
    "firewall · host vs router firewall · deny by default · allow-listing trusted apps · one wall not the castle")

add_activity("S28 — 'Where is your only copy?'  ·  ~5 min",
    ["In pairs (2 min): name the ONE file you'd be devastated to lose (thesis, project, photos).",
     "Say exactly where its only copy lives right now, and what happens if that device dies tonight.",
     "Take 3–4 answers aloud (3 min); for each, place it on the 3-2-1 rule — how many copies, how many media, any offsite?",
     "Close: agree one concrete backup each student will set up this week."],
    "Most students will admit the only copy is on one laptop or phone. Push them to convert 'it's on my laptop' into a real 3-2-1 plan, and to notice that a cloud copy is the single biggest upgrade.",
    "ACTIVITY [~5 min].")
add_quiz("S28 — Quick Check  ·  ~5 min",
    [("Q1.  The best defence against ransomware locking your files is:","q"),
     ("a) a faster antivirus   b) ✅ recent offline/cloud backups (3-2-1)   c) a longer password   d) a new laptop","a"),
     ("     Why: a clean, recent backup lets you restore instead of paying — it beats theft and disk failure too.","o"),
     ("Q2.  Running two real-time antivirus programs at once usually:","q"),
     ("a) doubles safety   b) ✅ causes conflicts/slowdowns with no extra safety   c) is required   d) speeds the PC up","a"),
     ("     Why: multiple real-time scanners fight each other; one good, updated AV (e.g. Defender) is enough.","o"),
     ("Discussion: right now, where is the ONLY copy of your most important file — and what if that device dies?","o")],
    "QUIZ [~5 min]. Draw out the four-layer posture and the 3-2-1 rule; both MCQ traps ('more AV = safer', 'pay to unlock') are the misconceptions students actually hold.")
add_summary("S28 · Summary  ·  [~2 min]",
    ["Security posture = patch + protect + back up + contain; most attacks are automated and hit whoever is unpatched.",
     "Turn on automatic updates and drop end-of-life/pirated software; run one good, updated antivirus (Defender is fine).",
     "Keep 3-2-1 backups (3 copies · 2 media · 1 offsite) and leave your firewall on with deny-by-default."],
    "This is your own laptop, your own thesis, your own banking session. A 10-minute self-audit this week — auto-updates on, Defender confirmed, one cloud backup, firewall on — is the cheapest insurance you will ever buy.",
    "S29 — the device in your pocket and the gadgets in your home: mobile & IoT security.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S29
add_divider("Session 29 · Lecture hour 2 (of 5)","Mobile Devices & Internet of Things (IoT)",
    "A free torch app asks for your contacts, microphone, location, and SMS — why does a flashlight need to read your texts? And your neighbour's CCTV still uses 'admin/admin', so anyone online can watch their living room. Mobile and IoT are where most of us are weakest.",
    "OPENING HOOK [~5 min]. Two hooks: over-broad permissions and default-password IoT. Agenda: app permissions → securing the phone → mobile banking/wallet safety → IoT risks.")

concept_understand("S29 · Concept 1 · [THEORY]","Mobile App Permissions",
    "A permission is the access — camera, mic, location, SMS, contacts, storage — that an app requests. The principle is least privilege: grant only what the app's actual function needs. Prefer 'while using the app' over 'always', and review and revoke permissions in Settings.",
    ["Least privilege: a torch needs the camera flash — not your SMS, contacts, or location.",
     "'While using the app' limits access to when it's open; 'always' lets it watch you in the background.",
     "Permissions can be reviewed and revoked any time in Settings → Apps → Permissions.",
     "Match the permission to the function: a map needs location, a chat app needs the mic — a flashlight needs neither."],
    None,"A flashlight that wants your SMS is not a flashlight — it's a data grab.",
    "~7 min. Anchor on the fake-loan/OTP-stealer apps: they demand SMS + contacts precisely to read OTPs and harass your contacts for repayment.")
add_examples_table("S29 · Concept 1 · concrete examples","Does this app really need it? — permission red flags",
    ["App asks for…","Reasonable?","Why (Nepal / IT)"],
    [["Torch app → SMS + contacts + location","No","A flashlight needs none of these — data grab"],
     ["Map app → location while using","Yes","Core to its function; 'while using' limits it"],
     ["Fake 'loan' app → SMS + contacts","No","Reads your OTPs and harasses contacts for repayment"],
     ["Camera app → camera + mic","Yes","Needed to record video with sound"],
     ["Cloned 'eSewa' app → SMS + accessibility","No","Steals OTPs and can control the screen"],
     ["Game → contacts + call logs","No","Unrelated to gameplay — revoke it"]],
    per_page=6,widths=[3.1,1.3,3.0],fs=11,
    note="The test is function-fit: does the app's real job require this access? Fake loan and cloned-wallet apps demand SMS specifically to intercept your OTPs.")
concept_apply("S29 · Concept 1 · [THEORY]","Mobile App Permissions",
    "Fake/cloned 'loan' and 'eSewa/Khalti' apps circulate on Nepali phones demanding SMS access. That's not a coincidence: SMS access lets them read the OTPs sent by your bank and harvest your contacts, so they can drain accounts and then harass your friends and family for 'repayment'. The permission request is the whole attack.",
    "\"If it's on the Play Store, it must be safe.\" Malicious and cloned apps slip through store review regularly. Check the developer name, the review quality, and the install count — and above all, judge the permissions: an app asking for far more than its function needs is the warning, store or not.",
    "A permission is the access (camera, mic, location, SMS, contacts, storage) an app requests, and the rule is least privilege: grant only what the app's function needs, prefer 'while using the app' over 'always', and review/revoke in Settings. Being on an app store is not proof of safety — cloned and fake apps (e.g. loan/wallet apps demanding SMS to steal OTPs) pass review, so over-broad permissions are the real red flag.",
    "permission · least privilege · while-using vs always · revoke in Settings · cloned/fake apps · OTP theft")

concept_understand("S29 · Concept 2 · [THEORY]","Securing the Phone Itself",
    "Your phone is a computer holding your money, identity, and OTPs — secure it like one. The essentials: a screen lock + biometrics, a short auto-lock timeout, OS updates, installing only from official stores, and enabling 'Find My Device' / remote wipe. Avoid sideloading APKs shared on Facebook/Messenger.",
    ["Screen lock + biometrics + short auto-lock means a lost phone doesn't hand over everything.",
     "OS + app updates patch the phone just like a laptop — cheap phones that stop updating age dangerously.",
     "Official stores only; sideloaded APKs from Facebook groups are a common malware route.",
     "'Find My Device' / remote wipe lets you locate or erase a lost or stolen phone."],
    None,"Your phone holds your bank and your OTPs — lock it, update it, and be able to wipe it.",
    "~7 min. The 'Dashain offer — win an iPhone! install this APK' case is the hook: the APK is a banking trojan that reads OTP SMS. Cheap phones that stop updating after a year are the local reality.")
add_examples_table("S29 · Concept 2 · concrete examples","Phone-hardening habits — strong vs weak",
    ["Habit","Verdict","Why (consequence)"],
    [["Biometric lock + 30-sec auto-lock","Strong","A lost phone stays locked to a thief"],
     ["No lock 'because it's faster'","Weak","Anyone who grabs it owns your accounts + OTPs"],
     ["Installing a 'Dashain offer' APK from Messenger","Dangerous","Banking trojans arrive exactly this way"],
     ["Apps only from the official store","Strong","Far lower chance of malware"],
     ["Cheap phone that stopped updating a year ago","Weak","Unpatched holes never get fixed"],
     ["'Find My Device' + remote wipe enabled","Strong","Locate or erase a lost/stolen phone remotely"]],
    per_page=6,widths=[3.0,1.3,3.0],fs=11,
    note="A phone is a bank, an ID, and an OTP inbox in your pocket. Sideloaded APKs and no screen lock are the two habits that most often end in account takeover.")
concept_apply("S29 · Concept 2 · [THEORY]","Securing the Phone Itself",
    "A 'Dashain offer — win an iPhone!' link asks you to install an APK outside the Play Store. That APK is typically a banking trojan: once installed, it reads your OTP SMS and drains your wallet. Cheap Android phones in Nepal that stop getting updates after a year make this worse — the holes the trojan uses never get patched.",
    "\"iPhones can't get hacked, so I don't need to worry.\" Less-common is not immune — phishing, account theft, and malicious profiles hit any platform. Security is about your habits (locks, updates, official stores, remote wipe), not a brand badge.",
    "Securing the phone means treating it as the computer it is: a screen lock plus biometrics, a short auto-lock timeout, OS/app updates, installing only from official stores (never sideloaded APKs from social media), and enabling Find My Device / remote wipe. Cheap phones that stop updating age into risk, and no platform is immune — phishing and account theft hit iPhone and Android alike, so habits matter more than brand.",
    "screen lock · auto-lock · OS updates · official stores only · sideloading APKs · Find My Device / remote wipe")

concept_understand("S29 · Concept 3 · [THEORY] [EXAMPLE]","Mobile Banking & Wallet Safety",
    "Mobile-money is a top target in Nepal, so guard the keys. Use an app-specific PIN, NEVER share your OTP or MPIN, beware SIM-swap, log out on shared devices, and watch URLs (esewa.com.np vs lookalikes). The core rule: eSewa, Khalti, and banks NEVER ask for your OTP or MPIN.",
    ["An OTP/MPIN is the last key to your money — anyone who has it can move your funds.",
     "SIM-swap: an attacker ports your number to their SIM to receive your OTPs — protect your SIM/number.",
     "Check the real domain (esewa.com.np) — lookalike sites and links harvest your login.",
     "Log out of wallet/banking on any shared or cyber-café device; never save the password there."],
    "s29_otp_scam.png","eSewa/Khalti/banks NEVER ask for your OTP — sharing it hands over your money.",
    "~8 min. Work the scam-call script from the diagram: fake authority → panic story → 'read me the OTP to reverse it' → money gone. The red flags are unsolicited + urgency + asks for OTP.")
add_examples_table("S29 · Concept 3 · concrete examples","OTP / wallet scams — spot the red flag and respond",
    ["Scenario (Nepal)","Red flag","Correct response"],
    [["Call: 'I'm from eSewa, read the OTP to reverse a wrong transfer'","Asks for OTP + urgency","Refuse and hang up — they never ask for OTP"],
     ["SMS link: 'Verify your Khalti account now or it's blocked'","Threat + unknown link","Don't click; open the app directly"],
     ["Caller already knows your name and number","Feels 'legit'","Knowing your name is not proof — still refuse the OTP"],
     ["Site 'esewa-rewards.com' asks you to log in","Lookalike domain","Only trust esewa.com.np / the official app"],
     ["Your number suddenly loses signal, then OTPs stop","Possible SIM-swap","Contact your telco/bank immediately"],
     ["Login saved on a cyber-café PC","Shared device","Log out; never save credentials there"]],
    per_page=6,widths=[3.2,1.7,2.5],fs=11,
    note="One rule covers most of these: a real bank/wallet NEVER asks for your OTP or MPIN. Unsolicited + urgency + asks-for-OTP = scam, every time.")
concept_apply("S29 · Concept 3 · [THEORY] [EXAMPLE]","Mobile Banking & Wallet Safety",
    "The classic Nepali scam: a call — 'I'm from eSewa/your bank, a wrong transfer hit your account, tell me the OTP to reverse it.' Sharing the OTP doesn't reverse anything; it authorises THEIR transfer out of your wallet. eSewa, Khalti, and every bank state plainly that they never ask for your OTP or MPIN — so the request itself is the proof of a scam.",
    "\"Telling the OTP is fine if they already know my name and number.\" An OTP is the LAST key — sharing it hands over your money regardless of what else the caller knows. Scammers buy or guess names and numbers precisely to sound legit; the one thing they still need is the OTP you must never give.",
    "Mobile banking/wallet safety means guarding the keys: an app-specific PIN, never sharing your OTP or MPIN, watching for SIM-swap, logging out on shared devices, and checking the real domain (esewa.com.np) against lookalikes. The anchoring rule is that eSewa, Khalti, and banks never ask for your OTP/MPIN, so any unsolicited, urgent request for it — however much the caller seems to know — is a scam to refuse and report.",
    "OTP / MPIN · never share · SIM-swap · lookalike domains · log out on shared devices · banks never ask")

concept_understand("S29 · Concept 4 · [THEORY] [EXAMPLE]","Internet of Things (IoT) Risks",
    "IoT devices are everyday things with internet connectivity — IP/CCTV cameras, smart bulbs, smart TVs, routers, smartwatches. They tend to ship with default passwords, get few or no updates, are always-on, and are usually unmonitored — which makes them easy bots. The Mirai botnet enslaved millions of IoT devices using default passwords alone.",
    ["Default passwords ('admin/admin') on a device reachable online = anyone can log in.",
     "Rare/no updates mean known holes stay open for the device's whole life.",
     "Always-on and unmonitored: nobody notices when an IoT device is misused.",
     "Compromised IoT devices get herded into botnets (Mirai) to attack others — or to spy on you."],
    "s29_iot_home.png","An IoT device on its default password is a house where the builder's key still works.",
    "~8 min. Localise: home/shop IP cameras in Kathmandu left on default logins and exposed online; WorldLink/Vianet routers kept on the sticker admin password. The baby-monitor/CCTV case makes it visceral.")
add_table_slide("S29 · Concept 4 · scaffolding","Why IoT devices are easy targets — and the fix",
    ["IoT weakness","Why it's dangerous","The fix"],
    [["Default password (admin/admin)","Anyone online can just log in","Change it on first setup"],
     ["Rare or no firmware updates","Known holes stay open for years","Update firmware; retire unsupported devices"],
     ["Always-on, unmonitored","Misuse goes unnoticed for months","Put IoT on a separate guest network"],
     ["Exposed directly to the internet","Scanners find it in minutes","Don't port-forward cameras; use the vendor app"],
     ["Weak/no encryption","Traffic and feeds can be intercepted","Prefer devices with proper security"]],
    per_page=5,widths=[2.1,2.7,2.5],fs=11,
    note="Mirai enslaved millions of devices using default passwords alone. The single highest-value action is changing the default password on every IoT device you own.")
concept_apply("S29 · Concept 4 · [THEORY] [EXAMPLE]","Internet of Things (IoT) Risks",
    "Home and shop IP/CCTV cameras across Kathmandu sit on default logins and are exposed online — meaning a stranger can watch the feed. ISP routers (WorldLink/Vianet) are routinely left on the sticker admin password. A baby monitor or CCTV streaming to the open internet because nobody changed the password lets anyone watch, and lets attackers herd the device into a botnet.",
    "\"An IoT gadget is too small/dumb to be a security problem.\" A default-password camera or router is a house where the builder's master key still opens the front door. Its size doesn't matter — it's always-on, reachable, and enslavable (Mirai proved it at the scale of millions).",
    "IoT devices are everyday internet-connected things (CCTV/IP cameras, smart bulbs/TVs, routers) that commonly ship with default passwords, get few updates, and run always-on and unmonitored — making them easy to hijack, as the Mirai botnet showed at the scale of millions. The defences: change every default password, update firmware, and put IoT on a separate network so a hacked gadget can't reach your real devices.",
    "IoT · default passwords · firmware updates · always-on/unmonitored · Mirai botnet · network segregation")

add_activity("S29 — 'Open your permission settings now'  ·  ~5 min",
    ["Right now (2 min): open Settings → Apps → Permissions on your own phone.",
     "Find one app with access it doesn't actually need, and one home device (router/CCTV) — is it still on a default password?",
     "Share 3–4 examples aloud (3 min); name the permission you'll revoke and the password you'll change.",
     "Close: commit to revoking 2 permissions and changing 1 default password this week."],
    "Students almost always find a game or torch with contacts/location access, and a router on the sticker password. Reward concrete, do-it-now changes over abstract intentions.",
    "ACTIVITY [~5 min].")
add_quiz("S29 — Quick Check  ·  ~5 min",
    [("Q1.  A flashlight app requesting SMS + contacts access is a sign of:","q"),
     ("a) a good feature   b) ✅ over-broad / suspicious permissions   c) faster performance   d) nothing","a"),
     ("     Why: least privilege — an app should get only what its function needs; a torch needs neither.","o"),
     ("Q2.  A caller claiming to be from your bank asks for the OTP to 'fix' a transfer. You should:","q"),
     ("a) share it to help   b) ✅ refuse and hang up — banks never ask for OTP   c) share half of it   d) call back and share","a"),
     ("     Why: the OTP is the last key to your money; a real bank/wallet never asks for it.","o"),
     ("Discussion: name one app on your phone with access it doesn't actually need.","o")],
    "QUIZ [~5 min]. The two MCQs target the two highest-impact habits: least-privilege permissions and never sharing an OTP. Reinforce the IoT default-password point in discussion.")
add_summary("S29 · Summary  ·  [~2 min]",
    ["Grant least-privilege permissions — a flashlight needs neither your SMS nor your contacts; an app store is not proof of safety.",
     "Lock, update, and official-stores-only your phone; enable remote wipe; never sideload APKs from social media.",
     "Never share your OTP/MPIN (banks never ask), and change the default password on every IoT device — Mirai proves why."],
    "The device in your pocket holds your money, your OTPs, and your identity, and the gadgets in your home are doors onto your network. A ten-minute permission-and-password sweep this week closes the gaps most Nepali users leave wide open.",
    "S30 — the physical world: theft, prying eyes, and what you throw away.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S30
add_divider("Session 30 · Lecture hour 3 (of 5)","Enhancing Physical Security",
    "Your password can be 20 characters long — and useless if someone watches you type it on the bus, or buys your old phone with your photos still on it. The cheapest hack is often physical, not digital.",
    "OPENING HOOK [~5 min]. Draw out that digital defences fail if the physical layer is ignored. Agenda: theft & loss → shoulder-surfing → secure disposal → screen locks & access control.")

concept_understand("S30 · Concept 1 · [THEORY]","Device Theft & Loss",
    "Losing a phone or laptop physically means losing everything logged in on it. The defences: full-disk encryption (BitLocker / FileVault / on by default on Android & iOS), a strong screen lock, remote-find/remote-wipe enabled, and simply not leaving devices unattended.",
    ["Full-disk encryption makes the stored data unreadable without your key — theft yields a brick, not your files.",
     "A strong screen lock stops a thief using the still-logged-in apps immediately.",
     "Remote-find/remote-wipe lets you locate or erase the device once it's gone.",
     "Most loss is opportunistic — an unattended device on a café table is the easy grab."],
    "s30_theft_chain.png","A lost UNLOCKED/unencrypted device is a data breach — not just lost hardware.",
    "~7 min. Localise: snatching in crowded micros, tempos, and Thamel/New Road cafés. Walk the attack chain — a stolen phone still logged into eSewa/Facebook/Gmail is account takeover, not just lost hardware.")
add_examples_table("S30 · Concept 1 · concrete examples","Stolen device — encrypted/locked vs not",
    ["Situation","Outcome","Why"],
    [["Encrypted + locked phone snatched in a tempo","Thief gets a brick","Data unreadable; remote-wipe finishes it"],
     ["Unlocked phone still in eSewa + Gmail","Account takeover","Thief resets passwords and drains the wallet"],
     ["Laptop with no disk encryption stolen","Full data breach","Files readable by pulling the drive"],
     ["Remote-wipe enabled on a lost phone","Data erased remotely","You cut off access once it's gone"],
     ["Device left unattended on a café table","Opportunistic theft","Most loss is convenience, not a targeted heist"],
     ["OTP SMS visible on the lock screen","Extra exposure","Thief reads reset codes without unlocking"]],
    per_page=6,widths=[3.1,1.6,2.6],fs=11,
    note="The hardware is cheap to replace; the logged-in accounts are not. Encryption + lock + remote wipe turn a theft into an inconvenience instead of a breach.")
concept_apply("S30 · Concept 1 · [THEORY]","Device Theft & Loss",
    "Phone and laptop snatching is common in crowded micros, tempos, and cafés around Thamel/New Road. A stolen phone still logged into eSewa, Facebook, and Gmail isn't just lost hardware — the thief resets passwords, reads OTP SMS, and empties the wallet. The same theft with encryption + a lock + remote wipe leaves them with a resettable brick.",
    "\"They'll just sell the hardware — my data is safe.\" An unlocked or unencrypted device exposes your accounts, OTP SMS, and saved passwords instantly. The resale value of the phone is trivial next to the eSewa balance and identity sitting unlocked inside it.",
    "Device theft or loss means losing everything logged in on the device, so the defences are full-disk encryption (BitLocker/FileVault, default on modern phones), a strong screen lock, and remote-find/remote-wipe. Encryption and a lock turn a stolen device into unusable hardware; without them, a snatched phone still logged into eSewa/Gmail is an immediate account takeover, not merely lost hardware.",
    "device theft · full-disk encryption · BitLocker/FileVault · remote wipe · still-logged-in = breach")

concept_understand("S30 · Concept 2 · [THEORY]","Shoulder-Surfing & Visual Exposure",
    "Shoulder-surfing is someone watching your screen or keystrokes to steal a PIN or information. Defend by shielding the keypad, using a privacy screen protector, sitting with your back to a wall, and being wary of ATM/POS camera overlays and strangers 'helping' at the machine.",
    ["Cover the keypad with your free hand when entering a PIN/MPIN — cameras and eyes both lose it.",
     "A privacy screen protector narrows the viewing angle so onlookers see a dark screen.",
     "Sit with your back to a wall so no one is reading over your shoulder.",
     "Beware skimmers/camera overlays at ATMs and people crowding you 'to help'."],
    None,"Shield the keypad — the cheapest attack is just watching you type.",
    "~6 min. Localise: shoulder-surfing PINs at ATMs and while entering an MPIN in a shared room or cyber café. Work the 'helpful stranger at the ATM' mini-case.")
add_examples_table("S30 · Concept 2 · concrete examples","Shoulder-surfing situations — risk and defence",
    ["Situation (Nepal)","Risk","Defence"],
    [["Typing an ATM PIN in a busy queue","Someone/ a camera sees it","Cover the keypad with your hand"],
     ["Stranger 'helps' you at the ATM, stands close","Watches PIN / swaps card","Decline help; keep your distance"],
     ["Entering MPIN on a bus / micro","Seatmate reads it","Angle the screen; shield entry"],
     ["Working on a laptop in a café","Screen visible behind you","Sit back-to-wall; privacy filter"],
     ["Camera overlay/skimmer on an ATM slot","PIN + card captured","Check the slot; use trusted ATMs"],
     ["Entering a password in a shared room","Roommate sees keystrokes","Shield; use a password manager autofill"]],
    per_page=6,widths=[3.0,1.8,2.5],fs=11,
    note="These attacks need no malware and no skill — just line of sight. Shielding the keypad and a privacy filter defeat almost all of them.")
concept_apply("S30 · Concept 2 · [THEORY]","Shoulder-Surfing & Visual Exposure",
    "A stranger at the ATM offers to 'help the queue move faster' and stands close while you enter your PIN. The risk is direct: they watch your PIN and may swap or grab your card. The same exposure happens entering an eSewa MPIN in a shared room or cyber café — anyone with line of sight has your key.",
    "\"No one bothers to watch what I type.\" Shoulder-surfing is the lowest-effort attack there is — no malware, no skill, just eyes or a hidden camera. It's common exactly because people assume no one is looking; shielding the keypad costs nothing and defeats it.",
    "Shoulder-surfing is someone observing your screen or keystrokes to steal a PIN or sensitive information, and it requires only line of sight — no malware. Defences are shielding the keypad, a privacy screen protector, sitting back-to-wall, and watching for ATM/POS camera overlays and over-helpful strangers. It matters most where Nepali users enter PINs and MPINs in public — ATMs, buses, and shared cyber cafés.",
    "shoulder-surfing · shield the keypad · privacy screen · ATM skimmer/overlay · line-of-sight attack")

concept_understand("S30 · Concept 3 · [THEORY]","Secure Disposal & Resale",
    "Secure disposal means making data unrecoverable before you sell, donate, or discard a device. A factory reset alone is not always enough: sign out of all accounts first, remove the SIM/SD card, encrypt-then-wipe, and physically destroy dead drives.",
    ["Sign out of every account first — otherwise the next owner may inherit your logins.",
     "Remove the SIM and SD card; they carry contacts, photos, and your number.",
     "Encrypt-then-wipe: with encryption on, a wipe leaves only unreadable ciphertext.",
     "For a dead drive that can't be wiped, physical destruction is the only sure erase."],
    "s30_delete_wipe.png","Delete ≠ erased. Encrypt-then-wipe is what actually makes data unrecoverable.",
    "~7 min. Localise: the second-hand phone/laptop market (Hattisar, online resale) where buyers recover the seller's photos and logins from a careless wipe.")
add_comparison_table("S30 · Concept 3 · comparison","Delete vs format vs factory reset vs encrypt-then-wipe",
    ["Method","How recoverable?","Safe to sell after?"],
    [["Delete / recycle bin","Fully recoverable","No — data is still there"],
     ["Quick format","Mostly recoverable","No — easily undeleted"],
     ["Factory reset (unencrypted)","Often recoverable","Risky — traces may remain"],
     ["Encrypt, then wipe","Unrecoverable","Yes — only ciphertext left"],
     ["Physically destroy the drive","Unrecoverable","Yes — for dead/failed drives"]],
    per_page=5,widths=[2.4,2.3,2.4],fs=11,
    note="Deleting or formatting only removes the 'index'; the data stays until overwritten. Encryption-then-wipe (or destruction) is the reliable erase before resale.")
concept_apply("S30 · Concept 3 · [THEORY]","Secure Disposal & Resale",
    "Nepal's busy second-hand market (Hattisar, online resale groups) means your old device goes to a stranger. Buyers routinely recover the previous owner's photos, chats, and even logins from a careless 'factory reset'. Signing out of accounts, removing SIM/SD, and encrypt-then-wiping first is the difference between selling a phone and selling your identity with it.",
    "\"Deleting my files / formatting the disk erases them.\" Deleted data is usually recoverable until it's overwritten — delete and quick-format only remove the pointer, not the content. Reliable erasure means encryption-then-wipe, or physically destroying a drive that can't be wiped.",
    "Secure disposal makes data unrecoverable before a device is sold, donated, or discarded. A factory reset alone can leave recoverable traces, so the process is: sign out of all accounts, remove SIM/SD, encrypt-then-wipe, and physically destroy dead drives. This matters acutely in Nepal's second-hand market, where careless wipes let buyers recover the seller's photos and logins.",
    "secure disposal · factory reset is not enough · encrypt-then-wipe · remove SIM/SD · physical destruction · resale risk")

concept_understand("S30 · Concept 4 · [THEORY]","Screen Locks & Access Control",
    "Access control is what stands between a person holding your device and your data. Use a PIN/password/biometric, a short auto-lock timeout, lock the screen when you walk away (Win+L), and disable lock-screen notification previews that leak OTPs and messages.",
    ["A PIN or biometric is far stronger than a pattern — patterns are guessable and smudge-readable.",
     "A short auto-lock (30 seconds) means a set-down device locks itself before anyone reaches it.",
     "Lock on walk-away (Win+L / power button) so an unattended machine is never open.",
     "Turn off lock-screen previews so OTPs and message contents aren't readable without unlocking."],
    None,"A short auto-lock + hidden OTP previews is the cheapest theft insurance you own.",
    "~6 min. Bust the pattern-lock myth (smudge-readable, common shapes). The notification-preview leak is the underrated one: OTPs visible on a locked screen defeat the lock.")
add_examples_table("S30 · Concept 4 · concrete examples","Access-control habits — strong vs weak",
    ["Habit","Verdict","Why"],
    [["6-digit PIN / biometric + 30-sec auto-lock","Strong","Fast for you, hard for a thief"],
     ["Simple pattern lock (L or Z shape)","Weak","Guessable + readable from screen smudges"],
     ["No auto-lock, screen stays on","Weak","A set-down device is wide open"],
     ["Lock on walk-away (Win+L)","Strong","No unattended open session"],
     ["OTP/message previews shown on lock screen","Weak","Codes readable without unlocking"],
     ["Previews hidden until unlocked","Strong","OTPs and messages stay private"]],
    per_page=6,widths=[3.2,1.3,2.8],fs=11,
    note="A lock you never trigger (no auto-lock) protects nothing, and previews that show OTPs defeat the lock entirely. Short timeout + hidden previews close both gaps.")
concept_apply("S30 · Concept 4 · [THEORY]","Screen Locks & Access Control",
    "Leaving a device unlocked is like leaving your house door open with a sign pointing to the cash. In practice: a laptop left unlocked at a café for two minutes, or a phone showing your bank OTP on its lock screen, hands over access without any hacking. A 30-second auto-lock and hidden notification previews shut both doors.",
    "\"A pattern lock is plenty.\" Common patterns (L, Z, box) are easy to guess and readable from the smudge trail on the screen; a PIN or biometric is markedly stronger. And any lock is undone if OTPs are previewed on the lock screen — hide previews too.",
    "Access control is the barrier between whoever holds the device and your data: a PIN/password/biometric (stronger than a guessable pattern), a short auto-lock timeout, locking on walk-away (Win+L), and disabling lock-screen notification previews that leak OTPs and messages. Each closes a common gap — an unattended open session, a smudge-readable pattern, or codes readable without ever unlocking the device.",
    "screen lock · PIN/biometric vs pattern · auto-lock timeout · Win+L · hide notification previews")

add_activity("S30 — 'Where do you type a PIN in public?'  ·  ~5 min",
    ["In pairs (2 min): name where you most often type a PIN/MPIN/password in public — and who could be watching.",
     "Trace what a thief would get from your phone RIGHT NOW if it were snatched unlocked.",
     "Take 3–4 answers aloud (3 min); separate 'lost hardware' from 'lost accounts'.",
     "Close: each student names one fix — encryption, auto-lock, hidden previews, or shielding the keypad."],
    "Draw out that the accounts (eSewa, Gmail, Facebook) are the real loss, not the device. Reward students who connect a specific public habit to a specific fix they'll adopt.",
    "ACTIVITY [~5 min].")
add_quiz("S30 — Quick Check  ·  ~5 min",
    [("Q1.  Before selling your old phone you should FIRST:","q"),
     ("a) just factory reset   b) ✅ sign out of all accounts, then encrypt/reset & remove SIM/SD   c) delete some files   d) nothing","a"),
     ("     Why: a reset alone can leave recoverable data and inherited logins; sign out + encrypt-then-wipe is safe.","o"),
     ("Q2.  'A factory reset alone guarantees no one recovers my data' is:","q"),
     ("a) true   b) ✅ false — encrypt-then-wipe (or destroy the drive) is safer   c) true for phones only   d) true if it's fast","a"),
     ("     Why: deleted/reset data is often recoverable until overwritten or the drive was encrypted.","o"),
     ("Discussion: where do you most often type a PIN/password in public, and who could be watching?","o")],
    "QUIZ [~5 min]. Both MCQs attack the 'delete = erased' and 'reset = safe' misconceptions. Tie back to the theft chain: physical loss becomes a data breach without encryption + lock.")
add_summary("S30 · Summary  ·  [~2 min]",
    ["A lost unencrypted/unlocked device is a data breach, not just lost hardware — encrypt, lock, and enable remote wipe.",
     "Shoulder-surfing needs only line of sight — shield the keypad, use a privacy screen, sit back-to-wall.",
     "Wipe properly before disposal (encrypt-then-wipe, remove SIM/SD, sign out); lock screens and hide OTP previews."],
    "You carry your bank, your ID, and your OTPs in your pocket through crowded micros and cafés every day. Encryption, a short auto-lock, hidden previews, and a careful wipe before resale are the physical-layer habits that keep a snatch or a sale from becoming a breach.",
    "S31 — taking all this into the home office: cybersecurity when working from home.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S31
add_divider("Session 31 · Lecture hour 4 (of 5)","Cybersecurity When Working from Home",
    "You join an office Zoom from your bedroom on the same Wi-Fi as your smart TV, your roommate's torrents, and a CCTV with a default password — and you've saved the company database to your Desktop 'just for now.' Where could this go wrong?",
    "OPENING HOOK [~5 min]. Draw out that home is now the office, but without the office's security. Agenda: securing the home network → VPNs → separating work & personal → video-call safety.")

concept_understand("S31 · Concept 1 · [THEORY]","Securing the Home Network",
    "Your router is the front gate of your digital home — secure it first. Change the default admin password, use WPA2/WPA3 with a strong Wi-Fi passphrase, update the router firmware, disable WPS, and set up a guest network for visitors and IoT devices.",
    ["Change the router's admin login off the sticker password — that panel controls everything.",
     "WPA2/WPA3 + a strong passphrase stops neighbours joining and snooping your traffic.",
     "Update firmware: the router is a computer with holes that need patching too.",
     "A guest/IoT network keeps a hacked camera or a visitor's laptop off your work devices."],
    "s31_network.png","Lock the router (the gate); split MAIN from a GUEST/IoT network.",
    "~7 min. Localise: WorldLink/Vianet/Subisu routers left on the sticker password, and shared-Wi-Fi buildings where everyone sees everyone's traffic. The guest-network split is the pro move.")
add_examples_table("S31 · Concept 1 · concrete examples","Home-network setup — strong vs weak",
    ["Setting (Nepal)","Verdict","Why (consequence)"],
    [["Router admin still on the sticker password","Weak","Anyone nearby/online can reconfigure it"],
     ["WPA3 (or WPA2) + a long passphrase","Strong","Neighbours can't join or snoop your traffic"],
     ["Open/'password123' Wi-Fi shared with the building","Weak","Everyone sees everyone's traffic"],
     ["Firmware updated on the router","Strong","Known router holes get patched"],
     ["WPS left enabled for convenience","Weak","WPS PIN can be brute-forced"],
     ["Guest/IoT network separate from work devices","Strong","A hacked camera can't reach your laptop"]],
    per_page=6,widths=[3.2,1.3,2.8],fs=11,
    note="'My Wi-Fi has a password' is not enough — a weak passphrase, default admin login, or old firmware still leaves the gate open. Lock all three, then segment.")
concept_apply("S31 · Concept 1 · [THEORY]","Securing the Home Network",
    "WorldLink/Vianet/Subisu routers are routinely left on the admin password printed on the sticker, and in shared-Wi-Fi buildings everyone can see everyone's traffic. Changing the admin login, setting a strong WPA2/WPA3 passphrase, updating firmware, and putting the CCTV/TV on a guest network turns that open gate into a locked, segmented one.",
    "\"My Wi-Fi has a password, so it's secure.\" A weak passphrase, a default router admin login, or outdated firmware still leaves you exposed even with 'a password' set. Wi-Fi security is the whole gate — passphrase, admin login, firmware, and segmentation — not just one lock.",
    "Securing the home network starts at the router — the gateway to everything — by changing the default admin password, using WPA2/WPA3 with a strong passphrase, updating firmware, disabling WPS, and adding a guest network for visitors and IoT. Having 'a Wi-Fi password' is not enough: a weak passphrase, a sticker admin login, or old firmware keeps the gate open, and segmenting IoT keeps a hacked device off your work machine.",
    "router security · default admin password · WPA2/WPA3 · firmware update · disable WPS · guest/IoT network")

concept_understand("S31 · Concept 2 · [THEORY]","VPNs",
    "A VPN (Virtual Private Network) encrypts your traffic through a secure tunnel. Use your company VPN to reach work resources, and a trusted VPN on public/untrusted Wi-Fi to stop local snooping. Be wary of 'free VPN' apps — some make money by selling your data.",
    ["The VPN tunnel encrypts your traffic so others on the same Wi-Fi can't read it.",
     "On café/public Wi-Fi a VPN stops local snooping of what you send and receive.",
     "A company VPN is often required to reach internal work systems securely.",
     "'Free' VPNs may log and sell your browsing — the product being sold is you."],
    None,"A VPN protects the transport — not against phishing, malware, or a weak password.",
    "~6 min. Localise: working from a café/co-working space in Kathmandu on open Wi-Fi — and the concrete difference a VPN makes there. Bust the 'VPN = anonymous & 100% safe' myth.")
add_examples_table("S31 · Concept 2 · concrete examples","VPN — when it helps and what it can't do",
    ["Situation","Does a VPN help?","Why"],
    [["Working on open café Wi-Fi in Kathmandu","Yes","Encrypts traffic against local snooping"],
     ["Reaching internal company systems from home","Yes (company VPN)","Secure tunnel into work resources"],
     ["You click a phishing link and log in","No","VPN protects transport, not your decisions"],
     ["You download and run malware","No","VPN doesn't scan or block files"],
     ["Using a 'free' VPN of unknown origin","Risky","It may log and sell your traffic"],
     ["Reusing a weak password over a VPN","No","The password is still weak — VPN can't fix that"]],
    per_page=6,widths=[3.0,1.7,2.6],fs=11,
    note="A VPN secures the pipe, not the person. It's essential on untrusted Wi-Fi, but it won't save you from phishing, malware, or a weak/reused password.")
concept_apply("S31 · Concept 2 · [THEORY]","VPNs",
    "Working from a café or co-working space in Kathmandu on open Wi-Fi, anyone on that network can potentially snoop your traffic. A trusted VPN encrypts the tunnel so they see only scrambled data, and a company VPN lets you reach internal systems securely. But a random 'free VPN' app may be quietly logging and selling the very traffic you installed it to protect.",
    "\"A VPN makes me anonymous and 100% safe.\" It protects the transport — it won't save you from phishing, malware, a weak password, or a site you log into willingly. And a free VPN can be worse than none if it sells your data. Use a trusted VPN, but keep every other layer too.",
    "A VPN encrypts your traffic through a secure tunnel, protecting it from local snooping on public/untrusted Wi-Fi and providing secure access to work systems via a company VPN. Its limit is important: it secures the transport only, not your choices — it does nothing against phishing, malware, or a weak password — and 'free' VPNs may log and sell your data, so trust matters.",
    "VPN · encrypted tunnel · public Wi-Fi snooping · company VPN · free-VPN data risk · protects transport only")

concept_understand("S31 · Concept 3 · [THEORY]","Separating Work and Personal",
    "Keep work and personal data and logins apart. Use the work-issued device/account for work, don't store company data on personal cloud or email, and lock the machine when you step away — even at home.",
    ["Mixing work logins with personal accounts spreads a breach from one into the other.",
     "Company data on personal Gmail/Drive is outside the company's control and protection.",
     "Use the work device/account for work so security policy and monitoring apply.",
     "Lock the machine when AFK at home too — flatmates and family are still 'in scope'."],
    None,"Emailing a work file to personal Gmail creates a leak the company can't see or control.",
    "~6 min. Work the mini-case: emailing a work file to personal Gmail 'to finish tonight' creates data leakage, no company control, and breach exposure. Bust the 'at home I can relax security' idea.")
add_examples_table("S31 · Concept 3 · concrete examples","Work/personal separation — risk vs safe practice",
    ["Action","Verdict","Why (consequence)"],
    [["Emailing a company file to personal Gmail","Risky","Data leaves company control; breach exposure"],
     ["Doing work on the work-issued device/account","Safe","Policy, backups, and monitoring apply"],
     ["Saving the client database to your Desktop 'for now'","Risky","Uncontrolled copy on an unmanaged machine"],
     ["Using a personal USB for work files","Risky","Easy to lose; may carry malware"],
     ["Locking the laptop when you leave the room","Safe","Flatmates/family can't wander into work data"],
     ["Same password for work and personal accounts","Risky","One breach cascades across both"]],
    per_page=6,widths=[3.2,1.3,2.8],fs=11,
    note="At home there IS someone around — flatmates, family, guests, IoT, and remote attackers. 'Just for now' copies on personal accounts are exactly how home-work data leaks.")
concept_apply("S31 · Concept 3 · [THEORY]","Separating Work and Personal",
    "You email a work file to your personal Gmail to finish it at night. You've just created three problems: the data left the company's control, it now sits in an account with your (maybe weak) personal security, and if either account is breached the company is exposed with no visibility. Doing the work on the issued device/account keeps it inside the protections built for it.",
    "\"At home there's no one around, so I can relax security.\" Flatmates, family, guests, insecure IoT, and remote attackers are all still in scope — 'home' is not 'safe'. Lock the machine when you step away and keep work on work systems, exactly as you would in an office.",
    "Separating work and personal means not mixing work logins/data with personal accounts: use the work-issued device/account for work, avoid storing company data on personal cloud/email or USBs, and lock the machine when away — even at home. Emailing a work file to personal Gmail leaks data outside company control and protection, and 'home' is not secure by default because flatmates, IoT, and remote attackers remain in scope.",
    "work/personal separation · data leakage · company control · use work device · lock when AFK · home is in scope")

concept_understand("S31 · Concept 4 · [THEORY]","Video-Call & Collaboration Safety",
    "Video calls and shared links leak more than people think. Require meeting passwords and waiting rooms (Zoom/Meet/Teams), don't post invite links publicly, mind what's visible and audible in your background, and beware screen-share leaks and fake meeting-invite phishing.",
    ["Meeting passwords + waiting rooms stop uninvited people 'walking in' (Zoom-bombing).",
     "Don't post invite links publicly — an open link is a public event anyone can join.",
     "Mind your background: whiteboards, screens, and documents behind you leak information.",
     "Beware screen-share slips (notifications, other tabs) and fake 'meeting invite' phishing links."],
    None,"An open meeting link with no password is a public poster — anyone who finds it walks in.",
    "~6 min. Localise: Zoom-bombing of online classes and Dashain/Tihar virtual meetings in Nepal during lockdown when links were shared openly. The background-leak point is underrated.")
add_examples_table("S31 · Concept 4 · concrete examples","Video-call safety — risk vs safe practice",
    ["Situation","Verdict","Why"],
    [["Meeting link posted publicly on Facebook","Risky","Anyone can join — 'Zoom-bombing'"],
     ["Meeting password + waiting room enabled","Safe","Only admitted, invited people get in"],
     ["Screen-sharing with other tabs/notifications open","Risky","Leaks messages, emails, other data"],
     ["Sensitive documents visible in your background","Risky","On-camera info leak"],
     ["Clicking a 'meeting invite' from an unknown sender","Risky","Fake-invite phishing / malware"],
     ["Blurred/neutral background + shared window only","Safe","Nothing extra leaks on camera or screen"]],
    per_page=6,widths=[3.2,1.3,2.8],fs=11,
    note="Two habits prevent most incidents: password + waiting room on every meeting, and sharing only the one window you intend (not the whole screen).")
concept_apply("S31 · Concept 4 · [THEORY]","Video-Call & Collaboration Safety",
    "During lockdown, Nepali online classes and virtual Dashain/Tihar gatherings were 'Zoom-bombed' because links were shared openly with no password. The same carelessness leaks data today: screen-sharing your whole desktop shows your notifications and open tabs, and a sensitive document on the wall behind you is broadcast to everyone on the call.",
    "\"It's just a quick call — I don't need a password or to check my background/share.\" An open link with no password is a public poster anyone can walk into, and a whole-screen share or a cluttered background leaks information silently. Passwords, waiting rooms, and sharing only one window cost seconds.",
    "Video-call and collaboration safety means requiring meeting passwords and waiting rooms, never posting invite links publicly, minding what's visible/audible in your background, and guarding against screen-share leaks and fake meeting-invite phishing. An unprotected link is a public event (the cause of 'Zoom-bombing'), and sharing the whole screen or an exposed background leaks data even when the meeting itself is legitimate.",
    "meeting password · waiting room · Zoom-bombing · background leak · screen-share slips · fake-invite phishing")

add_activity("S31 — 'Weakest link on your Wi-Fi'  ·  ~5 min",
    ["In pairs (2 min): list three devices on your home Wi-Fi right now (phone, laptop, TV, CCTV, roommate's PC…).",
     "Decide which is the weakest link an attacker would target, and why.",
     "Take 3–4 answers aloud (3 min); note how many homes still have the router on its sticker password.",
     "Close: each student names one fix (change router admin, make a guest network, or set meeting passwords)."],
    "The weakest link is usually a default-password IoT device or the router itself. Reward students who connect the weak device to the guest-network fix and to the S29 IoT lesson.",
    "ACTIVITY [~5 min].")
add_quiz("S31 — Quick Check  ·  ~5 min",
    [("Q1.  On open café Wi-Fi, the best protection for work traffic is:","q"),
     ("a) hoping no one looks   b) ✅ a trusted / company VPN   c) a longer password   d) airplane mode","a"),
     ("     Why: a VPN encrypts the tunnel so others on the same Wi-Fi can't snoop your traffic.","o"),
     ("Q2.  Emailing a company file to your personal Gmail to finish later is:","q"),
     ("a) fine and efficient   b) ✅ a data-leakage risk — avoid it   c) required for backup   d) safe if you delete it after","a"),
     ("     Why: the data leaves company control and protection, exposing it (and you) if either account is breached.","o"),
     ("Discussion: list three devices on your home Wi-Fi — which is the weakest link an attacker would target?","o")],
    "QUIZ [~5 min]. MCQ1 rewards the VPN-on-untrusted-Wi-Fi habit; MCQ2 the work/personal separation rule. Draw the router-as-gate and guest-network points out in discussion.")
add_summary("S31 · Summary  ·  [~2 min]",
    ["Lock down the router (the gate): change admin password, use WPA2/WPA3, update firmware, add a guest/IoT network.",
     "Use a trusted/company VPN on untrusted networks — but it protects transport only, not against phishing or weak passwords.",
     "Keep work and personal separate, and protect meetings with passwords + waiting rooms while minding your background."],
    "Home is the office now, without the office's IT team. The habits here — a locked, segmented router, a VPN on café Wi-Fi, work kept on work systems, and password-protected calls — are exactly what a remote Nepali developer or BPO worker needs to work safely and keep a client's trust.",
    "S32 — the keys to everything: securing your accounts and passwords (closes Unit 6).",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S32
add_divider("Session 32 · Lecture hour 5 (of 5) — CLOSES UNIT 6","Securing Your Accounts & Passwords",
    "You reuse one password across Facebook, Gmail, eSewa, and your college portal. One of those sites gets breached — now attackers try that same password everywhere (credential stuffing). How many of your accounts just fell with one domino?",
    "OPENING HOOK [~5 min]. Land that accounts are the real target and passwords the lock. Agenda: strong passwords → password managers → MFA/2FA → breach awareness & response.")

concept_understand("S32 · Concept 1 · [THEORY]","Strong Passwords",
    "A strong password is long, unique, and hard to guess. Length beats complexity: a passphrase like 'hariyo!gai-khana-25' beats 'P@ss123'. Make every account unique, and never use names, DOB, 'password', or '123456'.",
    ["Length beats complexity — a long passphrase has far more combinations than a short symbolic one.",
     "Unique per site: reuse means one breach unlocks everything (credential stuffing).",
     "Avoid personal, guessable bases: phone number, DOB, favourite team/idol, 'nepal123'.",
     "A memorable passphrase of a few unrelated words is both strong and usable."],
    "s32_strength.png","A long unique passphrase beats a short symbolic one — and never reuse it.",
    "~7 min. Localise the weak-password list: phone number, 'nepal123', favourite team/idol, DOB — and the reuse habit across every account. Use the strength ladder diagram.")
add_comparison_table("S32 · Concept 1 · comparison","Weak vs strong passwords — why length wins",
    ["Password","Weak or strong?","Why"],
    [["nepal123 / your phone number","Weak","Guessable, common, in every wordlist"],
     ["P@ss123 (short + symbols)","Weak","Short — cracked in seconds despite symbols"],
     ["Ram@2003 (name + DOB)","Weak","Personal info is easy to find/guess"],
     ["Kathmandu@2026","Medium","Better, but still short and guessable"],
     ["hariyo!gai-khana-25 (passphrase)","Strong","Long + unique — huge search space"],
     ["Same password reused everywhere","Weak","One breach topples every account"]],
    per_page=6,widths=[2.9,1.6,2.7],fs=11,
    note="Length beats complexity, and uniqueness beats everything: a long passphrase is strong, but reusing even a strong password across sites makes it weak again.")
concept_apply("S32 · Concept 1 · [THEORY]","Strong Passwords",
    "Common Nepali passwords — a phone number, 'nepal123', a favourite football team or idol, a date of birth — are exactly what attackers try first, and reusing one across Facebook, Gmail, eSewa, and the college portal means one leak unlocks them all. A passphrase like 'hariyo!gai-khana-25', unique per site, is both easy to remember and hard to crack.",
    "\"Adding @ and a number makes a password strong.\" Short-but-symbolic ('P@ss123') is still weak — length and uniqueness matter most. A long passphrase of a few words beats a short cryptic one, and no amount of symbols saves a password that's reused everywhere.",
    "A strong password is long, unique, and hard to guess, and length beats complexity — a multi-word passphrase ('hariyo!gai-khana-25') outperforms a short symbolic one ('P@ss123'). Every account needs a unique password so one breach can't unlock the rest, and guessable bases (phone number, DOB, favourite team, 'nepal123') must be avoided. Symbols alone don't rescue a short or reused password.",
    "strong password · length beats complexity · passphrase · unique per site · avoid personal/common bases")

concept_understand("S32 · Concept 2 · [THEORY]","Password Managers",
    "A password manager generates and stores a unique password for every site behind one master password. You remember one strong master password (plus MFA on it), and the manager does the rest — which is what makes 'unique everywhere' realistic.",
    ["The manager generates long, random, unique passwords you never have to memorise.",
     "You remember only one strong master password — protect it with MFA.",
     "It removes the reason people reuse passwords: no human can recall 60 unique ones.",
     "Options: Bitwarden, the built-in browser manager, or Google's — pick one and use it consistently."],
    None,"You can't remember 60 unique passwords — a manager is how 'unique everywhere' becomes real.",
    "~7 min. Work the mini-case: with 60 accounts, no human uses 60 unique strong passwords unaided — that's WHY people reuse. Bust the 'manager = single point of failure' fear.")
add_examples_table("S32 · Concept 2 · concrete examples","Password manager — myth vs reality",
    ["Claim / situation","Verdict","Why"],
    [["'I can remember 60 unique strong passwords'","Unrealistic","No one can — which is why people reuse"],
     ["Manager + strong master password + MFA","Strong","One secured vault beats reuse everywhere"],
     ["Writing passwords on sticky notes / a notes app","Weak","Easily seen, lost, or synced insecurely"],
     ["'A manager is one single point of failure'","Overstated","A well-secured vault is far safer than reuse"],
     ["Reusing one password to 'keep it simple'","Weak","One breach = credential stuffing everywhere"],
     ["Letting the manager autofill on the real site","Strong","Also resists lookalike-phishing domains"]],
    per_page=6,widths=[3.1,1.4,2.7],fs=11,
    note="The realistic choice isn't 'manager vs perfect memory' — it's 'manager vs reuse and sticky notes'. A strong master password + MFA makes the vault the safe option.")
concept_apply("S32 · Concept 2 · [THEORY]","Password Managers",
    "You realistically have 50–60 accounts. No human can use 60 unique strong passwords from memory — so people reuse one, which is exactly the vulnerability. A password manager (Bitwarden, your browser's, or Google's) generates and stores a unique password for each, so you memorise one strong master password and the reuse problem disappears.",
    "\"A password manager is a single point of failure / unsafe.\" A well-secured manager — a strong master password plus MFA — is far safer than reusing one password across every site and scribbling others on sticky notes. The real comparison is manager vs reuse, and the manager wins decisively.",
    "A password manager generates and stores a unique password for every site behind one master password (itself protected with MFA), making 'unique everywhere' achievable — which is impossible from memory across 50-60 accounts. The common fear that a manager is a single point of failure is outweighed by the alternative it replaces: password reuse and sticky notes. A well-secured vault is the safer, realistic choice.",
    "password manager · master password · unique-everywhere · Bitwarden/browser/Google · manager vs reuse")

concept_understand("S32 · Concept 3 · [THEORY]","MFA / 2FA",
    "MFA (multi-factor authentication) adds a second proof beyond your password — something you have or are. The strength ladder: SMS OTP < authenticator app (TOTP) < hardware key. Turn it on for your email and banking and social accounts first — and note that SMS-OTP is weakened by SIM-swap.",
    ["A second factor means a stolen password alone isn't enough to get in.",
     "SMS OTP is good but vulnerable to SIM-swap; an authenticator app (Google/Microsoft, TOTP) is stronger.",
     "A hardware key is strongest, resisting phishing outright.",
     "Enable MFA on email first — your email can reset every other account."],
    "s32_mfa.png","MFA blocks most takeovers even when your password is stolen — start with email.",
    "~8 min. Localise: turning on 2FA for eSewa/Khalti, bank apps, Gmail, and Facebook, and WHY email 2FA matters most (email resets everything else). Bust 'MFA is too much hassle'.")
add_comparison_table("S32 · Concept 3 · comparison","MFA factors — weakest to strongest",
    ["Factor","Strength","Trade-off"],
    [["Password only","Weakest","One stolen secret = full access"],
     ["SMS OTP","Better","Vulnerable to SIM-swap; still far better than none"],
     ["Authenticator app (TOTP)","Strong","Codes on your device, no SIM-swap risk"],
     ["Hardware security key","Strongest","Resists phishing; small cost/effort"],
     ["MFA on email specifically","Highest priority","Email resets all other accounts — protect it first"]],
    per_page=5,widths=[2.4,1.8,2.8],fs=11,
    note="Move up the ladder where you can (app over SMS), but any MFA beats none. Enable it on email first — it's the master key that resets everything else.")
concept_apply("S32 · Concept 3 · [THEORY]","MFA / 2FA",
    "Turn on 2FA for eSewa/Khalti, your bank app, Gmail, and Facebook — but do email FIRST, because whoever controls your email can reset the password on every other account. Prefer an authenticator app over SMS where offered: SMS OTP can be intercepted via SIM-swap, while a TOTP app generates codes on your device with no SIM to hijack.",
    "\"MFA is too much hassle for what it's worth.\" MFA blocks the vast majority of account takeovers even when your password is stolen — a few seconds per login against losing your wallet and identity. It's the single highest-value habit after not reusing passwords.",
    "MFA/2FA adds a second proof beyond the password (something you have or are), and its strength runs SMS OTP < authenticator app (TOTP) < hardware key. It blocks most account takeovers even when the password is stolen, so it should go on email first (email resets everything else), then banking and social. SMS-OTP is weakened by SIM-swap, so an authenticator app is preferable where available.",
    "MFA / 2FA · second factor · SMS vs authenticator app vs hardware key · SIM-swap · email first")

concept_understand("S32 · Concept 4 · [THEORY]","Breach Awareness & Response",
    "Breach awareness is knowing when your credentials leak and acting fast. Check haveibeenpwned.com; if you're breached, change that password everywhere it was reused, enable MFA, and watch for follow-on phishing that uses your real leaked details to seem legit.",
    ["Leaks are normal — check haveibeenpwned.com to see if your email appears in known breaches.",
     "On a breach: change that password (and anywhere it was reused), then enable MFA.",
     "Expect follow-on scams: attackers use your real leaked details to make phishing convincing.",
     "This is why reuse is so dangerous — one leaked password is tried everywhere (credential stuffing)."],
    "s32_domino.png","One leaked reused password topples every account — unique passwords contain the blast.",
    "~7 min. Localise: leaked Nepali service/forum databases circulating, then targeted scam calls/SMS quoting your real details. Use the credential-stuffing domino diagram.")
add_examples_table("S32 · Concept 4 · concrete examples","Breach response — right vs wrong moves",
    ["Situation","Right move","Why"],
    [["Your email shows up on haveibeenpwned","Change that password + enable MFA","Assume the leaked password is now public"],
     ["You reused that password on 5 sites","Change it on all 5","Credential stuffing tries it everywhere"],
     ["A scam SMS quotes your real name + last order","Treat as phishing; don't click","Leaked data makes scams look legit"],
     ["Ignoring a breach notice 'it's probably nothing'","Wrong","The password is already circulating"],
     ["Adding MFA after a breach","Right","Blocks takeover even with the leaked password"],
     ["Using the same 'new' password again everywhere","Wrong","Re-creates the reuse vulnerability"]],
    per_page=6,widths=[3.1,2.0,2.1],fs=11,
    note="A breach is a when, not an if. Fast response — change + de-reuse + MFA — plus scepticism toward follow-on phishing is what limits the damage.")
concept_apply("S32 · Concept 4 · [THEORY]","Breach Awareness & Response",
    "Leaked Nepali service and forum databases circulate, and are often followed by targeted scam calls and SMS that quote your real name, number, or recent activity to seem legitimate. Running your email through haveibeenpwned.com tells you if you're exposed; if so, change that password everywhere it was reused, enable MFA, and treat any 'official' follow-up that knows your details as likely phishing.",
    "\"Reusing one password is fine if it's a strong one.\" Once any one site leaks it, attackers replay it across all your accounts — credential stuffing — so a strong-but-reused password topples like a domino. Uniqueness (via a manager) is what contains a single leak to a single account.",
    "Breach awareness is knowing when your credentials leak (e.g. via haveibeenpwned.com) and responding fast: change the exposed password everywhere it was reused, enable MFA, and stay alert to follow-on phishing that uses your real leaked details. Credential stuffing — replaying one leaked password across your accounts — is why reuse is so dangerous, and unique passwords per site are what contain a single breach.",
    "breach awareness · haveibeenpwned · credential stuffing · change + de-reuse + MFA · follow-on phishing")

add_activity("S32 — 'How many accounts share a password?'  ·  ~5 min",
    ["In pairs (2 min): honestly, how many of your accounts share a password right now?",
     "Identify which account breaking would hurt the most (usually your primary email) and why.",
     "Take 3–4 answers aloud (3 min); connect reuse to the credential-stuffing domino.",
     "Close: each student names their plan — set up a manager, make email unique, and turn on email MFA this week."],
    "Most students share one password widely and haven't protected email first. Reward the realisation that email is the master key and that a manager + MFA is the concrete fix, not more willpower.",
    "ACTIVITY [~5 min].")
add_quiz("S32 — Quick Check  ·  ~5 min",
    [("Q1.  The single most important account to protect with a strong password + MFA is usually:","q"),
     ("a) a game account   b) ✅ your primary email (it can reset all the others)   c) a shopping app   d) a news site","a"),
     ("     Why: whoever controls your email can trigger password resets on everything linked to it.","o"),
     ("Q2.  Reusing one password and having one site breached enables:","q"),
     ("a) faster login   b) ✅ credential stuffing across your other accounts   c) stronger security   d) nothing","a"),
     ("     Why: attackers replay the leaked password everywhere; unique passwords contain the breach to one account.","o"),
     ("Discussion: how many of your accounts share a password right now — and which one breaking would hurt most?","o")],
    "QUIZ [~5 min]. MCQ1 lands the email-is-the-master-key point; MCQ2 the credential-stuffing danger of reuse. Close the unit by tying passwords → manager → MFA → breach response together.")
add_summary("S32 · Summary  ·  [~2 min]",
    ["Use long, unique passphrases per site — length beats complexity, and reuse is the real weakness.",
     "A password manager makes 'unique everywhere' realistic; MFA (authenticator app > SMS) stops most takeovers — protect email first.",
     "Assume breaches happen: check haveibeenpwned, change + de-reuse the password, enable MFA, and expect follow-on phishing."],
    "Your accounts — email, eSewa, bank, Facebook — are the real prize, and passwords are the lock. Setting up a manager, making your email password unique, and turning on authenticator-app MFA this week is the highest-return hour of security work you can do.",
    "End of Unit 6. Next unit: Social Engineering & Cyber Terrorism — how attackers target the human, not the machine.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 6 · Cheat Sheet","One-page revision reference",
    [("Home computer (S28)","Posture = patch + protect + back up + contain. Auto-update; drop end-of-life/pirated OS. One good AV (Defender). 3-2-1 backups (3 copies · 2 media · 1 offsite). Firewall on, deny-by-default."),
     ("Mobile & IoT (S29)","Least-privilege permissions (a torch needs no SMS). Lock + update + official stores + remote wipe. NEVER share OTP/MPIN — banks never ask. Change EVERY IoT default password (Mirai)."),
     ("Physical security (S30)","Lost unlocked/unencrypted device = data breach. Encrypt + lock + remote wipe. Shield the keypad (shoulder-surfing). Encrypt-then-wipe before resale; hide OTP lock-screen previews."),
     ("Work from home (S31)","Router = the gate: change admin pw, WPA2/3, update firmware, guest/IoT network. VPN on untrusted Wi-Fi (transport only). Keep work/personal separate. Meeting passwords + waiting rooms."),
     ("Accounts & passwords (S32)","Long unique passphrases (length > complexity). Password manager makes unique realistic. MFA (app > SMS), email FIRST. Check haveibeenpwned; on breach change + de-reuse + MFA."),
     ("The one-line unit","Most personal security is basic hygiene: patch, back up, least privilege, never share OTPs, unique passwords + MFA. Automated attacks hit whoever skipped a layer.")])

add_glossary("Unit 6 · Glossary","Key terms — quick reference",
    [("Security posture","overall state of how well your device/habits resist and recover from threats."),
     ("Patch","a fix for a known security hole; apply via automatic updates."),
     ("End-of-life software","software no longer receiving security updates (e.g. Windows 7)."),
     ("Antivirus / anti-malware","software that detects and blocks malicious files/behaviour."),
     ("Scareware","fake-AV pop-up that rushes you to 'pay to fix' viruses — itself malware."),
     ("Backup (3-2-1)","3 copies, 2 media types, 1 offsite/cloud copy of your data."),
     ("Firewall","filter controlling which network traffic is allowed in/out."),
     ("Permission","the access (camera, SMS, location…) an app requests."),
     ("Least privilege","grant only the access an app's function actually needs."),
     ("OTP / MPIN","one-time / mobile PIN — the last key; banks NEVER ask for it."),
     ("SIM-swap","attacker ports your number to their SIM to steal SMS OTPs."),
     ("IoT","everyday internet-connected devices (CCTV, bulbs, TVs, routers)."),
     ("Mirai botnet","malware that enslaved millions of default-password IoT devices."),
     ("Full-disk encryption","BitLocker/FileVault — makes stored data unreadable without the key."),
     ("Remote wipe","erasing a lost/stolen device remotely (Find My Device)."),
     ("Shoulder-surfing","watching your screen/keystrokes to steal a PIN or data."),
     ("Encrypt-then-wipe","reliable erase before disposal; delete/format is recoverable."),
     ("VPN","encrypted tunnel protecting traffic on untrusted networks (transport only)."),
     ("Guest network","separate Wi-Fi keeping IoT/visitors off your work devices."),
     ("WPA2/WPA3","strong Wi-Fi encryption standards for your home network."),
     ("Zoom-bombing","uninvited people joining a meeting whose link had no password."),
     ("Password manager","tool that generates/stores unique passwords behind one master password."),
     ("Passphrase","a long multi-word password; length beats complexity."),
     ("MFA / 2FA","a second proof beyond the password (SMS < app < hardware key)."),
     ("Credential stuffing","replaying one leaked password across your other accounts."),
     ("haveibeenpwned","site to check if your email appears in known data breaches.")])

# ============= CONSOLIDATED END-OF-UNIT QUIZ =============
add_divider("Unit 6 · Revision","Consolidated end-of-unit quiz",
    "Eleven MCQs across the whole unit (answers shown), then short-answer, applied-case, and discussion questions to work from the concept slides and Unit6_material.md.",
    "Use as a 15–20 min in-class quiz or take-home review.")
add_quiz("Section A — Multiple choice (answers shown)",
    [("1.  'Security posture' means   →  ✅ how well your device+habits resist AND recover from threats","a"),
     ("2.  The 3-2-1 backup rule is   →  ✅ 3 copies · 2 media types · 1 offsite/cloud","a"),
     ("3.  The purpose of patching is   →  ✅ to close known security holes attackers exploit","a"),
     ("4.  Running two real-time antiviruses at once   →  ✅ causes conflicts, no extra safety","a"),
     ("5.  A torch app wanting SMS + contacts is   →  ✅ over-broad / suspicious permissions","a"),
     ("6.  If a 'bank' caller asks for your OTP you should   →  ✅ refuse and hang up — banks never ask","a"),
     ("7.  The main IoT risk is   →  ✅ default passwords + no updates (enslaved by Mirai)","a"),
     ("8.  Before selling a phone you should   →  ✅ sign out, encrypt-then-wipe, remove SIM/SD","a"),
     ("9.  On public café Wi-Fi, best protection is   →  ✅ a trusted / company VPN","a"),
     ("10.  Reusing one leaked password enables   →  ✅ credential stuffing across accounts","a"),
     ("11.  The account to protect with MFA first is   →  ✅ your primary email (it resets the rest)","a")],
    "Consolidated quiz Section A.",compact=True)
add_quiz("Sections B–D — short answer, applied case & discussion",
    [("Section B — Short answer","q"),
     ("12. Explain the 3-2-1 backup rule.   13. List 3 things to check when auditing a phone.   14. Why is a factory reset not always enough?","o"),
     ("15. Name the MFA factor types from weakest to strongest.   16. What is credential stuffing?","o"),
     ("Section C — Applied case","q"),
     ("17. A messy home setup: default router password, no backups, reused passwords, IoT on default logins — write a PRIORITISED hardening plan.","o"),
     ("18. You get a 'from eSewa' call asking for an OTP plus an SMS link — identify the red flags and the correct response.","o"),
     ("Section D — Discussion","q"),
     ("19. Are password managers safer or riskier than memorising passwords? Argue both sides, then take a position.","o")],
    "Consolidated quiz Sections B–D. Model answers on the concept slides and in Unit6_material.md.",compact=True)

# ---- close ----
add_title("End of Unit 6  ·  IT 246",
          "S28–S32 complete: home-computer posture · mobile & IoT · physical security · work-from-home · accounts & passwords",
          "Built to COURSE_MATERIAL_STANDARD.md incl. the §7A depth rule · comparison & concrete-example tables throughout · "
          "self-contained, PDF-safe · Next: Unit 7 — Social Engineering & Cyber Terrorism.")

_add_page_numbers()
save("IT246_Unit6.pptx")
