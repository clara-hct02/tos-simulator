from models.phase import Phase
from models.player import Player, Townie
from schemas.game import GameEvent
import random

class JudgementPhase(Phase):
    name = "Judgement"

    def __init__(self, game, lynched: Player):
        self.game = game
        self.lynched = lynched
    
    def next_phase(self, game):
        if game.remaining_trials > 0:
            from models.voting_phase import VotingPhase
            return VotingPhase()
        else :
            from models.night_phase import NightPhase
            return NightPhase()

    def get_events(self, game):
        events = []

        verdict = [' voted innocent', ' voted guilty', ' abstained']

        events.append(GameEvent(
                type="judgement",
                text=f"The town is now voting on the fate of player {self.lynched.number}"
            ))

        guilty_weight = self.lynched.suspicion
        innocent_weight = (1 - guilty_weight) * 0.6
        abstain_weight = (1 - guilty_weight) * 0.4

        weights = [innocent_weight, guilty_weight, abstain_weight]
        guilty = 0
        inno = 0

        for p in game.living_players:
            if self.lynched.number == p.number:
                continue

            choice = random.choices(verdict, weights=weights, k=1)[0]
            if choice == ' voted innocent':
                inno += 1
            if choice == ' voted guilty':
                guilty += 1
            
            events.append(GameEvent(
                type="judgement",
                text=f"Player {p.number} {choice}"
            ))

        if guilty > inno:
            events.append(GameEvent(
                type="judgement",
                text=f"The town has voted {guilty} to {inno} to put player {self.lynched.number} to death"
            ))
            
            game.kill_player(self.lynched)

            events.append(GameEvent(
                type="reveal",
                text=f"{self.lynched.number} was an innocent town member!" if isinstance(self.lynched, Townie) 
                else f"{self.lynched.number} was a member of the coven!"
            ))


        else:
            events.append(GameEvent(
                type="judgement",
                text=f"The town has voted {inno} to {guilty} to pardon player {self.lynched.number}"
            ))
        
        return events
