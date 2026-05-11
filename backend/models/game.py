from models.day_phase import DayPhase
from models import player
from models.player import Coven, Townie
from services import setup
from uuid import uuid4


class Game:
    def __init__(self):
        self.id = str(uuid4())
        self.living_players = setup.setup_players()
        self.dead_players = []
        self.day = 1
        self.phase = DayPhase()
        self.remaining_trials = 3

    def advance_phase(self):
        if self.phase.name == "Night":
            self.day += 1
            self.remaining_trials = 3

        self.phase = self.phase.next_phase(self)

    def get_phase_data(self):
        return self.phase.get_events(self)
    
    def get_player(self, number: int):
        return next(p for p in self.living_players if p.number == number)
    
    def kill_player(self, p):
        if p in self.living_players:
            self.living_players.remove(p)

    def dayOne(self):
        return "Welcome to Town of Salem! Please take your leave for tonight."
