# Usage Guide

## Basic Programmatic Usage

Example:

from src.scoring_engine import compute_crisis_score

county_id = "AL-County-01"

county_data = {
    "sentiment": -0.8,
    "volume": 120,
    "amplification_ratio": 0.1,
    "event_similarity": 0.0
}

baseline_stats = {
    "mean_sentiment": -0.4,
    "std_sentiment": 0.1,
    "mean_volume": 60,
    "std_volume": 15
}

neighbor_z_scores = [2.5, 2.6]

result = compute_crisis_score(
    county_id,
    county_data,
    baseline_stats,
    neighbor_z_scores
)

print(result)

---

## Output

Returns a structured dictionary including:

- crisis_score
- confidence
- escalation_level
- model_version
