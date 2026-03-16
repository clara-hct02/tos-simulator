from fastapi import FastAPI
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

game = Game()

@app.get("/")
def start():
    return {"message": "Hello from FastAPI"}

@app.post("/setup")
def setup():
    return {"message": "Game starting"}