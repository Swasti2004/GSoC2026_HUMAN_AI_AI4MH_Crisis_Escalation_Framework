from src.scoring_engine import compute_crisis_score

county_id = "AL-County-02"

county_data = {
    "sentiment": -0.9,
    "volume": 150,
    "amplification_ratio": 0.6,  # suspiciously high
    "event_similarity": 0.2
}

baseline_stats = {
    "mean_sentiment": -0.4,
    "std_sentiment": 0.1,
    "mean_volume": 60,
    "std_volume": 15
}

neighbor_z_scores = [2.4, 2.2]

result = compute_crisis_score(
    county_id,
    county_data,
    baseline_stats,
    neighbor_z_scores
)

print("Bot Amplification Test:")
print(result)