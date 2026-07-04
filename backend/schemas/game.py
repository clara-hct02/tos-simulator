from pydantic import BaseModel
from typing import List

class GameEvent(BaseModel):
    type: str
    text: str

class GameSchema(BaseModel):
    id: str
    phase: str
    day: int
    players: list
    message: str
    events: List[GameEvent] = []
    isOver: bool
    winner: str

    @classmethod
    def from_game(cls, game, events):
        return cls(
            id=game.id,
            phase=game.phase.name,
            day=game.day,
            players=game.living_players,
            isOver=game.is_over,
            winner=game.winner,
            message="Placeholder continue info",
            events=events
        )