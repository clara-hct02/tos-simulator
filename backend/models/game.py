import random
from models import player
from models.player import Coven, Townie
from services import setup


class Game:
    def __init__(self):
        self.living_players = setup.setup_players()
        self.dead_players = []
        self.day = 1

    def advance_day(self):
        self.day += 1

    def dayOne(self):
        return "Welcome to Town of Salem! Please take your leave for tonight."
