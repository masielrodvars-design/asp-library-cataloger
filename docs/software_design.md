# Cataloging Pipeline

Every book follows the same workflow from import to publication.

```
Import
    ↓
Quality Check
    ↓
Metadata Enrichment
    ↓
Rules Engine
    ↓
AI Recommendations
    ↓
Human Review
    ↓
Learning
    ↓
Publish
```

Each stage has a single responsibility.

No stage should duplicate the work of another stage.

---

## Stage 1 — Import

Purpose:

Read books from external sources and create internal Book records.

Supported sources:

- Goodreads
- Excel
- CSV

Future:

- Google Sheets
- Airtable

Output:

Book objects.

---

## Stage 2 — Quality Check

Purpose:

Identify missing or suspicious information before cataloging begins.

Examples:

- Missing ISBN
- Duplicate ISBN
- Missing author
- Invalid publication year

Output:

Quality report.

---

## Stage 3 — Metadata Enrichment

Purpose:

Collect authoritative information.

Priority:

1. Open Library
2. Google Books
3. Publisher metadata

Retrieve:

- Language
- Subjects
- Description
- Audience
- Publisher
- Publication year
- Cover image

Output:

Enriched Book.

---

## Stage 4 — Rules Engine

Purpose:

Apply organization-specific cataloging standards.

Examples:

Spanish language

↓

SP Collection

Graphic novel

↓

J GN

Picture book

↓

E

Output:

Recommended catalog fields.

---

## Stage 5 — AI Recommendations

Purpose:

Make recommendations where rules cannot.

Examples:

Themes

Representation

SEL

Reading level

Output:

Recommendations with confidence scores and explanations.

---

## Stage 6 — Human Review

Purpose:

Approve or modify recommendations.

Humans always make final cataloging decisions.

---

## Stage 7 — Learning

Purpose:

Remember approved decisions.

Future recommendations should improve over time.

---

## Stage 8 — Publishing

Purpose:

Generate the organization's official catalog.

Supported formats:

- Excel
- Google Sheets
- Airtable
- CSV