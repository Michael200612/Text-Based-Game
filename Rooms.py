
class Room:
    rooms = {'gate': {'Exits': {'east' : 'maze'}, 'Items': ['grey key'], 'Enemies': [], 'Description' : 'You stand at the entrance to an ancient castle. Dead plants and trees surround you, and the sky is overcast\nAhead of you is your first obstacle: A large grey gate, with tall stone walls on either sides.'''},
             'maze': {'Exits': {'north' : 'garden','west' : 'gate'}, 'Items': ['sword'], 'Enemies': [],  'Description' : 'You are in the center of the maze. The skeleton of a man lays on the ground, an old rusting sword still in his hand.'''},
             'garden': {'Exits': {'north' : 'entrance', 'south' : 'maze'}, 'Items': ['gold coin'], 'Enemies': [],  'Description' : 'You stand in a large garden, with a stone fountain in the center.\nYou see gold coins glistening at the bottom, while strange eel like creatures swim around in the clear blue water.'''},
             'entrance': {'Exits': {'south' : 'garden', 'east' : 'grand hall', 'west' : 'library'}, 'Items': ['map'],'Enemies': [], 'Description' : 'A larger metal chandelier with hundreds of candles hangs from the cieling, dimly lighting the large room.\nRed carpet covers the floors, and the smooth stone walls are covered in cobwebs.'''},
             'grand hall': {'Exits': {'west' : 'entrance', 'north' : 'kitchen'}, 'Items': ['green key','bread'],'Enemies': ['suit of armour'], 'Description' : 'A large spruce table sits in the center of the hall, with many chairs all perfectly in thier places. There is some food on the table, and a shiny suit of armour stands at the end of the hall.'''},
             'library': {'Exits': {'south' : 'watch tower', 'east' : 'entrance', 'north' : 'armoury'}, 'Items': ['book','spell book','health potion','health potion','health potion'],'Enemies': [], 'Description' : 'Tall wooden bookshelves line the walls, packed tight with thousands of dark leather-bound volumes.\nA heavy reading desk sits near the window, holding an open, brittle book and a ceramic inkwell.'''},
             'armoury': {'Exits': {'south' : 'library', 'north' : 'graveyard'}, 'Items': ['chain mail'],'Enemies': [], 'Description' : 'The small room is filled with chests, most of them empty.'''},
             'dungeon': {'Exits': {'north' : 'laboratory'},'Items': [], 'Enemies': ['shadow wizard'], 'Description': 'A strange purple light '},
             'graveyard': {'Exits': {'south' : 'armoury', 'east' : 'laboratory'},'Items': ['shovel'], 'Enemies': ['zombie', 'zombie', 'zombie'], 'Description': 'The small plot of land is surrounded by a short metal fence, with many tombstones filling the cramped space.\nTwo of the graves seem to have been dug up.'},
             'watch tower': {'Exits': {'north': 'library'}, 'Items': ['blue key','health potion'],'Enemies': [], 'Description': 'The circular stone room is cramped and cold, the wind blowing in from the many arrow slits in the walls.'},
             'laboratory': {'Exits': {'west': 'graveyard','south' : 'dungeon'}, 'Items': ['health potion','gold key'], 'Enemies': ['gargoyle','giant rat'],'Description': 'Large vats of liquid steam in the laboratory, with many strange potions on the shelves.\n'},
             'kitchen': {'Exits': {'south': 'grand hall'}, 'Items': ['bread','knife','cheese'], 'Enemies': ['rat'], 'Description': 'Cobwebs fill every corner and dust is on every surface.\nRodents scurry amount the old shelves where some stale food is kept. '}
             }


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

    def addnpc(self, npc):
        Room.rooms[self.room]['NPC'].append(npc)