from abc import ABC, abstractmethod
from schemas.game import GameEvent

class Phase(ABC):

    @abstractmethod
    def next_phase(self):
        raise NotImplementedError

    @abstractmethod
    def get_events(self) -> list[GameEvent]:
        raise NotImplementedError

