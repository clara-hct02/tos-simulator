from models.phase import Phase

class JudgementPhase(Phase):
    name = "Judgement"
    
    def next_phase(self, game):
        from models.night_phase import NightPhase
        return NightPhase()