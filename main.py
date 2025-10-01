from Player import Player
from Rooms import Room


def askname():
    name = input('Enter your name\n')
    return name



def main():
    p1 = Player(askname(), [])
    room = Room('')
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
                room.changeroom(room.getexits()[command.split()[1]])

            if command.startswith('take '):
                if command.strip('take ') not in room.getitems():
                    print('Invalid item')
                    continue
                p1.takeitem(command.strip('take '))










        except EOFError:
            break

main()