from random import randint




class Player:
    def __init__(self, playername, playeritems, damage, hp, weapon,armour, armourhp, gold ):
        self.playername = playername
        self.playeritems = playeritems
        self.damage = damage
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.armourhp = armourhp
        self.gold = gold

    def getplayername(self):
        return self.playername

    def takeitem(self, item):
        print(f'You pick up the {item}')
        self.playeritems.append(item)

    def stats(self):
        print(f'Inventory: {(", ".join(self.playeritems), "Empty")[len(self.playeritems) == 0]}')
        print(f'Weapon: {self.weapon} \nDamage: {self.damage}')
        print(f'Armour: {self.armour} \nProtection: {self.armourhp}')
        print(f'Gold: {self.gold}')
        print(f'Health: {self.hp * "- "}')

    def hurt(self, amount):
        if self.armourhp < 1:
            self.hp -= amount

        else:
            print(f'Your armour absorbs some of the damage')
            self.armourhp -= amount - 1
            self.hp -= 1

    def heal(self, item):

        med = {'health potion': 9,
               'bread': 2,
               'spinach': 100,}
        self.hp += med[item]
        print(f'You health goes up {med[item]} points')

    def attack(self,action):
        match action:
            case 'attack':
                return randint(1,self.damage)
            case 'heavy attack':
                return randint(1+2,self.damage+2)
            case 'block':
                return 0
            case _:
                pass

    def equip(self, item):
        print(f'You take the {item} and hold it firmly in your hand')
        weaponslist = {'sword' : 4,
                       'knife' : 5,
                       'fists' : 2,
                       'gun' : 100,}

        if self.weapon != 'fists':
            self.takeitem(self.weapon)
        if item != 'fists':
            self.playeritems.remove(item)

        self.weapon = item
        self.damage = weaponslist[item]

    def equiparmour(self, item):
        print(f'You put on the {item}')
        armourslist = {'chain mail' : 2,
                       'plate armour' : 4,
                       'bomb suit' : 100,}

        if self.armour != 'plaid shirt':
            self.takeitem(self.armour)
        self.playeritems.remove(item)
        self.armour = item
        self.armourhp = armourslist[item]

    def addgold(self, amount):
        self.gold += amount
