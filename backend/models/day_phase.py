from models.phase import Phase

class DayPhase(Phase):
    name = "Day"
    
    def next_phase(self, game):
        if game.day == 1:
            from models.night_phase import NightPhase
            return NightPhase()

        from models.voting_phase import VotingPhase
        return VotingPhase()

    def get_events(self, game):
        return []
