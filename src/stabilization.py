def exponential_moving_average(current_value, previous_ema, alpha=0.3):
    """
    Computes Exponential Moving Average (EMA) to stabilize short-term fluctuations.
    """
    return (alpha * current_value) + ((1 - alpha) * previous_ema)