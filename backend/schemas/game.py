from pydantic import BaseModel

class GameSchema(BaseModel):
    id: str
    phase: str
    day: int
    players: list
    message: str