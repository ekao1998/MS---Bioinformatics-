# from HintTexts import HintTexts
from InfoTools import Dialog,Hint

class Menu:

    def __init__(self,options,actions,M,H) -> None:
        self.options=options
        self.actions=actions
        self.M = M
        self.H = H

    def set_menu(self):
        pass

    def get_menu(self):
        menu_options = list(zip(self.options, self.actions))
        return menu_options

    def show_menu(self):

        options_text = []
        menu_options = self.get_menu()

        for x in menu_options:
            option = "[" +str(x[1]) +"|" +str(x[0])+ "]"
            options_text.append(option)

        return options_text
    
    def map_options_functions(self):

        option_functions = {}
        menu_options = self.get_menu()
        
        for x in menu_options:
            option_functions[x[1]] = x[1]

        return option_functions

    def ChangeCharacterClothing(self,Appearance):
        self.M.act.action("SetClothing(Mirabel,"+Appearance+")")
        self.M.act.action("HideDialog()")
        self.M.act.action("EnableInput()")
        return True

    def MenuShowHint(self):

        current_location = self.M.character_Mirabel.current_location

        places_list = [

            "Sedonia","Ginezin","Home","Bar","CityLibrary","Storage","Elmwood2","Elmwood",\
                "SpookyPath","CastleCrossroads","Castle","Dungeon","G_Library","Hallway"
        ]

        # if current_location != "":

        for x in places_list:

            if x.lower() in current_location.lower():
                hints = self.H.get_specific_class(hint_class = x.lower())

                if len(hints) > 0:
                    self.M.act.action("HideDialog()")
                    for hint in hints:
                        hintt = Hint(hint,"",3)

                    break


                else:
                    self.M.act.action("HideDialog()")
                    nothing_to_show = Hint(["Sorry no hints here"],"",2)
                    self.M.act.action("EnableInput()")
                    break


    
            else:
                self.M.act.action("HideDialog()")
                nothing_to_show = Hint(["Sorry no hints here"],"",2)
                self.M.act.action("EnableInput()")
                break
                
        return True
        
    def MenuChangeAppearance(self):
        narration_text = [
                "Choose your character appearance",
                "[changetoBandit|Bandit] | [changetopeasant|Peasant]"
        ]
        self.M.change_clothing = Dialog(narration_text, "", "", soundtrack="",completed = False,pause_duration=2) 
        self.M.change_clothing.display_dialog(True,False)

        return True
    
    def MenuChangeLanguage(self):

        narration_text = [
                "Choose your clan peasant",
                "[changetoEnglish|English] | [changetoSwahili|Kiswahili]"
        ]
        self.M.change_language = Dialog(narration_text, "", "", soundtrack="",completed = False,pause_duration=2) 
        self.M.change_language.display_dialog(True, False)
        return True
    
    def ChangeLanguage(self,game_language):
        self.M.game_language = game_language
        self.M.act.action("HideDialog()")
        self.M.act.action("EnableInput()")
        return True

        
    def open_menu(self):

        options_text = self.show_menu()
        options_text.insert(0, "Menu Options:")

        self.M.menu_dialog = Dialog(options_text,"","","",False,0)
        self.M.menu_dialog.display_dialog(player_ends_dialog=True,clear_each_line=False)

        return True

