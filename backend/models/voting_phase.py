from models.phase import Phase
from schemas.game import GameEvent
import random

class VotingPhase(Phase):
    name = "Voting"
    
    def next_phase(self, game):
        from models.judgement_phase import JudgementPhase
        return JudgementPhase()


    def get_events(self, game) -> list[GameEvent]:
        events = []
        votes_tally = []

        for player in game.living_players:
            voted = random.choice(game.living_players)
            votes_tally.append(voted.number)
            events.append(GameEvent(
                type="vote",
                text=f"Player {player.number} voted for Player {voted.number}",
                player_number=player.number
            ))

        on_stand = max(set(votes_tally), key=votes_tally.count)
        player_on_stand = game.get_player(on_stand)

        if votes_tally.count(player_on_stand) > len(game.living_players) // 2:
            self.living_players.remove(player_on_stand)
            events.append(GameEvent(
                type="elimination",
                text=f"Player {player_on_stand.number} was eliminated by the town!",
                player_number=player_on_stand.number
            ))
        else:
            events.append(GameEvent(
                type="no_execution",
                text="The town has decided not to execute anyone today."
            ))

        return events