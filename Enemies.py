from random import randint

class Enemy:
    def __init__(self, type, level, hp):
        self.type = type
        self.level = level
        self.hp = hp

    def assign(self):

        if self.type == 'imp':
            self.level = 1
            self.hp = 2

        if self.type == 'gargoyle':
            self.level = 2
            self.hp = 5

        elif self.type == 'statue':
            self.level = 3
            self.hp = 5

        elif self.type == 'goblin':
            self.level = 5
            self.hp = 7

        elif self.type == 'orc':
            self.level = 7
            self.hp = 10

    def attack(self):
        return randint(1, self.level)

    def hurt(self, damage):
        self.hp -= damage
        return self.hp
