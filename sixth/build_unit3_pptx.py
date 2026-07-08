#!/usr/bin/env python3
"""IT246 (sixth) Unit 3 deck — Intellectual Property (S11–S16), built to
COURSE_MATERIAL_STANDARD.md INCLUDING the §7A depth rule: every confusable set is a comparison
table, every 'X vs not-X' concept a concrete-example table, claims get scaffolding tables — each
table on its OWN slide, paginated, never squeezed. Generous slide count by design. Self-contained
& PDF-safe. Imports the shared toolkit deckkit.py. Diagrams in images/.
Run: python3 build_unit3_pptx.py -> IT246_Unit3.pptx
"""
from deckkit import *

# ============================================================
#                        BUILD
# ============================================================
add_title("Unit 3 — Intellectual Property",
          "IT 246: IT Ethics & Cybersecurity  ·  BIM 6th Semester  ·  Sessions S11–S16",
          "Self-contained slides with depth: every concept grounded in comparison & concrete-example TABLES "
          "(Nepal / IT localised) — no abstraction without instances. Exports to PDF with no information lost.")

add_outcomes("Unit 3 — Learning Outcomes","intellectual property  ·  s11–s16",
    "By the end of this unit, you will be able to:",
    ["Define IP and distinguish copyright, patent, trade secret, and trademark (S11–S16)",
     "Explain what copyright protects, its duration, and the limits of fair use (S11)",
     "Describe what is patentable, the software-patent debate, and the patent process (S12)",
     "Explain trade secrets, how they're protected, and how they differ from patents (S13)",
     "Judge the ethical line in plagiarism, reverse engineering, open source, competitive intelligence, trademarks & cybersquatting (S14–S16)"],
    "This is Unit 3 of IT 246. It builds on Unit 2's software-piracy and 'who owns the code' questions, and feeds Unit 9's cyber-law treatment. Nepal IP is administered by the Department of Industry and the Copyright Registrar's Office.")

add_roadmap("Unit 3 — Roadmap","Where each session fits (S11–S16)",
    ["S11  IP overview + Copyright (expression, fair use)",
     "S12  Patent (patentability, software patents, process)",
     "S13  Trade secrets (protection, vs patent)",
     "S14  IP issues: plagiarism · reverse engineering",
     "S15  IP issues: open source · competitive intelligence",
     "S16  IP issues: trademark · cybersquatting (closes unit)"],
    ["Unit 4   Ethics in software development & IT orgs",
     "Units 5–8   Cybersecurity & digital forensics",
     "Unit 9   Cyber law in Nepal (ETA, IP enforcement)"])

# ============================================================ S11
add_divider("Session 11 · Lecture hour 1 (of 6)","Intellectual Property Overview · Copyright",
    "You record a song on your phone, write code for a class app, and design a logo for your dai's momo shop. The moment you create them — who OWNS them, and what stops a stranger from selling them as their own? IP is property you can't touch.",
    "OPENING HOOK [~5 min]. Draw out that ownership exists the instant of creation, invisibly. Agenda: what is IP → the four families → copyright (what it protects) → duration & fair use.")

concept_understand("S11 · Concept 1 · [THEORY]","Intellectual Property — property you can't touch",
    "Intellectual property (IP) = legal rights over creations of the mind — works, inventions, names, and secrets. There are four main families: copyright, patent, trade secret, and trademark. IP protects expression and invention, NOT abstract ideas, and balances rewarding creators against public access.",
    ["Copyright protects expression; patent protects inventions; trade secret protects secret info; trademark protects brand identity.",
     "The bargain: creators get temporary control, society eventually gets access — innovation needs both.",
     "In Nepal, IP is administered by the Department of Industry (DoI) and, for copyright, the Copyright Registrar's Office.",
     "Nepal is a WTO / TRIPS member, so its IP law aligns with international minimums."],
    "s11_families.png","Four families: copyright · patent · trade secret · trademark.",
    "~7 min. Keep the four-families image up as the unit's map. Stress that IP is real property with owners, even though it's intangible.")
add_table_slide("S11 · Concept 1 · comparison","The four IP families at a glance",
    ["Family","Protects","Everyday example"],
    [["Copyright","Original expression fixed in form","Your app's source code; a song; a novel"],
     ["Patent","A new, useful, non-obvious invention","A drug formula; a novel machine"],
     ["Trade secret","Confidential info kept secret","Wai Wai's masala ratio; a search algorithm"],
     ["Trademark","A brand's identifying sign","The Goldstar name & logo; eSewa's logo"]],
    per_page=4,widths=[1.5,2.6,3.0],fs=12,
    note="Each protects a DIFFERENT thing and is acquired differently — the full master comparison (what/how/how-long) closes the unit in S16.")
concept_apply("S11 · Concept 1 · [THEORY]","Intellectual Property",
    "Nepali IP is administered by the Department of Industry (DoI) under the Patent, Design and Trademark Act, 2022 BS (1965), while copyright sits with the Copyright Registrar's Office. As a WTO/TRIPS member, Nepal must meet international IP minimums — so a foreign client's IP expectations map onto real Nepali law.",
    "\"If it's on the internet, it's free to use.\" Publication is not permission — most online content is still owned by someone. Being able to right-click and save a photo, or copy a paragraph, gives you access, not rights. The default is 'owned', not 'free'.",
    "Intellectual property is the set of legal rights over creations of the mind, in four families: copyright (expression), patent (invention), trade secret (secret info), and trademark (brand identity). It protects expression and invention rather than abstract ideas, balancing creator reward against public access. In Nepal it is administered by the DoI and the Copyright Registrar's Office.",
    "intellectual property · copyright · patent · trade secret · trademark · DoI · publication ≠ permission")

concept_understand("S11 · Concept 2 · [THEORY]","Copyright — what it protects",
    "Copyright protects original EXPRESSION fixed in a tangible form — text, music, film, software code, art. It protects the expression, NOT the underlying idea, fact, or method. It arises automatically the instant the work is fixed; no registration is needed (though registration helps in a dispute).",
    ["Two people can write different code for the same idea — each owns their own expression.",
     "Facts, ideas, and methods are free; only your particular way of expressing them is protected.",
     "In Nepal, copyright is governed by the Copyright Act, 2059 (2002), registered at the Copyright Registrar's Office.",
     "Source code and a novel are both copyrighted the instant they are written down."],
    "s11_idea_expr.png","Copyright protects the expression, never the idea behind it.",
    "~8 min. Registration is optional but powerful evidence in a dispute. The idea/expression split is the single most-tested copyright point.")
add_table_slide("S11 · Concept 2 · examples","Idea vs expression — what copyright does and doesn't cover",
    ["The work","The IDEA (not protected)","The EXPRESSION (protected)"],
    [["A mobile app","'An app that splits a restaurant bill'","Your actual code implementing it"],
     ["A song","A chord progression / a genre","The specific recorded melody & lyrics"],
     ["A textbook","The facts and concepts taught","The author's particular wording & layout"],
     ["A photo","'A sunrise over the Himalayas'","This photographer's specific shot"],
     ["A recipe","The dish and its method","The written wording of the cookbook page"],
     ["A news event","What happened (the facts)","A journalist's specific article about it"]],
    per_page=6,widths=[1.6,2.7,2.7],fs=11,
    note="Anyone may build the same idea; no one may copy your expression of it. This is why two teams can legally build rival bill-splitting apps.")
concept_apply("S11 · Concept 2 · [THEORY]","Copyright — what it protects",
    "Piracy of Nepali films and music — a film like Kabaddi or popular songs copied to YouTube and sold as pirated DVDs in New Road — infringes the creators' copyright in their expression. A student who copies a Nepali band's melody note-for-note into a college jingle and uploads it has copied the expression: that's infringement, even for a class project.",
    "\"If I change the idea a little, or it's just a class project, copying is fine.\" Copyright attaches to expression the instant it's fixed and covers non-commercial copying too. Copying a melody note-for-note is taking the expression, not being inspired by the idea — the size of the project doesn't change that.",
    "Copyright protects original expression fixed in a tangible form (code, music, text, film, art) — the expression, never the idea, fact, or method behind it. It arises automatically on creation, with registration optional but useful in disputes; in Nepal it is governed by the Copyright Act, 2059 (2002). Copying someone's specific expression, even non-commercially, is infringement.",
    "copyright · expression not idea · fixed form · automatic on creation · Copyright Act 2059")

concept_understand("S11 · Concept 3 · [THEORY]","Copyright Duration & Fair Use",
    "Copyright lasts a limited term, then the work enters the public domain (free for all). In Nepal the general term is the author's lifetime + 50 years, with defined terms for some categories. FAIR USE allows limited use for education, research, news, criticism, and parody without permission.",
    ["The public-domain endpoint is deliberate: society eventually gets free access to all creative work.",
     "Fair use is a limited exception, judged by purpose, amount used, and effect on the work's market.",
     "Quoting a few lines of a poem for a class essay is fair use; photocopying a whole textbook is not.",
     "Attribution and permission are SEPARATE: crediting the author avoids plagiarism, not infringement."],
    None,"Copyright = owning a written recipe: others may cook it, not photocopy the cookbook.",
    "~8 min. The Bhotahity/photocopy-shop dilemma makes fair use concrete. Hammer the attribution≠permission point — it's the most common student misconception.")
add_table_slide("S11 · Concept 3 · examples","Fair use vs infringement — where the line falls (Nepal)",
    ["Use of the work","Fair use?","Why"],
    [["Quoting a few lines of a Nepali poem in an essay","Fair use","Small amount, educational, no market harm"],
     ["Photocopying a whole textbook for the class","Infringement","Copies the entire work; harms the book's market"],
     ["A short clip in a news report / review","Fair use","News/criticism purpose, limited amount"],
     ["Uploading a full movie to YouTube","Infringement","Whole work, no permission, destroys its market"],
     ["A parody of a popular song","Often fair use","Parody is a recognised transformative purpose"],
     ["Reposting an artist's full image on your page","Infringement","Whole work copied without permission"]],
    per_page=6,widths=[3.0,1.4,2.6],fs=11,
    note="Fair use turns on purpose, how much you take, and market effect — not on whether you credited the author. Attribution avoids plagiarism, not infringement.")
concept_apply("S11 · Concept 3 · [THEORY]","Copyright Duration & Fair Use",
    "The Bhotahity photocopy-shop dilemma: quoting a few lines of a Nepali poem in your essay is fair use, but photocopying an entire textbook to save money is infringement — it copies the whole work and undercuts the book's market, no matter how unaffordable the original feels.",
    "\"Crediting the author makes copying legal.\" Attribution and permission are different issues: crediting avoids plagiarism (an integrity offence) but does NOT grant copyright permission (a legal one). You can be a scrupulous citer and still infringe by copying too much.",
    "Copyright lasts a limited term — in Nepal generally the author's lifetime + 50 years — after which the work enters the public domain. Fair use permits limited use for education, research, news, criticism, and parody, judged by purpose, amount, and market effect. Crucially, attribution avoids plagiarism but is separate from copyright permission.",
    "duration · public domain · life + 50 years · fair use · attribution ≠ permission")

add_activity("S11 — 'Fair use or infringement?'  ·  ~5 min",
    ["In pairs (2 min): decide fair use or infringement for three acts you've actually done or seen.",
     "Seeds: sharing a full PDF textbook in a class group; quoting two lines of a song in a caption; reposting a meme.",
     "Take 3–4 answers aloud (3 min); test each with purpose + amount + market effect.",
     "Close: notice attribution didn't decide any of them — that's the key trap."],
    "Push students past 'but I credited it': crediting avoids plagiarism, not infringement. The full-textbook PDF is the clearest infringement (whole work, market harm); a two-line quote is the clearest fair use.",
    "ACTIVITY [~5 min].")
add_quiz("S11 — Quick Check  ·  ~5 min",
    [("Q1.  Copyright protects:","q"),
     ("a) ideas and facts   b) ✅ the expression, not the underlying idea   c) brand names   d) inventions","a"),
     ("     Why: copyright covers your specific expression; the idea/fact/method behind it stays free.","o"),
     ("Q2.  In Nepal, copyright generally lasts:","q"),
     ("a) 10 years   b) forever   c) ✅ the author's life + 50 years   d) until registration lapses","a"),
     ("     Why: after the term the work enters the public domain, free for everyone to use.","o"),
     ("Discussion: is photocopying an entire textbook to save money fair use? Argue both sides.","o")],
    "QUIZ [~5 min]. Draw out affordability vs the author's market — fair use weighs amount + market effect, so a whole book fails even if the motive is sympathetic.")
add_summary("S11 · Summary  ·  [~2 min]",
    ["IP = legal rights over creations of the mind, in four families (copyright, patent, trade secret, trademark).",
     "Copyright protects fixed expression automatically — the expression, not the idea — under Nepal's Copyright Act 2059.",
     "Copyright expires (life + 50 yrs → public domain) and has fair-use limits; attribution ≠ permission."],
    "Every project, blog, song, or app you publish is automatically copyrighted — and so is everything you might be tempted to copy. Knowing the idea/expression line and fair use protects you from both infringing others and being infringed.",
    "S12 — protecting inventions, not expression: patents.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S12
add_divider("Session 12 · Lecture hour 2 (of 6)","Patent",
    "Khalti and eSewa both let you pay by phone — could one have PATENTED mobile wallets and shut the other down? Why do drug prices and phone features hinge on this one question? A patent grants a temporary monopoly on an invention.",
    "OPENING HOOK [~5 min]. Draw out that a patent is a deliberate trade: monopoly now, public knowledge later. Agenda: what's patentable → the software-patent debate → the patent process.")

concept_understand("S12 · Concept 1 · [THEORY]","Patent — what it is and what is patentable",
    "A patent is an exclusive right granted for an invention — a new, useful, non-obvious product or process — in exchange for public disclosure. Unlike copyright (which protects expression), a patent protects the functional idea. It typically lasts about 20 years, then the invention becomes public.",
    ["Three tests: novelty (genuinely new), inventiveness (non-obvious to an expert), industrial applicability (useful/makeable).",
     "You must publicly DISCLOSE how it works — the public's payoff for granting you the monopoly.",
     "In Nepal, patents are registered with the Department of Industry; local tech patents are few (mostly designs, agro, herbal).",
     "Pure ideas, discoveries, and laws of nature are NOT patentable — only concrete, applicable inventions."],
    "s12_funnel.png","Novel + non-obvious + useful — pass all three or no patent.",
    "~8 min. Contrast with S11: copyright would protect the code of a wallet app; a patent would protect the method — a much stronger, rarer right.")
add_table_slide("S12 · Concept 1 · scaffolding","The three patentability tests",
    ["Test","The question it asks","Fails if…"],
    [["Novelty","Is it genuinely new?","It's already known or published (prior art exists)"],
     ["Inventiveness (non-obviousness)","Is it non-obvious to a skilled expert?","An expert would find it an obvious next step"],
     ["Industrial applicability","Is it useful and can it be made?","It's abstract, a pure discovery, or a law of nature"]],
    per_page=3,widths=[1.8,3.0,2.7],fs=12,
    note="All three must pass. 'Being popular' or 'being clever' is not enough — and pure ideas/discoveries fail the third test outright.")
concept_apply("S12 · Concept 1 · [THEORY]","Patent — what is patentable",
    "Patents are registered with the Department of Industry, Nepal under the Patent, Design and Trademark Act. In practice Nepal has relatively few local tech patents — most filings are designs, agricultural, or herbal products — which is why a Nepali software team rarely relies on patents at all (S12 Concept 2).",
    "\"You can patent any good idea.\" Pure ideas, discoveries, and laws of nature are not patentable — only a concrete, novel, non-obvious, useful invention is. 'I thought of mobile payments first' patents nothing; a specific new mechanism for doing it might.",
    "A patent is an exclusive right over a new, useful, non-obvious invention, granted in exchange for public disclosure and lasting about 20 years. It protects the functional idea (unlike copyright's expression) and must pass three tests: novelty, inventiveness, and industrial applicability. Abstract ideas, discoveries, and laws of nature cannot be patented.",
    "patent · novelty · non-obviousness · industrial applicability · disclosure · ~20 years · protects the method")

concept_understand("S12 · Concept 2 · [THEORY] [EXAMPLE]","Software Patents — the debate",
    "Software patents cover software-implemented methods or algorithms — and are controversial worldwide. Copyright already covers the CODE; a patent would cover the METHOD/function. Many jurisdictions (and Nepal in practice) restrict or disallow pure-software patents, partly because of the 'patent troll' problem.",
    ["Copyright protects the specific code; a software patent would monopolise the underlying technique itself.",
     "Broad software patents can block whole approaches, not just one product — a much bigger hammer.",
     "'Patent trolls' acquire patents only to sue, not to build — a widely-cited harm of software patents.",
     "In Nepal, a fintech innovation is usually protected by copyright + trade secret, not patent."],
    None,"Copyright covers the code; a patent would cover the method — that's why it's contested.",
    "~8 min. Amazon '1-Click' and the Apple-vs-Samsung smartphone patent wars show how far software/design patents can reach. Keep the Nepal-startup angle central.")
add_table_slide("S12 · Concept 2 · comparison","Copyright vs patent — for the same piece of software",
    ["Question","Copyright","Patent"],
    [["What does it cover?","The specific written code","The underlying method / function"],
     ["How strong is it?","Blocks copying your code","Blocks anyone using the technique at all"],
     ["How do you get it?","Automatic on writing the code","Apply, disclose, pass 3 tests, pay fees"],
     ["Available for pure software?","Yes — code is copyrightable","Often restricted / disallowed (incl. Nepal in practice)"],
     ["Typical use by a Nepali startup","Yes — protects their codebase","Rare — copyright + trade secret used instead"]],
    per_page=5,widths=[2.1,2.4,2.5],fs=11,
    note="This is why 'just copyright it' is usually the realistic answer for Nepali software — patents on pure software are contested and largely unavailable locally.")
concept_apply("S12 · Concept 2 · [THEORY] [EXAMPLE]","Software Patents",
    "A Kathmandu startup invents a clever load-balancing algorithm. Options: patent it (public disclosure, ~20-yr monopoly — but pure-software patents are largely unavailable in Nepal and costly), keep it a trade secret (private, unlimited — but no protection if a rival independently invents it), or open-source it (community adoption, no monopoly). Most local teams choose copyright + trade secret.",
    "\"We should patent our software to protect it.\" For pure software this is often impossible or impractical — copyright already protects the code, and patents on software are restricted (including in Nepal) and expensive. The realistic tools are copyright + trade secret, sometimes open source.",
    "Software patents cover the method or algorithm, not the code (which copyright already protects); they are controversial and, in many jurisdictions and Nepal in practice, restricted or disallowed, partly due to patent trolls who sue rather than build. A Nepali software innovation is usually protected by copyright plus trade secret rather than patent.",
    "software patent · code vs method · patent troll · restricted for software · copyright + trade secret")

concept_understand("S12 · Concept 3 · [THEORY]","The Patent Process",
    "Getting a patent is a defined sequence: prior-art search → file an application with claims → examination → grant → maintenance/renewal fees. It is slow, costly, public, and TERRITORIAL — a Nepal patent gives no protection in India or the US.",
    ["The 'claims' precisely mark the boundaries of what you're monopolising — like a land survey.",
     "Because it's public, competitors can read exactly how your invention works (that's the disclosure bargain).",
     "Territoriality means global protection requires filing (and paying) in each country separately.",
     "Cost and effort push many Nepali startups to file abroad or skip patents entirely."],
    "s12_process.png","Search → file claims → examine → grant → renew (~20 yrs), one country at a time.",
    "~7 min. The land-claim analogy: you must publicly mark your boundaries (claims), and after the lease (20 yrs) the land becomes public.")
add_table_slide("S12 · Concept 3 · scaffolding","Four things the patent system demands",
    ["Trait","What it means for you","Consequence"],
    [["Slow","Examination can take years","Not a quick fix for a fast-moving product"],
     ["Costly","Filing, attorney, and renewal fees","Prices out many small Nepali startups"],
     ["Public","Your invention is fully disclosed","Rivals learn exactly how it works"],
     ["Territorial","A Nepal patent protects only in Nepal","Global cover needs a filing per country"]],
    per_page=4,widths=[1.4,2.9,2.9],fs=11.5,
    note="These four traits together explain why patents suit visible, high-value, reverse-engineerable inventions — and why software teams often prefer trade secrets (S13).")
concept_apply("S12 · Concept 3 · [THEORY]","The Patent Process",
    "A Nepali startup weighing a patent files at the DoI, but faces the cost/effort of a slow, public, territorial process — and a Nepal patent won't protect them in their export markets. That calculus pushes many to file abroad (expensive) or skip patents and rely on trade secrets and speed-to-market instead.",
    "\"Once I have a patent, I'm protected everywhere.\" Patents are territorial — a Nepal patent means nothing in India, the US, or the EU. Worldwide protection means filing and paying in each jurisdiction separately, which is why global patents are a big-company game.",
    "The patent process runs prior-art search → file claims → examination → grant → renewal fees, and is slow, costly, public, and territorial. The claims define the monopoly's boundaries; disclosure is the public's payoff; and territoriality means protection stops at the border. These costs are why many Nepali startups file abroad or forgo patents.",
    "prior-art search · claims · examination · grant · renewal · territorial · public disclosure")

add_activity("S12 — 'Patent, secret, or open?'  ·  ~5 min",
    ["In pairs (2 min): a Kathmandu startup has a clever new algorithm. Recommend patent / trade secret / open source.",
     "State one reason for and one reason against your choice.",
     "Take 3 answers aloud (3 min); surface the trade-offs (cost, disclosure, reverse-engineerability).",
     "Close: note that for pure software in Nepal, patent is usually the weakest real option."],
    "Good answers weigh: is it reverse-engineerable once shipped? Is it costly to patent? Is community adoption valuable? Most land on copyright + trade secret, occasionally open source for adoption.",
    "ACTIVITY [~5 min].")
add_quiz("S12 — Quick Check  ·  ~5 min",
    [("Q1.  Which is NOT required for patentability?","q"),
     ("a) novelty   b) non-obviousness   c) usefulness   d) ✅ being widely popular","a"),
     ("     Why: popularity is irrelevant — the three tests are novelty, inventiveness, and industrial applicability.","o"),
     ("Q2.  A typical patent term is about:","q"),
     ("a) 5 years   b) ✅ 20 years   c) the author's life + 50   d) unlimited","a"),
     ("     Why: ~20 years of monopoly, then the invention enters the public domain (the disclosure bargain).","o"),
     ("Discussion: should software be patentable in Nepal? What would it do to local startups?","o")],
    "QUIZ [~5 min]. Push the trade-off: patents could reward local R&D but could also let trolls and big firms block small startups from common techniques.")
add_summary("S12 · Summary  ·  [~2 min]",
    ["Patents protect novel, useful, non-obvious inventions (the method) for ~20 years, in exchange for public disclosure.",
     "Software patents are restricted/contested; Nepali software is usually protected by copyright + trade secret.",
     "The process is slow, costly, public, and territorial — a Nepal patent protects only in Nepal."],
    "Before launching a product you'll do a 'freedom-to-operate' check (are you infringing someone's patent?) and decide patent vs secret vs open source. That decision shapes cost, secrecy, and how you defend your product.",
    "S13 — the patent's silent rival: trade secrets.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S13
add_divider("Session 13 · Lecture hour 3 (of 6)","Trade Secrets",
    "Wai Wai's exact masala blend, KFC's spice mix, Google's search ranking — none are patented. They're protected by keeping quiet. How is silence a legal strategy? That's the trade secret.",
    "OPENING HOOK [~5 min]. Draw out that these could be patented but deliberately aren't — because a patent expires and discloses, while a secret can last forever. Agenda: what a trade secret is → how it's protected → trade secret vs patent.")

concept_understand("S13 · Concept 1 · [THEORY]","Trade Secret — definition",
    "A trade secret is confidential business information that gives a competitive edge and is kept secret through reasonable effort. It covers formulas, recipes, processes, customer lists, algorithms, and source code. Protection lasts as long as it stays secret — potentially forever — and needs no registration.",
    ["No government grant and no filing — the protection IS the secrecy plus reasonable effort to keep it.",
     "It can last indefinitely (Coca-Cola's formula is over a century old and still secret).",
     "But it offers NO protection against independent discovery or legitimate reverse engineering.",
     "The moment the secret leaks or is figured out, the protection evaporates."],
    None,"A trade secret lasts forever — until the day someone else figures it out.",
    "~8 min. The contrast that matters: patent = public + time-limited; trade secret = private + unlimited but fragile.")
add_table_slide("S13 · Concept 1 · comparison","Trade secret vs patent — the key confusable",
    ["Dimension","Trade secret","Patent"],
    [["Public or private?","Private — kept confidential","Public — fully disclosed"],
     ["How long?","Unlimited — while it stays secret","~20 years, then public domain"],
     ["Registration?","None","Formal application & fees"],
     ["Protects against independent discovery?","No — rival may invent it too","Yes — monopoly even vs independent inventors"],
     ["Protects against reverse engineering?","No — legal reverse engineering breaks it","Yes — within the patent term"]],
    per_page=5,widths=[2.3,2.4,2.3],fs=11,
    note="Same invention, opposite strategies: a patent trades secrecy for a strong-but-temporary monopoly; a trade secret trades that monopoly for potentially-forever secrecy — but with no protection if independently found.")
concept_apply("S13 · Concept 1 · [THEORY]","Trade Secret — definition",
    "A noodle/masala brand's spice ratio (Wai Wai / CG Foods), a restaurant's signature recipe, or a remittance company's pricing model are classic trade secrets — valuable, kept confidential, and protected simply by not telling anyone. No form is filed; the secrecy itself is the protection.",
    "\"A trade secret is basically the same as a patent.\" Opposite, in fact: a patent is public and time-limited; a trade secret is private and unlimited — but a patent protects you even if a rival independently invents the same thing, while a trade secret gives you nothing against independent discovery or legitimate reverse engineering.",
    "A trade secret is confidential business information (formula, recipe, process, customer list, algorithm, code) that provides a competitive edge and is protected by reasonable secrecy efforts, with no registration and potentially unlimited duration. Unlike a patent, it is private and can last forever, but offers no protection against independent discovery or legitimate reverse engineering.",
    "trade secret · confidential · reasonable effort · unlimited but fragile · no registration · no protection vs independent discovery")

concept_understand("S13 · Concept 2 · [THEORY]","How Trade Secrets Are Protected",
    "Trade secrets are protected by secrecy MEASURES, not a government grant. The toolkit: NDAs, confidentiality clauses in employment contracts, access controls, 'need-to-know' limits, and non-compete agreements. The law gives a remedy only if the secret was MISAPPROPRIATED — stolen, not independently discovered.",
    ["An NDA (non-disclosure agreement) legally binds people who must know the secret to keep it.",
     "Access controls + 'need-to-know' shrink the circle of people who could leak it.",
     "'Reasonable effort' matters legally: a secret you didn't try to protect may not count as one.",
     "If a rival independently invents or legally reverse-engineers it, that's not misappropriation — no remedy."],
    None,"You only own the secret if you can show you actually tried to keep it.",
    "~8 min. NDAs in Nepali IT outsourcing/BPO firms are the everyday face of this. The developer-leaving-for-a-rival worry is the classic tension.")
add_table_slide("S13 · Concept 2 · scaffolding","How a trade secret is actually protected",
    ["Protection measure","What it does","Nepal / IT example"],
    [["NDA / confidentiality clause","Legally binds insiders to keep quiet","Standard in Nepali IT/BPO employment contracts"],
     ["Access controls","Limits who can even see the secret","Source code repo restricted to a small team"],
     ["Need-to-know","Shares the secret only where essential","Only two staff know the full masala ratio"],
     ["Non-compete agreement","Limits leaving to help a direct rival","A departing developer's contract terms"],
     ["Legal remedy (misappropriation)","Sue only if the secret was stolen","No remedy if a rival independently invents it"]],
    per_page=5,widths=[2.1,2.6,2.6],fs=11,
    note="'Reasonable effort' is a legal requirement — a company that didn't lock down its secret may lose the right to call it one. Independent discovery is never misappropriation.")
concept_apply("S13 · Concept 2 · [THEORY]","How Trade Secrets Are Protected",
    "A developer leaves a Lalitpur software house and rebuilds a similar module from memory at a rival. Theft of a secret, or fair reuse of skill? The line: general skills and know-how you carry in your head are yours to reuse; the employer's specific confidential code, data, or documented processes are not. NDAs and non-competes are what make that line enforceable.",
    "\"If I didn't copy any files, I can't have stolen a trade secret.\" Misappropriation covers taking confidential information, not just files — rebuilding a protected proprietary process from memory can still breach an NDA. But genuinely general skill you learned is yours; the hard cases sit exactly on that boundary.",
    "Trade secrets are protected by secrecy measures rather than registration: NDAs, confidentiality clauses, access controls, need-to-know limits, and non-competes. The law provides a remedy only for misappropriation (theft or breach of confidence), not for independent discovery or legitimate reverse engineering — and only if the owner made reasonable efforts to keep it secret.",
    "NDA · confidentiality clause · access control · need-to-know · non-compete · misappropriation · reasonable effort")

concept_understand("S13 · Concept 3 · [THEORY]","Trade Secret vs Patent — choosing",
    "Choosing how to protect an invention is a strategic call. Rule of thumb: use a TRADE SECRET if it's hard to reverse-engineer and its value is long-term (recipes, internal algorithms); use a PATENT if it will be sold or visible and is reverse-engineerable (a machine, a device mechanism).",
    ["If rivals can take your product apart and copy it, secrecy won't hold — patent it instead.",
     "If the secret can be kept behind closed doors (a recipe, a server-side algorithm), a trade secret can outlast any patent.",
     "Patents trade disclosure for a strong 20-year monopoly; secrets trade that monopoly for potential forever.",
     "Many products use BOTH: patent the visible mechanism, keep the tuning/parameters secret."],
    "s13_tree.png","Reverse-engineerable & visible → patent. Hard to copy & long-term → secret.",
    "~7 min. Run the Wai Wai example: keep the recipe secret (hard to reverse-engineer, forever value) rather than patent it (which would disclose it and expire).")
add_table_slide("S13 · Concept 3 · examples","Which protection fits which asset?",
    ["The asset","Best protection","Why"],
    [["Coca-Cola's formula","Trade secret","Hard to reverse-engineer; value is long-term"],
     ["A new drug molecule","Patent","Reverse-engineerable once sold; needs strong monopoly"],
     ["Google's search ranking","Trade secret","Runs server-side; never shipped to be copied"],
     ["A novel machine mechanism","Patent","Visible in the product; rivals could copy it"],
     ["Wai Wai's masala ratio","Trade secret","Kept in-house; would only expire if patented"],
     ["A consumer gadget's circuit","Patent","Ships to customers who can open it up"]],
    per_page=6,widths=[2.4,1.6,2.6],fs=11,
    note="The deciding question: once it's in customers' hands, can they figure it out? If yes → patent. If it stays behind your walls → trade secret.")
concept_apply("S13 · Concept 3 · [THEORY]","Trade Secret vs Patent",
    "Wai Wai keeps its masala ratio a trade secret rather than patenting it: the recipe is hard to reverse-engineer from the finished noodle, and a patent would both disclose it publicly and expire in ~20 years. Secrecy gives potentially unlimited protection — exactly right for a recipe that never ships in a copyable form.",
    "\"Stronger protection is always better, so always patent.\" Not so: patenting a recipe would publish it and put a 20-year clock on it, when keeping it secret could protect it forever. The right choice depends on reverse-engineerability and time horizon, not on which right sounds strongest.",
    "Choosing between a trade secret and a patent is strategic: patent inventions that are visible and reverse-engineerable (you need a monopoly before rivals copy them); keep trade secrets for information that's hard to reverse-engineer and valuable long-term (a patent would only disclose it and impose a 20-year limit). Many products sensibly use both.",
    "patent vs trade secret · reverse-engineerability · time horizon · disclosure trade-off · use both")

add_activity("S13 — 'Protect this asset'  ·  ~5 min",
    ["In pairs (2 min): assign patent or trade secret to three assets and justify with the reverse-engineerability test.",
     "Assets: a momo shop's signature sauce; a new folding-phone hinge; a bank's fraud-scoring algorithm.",
     "Take 3 answers aloud (3 min).",
     "Close: the deciding question is always 'once it's in customers' hands, can they figure it out?'"],
    "Sauce → trade secret (hard to reverse from taste, forever value); hinge → patent (visible, copyable); fraud algorithm → trade secret (runs server-side, never shipped). Reward the reverse-engineerability reasoning.",
    "ACTIVITY [~5 min].")
add_quiz("S13 — Quick Check  ·  ~5 min",
    [("Q1.  A trade secret stays protected:","q"),
     ("a) for 20 years   b) ✅ as long as it remains secret   c) for life + 50 years   d) until registered","a"),
     ("     Why: protection is the secrecy itself — it can last forever, but ends the moment the secret is out.","o"),
     ("Q2.  The main tool to protect a trade secret with employees is:","q"),
     ("a) a patent   b) a trademark   c) ✅ an NDA / confidentiality agreement   d) a copyright notice","a"),
     ("     Why: NDAs legally bind insiders who must know the secret to keep it confidential.","o"),
     ("Discussion: Wai Wai's recipe — patent it or keep it secret? Justify the choice.","o")],
    "QUIZ [~5 min]. The strong answer: keep it secret — hard to reverse-engineer, unlimited duration; patenting would disclose it and expire in ~20 years.")
add_summary("S13 · Summary  ·  [~2 min]",
    ["A trade secret is valuable confidential info protected by secrecy (NDAs, access controls), not registration.",
     "It can last forever but offers no protection against independent discovery or legitimate reverse engineering.",
     "Trade secret vs patent: private+unlimited+fragile vs public+20 years+strong — choose by reverse-engineerability."],
    "Your first job will likely include an NDA — understanding it protects both you and your employer, and knowing where 'general skill' ends and 'the company's secret' begins keeps you out of legal trouble when you move jobs.",
    "S14 — the IP issues begin: plagiarism and reverse engineering.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S14
add_divider("Session 14 · Lecture hour 4 (of 6)","IP Issues: Plagiarism · Reverse Engineering",
    "You paste a GitHub function into your project, and your friend pastes a Wikipedia paragraph into a report — both 'borrowed'. Is either illegal? Is either wrong? These are different questions, and telling them apart is the whole session.",
    "OPENING HOOK [~5 min]. Separate three things students blur: plagiarism (ethical), copyright infringement (legal), and legitimate study. Agenda: plagiarism → reverse engineering.")

concept_understand("S14 · Concept 1 · [THEORY]","Plagiarism",
    "Plagiarism is presenting someone else's work or ideas as your own, without credit. It is an ETHICAL / academic offence — distinct from copyright infringement, which is a LEGAL one — though they often overlap. It includes self-plagiarism and passing off AI-generated text as your own original work.",
    ["Plagiarism can occur even with uncopyrighted material (copying an idea with no credit).",
     "Infringement can occur even when you credit the source (copying too much protected expression).",
     "Paraphrasing without real understanding, or copying structure, is still plagiarism.",
     "Citing avoids plagiarism only if the work is genuinely attributed AND quoted properly."],
    "s14_venn.png","Plagiarism (ethics) and infringement (law) overlap — but aren't the same.",
    "~8 min. TU's plagiarism rules are real and enforced. AI-written essays submitted as original are today's fastest-growing form.")
add_table_slide("S14 · Concept 1 · examples","Is it plagiarism? — common student cases",
    ["What you did","Plagiarism?","Why"],
    [["Copy-paste a senior's project report as your own","Yes","Presenting others' work as yours, no credit"],
     ["Paraphrase a source but cite it properly","No","Genuine attribution; your own wording"],
     ["Submit an AI-generated essay as your own","Yes","Passing off non-original work as yours"],
     ["Reuse your OWN past submitted essay as new","Yes (self-plagiarism)","Presenting old work as new original work"],
     ["Quote two lines and attribute them","No","Properly quoted and credited"],
     ["Reword a paragraph but keep its structure/ideas, no credit","Yes","Copied structure/ideas without attribution"]],
    per_page=6,widths=[3.1,1.5,2.4],fs=11,
    note="Tribhuvan University enforces anti-plagiarism rules on reports and theses. Note row 2 vs row 6: citing helps ONLY if the wording is genuinely your own or properly quoted.")
concept_apply("S14 · Concept 1 · [THEORY]","Plagiarism",
    "Copy-paste BIM project reports and thesis sections lifted from seniors or online are plagiarism under Tribhuvan University's rules — an integrity offence that can fail you regardless of whether the source was copyrighted. AI-generated essays submitted as your own are the same offence in a new form.",
    "\"Changing a few words, or citing the source, means it's not plagiarism.\" Paraphrasing without real understanding — or keeping the original's structure and ideas — is still plagiarism, and a citation only helps if the work is genuinely attributed and properly quoted. Sprinkling a reference at the end does not launder copied text.",
    "Plagiarism is presenting someone else's work or ideas as your own without credit — an ethical/academic offence, distinct from (though often overlapping) copyright infringement, which is legal. It includes self-plagiarism and passing off AI-generated text as original. Superficial paraphrasing or copied structure is still plagiarism; proper attribution and quotation are what avoid it.",
    "plagiarism · ethical vs legal · self-plagiarism · AI-generated text · paraphrase ≠ original · TU rules")

concept_understand("S14 · Concept 2 · [THEORY] [EXAMPLE]","Reverse Engineering",
    "Reverse engineering is analysing a finished product to discover how it was built or how it works. It is legal and common for interoperability, security research, and learning. It crosses the line when used to copy protected code or break a trade secret/contract — and EULAs often forbid it outright.",
    ["Legitimate uses: making products work together (interoperability), finding vulnerabilities, and learning.",
     "The line is crossed when you copy protected expression or misappropriate a trade secret.",
     "A 'clean-room' re-implementation (rebuild from behaviour, not from the code) is the lawful way to copy a function.",
     "Many licences (EULAs) contractually ban reverse engineering, adding a contract issue on top."],
    None,"Reverse-engineer to understand or interoperate — not to copy protected work.",
    "~7 min. Security careers depend on ethical reverse engineering (studying malware). Intent and use define the line.")
add_table_slide("S14 · Concept 2 · comparison","Reverse engineering — legitimate use vs misuse",
    ["Purpose","Legitimate?","Why"],
    [["Building a tool that interoperates with an app","Legitimate","Interoperability is a recognised lawful purpose"],
     ["Security research (studying malware, finding bugs)","Legitimate","Protects users; standard security practice"],
     ["Learning how a technique works","Legitimate","Understanding is not copying"],
     ["Cloning an app's protected code 1:1","Misuse","Copies protected expression — infringement"],
     ["Extracting a competitor's trade secret","Misuse","Misappropriation of a trade secret"],
     ["Reverse-engineering where the EULA forbids it","Misuse (contract)","Breaches the licence you agreed to"]],
    per_page=6,widths=[3.1,1.6,2.3],fs=11,
    note="Intent and use draw the line: understanding/interoperability/security = legitimate; copying protected code or breaking a secret/contract = misuse.")
concept_apply("S14 · Concept 2 · [THEORY] [EXAMPLE]","Reverse Engineering",
    "A Nepali developer decompiles eSewa's app: to build a compatible tool that works alongside it (legitimate interoperability) versus to clone its features and UI 1:1 (copying protected expression). Same technique, opposite ethics — the purpose and what you do with the result decide which side of the line you're on.",
    "\"Reverse engineering is hacking / always illegal.\" It's a standard, lawful practice for interoperability, security research, and learning — whole security careers depend on it. It becomes wrong only when used to copy protected code, steal a trade secret, or breach a EULA that forbids it.",
    "Reverse engineering is analysing a finished product to learn how it works. It is legal and routine for interoperability, security research, and learning, and a clean-room re-implementation is the lawful way to match a function. It becomes misuse when used to copy protected code, misappropriate a trade secret, or breach a EULA — intent and use define the line.",
    "reverse engineering · interoperability · security research · clean-room · EULA · intent defines the line")

add_activity("S14 — 'Borrowed — wrong, illegal, or fine?'  ·  ~5 min",
    ["In pairs (2 min): classify three acts as plagiarism / copyright infringement / fair study — some are more than one.",
     "Acts: pasting a GitHub function without credit; using AI to write a whole assignment; decompiling an app to learn its API.",
     "Take 3 answers aloud (3 min); place overlaps on the plagiarism/infringement Venn.",
     "Close: 'wrong' (ethics) and 'illegal' (law) are separate axes — an act can be one, both, or neither."],
    "GitHub function without credit = plagiarism (+ possible infringement/licence breach); AI whole assignment = plagiarism; decompiling to learn = legitimate reverse engineering. The AI case is the liveliest — push on where the line is.",
    "ACTIVITY [~5 min].")
add_quiz("S14 — Quick Check  ·  ~5 min",
    [("Q1.  Plagiarism is primarily a violation of:","q"),
     ("a) criminal law   b) ✅ academic / ethical integrity (not always law)   c) patent law   d) trademark law","a"),
     ("     Why: plagiarism is an integrity offence; it may or may not also be copyright infringement.","o"),
     ("Q2.  Reverse engineering is generally legal when done for:","q"),
     ("a) cloning protected code   b) ✅ interoperability / security research   c) stealing a trade secret   d) breaching a EULA","a"),
     ("     Why: understanding, interoperability, and security research are recognised lawful purposes.","o"),
     ("Discussion: is using AI to write your whole assignment plagiarism? Where's the line?","o")],
    "QUIZ [~5 min]. Draw the line at authorship + disclosure: AI as a drafting aid you understand and disclose differs from submitting AI output as your own original work.")
add_summary("S14 · Summary  ·  [~2 min]",
    ["Plagiarism = passing off others' work/ideas as your own — an ethical/academic offence (TU enforces it).",
     "Reverse engineering is legitimate for learning, interoperability, and security — but not for copying.",
     "Intent and use define the line; 'wrong' (ethics) and 'illegal' (law) are separate, overlapping questions."],
    "Every report, thesis, and codebase you submit is checked for plagiarism — and entire security careers are built on ETHICAL reverse engineering. Knowing which axis (ethics vs law) an act sits on tells you both the penalty and the fix.",
    "S15 — open source licensing and the ethics of competitive intelligence.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S15
add_divider("Session 15 · Lecture hour 5 (of 6)","IP Issues: Open Source Code · Competitive Intelligence",
    "Linux, Android, and most of the internet run on code anyone can copy for free — yet companies make billions on it. And firms legally 'spy' on competitors every day. How is any of this allowed? The answers are licensing and the ethics of intelligence-gathering.",
    "OPENING HOOK [~5 min]. Bust the myth that open source means 'no rules'. Agenda: open source (copyright + a licence) → competitive intelligence vs espionage.")

concept_understand("S15 · Concept 1 · [THEORY]","Open Source Code",
    "Open source software is released under a licence that grants rights to use, study, modify, and share the source. Crucially, open source is NOT the absence of copyright — it's copyright PLUS a licence. Licences split into permissive (MIT, Apache — use freely) and copyleft (GPL — derivatives must also be open).",
    ["The author keeps copyright and uses the licence to grant specific rights on specific conditions.",
     "Permissive (MIT, Apache): use it almost anywhere, just keep the attribution/notice.",
     "Copyleft (GPL): if you distribute a derivative, you must release its source under the same terms.",
     "Violating the licence (e.g. shipping GPL code inside a closed product) is copyright infringement."],
    "s15_licenses.png","Open source = copyright + a licence with real obligations.",
    "~8 min. Companies have been sued for shipping GPL code in closed products. The 'free = no rules' myth is the key correction.")
add_table_slide("S15 · Concept 1 · comparison","Permissive vs copyleft — the two open-source families",
    ["Question","Permissive (MIT, Apache)","Copyleft (GPL)"],
    [["Can you use it in closed software?","Yes","Only if you also open your derivative"],
     ["Main obligation","Keep the attribution / licence notice","Release derivative source under the same licence"],
     ["Why a company might avoid it","(rarely avoided)","Can 'infect' proprietary code with openness"],
     ["Example projects","React (MIT); much of Apache's stack","Linux, Android core (GPL)"],
     ["Violation =","Dropping attribution → infringement","Shipping GPL code closed → infringement"]],
    per_page=5,widths=[2.2,2.4,2.4],fs=11,
    note="Both are real copyright licences with enforceable obligations — 'open' means 'licensed on conditions', not 'do whatever you like'.")
concept_apply("S15 · Concept 1 · [THEORY]","Open Source Code",
    "Nepali startups and government projects build on WordPress, Linux, and open frameworks to cut cost — which is exactly what open source is for. But the licences carry obligations: keep attribution for MIT/Apache code, and open your source if you distribute a GPL-based derivative. Honouring the licence is not optional politeness; it's the condition of the grant.",
    "\"Open source means free with no rules — I can use it however I like.\" Open source is copyright plus a licence, and the licence imposes real obligations (attribution, share-alike). Ignoring them is infringement — companies have been sued for shipping GPL code inside closed products.",
    "Open source software is licensed, not un-owned: it is copyright plus a licence granting rights to use, study, modify, and share. Permissive licences (MIT, Apache) require little beyond attribution; copyleft licences (GPL) require derivatives to be released open too. Violating either — dropping attribution, or closing GPL-derived code — is copyright infringement.",
    "open source · copyright + licence · permissive (MIT/Apache) · copyleft (GPL) · attribution · share-alike")

concept_understand("S15 · Concept 2 · [THEORY] [EXAMPLE]","Competitive Intelligence — ethical vs espionage",
    "Competitive intelligence (CI) is legally and ethically gathering PUBLIC information about competitors to inform strategy. It uses public, legal sources — websites, ads, public filings, job posts, trade shows. It becomes industrial ESPIONAGE when it involves theft, bribery, hacking, misrepresentation, or stealing trade secrets.",
    ["CI is normal, legal business homework — reading what a rival has already made public.",
     "The line is crossed by HOW you get the information, not by wanting it.",
     "Espionage: hacking systems, bribing staff, posing as someone else, or lifting trade secrets.",
     "Misrepresentation (lying about who you are to extract info) is a classic espionage tactic."],
    None,"CI reads the published playbook; espionage breaks into the locker room.",
    "~8 min. Analysing a rival's public annual report is CI; hacking their servers is espionage. The salesperson-posing-as-a-customer case is the sharp edge.")
add_table_slide("S15 · Concept 2 · examples","Competitive intelligence vs industrial espionage",
    ["Method","CI or espionage?","Why"],
    [["Reading a rival's public annual report / rates","CI","Public, legal source"],
     ["Studying competitors' ads and job postings","CI","Freely published information"],
     ["Walking a competitor's public trade-show booth","CI","Openly available to anyone"],
     ["Hacking a rival's servers for their data","Espionage","Illegal intrusion / theft"],
     ["Bribing a staffer for a customer list","Espionage","Theft of a trade secret via bribery"],
     ["Posing as a customer to extract secret pricing","Espionage","Misrepresentation to obtain confidential info"]],
    per_page=6,widths=[3.1,1.6,2.3],fs=11,
    note="The test is HOW you obtain it: public + honest = CI; theft, bribery, hacking, or lies = espionage (illegal and unethical).")
concept_apply("S15 · Concept 2 · [THEORY] [EXAMPLE]","Competitive Intelligence",
    "A Nepali bank studying competitors' published interest rates and branch networks is doing legitimate competitive intelligence. The same bank bribing a rival's staffer for a customer list, or breaching their systems, is industrial espionage — a crime. And a salesperson posing as a customer to extract a rival's secret pricing is espionage by misrepresentation, even though no system was hacked.",
    "\"If I can get the information, gathering it is fine.\" What matters is HOW you obtain it. Public, honest sources are fair game; theft, bribery, hacking, or lying about who you are turn research into espionage — illegal and unethical — regardless of how useful the information is.",
    "Competitive intelligence is the legal, ethical gathering of public information about competitors (websites, ads, filings, job posts, trade shows) to inform strategy. It becomes industrial espionage when the method involves theft, bribery, hacking, misrepresentation, or stealing trade secrets. The line is defined by how the information is obtained, not by the desire to have it.",
    "competitive intelligence · public sources · industrial espionage · theft/bribery/hacking/misrepresentation · the method defines it")

add_activity("S15 — 'CI or over the line?'  ·  ~5 min",
    ["In pairs (2 min): sort four intelligence-gathering acts into CI / espionage and name the deciding factor.",
     "Acts: scraping a rival's public price page; posing as a job applicant to learn internal plans; reading their public filings; bribing a contractor for designs.",
     "Take answers aloud (3 min).",
     "Close: the deciding factor is always HOW you got it — public + honest vs theft/lies/hacking."],
    "Public price page = CI (though check terms/scale); fake job applicant = espionage (misrepresentation); public filings = CI; bribing for designs = espionage. The scraping case is the useful grey area — discuss scale and terms of use.",
    "ACTIVITY [~5 min].")
add_quiz("S15 — Quick Check  ·  ~5 min",
    [("Q1.  GPL (copyleft) licences require that:","q"),
     ("a) you pay a fee   b) ✅ derivative works also be released as open source   c) you drop attribution   d) nothing","a"),
     ("     Why: copyleft's share-alike rule keeps derivatives open; closing GPL-derived code is infringement.","o"),
     ("Q2.  Gathering competitor info crosses into espionage when it involves:","q"),
     ("a) reading public ads   b) ✅ theft, bribery, hacking, or misrepresentation   c) visiting a trade show   d) reading filings","a"),
     ("     Why: the method defines it — dishonest or illegal means turn research into espionage.","o"),
     ("Discussion: is scraping a competitor's public website for prices ethical CI? Where would it cross the line?","o")],
    "QUIZ [~5 min]. Surface nuance: public data leans CI, but terms-of-service, scale, and any deception (fake accounts) can push it over the line.")
add_summary("S15 · Summary  ·  [~2 min]",
    ["Open source = copyright + a licence with real obligations; permissive (MIT/Apache) vs copyleft (GPL).",
     "Violating a licence (e.g. closing GPL-derived code, dropping attribution) is copyright infringement.",
     "Competitive intelligence is legal/public; it becomes espionage when the method is theft, bribery, hacking, or lies."],
    "You'll ship products built on open source (mind the licences — a GPL slip can force you to open your code or face a suit) and research competitors (stay on the public, honest side of the line). Both are everyday professional judgment calls.",
    "S16 — trademarks and cybersquatting close the unit.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S16
add_divider("Session 16 · Lecture hour 6 (of 6) — CLOSES UNIT 3","IP Issues: Trademark Infringement · Cybersquatting",
    "Someone registers daraz.com.np before Daraz does, or sells momos under a logo identical to a famous brand's — they grabbed a name, not code. Is a NAME really property? Trademarks say yes.",
    "OPENING HOOK [~5 min]. Draw out that brand identity is valuable property worth protecting. Agenda: trademarks & infringement → cybersquatting → the master 4-way IP comparison that ties the whole unit together.")

concept_understand("S16 · Concept 1 · [THEORY]","Trademark & Trademark Infringement",
    "A trademark is a sign, name, logo, or slogan that identifies the SOURCE of goods or services. Infringement is unauthorized use of a confusingly similar mark. Trademarks protect brand identity and prevent consumer confusion; they can last indefinitely with renewal, and are registered in Nepal at the Department of Industry.",
    ["The core purpose is preventing consumer confusion about who really made a product.",
     "A mark can last forever as long as it's used and renewed — unlike copyright and patents.",
     "Infringement doesn't need an identical copy — a confusingly SIMILAR mark is enough.",
     "Company registration and trademark registration are SEPARATE filings."],
    None,"A trademark protects the brand's identity — and the customer from confusion.",
    "~7 min. Counterfeit Goldstar shoes and Wai Wai packets are trademark infringement — the confusion (buyers think it's genuine) is the harm.")
add_table_slide("S16 · Concept 1 · examples","Trademark infringement — what crosses the line",
    ["Situation","Infringement?","Why"],
    [["Selling fake 'Goldstar' shoes with the logo","Yes","Uses the mark to pass off fakes as genuine"],
     ["Counterfeit 'Wai Wai' packets","Yes","Confuses buyers about the true source"],
     ["A momo stall using a near-identical famous logo","Yes","Confusingly similar mark → consumer confusion"],
     ["Your own original shop name & logo","No","Distinct mark; no confusion with others"],
     ["Naming a product with a common dictionary word","Usually no","Generic terms are weak/unprotectable marks"],
     ["Comparative ad naming a rival truthfully","Usually no","Nominative reference, not passing off"]],
    per_page=6,widths=[3.1,1.5,2.4],fs=11,
    note="The test is consumer confusion about SOURCE. Registered TM disputes in Nepal are filed at the Department of Industry.")
concept_apply("S16 · Concept 1 · [THEORY]","Trademark & Trademark Infringement",
    "Fake Goldstar shoes, counterfeit Wai Wai packets, and copycat momo/restaurant logos around Kathmandu are trademark infringement: they use a confusingly similar mark so buyers think they're getting the genuine brand. Well-known trademark disputes are filed at the Department of Industry under the Patent, Design and Trademark Act.",
    "\"Registering my company name means I own the trademark.\" Company registration and trademark registration are separate filings — registering a company doesn't secure the brand mark, and vice versa. To protect a brand identity you must register the trademark specifically.",
    "A trademark is a sign, name, logo, or slogan identifying the source of goods or services; infringement is unauthorized use of a confusingly similar mark. Trademarks protect brand identity and prevent consumer confusion, can last indefinitely with renewal, and are registered in Nepal at the DoI. Company registration is a separate filing from trademark registration.",
    "trademark · source identifier · confusingly similar · consumer confusion · indefinite with renewal · DoI · ≠ company registration")

concept_understand("S16 · Concept 2 · [THEORY] [EXAMPLE]","Cybersquatting",
    "Cybersquatting is registering a domain name matching someone else's trademark in bad faith — to resell it or divert traffic. It's resolved via the UDRP (ICANN's dispute process) for .com, or the local registry for .np. It's distinct from legitimate domain investing; typosquatting (misspelled lookalikes) is a close cousin.",
    ["The defining element is BAD FAITH — grabbing a known brand's name to profit from it.",
     "Legitimate domain investing (generic names, no target brand) is different and lawful.",
     "Typosquatting registers misspellings (e-sewa vs esewa) to catch mistyped traffic — often for phishing.",
     "Disputes: .com via UDRP; .np domains are managed by Mercantile (register.com.np)."],
    "s16_squat.png","Grabbing a brand's domain in bad faith to resell → cybersquatting.",
    "~8 min. Tie forward to Unit 7 phishing: a lookalike e-sewa.com.np domain is both cybersquatting and a phishing vector.")
add_table_slide("S16 · Concept 2 · examples","Cybersquatting vs legitimate — and the close cousins",
    ["Scenario","Verdict","Why"],
    [["Registering a Nepali bank's name as .com.np to resell it","Cybersquatting","Bad-faith grab of a known trademark"],
     ["Registering 'e-sewa.com.np' to mimic eSewa","Cybersquatting + phishing risk","Lookalike to divert/deceive users"],
     ["Registering a generic word like 'momos.com'","Legitimate","No target brand; generic term"],
     ["Buying/selling generic domains as investment","Legitimate","Domain investing, no bad-faith target"],
     ["Typosquatting 'gogle.com' to catch typos","Cybersquatting (typosquatting)","Bad-faith lookalike of a known mark"],
     ["Owning your OWN brand's domain","Legitimate","Rightful use of your own mark"]],
    per_page=6,widths=[3.2,1.7,2.1],fs=10.5,
    note="Bad faith toward a known brand is the deciding factor. .com disputes go to UDRP; .np disputes go through the local registry (Mercantile / register.com.np).")
concept_apply("S16 · Concept 2 · [THEORY] [EXAMPLE]","Cybersquatting",
    "A person registers a .com.np domain matching a famous Nepali brand and offers to sell it back for Rs 5 lakh — that's cybersquatting (bad-faith grab to ransom the name), not legitimate business, and the brand can challenge it through the .np registry. A lookalike 'e-sewa.com.np' is worse still: cybersquatting that doubles as a phishing trap.",
    "\"First to register a domain owns it fairly.\" Registration in BAD FAITH toward a known trademark is cybersquatting, not fair ownership — the brand can recover it via UDRP (.com) or the .np registry. Legitimate domain investing (generic names, no target brand) is a different, lawful activity.",
    "Cybersquatting is registering a domain matching someone else's trademark in bad faith, to resell it or divert traffic; typosquatting (misspelled lookalikes) is a close cousin often used for phishing. It is distinct from legitimate domain investing in generic names. Disputes are resolved via the UDRP for .com and through the local registry (Mercantile) for .np.",
    "cybersquatting · bad faith · typosquatting · UDRP · .np registry · vs legitimate domain investing")

concept_understand("S16 · Concept 3 · [THEORY]","Pulling It Together — the four IP types",
    "The whole unit in one frame: copyright protects EXPRESSION, patent protects an INVENTION, trade secret protects SECRET information, and trademark protects BRAND IDENTITY. Each differs in what it protects, how you acquire it, and how long it lasts.",
    ["Copyright: automatic on creation; protects expression; lasts life + 50 years.",
     "Patent: applied for and disclosed; protects a novel invention; ~20 years.",
     "Trade secret: kept confidential; protects secret info; unlimited while secret.",
     "Trademark: registered and renewed; protects brand identity; potentially forever."],
    None,"Expression · Invention · Secret · Brand — four protections, four different rules.",
    "~7 min. This is the master differentiator. Walk each row of the comparison table on the next slide as the unit's capstone.")
add_table_slide("S16 · Concept 3 · comparison","MASTER comparison — the four IP types side by side",
    ["","Copyright","Patent","Trade secret","Trademark"],
    [["What it protects","Original expression","A new invention (method)","Confidential info","Brand identity (name/logo)"],
     ["How you get it","Automatic on creation","Apply + disclose + 3 tests","Keep it secret (no filing)","Register (DoI) + renew"],
     ["How long it lasts","Life + 50 years","~20 years","While it stays secret","Indefinite with renewal"],
     ["Then what?","Public domain","Public domain","Gone if leaked/found","Lost if not used/renewed"],
     ["Nepal example","A pirated Kabaddi film","A DoI-registered device","Wai Wai's masala ratio","Fake Goldstar logo"]],
    per_page=5,widths=[1.7,1.9,1.9,1.9,1.9],fs=9.8,
    note="Capstone table for Unit 3: the four IP types differ by WHAT they protect, HOW you acquire them, and HOW LONG they last. Master this and you can classify any IP question.")
concept_apply("S16 · Concept 3 · [THEORY]","Pulling It Together — the four IP types",
    "One product can involve all four: a fintech app's code is COPYRIGHTED, a novel mechanism inside it might be PATENTED, its fraud-scoring algorithm is a TRADE SECRET, and its name and logo are TRADEMARKED. Classifying an IP question means asking which of the four — expression, invention, secret, or brand — is at stake.",
    "\"IP is basically all one thing.\" The four types protect different things, are acquired differently, and last different lengths of time — mixing them up gives wrong answers (e.g. 'patent your logo' or 'copyright your brand name'). Ask what is at stake: expression → copyright, invention → patent, secret → trade secret, brand → trademark.",
    "The four IP types are best understood side by side: copyright (expression, automatic, life + 50 yrs), patent (invention, applied-for + disclosed, ~20 yrs), trade secret (secret info, kept confidential, unlimited but fragile), and trademark (brand identity, registered + renewed, potentially forever). They differ by what they protect, how they're acquired, and how long they last — the unit's core differentiator.",
    "copyright (expression) · patent (invention) · trade secret (secret) · trademark (brand) · what/how/how-long")

add_activity("S16 — 'Name it and protect it'  ·  ~6 min",
    ["In pairs (2 min): you're launching a Nepali startup. For your product, name what each IP type covers.",
     "Which parts are copyright, patent (or not), trade secret, and trademark? What must you register on day one?",
     "Take 3 answers aloud (4 min); check each against the master comparison table.",
     "Close: a name + domain + trademark check is literally a day-one task — get it wrong and you rebrand or face a dispute."],
    "Strong answers: code = copyright (automatic); brand name/logo = trademark (must register at DoI + grab the domain); a secret algorithm = trade secret (NDA); patent usually N/A for pure software. Reward day-one trademark + domain awareness.",
    "ACTIVITY [~6 min].")
add_quiz("S16 — Quick Check  ·  ~5 min",
    [("Q1.  A logo or brand name that identifies a product's source is protected by:","q"),
     ("a) copyright   b) patent   c) trade secret   d) ✅ trademark","a"),
     ("     Why: trademarks protect source-identifying brand identity and prevent consumer confusion.","o"),
     ("Q2.  Registering a brand's domain in bad faith to resell it is:","q"),
     ("a) fair investing   b) ✅ cybersquatting   c) trademark licensing   d) fair use","a"),
     ("     Why: bad-faith registration of a known mark's domain is cybersquatting, resolvable via UDRP/.np registry.","o"),
     ("Discussion: if you register famousbrand.com.np before the brand does, should you be allowed to sell it to them?","o")],
    "QUIZ [~5 min]. Draw out bad faith vs legitimate investing — grabbing a KNOWN brand's name to ransom it is the line, and .np disputes go through the local registry.")
add_summary("S16 · Summary  ·  [~2 min]",
    ["Trademarks protect brand identity against confusingly similar use; company reg ≠ trademark reg.",
     "Cybersquatting is bad-faith domain grabbing (typosquatting is its cousin); resolved via UDRP or the .np registry.",
     "The four IP types differ by what they protect, how you acquire them, and how long they last (master table)."],
    "Naming a startup means a trademark + domain check on day one — get it wrong and you rebrand or face a dispute. And you'll classify IP questions constantly: knowing expression→copyright, invention→patent, secret→trade secret, brand→trademark is a core professional reflex.",
    "Unit 4 — ethical decisions in software development and IT organizations (whistle-blowing, safety, quality).",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 3 · Cheat Sheet","One-page revision reference",
    [("The four IP types","Copyright = expression (auto, life+50). Patent = invention (apply+disclose, ~20 yr). Trade secret = secret info (kept quiet, unlimited). Trademark = brand identity (register+renew, forever)."),
     ("Copyright (S11)","Protects EXPRESSION not idea; automatic on creation; fair use for education/news/criticism/parody; attribution ≠ permission."),
     ("Patent (S12)","3 tests: novelty + non-obviousness + industrial applicability. ~20 yrs, public, territorial. Software patents restricted → use copyright + trade secret."),
     ("Trade secret (S13)","Confidential info + reasonable secrecy (NDAs). Unlimited but fragile — no protection vs independent discovery / legal reverse engineering."),
     ("Plagiarism & reverse eng. (S14)","Plagiarism = ethical (pass off work); infringement = legal. Reverse engineering OK for interoperability/security/learning, not copying."),
     ("Open source, CI, trademark (S15–16)","Open source = copyright + licence (MIT/Apache permissive vs GPL copyleft). CI = public/legal; espionage = theft/bribery/hacking/lies. Cybersquatting = bad-faith domain grab.")])

add_glossary("Unit 3 · Glossary","Key terms — quick reference",
    [("Intellectual property (IP)","legal rights over creations of the mind."),
     ("Copyright","protects original expression fixed in form; automatic on creation."),
     ("Idea vs expression","copyright covers the expression, never the underlying idea."),
     ("Fair use","limited use for education, research, news, criticism, parody."),
     ("Public domain","status after copyright expires — free for all."),
     ("Patent","exclusive right over a new, useful, non-obvious invention (~20 yrs)."),
     ("Patentability tests","novelty, inventiveness (non-obviousness), industrial applicability."),
     ("Software patent","patent on a method/algorithm — restricted/contested."),
     ("Patent troll","acquires patents only to sue, not to build."),
     ("Territorial","a patent protects only in the country that granted it."),
     ("Trade secret","confidential info kept secret through reasonable effort."),
     ("NDA","non-disclosure agreement binding insiders to confidentiality."),
     ("Misappropriation","theft/breach of confidence of a trade secret (the actionable wrong)."),
     ("Plagiarism","passing off others' work/ideas as your own — an ethical offence."),
     ("Reverse engineering","analysing a product to learn how it works."),
     ("Clean-room","re-implementing from behaviour, not from the protected code."),
     ("Open source","code released under a licence (copyright + a licence)."),
     ("Permissive vs copyleft","MIT/Apache (use freely) vs GPL (derivatives stay open)."),
     ("Competitive intelligence","legally gathering public info on competitors."),
     ("Industrial espionage","gathering info via theft, bribery, hacking, or lies."),
     ("Trademark","a sign/name/logo identifying a product's source."),
     ("Trademark infringement","unauthorized use of a confusingly similar mark."),
     ("Cybersquatting","bad-faith registration of a brand's domain to resell/divert."),
     ("UDRP","ICANN process for resolving .com domain disputes.")])

# ============= CONSOLIDATED END-OF-UNIT QUIZ =============
add_divider("Unit 3 · Revision","Consolidated end-of-unit quiz",
    "Twelve MCQs across the whole unit (answers shown), then short-answer, applied-case, and discussion questions to work from the concept slides and Unit3_material.md.",
    "Use as a 15–20 min in-class quiz or take-home review.")
add_quiz("Section A — Multiple choice (answers shown)",
    [("1.  Copyright protects   →  ✅ the expression, not the underlying idea","a"),
     ("2.  In Nepal, copyright generally lasts   →  ✅ the author's life + 50 years","a"),
     ("3.  NOT a patentability test   →  ✅ being widely popular (vs novelty/non-obviousness/usefulness)","a"),
     ("4.  A typical patent term is about   →  ✅ 20 years","a"),
     ("5.  A trade secret stays protected   →  ✅ as long as it remains secret","a"),
     ("6.  The main tool to protect a secret with employees is   →  ✅ an NDA / confidentiality agreement","a"),
     ("7.  Plagiarism is primarily a violation of   →  ✅ academic / ethical integrity","a"),
     ("8.  Reverse engineering is generally legal for   →  ✅ interoperability / security research","a"),
     ("9.  GPL (copyleft) licences require   →  ✅ derivative works also be released as open source","a"),
     ("10.  Competitive info-gathering becomes espionage with   →  ✅ theft, bribery, hacking, or misrepresentation","a"),
     ("11.  A brand name/logo identifying a product's source is   →  ✅ a trademark","a"),
     ("12.  Registering a brand's domain in bad faith to resell it is   →  ✅ cybersquatting","a")],
    "Consolidated quiz Section A.",compact=True)
add_quiz("Sections B–D — short answer, applied case & discussion",
    [("Section B — Short answer","q"),
     ("13. Define a trade secret + 2 protection methods.   14. Explain fair use with one Nepal example.   15. Difference between patent and trade secret.","o"),
     ("16. What makes reverse engineering legal vs illegal?   17. What is cybersquatting and how is a .np dispute resolved?","o"),
     ("Section C — Applied case","q"),
     ("18. A Kathmandu startup invents an algorithm — recommend copyright / patent / trade secret / open source and justify.","o"),
     ("19. Classify each as plagiarism / copyright infringement / fair use / none: (a) quoting 2 cited lines of a poem (b) uploading a full movie (c) copy-pasting a senior's report (d) building a rival bill-split app with your own code.","o"),
     ("Section D — Discussion","q"),
     ("20. Should Nepal allow software patents? Weigh innovation incentives against harm to local startups.","o")],
    "Consolidated quiz Sections B–D. Model answers on the concept slides and in Unit3_material.md. Q19: (a) fair use, (b) infringement, (c) plagiarism (+infringement), (d) none.",compact=True)

# ---- close ----
add_title("End of Unit 3  ·  IT 246",
          "S11–S16 complete: IP overview & copyright · patents & the software-patent debate · trade secrets · plagiarism & reverse engineering · open source & competitive intelligence · trademarks & cybersquatting",
          "Built to COURSE_MATERIAL_STANDARD.md incl. the §7A depth rule · comparison & concrete-example tables throughout · "
          "self-contained, PDF-safe · Next: Unit 4 — Ethics in Software Development & IT Organizations.")

_add_page_numbers()
save("IT246_Unit3.pptx")
