
from control_plane.policy_engine import evaluate_policy
from control_plane.ai_risk_engine import calculate_risk
from control_plane.cost_simulator import estimate_cost

def handle_intent(intent):
    policy = evaluate_policy(intent)
    risk = calculate_risk(intent)
    cost = estimate_cost(intent)

    return {
        "policy_result": policy,
        "risk_result": risk,
        "cost_estimate": cost
    }
