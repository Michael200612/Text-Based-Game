
class Room:
    rooms = {'gate': {'Exits': {'east' : 'maze'}, 'Items': ['grey key'], 'Description' : 'You stand at the entrance to an ancient castle. \nYour first obstacle: A large grey gate, with tall stone walls on either sides.','Enemies': ['imp']},
             'maze': {'Exits': {'north' : 'garden','west' : 'gate'}, 'Items': ['sword'], 'Description' : '...','Enemies': []},
             'garden': {'Exits': {'north' : 'entrance', 'south' : 'maze'}, 'Items': [], 'Description' : '...','Enemies': ['statue']},
             'entrance': {'Exits': {'south' : 'garden', 'east' : 'ball room', 'west' : 'library'}, 'Items': [], 'Description' : '...','Enemies': []},
             'ballroom': {'Exits': {'west' : 'entrance', 'north' : 'dining room'}, 'Items': [], 'Description' : '...','Enemies': []},
             'library': {'Exits': {'south' : 'watch tower', 'east' : 'entrance'}, 'Items': [], 'Description' : '...'},'Enemies': ['wise owl']}

    def __init__(self, room, locked):
        self.room = room
        self.locked = locked

    def getexits(self):
        return Room.rooms[self.room]['Exits']

    def getitems(self):
        return Room.rooms[self.room]['Items']

    def getenemies(self):
        return Room.rooms[self.room]['Enemies']

    def look(self):
        print(f'Yuo are at the {self.room}')
        print(f"Description: {Room.rooms[self.room]['Description']}")
        print(f"Exit{('s','')[len(self.getexits()) == 1]} in room: {', '.join(self.getexits())}")
        print(f"Item{('s','')[len(self.getitems()) == 1]} in room: {(', '.join(self.getitems()), 'There are no items')[len(self.getitems()) == 0]}")
        if len(self.getenemies()) > 0:
            print(f"Enem{('ies', 'y')[len(self.getenemies()) == 1]} in room: {', '.join(self.getenemies())}")

    def changeroom(self, room):
        self.room = room

    def removeitem(self, item):
        Room.rooms[self.room]['Items'].remove(item)

    def unlock(self,room):
        self.locked.pop(self.locked.index(room))

    def removeenemy(self,enemy):
        Room.rooms[self.room]['Enemies'].pop(self.getenemies().index(enemy))