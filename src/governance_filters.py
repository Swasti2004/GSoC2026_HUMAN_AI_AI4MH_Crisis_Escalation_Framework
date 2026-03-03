def apply_governance_checks(county_data):
    """
    Applies governance filters for bot amplification and media-driven spikes.
    Returns True if escalation should be blocked.
    """

    amplification_ratio = county_data.get("amplification_ratio", 0)
    event_similarity = county_data.get("event_similarity", 0)

    # Bot amplification risk
    if amplification_ratio > 0.4:
        return True

    # Media-driven spike risk
    if event_similarity > 0.7:
        return True

    return False