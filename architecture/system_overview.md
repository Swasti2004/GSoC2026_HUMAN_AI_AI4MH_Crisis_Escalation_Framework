# Crisis Escalation Framework — System Overview

## Objective

This framework detects statistically significant signals of mental health crisis escalation at county-level resolution.
The system combines statistical anomaly detection, spatial reinforcement modeling, and governance safeguards to produce tiered escalation decisions.

## Core Components

- `scoring_engine.py` — Composite crisis scoring logic
- `spatial_analysis.py` — Geographic cluster reinforcement
- `governance_filters.py` — Bot/media amplification mitigation
- `confidence.py` — Sample-size confidence modeling
- `audit_logger.py` — Structured audit logging (v1.1 schema)

## Processing Pipeline

Raw County Data
→ Z-score normalization
→ Spatial reinforcement scoring
→ Composite crisis score calculation
→ Governance filtering
→ Tiered escalation assignment
→ Audit record persistence

## Design Principles

- Statistical grounding (Z-score normalization)
- False-positive mitigation
- Multi-layer governance safeguards
- Transparent audit logging
- Tiered escalation rather than binary triggers
