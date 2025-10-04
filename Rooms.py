
class Room:
    rooms = {'gate': {'Exits': {'east' : 'maze'}, 'Items': ['grey key'], 'Enemies': ['imp'], 'Description' : 'You stand at the entrance to an ancient castle. Dead plants and trees surround you, and the sky is overcast\nAhead of you is your first obstacle: A large grey gate, with tall stone walls on either sides.', 'NPC' : []},
             'maze': {'Exits': {'north' : 'garden','west' : 'gate'}, 'Items': ['sword'], 'Enemies': [],  'Description' : 'You are in the center of the maze. The skeleton of a man lays on the ground, an old rusting sword still in his hand.', 'NPC' : []},
             'garden': {'Exits': {'north' : 'entrance', 'south' : 'maze'}, 'Items': ['gold coin'], 'Enemies': [],  'Description' : 'You stand in a large garden, with a stone fountain in the center.\nYou see gold coins glistening at the bottom, while strange eel like creatures swim around in the clear blue water.', 'NPC' : []},
             'entrance': {'Exits': {'south' : 'garden', 'east' : 'grand hall', 'west' : 'library'}, 'Items': [],'Enemies': [], 'Description' : '...', 'NPC' : []},
             'grand hall': {'Exits': {'west' : 'entrance', 'north' : 'servants quarters'}, 'Items': ['green key'],'Enemies': [], 'Description' : '...', 'NPC' : []},
             'library': {'Exits': {'south' : 'watch tower', 'east' : 'entrance', 'north' : 'armoury'}, 'Items': ['book','spell book','health potion'],'Enemies': ['ghost'], 'Description' : '...', 'NPC' : []},
             'armoury': {'Exits': {'east' : 'kitchen', 'south' : 'library', 'north' : 'graveyard'}, 'Items': ['chain mail','blue key'],'Enemies': [], 'Description' : '...', 'NPC' : []},
             'kitchen': {'Exits': {'east': 'servants quarters', 'west': 'armoury'},'Items': ['bread'], 'Enemies': ['rat'], 'Description': '...', 'NPC': []},
             'graveyard': {'Exits': {'south' : 'graveyard', 'east' : 'laboratory'},'Items': ['shovel'], 'Enemies': ['zombie', 'zombie', 'zombie'], 'Description': '...', 'NPC': []}
             'watch tower': {'Exits': {'north': 'library'}, 'Items': ['plate armour'],'Enemies': ['suit of armour'], 'Description': '...', 'NPC': []},
             'laboratory': {'Exits': {'west': 'graveyard'}, 'Items': [''], 'Enemies': [],'Description': '...', 'NPC': []}
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

    def getnpcs(self):
        return Room.rooms[self.room]['NPC']

    def look(self):
        print(f'Yuo are at the {self.room}')
        print(f"Description: {Room.rooms[self.room]['Description']}")
        print(f"Exit{('s','')[len(self.getexits()) == 1]} in room: {', '.join(self.getexits())}")
        print(f"Item{('s','')[len(self.getitems()) == 1]} in room: {(', '.join(self.getitems()), 'There are no items')[len(self.getitems()) == 0]}")
        if len(self.getenemies()) > 0:
            print(f"Enem{('ies', 'y')[len(self.getenemies()) == 1]} in room: {', '.join(self.getenemies())}")
        if len(self.getnpcs()) > 0:
            print(f"NPC{('s', '')[len(self.getnpcs()) == 1]} in room: {', '.join(self.getnpcs())}")

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