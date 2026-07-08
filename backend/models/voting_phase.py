from models.phase import Phase
from schemas.game import GameEvent
import random

class VotingPhase(Phase):
    name = "Voting"
    
    def next_phase(self, game):
        if self.player_on_stand:
            from models.judgement_phase import JudgementPhase
            game.remaining_trials -= 1
            return JudgementPhase(game, self.player_on_stand)
        else:
            from models.night_phase import NightPhase
            return NightPhase()


    def get_events(self, game) -> list[GameEvent]:
        events = []
        votes_tally = []

        for player in game.living_players:
            other_players = [p for p in game.living_players if p != player]
            voted = random.choice(other_players)
            votes_tally.append(voted.number)
            events.append(GameEvent(
                type="vote",
                text=f"{player.name} voted for {voted.name}",
                player_number=player.number
            ))

        on_stand = max(set(votes_tally), key=votes_tally.count)
        self.player_on_stand = game.get_player(on_stand)

        return events