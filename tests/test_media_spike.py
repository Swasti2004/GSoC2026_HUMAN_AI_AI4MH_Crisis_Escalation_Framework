from src.scoring_engine import compute_crisis_score

county_id = "AL-County-03"

county_data = {
    "sentiment": -0.85,
    "volume": 200,
    "amplification_ratio": 0.1,
    "event_similarity": 0.85  # media similarity high
}

baseline_stats = {
    "mean_sentiment": -0.4,
    "std_sentiment": 0.1,
    "mean_volume": 60,
    "std_volume": 15
}

neighbor_z_scores = [0.5, 0.7]  # no spatial reinforcement

result = compute_crisis_score(
    county_id,
    county_data,
    baseline_stats,
    neighbor_z_scores
)

print("Media Spike Test:")
print(result)