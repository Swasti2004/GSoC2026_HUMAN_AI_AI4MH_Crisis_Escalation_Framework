# Evaluation Strategy

## Scenario-Based Validation

The system is validated using controlled synthetic test cases:

1. Normal Crisis Escalation

   - High sentiment deviation
   - High volume spike
   - Geographic reinforcement
     → Escalation Level 2+
2. Bot Amplification Case

   - High anomaly
   - Amplification ratio above threshold
     → Escalation suppressed
3. Media Spike Case

   - Large volume spike
   - Event similarity triggered
     → Escalation suppressed
4. Rural Sparse Case

   - Volume below MIN_SAMPLE
     → Confidence LOW
     → Escalation suppressed

---

## Robustness Goals

- Minimize false positives
- Maintain escalation sensitivity
- Ensure governance compliance
- Maintain deterministic reproducibility
