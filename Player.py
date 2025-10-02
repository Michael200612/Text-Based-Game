from random import randint

class Player:
    def __init__(self, playername, playeritems, damage, hp, weapon):
        self.playername = playername
        self.playeritems = playeritems
        self.damage = damage
        self.hp = hp
        self.weapon = weapon

    def getplayername(self):
        return self.playername

    def takeitem(self, item):
        self.playeritems.append(item)



    def stats(self):
        print(f'Inventory: {(", ".join(self.playeritems), "Empty")[len(self.playeritems) == 0]}')
        print(f'Weapon: {self.weapon} \nDamage: {self.damage}')
        print(f'HP: {self.hp * "- "}')

    def hurt(self, amount):
        self.hp -= amount

    def armour(self, amount):
        self.hp += amount

    def heal(self, item):
        pass

    def attack(self):
        return randint(1,self.damage)

    def equip(self, item):
        weaponslist = {'sword' : 4,
                       'knife' : 5,
                       'fists' : 2,
                       'gun' : 100,}

        if self.weapon != 'fists':
            self.takeitem(self.weapon)
            self.playeritems.remove(item)

        self.weapon = item
        self.damage = weaponslist[item]

