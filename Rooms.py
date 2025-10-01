
class Room:
    rooms = {'gate': {'Exits': {'east' : 'maze'}, 'Items': ['grey key'], 'Description' : '...',},
             'maze': {'Exits': {'north' : 'garden','west' : 'gate'}, 'Items': ['sword'], 'Description' : '...'},
             'garden': {'Exits': {'north' : 'entrance', 'south' : 'maze'}, 'Items': [], 'Description' : '...'},
             'entrance': {'Exits': {'south' : 'garden', 'east' : 'ball room', 'west' : 'library'}, 'Items': [], 'Description' : '...'},
             'ballroom': {'Exits': {'west' : 'entrance', 'north' : 'dining room'}, 'Items': [], 'Description' : '...'},
             'library': {'Exits': {'south' : 'watch tower', 'east' : 'entrance'}, 'Items': [], 'Description' : '...'},}

    def __init__(self, room, locked):
        self.room = room
        self.locked = locked

    def getexits(self):
        return Room.rooms[self.room]['Exits']

    def getitems(self):
        return Room.rooms[self.room]['Items']

    def look(self):
        print(f'Yuo are at the {self.room}')
        print(f"Description: {Room.rooms[self.room]['Description']}")
        print(f"Exit{('s','')[len(self.getexits()) == 1]} in room: {', '.join(self.getexits())}")
        print(f"Item{('s','')[len(self.getitems()) == 1]} in room: {(', '.join(Room.rooms[self.room]['Items']), 'There are no items')[len(self.getitems()) == 0]}")

    def changeroom(self, room):
        self.room = room

    def removeitem(self, item):
        Room.rooms[self.room]['Items'].remove(item)

