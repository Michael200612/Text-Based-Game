from random import randint
from time import sleep

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
        print(f'You put the {item} in your bag')
        if item == 'gold coin':
            self.addgold(1)
        else:
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

        med = {'health potion': 6,
               'bread': 2,
               'spinach': 100,
               'cheese' : 4}
        if 10 < self.hp + med[item] and item != 'spinach':
            self.hp = 10
            print("You are at full health")
        else:
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
                return 0

    def equip(self, item):
        print(f'You take the {item} and hold it firmly in your hand')
        weaponslist = {'sword' : 4,
                       'knife' : 5,
                       'fists' : 2,
                       'shovel' : 7,
                       'spell book': 8,
                       'gun' : 100,}

        if self.weapon != 'fists':
            self.takeitem(self.weapon)
        if item != 'fists':
            self.playeritems.remove(item)

        self.weapon = item
        self.damage = weaponslist[item]

    def equiparmour(self, item):
        armourslist = {'plaid shirt' : 0,
                        'chain mail' : 3,
                        'plate armour' : 5,
                        'bomb suit' : 100,}
        if item != self.armour:
            print(f'You put on the {item}')
            if self.armour != 'plaid shirt':
                self.takeitem(self.armour)
            self.playeritems.remove(item)
            self.armour = item
        self.armourhp = armourslist[item]

    def addgold(self, amount):
        self.gold += amount

    def use(self, item, room):
        if item == 'book':
            print('You open the book to a random page. This is what you read.')
            sleep(1)
            match room.room:
                case 'gate':
                    print('You are very strong. The lock is very weak.\n(Also, "xyz" is a hidden command!)')
                    sleep(1)
                case 'maze':
                    print('Equip the sword to use it instead of your fists')
                    sleep(1)
                case 'garden':
                    print('Do not be too greedy')
                    sleep(1)
                case 'entrance':
                    print('Use the map to see the layout of the rooms')
                    sleep(1)
                case 'grand hall':
                    print('Defeat the animated suit of armour to wear it')
                    sleep(1)
                case 'library':
                    print('The kitchen is infested with rodents')
                    sleep(1)
                case 'watch tower':
                    print('Giving up can help you in some situations...')
                    sleep(1)
                case 'armoury':
                    print('Equip the armour to wear it')
                    sleep(1)
                case 'dungeon':
                    print('Defeat the evil wizard to win the game')
                    sleep(1)
                case 'graveyard':
                    print('Defeat the zombies to get gold coins')
                    sleep(1)
                case 'laboratory':
                    print('The laboratory has been said to be the birth place of all the strange creatures...')
                    sleep(1)

        elif item in ['bread','health potion', 'spinach', 'cheese']:
            print(f'You consume the {item}')
            self.heal(item)
            self.playeritems.remove(item)
            sleep(1)
        elif item == 'map':
            print("""
+-----------+-------------+
|   Grave   |             |
|   Yard       Laboratory |
|           |             |
|----   ----|----    -----|-------------+
|           |             |             |
|  Armoury  |   Dungeon   |  Kitchen    |
|           |             |             |
+---    ----|-------------|-----    ----+
|           |             |    Grand    |
|  Library     Entrance        Hall     |
|           |             |             |
|---    ----|----    -----|-------------+
|   Watch   |             |        
|   Tower   |   Garden    |     
|           |             |            
|-----------|----    -----|
|           |             |
|   Gate         Maze     |
|           |             |
+-----------+-------------+
""")