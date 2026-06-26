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
            text=(f"{coven_kill.name} has been killed by the coven!")
        )) 

        events.append(GameEvent(
            type="reveal",
            text=(f"{coven_kill.name} was a {coven_kill.role_name}!")
        ))

        return events