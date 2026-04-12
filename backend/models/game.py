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

    def advance_phase(self):
        if self.phase.name == "Night":
            self.day += 1

        self.phase = self.phase.next_phase(self)

    def dayOne(self):
        return "Welcome to Town of Salem! Please take your leave for tonight."
