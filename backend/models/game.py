from models.day_phase import DayPhase
from models.player import Coven, Townie
from services import setup
from uuid import uuid4


class Game:
    def __init__(self, names):
        self.id = str(uuid4())
        self.living_players = setup.setup_players(names)
        self.dead_players = []
        self.day = 1
        self.phase = DayPhase()
        self.remaining_trials = 3
        self.winner = ""
        self.is_over = False

    def advance_phase(self):
        if self.phase.name == "Night":
            self.day += 1
            self.remaining_trials = 3

        self.phase = self.phase.next_phase(self)

    def get_phase_data(self):
        if self.is_over:
            return []

        return self.phase.get_events(self)
    
    def get_player(self, number: int):
        return next(p for p in self.living_players if p.number == number)
    
    def kill_player(self, p):
        if p in self.living_players:
            self.living_players.remove(p)

        self.check_win()

    def check_win(self):
        living_town = 0
        living_coven = 0

        for player in self.living_players:
            if isinstance(player, Townie):
                living_town += 1
            else:
                living_coven += 1

        if living_town == 0:
            self.is_over = True
            self.winner = "Coven"
            return True
        
        elif living_coven == 0:
            self.is_over = True
            self.winner = "Town"
            return True

        return False

    def dayOne(self):
        return "Welcome to Town of Salem! Please take your leave for tonight."
