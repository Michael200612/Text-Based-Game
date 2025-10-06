from Player import Player
from Rooms import Room
from Enemies import Enemy
from time import sleep
from random import choice, randint
import os
from test import nuclearbomb


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


def tower():
    orcs = 0
    field = []
    for i in range(7):
        creature = choice([' cow',' orc'])
        if creature == ' orc':
            orcs += 1
        field.append(creature)
    clear()
    printdelay('',1)
    printdelay(''.join(field),1.5)
    clear()
    answer = input('How many orcs did you see?\n>> ')
    if answer == 'i give up':
            return True
    if answer == str(orcs):
        return True
    return False


def library(player, item):
    prices = {'health potion' : 2,
              'spell book' : 3
              }
    if player.gold < prices[item]:
        printdelay('"Hoot! Come back when you have more gold"',2)
        return False

    if ask(f'"Hoot! Would you like to buy a {item}?'):
        player.addgold(-(prices[item]))
        return True
    
    return False

def laboratory():
    listo = []
    userwords = []
    for j in range(5):
        gems = 0
        shelf = []
        for i in range(7):
            element = choice(['gem','coal'])
            if element == 'gem':
                gems += 1
            shelf.append(element)
        printdelay(', '.join(shelf),1.5)
        listo.append(str(gems))
        clear()

    for i ,name in enumerate(['first', 'second', 'third', 'fourth','fifth']):
        word = input(f'Amount of gems on {name} shelf\n>> ').strip().lower()
        userwords.append(word)
        if word == 'i give up':
            return True
    if userwords == listo:
        return True
    return False

def movinglogic(room,roomtomove,player):

    if roomtomove in room.locked:
        if roomtomove == 'maze' and room.room == 'gate':
            printdelay("""You walk up to the cold grey metal gate, it towering above you.""",2)
            printdelay("""A single padlock is all that keeps it closed. Maybe there is a way of opening it""", 2)
            return False
        if roomtomove == 'watch tower' and room.room == 'library':
            printdelay("You try the small green painted wooden door. Its locked.", 2)
            return False
        if roomtomove == 'laboratory' and room.room == 'graveyard':
            printdelay('You try to open the large blueish metal door. Its locked.',2)
            return False
        
        if roomtomove == 'entrance' and room.room == 'garden':
            printdelay('You walk along the thin gravel paths surrounded by many exotic plants, eventually arriving at the doorway of the castle.',2)
            printdelay('A gargoyle stands guard, its stone eyes following your every move.', 2)
            printdelay('As you approach, the gargoyle suddenly swivels its head, and leaps towards you.', 2)
            if not fight('gargoyle', player, room):
                pass
            else:
                printdelay('The gargoyle crumbles into pieces, turning to powder as it falls down to the ground.',2)
                printdelay('You are now free to enter',1)
                room.unlock(roomtomove)
            return False

        if roomtomove == 'dungeon' and room.room == 'laboratory':
            printdelay('You try to open the metal door. Its locked.',2)
            return False

    if roomtomove == 'dungeon' and room.room == 'laboratory':
            if room.getenemies() != []:
                printdelay('You must defeat all enemies in the room.',2)
                
                return False

    if roomtomove == 'maze' and room.room == 'gate':
        printdelay("""The gate creaks eerily as you push it open, its hinges worn down by time and the environment..""",2)
        printdelay("""You walk along a large dirt path, eventually coming to the entrance of a maze""", 2)
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
        

    if item == 'gold coin' and room.room == 'garden':
    
        printdelay("""You put your hand in the cold water and reach down to pick up a coin.""",2)
        if garden(player):
            printdelay("""You take a coin from the fountain.\nThe strange creatures do not seem happy.""",2)
            player.addgold(1)
            return False
        printdelay("""You feel a sharp pain on your hand, and quickly pull your hand out from the water.\nOne of the creatures bit you.""",2)
        player.hurt(1)

    if item == 'blue key' and room.room == 'watch tower':
        printdelay('As you go to take the key, you peer out of a widnow at the world below. The skey is dark and grey, but you can make out figures in a field',3)
        printdelay('Suddenly a flash of lightning illuminates the surrondings, letting you catch a glimpse of the creatures',3)
        printdelay('What you see is...',3)
        if not tower():
            printdelay("Unsure if you're right, You take another look. As you do, an arrow hits the side of the tower, splintering into many pieces.",2)
            printdelay('You quickly retreat back to safety',2)
            return False
        printdelay('You quickly go passed the window before they notice you',2)

    if item == 'gold key' and room.room == 'laboratory':
        printdelay('As you go to take the gold key, you glance to your right and notice shelves with many precious materials on it',3)
        printdelay('What you see is ...',3)
        if not laboratory():
            printdelay('While trying to remember how many gems you saw, you forget about the key.',2)
            return False
            

    if item in ['health potion', 'spell book'] and room.room == 'library':
        printdelay(f'As you go to take the {item} from the shelf, an owl silently glides down from the shadows, and perches on your arm.',2)
        if 'rat' in room.rooms['kitchen']['Enemies']:
            printdelay('"Hoot!", Says the owl, "I have some items for you traveler... but I am far too hungry to do business right now. Hoot!"',2)
            return False
        rich = library(player, item)
        printdelay('The owl flies silently away and watches you with its large yellow eyes from the dark',2)

        if not rich:
            return False

    if item in ['gold coin']:
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
        if word == 'i give up':
            return True
    if directions == userswords:
        return True
    return False


def garden(player):
    amount = player.gold
    
    chance = randint(1, amount + 1)
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
        clear()
        listo.reverse()
        printdelay(f'{listo[0]}s turn to attack',1)
        for i in listo:
            if i == 'player':
                while True:
                    print(f'Enemy health: {enemy.hp * "- "}')
                    print(f'Enemy level: {enemy.level}')
                    print(f'Your health: {player.hp * "- "}')
                    command = input('Input\n').strip().lower()

                    if command in ['retreat','exit','quit']:
                        if enemy.type in ['gargoyle']:
                            printdelay('You may not flee this battle.',1)
                            break
                        print('You flee the battle.')
                        player.equiparmour(player.armour)
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
                        printdelay('Invalid command',3)
                        continue

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
                enemydamage -= 2
            printdelay(f'The {enemy.type} does {enemydamage} points of damage', 2)
            player.hurt(enemydamage)

        elif enemyhurt:
            if enemyaction == 'block':
                playerdamage -= 2
            enemy.hurt(playerdamage)
            printdelay(f'You do {playerdamage} points of damage', 2)

        else:
            printdelay('No damage is done',2)

        firstaction = ''
        secondaction = ''
        
    if player.hp > 0:
        player.equiparmour(player.armour)
        printdelay(f'You defeated the {enemy.type}.',1)
        if enemy.item:
            player.takeitem(enemy.item)
        if enemy.type not in ['gargoyle']:
            room.removeenemy(enemy.type)
        return True
    print('You were slain :(')
    return False


def main():
    player = Player(askname(), [],2, 10, 'fists','plaid shirt',0,0)
    room = Room('',['maze','entrance','laboratory','watch tower','dungeon'])
    room.changeroom('gate') 
    while True:
        try:
            if 'shadow wizard' not in Room.rooms['dungeon']['Enemies']:
                printdelay('You win the game! :)',2)
                break
            command = input('\n>> ').strip().lower()
            if command in ('exit', 'quit'):
                break
            clear()

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

            if command == 'xyz':
                player.addgold(100)
                player.takeitem('gun')
                player.takeitem('bomb suit')
                player.takeitem('spinach')
                continue

            if command.startswith('xyz teleport '):
                if command.replace('xyz teleport ','') not in Room.rooms:
                    print('Room does not exist')
                    continue
                room.changeroom(command.replace('xyz teleport ','')) 
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

                if takinglogic(room, item, player):
                    room.removeitem(item)
                    player.takeitem(item)
                continue

            if command.startswith('use '):
                used = command.replace('use ','')
                if used not in player.playeritems:
                    print('You do not have that item')
                    continue
                player.use(used,room)
                if used == 'grey key' and room.room == 'gate' and 'maze' in room.locked:
                    print('You use the key to unlock the gate.')
                    room.unlock('maze')
                if used == 'green key' and room.room == 'library' and 'watch tower' in room.locked:
                    print('You use the key to unlock the door to the watch tower.')
                    room.unlock('watch tower')
                if used == 'blue key' and room.room == 'graveyard' and 'laboratory' in room.locked:
                    printdelay('You use the key to unlock the door to the laboratory.',2)
                    printdelay('As the door opens, you see a tall figure in the laboratory run out of view into the shadows, and hear the sound of a metal door slam shut.',2)
                    room.unlock('laboratory')
                if used == 'gold key' and room.room == 'laboratory' and 'dungeon' in room.locked:
                    printdelay('You use the key to unlock the door to the dungeon.',2)
                    room.unlock('dungeon')
                continue

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
                elif (player.playername).lower() == 'ryan':
                    nuclearbomb()
                break

            if command.startswith('equip '):
                item = command.replace('equip ','')
                if item in ['fists','sword','knife','gun','shovel','spell book']:

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

        except:
            pass

main()