
# 🚀 AI Assisted Software Defined Platform

> Intent-based infrastructure provisioning with AI-powered risk intelligence.

Provision infrastructure by declaring **intent**, not writing complex IaC manually.  
The platform evaluates **risk, cost, policy, and blast radius** before provisioning anything.

---

# 🧠 How It Works

User Intent  
⬇  
Policy Engine  
⬇  
AI Risk Engine  
⬇  
Cost Simulator  
⬇  
Orchestrator  
⬇  
Provisioning Execution  

---

# ⚙️ Run Locally

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 2️⃣ Start API

```bash
uvicorn control_plane.api:app --reload
```

API available at:

http://localhost:8000

---

# 📡 API Usage

Endpoint:

POST /intent/apply

Send JSON payload describing your infrastructure intent.

---

# 📦 Example 1 — Create Kubernetes Cluster

### Request

```json
{
  "resource": "kubernetes_cluster",
  "provider": "aws",
  "node_count": 5,
  "instance_type": "m5.large",
  "criticality": "high"
}
```

### Response

```json
{
  "policy_result": "Additional approval required",
  "risk_result": {
    "risk_score": 70,
    "approval_required": "Approvers"
  },
  "cost_estimate": {
    "estimated_monthly_cost_usd": 1250
  }
}
```

---

# 📦 Example 2 — Deploy AI Workload

### Request

```json
{
  "resource": "ai_workload",
  "provider": "aws",
  "gpu_count": 4,
  "node_count": 2,
  "criticality": "high"
}
```

### Response

```json
{
  "policy_result": "Additional approval required",
  "risk_result": {
    "risk_score": 70,
    "approval_required": "Approvers"
  },
  "cost_estimate": {
    "estimated_monthly_cost_usd": 500
  }
}
```

---

# 📦 Example 3 — Low-Risk Development Cluster

### Request

```json
{
  "resource": "kubernetes_cluster",
  "provider": "aws",
  "node_count": 2,
  "instance_type": "t3.medium",
  "criticality": "low"
}
```

### Response

```json
{
  "policy_result": "Policy check passed",
  "risk_result": {
    "risk_score": 20,
    "approval_required": "Approvers"
  },
  "cost_estimate": {
    "estimated_monthly_cost_usd": 500
  }
}
```

---

# 📦 Example 4 — Scale Existing Cluster

### Request

```json
{
  "resource": "scale_cluster",
  "provider": "aws",
  "node_count": 8,
  "criticality": "high"
}
```

### Response

```json
{
  "policy_result": "Additional approval required",
  "risk_result": {
    "risk_score": 70,
    "approval_required": "Approvers"
  },
  "cost_estimate": {
    "estimated_monthly_cost_usd": 2000
  }
}
```

---

# 🔥 Why This Platform Is Different

Traditional infrastructure tools:
- Execute blindly  
- Require manual review  
- Offer no predictive risk scoring  

This platform:
- Scores risk *before* execution  
- Simulates cost impact  
- Applies approval tiers automatically  
- Makes infrastructure measurable  

---

# 🏗 Vision

> Infrastructure should be declarative, intelligent, and risk-aware.

Build platforms that think before they provision.
