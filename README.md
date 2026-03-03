
# 🚀 AI Assisted Software Defined Platform

Intent-based infrastructure provisioning with AI risk intelligence.

## How It Works

User Intent → Policy Engine → AI Risk Engine → Cost Simulator → Orchestrator → Provisioning

## Run Locally

pip install -r requirements.txt
uvicorn control_plane.api:app --reload

## Example Intent

POST /intent/apply

{
  "resource": "kubernetes_cluster",
  "provider": "aws",
  "node_count": 5,
  "instance_type": "m5.large",
  "criticality": "high"
}
