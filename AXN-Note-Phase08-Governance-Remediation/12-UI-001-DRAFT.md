# UI-001 — Navigation and Adaptive UI Specification
Status: **DRAFT — NOT FROZEN**

## Evidence basis

- `01-OWNER/01-OWNER-DECISIONS-BASELINE.md` P0-12
- `02-FOUNDATION/03-FOUNDATION-AUDIT.md` §12
- `05-INDEPENDENT-CROSS-AUDIT/01-AUDIT-REPORT.md` §§16–17

## Owner-backed direction

Adaptive + Content-first UI with consistent information architecture across screen sizes.

## Specification coverage required

- navigation hierarchy
- mobile navigation
- large-screen navigation
- editor layout
- toolbar behavior
- search behavior
- Trash UI
- attachment UI
- settings
- empty states
- loading states
- error states
- destructive actions
- accessibility
- font scaling
- keyboard behavior
- state preservation where required

## Accessibility coverage

At minimum:
- TalkBack
- semantic labels
- focus order
- keyboard navigation
- font scaling
- touch target
- contrast
- state announcements
- error announcements
- reduced motion

## Event theme constraint

Event themes are presentation-only and may not alter data, navigation semantics, lifecycle, or security behavior.

## Closure rule

UI-001 must remain consistent with P0-12 and DATA/EDITOR lifecycles and must be tied to TEST-001.
