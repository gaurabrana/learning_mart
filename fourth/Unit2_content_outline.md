# Unit 2 — Data Modelling Using ER Model & Relational Model · Content Outline

**8 LHs → 8 sessions (S5–S12) · 50 min each**
This is the *content map* — what will fill each slot before we generate full material.
Local examples use Nepal / South Asia. Review and tell me what to swap.

> Template per session (from the guide):
> Opening hook (5m) → Content sections (35m) → Check for understanding (5m) →
> Real-life application (3m) → Summary & takeaways (2m), with speaker notes + visual cues.

---

## Unit 2 learning outcomes (what students can do after S5–S12)
1. Explain the database design process and the role of a high-level conceptual (ER) model in it.
2. Identify entity types, entity sets, and classify attributes (simple, composite, derived, multivalued) and keys.
3. Model relationship types/sets with roles and structural constraints (cardinality ratio, participation).
4. Recognize and diagram weak entity types using identifying relationships and partial keys.
5. Draw clean, correctly-named ER diagrams and avoid common design pitfalls.
6. Handle relationships of degree higher than two (ternary and beyond).
7. Apply specialization/generalization with disjoint/overlap and total/partial constraints.
8. Convert (map) a complete ER diagram into relational tables using the standard algorithm.

---

## S5 — High-Level Conceptual Data Models & the Database Design Process

**Hook:** "Before Daraz wrote a single line of code, someone drew boxes and lines on a whiteboard for *products*, *customers*, and *orders*. Why draw before you build?" → conceptual design comes first.

**Concepts & how each will be filled:**

1. **What a conceptual data model is (and why ER)**
   - Definition: a high-level, implementation-independent description of *what* data the system holds, not *how* it's stored.
   - Theory bullets: technology-neutral, easy for non-technical stakeholders, ER = most popular notation.
   - Global example: an airline reservation system modelled as Passenger/Flight/Booking before choosing Oracle vs MySQL.
   - Local example: modelling a college's exam system (Student, Course, Result) on a whiteboard before picking a DBMS.
   - Misconception: *"Modelling = drawing the database tables."* Correction: conceptual model is above tables; tables come later (S12).
   - Analogy: architect's floor plan before bricks are laid.

2. **The database design process (the full pipeline)**
   - Steps: Requirements collection & analysis → Conceptual design (ER) → Logical design (mapping to relational) → Physical design.
   - Theory bullets: each stage feeds the next; ER sits at conceptual; relational mapping (S12) is logical design.
   - Local example: building eSewa's wallet system — gather requirements from finance team → ER → tables → indexes/storage.
   - Mini case: "A team skips requirements gathering and starts coding tables; halfway, they realize 'wallet top-up source' was never captured" → rework cost.

3. **Requirements vs functional requirements**
   - Definition: data requirements (what to store) vs functional requirements (operations/transactions to support).
   - Local example: Khalti data req = users, transactions; functional req = "send money", "view statement".
   - Misconception: *"Requirements are only about data."* Correction: must also capture the operations the DB must support.

**Check for understanding:**
- MCQ1: Which design phase produces the ER diagram? (a) physical (b) conceptual ✅ (c) implementation (d) testing
- MCQ2: A conceptual model is independent of: → the specific DBMS/storage ✅
- Discussion: "Pick a Nepali app and list two data requirements and two functional requirements for it."

**Real-life application:** every software/data-engineering project in Nepal starts with requirements + a conceptual model; skipping it is the #1 cause of costly rework.

**Summary:** (1) conceptual models describe *what*, not *how*; (2) ER is the standard conceptual notation; (3) design flows requirements → conceptual → logical → physical. **Next:** the building blocks of ER — entities, attributes, and keys.

**Visual cues:** pipeline diagram "Requirements → Conceptual (ER) → Logical → Physical"; floor-plan-vs-house image. Mark slides [THEORY]/[EXAMPLE].

---

## S6 — Entity Types, Entity Sets, Attributes & Keys

**Hook:** "On the Nagarik App, *you* are a citizen, *your friend* is a citizen — same 'shape', different data. What's the shape, and what's the data?" → entity type vs entity.

**Concepts & how each will be filled:**

1. **Entity, Entity Type, Entity Set**
   - Definition: entity = a real-world thing; entity type = the schema/category; entity set = all entities of that type at a moment.
   - Theory bullets: entity type is design-time (like schema), entity set is instance-time (like instance — links back to S2).
   - Global example: Entity type STUDENT; one entity = student "Sita"; entity set = all enrolled students.
   - Local example: entity type CUSTOMER on Daraz; entity set = all registered Daraz customers today.
   - Misconception: *"Entity = a table row only."* Correction: an entity is the real-world thing; the row is its later representation.

2. **Attributes and their types**
   - Definition: properties that describe an entity.
   - Simple (atomic): citizenship_number; Composite: name = (first, middle, last), address = (district, municipality, ward); Derived: age (from DOB); Multivalued: phone_numbers, multiple emails; Stored vs derived contrast.
   - Local example: a college STUDENT — simple (roll_no), composite (full_name, address with district/ward), derived (semester from admission year), multivalued (contact numbers).
   - Mini case: "Daraz lets a user save *multiple* delivery addresses" → multivalued composite attribute.
   - Misconception: *"Age should be stored."* Correction: age is derived from DOB; storing it causes update anomalies.
   - Analogy: composite attribute = a postal address written on one line vs broken into fields.

3. **Keys (value constraints on entities)**
   - Definition: key/uniqueness constraint — an attribute (or set) whose value is unique per entity.
   - Types: candidate key, primary key, composite key; key attribute underlined in ER.
   - Local example: citizenship number or national ID as a key for a citizen; roll_no + program for a student.
   - Misconception: *"Name can be a key."* Correction: names repeat; use citizenship/ID/roll number.

**Check for understanding:**
- MCQ1: "age" computed from date of birth is a: (a) stored (b) multivalued (c) derived ✅ (d) composite attribute
- MCQ2: All STUDENT entities at one moment form the: → entity set ✅
- Discussion: "List the attributes of a Khalti user account and label each simple/composite/derived/multivalued."

**Real-life application:** correctly classifying attributes (especially multivalued and derived) decides table design later and prevents data duplication in real systems.

**Summary:** (1) entity type = category, entity set = current members; (2) attributes come in simple/composite/derived/multivalued flavors; (3) keys uniquely identify entities. **Next:** how entities *connect* — relationships and their constraints.

**Visual cues:** ER fragment showing oval attribute types (composite=tree, multivalued=double oval, derived=dashed oval, key=underlined); attribute classification table.

---

## S7 — Relationship Types, Sets, Roles & Structural Constraints

**Hook:** "A student *enrolls in* a course; a customer *places* an order. Those verbs are where the real modelling happens." → relationships.

**Concepts & how each will be filled:**

1. **Relationship Type, Relationship Set, Degree**
   - Definition: relationship type = association among entity types; relationship set = current set of associations; degree = number of participating entity types (binary = 2).
   - Global example: WORKS_FOR between EMPLOYEE and DEPARTMENT.
   - Local example: ENROLLS between STUDENT and COURSE; PLACES between CUSTOMER and ORDER on Daraz.
   - Misconception: *"A relationship is just a foreign key."* Correction: at conceptual level it's a real-world association; FKs are the later implementation.

2. **Roles and Recursive (self) relationships**
   - Definition: role name = the part an entity plays in a relationship; recursive relationship = same entity type on both ends, needing role names.
   - Local example: EMPLOYEE *supervises* EMPLOYEE at Ntc — roles "supervisor" and "supervisee".
   - Mini case: a college where a senior student *mentors* a junior student → recursive MENTORS relationship.

3. **Structural constraints — Cardinality Ratio**
   - Definition: max number of relationship instances an entity can participate in: 1:1, 1:N, N:1, M:N.
   - Examples: 1:1 (CITIZEN — PASSPORT), 1:N (DEPARTMENT — EMPLOYEE), M:N (STUDENT — COURSE), and Daraz ORDER — PRODUCT (M:N).
   - Misconception: *"M:N can be stored directly as-is."* Correction: M:N needs a junction table later (preview S12).

4. **Structural constraints — Participation (total vs partial)**
   - Definition: total participation (every entity must participate, double line) vs partial (may participate, single line).
   - Local example: every LOAN must belong to a CUSTOMER (total); not every CUSTOMER has a loan (partial) at a local bank like NIC Asia.
   - Analogy: total participation = a mandatory field on a form; partial = optional field.

**Check for understanding:**
- MCQ1: "One department has many employees, each employee in one department" is: (a) 1:1 (b) 1:N ✅ (c) M:N (d) recursive
- MCQ2: A double line from an entity to a relationship means: → total participation ✅
- Discussion: "On eSewa, model the relationship between USER and TRANSACTION — what's its cardinality and participation?"

**Real-life application:** cardinality + participation directly drive whether you get a foreign key or a junction table — the core of correct schema design.

**Summary:** (1) relationships are associations with a degree; (2) roles name the parts (vital for recursive ones); (3) two structural constraints — cardinality ratio and participation. **Next:** entities that can't stand on their own — weak entities.

**Visual cues:** diamond-notation diagrams; cardinality table (1:1/1:N/M:N) with examples; single vs double line participation graphic.

---

## S8 — Weak Entity Types (Identifying Relationship, Partial Key)

**Hook:** "An 'order item' on Daraz means nothing without its order. Delete the order — the line items vanish. Some entities can't exist alone." → weak entities.

**Concepts & how each will be filled:**

1. **Weak vs Strong (regular) entity types**
   - Definition: weak entity = has no key attribute of its own; identified only through another (owner/identifying) entity.
   - Theory bullets: drawn with double rectangle; depends on owner for identity.
   - Global example: DEPENDENT (of an employee) — two employees can both have a child "Ram"; needs employee to identify.
   - Local example: ORDER_ITEM depends on ORDER on Daraz; INSTALLMENT depends on LOAN at a bank.
   - Misconception: *"Weak = unimportant / optional."* Correction: 'weak' means *identity-dependent*, not low-priority.

2. **Identifying (owner) relationship**
   - Definition: the relationship that connects the weak entity to its owner; drawn as a double diamond; always total participation on the weak side.
   - Local example: LOAN —has→ INSTALLMENT is the identifying relationship.
   - Analogy: a hotel room number (101) only makes sense *within* a specific hotel.

3. **Partial key (discriminator)**
   - Definition: an attribute that distinguishes weak entities of the *same owner*; underlined with a dashed line.
   - Full identity = owner's key + partial key (e.g., LOAN_id + installment_no).
   - Mini case: installment "3" exists for many loans; only LOAN_id 4521 + installment 3 is unique.
   - Misconception: *"Partial key alone is unique."* Correction: it's unique only within one owner; combine with owner key.

**Check for understanding:**
- MCQ1: A weak entity is one that: (a) is unimportant (b) has no key of its own ✅ (c) has no attributes (d) is always 1:1
- MCQ2: The full identifier of a weak entity is: → owner's primary key + its partial key ✅
- Discussion: "Find a weak entity in a Nepali app (e.g., a comment on a Facebook post, a room in a hotel booking) and name its owner + partial key."

**Real-life application:** invoice line-items, loan installments, exam answer-sheets per exam — weak entities appear in almost every real system; modelling them wrong corrupts data integrity.

**Summary:** (1) weak entities have no key of their own; (2) an identifying relationship (double diamond) ties them to an owner; (3) identity = owner key + partial key. **Next:** putting it all together into clean ER diagrams.

**Visual cues:** double-rectangle + double-diamond + dashed-underline diagram; side-by-side strong vs weak entity comparison.

---

## S9 — ER Diagrams, Naming Conventions & Design Issues

**Hook:** "Here are two ER diagrams of the *same* college system — one is clear, one is a spaghetti mess. What makes the difference?" → conventions and good design choices.

**Concepts & how each will be filled:**

1. **ER notation recap (one consolidated legend)**
   - Definition: full symbol set — rectangle (entity), double rectangle (weak), oval (attribute), diamond (relationship), double diamond (identifying), lines/double lines (participation), underline (key), dashed underline (partial key).
   - Local example: a complete small ER diagram for a college (STUDENT, COURSE, ENROLLS, DEPARTMENT).
   - Visual: one "cheat sheet" legend slide.

2. **Naming conventions**
   - Theory bullets: entity types = singular nouns (STUDENT not STUDENTS), relationships = verbs (ENROLLS, WORKS_FOR), consistent case, meaningful names; relationship reads left-to-right as a sentence.
   - Misconception: *"Naming doesn't matter, it's just a diagram."* Correction: bad names cause miscommunication and mapping errors later.
   - Mini case: relationship named "REL1" vs "TEACHES" — which can a non-technical stakeholder verify?

3. **Design issues / common pitfalls**
   - Attribute vs entity: should "department" be an attribute of STUDENT or its own entity? (depends on whether it has its own attributes/relationships).
   - Attribute vs relationship; binary vs combining into one entity.
   - Local example: on Daraz, is "category" an attribute of PRODUCT or a separate CATEGORY entity? → entity, because categories have their own data.
   - Misconception: *"More entities = better design."* Correction: over-modelling adds needless complexity; model what the requirements need.
   - Analogy: choosing whether 'colour' is a sticker on a box (attribute) or a whole separate filing cabinet (entity).

**Check for understanding:**
- MCQ1: Best name for an entity type representing course-takers: (a) ENROLLS (b) STUDENTS (c) STUDENT ✅ (d) TBL1
- MCQ2: You should model X as a separate entity (not an attribute) when: → it has its own attributes/relationships ✅
- Discussion: "For an eSewa-like app, decide whether 'merchant' should be an attribute of TRANSACTION or its own entity, and justify."

**Real-life application:** clean, well-named ER diagrams are the shared language between business analysts, developers, and DBAs in every Nepali IT company.

**Summary:** (1) one consistent notation legend; (2) singular-noun entities, verb relationships; (3) watch the attribute-vs-entity-vs-relationship design decisions. **Next:** when two entities aren't enough — higher-degree relationships.

**Visual cues:** ER symbol cheat-sheet; "good vs messy" ER diagram comparison; attribute-vs-entity decision flowchart.

---

## S10 — Relationship Types of Degree Higher Than Two (Ternary etc.)

**Hook:** "A supplier *supplies* a product *for* a project. Three things in one fact — can a normal two-sided arrow capture that?" → ternary relationships.

**Concepts & how each will be filled:**

1. **Degree of a relationship revisited**
   - Definition: binary (2 entity types), ternary (3), n-ary (n); recap from S7.
   - Global example: SUPPLY(SUPPLIER, PART, PROJECT) — the classic ternary.
   - Local example: a college timetable — TEACHES(TEACHER, COURSE, ROOM/TIMESLOT) as a ternary fact.

2. **Why a ternary is NOT always three binaries**
   - Theory bullets: three separate binary relationships lose information that the *combination* is what matters.
   - Mini case: "Supplier S supplies Part P" + "Part P used in Project J" + "Supplier S works on Project J" does NOT tell us S supplied P *to* J — only the ternary does.
   - Misconception: *"Any ternary can be split into binaries without loss."* Correction: sometimes it loses meaning; depends on constraints.
   - Analogy: a three-way handshake/contract vs three separate two-person agreements.

3. **Constraints on higher-degree relationships**
   - Cardinality on n-ary relationships; when to introduce an intermediate (associative) entity instead.
   - Local example: a food-delivery (Foodmandu/Pathao Food) DELIVERY linking CUSTOMER, RESTAURANT, RIDER — model as ternary or as an associative DELIVERY entity.
   - Misconception: *"Higher-degree relationships are common."* Correction: most real designs are binary; ternary is occasional, n>3 rare.

**Check for understanding:**
- MCQ1: A relationship among three entity types is called: (a) binary (b) recursive (c) ternary ✅ (d) weak
- MCQ2: Splitting a ternary into three binaries is risky because: → it can lose the combined-fact meaning ✅
- Discussion: "Model a Pathao ride that involves a RIDER, a PASSENGER, and a LOCATION/ROUTE — is a ternary justified, or would an associative entity be cleaner?"

**Real-life application:** logistics, delivery, and booking systems (very common in Nepal's startup scene) frequently need ternary thinking; getting it wrong silently loses business facts.

**Summary:** (1) degree = number of participating entity types; (2) ternary ≠ three binaries when the combination carries meaning; (3) prefer binary, use ternary/associative entities only when needed. **Next:** modelling "is-a" hierarchies with specialization and generalization.

**Visual cues:** ternary diamond connecting three entities; "ternary vs three-binaries" loss-of-information illustration; associative-entity conversion diagram.

---

## S11 — Specialization & Generalization · Their Constraints & Characteristics

**Hook:** "On the Nagarik App, a USER can be a citizen, a government employee, or a business owner — same person-record, but each kind stores extra things. How do we model 'kinds of'?" → specialization/generalization.

**Concepts & how each will be filled:**

1. **Specialization & Generalization (EER concepts)**
   - Definition: specialization = top-down, splitting a superclass into subclasses (EMPLOYEE → ENGINEER, SECRETARY); generalization = bottom-up, combining similar entities into a superclass.
   - Theory bullets: subclass inherits superclass attributes + relationships; "is-a" relationship.
   - Global example: VEHICLE generalizing CAR and TRUCK.
   - Local example: ACCOUNT at a bank specialized into SAVINGS and CURRENT; USER on a platform → CUSTOMER and MERCHANT.
   - Misconception: *"Specialization and generalization are different tools."* Correction: they're inverse directions of the same modelling idea.
   - Analogy: biological taxonomy (animal → mammal → dog).

2. **Disjoint vs Overlap constraint**
   - Definition: disjoint (d) = an entity belongs to at most one subclass; overlap (o) = can belong to several.
   - Local example: disjoint — a bank ACCOUNT is either SAVINGS or CURRENT, not both; overlap — a college PERSON can be both STUDENT and STAFF (teaching assistant).
   - Misconception: *"Subclasses are always mutually exclusive."* Correction: overlap is allowed and common.

3. **Total vs Partial (completeness) constraint**
   - Definition: total/total specialization = every superclass member must belong to some subclass (double line); partial = some may belong to none.
   - Local example: total — every EMPLOYEE is either PERMANENT or CONTRACT; partial — a VEHICLE that is neither CAR nor TRUCK (e.g., a bus) when only those two subclasses exist.
   - Combined: four combinations (disjoint-total, disjoint-partial, overlap-total, overlap-partial) summarized in a 2×2.

4. **Attribute inheritance & specific (local) attributes**
   - Subclass gets superclass attributes plus its own (e.g., SAVINGS has interest_rate, CURRENT has overdraft_limit).

**Check for understanding:**
- MCQ1: "Every employee must be either permanent or contract" is a ___ constraint: (a) overlap (b) disjoint (c) total ✅ (d) partial
- MCQ2: A subclass automatically receives the superclass's attributes via: → inheritance ✅
- Discussion: "On a platform like Daraz, model USER → CUSTOMER and SELLER. Is it disjoint or overlap? Total or partial? Justify."

**Real-life application:** banking (account types), HR (employee types), and e-commerce (user roles) systems all rely on specialization; choosing disjoint/total correctly prevents impossible or missing records.

**Summary:** (1) specialization (down) and generalization (up) are inverses sharing inheritance; (2) disjoint vs overlap controls multi-membership; (3) total vs partial controls mandatory subclass membership. **Next:** turning all of these ER constructs into real tables.

**Visual cues:** "is-a" triangle/circle notation with d/o symbol; 2×2 grid of (disjoint/overlap × total/partial); inheritance arrow diagram.

---

## S12 — Converting ER Diagrams to Tables (Mapping Algorithm) — closes Unit 2

**Hook:** "We've drawn beautiful diagrams. But MySQL doesn't understand diamonds and ovals — it understands *tables*. How do we translate?" → the ER-to-relational mapping algorithm.

**Concepts & how each will be filled:**

1. **The 7-step mapping algorithm (overview)**
   - Step 1: Strong/regular entity → table with its simple attributes; choose primary key.
   - Step 2: Weak entity → table including the owner's primary key as part of its (composite) primary key (owner key + partial key).
   - Step 3: 1:1 relationship → add foreign key to one side (the total-participation side preferred).
   - Step 4: 1:N relationship → put the FK on the "N" (many) side.
   - Step 5: M:N relationship → create a new junction/relationship table with both primary keys as a composite key.
   - Step 6: Multivalued attribute → create a separate table (with the entity's key + the value).
   - Step 7: Higher-degree (n-ary) relationship → create a table with the keys of all participating entities.
   - Theory bullets: composite attributes are flattened to their simple components; derived attributes are NOT stored.

2. **Worked mapping — a small Nepali system end-to-end**
   - Local example: map a college ER (STUDENT, COURSE, ENROLLS M:N, DEPARTMENT 1:N, student phone multivalued) into tables — show STUDENT, COURSE, DEPARTMENT, ENROLLS junction, STUDENT_PHONE tables with keys/FKs.
   - Mini case: map Daraz CUSTOMER—PLACES—ORDER (1:N) and ORDER—CONTAINS—PRODUCT (M:N) → ORDER gets customer_id FK; an ORDER_ITEM junction table for products.

3. **Mapping specialization/generalization (link to S11)**
   - Brief: options — one table per subclass, single table with type field, etc. (kept light; full normalization is Unit 4).

4. **Common mapping mistakes**
   - Misconception: *"M:N can be one table with a list of products in a column."* Correction: needs a separate junction table (atomic rows).
   - Misconception: *"Put the FK on the 1 side of a 1:N."* Correction: FK goes on the N side.
   - Misconception: *"Store derived attributes like age/total."* Correction: leave derived out; compute on query.

**Check for understanding:**
- MCQ1: An M:N relationship maps to: (a) a FK on either side (b) a new junction table ✅ (c) nothing (d) a derived attribute
- MCQ2: In a 1:N relationship the foreign key is placed on the: → N (many) side ✅
- Discussion: "Take the eSewa USER—TRANSACTION model from S7 and write out the tables (with keys and FKs) it maps to."

**Real-life application:** this is the exact step every developer does between design and `CREATE TABLE` (Unit 5) — the bridge from theory to a running database in any Nepali tech job.

**Summary:** (1) a 7-step algorithm mechanically turns ER into tables; (2) FK on the N side, junction table for M:N, separate table for multivalued/weak; (3) don't store derived data. **Next unit:** querying these tables formally with relational algebra and calculus (Unit 3).

**Visual cues:** the 7-step mapping table (ER construct → relational result); before/after diagram (ER fragment → table schemas with keys/FKs); junction-table illustration.

---

## END-OF-UNIT QUIZ (Unit 2 consolidated)

*Use after S12 for revision/assessment. Mix of recall and applied. Answers marked ✅.*

### Part A — Multiple Choice (12)
1. The ER model is used mainly at which design phase? (a) physical (b) **conceptual ✅** (c) testing (d) tuning
2. All students enrolled today form a/an: (a) entity type (b) **entity set ✅** (c) attribute (d) relationship type
3. "Age" derived from date of birth is a/an ___ attribute: (a) simple (b) composite (c) **derived ✅** (d) multivalued
4. A user's multiple saved phone numbers is a/an ___ attribute: (a) simple (b) composite (c) derived (d) **multivalued ✅**
5. "One department, many employees" is cardinality: (a) 1:1 (b) **1:N ✅** (c) M:N (d) recursive
6. A double line between an entity and a relationship denotes: (a) partial (b) **total participation ✅** (c) M:N (d) weak entity
7. A weak entity is one that: (a) is unimportant (b) **has no key of its own ✅** (c) has no attributes (d) is always 1:1
8. The full identifier of a weak entity = (a) its partial key only (b) **owner's primary key + partial key ✅** (c) any attribute (d) a derived attribute
9. A relationship among three entity types is: (a) binary (b) recursive (c) **ternary ✅** (d) weak
10. "An account is either savings or current, never both" is a ___ constraint: (a) overlap (b) **disjoint ✅** (c) total (d) partial
11. An M:N relationship is mapped to: (a) FK on either side (b) **a junction table ✅** (c) nothing (d) a derived column
12. In a 1:N relationship, the foreign key goes on the: (a) 1 side (b) **N side ✅** (c) both sides (d) neither

### Part B — Short Answer (5)
1. Differentiate entity type vs entity set with one example each.
2. List the four attribute types and give a Nepali example of each.
3. Define cardinality ratio and participation constraint; how do they differ?
4. Explain why a weak entity needs an identifying relationship and a partial key.
5. State the difference between disjoint and overlap specialization constraints.

### Part C — Diagramming / Applied (3)
1. Draw an ER diagram for a **college library**: MEMBER, BOOK, BORROWS (with date), a book has multiple COPIES (weak entity). Mark keys, partial key, cardinality, and participation.
2. Given an ER fragment for **Daraz** (CUSTOMER 1:N ORDER, ORDER M:N PRODUCT, customer has multiple ADDRESSES), apply the mapping algorithm and write all resulting tables with primary keys and foreign keys.
3. For a banking USER, model a specialization into CUSTOMER and EMPLOYEE. Decide and justify the disjoint/overlap and total/partial constraints, then list each subclass's specific attributes.

### Part D — Discussion / Critical Thinking (2)
1. A teammate models a food-delivery fact as three separate binary relationships (customer–restaurant, restaurant–rider, rider–customer). Explain what information is lost and when a ternary relationship is the right call.
2. When should a real-world concept (e.g., "category" on Daraz) be modelled as an attribute vs its own entity? Argue both sides with examples.

---

## Open questions before I generate Unit 2 material
1. Keep all the **Nepali examples** above (eSewa/Khalti/Daraz/Nagarik App/Pathao/Foodmandu/local banks), or swap any?
2. Should the EER specialization/generalization mapping in S12 be kept **light** (as now) or expanded, given full normalization is Unit 4?
3. Quiz depth — is the **per-session 2 MCQ + 1 discussion PLUS this end-of-unit quiz** the right balance, or trim one?
4. Do you want the **ER notation** standardized to Elmasri/Navathe (the prescribed text) or Chen/crow's-foot, before I draw the diagrams?
