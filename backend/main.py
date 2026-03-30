from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
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

game = None

@app.get("/")
def start():
    return {"message": "Hello from FastAPI"}

@app.post("/setup")
def setup(options: dict = Body(default={})):
    global game
    game = Game()
    data = game.dayOne()

    return {"message": data, "phase": "day", "day": 1}

@app.get("/day")
def getDay():
    global game
    data = None

    return {"message": data}

@app.post("/continue")
def advance_game():
    global game
    return {"message": "continue debug", "phase": "day", "day": 1}