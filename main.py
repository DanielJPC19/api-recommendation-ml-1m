from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json
from pathlib import Path

app = FastAPI(title="Recommendations API")
recommendations: list = []
recommendations_by_user: dict = {}


@app.on_event("startup")
def load_data():
    global recommendations, recommendations_by_user
    try:
        recommendations = json.loads(Path("recommendations.json").read_text())
        recommendations_by_user = {entry["user_id"]: entry for entry in recommendations}
    except FileNotFoundError:
        raise RuntimeError("recommendations.json not found")
    except json.JSONDecodeError:
        raise RuntimeError("recommendations.json has invalid JSON")


@app.get("/recommendations", status_code=200)
def get_recommendations():
    try:
        if not recommendations:
            raise HTTPException(status_code=404, detail="No recommendations available")
        return JSONResponse(content=recommendations)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.get("/recommendations/{user_id}", status_code=200)
def get_recommendations_by_user(user_id: int):
    try:
        user_data = recommendations_by_user.get(user_id)
        if user_data is None:
            raise HTTPException(status_code=404, detail=f"User {user_id} not found")
        return JSONResponse(content=user_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
