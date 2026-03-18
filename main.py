from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore
from typing import List

app = FastAPI()

ratings_db = []

class Rating(BaseModel):
    idea_id: str
    rating: int
    comment: str = ""

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/rate")
def submit_rating(rating: Rating):
    ratings_db.append(rating.dict())
    return {"message": "Rating submitted!", "total": len(ratings_db)}

@app.get("/ratings/{idea_id}")
def get_ratings(idea_id: str):
    results = [r for r in ratings_db if r["idea_id"] == idea_id]
    return {"idea_id": idea_id, "ratings": results}