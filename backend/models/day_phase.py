from models.phase import Phase
from schemas.game import GameEvent

class DayPhase(Phase):
    name = "Day"
    
    def next_phase(self, game):
        if game.day == 1:
            from models.night_phase import NightPhase
            return NightPhase()

        from models.voting_phase import VotingPhase
        return VotingPhase()

    def get_events(self, game):
        events = []

        if game.day == 1:
            events.append(GameEvent(
                type="day",
                text="Welcome to Town of Salem! Please take your leave for tonight."
            ))
        else:
            events.append(GameEvent(
                type="day",
                text="The town begins discussing what happened last night."
            ))
            
        return events
