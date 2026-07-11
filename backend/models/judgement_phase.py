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

    def get_events(self, game, vote_choices = None):
        events = []

        verdict = [' voted innocent', ' voted guilty', ' abstained']

        events.append(GameEvent(
                type="judgement",
                text=f"The town is now voting on the fate of {self.lynched.name}"
            ))

        guilty_weight = self.lynched.suspicion
        innocent_weight = (1 - guilty_weight) * 0.7
        abstain_weight = (1 - guilty_weight) * 0.3

        weights = [innocent_weight, guilty_weight, abstain_weight]
        guilty = 0
        inno = 0

        if vote_choices is None:
            vote_choices = random.choices(verdict, weights=weights, k=len(game.living_players) - 1)

        i = 0

        for p in game.living_players:
            if self.lynched.number == p.number:
                continue

            choice = vote_choices[i]
            i += 1

            if choice == ' voted innocent':
                inno += 1
            if choice == ' voted guilty':
                guilty += 1
            
            events.append(GameEvent(
                type="judgement",
                text=f"{p.name} {choice}"
            ))

        if guilty > inno:
            events.append(GameEvent(
                type="judgement",
                text=f"The town has voted {guilty} to {inno} to put {self.lynched.name} to death"
            ))
            
            game.kill_player(self.lynched)
            game.remaining_trials = 0

            events.append(GameEvent(
                type="reveal",
                text=f"{self.lynched.name} was a {self.lynched.role_name}!"
            ))


        else:
            self.lynched.suspicion += 0.1
            events.append(GameEvent(
                type="judgement",
                text=f"The town has voted {inno} to {guilty} to pardon {self.lynched.name}"
            ))
        
        return events
