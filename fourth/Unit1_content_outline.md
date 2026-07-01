# Unit 1 — Database Concepts & Architecture · Content Outline

**4 LHs → 4 sessions (S1–S4) · 50 min each**
This is the *content map* — what will fill each slot before we generate full material.
Local examples use Nepal / South Asia. Review and tell me what to swap.

> Template per session (from the guide):
> Opening hook (5m) → Content sections (35m) → Check for understanding (5m) →
> Real-life application (3m) → Summary & takeaways (2m), with speaker notes + visual cues.

---

## Unit 1 learning outcomes (what students can do after S1–S4)
1. Define database, DBMS, and the roles around it; explain why a DBMS beats flat files.
2. Distinguish data models, schemas, and instances.
3. Explain the three-schema architecture and the two kinds of data independence.
4. Identify database languages/interfaces and components of the DBMS environment.
5. Compare centralized vs client/server architecture and classify DBMSs.

---

## S1 — What is a Database & DBMS? (Users, DBA, advantages)

**Hook:** "Your eSewa balance, your college's exam results, and your Facebook feed all survive a phone reboot. Where do they actually *live*?" → everything is a database.

**Concepts & how each will be filled:**

1. **Data vs Information vs Database**
   - Definition: data = raw facts; database = organized, related collection of data.
   - Theory bullets: persistent, shared, structured.
   - Global example: a bank's account ledger.
   - Local example: a college's student record system (e.g. TU/Pokhara University exam DB).
   - Mini case: "A kirana shop tracks stock in a notebook" → why that's a 'database' but a fragile one.

2. **DBMS (Database Management System)**
   - Definition: software that lets users define, create, query, and administer databases.
   - Theory: examples — MySQL, PostgreSQL, Oracle, SQL Server.
   - Misconception: *"Excel is a database."* Correction: spreadsheet ≠ DBMS (no concurrency, integrity, querying at scale).
   - Fun element: analogy — DBMS = a librarian; data = books; without the librarian you just have a pile.

3. **Database users**
   - Naive/end users, application programmers, sophisticated users, DBA — one line each.
   - Local example: at a bank — teller (naive), the core-banking dev (app programmer), the data analyst (sophisticated), the DBA.

4. **Database Administrator (DBA)**
   - Definition + responsibilities: schema design, security/permissions, backups, tuning.
   - Mini case: "Who do you call when the exam-result server is slow the night before results?" → the DBA.

5. **Advantages of databases over file systems**
   - Controlled redundancy, consistency, integrity, sharing, security, backup/recovery.
   - Misconception: *"More copies = safer."* Correction: uncontrolled redundancy causes inconsistency.

**Check for understanding:**
- MCQ1: Which is NOT a function of a DBMS? (a) define data (b) print documents ✅ (c) query (d) control access
- MCQ2: Who is responsible for granting user permissions? → DBA ✅
- Discussion: "Name one app on your phone and guess what its database stores."

**Real-life application:** every fintech/e-commerce job in Nepal (eSewa, Khalti, Daraz) runs on a DBMS — this is foundational employability.

**Summary:** (1) Database = organized shared data; (2) DBMS manages it; (3) beats files via controlled redundancy, integrity, security. **Next:** how we *describe* data — models, schemas, instances.

**Visual cues:** diagram "Users → DBMS → Database"; comparison table File System vs DBMS. Mark slides [THEORY]/[EXAMPLE].

---

## S2 — Data Models, Schemas & Instances · Three-Schema Architecture & Data Independence

**Hook:** "When the college changes how grades are stored internally, why don't *you* (the student checking marks) notice anything?" → data independence.

**Concepts & how each will be filled:**

1. **Data models**
   - Definition: a set of concepts to describe structure + constraints + operations.
   - Categories: high-level/conceptual (ER), representational (relational), low-level/physical.
   - Analogy: blueprint (conceptual) vs built house (physical).

2. **Schema vs Instance**
   - Schema = the design/structure (changes rarely); instance = the data at a moment (changes constantly).
   - Local example: schema = "Student(roll, name, program)"; instance = today's actual 60 students.
   - Misconception: *"Schema and data are the same thing."* Correction: schema is the mold, instance is what's poured in.

3. **Three-Schema Architecture**
   - Internal level (physical storage), conceptual level (whole-DB logical), external level (per-user views).
   - Diagram-heavy slide: three stacked layers + mappings.
   - Local example: external view = "student sees only own marks"; conceptual = full exam DB; internal = how it's stored on disk.

4. **Data independence**
   - Logical data independence: change conceptual schema w/o touching external views.
   - Physical data independence: change storage w/o touching conceptual schema.
   - Mini case: "DB admin moves data to faster SSDs overnight — apps keep working" → physical independence.

**Check for understanding:**
- MCQ1: Adding a new column without breaking existing user views = which independence? → logical ✅
- MCQ2: Which level is closest to physical storage? → internal ✅
- Discussion: "Give an everyday example of 'changing the inside without changing the outside.'"

**Real-life application:** data independence is *why* large systems (banks, telecoms like Ntc/Ncell) can upgrade storage without rewriting every app.

**Summary:** (1) models describe data at 3 abstraction levels; (2) schema = structure, instance = current data; (3) two independences insulate users from change. **Next:** the languages and interfaces we use to talk to a DBMS.

**Visual cues:** the three-schema pyramid is the centerpiece visual; schema-vs-instance side-by-side table.

---

## S3 — Database Languages & Interfaces · The Database System Environment

**Hook:** "There are different 'languages' to talk to a database — one to *build* it, one to *use* it, one to *protect* it. Which have you already heard of?"

**Concepts & how each will be filled:**

1. **Database languages**
   - DDL (define schema), DML (query/modify), DCL (permissions), TCL (commit/rollback) — one line + tiny SQL teaser each (full SQL is Unit 5).
   - Mini case: registering a new course = DDL; enrolling a student = DML; giving a TA read access = DCL.
   - Misconception: *"SQL is one single language."* Correction: SQL bundles DDL+DML+DCL+TCL.

2. **Interfaces to a DBMS**
   - Menu-based, form-based, GUI, natural language, app-program interfaces (APIs/embedded SQL).
   - Local example: a bank teller's form-based screen vs a developer using SQL directly.

3. **The Database System Environment (components)**
   - DBMS components: query processor, storage manager, buffer manager, transaction manager, catalog/metadata.
   - Diagram: layered DBMS internals.
   - Fun element: analogy — restaurant: waiter (query processor), kitchen (storage), receipts (catalog), manager (transaction mgr).

4. **Data dictionary / catalog**
   - Definition: "database about the database" (metadata).
   - Local example: the system table that knows every table name in the college DB.

**Check for understanding:**
- MCQ1: `CREATE TABLE` belongs to which language? → DDL ✅
- MCQ2: Which component decides the cheapest way to run a query? → query processor/optimizer ✅
- Discussion: "Which DBMS interface would you build for a non-technical shopkeeper, and why?"

**Real-life application:** knowing DDL/DML/DCL is the literal day-1 skill in any backend/data role.

**Summary:** (1) DDL/DML/DCL/TCL each have a job; (2) many interface styles for many users; (3) DBMS = several cooperating components + a catalog. **Next:** *where* the database runs — centralized vs client/server, and how we classify DBMSs.

**Visual cues:** language-to-purpose table; DBMS component block diagram.

---

## S4 — Centralized vs Client/Server Architectures · Classification of DBMSs (closes Unit 1)

**Hook:** "When 5,000 students refresh their results at the same minute, what stops the system from collapsing?" → architecture matters.

**Concepts & how each will be filled:**

1. **Centralized architecture**
   - Definition: everything (data + DBMS + apps) on one central machine; terminals just display.
   - Pros/cons: simple vs single point of failure.
   - Local example: an old standalone office system on one PC.

2. **Client/Server architecture**
   - Two-tier vs three-tier; where the DBMS sits vs the app logic vs the UI.
   - Diagram: client ↔ app server ↔ DB server.
   - Local example: Daraz app (client) → app servers → database servers.
   - Mini case: "Why a mobile banking app doesn't store your full ledger on the phone" → server-side data.

3. **Classification of DBMSs**
   - By data model: relational, object, object-relational, hierarchical/network (legacy), NoSQL (preview of Unit 7).
   - By number of users: single-user vs multi-user.
   - By distribution: centralized vs distributed (preview of Unit 7).
   - Misconception: *"NoSQL means 'no SQL / SQL is dead.'"* Correction: it means 'not only SQL'; relational still dominates.

4. **Unit 1 synthesis**
   - One slide tying users → models/schemas → languages → architecture into one picture.

**Check for understanding:**
- MCQ1: Main weakness of a purely centralized system? → single point of failure ✅
- MCQ2: A three-tier architecture adds which layer between client and DB? → application/business-logic server ✅
- Discussion: "Pick a Nepali app and sketch whether it's two-tier or three-tier."

**Real-life application:** every scalable product (e-commerce, fintech, gov portals like Nagarik App) is client/server — this frames the rest of the course.

**Summary:** (1) centralized = simple but fragile; (2) client/server (esp. 3-tier) = scalable standard; (3) DBMSs classify by model, users, distribution. **Next unit:** modelling real-world data with the ER model.

**Visual cues:** centralized vs 2-tier vs 3-tier comparison diagram; classification mind-map.

---

## Open questions before I generate Unit 1 material
1. Keep all the **Nepali examples** above (eSewa/Khalti/Daraz/Ntc/Nagarik App), or prefer different ones?
2. Quiz depth — is **2 MCQs + 1 discussion per session** right, or do you want a larger end-of-unit quiz instead?
3. Should I include **speaker notes** and **visual/diagram suggestions** inline (good for PPT later), or keep the markdown lean?
4. After you approve this, do you want me to outline **Units 2–7** the same way *before* generating anything, or generate Unit 1 material now and outline later units as we reach them?
