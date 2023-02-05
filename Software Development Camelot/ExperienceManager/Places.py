from Action import Action

class Places:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.act = Action()

        self.create()


    def create(self):
        self.act.action("CreatePlace("+self.name+","+self.type+")")
        return True


class Furniture(Places):
    def __init__(self,name,location,visible,opened):
        super().__init__(name,type)
        self.visible = visible
        self.opened = opened
        self.location = location
        self.act = Action()
        
    def create(self):
        pass

    def hide(self):
        #HideFurniture(Market.Stall)
        self.act.action("HideFurniture("+self.location+"."+self.name+")")
        self.visible = False
        return True
    
    def reveal(self):
        self.act.action("ShowFurniture("+self.location+"."+self.name+")")
        self.visible = True
        return True

    def open(self, character_name):
        #OpenFurniture(Tom, Camp.Chest)
        self.act.action("OpenFurniture("+character_name+", "+self.location+"."+self.name+")")
        self.opened=True
        return True


    def close(self, character_name):
        self.act.action("CloseFurniture("+character_name+", "+self.location+"."+self.name+")")
        self.opened=False
        return True


class Scene():
    def __init__(self,playerName,exitPoints):
        self.playerName = playerName
        self.exitPoints = exitPoints
        self.act = Action()

    def exit(self):
        self.act.action("Exit("+self.playerName+", "+self.exitPoints+")")
        return True

    def enter(self):
        self.act.action("SetPosition("+self.playerName+", "+self.exitPoints+")")
        self.act.action("FadeIn()")
        return True

if __name__ == '__main__':
    ginezin_library = Places("GinezinLibrary","Library")
    ginezin_library.name
    libray_chest = Furniture("Chest",ginezin_library.name,True,False)
    libray_chest.open("Mirabel")
    libray_chest.opened
