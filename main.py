from Player import Player
from Rooms import Room
from Enemies import Enemy
from time import sleep
from random import choice
import os

def printdelay(text, delay):
    print(text)
    sleep(delay)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ask(text):
    x = input(f'{text}\n>>').lower().strip()
    if x in ['yes', 'y']:
        return True
    else:
        return False

def maze():
    directions = []
    userswords = []
    for i in range(4):
        clear()
        word = choice(['right', 'left', 'straight', 'back'])
        print(word)
        sleep(1)
        clear()
        directions.append(word)

    for i ,name in enumerate(['first', 'second', 'third', 'fourth']):
        word = input(f'{name} direction\n').strip().lower()
        userswords.append(word)

    if directions == userswords:
        return True
    return False


def askname():
    name = input('Enter your name\n')
    return name

def fight(e,p1,room):
    enemy = Enemy(e,0,0)
    enemy.assign()

    listo = ['player','enemy']

    while enemy.hp > 0 and p1.hp > 0:
        for i in listo:
            if i == 'player':
                while True:
                    print(f'Enemies health: {enemy.hp * "- "}')
                    print(f'Your health: {p1.hp * "- "}')
                    command = input('Input\n').strip().lower()

                    if command in ['retreat','exit','quit']:
                        print('You flee the battle.')
                        return True

                    if command == 'attack':
                        damage = p1.attack()
                        print(f'You do {damage} damage.')
                        enemy.hurt(damage)
                        sleep(2)
                        break

                    if command == 'commands':
                        print("""----COMBAT----
    retreat: exit the battle. (warning: The enemy will have healed if you decide to fight them again)
    attack: attack the enemy using your equipped weapon
    block: IN DEVELOPMENT
    heavy attack: IN DEVELOPMENT""")
                        continue

                    else:
                        printdelay('The pressure of battle gets to you.\nYou stand there motionless.\n(Invalid command)',3)

            elif enemy.hp > 0:
                damage = enemy.attack()
                print(f'the {enemy.type} does {damage} damage.')
                p1.hurt(damage)
                sleep(2)

    if p1.hp > 0:
        print(f'You defeated the {enemy.type}.')
        sleep(1)
        if enemy.type != 'snake':
            room.removeenemy(enemy.type)
        return True
    print('You were slain :(')
    return False


def main():
    p1 = Player(askname(), [],1, 10, 'fists')
    room = Room('',['maze'])
    room.changeroom('gate')
    while True:
        try:
            command = input('\n>> ').strip().lower()

            if command in ('exit', 'quit'):
                break

            if command == 'commands':
                print("""----GAME----
commands: see a list of commands
look: see information about the room you are in
stats: see information about your character
go 'direction': move in a certain direction
take 'item': take a certain item in the room
use 'item': use a certain item in your inventory
equip 'weapon': equip a weapon that is in your inventory
fight 'enemy': fight a specific enemy in the room
exit / quit: exit game
----COMBAT----
retreat: exit the battle. (warning: The enemy will have healed if you decide to fight them again)
attack: attack the enemy using your equipped weapon
block: IN DEVELOPMENT
heavy attack: IN DEVELOPMENT 
""")

            if command == 'look':
                room.look()
                continue

            if command == 'stats':
                p1.stats()

            if command.startswith('go '):

                if command.split()[1] not in room.getexits():
                    print('Invalid direction')
                    continue

                roomtomove = room.getexits()[command.split()[1]]

                if roomtomove in room.locked:
                    if roomtomove == 'maze':
                        printdelay("""You walk up to the cold grey metal gate, it towering above you.
A single copper padlock is all that keeps it closed. Maybe there is a way of opening it""",2)
                    continue


                if roomtomove == 'maze' and room.room == 'gate':
                    printdelay("""The gate creaks eerily as you push it open, its hinges worn down by time and the environment..""",2)
                    printdelay("""You walk along a large dirt path, eventually coming to the entrance of a maze""",2)
                    if not ask('Would you like to enter the maze?\n'):
                        printdelay('You are too scared to enter the maze and run back.',2)
                        continue
                    printdelay("""You enter the maze, searching for many hours to find a path that will lead you somewhere.""", 2)


                if roomtomove == 'garden' and room.room == 'maze':
                    printdelay("""You now must find the other exit to the maze.""",2)
                    printdelay("""While you walk between the tall hedges, you hear faint voices in the wind. They say...""",3)
                    if not maze():
                        printdelay("""You could not understand their directions and ended up at the center of the maze again.""",1)
                        continue
                    print('You make it out of the maze')


                room.changeroom(roomtomove)
                continue



            if command.startswith('take '):
                item = command.replace('take ','')
                if item not in room.getitems():
                    print('Invalid item')
                    continue

                p1.takeitem(item)
                room.removeitem(item)

                if item == 'sword' and room.room == 'maze':
                    printdelay("""You slowly take the sword from the skeletons hand, trying your best not to disturb his peace.
You notice two small holes engraved on his wrist bone, like he was bitten by an animal.
A snake reveals itself from the hedges of the maze, hissing at you and approaching you with speed.""",3)
                    if fight('snake',p1,room):
                        printdelay('You rest for a while after the intense battle, and try to regain your strength.',1)
                        p1.heal('bread')
                        continue
                    printdelay("""The snake slithers away from your lifeless body, triumphant.
A magical fairy appears from thin air and revives you.
'How could you die to the first enemy?', it asks.
It flies away""",2)
                    p1.heal('health potion')

            if command.startswith('use '):
                used = command.replace('use ','')
                if used not in p1.playeritems:
                    print('You do not have that item')
                    continue


                if used == 'grey key' and room.room == 'gate' and 'maze' in room.locked:
                    print('You use the key to unlock the gate')
                    room.unlock('maze')


            if command.startswith('fight '):
                enemy = command.replace('fight ','')
                if room.room == 'gate' and enemy in ['gate','lock','padlock',] and 'maze' in room.locked:
                    print(f'You break the lock open with your {p1.weapon}.')
                    room.unlock('maze')
                    continue
                if enemy not in room.getenemies():
                    print('Enemy does not exist')
                    continue

                if fight(enemy,p1,room):
                    continue
                break

            if command.startswith('equip '):
                weapon = command.replace('equip ','')
                if weapon not in ['fists','sword','knife','gun',]:
                    print('Not a valid weapon')
                    continue
                if weapon == p1.weapon:
                    print('You already have this weapon equipped!')
                    continue
                if weapon not in p1.playeritems and weapon != 'fists':
                    print('You do not have that weapon.')
                    continue
                p1.equip(weapon)

            else:
                print("Invalid command\nHint: use 'commands' to see available commands")





        except EOFError:
            pass

main()