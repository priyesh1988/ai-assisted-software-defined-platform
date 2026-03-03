
from fastapi import FastAPI
from control_plane.orchestrator import handle_intent

app = FastAPI()

@app.post("/intent/apply")
def apply_intent(payload: dict):
    return handle_intent(payload)
