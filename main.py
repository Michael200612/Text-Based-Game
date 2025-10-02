from Player import Player
from Rooms import Room
from Enemies import Enemy
from time import sleep



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
                print(f'Enemies health: {enemy.hp * "- "}')
                print(f'Your health: {p1.hp * "- "}')
                command = input('Input\n').strip().lower()

                if command == 'retreat':
                    print('You flee the battle.')
                    return True

                if command == 'attack':
                    damage = p1.attack()
                    print(f'You do {damage} damage.')
                    enemy.hurt(damage)
                    sleep(2)

            elif enemy.hp > 0:
                damage = enemy.attack()
                print(f'the {enemy.type} does {damage} damage.')
                p1.hurt(damage)
                sleep(2)

    if p1.hp > 0:
        print(f'You defeated the {enemy.type}.')
        sleep(1)
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
            command = input('\nInput\n').strip().lower()

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
----COMBAT----
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
                        print("""You walk up to the cold grey metal gate, it towering above you.
A single copper padlock is all that keeps it closed. Maybe there is a way of opening it""")

                    continue
                room.changeroom(roomtomove)

            if command.startswith('take '):
                item = command.replace('take ','')
                if item not in room.getitems():
                    print('Invalid item')
                    continue

                p1.takeitem(item)
                room.removeitem(item)

                if item == 'sword':
                    print("""You slowly take the sword from the skeletons hand, trying your best not to disturb his peace.
You notice two small holes engraved on his wrist bone, like he was bitten by an animal.""")
                    if fight('snake',p1,room):
                        continue
                    print("""The snake slithers away from your lifeless body, triumphant.
    A magical fairy appears from thin air and revives you.
    'How could you die to the first enemy?', it asks.
    It flies away""")
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





        except EOFError:
            break

main()