from models.phase import Phase


class VotingPhase(Phase):
    name = "Voting"
    
    def next_phase(self, game):
        from models.judgement_phase import JudgementPhase
        return JudgementPhase()