from random import randint,choice
from unittest import case


class Enemy:
    def __init__(self, type, level, hp):
        self.type = type
        self.level = level
        self.hp = hp

    def assign(self):

        if self.type == 'imp':
            self.level = 1
            self.hp = 2

        elif self.type == 'gargoyle':
            self.level = 2
            self.hp = 5

        elif self.type == 'rat':
            self.level = 3
            self.hp = 5

        elif self.type == 'zombie':
            self.level = 5
            self.hp = 7

        elif self.type == 'suit of armour':
            self.level = 7
            self.hp = 10

    def attack(self):
        #choice = 'attack'
        action = choice(['heavy attack','block','attack'])
        match action:
            case 'attack':
                return action, randint(1, self.level)
            case 'block':
                return action, 0
            case 'heavy attack':
                return action, randint(2, self.level + 2)
            case _:
                pass

    def hurt(self, damage):
        self.hp -= damage
        return self.hp
