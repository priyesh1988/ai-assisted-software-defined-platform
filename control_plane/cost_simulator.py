
def estimate_cost(intent):
    nodes = intent.get("node_count", 1)
    return {"estimated_monthly_cost_usd": nodes * 250}
