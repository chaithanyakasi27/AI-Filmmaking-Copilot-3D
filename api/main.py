from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path
app = FastAPI(title="AI Filmmaking Copilot API")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
VIEWER_DIR = PROJECT_ROOT / "viewer"

#Serve static files (Three.js assets, textures, models, etc.)
app.mount("/viewer", StaticFiles(directory=VIEWER_DIR, html=True), name="viewer")

@app.get("/")
def root():
    return {"Status": "AI Filmmaking Copilot API is running."}
