from Player import Player
from Rooms import Room
from Enemies import Enemy
from time import sleep
from random import choice, randrange
import os

def printdelay(text, delay):
    print(text)
    sleep(delay)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def ask(text):
    x = input(f'{text}\n>> ').lower().strip()
    if x in ['yes', 'y']:
        return True
    else:
        return False

def library(player):
    if player.gold < 2:
        printdelay('"Hoot! Come back when you have more gold"',2)
        return False

    if player.gold >= 2:
        if ask('"Hoot! Would you like to buy a health potion?'):
            player.addgold(-2)
            player.takeitem('health potion')

    if player.gold >= 3:
        if ask('"Hoot! Would you like to buy the spell book?'):
            player.addgold(-3)
            player.takeitem('spell book')
    return True


def movinglogic(room,roomtomove,player):

    if roomtomove in room.locked:
        if roomtomove == 'maze' and room.room == 'gate':
            printdelay("""You walk up to the cold grey metal gate, it towering above you.""",2)
            printdelay("""A single padlock is all that keeps it closed. Maybe there is a way of opening it""", 2)
        if roomtomove == 'watch tower' and room.room == 'library':
            printdelay("""You try the small green painted wooden door. Its locked""", 2)

        return False


    if roomtomove == 'entrance' and room.room == 'garden':
        printdelay('You walk along the thin gravel paths surrounded by many exotic plants, eventually arriving at the doorway of the castle.',2)
        printdelay('A gargoyle stands guard, its stone eyes following your every move.', 2)
        printdelay('As you approach, the gargoyle suddenly swivels its head, and leaps towards you.', 2)
        if not fight('gargoyle', player, room):
            print('lost')
            return False
        else:
            print('won')
            room.unlock(roomtomove)

    if roomtomove == 'maze' and room.room == 'gate':
        printdelay("""The gate creaks eerily as you push it open, its hinges worn down by time and the environment..""",
                   2)
        printdelay("""You walk along a large dirt path, eventually coming to the entrance of a maze""", 2)
        if not ask('Would you like to enter the maze?\n'):
            printdelay('You are too scared to enter the maze and run back.', 2)
            return False
        printdelay("""You enter the maze, searching for many hours to find a path that will lead you somewhere.""", 2)

    if roomtomove == 'garden' and room.room == 'maze':
        printdelay("""You now must find the other exit to the maze.""", 3)
        printdelay("""While you walk between the tall hedges, you hear faint voices in the wind. They say...""", 4)
        if not maze():
            printdelay("""You could not understand their directions and ended up at the center of the maze again.""", 1)
            return False
        printdelay('You make it out of the maze thanks to the help of some unseen force.', 2)
        printdelay("""You approach a beautiful garden, the sound of running water echoing around you""", 2)

    return True

def takinglogic(room,item,player):


    if item == 'sword' and room.room == 'maze':
        printdelay("""You slowly take the sword from the skeletons hand, trying your best not to disturb his peace.""",2)
        printdelay("""There is heavy damage to his skull, as well as many gnaw mark on his bones. You wonder what happened...""",2)
        printdelay("""You notice a small leather bag of gold coins laying next to him.""",2)
        player.addgold(2)

    if item == 'gold coin' and room.room == 'garden':
        printdelay("""You put your hand in the cold water and reach down to pick up a coin.""",2)
        if garden(player):
            printdelay("""You take a coin from the fountain.\nThe strange creatures do not seem happy.""",2)
            player.addgold(1)
            return False
        printdelay("""You feel a sharp pain on your hand, and quickly pull your hand out from the water.\nOne of the creatures bit you.""",2)
        player.hurt(1)

    if item in ['health potion', 'spell book'] and room.room == 'library':
        printdelay(f'As you go to take the {item} from the shelf, an owl silently glides down from the shadows, and perches on your arm.',2)
        if 'rat' in room.rooms['kitchen']['Enemies']:
            printdelay('"Hoot!", Says the owl, "I have some items for you traveler... but I am far too hungry to do business right now. Hoot!"',2)
            return False

        rich = library(player)

        printdelay('The owl flies silently away and watches you with its large yellow eyes from the dark',2)

        if not rich:
            return False

    if item in ['gold coin', 'health potion',]:
        return False
    return True


def maze():
    directions = []
    userswords = []
    for i in range(5):
        word = choice(['right', 'left', 'straight', 'back'])
        clear()
        print('')
        sleep(0.5)
        print(word)
        sleep(0.5)
        print('')
        clear()
        directions.append(word)

    for i ,name in enumerate(['first', 'second', 'third', 'fourth','fifth']):
        word = input(f'{name} direction\n>> ').strip().lower()
        userswords.append(word)

    if directions == userswords:
        return True
    return False


def garden(player):
    chance = randrange(1, 1 + (player.gold + 1) * (player.gold + 1))
    if chance == 1:
        return True
    return False


def askname():
    name = input('Enter your name\n')
    return name


def calculateresult(firstaction,secondaction):
    match [firstaction,secondaction]:
        case ['attack', 'block'] | ['block', 'block'] | ['block','attack']:
            return False, False
        case ['heavy attack','block']:
            return False, True
        case ['block','heavy attack']:
            return True, False
        case ['heavy attack', 'attack']:
            result = choice([True, False ,False, False])
            if result:
                return False, True
            else:
                return True, False
        case ['attack','heavy attack']:
            result = choice([True, False ,False, False])
            if result:
                return True, False
            else:
                return False, True
        case ['heavy attack', 'heavy attack']:
            result = choice([True, False])
            if result:
                return False, True 
            else:
                return True, False
        case ['attack', 'attack']:
            result = choice([True, False])
            if result:
                return False, True 
            else:
                return True, False
        case _:
            print('UMMMMMMMMM')


def fight(enemytype,player,room):
    enemy = Enemy(enemytype,0,0,'')
    enemy.assign()
    firstaction = ''
    secondaction = ''
    listo = ['enemy','player']

    while enemy.hp > 0 and player.hp > 0:
        listo.reverse()
        printdelay(f'{listo[0]}s turn to attack',1)
        for i in listo:
            if i == 'player':
                while True:
                    print(f'Enemys health: {enemy.hp * "- "}')
                    print(f'Your health: {player.hp * "- "}')
                    command = input('Input\n').strip().lower()

                    if command in ['retreat','exit','quit']:
                        if enemy.type in ['gargoyle']:
                            printdelay('You may not flee this battle.',1)
                            break
                        print('You flee the battle.')
                        return True

                    if command in ['attack', 'heavy attack', 'block']:
                        playeraction = command
                        if not firstaction:
                            firstaction = command
                        else:
                            secondaction = command
                        playerdamage = player.attack(command)
                        break

                    if command == 'commands':
                        print("""----COMBAT----
retreat: exit the battle. (warning: The enemy will have healed if you decide to fight them again)
attack: attack the enemy using your equipped weapon
block: block the enemies attack to take less damage
heavy attack: inflict more damage on your enemy """)
                        continue
                    else:
                        printdelay('The pressure of battle gets to you.\nYou stand there motionless.\n(Invalid command)',3)
                        break

            elif enemy.hp > 0:
                enemyaction, enemydamage = enemy.attack()
                if not firstaction:
                    firstaction = enemyaction
                else:
                    secondaction = enemyaction
                printdelay(f'{enemy.type} uses {enemyaction}',1)
        first, second = calculateresult(firstaction,secondaction)
        if listo[0] == 'player':
            playerhurt = first
            enemyhurt = second
        else:
            playerhurt = second
            enemyhurt = first

        if playerhurt:
            if playeraction == 'block':
                enemyaction -= 2
            printdelay(f'The {enemy.type} does {enemydamage} points of damage', 2)
            player.hurt(enemydamage)

        if enemyhurt:
            if enemyaction == 'block':
                playerdamage -= 2
            enemy.hurt(playerdamage)
            printdelay(f'You do {playerdamage} points of damage', 2)

        firstaction = ''
        secondaction = ''
        
    if player.hp > 0:
        printdelay(f'You defeated the {enemy.type}.',1)
        if enemy.item:
            player.takeitem(enemy.item)
        if enemy.type not in ['gargoyle']:
            room.removeenemy(enemy.type)
        return True
    print('You were slain :(')
    return False


def main():
    player = Player(askname(), ['chain mail','sword'],2, 10, 'fists','plaid shirt',0,0,10)
    room = Room('',['maze','entrance','laboratory','watch tower'])
    room.changeroom('kitchen')
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
equip 'item': equip an item that is in your inventory
fight 'enemy': fight a specific enemy in the room
exit / quit: exit game
----COMBAT----
retreat: exit the battle. (warning: The enemy will have healed if you decide to fight them again)
attack: attack the enemy using your equipped weapon
block: block the enemies attack to take less damage
heavy attack: inflict more damage on your enemy 
""")
                continue

            if command == 'look':
                room.look()
                continue

            if command == 'stats':
                player.stats()
                continue

            if command.startswith('go '):
                if command.split()[1] not in room.getexits():
                    print('Invalid direction')
                    continue
                roomtomove = room.getexits()[command.split()[1]]
                if movinglogic(room, roomtomove, player):
                    room.changeroom(roomtomove)
                continue


            if command.startswith('take '):
                item = command.replace('take ','')
                if item not in room.getitems():
                    print('Invalid item')
                    continue
                if not takinglogic(room, item, player):
                    continue
                room.removeitem(item)
                if item not in ['gold coin']:
                    player.takeitem(item)
                continue


            if command.startswith('use '):
                used = command.replace('use ','')
                if used not in player.playeritems:
                    print('You do not have that item')
                    continue

                if used == 'grey key' and room.room == 'gate' and 'maze' in room.locked:
                    print('You use the key to unlock the gate')
                    room.unlock('maze')

                if used == 'green key' and room.room == 'library' and 'watch tower' in room.locked:
                    print('You use the key to unlock the door to the watch tower')
                    room.unlock('watch tower')

            if command.startswith('fight '):
                enemy = command.replace('fight ','')
                if room.room == 'gate' and enemy in ['gate','lock','padlock',] and 'maze' in room.locked:
                    print(f'You break the lock open with your {player.weapon}.')
                    room.unlock('maze')
                    continue
                if enemy not in room.getenemies():
                    print('Enemy does not exist')
                    continue

                if fight(enemy,player,room):
                    continue
                break


            if command.startswith('equip '):
                item = command.replace('equip ','')
                if item in ['fists','sword','knife','gun',]:

                    if item == player.weapon:
                        print('You already have this weapon equipped!')
                        continue
                    if item not in player.playeritems and item != 'fists':
                        print('You do not have that weapon.')
                        continue
                    player.equip(item)

                elif item in ['chain mail','plate armour','bomb suit']:

                    if item == player.armour:
                        print('You already have this set of armour equipped!')
                        continue
                    if item not in player.playeritems:
                        print('You do not have that set of armour')
                        continue
                    player.equiparmour(item)


            else:
                print("Invalid command\nHint: use 'commands' to see available commands")





        except EOFError:
            pass

main()