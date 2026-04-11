from models.phase import Phase

class DayPhase(Phase):
    name = "Day"
    
    def next_phase(self):
        from models.voting_phase import VotingPhase
        return VotingPhase()