from src.scoring_engine import compute_crisis_score

county_id = "AL-County-04"

county_data = {
    "sentiment": -0.9,
    "volume": 12,  # below minimum threshold
    "amplification_ratio": 0.0,
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

print("Rural Sparse Test:")
print(result)