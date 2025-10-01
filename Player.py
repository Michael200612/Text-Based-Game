
class Player:
    def __init__(self, playername, playeritems):
        self.playername = playername
        self.playeritems = playeritems

    def getplayername(self):
        return self.playername

    def takeitem(self, item):
        self.playeritems.append(item)

    def inventory(self):
        print(self.playeritems)
