from models import actions
from pydantic import BaseModel

class Player(BaseModel):
    name: str
    number: int
    votes: int = 1
    defense: int = 0
    suspicion: float = 0.3
    blocked: bool = False

    def night_action(self, *args):
        pass

    def day_action(self, *args):
        pass


# Town Members
class Townie(Player):
    role_name: str = "Pilgrim"
    attack: int = 0

    def hangman(self):
        print(f"{self.name} has dishonoured the town and will be put to death!")
        self.alive = False


# Coven Members
class Coven(Player):
    role_name: str = "Covenite"
    necro: bool = False
    attack: int = 0

    def night_action(self, target):
        if self.necro:
            return actions.BookAction(self, target, priority=5)


# Basic healer role
class Cleric(Townie):
    role_name: str = "Cleric"
    alignment: str = "tp"
    priority: int = 2

    def night_action(self, target):
        return actions.ClericAction(self, target, priority=self.priority)


# Stops their target from performing their night action
class Tavern(Townie):
    role_name: str = "Tavern Keeper"
    alignment: str = "ts"
    priority: int = 1

    def night_action(self, target):
        return actions.TavAction(self, target, priority=self.priority)


class Sheriff(Townie):
    role_name: str = "Sheriff"
    alignment: str = "ti"
    priority: int = 3

    def night_action(self, target):
        return actions.SheriffAction(self, target, priority=self.priority)


# Checks 2 roles and knows if the players are on the same team
class Seer(Townie):
    role_name: str = "Seer"
    alignment: str = "ti"

    def night_action(self, target1, target2):
        if type(target1) == type(target2):
            print(f"A seer has checked players {target1.number} and {target2.number}, finding them to be friends")
        else:
            print(f"A seer has checked players {target1.number} and {target2.number}, finding them to be enemies")


# Mayor Class
class Mayor(Townie):
    role_name: str = "Mayor"
    alignment: str = "tpow"

    def day_action(self):
        print("{self.name} has revealed themselves as the mayor!")
        self.votes += 2
        self.suspicion = 0.0


class Conjurer(Player):

    def day_action(self, target):
        print("The conjurer has conjured a meteor!")
        print(f"Player {target.number} faces an untimely end!")
        target.alive = False
