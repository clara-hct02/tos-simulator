from models.phase import Phase

class JudgementPhase(Phase):
    name = "Judgement"
    
    def next_phase(self):
        from models.night_phase import NightPhase
        return NightPhase()