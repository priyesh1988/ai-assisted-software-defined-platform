
def evaluate_policy(intent):
    if intent.get("criticality") == "high":
        return "Additional approval required"
    return "Policy check passed"
