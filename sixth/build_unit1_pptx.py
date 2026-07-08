#!/usr/bin/env python3
"""IT246 (sixth) Unit 1 deck — An Overview of Ethics (S1–S5), rebuilt to
COURSE_MATERIAL_STANDARD.md INCLUDING the §7A depth rule: every confusable set is a comparison
table, every 'X vs not-X' concept a concrete-example table, claims get scaffolding tables, plus
payoff tables — each table on its OWN slide, paginated, never squeezed. Generous slide count by
design. Diagrams in images/. Run: python3 build_unit1_pptx.py -> IT246_Unit1.pptx
"""
from deckkit import *

# ============================================================
#                        BUILD
# ============================================================
add_title("Unit 1 — An Overview of Ethics",
          "IT 246: IT Ethics & Cybersecurity  ·  BIM 6th Semester  ·  Sessions S1–S5",
          "Self-contained slides with depth: every concept grounded in comparison & concrete-example TABLES "
          "(Nepal / IT localised) — no abstraction without instances. Exports to PDF with no information lost.")

add_outcomes("Unit 1 — Learning Outcomes","overview  ·  s1–s5",
    "By the end of this unit, you will be able to:",
    ["Define ethics and distinguish it from morals, law, and etiquette (S1)",
     "Explain ethics in the business world and Corporate Social Responsibility (S1–S2)",
     "Describe how organizations foster CSR and improve business ethics (S2–S3)",
     "Apply a structured 5-step ethical decision-making process to a dilemma (S4)",
     "Explain why ethics matters specifically in Information Technology (S5)"],
    "This is Unit 1 of IT 246. It is the reasoning foundation for every later unit — IT workers/users, intellectual property, cybersecurity, digital forensics, and Nepal's cyber law.")

add_roadmap("Unit 1 — Roadmap","Where each session fits (S1–S5)",
    ["S1   What is ethics? · ethics in the business world",
     "S2   Corporate Social Responsibility (CSR)",
     "S3   Improving business ethics (systems, not posters)",
     "S4   Ethical decision-making (5 steps · 4 lenses)",
     "S5   Ethics in Information Technology (closes Unit 1)"],
    ["Unit 2   Ethics for IT workers & users",
     "Unit 3   Intellectual property",
     "Units 5–8   Cybersecurity & digital forensics",
     "Unit 9   Cyber law in Nepal"])

# ============================================================ S1
add_divider("Session 1 · Lecture hour 1 (of 5)","What is Ethics? · Ethics in the Business World",
    "Three cases: sharing one paid Netflix/Canva login among 8; taking 'chiya kharcha' to push a file up the pile; dumping e-waste in the river at night. Vote 'which are illegal?' then 'which are unethical?' — the counts won't match. That mismatch is the whole lesson.",
    "OPENING HOOK [~5 min]. Run the two votes; don't resolve the scenarios. Agenda: ethics vs law → ethics in business → why good companies still go wrong.")

concept_understand("S1 · Concept 1 · [THEORY]","Ethics, Morals, Law & Etiquette — four words people mix up",
    "Four related ideas people use interchangeably — a professional must not. Ethics = a code of right/wrong owned by a GROUP. Morals = an INDIVIDUAL's personal beliefs. Law = rules the STATE enforces. Etiquette = social MANNERS.",
    ["Ethics is shared (a profession, a company, a society can each have one).",
     "Morals are personal (family, religion, upbringing) — two ethical people can differ.",
     "Law is codified and backed by force, but slow and can't cover everything.",
     "Etiquette breaches are rude, not deeply wrong. They usually overlap — the cases that matter are where they PULL APART."],
    None,"Law = must; ethics = should; morals = I believe; etiquette = polite.",
    "~8 min. Full comparison table on the next slide; spend time on how the four RELATE, not just definitions.")
add_table_slide("S1 · Concept 1 · comparison","Ethics vs Morals vs Law vs Etiquette — at a glance",
    ["Concept","Meaning","Source","Who decides","If broken","Example"],
    [["Ethics","Shared standards of right/wrong for a group, profession, or society","Professional codes, organizations, society","Professional bodies / organizations / society","Loss of trust, disciplinary action, suspension, lost reputation","A doctor shares a patient's confidential records → disciplinary action, possible loss of licence"],
     ["Morals","An individual's personal beliefs about right and wrong","Family, religion, culture, upbringing, personal values","The individual","Personal guilt, regret, conflict with one's conscience","Returning a lost wallet because keeping it feels wrong, even if no one would know"],
     ["Law","Official rules created and enforced by the government","Constitution, legislation, regulations, courts","Government (legislature and courts)","Fines, imprisonment, community service, legal penalties","Driving under the influence is illegal → arrest, fine, licence suspension"],
     ["Etiquette","Social rules of politeness and good manners","Social customs, traditions, cultural norms","Society and culture","Seen as rude/impolite; usually no legal or professional penalty","Using your phone during a formal meeting is considered poor manners"]],
    per_page=4,widths=[1.1,2.4,2.0,1.9,2.2,3.0],fs=10.5,
    note="Same situation can sit in several columns: a bribe is illegal AND unethical; queue-jumping is unethical but legal; left-hand at a feast is only etiquette.")

concept_apply("S1 · Concept 1 · [THEORY]","Ethics, Morals, Law & Etiquette",
    "In Nepal: paying a bribe ('ghus') is illegal AND unethical; jumping a government-office queue via 'source-force' is unethical but not illegal; eating with the left hand at a feast is only an etiquette breach. The same three cases fall in three different places.",
    "\"If it's legal, it's ethical.\" The law is the FLOOR, not the ceiling — the minimum society tolerates, not the maximum you should aim for. History is full of things that were legal and deeply wrong.",
    "Ethics is a shared code of right/wrong owned by a group, profession, or society; morals are an individual's personal beliefs; law is the state's enforced rules with penalties; etiquette is social manners. They overlap, but the important cases are where they diverge — and 'legal' is never the end of an ethical question.",
    "ethics (group code) · morals (personal) · law (state-enforced) · etiquette (manners) · 'law is the floor, not the ceiling'")

add_table_slide("S1 · examples","Ethical vs Unethical behaviour — by situation",
    ["Situation","Ethical behaviour","Unethical behaviour"],
    [["Patient confidentiality","A doctor keeps a patient's records private","A doctor shares patient information without permission"],
     ["Academic research","A researcher reports accurate results","A researcher fabricates or falsifies data"],
     ["Engineering","An engineer reports a safety flaw in a design","An engineer hides the flaw to save money or time"],
     ["Accounting","An accountant reports records honestly","An accountant manipulates financial statements"],
     ["Business","A company advertises products truthfully","A company uses misleading ads to deceive customers"],
     ["Software development","A developer protects users' personal data","A developer secretly sells user data for profit"],
     ["Artificial intelligence","A developer works to reduce bias in AI","A developer knowingly ships a discriminatory system"],
     ["Procurement","A purchasing officer selects suppliers fairly","A purchasing officer accepts bribes to award contracts"],
     ["Public service","An officer serves citizens impartially","An officer demands a bribe for faster service"],
     ["Recruitment","An HR manager hires on qualifications","An HR manager hires relatives regardless of merit (nepotism)"]],
    per_page=6,widths=[1.5,2.6,2.9],fs=11.5)

add_table_slide("S1 · examples","Moral vs Immoral behaviour (personal beliefs)",
    ["Situation","Moral behaviour","Immoral behaviour"],
    [["Finding a lost wallet","Return it with the money inside","Keep it because no one is watching"],
     ["Telling the truth","Admit a mistake even if punished","Lie to avoid trouble"],
     ["Cheating in an exam","Study honestly and earn your grade","Cheat to get higher marks"],
     ["Returning extra change","Give back money handed to you by mistake","Keep it knowing it was an error"],
     ["Standing up for others","Defend someone being bullied","Stay silent because it's easier"],
     ["Keeping promises","Fulfil a promise to a friend","Break it for personal convenience"],
     ["Helping others","Help an elderly person cross the road","Ignore someone who clearly needs help"],
     ["Environmental care","Avoid littering because nature matters","Litter because you don't think it matters"]],
    per_page=6,widths=[1.6,2.7,2.7],fs=11.5,
    note="Morals are personal — driven by individual values, not by a group's code or the state's law.")

add_table_slide("S1 · examples","Lawful vs Illegal behaviour — and the consequence",
    ["Situation","Lawful","Illegal","Possible consequence"],
    [["Traffic","Stop at a red light","Drive through a red light","Fine, licence points/suspension"],
     ["Taxation","Pay taxes as required","Evade taxes / file false returns","Fines, penalties, imprisonment"],
     ["Theft","Respect others' property","Steal money or belongings","Arrest, fine, imprisonment"],
     ["Copyright","Use content with a licence","Distribute pirated media/software","Fines, lawsuits, criminal penalties"],
     ["Cybercrime","Access only authorized systems","Hack an account or network","Criminal charges, fines, imprisonment"],
     ["Environment","Dispose of hazardous waste legally","Dump toxic waste into rivers","Heavy fines, cleanup costs, jail"],
     ["Fraud","Provide truthful information","Use deception for financial gain","Prosecution and imprisonment"],
     ["Employment","Pay at least the legal minimum wage","Refuse legally required wages","Government penalties, legal action"]],
    per_page=6,widths=[1.3,2.3,2.3,2.3],fs=11,
    note="Law adds a distinctive feature the other three lack: state-enforced penalties.")

add_table_slide("S1 · examples","Good vs Poor Etiquette — and the social cost",
    ["Situation","Good etiquette","Poor etiquette","Possible cost"],
    [["Greeting","Greet people politely","Ignore someone who greets you","Seen as rude/unfriendly"],
     ["Queueing","Wait your turn","Cut in front of others","Annoyance, embarrassment"],
     ["Phone use","Silence it in meetings/class","Take loud calls during a lecture","Disturbs others, appears disrespectful"],
     ["Interrupting","Let people finish speaking","Cut people off mid-sentence","Others feel disrespected"],
     ["Punctuality","Arrive on time","Arrive late without informing","Seen as unreliable"],
     ["Public transport","Offer your seat to those in need","Refuse when someone clearly needs it","Seen as inconsiderate"],
     ["Online","Be respectful in comments","Use insults, offensive language, spam","Others block or report you"],
     ["Workplace","Respect others' space/belongings","Borrow things without asking","Tension, loss of trust"]],
    per_page=6,widths=[1.4,2.3,2.4,2.2],fs=11,
    note="Breaking etiquette is rude, not deeply wrong — usually no legal or professional penalty, only a social one.")

concept_understand("S1 · Concept 2 · [EXAMPLE]","The Legal / Ethical Grid — two axes, four quadrants",
    "Because legal and ethical are separate questions, every action sits on a 2×2 grid: Legal↔Illegal on one axis, Ethical↔Unethical on the other. Four quadrants result.",
    ["Legal + Ethical — the easy quadrant (pay taxes honestly; keep a promise).",
     "Legal + Unethical — technically allowed, clearly wrong (tax loophole; queue-jumping). MOST scandals live here.",
     "Illegal + Ethical — rare and debated (justified civil disobedience; whistle-blowing that breaks an NDA).",
     "Illegal + Unethical — the obvious-wrong quadrant (a bribe; leaking private data)."],
    "s1_grid.png","The dangerous quadrant is legal-but-unethical — only your judgment stops you.",
    "~6 min. Fill the grid live, asking the class for each cell; place the 'chiya kharcha' bribe (bottom-right) and the shared login (argue it).")
concept_apply("S1 · Concept 2 · [EXAMPLE]","The Legal / Ethical Grid",
    "Place the hook's shared streaming login: it's arguably legal-but-unethical (a grey contract violation) — let the class argue which quadrant. The 'chiya kharcha' bribe is clearly illegal-and-unethical (bottom-right).",
    "\"Wrong things are always illegal.\" No — the legal-but-unethical quadrant is full of everyday, perfectly-legal harm. That quadrant is exactly what this course trains you to handle.",
    "The legal/ethical grid plots an action on two independent axes (legal↔illegal, ethical↔unethical), giving four quadrants. The critical one is legal-but-unethical — technically allowed but clearly wrong — because nothing external stops you there; only your own judgment does.",
    "legal/ethical grid · four quadrants · legal-but-unethical (the danger zone) · judgment call")

add_table_slide("S1 · recall","The four concepts — one-line recall table",
    ["Concept","Main focus","Example question it answers"],
    [["Ethics","What should members of this profession/group do?","Is this professionally acceptable?"],
     ["Morals","What do I personally believe is right or wrong?","Does this align with my values?"],
     ["Law","What does the government require or prohibit?","Is this legal?"],
     ["Etiquette","What is considered polite and socially appropriate?","Is this good manners?"]],
    per_page=4,widths=[1.2,3.0,3.0],fs=12.5)

concept_understand("S1 · Concept 3 · [THEORY]","Ethics in the Business World",
    "Business ethics = applying ethical standards to commercial conduct. Business is special because it serves MANY stakeholders at once (customers, staff, society, owners) whose interests conflict — so the central tension is short-term profit vs long-term trust.",
    ["Customers can't verify most claims (does the medicine work? is my data safe?) → business runs on TRUST.",
     "Trust is slow to build, instant to lose — unethical shortcuts spend a years-long reserve.",
     "Nepal: in a festival shortage, Shop A triples prices (wins today); Shop B holds (longer queue every Dashain after).",
     "Good ethics is often good business — just on a longer clock."],
    None,"Profit is quarterly; trust compounds for years.",
    "~8 min. Walk the two-shop example fully; then the trekking-agency mini case (who bears the hidden cost?).")
add_table_slide("S1 · Concept 3 · scaffolding","A business serves many stakeholders — who wants what",
    ["Stakeholder","What they want from the business"],
    [["Customers","Quality products, fair prices, safety, honesty"],
     ["Employees","Fair wages, safe working conditions, respect"],
     ["Owners / shareholders","Profit, business growth, return on investment"],
     ["Suppliers","Fair contracts and timely payments"],
     ["Government","Compliance with laws and payment of taxes"],
     ["Society & community","Environmental responsibility, ethical behaviour, contribution"]],
    per_page=6,widths=[1.6,4.4],fs=13,
    note="These wants conflict — maximising this quarter's profit can harm customers or staff. Business ethics is managing that conflict.")
add_table_slide("S1 · Concept 3 · scaffolding","The central tension: short-term profit vs long-term trust",
    ["Short-term profit","Long-term trust"],
    [["Increase revenue quickly","Build lasting customer relationships"],
     ["Maximise immediate gains","Earn customer loyalty and reputation"],
     ["May involve ethical shortcuts","Requires honesty and fairness"]],
    per_page=3,widths=[1,1],fs=13.5,
    note="Shop A vs Shop B: the price-gouger wins the festival; the fair shop wins the decade.")
add_table_slide("S1 · Concept 3 · payoff","Why ethics pays — practice → business benefit",
    ["Ethical practice","Business benefit"],
    [["Honest advertising","Builds customer confidence"],
     ["Fair pricing","Encourages customer loyalty"],
     ["Paying employees fairly","Increases motivation and retention"],
     ["Protecting customer data","Strengthens trust and privacy"],
     ["Selling safe, quality products","Improves reputation"],
     ["Environmental responsibility","Supports sustainable growth"],
     ["Transparent communication","Reduces disputes, builds credibility"]],
    per_page=7,widths=[1.4,1.6],fs=13,
    note="Good ethics is not a cost centre — each practice buys a concrete, compounding return.")
concept_apply("S1 · Concept 3 · [THEORY]","Ethics in the Business World",
    "A trekking agency hides a current route safety risk to keep a booking. The hidden cost lands on the client (safety), the agency (reputation, lawsuits), AND the whole Nepali tourism sector (one accident scares off thousands of future tourists). One shortcut, an industry's loss.",
    "\"Ethics slows business down.\" Ethics is the brakes that let a business move FAST safely — spend the trust reserve on shortcuts and you don't speed, you crash (reputation collapse).",
    "Business ethics applies ethical standards to commercial conduct. Because a business serves conflicting stakeholders, its core tension is short-term profit vs long-term trust; since customers can't verify most claims, business runs on trust, which is slow to build and instant to lose. Ethical conduct is usually good business on a longer horizon.",
    "business ethics · stakeholders · profit vs trust · trust is slow to build, instant to lose")

concept_understand("S1 · Concept 4 · [THEORY]","Why Good People & Businesses Still Go Wrong",
    "Most misbehaviour comes from ordinary people under predictable PRESSURE — not 'bad people'. Because it is situational, good systems and culture can prevent it (which is what S2 and S3 build).",
    ["Results pressure — 'hit the target or you're out' crowds out the ethics.",
     "'Everyone does it' — normalization makes wrong feel normal.",
     "Weak oversight — nobody watching, so cutting corners feels free.",
     "Diffusion of responsibility — 'I just followed the process / my manager decided.'"],
    None,"Ethics fails are usually situational, not personal — so fix the situation.",
    "~7 min. Correct the 'bad apples' assumption; deliver the brakes analogy with conviction.")
concept_apply("S1 · Concept 4 · [THEORY]","Why Good People & Businesses Still Go Wrong",
    "A junior employee fudges one report under a manager's 'just this once' pressure, in an office where 'everyone rounds the numbers'. No villain — just results pressure + normalization + diffusion of responsibility. Change those conditions and the behaviour changes.",
    "\"We just need to hire good people.\" Good people misbehave under bad systems. You don't only hire virtue — you build conditions where the ethical choice is the easy default.",
    "Unethical behaviour is mostly situational, driven by results pressure, normalization ('everyone does it'), weak oversight, and diffusion of responsibility — not by inherently bad people. Because it is situational, ethical systems and culture (leadership, codes, reporting, consequences) prevent it.",
    "situational (not 'bad apples') · results pressure · normalization · weak oversight · diffusion of responsibility")

add_activity("S1 — 'Find the grey area'  ·  ~6 min",
    ["In pairs (2 min): invent ONE act that is legal-but-unethical and ONE illegal-but-arguably-ethical.",
     "Draw from Nepali daily life or IT.",
     "Take 4–5 answers aloud (3 min); place each on the 2×2 grid.",
     "Close (1 min): notice how EASY legal-but-unethical was to find — that's the quadrant this course trains."],
    "Seeds if stuck: selling legally-collected user data (legal, unethical); a politician's legal conflict of interest; pirating unaffordable software (illegal, students argue ethical). The ease of finding legal-but-unethical cases is the point.",
    "ACTIVITY [~6 min].")
add_quiz("S1 — Quick Check  ·  ~5 min",
    [("Q1.  An action that is legal but still wrong is best described as:","q"),
     ("a) illegal   b) ✅ unethical   c) good etiquette   d) a moral duty","a"),
     ("Q2.  A profession's written code of conduct is an example of:","q"),
     ("a) personal morals   b) etiquette   c) ✅ ethics (a group code)   d) law","a"),
     ("Discussion: name one thing legal in Nepal you consider unethical — which grid quadrant is it in?","o")],
    "QUIZ [~5 min].")
add_summary("S1 · Summary  ·  [~2 min]",
    ["Ethics = a group's code of right/wrong; distinct from morals (personal), law (state-enforced), etiquette (manners).",
     "Legal ≠ ethical — the law is the floor, not the ceiling; watch the legal-but-unethical quadrant.",
     "Business ethics trades short-term profit against long-term trust; misbehaviour is situational, so systems and culture fix it."],
    "Every job offer comes with a code of conduct, and employers check your online reputation before the interview. Recruiters literally ask 'tell me about an ethical dilemma' — the grey-area judgment you practised today is a tested professional skill.",
    "S2 — when companies act for society's benefit: Corporate Social Responsibility (CSR).",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S2
add_divider("Session 2 · Lecture hour 2 (of 5)","Corporate Social Responsibility (CSR)",
    "When Ncell funds a rural school, a bank runs a tree-planting drive, or a company sponsors flood relief — is that generosity, clever marketing, or a responsibility they actually OWE society? What if it's all three — and what if society can legitimately expect it?",
    "OPENING HOOK [~5 min]. Keep the cynicism ('it's just marketing') alive as a thread for the greenwashing activity. Agenda: CSR → Carroll's pyramid → stakeholder theory → fostering ethics.")

concept_understand("S2 · Concept 1 · [THEORY]","What CSR Means",
    "Corporate Social Responsibility (CSR) = a company's DUTY to act for the benefit of society, not only its shareholders. The key word is duty: a business owes something to the society that lets it operate (using public infrastructure, workers, resources, and trust).",
    ["Contrast the old view — 'the only job of business is profit'.",
     "Modern consensus: profit AND responsibility, together.",
     "In Nepal, part of CSR is regulated, not optional (see the pyramid slide).",
     "CSR is embedded in daily operations, not just donations."],
    None,"CSR = a duty owed to society, not optional charity.",
    "~7 min. Stress 'duty' — society can legitimately expect it, not merely hope for it.")
concept_understand("S2 · Concept 2 · [THEORY]","Carroll's CSR Pyramid — four levels of responsibility",
    "Carroll's pyramid stacks a company's responsibilities in order: Economic → Legal → Ethical → Philanthropic. Lower layers must hold before upper ones mean anything.",
    ["Economic (base) — be profitable; survival funds everything above.",
     "Legal — obey the law (society's codified minimum).",
     "Ethical — do what's right beyond the law (the S1 'above the floor' idea).",
     "Philanthropic (top) — give back (donations, community programs)."],
    "s2_pyramid.png","Be profitable → legal → ethical → give back — in that order.",
    "~7 min. A company donating to charity while underpaying staff is doing CSR backwards — image without foundation.")
add_table_slide("S2 · Concept 2 · comparison","Carroll's four levels — meaning, example, Nepal",
    ["Level","What it means","Example","Nepal context"],
    [["Economic (base)","Be profitable and viable","Earn enough to pay staff and reinvest","A bank must be solvent before it can fund anything"],
     ["Legal","Obey all laws and regulations","Follow labour, tax, environmental law","Comply with Nepal Rastra Bank / government rules"],
     ["Ethical","Do what's right beyond the law","Fair wages, honest marketing, safe products","Not exploiting a legal loophole that harms customers"],
     ["Philanthropic (top)","Give back to the community","Donations, scholarships, relief, tree-planting","Telecom rural-coverage & education programs"]],
    per_page=4,widths=[1.3,2.2,2.5,2.6],fs=11.5,
    note="Nepal Rastra Bank directs commercial banks to allocate part of profit to CSR — so here, CSR is partly built into regulation, not just goodwill.")
concept_apply("S2 · Concept 2 · [THEORY]","Carroll's CSR Pyramid",
    "Nepal Rastra Bank directs commercial banks to allocate a portion of profit to CSR activities — so part of Nepali CSR isn't optional charity, it's built into how the banking sector is regulated. Telecoms similarly run rural-coverage and education programs.",
    "\"CSR is just charity / a PR stunt.\" Real CSR is responsibility embedded in operations — fair wages, clean production, honest marketing, safe products. Donations are the visible tip; the base is how you run the business every day.",
    "CSR is a company's duty to act for society's benefit, not only shareholders'. Carroll's pyramid orders four responsibilities — economic (be profitable), legal (obey the law), ethical (do right beyond the law), and philanthropic (give back) — with lower layers foundational to the upper ones.",
    "CSR · duty to society · Carroll's pyramid (economic→legal→ethical→philanthropic) · embedded-not-decorative")

concept_understand("S2 · Concept 3 · [THEORY]","Stakeholder Theory — who is a business accountable to?",
    "Central question: to whom does a company answer? The narrow answer is shareholders (owners). Stakeholder theory widens it to EVERYONE materially affected — customers, employees, suppliers, community, environment, government, and owners.",
    ["Under a stakeholder view, a decision great for owners but harmful to the community is a FAILURE.",
     "Costs pushed onto stakeholders are hidden, not absent (health costs, lawsuits, lost social licence).",
     "Two lenses give opposite verdicts on the same decision (see the table).",
     "'Ethics fails when we count only the stakeholders who show up on the balance sheet.'"],
    "s2_stakeholders.png","Count everyone affected — not just those on the balance sheet.",
    "~8 min. Work the polluting-factory mini case through both lenses.")
add_table_slide("S2 · Concept 3 · comparison","One decision, two lenses — the polluting factory",
    ["Question","Shareholder lens","Stakeholder lens"],
    [["Who counts?","The owners","Everyone materially affected"],
     ["Factory is profitable but pollutes a village's water","Success — profits are up","Failure — the village is harmed"],
     ["Are the costs real?","Ignored — off the balance sheet","Real but hidden: health costs, lawsuits, lost licence"],
     ["Verdict","Great result","Ethical failure"]],
    per_page=4,widths=[1.8,2.1,2.6],fs=11.5,
    note="Same facts, opposite conclusions — which is why 'whose interests count?' is the first ethical question in business.")
concept_apply("S2 · Concept 3 · [THEORY]","Stakeholder Theory",
    "A factory highly profitable for owners but quietly polluting a village's drinking water is a shareholder-lens success and a stakeholder-lens failure. The health costs and future lawsuits are real — just not yet on the balance sheet.",
    "\"A company only answers to its owners.\" Stakeholder theory: it answers to everyone it materially affects. Ignoring non-owner stakeholders doesn't remove the cost — it hides it until it returns as lawsuits, boycotts, or lost licence to operate.",
    "Stakeholder theory holds that a business is accountable to all groups materially affected by it — customers, employees, suppliers, community, environment, government, and owners — not shareholders alone. A decision that profits owners while harming another stakeholder is an ethical failure, because the cost is hidden, not absent.",
    "stakeholder theory · shareholder vs stakeholder lens · social licence to operate · hidden costs")

concept_understand("S2 · Concept 4 · [THEORY]","Fostering CSR & an Ethical Culture",
    "Good ethics is BUILT, not wished. Four levers turn CSR from a slogan into practice.",
    ["Tone from the top — staff copy what leaders DO, not what posters say.",
     "A clear, public code of ethics — turns vague values into specific expectations.",
     "An ethical culture — raising a concern is rewarded, not punished; doing right is the easy path.",
     "Social-responsibility reporting — publishing your impact creates accountability you can't quietly walk back."],
    None,"Trust compounds like interest; one scandal is a withdrawal that empties the account.",
    "~7 min. Deliver the 'trust compounds' line; sets up the greenwashing activity.")
add_table_slide("S2 · Concept 4 · comparison","Genuine CSR vs Greenwashing — apply the test",
    ["Test question","Genuine CSR","Greenwashing"],
    [["Does daily operation match the message?","Yes — the ad reflects how they actually run","No — the ad contradicts the behaviour"],
     ["Where does the responsibility live?","Embedded in wages, production, products","Only in the marketing / a one-off donation"],
     ["Bank: 'we care about farmers'","Loan terms are genuinely fair to farmers","Loan terms quietly crush the same farmers"],
     ["What survives scrutiny?","Consistent record over years","A campaign that falls apart on a closer look"]],
    per_page=4,widths=[2.2,2.4,2.4],fs=11.5,
    note="The one-line test: does the company's everyday operation match its CSR message, or does the ad contradict the behaviour?")
concept_apply("S2 · Concept 4 · [THEORY]","Fostering CSR & an Ethical Culture",
    "A bank advertising 'we care about farmers' while its loan terms crush them is greenwashing — the message contradicts the operation. A genuine CSR claim survives the test: daily practice matches the ad.",
    "\"A good CSR campaign proves a company is ethical.\" The ad is not the evidence — the operation is. Apply the test: does everyday behaviour match the message?",
    "CSR and an ethical culture are built through tone from the top (leaders' actions), a clear public code, a culture that rewards raising concerns, and social-responsibility reporting. Genuine CSR is embedded in operations; greenwashing lives only in marketing and fails the 'does daily operation match the message?' test.",
    "tone from the top · code of ethics · ethical culture · CSR reporting · greenwashing test")

add_activity("S2 — 'Genuine or greenwashing?'  ·  ~6 min",
    ["In pairs (2 min): name ONE Nepali company's CSR activity you've seen.",
     "For 2–3 examples aloud (4 min), the class judges: genuine responsibility or image-building?",
     "Apply the test: does the company's everyday operation match the CSR message?",
     "Flag contradictions (e.g. 'we care about farmers' vs crushing loan terms)."],
    "The test to apply every time: match the message against the daily operation. A tree-planting ad from a firm that pollutes is greenwashing; consistent fair practice backing a modest claim is genuine.",
    "ACTIVITY [~6 min].")
add_quiz("S2 — Quick Check  ·  ~5 min",
    [("Q1.  The BASE of Carroll's CSR pyramid is:","q"),
     ("a) philanthropic   b) ethical   c) legal   d) ✅ economic responsibility","a"),
     ("Q2.  Stakeholders of a company include all of these EXCEPT:","q"),
     ("a) employees   b) customers   c) ✅ only the shareholders   d) the local community","a"),
     ("Discussion: a Nepali company doing visible CSR — genuine or image-building? Apply the test.","o")],
    "QUIZ [~5 min].")
add_summary("S2 · Summary  ·  [~2 min]",
    ["CSR = a company's duty to society (Carroll: economic → legal → ethical → philanthropic).",
     "Stakeholders are everyone affected, not just owners; count the costs that don't show on the balance sheet.",
     "Good ethics is built through leadership, culture, codes, and transparency — genuine CSR beats greenwashing."],
    "CSR shapes which companies attract talent and investment and which face boycotts. As employee, consumer, and future manager you'll make and judge these choices — the pyramid lets you build CSR that's real, not decorative.",
    "S3 — the systems that turn ethical values into actual behaviour: improving business ethics.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S3
add_divider("Session 3 · Lecture hour 3 (of 5)","Improving Business Ethics",
    "A company hires consultants, writes an inspiring 'Code of Ethics', prints it on glossy paper, frames it in reception… and behaves exactly as before. Why didn't the document change anything?",
    "OPENING HOOK [~5 min]. Pull answers together: a value written down is not a value practised. Ethics needs systems, not posters. Agenda: values→behaviour → program components → measuring & sustaining.")

concept_understand("S3 · Concept 1 · [THEORY]","From Values to Behaviour",
    "An ethics program = the set of SYSTEMS that turn stated values into actual behaviour. Every company says it values integrity; the program is what makes that true on a normal Tuesday under deadline pressure.",
    ["Take two companies with the IDENTICAL code.",
     "In one, leaders visibly follow it and violations have consequences.",
     "In the other, leaders quietly break it.",
     "Same document, opposite cultures — the document was never the cause; the system around it was."],
    None,"A framed code changes nothing; the system around it changes everything.",
    "~7 min. The 'same code, opposite cultures' contrast is the whole point.")
add_table_slide("S3 · Concept 1 · comparison","Same code, opposite outcomes — values written vs practised",
    ["Aspect","Company A (values practised)","Company B (values on the wall)"],
    [["The code","Specific and enforced","Glossy but ignored"],
     ["Leaders","Visibly follow it","Quietly break it"],
     ["Violations","Have real consequences","Overlooked, especially at the top"],
     ["Reporting a concern","Safe and rewarded","Risky — you stay quiet"],
     ["Result","Ethical behaviour is the default","The code is decoration; people ignore it"]],
    per_page=5,widths=[1.6,2.5,2.5],fs=11.5,
    note="An unenforced code can be WORSE than none — it signals the rules are for show, teaching everyone to ignore them.")
concept_apply("S3 · Concept 1 · [THEORY]","From Values to Behaviour",
    "Two Nepali offices adopt the same 'integrity' code. In one, a manager who takes a kickback is dismissed; in the other, seniors are quietly excused. Within months the second office's staff have learned the code is theatre — same words, opposite behaviour.",
    "\"Writing a good code makes a company ethical.\" The document is not the cause. Enforcement and culture make values real; an unenforced code actively teaches people that rules don't matter.",
    "An ethics program is the system of practices that converts stated values into real behaviour. Its power is shown by the fact that two companies with the identical code can have opposite cultures — the difference is leadership, enforcement, and culture, not the document.",
    "ethics program · values vs behaviour · enforcement · culture · unenforced code (worse than none)")

concept_understand("S3 · Concept 2 · [THEORY]","Components of an Effective Program",
    "The machinery that actually works — a cycle of mutually-reinforcing parts, not a single document.",
    ["An ethics officer/committee with real authority (not a side duty everyone ignores).",
     "Board-level oversight so ethics can't be buried by middle management.",
     "A specific code of conduct ('no gifts over X; no unlicensed software; report conflicts').",
     "Ongoing training, safe (anonymous, retaliation-free) reporting channels, and periodic audits."],
    "s3_cycle.png","Code → train → report → audit → consequences → repeat.",
    "~9 min. Walk each component with its purpose; the cycle image shows they reinforce each other.")
add_table_slide("S3 · Concept 2 · comparison","Ethics-program components — part → purpose → Nepal example",
    ["Component","What it does","Nepal example"],
    [["Ethics officer / committee","Gives ethics a real owner with authority","A compliance officer at a commercial bank"],
     ["Board-level oversight","Reports ethics to the top so it can't be buried","Board audit/compliance committee"],
     ["Specific code of conduct","Turns 'be good' into concrete rules","'No gifts over Rs X; report conflicts of interest'"],
     ["Ongoing training","Keeps rules alive with real scenarios","AML / anti-money-laundering staff training"],
     ["Safe reporting channel","Lets staff report without fear","Anonymous whistle-blower / grievance hotline"],
     ["Periodic audits","Checks rules are followed, not just posted","Internal compliance audit"]],
    per_page=6,widths=[1.8,2.4,2.4],fs=11.5,
    note="Nepali banks are regulated to have AML training and a grievance/whistle-blower hotline — the concrete machinery of 'we value integrity'.")
concept_apply("S3 · Concept 2 · [THEORY]","Components of an Effective Program",
    "A commercial bank's anti-money-laundering training plus an anonymous grievance/whistle-blower hotline is the concrete machinery that turns 'we value integrity' into measurable daily practice — and Nepali banks are regulated to have it.",
    "\"Having a code of conduct guarantees ethical behaviour.\" Enforcement and culture matter far more than the document. A safe reporting channel that staff are scared to use is no channel at all.",
    "An effective ethics program combines an ethics officer/committee with authority, board-level oversight, a specific code of conduct, ongoing training, safe (anonymous, retaliation-free) reporting channels, and periodic audits — a reinforcing cycle, not a single document.",
    "ethics officer · board oversight · specific code · training · whistle-blower hotline · audits")

concept_understand("S3 · Concept 3 · [THEORY]","Measuring & Sustaining Ethics",
    "A program isn't 'set and forget'. It is maintained with audits, surveys, and — above all — CONSISTENT consequences at every level.",
    ["Ethics audits and anonymous culture surveys surface problems before they become scandals.",
     "Consistent consequences for violations — especially at the top.",
     "Track reported concerns and act on them, so reporting feels worthwhile.",
     "The fastest way to destroy a program is to punish violations SELECTIVELY."],
    None,"Selective punishment destroys trust faster than having no code at all.",
    "~7 min. Work the two-employees mini case (senior excused, junior punished).")
add_table_slide("S3 · Concept 3 · comparison","Consistent vs selective enforcement — what everyone learns",
    ["Situation","Consistent enforcement","Selective enforcement"],
    [["Two staff break the same rule","Both face the same consequence","Senior excused, junior punished"],
     ["What the code signals","Rules apply to everyone","The code is power-dependent"],
     ["Effect on trust","Trust is reinforced","Trust collapses — visible hypocrisy"],
     ["Net result","Ethical culture strengthens","Worse than having no code at all"]],
    per_page=4,widths=[1.9,2.3,2.3],fs=11.5,
    note="Consistency is the make-or-break factor — a code applied only to the powerless teaches everyone that ethics is negotiable.")
concept_apply("S3 · Concept 3 · [THEORY]","Measuring & Sustaining Ethics",
    "Two employees break the same rule: the senior manager is quietly let off, the junior is publicly punished. Everyone watching now believes the code is power-dependent — which destroys trust faster than having no code at all, because the hypocrisy is visible.",
    "\"As long as we have rules, we're fine.\" Rules enforced selectively are worse than none. Consistency — especially punishing seniors — is what keeps a program credible.",
    "Ethics programs are sustained through audits, anonymous culture surveys, tracking of reported concerns, and — most importantly — consistent consequences applied at every level. Selective enforcement (excusing seniors) destroys trust faster than having no code, because it exposes visible hypocrisy.",
    "ethics audit · culture survey · consistent consequences · selective enforcement (the killer)")

add_activity("S3 — 'Design one enforceable rule'  ·  ~5 min",
    ["In pairs (2 min): design ONE concrete rule to make the college exam process more ethical.",
     "State HOW it would be enforced — a rule with no enforcement is a poster.",
     "Take 3 answers aloud (3 min).",
     "Pressure-test each: Who checks it? What's the consequence? Could a senior person dodge it?"],
    "Good answers pair a specific rule with a specific enforcer and consequence, and survive the 'could a senior dodge it?' test — tying straight back to the consistency point.",
    "ACTIVITY [~5 min].")
add_quiz("S3 — Quick Check  ·  ~5 min",
    [("Q1.  The single most important driver of an ethical culture is:","q"),
     ("a) a long code document   b) ✅ leadership / tone at the top   c) the company logo   d) annual profit","a"),
     ("Q2.  A safe, retaliation-free way for staff to report wrongdoing is a:","q"),
     ("a) marketing channel   b) ✅ whistle-blower / reporting hotline   c) sales funnel   d) press release","a"),
     ("Discussion: which single component would do the most good in a typical Nepali office — and why?","o")],
    "QUIZ [~5 min].")
add_summary("S3 · Summary  ·  [~2 min]",
    ["Values need systems, not posters — a framed code changes nothing on its own.",
     "Effective programs combine leadership, a specific code, training, safe reporting, and audits.",
     "Consistent enforcement beats any document — selective punishment is worse than none."],
    "In your first weeks at any job these signals reveal a healthy vs toxic employer: is there a real reporting channel? Are rules applied to seniors too? Is training genuine or a checkbox? You'll use this to read a workplace — and later to build a good one.",
    "S4 — a repeatable process for making the tough calls: ethical decision making.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S4
add_divider("Session 4 · Lecture hour 4 (of 5)","Ethical Considerations in Decision Making",
    "The night before the exam, a classmate accidentally shares a Drive folder — and inside are tomorrow's answers. You have them now. Don't ask 'what's right' yet — ask 'how would you even DECIDE?'",
    "OPENING HOOK [~5 min]. Point out everyone jumped to an answer with no method. Agenda: the 5-step process → four ethical lenses → common decision traps.")

concept_understand("S4 · Concept 1 · [THEORY]","The 5-Step Decision Process",
    "A repeatable method you'll reuse in every later unit and every workplace dilemma: Facts → Stakeholders & options → Evaluate → Choose & act → Reflect.",
    ["1 Get the facts — most 'dilemmas' dissolve once you have them; never reason on assumptions.",
     "2 Identify stakeholders & realistic options (not just two extremes).",
     "3 Evaluate options using ethical lenses (next concept).",
     "4 Choose and act — and own it.   5 Reflect — what would you do differently? (judgment improves)"],
    "s4_5step.png","Facts → stakeholders/options → evaluate → act → reflect.",
    "~9 min. Steps 1 and 2 are the ones people skip — where most bad decisions are born.")
add_table_slide("S4 · Concept 1 · worked example","The 5 steps on the leaked-exam-answers dilemma",
    ["Step","What it involves","On this dilemma"],
    [["1. Get the facts","Establish what's actually true","Are these really tomorrow's answers? How did I get them?"],
     ["2. Stakeholders & options","Who's affected; realistic choices","You, honest classmates, the teacher, the institution; options beyond just use/ignore"],
     ["3. Evaluate","Test options through the four lenses","Fairness: using them cheats honest students"],
     ["4. Choose & act","Decide and own it","Report the leak / delete without looking"],
     ["5. Reflect","Review outcome; improve judgment","What pressure made it tempting? What next time?"]],
    per_page=5,widths=[1.7,2.4,2.6],fs=11.5,
    note="The method matters more than instant agreement — everyone should be able to defend their choice.")
concept_apply("S4 · Concept 1 · [THEORY]","The 5-Step Decision Process",
    "Applied to the leaked answers: get the facts (is it really the exam?), name stakeholders (honest classmates, teacher, institution) and real options, evaluate (fairness lens: using them cheats others), act (report/delete), reflect. The process turns a gut reaction into a defensible choice.",
    "\"You either know the right thing or you don't.\" People skip steps 1–2 (facts, stakeholders) and jump to an answer — that's where bad decisions are born. The method forces those steps.",
    "The 5-step ethical decision process is: (1) get the facts; (2) identify stakeholders and realistic options; (3) evaluate options through ethical lenses; (4) choose and act, owning it; (5) reflect to improve future judgment. Steps 1–2 are the most-skipped and most important.",
    "5-step process · facts · stakeholders & options · evaluate · act · reflect")

concept_understand("S4 · Concept 2 · [THEORY]","Four Ethical Lenses",
    "Four complementary ways to TEST an option in step 3. Each asks a different question; on hard cases they disagree, and naming the disagreement is half the work.",
    ["Utilitarian — 'Which option does the most good for the most people?' (weighs consequences).",
     "Rights / duty (deontology) — 'Does this respect basic rights and my duties, regardless of outcome?'",
     "Fairness / justice — 'Am I treating similar people alike? Is this fair?'",
     "Virtue / common good — 'What would a person of good character do? What serves the community?'"],
    None,"Consequences · rights · fairness · character — four questions, one decision.",
    "~9 min. Walk the ambulance-queue case where all four converge; then note hard cases are where they disagree.")
add_table_slide("S4 · Concept 2 · comparison","The four lenses — test question & the ambulance-jumps-the-fuel-queue case",
    ["Lens","Its test question","Verdict on the ambulance"],
    [["Utilitarian","Which option does the most good for the most people?","Let it pass — a life outweighs everyone's wait"],
     ["Rights / duty","Does this respect basic rights and duties, regardless of outcome?","The patient's right to life takes priority"],
     ["Fairness / justice","Am I treating similar cases alike? Is it fair?","A medical emergency is a genuinely different case — not unfair"],
     ["Virtue / common good","What would a person of good character do?","A decent person waves them through"]],
    per_page=4,widths=[1.5,2.7,2.5],fs=11.5,
    note="All four CONVERGE here — which is why it feels obviously right. The hard cases are where the lenses disagree.")
concept_apply("S4 · Concept 2 · [THEORY]","Four Ethical Lenses",
    "During a fuel shortage an ambulance asks to jump the queue: utilitarian (a life outweighs the wait), rights (right to life), fairness (an emergency is a different case), and virtue (a decent person waves it through) all agree — which is exactly why it feels obviously right.",
    "\"Ethics is just personal opinion — anything goes.\" Structured reasoning gives defensible, comparable answers. Two people using the lenses can disagree, but they can explain and compare their reasoning — the opposite of 'just opinion'.",
    "The four ethical lenses test an option from complementary angles: utilitarian (greatest good for the greatest number), rights/duty (respect rights and duties regardless of outcome), fairness/justice (treat like cases alike), and virtue/common good (what a person of good character would do). On easy cases they converge; naming their disagreement is the work on hard cases.",
    "utilitarian · rights/duty (deontology) · fairness/justice · virtue/common good · lenses converge vs disagree")

concept_understand("S4 · Concept 3 · [THEORY]","Common Decision Traps",
    "Four predictable pressures that derail good people — learn to name them in the moment.",
    ["Rationalization — 'It's not really cheating, everyone uses these notes.'",
     "Groupthink — going along because the whole team is, even when it feels wrong.",
     "Slippery slope — one small compromise ('just this once') that lowers the bar for next time.",
     "Blind obedience to authority — 'My manager told me to, so it's on them.' (It isn't — you're still responsible.)"],
    None,"Name the trap out loud and it loses half its power.",
    "~7 min. Work the 'just fudge this one report' mini case — obedience + slippery slope.")
add_table_slide("S4 · Concept 3 · comparison","Decision traps — how it sounds & how to counter it",
    ["Trap","How it sounds in real life","Counter"],
    [["Rationalization","'It's not really cheating — everyone uses these notes'","Name the act plainly; would you defend it openly?"],
     ["Groupthink","'The whole team agreed, so it must be fine'","Ask for one dissenting view; decide on merits"],
     ["Slippery slope","'Just this once, it won't happen again'","Set the bright line before the pressure, not during"],
     ["Blind obedience","'My manager told me to, so it's on them'","You remain responsible — run it through the 5 steps"]],
    per_page=4,widths=[1.5,3.0,2.4],fs=11.5,
    note="'Just fudge this one report' uses TWO traps at once — blind obedience + slippery slope.")
concept_apply("S4 · Concept 3 · [THEORY]","Common Decision Traps",
    "A manager says 'just fudge this one report — only this once.' Two traps are being used to pressure you: blind obedience ('the boss decided') and slippery slope ('just once'). Recognising them by name lets you resist and run the 5 steps instead.",
    "\"If my boss told me to, it's not my fault.\" Blind obedience doesn't transfer responsibility — you're still accountable. 'Just this once' is a slippery slope that lowers the bar for the next time.",
    "Common decision traps are rationalization ('everyone does it'), groupthink (going along with the team), slippery slope ('just this once'), and blind obedience to authority ('the boss decided'). They pressure ordinary people into wrong choices; naming the trap in the moment is the defence.",
    "rationalization · groupthink · slippery slope · blind obedience · you remain responsible")

add_activity("S4 — 'Run the dilemma'  ·  ~6 min",
    ["In pairs (3 min): take the leaked-exam-answers hook and work it through ALL 5 steps explicitly.",
     "Name at least ONE lens used in step 3.",
     "Take 2 pairs' walkthroughs aloud (3 min).",
     "The goal isn't unanimity — it's that everyone USED the method and can defend their choice."],
    "A good walkthrough gets the facts, names stakeholders (honest classmates, teacher), evaluates via fairness/rights, acts (report or delete), and reflects. Different final choices are fine if the method is used.",
    "ACTIVITY [~6 min].")
add_quiz("S4 — Quick Check  ·  ~5 min",
    [("Q1.  The FIRST step in ethical decision making is to:","q"),
     ("a) pick an option   b) ✅ gather the facts   c) punish someone   d) write a report","a"),
     ("Q2.  'The greatest good for the greatest number' describes which lens?","q"),
     ("a) rights/duty   b) fairness   c) ✅ utilitarian   d) virtue","a"),
     ("Discussion: give a workplace example where two lenses would disagree — how would you decide?","o")],
    "QUIZ [~5 min].")
add_summary("S4 · Summary  ·  [~2 min]",
    ["Use the 5-step process: facts → stakeholders/options → evaluate → act → reflect.",
     "Test options through four lenses: utilitarian, rights/duty, fairness, virtue.",
     "Watch for traps: rationalization, groupthink, slippery slope, blind obedience."],
    "You'll face grey-area calls constantly — a vendor's gift, a boss bending a rule, a deadline shortcut. A repeatable process protects you (your choices are defensible) and everyone affected. Interviewers literally ask: 'walk me through a hard decision you made.'",
    "S5 — why all of this gets sharper and bigger in Information Technology.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S5
add_divider("Session 5 · Lecture hour 5 (of 5) — CLOSES UNIT 1","Ethics in Information Technology",
    "An app quietly sells your location data. A loan algorithm rejects applicants by neighbourhood (digital redlining). A deepfake of a politician goes viral the night before an election. A dishonest shopkeeper cheats one customer at a time — a bad line of code can harm millions in seconds, permanently.",
    "OPENING HOOK [~5 min]. Ask: what makes the IT versions worse than the offline versions? Agenda: why IT is distinct → the PAPA pillars → 'can vs should'.")

concept_understand("S5 · Concept 1 · [THEORY]","Why IT Raises Distinct Ethical Challenges",
    "IT amplifies ethical impact along five dimensions, so ordinary ethics gets sharper and bigger — and the law is often missing, leaving your own ethics as all that holds.",
    ["Scale — one decision (a default, an algorithm) affects millions at once.",
     "Speed — harm spreads in seconds, before anyone can intervene.",
     "Anonymity — wrongdoers hide; victims can be targeted from a distance, across borders.",
     "Permanence — leaked/posted data is almost impossible to fully erase. Plus a capability–regulation gap: tech outruns the law."],
    "s5_scale.png","IT makes ethical mistakes scale to millions — instantly and permanently.",
    "~9 min. Tie back to S1: 'the law is the floor' matters MOST in IT — the floor is often missing entirely.")
add_table_slide("S5 · Concept 1 · comparison","What makes IT ethics distinct — offline vs at IT scale",
    ["Factor","Offline","At IT scale","Consequence"],
    [["Scale","One person at a time","Millions at once (one setting/algorithm)","A single choice harms a whole population"],
     ["Speed","Slow to spread","Seconds","Harm is done before anyone can react"],
     ["Anonymity","Wrongdoer is visible","Wrongdoer can hide, across borders","Hard to catch or hold accountable"],
     ["Permanence","A rumour fades","A screenshot is forever","Leaked data can't be fully erased"],
     ["Regulation","Law usually exists","Capability outruns the law","'Is it legal?' often has no answer yet"]],
    per_page=5,widths=[1.2,1.9,2.6,2.4],fs=11,
    note="Because the legal 'floor' is often missing in IT, your own ethics is frequently the only thing holding.")
concept_apply("S5 · Concept 1 · [THEORY]","Why IT Raises Distinct Ethical Challenges",
    "Personal data leaked from a Nepali online service spreads instantly and can never be fully recalled (scale + speed + permanence); viral election misinformation outruns the fact-checkers (speed). Both are everyday failures happening at machine scale.",
    "\"IT ethics is the same as normal ethics.\" The scale, speed, anonymity, and permanence of IT make the stakes and irreversibility far higher — and the law often hasn't caught up, so you can't lean on 'is it legal?'.",
    "IT raises distinct ethical challenges because of scale (millions affected at once), speed (harm spreads in seconds), anonymity (wrongdoers hide), permanence (data can't be erased), and a capability–regulation gap (technology outruns the law). This is why 'the law is only the floor' matters most in IT.",
    "scale · speed · anonymity · permanence · capability–regulation gap")

concept_understand("S5 · Concept 2 · [THEORY]","The Four Pillars — 'PAPA'",
    "PAPA names the four core IT-ethics themes — Privacy, Accuracy, Property, Access — and doubles as a map of the whole IT 246 course.",
    ["Privacy — who can collect and see your data? (→ Unit 2 privacy, Unit 9 law).",
     "Accuracy — who's responsible when data or an algorithm is WRONG and someone is harmed?",
     "Property — who OWNS information and software? (→ Unit 3 intellectual property).",
     "Access — who gets to use technology, and who's left out (the digital divide)? Security threads through all four (→ Units 5–8)."],
    None,"Privacy · Accuracy · Property · Access — the map of the whole course.",
    "~9 min. Connect each pillar forward to the unit that develops it.")
add_table_slide("S5 · Concept 2 · comparison","PAPA — the four pillars mapped to examples & course units",
    ["Pillar","The question it raises","Example","Where in this course"],
    [["Privacy","Who can collect and see your data?","An app sells your location data","Unit 2 (privacy), Unit 9 (law)"],
     ["Accuracy","Who's responsible when data/an algorithm is wrong?","A biased loan algorithm wrongly rejects you","This unit; cybersecurity units"],
     ["Property","Who owns information and software?","Pirating software; stealing a code repo","Unit 3 (intellectual property)"],
     ["Access","Who gets to use tech — and who's left out?","The rural digital divide","Course-wide; policy"]],
    per_page=4,widths=[1.1,2.4,2.4,2.1],fs=11,
    note="Security threads through all four pillars (Units 5–8) — so this single table is a map of the entire IT 246 course.")
concept_apply("S5 · Concept 2 · [THEORY]","The Four Pillars — 'PAPA'",
    "A Nepali service leaking personal data is a Privacy + security failure; viral misinformation after a disaster is an Accuracy failure; pirating software is a Property issue; the rural digital divide is an Access issue. PAPA lets you name any IT-ethics concern precisely.",
    "\"It's just technology — the tool is neutral.\" Technology is NOT value-neutral: what you build, what data you collect, and how an algorithm decides all encode human values and bias. A model trained on biased data discriminates automatically, at scale.",
    "The PAPA framework names four core IT-ethics themes: Privacy (who sees your data), Accuracy (responsibility for wrong data/algorithms), Property (who owns information/software), and Access (who can use technology and who is excluded). Security runs through all four; together they map the whole course.",
    "PAPA · Privacy · Accuracy · Property · Access · technology is not value-neutral")

concept_understand("S5 · Concept 3 · [THEORY]","The IT Professional's Responsibility — 'Can' vs 'Should'",
    "The defining question of IT ethics: just because you CAN build or do something, does that mean you SHOULD? As a BIM graduate, you'll be the one choosing what data to collect, how an algorithm treats people, what to log, what to expose.",
    ["'Public' data is not the same as 'consented' data.",
     "Professional codes (ACM, IEEE) put your duty to users and the public above an employer's convenience.",
     "The 5-step process (S4) is exactly how you answer a 'can vs should' question.",
     "This is where every later unit — IP, security, forensics, cyber law — plugs in."],
    None,"'Can' is an engineering question; 'should' is an ethics question — you own both.",
    "~7 min. Run the 100,000-public-posts scraping mini case through the S4 process.")
add_table_slide("S5 · Concept 3 · comparison","'Can' vs 'Should' — scraping 100,000 public posts",
    ["Question","'Can' (engineering)","'Should' (ethics)"],
    [["Is it possible?","Yes — technically easy","Not the right question"],
     ["Is the data 'public'?","Yes, visible to anyone","Public ≠ consented to THIS use"],
     ["Who's affected?","(ignored)","The 100,000 people whose posts they are"],
     ["Rights/duty lens","(ignored)","Did they agree to be scraped for this?"],
     ["Verdict","'We can, so let's'","Often: don't — or seek consent / anonymise"]],
    per_page=5,widths=[1.7,2.2,2.6],fs=11.5,
    note="'Can' and 'should' give different answers — professional codes (ACM, IEEE) exist to keep 'should' in front.")
concept_apply("S5 · Concept 3 · [THEORY]","The IT Professional's Responsibility",
    "For a class project you CAN scrape 100,000 users' public posts — easy, and the data is 'public'. SHOULD you? Run the S4 process: facts (public ≠ consented), stakeholders (those 100,000 people), rights lens (did they agree to this use?). 'Can' and 'should' diverge.",
    "\"If the data is public, using it is fine.\" Public visibility isn't consent to any use. The professional's duty (per ACM/IEEE codes) is to the people in the data, not just to what's technically allowed.",
    "IT-ethics responsibility centres on 'can vs should': technical possibility does not settle whether an action is right. IT professionals decide what data to collect and how algorithms treat people, so professional codes (ACM, IEEE) place their duty to users and the public above an employer's short-term convenience.",
    "can vs should · public ≠ consented · professional codes (ACM/IEEE) · duty to users & public")

add_activity("S5 — 'Can vs Should audit'  ·  ~6 min",
    ["In pairs (2 min): pick ONE app you use daily.",
     "Identify one PAPA theme it raises a concern about (Privacy / Accuracy / Property / Access).",
     "Identify one 'can but maybe shouldn't' thing it does with your data.",
     "Take 3 answers aloud (4 min) — makes the framework personal and closes the unit on your real digital life."],
    "Strong answers name a specific PAPA theme (e.g. Privacy: the app tracks location in the background) and a concrete 'can-but-shouldn't' (e.g. it CAN sell that data; it probably SHOULDN'T without clear consent).",
    "ACTIVITY [~6 min].")
add_quiz("S5 — Quick Check  ·  ~5 min",
    [("Q1.  Which factor most makes IT ethics DISTINCT from everyday ethics?","q"),
     ("a) it's cheaper   b) ✅ the scale, speed, and permanence of impact   c) it's always legal   d) it needs no rules","a"),
     ("Q2.  In 'PAPA', the four themes are Privacy, Accuracy, Property, and:","q"),
     ("a) Advertising   b) Authority   c) ✅ Access   d) Automation","a"),
     ("Discussion: name one IT product you use that raises an ethical concern — which PAPA theme, and why?","o")],
    "QUIZ [~5 min].")
add_summary("S5 · Summary  ·  [~2 min]",
    ["IT amplifies ethical impact through scale, speed, anonymity, and permanence.",
     "Technology is value-laden, not neutral; the four pillars are PAPA (Privacy, Accuracy, Property, Access).",
     "Professionals own the 'can vs should' question — guided by professional codes (ACM, IEEE)."],
    "As BIM graduates you'll build, manage, or buy information systems — deciding what data to collect, how algorithms treat people, and what to do when things go wrong. Every later unit (IP, cybersecurity, forensics, cyber law) is a tool for the 'can vs should' question you met today.",
    "Unit 2 — ethics specifically for IT workers and IT users: professional duties, privacy, and social-networking issues.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 1 · Cheat Sheet","One-page revision reference",
    [("Ethics vs morals vs law vs etiquette","Group code · personal belief · state-enforced · manners. Law is the FLOOR, not the ceiling."),
     ("Legal/ethical grid","Two axes → 4 quadrants. The danger zone is legal-but-unethical (only judgment stops you)."),
     ("Business ethics","Serves conflicting stakeholders; core tension = short-term profit vs long-term trust."),
     ("CSR (Carroll)","Duty to society: economic → legal → ethical → philanthropic. Stakeholders = all affected, not just owners."),
     ("Improving ethics","Systems, not posters: leadership, specific code, training, safe reporting, audits, CONSISTENT consequences."),
     ("Decisions & IT","5 steps (facts→stakeholders→evaluate→act→reflect); 4 lenses; IT = scale/speed/permanence; PAPA; can vs should.")])

add_glossary("Unit 1 · Glossary","Key terms — quick reference",
    [("Ethics","a group/profession/society's shared code of right and wrong."),
     ("Morals","an individual's personal beliefs about right and wrong."),
     ("Law","rules the state enforces, with penalties."),
     ("Etiquette","social manners; breaking them is rude, not deeply wrong."),
     ("Legal ≠ ethical","law is the floor, not the ceiling."),
     ("Business ethics","applying ethical standards to commercial conduct."),
     ("CSR","a company's duty to act for society's benefit."),
     ("Carroll's pyramid","economic → legal → ethical → philanthropic."),
     ("Stakeholder theory","accountable to all affected, not just owners."),
     ("Greenwashing","a CSR message the daily operation contradicts."),
     ("Ethics program","the systems that turn values into behaviour."),
     ("Whistle-blower hotline","a safe, retaliation-free reporting channel."),
     ("5-step process","facts → stakeholders/options → evaluate → act → reflect."),
     ("Four lenses","utilitarian · rights/duty · fairness · virtue."),
     ("Decision traps","rationalization · groupthink · slippery slope · blind obedience."),
     ("PAPA","Privacy · Accuracy · Property · Access (IT ethics pillars).")])

# ============= CONSOLIDATED END-OF-UNIT QUIZ =============
add_divider("Unit 1 · Revision","Consolidated end-of-unit quiz",
    "Twelve MCQs across the whole unit (answers shown), then short-answer, applied-case, and discussion questions to work from the concept slides and Unit1_material.md.",
    "Use as a 15–20 min in-class quiz or take-home review.")
add_quiz("Section A — Multiple choice (answers shown)",
    [("1.  Ethics is best defined as   →  ✅ a group/society's code of right and wrong","a"),
     ("2.  An action legal but widely considered wrong is   →  ✅ unethical","a"),
     ("3.  'Floor, not the ceiling' describes ethics' relation to   →  ✅ law","a"),
     ("4.  The base of Carroll's CSR pyramid is   →  ✅ economic","a"),
     ("5.  Stakeholder theory: a business is accountable to   →  ✅ all affected groups, not just owners","a"),
     ("6.  The most important driver of an ethical culture is   →  ✅ leadership / tone at the top","a"),
     ("7.  A retaliation-free channel to report wrongdoing is a   →  ✅ whistle-blower hotline","a"),
     ("8.  The first step in ethical decision making is to   →  ✅ gather the facts","a"),
     ("9.  'Greatest good for the greatest number' is the   →  ✅ utilitarian lens","a"),
     ("10.  Going along with a bad team decision is   →  ✅ groupthink","a"),
     ("11.  What most makes IT ethics distinct is the   →  ✅ scale, speed & permanence of impact","a"),
     ("12.  In 'PAPA' the four themes are Privacy, Accuracy, Property and   →  ✅ Access","a")],
    "Consolidated quiz Section A.",compact=True)
add_quiz("Sections B–D — short answer, applied case & discussion",
    [("Section B — Short answer","q"),
     ("13. Define CSR + Carroll's four levels in order.   14. Four components of an effective ethics program.","o"),
     ("15. Three ethical lenses + a test question each.   16. Explain 'tone at the top'.   17. Two reasons technology is not value-neutral.","o"),
     ("Section C — Applied case","q"),
     ("18. Apply the 5-step process: a vendor offers your procurement officer a 'gift' to win a tender.","o"),
     ("19. Place on the legal/ethical grid, with a reason: (a) a bribe (b) a tax loophole (c) whistle-blowing on fraud (d) sharing one paid login.","o"),
     ("Section D — Discussion","q"),
     ("20. 'Sharing one paid streaming/Canva account among friends is unethical.' Argue both sides, then take a position using one lens.","o")],
    "Consolidated quiz Sections B–D. Model answers on the concept slides and in Unit1_material.md.",compact=True)

# ---- close ----
add_title("End of Unit 1  ·  IT 246",
          "S1–S5 complete: ethics vs law/morals/etiquette · the legal/ethical grid · business ethics & CSR · improving ethics · 5-step decisions & 4 lenses · ethics in IT (PAPA, can vs should)",
          "Built to COURSE_MATERIAL_STANDARD.md incl. the §7A depth rule · comparison & concrete-example tables throughout · "
          "self-contained, PDF-safe · Next: Unit 2 — Ethics for IT Workers & Users.")

_add_page_numbers()
save("IT246_Unit1.pptx")
