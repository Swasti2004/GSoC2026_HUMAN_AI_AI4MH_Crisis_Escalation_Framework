from src.spatial_analysis import spatial_cluster_score
from src.confidence import compute_confidence
from src.governance_filters import apply_governance_checks
from src.audit_logger import generate_audit_record, save_audit_record

MIN_SAMPLE = 30

# Tiered escalation thresholds
LEVEL_1_THRESHOLD = 2.5   # Analyst Review
LEVEL_2_THRESHOLD = 3.5   # Behavioral Health Office
LEVEL_3_THRESHOLD = 4.5   # Multi-Agency Coordination


def compute_z_score(current, mean, std):
    """
    Computes standard Z-score.
    """
    if std == 0:
        return 0
    return (current - mean) / std


def compute_crisis_score(county_id, county_data, baseline_stats, neighbor_z_scores):
    """
    Core crisis scoring engine.
    Returns structured audit-ready record.
    """

    volume = county_data["volume"]

    # Minimum sample safeguard
    if volume < MIN_SAMPLE:
        return {
            "county_id": county_id,
            "crisis_score": None,
            "confidence": "LOW",
            "escalation_level": 0,
            "reason": "Insufficient sample size"
        }

    # Sentiment Z-score (invert sign so stronger negativity increases crisis score)
    sentiment_z = -1 * compute_z_score(
        county_data["sentiment"],
        baseline_stats["mean_sentiment"],
        baseline_stats["std_sentiment"]
    )

    # Volume spike Z-score
    volume_z = compute_z_score(
        volume,
        baseline_stats["mean_volume"],
        baseline_stats["std_volume"]
    )

    # Geographic reinforcement
    geo_score = spatial_cluster_score(neighbor_z_scores)

    # Composite crisis score
    crisis_score = (0.5 * sentiment_z) + (0.3 * volume_z) + (0.2 * geo_score)

    # Confidence level
    confidence = compute_confidence(volume)

    # Governance filters (bot/media)
    governance_block = apply_governance_checks(county_data)

    # Tiered escalation logic
    if governance_block or confidence == "LOW":
        escalation_level = 0
    elif crisis_score >= LEVEL_3_THRESHOLD:
        escalation_level = 3
    elif crisis_score >= LEVEL_2_THRESHOLD:
        escalation_level = 2
    elif crisis_score >= LEVEL_1_THRESHOLD:
        escalation_level = 1
    else:
        escalation_level = 0

    # Generate audit record
    audit_record = generate_audit_record(
        county_id=county_id,
        crisis_score=crisis_score,
        confidence=confidence,
        escalate=escalation_level,
        sentiment_z=sentiment_z,
        volume_z=volume_z,
        geo_score=geo_score
    )

    # Save to audit log
    save_audit_record(audit_record)

    return audit_record