from random import randrange

class Enemy:
    def __init__(self, type, level, hp):
        self.type = type
        self.level = level
        self.hp = hp

    def assign(self):
        if self.type == 'statue':
            self.level = 1
            self.hp = 5

        elif self.type == 'goblin':
            self.level = 2
            self.hp = 7

        elif self.type == 'orc':
            self.level = 4
            self.hp = 10

    def attack(self):
        return randrange(self.level, self.hp)

    def hurt(self, damage):
        self.hp -= damage
        return self.hp
