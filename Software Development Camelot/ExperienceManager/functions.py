import time



from Menu import Menu
from Action import Action,Motion
from InfoTools import Narration,Hint,Dialog
from Items import Items,Weapon
from Character import Character
from Places import Places
from Icon import Icon


class globalVars():
    pass

G = globalVars() #empty object to pass around global state
G.kill = False
G.conversation = False
G.note_read = False
G.magnifying_glass = False
G.ginezin_coin = False
G.Hamlin_Dorothy_dialog_switch = False
G.bandit_appearance = True
G.elmwood_backstory = False
G.Hallwaysequence = True


class MainGamePlay:

    hamlins_note = ""
    ginezin_coin = ""
    magnifying_glass = ""
    sedonia = ""
    hamlin_conversation = ""
    elmwood_back_story =""
    hallway_conversation =""
    go_GLibrary_conversation = False
    castle_warning_conversation =""
    Sedonia_weapon=""
    bandit_appearance = True
    addtolistmagnifyingglass=False
    addtolistcoin=False
    eavesdrop_dialog = ""
    game_language = "en"
        

    def __init__(self):

        self.act = Action()
        self.initialize_places()
        self.initialize_items()
        self.initialize_characters()
        self.initialize_camera()
        self.initialize_soundtrack()
        self.initialize_icons()
    
    def initialize_places(self):

        self.sedonia = Places("Sedonia", "City")
        self.ginezin = Places("Ginezin","City")
        self.sedonia_home = Places("Home","Cottage")
        self.sedonia_bar = Places("Bar","Tavern")
        self.ginezin_library = Places("CityLibrary","Library")
        self.ginezin_storage = Places("Storage","Storage")
        self.elmwood_1 = Places("Elmwood","ForestPath")
        self.elmwood_2 = Places("Elmwood2","ForestPath")
        self.spooky_path = Places("SpookyPath","SpookyPath")
        self.library = Places("G_Library","Library")
    
        
        return True

    def initialize_camera(self):

        self.character_Mirabel.set_camera_focus('follow')

        return True

    def initialize_characters(self):
        
        # self.character_Mirabel = Character("Mirabel","C","Happy","Peasant","Home","6","brown","Gray","Ponytail")
        self.character_Hamlin = Character("Hamlin","F","Sad","Peasant","Sedonia.Barrel","6","Brown","Gray","Mage_Beard","Cry2")
        self.character_Dorothy = Character("Dorothy","G","Neutral","Peasant","Sedonia.Bench","6","Brown","Gray","Straight")
        self.character_Nicholaus = Character("Nicholaus","D","Neutral","Noble","Elmwood.PathBlock","6","Brown","Gray","Long")
        self.character_Bandit_1=Character("Bandit1","H","angry","Bandit","Elmwood2","6","brown","Gray","Short_Full")
        self.character_Bandit_2=Character("Bandit2","H","angry","Bandit","","6","brown","Gray","Short_Full")

        self.character_Mirabel = Character("Mirabel","C","Happy","Peasant","G_Library","6","brown","Gray","Ponytail")

        return True

    def initialize_items(self): 

        self.hamlins_note = Items("HamlinNote", "OpenScroll", "Home.Table","A note written by your father. Sounds urgent.")
        self.ginezin_coin = Items("GinezinCoin", "Coin", "Bar.Shelf", "This is a coin of House Ginezin")
        self.magnifying_glass = Items("MagnifyingGlass", "MagnifyingGlass", "Home.Shelf", "Magnifying glass. Handy when inspecting new things.")        
        self.act.action('EnableIcon("InspectCoin", MagnifyingGlass, GinezinCoin,"Inspect the Coin", True)')

        return True

    def initialize_weapons(self):
        pass

    def initialize_soundtrack(self):

        '''
        Create soundtrack for places where user cannot explicitly create: such as:
        city fountain, furniture etc
        '''

        self.act.action("PlaySound(River,Sedonia.Fountain)")

        return True


    def initialize_icons(self):
        self.act.action('EnableIcon("TalkToHamlin", Talk, Hamlin,"Talk to Hamlin", false)')
        self.act.action('EnableIcon("TalkToDorothy", Talk, Dorothy,"Talk to Dorothy", false)')
        self.act.action('EnableIcon("TalkToNicholaus", Talk, Nicholaus,"Talk to Nicholaus", false)') #Talk to Nicholaus1
        
        #place interactions
        self.act.action('EnableIcon("EnterHome", Exit, Sedonia.BlueHouseDoor,"Enter Home", false)')

        #item interactions
        self.act.action('EnableIcon("ReadScroll", Openscroll, HamlinNote, "Read note", true)')
        self.act.action('EnableIcon("PickUpMagnifyingGlass", Hand, MagnifyingGlass, "Pick up", true)')
        self.act.action('EnableIcon("StashMagnifyingGlass", Chest, MagnifyingGlass, "Stash away", false)')



    def EnemiesOfKingdomSequence(self):
        
        #self.bandits_conversation
        pass

    def PickupMagnifyingGlass(self):
        self.magnifying_glass.pick_up("Mirabel")
        if not self.addtolistmagnifyingglass:
            self.magnifying_glass.add_to_list()
        self.addtolistmagnifyingglass=True
        #self.act.action("ShowList(Mirabel)")

        return True 

    def PickupSedoniaSword(self):
        self.Sedonia_weapon.pick_up("Mirabel")
        self.Sedonia_weapon.add_to_list() 
        self.act.action("ShowList(Mirabel)")
        return True 

    def StashMagnifyingGlass(self):
        self.magnifying_glass.pocket("Mirabel") 
        self.magnifying_glass.add_to_list()
        #self.act.action("ShowList(Mirabel)")    

        return True

    def StashCoin(self):
        self.act.action("Sheathe(Mirabel, MagnifyingGlass)")
        self.ginezin_coin.player_owned = True        

    def PickupCoin(self):
        self.ginezin_coin.pick_up("Mirabel")
        # G.ginezin_coin = True
        if not self.addtolistcoin:
            self.ginezin_coin.add_to_list()       #Inventory Implementation
        self.addtolistcoin=True
        #self.act.action("ShowList(Mirabel)")    

        return True 

    def TransitionElmwoodToSpookyPath(self):

        text_list = [
            "Seems like there is a spooky path ahead"

        ]

        narration = Narration(text_list,"",2)

        narration.display_narration()
        self.character_Mirabel.teleport("SpookyPath.WestEnd")
        self.act.action("HideNarration()")       
        if not self.bandit_appearance:
            self.act.action("SetPosition(Bandit1, SpookyPath.EastEnd)")
            self.act.action("SetPosition(Bandit2, SpookyPath.EastEnd)")

        return True
      
    # TRANSITION FUNCTIONS
    def TransitionSedoniaToElmwood(self):
        self.act.action("SetCameraMode(follow)")
        self.act.action("Exit(Mirabel, Sedonia.NorthEnd, true)")
        self.act.action("SetPosition(Mirabel, Elmwood.WestEnd)")
        self.act.action("FadeIn()")

        return True

    def create_castle_sorrounding(self):
                
        self.castlecrossroad = Places("CastleCrossroads","CastleCrossroads")
        self.castle = Places("Castle","GreatHall")
        self.dungeon = Places("Dungeon","Dungeon")
        self.library = Places("G_Library","Library")
        self.hallway = Places("Hallway","Hallway")
        self.castleguard_One=Character("Guard","F","","HeavyArmour","CastleCrossroads.Gate","","","","")

        return True
        
    def transition_to_dungeon(self):
        self.act.action("FadeOut()")
        self.act.action("SetPosition(Mirabel, Dungeon.DirtPile)")
        self.act.action("FadeIn()")
        text_list = [
                    "You will rotten here..."
                    
                    ]
        self.dungeon = Hint(text_list,"",2) 
        self.act.action("Die(Mirabel)")
        return True

    def transition_to_castlecrossroads(self):
        self.act.action("StopSound()")
        self.act.action("FadeOut()")
        self.act.action("SetPosition(Mirabel, CastleCrossroads.WestEnd)")
        self.act.action("FadeIn()")
        return True
        
    def arrived_city_ginezin(self):
        #self.act.action("PlaySound(Town_Day)")
        text_list = [
                    "Seems like there is a city ahead..."
                    ]

        self.transition_to_ginezin = Hint(text_list,"Town_Day",2)

        self.act.action("FadeOut()")
        self.act.action("Exit(Mirabel, Elmwood2.EastEnd, true)")

        self.act.action("SetPosition(Mirabel, Ginezin.WestEnd)")
        self.act.action("FadeIn()")
        text_list = [
                    "Beware the guard neer the castle!",
                    ]

        self.hint_ginezin = Hint(text_list,"Town_Day",2)
        return True

    def trasition_to_G_library(self):
        if self.go_GLibrary_conversation:
            # self.character_Mirabel.exit_from_to("Ginezin.Fountain","G_Library.Door" )
            self.act.action("FadeOut()")
            self.act.action("SetPosition(Mirabel, G_Library.Door)")
            self.act.action("FadeIn()")
            return True
    
    def G_Library_letter(self):
        self.G_letter = Items("Letter", "OpenScroll", "G_Library.Table","Some info in it!")
        self.act.action('EnableIcon("ReadLetter", Openscroll, Letter, "Read letter", true)')
        return True

    def Hallwaysequence(self):
        
        self.character_Guard1 = Character("Guard1", "F","Neutral","HeavyArmour","Hallway","6","brown","Gray","long") 
        self.character_Guard2 = Character("Guard2", "F","Neutral","HeavyArmour","Hallway","6","brown","Gray","long")
        self.Guard1_weapon = Weapon("GuardSword", "Sword", "Guard1", "Sword.")
        self.Guard2_weapon = Weapon("GuardSword2", "Sword", "Guard2", "Sword.")
        text_list = [
            "Guard1: How did you get in? Come with us",
            "[Listen_to_the_guard1|Surrender] | [Ignore_the_guard1|Fight]"
        ] 

        self.hallway_conversation = Dialog(text_list, left_char="Guard1", right_char="Mirabel", pause_duration=3)
        self.hallway_conversation.display_dialog(player_ends_dialog=True)

        return True

    def MirabelSurrender(self):
        self.act.action("SetCameraFocus(Mirabel)")
        self.character_Mirabel.teleport("Dungeon.DirtPile") 
        #self.act.action("FadeOut()") 
        #self.act.action("SetPosition(Mirabel, Dungeon.DirtPile)")  
        #self.act.action("FadeIn()")

        return True

    def MirabelFight(self):
        self.Guard1_weapon.weapon_attack(self.character_Guard1.character_name, self.character_Mirabel.character_name, hit = "true")
        self.act.action("Die(Mirabel)")

        return True

    def transition_castlecrossroads_to_G(self):
        self.act.action("FadeOut()")
        self.act.action("SetPosition(Mirabel,Ginezin.EastEnd)")
        self.act.action("FadeIn()")
    
    def BanditAttackMirabel(self):
        self.act.action("Attack(Bandit1, Mirabel, true)")
        if self.ginezin_coin.player_owned:
            self.ginezin_coin.take_from("Bandit1", "Mirabel")
        self.act.action("Die(Mirabel)")
        self.act.action("CreateEffect(Mirabel, Death)")

        return True

    def TransitionElmwood1ToElmwood2(self):
        self.act.action("FadeOut()")
        self.act.action("SetPosition(Mirabel, Elmwood2.WestEnd)")

        if self.bandit_appearance:
            self.act.action("SetPosition(Bandit1, Elmwood2.EastEnd)")
            self.act.action("SetPosition(Bandit2, Elmwood2.EastEnd)")   
        else:
            self.act.action("SetPosition(Bandit1, SpookyPath.EastEnd)")
            self.act.action("SetPosition(Bandit2, SpookyPath.EastEnd)")                          
        self.act.action("FadeIn()")    

        return True

    def Elmwood2ToSpookyPath(self):
        self.act.action("SetNarration(""Seems like there is a spooky path ahead"")")
        self.act.action("ShowNarration()")
        time.sleep(2) 
        self.act.action("FadeOut()")
        self.act.action("SetPosition(Mirabel, SpookyPath.WestEnd)")
        self.act.action("FadeIn()")
        self.act.action("HideNarration()")       
        if not self.bandit_appearance:
            self.act.action("SetPosition(Bandit1, SpookyPath.EastEnd)")
            self.act.action("SetPosition(Bandit2, SpookyPath.EastEnd)")

        return True

    def GuardAttackMirabel(self):
        self.act.action("Attack(Guard1, Mirabel, true)") 
        self.act.action("Attack(Guard2,Mibrabel,true)")
        self.act.action("Die(Mirabel)")
        self.act.action("CreateEffect(Mirabel, Death)")

        return True

    def ReturnToSedonia(self):

        text_list = [
            "Oh! Seems like Nicholaus is under attack and he is in danger.",
            "[save Nicholaus|Help Nicholaus !] | [find father|Find father]"
        ]

        self.character_Knight_1=Character("knight1","H","angry","HeavyArmour","Sedonia.BrownHouseDoor","4","brown","black","Short_Full") 
        self.character_Knight_2=Character("knight2","H","angry","HeavyArmour","Sedonia.RedHouseDoor","4","brown","black","Short_Full") 
        self.character_Knight_3=Character("knight3","H","angry","HeavyArmour","Sedonia.EastEnd","4","brown","black","Short_Full")
        self.character_Villager_1=Character("villager1","D","scared","Peasant",'Sedonia.BrownHouseDoor',"7",'brown',"black","Short")
        self.character_Villager_2=Character("villager2","F","scared","Beggar",'Sedonia.RedHouseDoor',"4",'brown',"red","Long")      
        self.act.action("SetPosition(Nicholaus, Sedonia.EastEnd)")
        self.act.action("SetPosition(Hamlin, Sedonia.Alley)")
        self.act.action('EnableIcon("MeetHamlin", Talk, Hamlin,"Meet Hamlin", false)')
        #self.character_Mirabel.exit_from_to("Elmwood.WestEnd","Sedonia.NorthEnd")

        # Nick Attack
        self.Knight_3_weapon = Weapon("Knight3Sword", "Sword", "knight3","Sword.")
        self.Nicholaus_weapon = Weapon("NicholausSword", "Sword", "Nicholaus","Sword.")
        self.act.action("SetCameraFocus(knight3)")
        self.Knight_3_weapon.weapon_attack("knight3", "Nicholaus", "true")
        self.Nicholaus_weapon.weapon_attack("Nicholaus", "knight3", "true")  

        #time.sleep(2)
        self.act.action("SetCameraFocus(Mirabel)")    
        time.sleep(1)
        self.nick_danger_narration = Dialog(text_list, "", "", soundtrack="Ominous",completed = False,pause_duration=2) 
        self.nick_danger_narration.display_dialog(True)
        self.act.action("SetCameraFocus(Mirabel)") 
        return True

    def SaveNicholaus(self):
        text_list = [
            "Look for Sword near any dead soldier"
        ]
        hint = Hint(text_list,"",2)
        self.act.action('CreatePlace(DiningRoom, DiningRoom)')        
        self.act.action('EnableIcon("AttackSoldierToSaveNicholaus",Attack,knight3,"Attack Soldier", false)')
        #self.Sedonia_weapon=Items("SedoniaSword", "Sword", "Sedonia.Bench", "This is Sedonia City Sword.")
        self.character_DeadKnight=Character("deadknight","H","angry","HeavyArmour","Sedonia","4","brown","black","Short_Full")
        self.character_King=Character("king","H","happy","King","DiningRoom.Table","4","brown","black","Short_Full")
        self.Sedonia_weapon = Weapon("deadknightSword", "Sword", "deadknight","Sword.")
        self.act.action("Die(deadknight)") 
        
        
        # self.Sedonia_weapon.take_from("deadknight", "Mirabel")

        #Act.action('EnableIcon("PickUpSedoniaSword", Hand, SedoniaSword, "Pick up", true)')
        return True

    def LetNickolausDie(self):
        self.act.action("SetCameraFocus(knight3)") 
        self.act.action("Attack(knight3,Nicholaus,true)")
        self.act.action("Die(Nicholaus)")
        self.act.action("SetCameraFocus(Mirabel)")
        self.act.action("SetCameraMode(follow)")
        self.act.action('CreatePlace(DiningRoom, DiningRoom)') 
        self.character_King=Character("king","H","happy","King","DiningRoom.Table","4","brown","black","Short_Full")
        self.character_Spokeperson=Character("scribe","D","scared","Peasant",'Sedonia',"7",'brown',"black","Short")
        #self.character_Villager_4=Character("villager4","F","scared","Beggar",'DiningRoom',"4",'brown',"red","Long")                
        return True
    
    def KingAnnouncment(self):

        text_list = [
            "I am happy to have you all here today.",
            "I have some important announcements to make today.",
            "As my son Nicholaus has been saved by Hamlin and her daughter Mirabel",
            "I appoint Hamlin as my Lord to one of the House",
            "I hope you all enjoy your time here today",
            "Please serve yourself with some drinks!",
            "Thank you all once again"

        ]

        self.act.action("SetCameraFocus(Sedonia.BrownHouseDoor)") 
        self.act.action("WalkTo(knight1, Sedonia.GreenHouseDoor)")
        self.act.action('SetPosition(knight2, SpookyPath.WestEnd)')  
        self.act.action('SetPosition(knight3, SpookyPath.Well)')  
        self.act.action("SetCameraFocus(villager1)")
        self.act.action("DanceTogether(villager1,villager2)")
        self.act.action("Clap(villager1)")
        self.act.action("Clap(villager2)")
        
        self.act.action('SetPosition(villager1, DiningRoom)')  
        self.act.action('SetPosition(villager2, DiningRoom)')          
        self.act.action("Sit(villager1, DiningRoom.RightChair)")
        
        self.act.action("Sit(villager2, DiningRoom.BackRightChair)")        
        self.act.action('SetPosition(Hamlin, DiningRoom)') 
        self.act.action('SetPosition(Mirabel, DiningRoom)')         
        
        self.act.action("Sit(Hamlin, DiningRoom.BackLeftChair)")
        self.act.action("Sit(Mirabel, DiningRoom.FrontRightChair)") 
        
        self.act.action("FadeOut()")
        self.act.action("FadeIn()")
        
        self.act.action("SetCameraFocus(DiningRoom.DiningTable)")
        time.sleep(2)
        
        self.king_narration = Dialog(text_list, "king", "", soundtrack="Ominous",completed = False,pause_duration=2) 
        self.king_narration.display_dialog(False)        
        
        self.glass = Items("Glass", "Cup", "DiningRoom.DiningTable", "Glass")
        self.king_glass = Items("KingGlass", "GoldCup", "DiningRoom.Table", "Glass")
        self.king_glass.pick_up("king")
        self.act.action("Pickup(Mirabel,Glass)")
        #self.glass.pick_up("Hamlin")
        #self.glass.pick_up("villager1")
        #self.glass.pick_up("villager2")
        self.act.action("Pickup(Hamlin,Glass)")
        self.act.action("Pickup(villager1,Glass)")
        self.act.action("Pickup(villager2,Glass)")
        self.act.action("Drink(king)")
        self.act.action("Drink(Mirabel)")
        self.act.action("Drink(Hamlin)")
        self.act.action("Drink(villager1)")
        self.act.action("Drink(villager2)")
        


        return True

    def KingSpokesPersonAnnouncement(self):
        
        text_list = [
            "I am Spokeperson of the King",
            "King recently got the news that Nicholaus has been killed by soldiers.",
            "Actually Nicholaus was the prince and son of the King.",
            "Now the King is very angry with you that you let his son die"
        ]        
        
        self.act.action("SetCameraFocus(scribe)") 
        self.act.action("WalkTo(scribe, Sedonia.Alley)")
        
        self.spokeperson_narration = Dialog(text_list, "scribe", "", soundtrack="Ominous",completed = False,pause_duration=2) 
        self.spokeperson_narration.display_dialog(False)  

        self.act.action("SetCameraFocus(Mirabel)")
        self.act.action("SetCameraMode(follow)") 

        return True

    def TakeSword(self):
        
        #self.ginezin_coin = Items("deadknightSword", "Sword", "deadknight", "This is a coin of House Ginezin")
        self.Sedonia_weapon.take_from("Mirabel","deadknight")
        self.Sedonia_weapon.pocket("Mirabel") 
        #self.act.action("Take(deadknight,Sword)")

    def AttackSoldierToSaveNicholaus(self):
        text_list = [
            "Nicholaus: Thank you Mira for helping me and saving my life.",
            "Nicholaus: You seem a bit worried. Is everything ok?",
            "Mirabel: Actually I am looking for my father",
            "Nichlous: Oh I can help you find your father. I will go search him North of city. You can go check East side of the city",
            #"[EndDialog|Exit]"
        ]        
        #self.act.action("Attack(Mirabel,knight3,true)")
        self.Sedonia_weapon.weapon_attack("Mirabel","knight3","true")
        self.act.action("Die(knight3)")
        self.nick_saved_narration = Dialog(text_list, "Mirabel", "Nicholaus", soundtrack="Ominous",completed = False,pause_duration=2) 
        self.nick_saved_narration.display_dialog(False)  
        self.act.action("SetCameraMode(track)")  
        self.act.action("WalkTo(Nicholaus, Sedonia.NorthEnd)")
        self.act.action("FadeOut()")
        self.act.action('SetCameraFocus(Mirabel)')
        self.act.action("SetCameraMode(follow)")
        self.act.action("FadeIn()")

        return True

    def transition_from_Library_to_Hallway(self):
        self.act.action("StopSound()")
        self.act.action("FadeOut()")
        self.act.action("SetPosition(Mirabel, Hallway.Door)")
        self.act.action("FadeIn()")

        return True

    def transition_from_Hallway_to_Library(self):
        self.act.action("StopSound()")
        self.act.action("FadeOut()")
        self.act.action("SetPosition(Mirabel, Library.Door)")
        self.act.action("FadeIn()")

        return True

    def PlayerAppearanceChoice(self):
        
        gamecontrol_text = [
                       "Game Controls for the player",
                       "Press 'I' to display inventory and select items from inventory",
                       "Press 'E' to display in game menu"
                        ]

        narration_text = [
                        "Choose your character appearance",
                       "[changetoBandit|Bandit] | [changetopeasant|Peasant]"
                        ]

        self.opening_narration = Narration(gamecontrol_text, "Kingdom", 3)
        self.opening_narration.display_narration()

        self.king_narration = Dialog(narration_text, "", "", soundtrack="Ominous",completed = False,pause_duration=2) 
        self.king_narration.display_dialog(True,False) 
        return True        
#End MainGamePlay Class