from models.phase import Phase

class NightPhase(Phase):
    name = "Night"
    
    def next_phase(self, game):
        from models.day_phase import DayPhase
        return DayPhase()