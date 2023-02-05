from Action import Action
from InfoTools import Narration,Hint,Dialog
from Items import Items,Weapon,Potion
from Character import Character
from Places import Places

import time

class Sequences:

    def __init__(self,M,D):
        self.M = M
        self.D = D

        # self.act = Action()
        
    def ReadRollSequence(self):

        text_list = self.D.get_text(conversation_label="hamlin_roll")

        self.M.readroll_conversation = Dialog(text_list, left_char="Hamlin",right_char="Mirabel", pause_duration=3)
        self.M.readroll_conversation.display_dialog(True)
        self.M.act.action('EnableIcon("LeaveHome", Exit, Home.Door,"Go to city", False)')

        return True

    def TalkToHamlinSequence(self):

        text_list = self.D.get_text("initial_hamlin_conversation")

        self.M.hamlin_conversation = Dialog(text_list, left_char="Hamlin", right_char="Mirabel",pause_duration=3,soundtrack="Cry2")
        self.M.hamlin_conversation.display_dialog(True)

        return True

    def TalkToDorothy(self):

        if self.M.hamlin_conversation == "" or not self.M.hamlin_conversation.completed:

            text_list = self.D.get_text("initial_dorothy_conversation_1")

            self.M.dorothy_conversation = Dialog(text_list, left_char="Dorothy", right_char="Mirabel",pause_duration=3,soundtrack="Cry2")
            self.M.dorothy_conversation.display_dialog(player_ends_dialog=True)

        else: 
            text_list = self.D.get_text("initial_dorothy_conversation_2")

            self.M.dorothy_conversation = Dialog(text_list, left_char="Dorothy", right_char="Mirabel",pause_duration=3,soundtrack="Cry2")
            self.M.dorothy_conversation.display_dialog(player_ends_dialog=True)

        return True

    def InsultsDorothy(self):

        text_list = self.D.get_text("insult_dorothy")

        self.M.insult_dorothy_conversation = Dialog(text_list, left_char="Dorothy", right_char="Mirabel",pause_duration=3)
        self.M.insult_dorothy_conversation.display_dialog(player_ends_dialog=True)

        self.M.act.action('EnableIcon("EnterCityLibrary", Exit, Sedonia.BrownHouseDoor,"Enter CityLibrary",true)')
        self.M.act.action('EnableIcon("EnterBar", Exit, Sedonia.RedHouseDoor,"Enter Tavern", true)')
        self.M.act.action('EnableIcon("EnterStorage", Exit, Sedonia.GreenHouseDoor,"Enter Storage", true)')
        self.M.act.action('EnableIcon("LeaveCityLibrary", Exit, CityLibrary.Door,"Go to city", true)')
        self.M.act.action('EnableIcon("LeaveBar", Exit, Bar.Door,"Go to city", false)')
        self.M.act.action('EnableIcon("LeaveStorage", Exit, Storage.Door,"Go to city", false)')
        self.M.act.action('EnableIcon("InspectCoin", MagnifyingGlass, GinezinCoin,"Inspect the Coin", true)')
        self.M.act.action("EnableInput()")

        return True

    def PraisesDorothy(self):

        text_list = self.D.get_text("praise_dorothy")

        self.M.praise_dorothy_conversation = Dialog(text_list, left_char="Dorothy", right_char="Mirabel", pause_duration=3)
        self.M.praise_dorothy_conversation.display_dialog(False)
        self.M.act.action('EnableIcon("InspectCoin", MagnifyingGlass, GinezinCoin,"Inspect the Coin", true)')
        self.M.act.action('EnableIcon("EnterBar", Exit, Sedonia.RedHouseDoor,"Enter Tavern", true)')
        self.M.act.action('EnableIcon("LeaveBar", Exit, Bar.Door,"Go to city", false)')

        self.M.act.action("EnableInput()")

        return True

    def ElmwoodBackstory(self):

        text_list = self.D.get_text("elmwood_backstory")
        self.M.act.action("FadeOut()")

        self.M.mousebeater_place = Places("MousebeatersPlace","AlchemyShop")
        self.M.mousebeater = Character("Mousebeater", "G", "","Witch",self.M.mousebeater_place.name+".Table","","","Gray","Long")

        self.M.act.action("PlaySound(Ominous)")

        self.M.PoisonPotion = Items("PoisonPotion", "RedPotion", "MousebeatersPlace","Deadly poison. Kills.") #instance of item for now, change to potion when implemented
        self.M.PoisonPotion2 = Potion("PoisonPotion2", "PurplePotion", "Mousebeater","Not so deadly potion. Resurrects drinker if they die.","Purple","resurrects",vfx="Brew")

        self.M.elmwood_back_story = Dialog(text_list, "", "", soundtrack="Ominous",completed = False,pause_duration=2)

        self.M.act.action("SetCameraFocus(MousebeatersPlace.Table)")


        # action("SetCameraMode(track)")


        self.M.elmwood_back_story.display_partial_dialog(0,1)

        #sequence
        self.M.act.action("FadeIn()")
        time.sleep(3)
        self.M.act.action("WalkTo(Mousebeater, MousebeatersPlace.Cauldron)")
        self.M.PoisonPotion2.place_at(self.M.mousebeater.character_name,self.M.mousebeater_place.name+'.Cauldron', effect="Brew")
        # self.M.act.action("Put(Mousebeater,"+self.M.PoisonPotion.name+",MousebeatersPlace.Cauldron)")
        # self.M.act.action("CreateEffect(MousebeatersPlace.Cauldron,Brew)")
        time.sleep(2)

        self.M.elmwood_back_story.display_partial_dialog(1, 3)
        self.M.knight_One=Character("Knight1","G","","HeavyArmour","MousebeatersPlace","","","","")
        self.M.soldier_One=Character("Soldier1","G","","LightArmour","MousebeatersPlace.Door","","","","")
        self.M.act.action("LookAt(Soldier1, Mousebeater)")

        self.M.witch_slayer = Weapon("TheWitchSlayer", "Sword", "Knight1","So many witches and mages have been slain by this sword.")
        self.M.act.action("SetCameraFocus(MousebeatersPlace.Door)")
        self.M.witch_slayer.weapon_attack("Knight1", "Mousebeater", "true")

        # self.M.act.action("Attack(Knight1, Mousebeater, true)")
        self.M.act.action("Die(Mousebeater)")

        self.M.elmwood_back_story.display_partial_dialog(3,5)
        self.M.act.action("SetCameraFocus(MousebeatersPlace.Table)")
        time.sleep(2)
        self.M.act.action("CreateEffect(Mousebeater,Resurrection)")
        self.M.act.action("Revive(Mousebeater)")

        self.M.witch_slayer.weapon_attack("Knight1", "Mousebeater", "false")

        # Second scene
        self.M.elmwood_3 = Places("Elmwood3","ForestPath")
        self.M.mousebeater.teleport(self.M.elmwood_3.name + ".EastEnd", effect="Poof", fade_out=False,fade_in=False)
        self.M.character_Beggar1=Character("Beggar1","F","","Beggar","Elmwood3.Plant","","","","")
        time.sleep(2)
        self.M.act.action("SetCameraFocus(Elmwood3.Well)")
        self.M.act.action("SetCameraMode(track)")
        self.M.elmwood_back_story.display_partial_dialog(5,7)
        self.M.mousebeater.teleport(self.M.elmwood_3.name + ".Well", effect="Poof", fade_out=False,fade_in=False)

        self.M.act.action("PlaySound(EvilLaugh1)")
        self.M.act.action("CreateEffect(Beggar1, Death)")
        self.M.act.action("Die(Beggar1)")
        self.M.PoisonPotion.place_at(self.M.mousebeater.character_name, self.M.character_Beggar1.character_name, effect="Resurrection")
        self.M.act.action("Revive(Beggar1)")

        self.M.elmwood_back_story.display_partial_dialog(7,8)

        self.M.character_Beggar1.teleport(self.M.mousebeater_place.name, effect="Poof",  fade_out=False,fade_in=False)
        self.M.mousebeater.teleport(self.M.mousebeater_place.name, effect="Poof", fade_out=False,fade_in=False)

        self.M.act.action("StopSound(Ominous)")
        self.M.character_Mirabel.set_camera_focus('follow')
        self.M.act.action("SetCameraFocus(Mirabel)")

        return True

    def WarnPlayer(self):

        # text_list = self.D.get_text("warn")
        # text_list = self.M.H.get_text("sedonia_1")
        # elmwood_warning = Hint(text_list,"",2) #pass vars: text-> list, soundtrack-> string, pause_duration->integer

        if self.M.elmwood_back_story =="" or not self.elmwood_back_story.completed:
            self.ElmwoodBackstory()

        return True
   
    def TalkToNicholaus(self):  #Talk to Nicholaus function added

        text_list = self.D.get_text("nicholaus_initial_conversation")

        self.M.talk_to_nicholaus_conversation = Dialog(text_list, left_char="Nicholaus", right_char="Mirabel", pause_duration=3)
        self.M.talk_to_nicholaus_conversation.display_dialog(player_ends_dialog=True)
        
        self.M.act.action('EnableIcon("TalkToNicholaus2", Talk, Nicholaus,"Talk to Nicholaus2", False)')
        self.M.act.action('DisableIcon("TalkToNicholaus", Nicholaus)')

        return True

    def TalkToNicholaus2(self):

        text_list = self.D.get_text("nicholaus_second_conversation")

        self.M.talk_to_nicholaus2_conversation = Dialog(text_list, left_char="Nicholaus", right_char="Mirabel", pause_duration=3)
        self.M.talk_to_nicholaus2_conversation.display_dialog(player_ends_dialog=False)
        
        return True

    def SecretPassageWaySequence(self):

        text_list = self.D.get_text("secret_passage_spellbook")
        self.M.spellbook_narration = Narration(text_list, "",3)
        self.M.spellbook_narration.display_narration()

        prompt_text = self.D.get_text("hail_help_prompt")
        self.M.spellbook_prompt = Dialog(prompt_text,"",self.M.character_Mirabel.character_name, "",completed=False,pause_duration= 0)
        self.M.spellbook_prompt.display_dialog(player_ends_dialog=True,clear_each_line=False)

        return True

    def WitchDialogSequence(self):
        self.M.act.action("CreateEffect(G_Library.Bookcase4,Poof)")
        self.M.benign_witch = Character("Witch1","C","Happy","Witch","G_Library.Bookcase4","","","Black","Long","")
        self.M.act.action("EnableEffect("+self.M.benign_witch.character_name+", Aura)")
        self.M.character_Mirabel.set_expression("Surprised")
        text_list = self.D.get_text("spellbook_riddle_prompt")
        self.M.riddle_prompt = Dialog(text_list, self.M.benign_witch.character_name, self.M.character_Mirabel.character_name, "", pause_duration=3)
        self.M.riddle_prompt.display_dialog(player_ends_dialog=True)
        
        return True

    def WitchAgreeRiddle(self):
        text_list = self.D.get_text("agree_riddle")
        self.M.riddle_attempt = Dialog(text_list, self.M.benign_witch.character_name, self.M.character_Mirabel.character_name, "", pause_duration=3)
        self.M.riddle_attempt.display_dialog(player_ends_dialog=True,clear_each_line=False)

        return True

    def WitchRefuseRiddle(self):
        self.M.act.action("HideDialog()")
        text_list = self.D.get_text("refuse_riddle")
        self.M.reveal_theft = Dialog(text_list, self.M.benign_witch.character_name, self.M.character_Mirabel.character_name, "", pause_duration=3)
        self.M.reveal_theft.display_dialog(player_ends_dialog=False)
        self.WitchRevealLetter()
        time.sleep(3)
        self.M.character_Mirabel.teleport(self.M.ginezin.name,"Poof")
        self.M.character_Mirabel.set_camera_focus("Follow")
        return True

    def WitchRevealLetter(self):
        self.M.act.action("HideDialog()")
        text_list = self.D.get_text("reveal_thief")
        self.M.reveal_theft = Dialog(text_list, self.M.benign_witch.character_name, self.M.character_Mirabel.character_name, "", pause_duration=3)
        self.M.reveal_theft.display_dialog(player_ends_dialog=False)
        self.M.covingtomb_coin = Items("CovingtombCoin", "Coin", self.M.benign_witch.character_name,"This is CovingTomb Coin")
        self.M.covingtomb_coin.give_to(self.M.benign_witch.character_name,self.M.character_Mirabel.character_name)
        self.M.covingtomb_coin.add_to_list()
        self.M.king_letter = Items("KingLetter", "Scroll", self.M.benign_witch.character_name, "The Kings letter!")
        self.M.king_letter.give_to(self.M.benign_witch.character_name,self.M.character_Mirabel.character_name)
        self.M.king_letter.add_to_list()
        return True

    def WitchSolveRiddle(self):
        self.M.act.action("HideDialog()")
        text_list = self.D.get_text("solved_riddle")
        self.M.solve_riddle_dialog = Dialog(text_list, self.M.benign_witch.character_name, self.M.character_Mirabel.character_name, "", pause_duration=3)
        self.M.solve_riddle_dialog.display_dialog(player_ends_dialog=False)
        self.WitchRevealLetter()
        time.sleep(3)
        self.M.character_Mirabel.teleport(self.M.sedonia.name,"Poof")
        self.M.act.action("EnableInput()")
        return True

    def WitchFailRiddle(self):

        self.M.act.action("HideDialog()")
        text_list = self.D.get_text("secret_passage_spellbook")
        self.M.fail_riddle_dialog = Dialog(text_list, self.M.benign_witch.character_name, self.M.character_Mirabel.character_name, "", pause_duration=3)
        self.M.fail_riddle_dialog.display_dialog(player_ends_dialog=False)
        self.WitchRevealLetter()
        self.M.character_Mirabel.teleport(self.M.ginezin.name,"Poof")
        self.M.act.action("EnableInput()")

        return True

    def startNarration(self):

        narration_text =  self.D.get_text("start_narration")
        self.opening_narration = Narration(narration_text, "Kingdom", 3)
        self.opening_narration.display_narration()

        return True

    def finalNarration(self):

        narration_text =  self.D.get_text("ginezin_narration")
        self.closing_narration = Narration(narration_text, "Danger1", 2)
        self.closing_narration.display_narration()

        return True

    def BanditsEavesdropSequence(self):    
        text_list = self.D.get_text("spooky_hint")
        hint = Hint(text_list,"",2)
        options_text = self.D.get_text("prompt_eavesdrop_bandits")
        eavedrop_prompt = Dialog(options_text,"","Mirabel","",False,2)
        eavedrop_prompt.display_dialog(True)
        return True
    
    def BanditEavesdropDialog(self):
        text_list = self.D.get_text("bandits_eavesdrop_dialog")
        self.M.eavesdrop_dialog = Dialog(text_list, self.M.character_Bandit_1.character_name, self.M.character_Bandit_2.character_name, pause_duration=3)
        self.M.eavesdrop_dialog.display_dialog(player_ends_dialog=False)
        return True

    def InspectCoin(self):
        text_list = self.D.get_text("inspect_coin_dialog")
        dialog = Dialog(text_list, self.M.character_Mirabel.character_name, "", pause_duration=3)
        self.M.act.action("HideDialog()")
        self.M.act.action('EnableIcon("PickUpCoin", Hand, GinezinCoin, "Pick up", true)') # Pickup coin icon appears after inspection
        self.finalNarration()
        self.M.ginezin_coin.player_owned = True

        return True

    def TakeNicholausHelp(self):

        self.M.act.action("HideDialog()")
        self.M.act.action("SetCameraMode(track)") 
        self.M.act.action("WalkTo(Nicholaus, Elmwood.EastEnd)")
        self.M.act.action("FadeOut()")
        self.M.act.action('SetCameraFocus(Mirabel)')
        self.M.act.action("SetCameraMode(follow)")
        self.M.act.action("SetPosition(Nicholaus, Elmwood2.WestEnd)")
        self.M.act.action("FadeIn()") 

        self.M.bandit_appearance=False

        return True

    def castle_warning(self):
        text_list = self.D.get_text("castle_warning")        
        self.M.castle_warning_conversation = Dialog(text_list, left_char="Guard", right_char="Mirabel", pause_duration=3)
        self.M.castle_warning_conversation.display_dialog(player_ends_dialog=True)
        self.M.go_GLibrary_conversation = True
        return True

    def G_Letter_content(self):
        text_list = self.D.get_text("ginezin_letter")
        self.readLetter_conversation = Dialog(text_list, left_char="null",right_char="Mirabel", pause_duration=3)
        self.readLetter_conversation.display_dialog(player_ends_dialog=True)
        return True 
