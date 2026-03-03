import math

def compute_confidence(volume, scale_factor=50):
    """
    Estimates confidence level based on data volume.
    """

    score = 1 - math.exp(-volume / scale_factor)

    if score < 0.4:
        return "LOW"
    elif score < 0.75:
        return "MODERATE"
    else:
        return "HIGH"