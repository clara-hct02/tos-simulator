from models import player


class Action:
    def __init__(self, actor, target, priority):
        self.actor = actor
        self.target = target
        self.priority = priority


class ClericAction(Action):
    def resolve(self):
        print(f"Player {self.actor.number} casts their barrier on player {self.target.number}")
        self.target.defense += 1


class TavAction(Action):
    def resolve(self):
        print(f"Player {self.actor.number} has decided to celebrate with player {self.target.number}")
        self.target.blocked = True


class BookAction(Action):
    def resolve(self):
        print(f"Player {self.actor.number} has decided to attack {self.target.number} with the necronomicon")

        if self.actor.attack > self.target.defense:
            print(f"Player {self.target.number} has been killed the coven!")


class SheriffAction(Action):
    def resolve(self):
        if isinstance(self.target, player.Townie) or self.target.necro:
            result = "innocent"
        else:
            result = "suspicious"
        print(f"Player {self.actor.number} has decided to interrogate {self.target.number} and found them {result}")
        return result