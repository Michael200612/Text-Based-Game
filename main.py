from Player import Player
from Rooms import Room


def askname():
    name = input('Enter your name\n')
    return name



def main():
    p1 = Player(askname(), [],2, 10)
    room = Room('',['maze'])
    room.changeroom('gate')
    while True:
        try:
            command = input('\nInput\n').strip().lower()

            if command in ('exit', 'quit'):
                break

            if command == 'look':
                room.look()
                continue

            if command == 'inventory':
                p1.inventory()

            if command.startswith('go '):

                if command.split()[1] not in room.getexits():
                    print('Invalid direction')
                    continue

                roomtomove = room.getexits()[command.split()[1]]

                if roomtomove in room.locked:
                    print('You may not go there.')
                    continue
                room.changeroom(roomtomove)

            if command.startswith('take '):
                item = command.strip('take ')
                if item not in room.getitems():
                    print('Invalid item')
                    continue

                p1.takeitem(item)
                room.removeitem(item)

            if command.startswith('use '):
                used = command.strip('use ')
                if used not in p1.playeritems:
                    print('You do not have that item')
                    continue

                if used == 'grey key' and room.room == 'gate' and 'maze' in room.locked:
                    print('You use the key to unlock the gate')
                    room.locked.pop(room.locked.index('maze'))






        except EOFError:
            break

main()