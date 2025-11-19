import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="FootManage API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Match(BaseModel):
    id: str
    league: str
    minute: int
    home: str
    away: str
    homeScore: int
    awayScore: int


class Tournament(BaseModel):
    id: str
    name: str
    region: str
    season: str
    teams: int


@app.get("/")
def read_root():
    return {"message": "FootManage backend is live"}


@app.get("/live-matches")
def get_live_matches():
    # Sample mocked data to power the landing page
    data = [
        {"id": "1", "league": "Premier League", "minute": 67, "home": "Arsenal", "away": "Chelsea", "homeScore": 2, "awayScore": 1},
        {"id": "2", "league": "La Liga", "minute": 53, "home": "Barcelona", "away": "Sevilla", "homeScore": 1, "awayScore": 1},
        {"id": "3", "league": "Serie A", "minute": 12, "home": "Milan", "away": "Inter", "homeScore": 0, "awayScore": 0},
        {"id": "4", "league": "Bundesliga", "minute": 74, "home": "Bayern", "away": "Dortmund", "homeScore": 3, "awayScore": 2},
        {"id": "5", "league": "Ligue 1", "minute": 41, "home": "PSG", "away": "Lyon", "homeScore": 1, "awayScore": 0},
        {"id": "6", "league": "Eredivisie", "minute": 25, "home": "Ajax", "away": "PSV", "homeScore": 0, "awayScore": 1},
    ]
    return {"matches": [Match(**m).dict() for m in data]}


@app.get("/tournaments")
def get_tournaments():
    data = [
        {"id": "t1", "name": "Champions Cup", "region": "Europe", "season": "2025", "teams": 32},
        {"id": "t2", "name": "Global Nations", "region": "International", "season": "2026", "teams": 48},
        {"id": "t3", "name": "Premier Invitational", "region": "UK", "season": "2025/26", "teams": 20},
        {"id": "t4", "name": "Copa Elite", "region": "South America", "season": "2025", "teams": 24},
        {"id": "t5", "name": "Asia Super League", "region": "Asia", "season": "2025", "teams": 18},
        {"id": "t6", "name": "Club World Series", "region": "World", "season": "2025", "teams": 16},
    ]
    return {"tournaments": [Tournament(**t).dict() for t in data]}


@app.get("/test")
def test_database():
    response = {
        "backend": "✅ Running",
        "database": "❌ Not Available",
        "database_url": "✅ Set" if os.getenv("DATABASE_URL") else "❌ Not Set",
        "database_name": "✅ Set" if os.getenv("DATABASE_NAME") else "❌ Not Set",
        "connection_status": "Not Connected",
        "collections": []
    }
    return response


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
