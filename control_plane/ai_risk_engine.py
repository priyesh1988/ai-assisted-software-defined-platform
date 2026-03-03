
def calculate_risk(intent):
    score = 20
    if intent.get("criticality") == "high":
        score += 30
    if intent.get("node_count", 0) > 3:
        score += 20

    return {
        "risk_score": score,
        "approval_required": "DIRECTOR" if score > 50 else "ENGINEER"
    }
