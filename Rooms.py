
class Room:
    rooms = {'gate': {'Exits': {'east' : 'maze'}, 'Items': ['grey key'], 'Description' : '...',},
             'maze': {'Exits': {'north' : 'garden','west' : 'gate'}, 'Items': ['sword'], 'Description' : '...'},
             'garden': {'Exits': {'north' : 'entrance'}}, 'Items': [], 'Description' : '...'}

    def __init__(self, room):
        self.room = room

    def getexits(self):
        return Room.rooms[self.room]['Exits']

    def getitems(self):
        return Room.rooms[self.room]['Items']

    def look(self):
        print(f'Yuo are at the {self.room}')
        print(f"Description: {Room.rooms[self.room]['Description']}")
        print(f"Exit{('','s')[len(self.getexits()) > 1]}in room: {', '.join(self.getexits())}")
        print(f"Item{('','s')[len(self.getitems()) > 1]} in room: {', '.join(Room.rooms[self.room]['Items'])}")

    def changeroom(self, room):
        self.room = room