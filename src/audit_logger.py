import json
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "audit_log.jsonl"


def generate_audit_record(
    county_id,
    crisis_score,
    confidence,
    escalate,
    sentiment_z,
    volume_z,
    geo_score
):
    """
    Generates a standardized audit record.
    This is the ONLY schema used across the system.
    """

    return {
        "county_id": county_id,
        "timestamp": datetime.utcnow().isoformat(),
        "sentiment_z": round(sentiment_z, 3) if sentiment_z is not None else None,
        "volume_z": round(volume_z, 3) if volume_z is not None else None,
        "geo_score": geo_score,
        "crisis_score": round(crisis_score, 3) if crisis_score is not None else None,
        "confidence": confidence,
        "escalation_level": escalate,   # ← STANDARDIZED FIELD
        "model_version": "v1.1"
    }


def save_audit_record(record):
    """
    Appends audit record as JSON line.
    """

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")