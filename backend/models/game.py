import random
from models import player
from models.player import Coven, Townie
from services import setup
# from services import day_events


class Game:
    def __init__(self):
        self.living_players = setup.setup_players()
        self.dead_players = []
        self.day = 1
