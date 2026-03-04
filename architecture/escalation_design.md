# Tiered Escalation Design

## Rationale

Binary alert systems create operational overload and increase false positives.
This framework implements a multi-tier escalation structure aligned with public-sector response models.

Escalation decisions are driven by:

- Composite crisis score
- Confidence level
- Governance safeguards

---

## Composite Crisis Score

The crisis score is calculated as:

CrisisScore =
(0.5 × Sentiment_Z) +
(0.3 × Volume_Z) +
(0.2 × GeoScore)

Where:

- Sentiment_Z captures deviation from baseline negativity
- Volume_Z captures abnormal spike in activity
- GeoScore captures spatial reinforcement from neighboring counties

---

## Escalation Thresholds (v1.1)

| Level | Threshold | Meaning                   | Operational Action         |
| ----- | --------- | ------------------------- | -------------------------- |
| 0     | < 2.5     | Monitor                   | No escalation              |
| 1     | ≥ 2.5    | Analyst Review            | Human analyst verification |
| 2     | ≥ 3.5    | Behavioral Health Office  | Regional coordination      |
| 3     | ≥ 4.5    | Multi-Agency Coordination | Cross-sector response      |

---

## Escalation Constraints

Escalation is automatically suppressed if:

- Confidence = LOW
- Governance filters detect amplification patterns
- Sample size < MIN_SAMPLE threshold

This prevents:

- Bot-driven escalation
- Media distortion events
- Sparse rural over-triggering

---

## Design Justification

Tiered escalation reduces operational overload while preserving sensitivity to significant statistical shifts.
The structure enables graduated response rather than binary alarm triggering.
