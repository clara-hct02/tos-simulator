from models import actions


class Player:
    def __init__(self, number):
        self.number = number
        self.votes = 1
        self.defense = 0
        self.suspicion = 0.3
        self.blocked = False

    def night_action(self, *args):
        pass

    def day_action(self, *args):
        pass


# Town Members
class Townie(Player):
    def __init__(self, number):
        super().__init__(number)
        self.attack = 0

    def hangman(self):
        print(f"Player {self.number} has dishonoured the town and will be put to death!")
        self.alive = False


# Coven Members
class Coven(Player):
    def __init__(self, number):
        super().__init__(number)
        self.necro = False
        self.attack = 0

    def night_action(self, target):
        if self.necro:
            return actions.BookAction(self, target, priority=5)


# Basic healer role
class Cleric(Townie):
    alignment = "tp"
    priority = 2

    def night_action(self, target):
        return actions.ClericAction(self, target, priority=self.priority)


# Stops their target from performing their night action
class Tavern(Townie):
    alignment = "ts"
    priority = 1

    def night_action(self, target):
        return actions.TavAction(self, target, priority=self.priority)


class Sheriff(Townie):
    alignment = "ti"
    priority = 3

    def night_action(self, target):
        return actions.SheriffAction(self, target, priority=self.priority)


# Checks 2 roles and knows if the players are on the same team
class Seer(Townie):
    alignment = "ti"

    def night_action(self, target1, target2):
        if type(target1) == type(target2):
            print(f"A seer has checked players {target1.number} and {target2.number}, finding them to be friends")
        else:
            print(f"A seer has checked players {target1.number} and {target2.number}, finding them to be enemies")


# Mayor Class
class Mayor(Townie):
    alignment = "tpow"

    def day_action(self):
        print("Player {self.number} has revealed themselves as the mayor!")
        self.votes += 2
        self.suspicion = 0.0


class Conjurer(Player):

    def day_action(self, target):
        print("The conjurer has conjured a meteor!")
        print(f"Player {target.number} faces an untimely end!")
        target.alive = False
