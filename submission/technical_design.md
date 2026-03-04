# Technical Design

## Architecture Overview

The framework follows a layered design:

Raw Input
→ Z-Score Normalization
→ Spatial Reinforcement
→ Composite Score
→ Governance Safeguards
→ Tiered Escalation
→ Audit Logging

---

## Composite Score Formula

CrisisScore =
(0.5 × Sentiment_Z) +
(0.3 × Volume_Z) +
(0.2 × GeoScore)

---

## Escalation Levels

| Level | Meaning                   |
| ----- | ------------------------- |
| 0     | Monitor                   |
| 1     | Analyst Review            |
| 2     | Behavioral Health Office  |
| 3     | Multi-Agency Coordination |

---

## Safeguards

- Minimum sample threshold
- Confidence gating
- Bot amplification filter
- Media spike filter

---

## Audit Design

All decisions are logged using a versioned JSON schema (v1.1).
This enables traceability and reproducibility.
