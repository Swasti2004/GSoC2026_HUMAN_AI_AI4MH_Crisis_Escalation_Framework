
# Crisis Escalation Framework (Governance-Aware Tiered Model)

A governance-aware crisis escalation framework for detecting statistically significant mental health distress signals at county-level resolution.

This system integrates statistical anomaly detection, spatial reinforcement modeling, and multi-layer governance safeguards to produce tiered escalation decisions with full audit transparency.

---

## Key Features

- Z-score based anomaly detection
- Spatial cluster reinforcement
- Governance filtering (bot & media distortion mitigation)
- Confidence gating for sparse regions
- Tiered escalation levels (0–3)
- Versioned structured audit logging (v1.1 schema)

---

## Architecture Overview

```
Raw Data
    ↓
Z-score Normalization
    ↓
Spatial Reinforcement
    ↓
Composite Crisis Score
    ↓
Governance Layer
    ↓
Tiered Escalation
    ↓
Audit Logging
```

See `/architecture` for detailed design documentation.

---

## Escalation Levels

| Level | Meaning |
|-------|---------|
| 0 | Monitor |
| 1 | Analyst Review |
| 2 | Behavioral Health Office |
| 3 | Multi-Agency Coordination |

Escalation is automatically suppressed under:
- Low confidence
- Bot amplification detection
- Media spike detection
- Insufficient sample size

---

## Installation

```bash
git clone https://github.com/Swasti2004/GSoC2026_HUMAN_AI_AI4MH_Crisis_Escalation_Framework.git
cd GSoC2026_HUMAN_AI_AI4MH_Crisis_Escalation_Framework
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Run Tests

```bash
python -m tests.test_scenarios
python -m tests.test_bot_amplification
python -m tests.test_media_spike
python -m tests.test_rural_sparse_case
```

---

## Repository Structure

```
src/            Core scoring and governance logic
tests/          Scenario validation modules
architecture/   System design documentation
audit/          Audit schema and policy
docs/           Developer documentation
submission/     Proposal and evaluation materials
logs/           Runtime audit logs (ignored via .gitignore)
```

---

## Design Philosophy

This framework assumes:

- Statistical signals alone are insufficient
- Adversarial distortion is possible
- Binary alert systems create operational overload
- Transparency is mandatory in public-sector systems

Therefore, escalation is tiered, governance-aware, and fully auditable.

---

## Model Version

Current version: v1.1

- Tiered escalation model
- Standardized audit schema
- Governance suppression logic

---

## Future Directions

- Rolling baseline recalibration
- Drift detection
- Adaptive thresholds
- API interface layer
- Visualization dashboard

