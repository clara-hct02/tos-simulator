import random
from models import player
from models.player import Coven, Townie
from services import setup


class Game:
    def __init__(self):
        print("creating game")
        self.living_players = setup.setup_players()
        self.dead_players = []
        self.day = 1
