# Data Flow Architecture

## Overview

This document describes how data moves through the Crisis Escalation Framework from input to final escalation decision.

---

## Step-by-Step Flow

### 1. County Input

Input structure:

- sentiment
- volume
- amplification_ratio
- event_similarity

Baseline statistics:

- mean_sentiment
- std_sentiment
- mean_volume
- std_volume

Neighboring county Z-scores:

- Used for spatial reinforcement scoring

---

### 2. Z-Score Normalization

Sentiment and volume are normalized:

Sentiment_Z = -1 × ((current - mean) / std)

Volume_Z = (current - mean) / std

Negative sentiment deviation increases crisis intensity.

---

### 3. Spatial Reinforcement

Neighboring county Z-scores are evaluated.

If multiple adjacent counties show elevated Z-scores,
a GeoScore is applied to reinforce the composite crisis signal.

---

### 4. Composite Crisis Score

CrisisScore =
(0.5 × Sentiment_Z) +
(0.3 × Volume_Z) +
(0.2 × GeoScore)

This balances emotional intensity, activity surge, and geographic clustering.

---

### 5. Governance Layer

The following checks are applied:

- Minimum sample threshold
- Confidence gating
- Bot amplification filter
- Media spike filter

If any safeguard triggers, escalation is suppressed.

---

### 6. Escalation Assignment

Escalation level is assigned based on thresholds:

Level 0–3

Only if governance conditions allow escalation.

---

### 7. Audit Logging

Final structured record (v1.1 schema) is written to:

logs/audit_log.jsonl

Each decision includes:

- County ID
- Timestamp
- Z-scores
- Crisis score
- Confidence
- Escalation level
- Model version

---

## System Characteristics

- Deterministic scoring
- Layered safeguards
- Tiered escalation
- Transparent audit trail
