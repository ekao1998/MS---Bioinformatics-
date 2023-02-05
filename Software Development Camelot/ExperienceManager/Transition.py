from InfoTools import Narration
from Action import Action
from InfoTools import Narration,Hint,Dialog
from Items import Items,Weapon
from Character import Character
from Places import Places


import time

class Transition:

    def __init__(self, M):
        self.M = M

    def TransitionElmwoodToSpookyPath(self):

        text_list = [
            "Seems like there is a spooky path ahead"

        ]

        narration = Narration(text_list,"",2)

        narration.display_narration()
        self.M.act.action("FadeOut()")
        self.M.act.action("SetPosition(Mirabel, SpookyPath.WestEnd)")
        self.M.act.action("FadeIn()")
        self.M.act.action("HideNarration()")
         
        if not self.M.bandit_appearance:
            self.M.act.action("SetPosition(Bandit1, SpookyPath.EastEnd)")
            self.M.act.action("SetPosition(Bandit2, SpookyPath.EastEnd)")

        return True
      

    def TransitionSedoniaToElmwood(self):
        #self.M.act.action("SetCameraMode(follow)")
        self.M.act.action("Exit(Mirabel, Sedonia.NorthEnd, true)")
        self.M.act.action("SetPosition(Mirabel, Elmwood.WestEnd)")
        self.M.act.action("FadeIn()")      
    

    def transition_to_dungeon(self):
        self.M.act.action("FadeOut()")
        self.M.act.action("SetPosition(Mirabel, Dungeon.DirtPile)")
        self.M.act.action("FadeIn()")
        text_list = [
                    "You will rotten here..."
                    
                    ]
        self.dungeon = Hint(text_list,"",2) 
        self.M.act.action("Die(Mirabel)")
        return True

    def transition_to_castlecrossroads(self):
        self.M.act.action("StopSound()")
        self.M.act.action("FadeOut()")
        self.M.act.action("SetPosition(Mirabel, CastleCrossroads.WestEnd)")
        self.M.act.action("FadeIn()")
        return True

    def transition_castlecrossroads_to_G(self):
        self.M.act.action("FadeOut()")
        self.M.act.action("SetPosition(Mirabel,Ginezin.EastEnd)")
        self.M.act.action("FadeIn()")        


    def TransitionElmwood1ToElmwood2(self):
        self.M.act.action("FadeOut()")
        self.M.act.action("SetPosition(Mirabel, Elmwood2.WestEnd)")

        if self.M.bandit_appearance:
            self.M.act.action("SetPosition(Bandit1, Elmwood2.EastEnd)")
            self.M.act.action("SetPosition(Bandit2, Elmwood2.EastEnd)")   
        else:
            self.M.act.action("SetPosition(Bandit1, SpookyPath.EastEnd)")
            self.M.act.action("SetPosition(Bandit2, SpookyPath.EastEnd)")                          
        self.M.act.action("FadeIn()")    

        return True


    def transition_from_Library_to_Hallway(self):
        self.M.act.action("StopSound()")
        self.M.act.action("FadeOut()")
        self.M.act.action("SetPosition(Mirabel, Hallway.Door)")
        self.M.act.action("FadeIn()")

        return True

    def transition_from_Hallway_to_Library(self):
        self.M.act.action("StopSound()")
        self.M.act.action("FadeOut()")
        self.M.act.action("SetPosition(Mirabel, Library.Door)")
        self.M.act.action("FadeIn()")

        return True

    def ElmwoodWestEndToElmwoodEastEnd(self):
        self.M.character_Mirabel.exit_from_to("Elmwood2.WestEnd","Elmwood.EastEnd")

        # Act.action("FadeOut()")
        # Act.action("SetPosition(Mirabel, Elmwood.EastEnd)")
        # Act.action("FadeIn()")
        return True

    def SpookyPathWestEndToElmwood2Plant(self):
        self.M.character_Mirabel.exit_from_to("SpookyPath.WestEnd","Elmwood2.Plant")
        return True       

    def SpookyPathEastEndToGinezinNorthEnd(self):
        self.M.character_Mirabel.exit_from_to("SpookyPath.EastEnd","Ginezin.NorthEnd")
        return True           

    def GinezinWestEndToElmwood2EastEnd(self):
        self.M.character_Mirabel.exit_from_to("Ginezin.WestEnd","Elmwood2.EastEnd")
        return True   

