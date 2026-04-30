from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from pathlib import Path

app = FastAPI(title="Recommendations API")
recommendations: list = []


@app.on_event("startup")
def load_data():
    global recommendations
    recommendations = json.loads(Path("recommendations.json").read_text())


@app.get("/recommendations")
def get_recommendations():
    return JSONResponse(content=recommendations)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
