from fastapi import FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas.game import GameSchema
from models.game import Game

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

games: dict[str, Game] = {}

@app.get("/")
def start():
    return {"message": "Hello from FastAPI"}

@app.post("/setup")
def setup(options: dict = Body(default={})) -> GameSchema:
    game = Game()
    games[game.id] = game
    dayOneMessage = game.dayOne()

    return GameSchema(
        id=game.id,
        phase=game.phase.name,
        day=game.day,
        players=game.living_players,
        message=dayOneMessage
    )

@app.post("/continue")
def advance_game(game_id: str) -> GameSchema:
    game = games.get(game_id)
    if not game:
        raise HTTPException(status_code=404)
    game.advance_phase()

    return GameSchema(
        id=game.id,
        phase=game.phase.name,
        day=game.day,
        players=game.living_players,
        message="Placeholder continue info"
    )