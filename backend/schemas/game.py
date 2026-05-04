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

    @classmethod
    def from_game(cls, game, events):
        return cls(
            id=game.id,
            phase=game.phase.name,
            day=game.day,
            players=game.living_players,
            message="Placeholder continue info",
            events=events
        )