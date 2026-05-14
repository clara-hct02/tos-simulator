from models.phase import Phase
from schemas.game import GameEvent
from models.player import Coven
import random

class NightPhase(Phase):
    name = "Night"
    
    def next_phase(self, game):
        from models.day_phase import DayPhase
        return DayPhase()

    def get_events(self, game):
        events = []

        non_coven = [p for p in game.living_players if not isinstance(p, Coven)]
        coven_kill = random.choice(non_coven)

        game.kill_player(coven_kill)

        events.append(GameEvent(
            type="night",
            text=(f"Player {coven_kill.number} has been killed by the coven!")
        ))

        return events