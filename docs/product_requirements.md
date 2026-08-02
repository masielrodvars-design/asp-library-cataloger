# Product Requirements Document (PRD)

# Small Library Cataloger

Version: 1.0 (Draft)

Owner: Masiel Rodriquez-Vars

Primary Implementation Partner: Montclair Fund for Educational Excellence (MFEE)

---

# Purpose

Small Library Cataloger is a configurable library catalog management platform that helps schools, nonprofits, classrooms, and community libraries build and maintain professional-quality catalogs with minimal manual effort.

The product combines authoritative metadata, configurable cataloging standards, artificial intelligence, and human review to streamline catalog creation while ensuring people remain in control of final cataloging decisions.

---

# Product Goals

The software should:

- Reduce manual cataloging work by at least 90%
- Maintain consistent cataloging standards
- Support volunteer participation
- Produce professional-quality catalogs
- Learn from user corrections
- Remain configurable for different organizations
- Preserve complete ownership of catalog data

---

# Target Users

## Library Manager

Responsible for:

- Managing the catalog
- Approving recommendations
- Configuring cataloging standards
- Publishing the official catalog

Needs:

- Accuracy
- Transparency
- Efficiency

---

## Volunteer Reviewer

Responsible for:

- Reviewing recommendations
- Correcting mistakes
- Completing catalog records

Needs:

- Simplicity
- Clear explanations
- Minimal training

---

## Organization Administrator

Responsible for:

- Managing users
- Organization settings
- Integrations
- Reporting

Needs:

- Reliability
- Security
- Easy administration

---

# Core Workflow

Every book follows the same lifecycle.

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

Publishing

---
# Organizations

The system shall support multiple organizations.

Each organization represents an independent library and stores its own cataloging standards and configuration.

An organization may define:

- Collection codes
- Call number conventions
- Themes
- Representation tags
- Format tags
- Review workflows
- Export preferences
- Branding
- Metadata preferences
- AI configuration (future)

Each organization's catalog data shall remain separate from all other organizations.

MFEE will serve as the primary implementation and testing organization during initial development.

# Functional Requirements

## Import

The system shall:

- Import Goodreads exports
- Import Excel workbooks
- Import CSV files
- Detect duplicate books
- Validate imported data

Future:

- Google Sheets
- Airtable

---

## Metadata

The system shall retrieve:

- Language
- Publisher
- Publication year
- Subjects
- Description
- Audience
- Cover image
- ISBN validation

The system shall cache metadata to avoid repeated lookups.

---

## Catalog Intelligence

The system shall recommend:

- Collection
- Call Number
- Themes
- Representation Tags
- Format Tags

Every recommendation shall include:

- Confidence score
- Explanation
- Supporting evidence

---

## Human Review

The system shall allow users to:

Approve recommendations

Reject recommendations

Modify recommendations

Leave review notes

Every approved decision becomes the organization's official catalog.

---

## Learning

The system shall:

Record user overrides

Improve future recommendations

Remember organization preferences

---

## Publishing

The system shall export:

Excel

Google Sheets

CSV

Future:

Airtable synchronization

Reports

Shelf labels

---

# Non-Functional Requirements

The product should:

Be easy for volunteers to learn.

Be configurable without programming.

Support organizations with thousands of books.

Remain independent of any single spreadsheet platform.

Protect organization data.

Support future cloud deployment.

---

# Success Metrics

Version 1 is successful when:

A Goodreads export can be transformed into a review-ready catalog.

At least 90% of books receive usable recommendations.

Only low-confidence recommendations require human review.

The complete workflow can be completed by a volunteer with minimal training.

---

# Out of Scope (Version 1)

The following features are intentionally excluded from Version 1:

Book circulation

Patron management

Fines

Reservations

Public OPAC

Barcode checkout

Inventory scanning

Mobile application

These features may be considered in future versions.

---

# Future Vision

Potential future capabilities include:

Inventory management

QR codes

Reading lists

Book recommendations

Classroom libraries

Multiple organizations

Multi-user collaboration

Permissions

Cloud hosting

API integrations

Web application

Analytics dashboard

Plugin architecture

---

# Product Principles

Human expertise comes first.

AI recommends.

People decide.

Recommendations should always be explainable.

Organizations own their data.

Cataloging standards should be configurable.

The software should continuously improve through human feedback.