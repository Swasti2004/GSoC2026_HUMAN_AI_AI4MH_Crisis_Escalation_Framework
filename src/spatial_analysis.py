def spatial_cluster_score(neighbor_z_scores, threshold=2.0):
    """
    Counts neighboring counties exceeding abnormal sentiment threshold.
    """

    return sum(1 for score in neighbor_z_scores if score > threshold)