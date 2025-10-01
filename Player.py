
class Player:
    def __init__(self, playername, playeritems, damage, hp):
        self.playername = playername
        self.playeritems = playeritems
        self.damage = damage
        self.hp = hp

    def getplayername(self):
        return self.playername

    def takeitem(self, item):
        self.playeritems.append(item)


    def inventory(self):
        print(self.playeritems)

    def hurt(self, amount):
        self.hp -= amount

    def armour(self, amount):
        self.hp += amount

    def heal(self, item):
        pass
