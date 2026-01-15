def calculate_risk(process_hits, file_events):
    score = 0

    # Process-based risk
    if process_hits:
        score += 5

    # File activity risk (scaled)
    file_count = len(file_events)

    if file_count >= 1:
        score += 2
    if file_count >= 3:
        score += 3
    if file_count >= 5:
        score += 5

    suspicious_ext = (".log", ".dat", ".tmp")

    for f in file_events:
        if f.endswith(suspicious_ext):
            score += 1

    # Threat levels
    if score >= 8:
        level = "HIGH"
    elif score >= 4:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level