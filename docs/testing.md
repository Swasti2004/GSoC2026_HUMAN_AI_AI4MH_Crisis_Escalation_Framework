# Testing Guide

The framework includes scenario-based test modules.

Run the following:

python -m tests.test_scenarios
python -m tests.test_bot_amplification
python -m tests.test_media_spike
python -m tests.test_rural_sparse_case

---

## Test Coverage

- Normal escalation case
- Bot amplification suppression
- Media spike suppression
- Sparse rural safeguard

Each test prints structured output for inspection.
