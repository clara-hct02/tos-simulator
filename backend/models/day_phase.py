from models.phase import Phase
from schemas.game import GameEvent
import random

class DayPhase(Phase):
    name = "Day"
    
    def next_phase(self, game):
        if game.day == 1:
            from models.night_phase import NightPhase
            return NightPhase()

        from models.voting_phase import VotingPhase
        return VotingPhase()

    def get_events(self, game):
        events = []

        if game.day == 1:
            events.append(GameEvent(
                type="day",
                text="Welcome to Town of Salem! Please take your leave for tonight."
            ))
        else:
            events.append(GameEvent(
                type="day",
                text="The town begins discussing what happened last night."
            ))

            discussion = [
                '{P1} accuses {P2} of suspicious behaviour',
                '{P1} shares their info',
                '{P1} and {P2} talk privately',
                '{P1} and {P2} have a heated debate',
                '{P1} refuses to reveal their information',
                '{P1} reminds everyone to stay calm',
            ]

            count = len(game.living_players) // 2

            for i in range(count):
                p1 = random.choice(game.living_players)
                other_players = [p for p in game.living_players if p != p1]
                p2 = random.choice(other_players)

                statement = discussion[random.randint(0, len(discussion) - 1)].format(P1=p1.name, P2=p2.name)

                events.append(GameEvent(
                    type="day",
                    text=statement
                ))

        return events
