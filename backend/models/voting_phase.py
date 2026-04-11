from models.phase import Phase


class VotingPhase(Phase):
    name = "Voting"
    
    def next_phase(self):
        from models.judgement_phase import JudgementPhase
        return JudgementPhase()