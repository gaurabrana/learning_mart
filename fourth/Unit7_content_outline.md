# Unit 7 — Advanced Topics · Content Outline

**4 LHs → 4 sessions (S45–S48) · 50 min each**
This is the *content map* — what will fill each slot before we generate full material.
Local examples use Nepal / South Asia. Review and tell me what to swap.

> Template per session (from the guide):
> Opening hook (5m) → Content sections (35m) → Check for understanding (5m) →
> Real-life application (3m) → Summary & takeaways (2m), with speaker notes + visual cues.
> Note: S48 is the **final session** — it is restructured as a course-wide review + project/exam prep, not new theory.

---

## Unit 7 learning outcomes (what students can do after S45–S48)
1. Explain how indexing and query tuning improve database performance, and apply basic tuning reasoning.
2. Identify core database security threats and controls: authentication, authorization, SQL injection, and encryption.
3. Describe parallel and distributed databases, including fragmentation, replication, and distribution transparency.
4. Distinguish OLTP from OLAP and explain data warehousing, ETL, and the goal of data mining.
5. Define BigData (the 3Vs) and classify the main NoSQL database types and when to use them.
6. (S48) Synthesize all seven units into one coherent picture and prepare for the final exam + project demo.

---

## S45 — Database Performance Tuning · Database Security

**Hook:** "On exam-results day, lakhs of students hit the result portal in one hour — some pages load instantly, some time out. Two questions decide everything today: *why is it slow*, and *who is allowed in*?" → performance + security.

**Concepts & how each will be filled:**

1. **Performance tuning — why it matters**
   - Definition: making the DB return correct answers *faster* using the same hardware.
   - Theory bullets: tune at three levels — query, schema/index, hardware/config; measure before you change.
   - Global example: an e-commerce search that drops from 4s to 200ms after tuning.
   - Local example: Daraz "search products" during Dashain sale traffic.
   - Misconception: *"Just buy a bigger server."* Correction: a missing index often beats expensive hardware.

2. **Indexing (recap from Unit 5)**
   - Definition: an auxiliary structure (often B-tree) that finds rows without scanning the whole table.
   - Theory: speeds up reads, slows down writes/inserts; index the columns in WHERE/JOIN/ORDER BY.
   - Local example: index on `citizenship_no` in a bank's customer table so KYC lookup is instant.
   - Fun element: analogy — an index is the back-of-book index; without it you read every page (full table scan).

3. **Query tuning**
   - Theory bullets: avoid `SELECT *`, use the right WHERE filters, read the *execution plan* (EXPLAIN), avoid unnecessary nested subqueries, prefer joins the optimizer can index.
   - Mini case: eSewa transaction-history query slow because it scans all transactions instead of filtering by `user_id` + date range first.
   - Misconception: *"More indexes always = faster."* Correction: too many indexes slow down every insert/update and waste space.

4. **Database security — authentication vs authorization**
   - Authentication = *who are you* (login, password, OTP); Authorization = *what are you allowed to do* (GRANT/REVOKE, roles).
   - Local example: Khalti login (authentication via OTP) vs a support agent who can view but not refund (authorization).
   - Fun element: analogy — authentication = showing your ID at the gate; authorization = which rooms your keycard opens.

5. **SQL Injection**
   - Definition: attacker injects malicious SQL through an input field to read/alter the database.
   - Theory: caused by concatenating user input into queries; fix = parameterized queries / prepared statements + input validation.
   - Mini case: a login form where typing `' OR '1'='1` logs you in as admin — show why, show the fix.
   - Misconception: *"Hiding the SQL/error messages makes it secure."* Correction: obscurity is not a control; use parameterized queries.

6. **Encryption**
   - Definition: encoding data so only authorized parties can read it; *at rest* (stored data) vs *in transit* (TLS/HTTPS).
   - Local example: a bank encrypting stored account data + HTTPS on the mobile-banking app.
   - Theory: even a stolen database dump is useless without keys.

**Check for understanding:**
- MCQ1: A query that filters by an indexed column avoids a... → full table scan ✅ (b) commit (c) deadlock (d) rollback
- MCQ2: The best defense against SQL injection is... → parameterized/prepared statements ✅ (vs hiding errors, more indexes, bigger server)
- Discussion: "Pick a Nepali app you use and name one thing it should authenticate and one thing it should authorize."

**Real-life application:** tuning + security are the two most common *job interview* topics for DB/backend roles in Nepali fintech (eSewa, Khalti, IME Pay) and banking core systems.

**Summary:** (1) tune query → index → hardware, measure first; (2) authentication = who, authorization = what; (3) SQL injection is fixed with parameterized queries, encryption protects data at rest and in transit. **Next:** what happens when one database is too big for one machine — parallel & distributed databases.

**Visual cues:** "full scan vs index" diagram (book + index); EXPLAIN-plan before/after table; authentication-vs-authorization 2-column slide; SQL-injection input box animation. Mark slides [THEORY]/[EXAMPLE].

---

## S46 — Concept of Parallel and Distributed Databases

**Hook:** "Ncell has subscribers in Mechi and in Mahakali. Should *all* their call records sit on one server in Kathmandu? What if that server burns down?" → distribute the data.

**Concepts & how each will be filled:**

1. **Parallel vs Distributed databases**
   - Parallel DB: many processors/disks in *one location* working together to speed up one system.
   - Distributed DB: data physically stored across *multiple sites/locations*, appearing as one logical DB.
   - Misconception: *"Parallel and distributed are the same."* Correction: parallel = one place, more power; distributed = many places, one logical view.
   - Analogy: parallel = many cooks in one kitchen; distributed = branches of the same restaurant in different cities.

2. **Why distribute? (motivation)**
   - Theory bullets: locality (data near users), reliability (no single point of failure), scalability.
   - Local example: a national telecom (Ntc/Ncell) keeping regional records in regional data centers.

3. **Fragmentation**
   - Definition: splitting a table across sites. Horizontal (split rows, e.g. by province), vertical (split columns), mixed.
   - Local example: customer table fragmented by province — Bagmati rows on the KTM server, Gandaki rows on the Pokhara server.
   - Mini case: a bank storing each branch's accounts at that branch but querying nationwide.

4. **Replication**
   - Definition: keeping copies of the same data at multiple sites.
   - Theory: improves read speed + availability; trade-off = keeping copies consistent on writes.
   - Misconception: *"Replication and fragmentation are opposites you must choose between."* Correction: real systems use both together.
   - Fun element: analogy — replication = photocopying the same notice for every branch noticeboard.

5. **Distribution transparency**
   - Definition: the user/app doesn't need to know *where* data lives or that it's fragmented/replicated.
   - Types (one line each): location, fragmentation, replication transparency.
   - Local example: a Daraz user in Biratnagar searches once — they never know which data center answered.
   - Analogy: callback to Unit 1 data independence — "hide the inside, keep the outside simple."

**Check for understanding:**
- MCQ1: Splitting a customer table so each province's rows live at that province's site is... → horizontal fragmentation ✅ (vs vertical, replication, indexing)
- MCQ2: A user querying a distributed DB without knowing data locations is enabled by... → distribution/location transparency ✅
- Discussion: "For a national e-commerce site, would you fragment by province, replicate the product catalog, or both — and why?"

**Real-life application:** every large-scale Nepali/regional service (telecoms, national ID/Nagarik App backend, big e-commerce) is distributed for reliability and locality — this is how systems stay up when one site fails.

**Summary:** (1) parallel = one site, more power; distributed = many sites, one logical DB; (2) fragmentation splits data, replication copies it (usually both); (3) transparency hides all of this from the user. **Next:** turning operational data into *insight* — data warehousing, data mining, BigData, and NoSQL.

**Visual cues:** map of Nepal with provincial servers; horizontal vs vertical fragmentation table split-diagram; replication copy-arrows; "user → transparency layer → sites" diagram.

---

## S47 — Data Warehousing & Data Mining · BigData · NoSQL Databases

**Hook:** "eSewa runs your wallet *right now* (fast, tiny transactions). But how does eSewa figure out 'which districts spend most during Tihar'? Different job, different kind of database." → OLTP vs OLAP and beyond.

**Concepts & how each will be filled:**

1. **OLTP vs OLAP**
   - OLTP (Online Transaction Processing): many small, fast read/write transactions — the *running* of the business.
   - OLAP (Online Analytical Processing): few large, complex read queries over history — the *analysis* of the business.
   - Local example: OLTP = a single Khalti payment; OLAP = "monthly spending trend by city" report.
   - Misconception: *"One database should do both well."* Correction: mixing heavy analytics on the live transaction DB slows down customers; separate them.

2. **Data Warehousing**
   - Definition: a separate, subject-oriented, integrated store of historical data built for analysis (OLAP).
   - Theory: data is read-mostly, organized for reporting, sourced from many operational systems.
   - Local example: a bank pooling data from branches + cards + loans into one warehouse for management dashboards.
   - Analogy: operational DBs = daily-use cash drawer; warehouse = the audited archive room.

3. **ETL (Extract, Transform, Load)**
   - Definition: the pipeline that moves data from operational systems into the warehouse — Extract from sources, Transform/clean/standardize, Load into the warehouse.
   - Mini case: combining eSewa + bank + telecom-recharge data where dates and phone formats differ → Transform step fixes it.
   - Misconception: *"You just copy the data over."* Correction: the Transform (cleaning/standardizing) step is the hard, essential part.

4. **Data Mining**
   - Definition: discovering patterns/relationships in large data sets (classification, clustering, association rules).
   - Local example: Daraz "customers who bought X also bought Y" (association); telecom predicting which customers will churn (classification).
   - Misconception: *"Data mining = just running queries / reports."* Correction: mining finds *previously unknown* patterns, not pre-asked questions.

5. **BigData & the 3Vs**
   - Definition: data too large/fast/varied for traditional DBMS handling.
   - Volume (huge size), Velocity (arriving fast/real-time), Variety (text, images, logs, GPS) — note extended Vs (Veracity, Value) as a bonus.
   - Local example: ride/delivery app GPS streams (Pathao/inDrive), or telecom call-detail-record floods.
   - Fun element: analogy — a regular DB is a bucket; BigData is a monsoon river — you need different tools.

6. **NoSQL databases & types**
   - Definition: "Not Only SQL" — non-relational stores built for scale, flexible schema, and the 3Vs (callback to Unit 1/Unit 4 misconception).
   - Four types (one line + example each): Key-Value (Redis — session/cart), Document (MongoDB — product catalog JSON), Column-family (Cassandra — telecom CDR at scale), Graph (Neo4j — social/fraud networks).
   - Misconception: *"NoSQL is replacing/killing SQL."* Correction: it complements relational DBs; pick the tool for the job (and most apps still need a relational core).
   - Theory: trade-off teaser — flexibility/scale vs strict ACID consistency.

**Check for understanding:**
- MCQ1: A single Khalti payment being recorded is an example of... → OLTP ✅ (vs OLAP, ETL, data mining)
- MCQ2: "Variety" in BigData's 3Vs refers to... → many different data formats/types ✅ (vs speed, size, accuracy)
- Discussion: "For storing a flexible, ever-changing product catalog, would you choose a relational DB or a document NoSQL DB — and why?"

**Real-life application:** analytics + BigData + NoSQL skills are the fastest-growing data jobs in Nepal/South Asia (fintech analytics, telecom churn, e-commerce recommendations) — this session points students toward that career path.

**Summary:** (1) OLTP runs the business, OLAP analyzes it; (2) warehouses store historical data fed by ETL, data mining finds hidden patterns; (3) BigData = Volume/Velocity/Variety, and NoSQL (key-value/document/column/graph) complements SQL. **Next:** the final session — we tie all 7 units together and prepare for the exam + project demo.

**Visual cues:** OLTP-vs-OLAP 2-column table; source systems → ETL pipeline → warehouse → dashboard flow diagram; "3 Vs" infographic; 4 NoSQL types comparison grid with logos/examples.

---

## S48 — Course Review · Project Presentations · Final Q&A (FINAL SESSION)

**Hook:** "Eight semesters of life run on databases — and in 4 months you went from 'what is a database?' to designing, querying, and securing one. Today we connect every dot and get you exam- and demo-ready."

> **Note:** No new theory. This session is a *synthesis + preparation* session: course-wide recap, exam guidance, and project-demo structure.

**Part A — Course-wide recap (the 7-unit story, ~18m)**
A single narrative thread, one slide per unit:
1. **Unit 1 — Concepts & Architecture:** what a DB/DBMS is, users/DBA, schemas/instances, 3-schema architecture, client/server.
2. **Unit 2 — ER & Relational Model:** entities, attributes, keys, relationships, ER→table conversion (the *design* stage).
3. **Unit 3 — Relational Algebra & Calculus:** SELECT/PROJECT/JOIN — the formal foundation under SQL.
4. **Unit 4 — Normalization:** functional dependencies, 1NF→BCNF, removing redundancy/anomalies.
5. **Unit 5 — SQL:** DDL/DML, joins, subqueries, views, stored procedures, triggers, indexing (the *practical* core).
6. **Unit 6 — Transactions, Concurrency & Recovery:** ACID, serializability, 2PL/timestamp, backup/recovery.
7. **Unit 7 — Advanced Topics:** tuning, security, distributed DBs, warehousing/mining/BigData/NoSQL.
- Visual centerpiece: one "course map" diagram — Design (U2) → Theory (U3) → Refine (U4) → Build/Query (U5) → Protect/Run (U6) → Scale/Advanced (U7), all on the Concepts foundation (U1).

**Part B — How the units connect (mini synthesis, ~7m)**
- Worked thread on one example (e.g. an eSewa-style wallet): ER design → normalize → SQL tables/queries → transactions for a transfer → index/secure → scale via distribution + analyze via warehouse.
- Common misconception to retire: *"These units are separate topics."* Correction: they are one lifecycle of building a real system.

**Part C — Exam preparation guidance (~10m)**
- Likely high-weight areas: ER→table conversion, normalization to 3NF/BCNF, SQL writing (joins/subqueries/aggregates), ACID + 2PL, definitions across Unit 1 & 7.
- How to answer: define → give an example → draw a diagram where asked; show working in normalization/SQL.
- Quick self-test pointer: the **End-of-Unit Quiz** below + advice to redo each unit's per-session MCQs.
- Time-management + diagram-marks tips.

**Part D — Project demo structure (~10m)**
Recommended 8–10 minute demo flow for groups (max 4 students, per syllabus):
1. Problem & scope (what real Nepali use-case: e.g. a clinic, a shop, a campus system).
2. ER diagram → schema (show design decisions).
3. Normalization evidence (which NF, why).
4. Live SQL demo: create, insert, 3–4 meaningful SELECT/JOIN queries, one view.
5. One "advanced" touch (an index, a transaction, or a security note) tying to Unit 7.
6. Q&A readiness — expect "why this key?", "is this normalized?", "what if two users update at once?".
- Evaluation reminder: clarity of design > number of features.

**Part E — Final Q&A (~5m)**
- Open floor; collect lingering doubts; point to the suggested readings (Elmasri/Navathe, Silberschatz) for depth.

**Real-life application:** the project demo *is* the rehearsal for a real job/internship technical interview and on-the-job system design in Nepal's IT sector.

**Summary:** (1) the 7 units are one lifecycle: concepts → design → theory → normalize → SQL → transactions/recovery → advanced/scale; (2) exam favors ER, normalization, SQL, ACID; (3) a strong demo shows design reasoning, not just a running app. **Course complete — you can now design, build, query, protect, and scale a real database.**

**Visual cues:** the single "course map" diagram (centerpiece); per-unit one-line recap slides; demo-flow checklist slide; exam-topic weighting chart.

---

# END-OF-UNIT 7 QUIZ (consolidated)

> Use after S47 (or as S48 self-test). 10 MCQs + 4 short-answer + 2 scenario questions. ✅ marks the correct option.

## Section A — Multiple Choice (10)
1. Adding an index primarily speeds up... (a) inserts (b) reads/lookups ✅ (c) backups (d) commits
2. The recommended fix for SQL injection is... (a) hide error messages (b) more indexes (c) parameterized/prepared statements ✅ (d) a bigger server
3. "Who are you" is decided by... (a) authorization (b) authentication ✅ (c) replication (d) encryption
4. Protecting a stored database dump from being read if stolen uses... (a) indexing (b) encryption at rest ✅ (c) fragmentation (d) OLAP
5. Splitting table rows by province across sites is... (a) vertical fragmentation (b) horizontal fragmentation ✅ (c) replication (d) normalization
6. Keeping copies of the same data at multiple sites is... (a) fragmentation (b) replication ✅ (c) indexing (d) transparency
7. A single ATM withdrawal being recorded is... (a) OLAP (b) data mining (c) OLTP ✅ (d) ETL
8. The "T" in ETL stands for... (a) Transfer (b) Transform ✅ (c) Transaction (d) Truncate
9. "Velocity" in BigData's 3Vs refers to... (a) data size (b) data variety (c) speed of incoming data ✅ (d) data accuracy
10. MongoDB is an example of a ___ NoSQL database. (a) key-value (b) document ✅ (c) graph (d) column-family

## Section B — Short Answer (4)
11. Differentiate authentication from authorization with one example each.
12. Define fragmentation and replication, and state why systems often use both.
13. Differentiate OLTP from OLAP in two points each.
14. List the 3Vs of BigData and give a one-line example of each.

## Section C — Scenario (2)
15. eSewa's transaction-history page is slow. List three things you would check/do (think: query, index, OLTP-vs-OLAP separation) and justify each.
16. A national telecom wants regional data near regional users but no data loss if one data center fails. Explain how fragmentation, replication, and distribution transparency together solve this.

## Answer key (MCQ)
1-b, 2-c, 3-b, 4-b, 5-b, 6-b, 7-c, 8-b, 9-c, 10-b

---

## Open questions before I generate Unit 7 material
1. Keep the **Nepali examples** above (eSewa/Khalti/Daraz/Ntc-Ncell/Pathao/Nagarik App), or swap any?
2. For S48, is the **5-part review structure** (recap → connections → exam prep → demo structure → Q&A) the split you want, or reweight the minutes?
3. Should the **end-of-unit quiz** stay at 10 MCQ + 4 short + 2 scenario, or expand/trim?
4. Want me to keep **speaker notes + visual cues** inline (PPT-ready) as done here, or lean markdown?
