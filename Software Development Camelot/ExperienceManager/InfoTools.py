from Action import Action
import time

class InfoTools:
    def __init__(self, text_list,soundtrack):
        self.text_list = text_list
        self.act = Action()
        self.soundtrack = soundtrack

    def show(self):
        pass

    def set(self):
        pass

    def hide(self):
        pass

    def play_soundtrack(self):
        
        if self.soundtrack != "":
            self.act.action("PlaySound("+self.soundtrack +")")
            time.sleep(3)
            self.act.action("StopSound("+self.soundtrack +")")

        return True

class Dialog(InfoTools):

    def __init__(self, text_list, left_char, right_char,soundtrack ="",completed=False,pause_duration=0):
        super().__init__(text_list,soundtrack)
        self.left_char = left_char
        self.right_char = right_char
        self.completed = completed
        self.pause_duration = pause_duration
        self.set_left_char()
        self.set_right_char()
        # self.play_soundtrack()

    def set_left_char(self):

        if self.left_char!="":
            self.act.action("SetLeft("+self.left_char+")")

        return True

    def set_right_char(self):

        if self.right_char!="":
            self.act.action("SetRight("+self.right_char+")")

        return True

    def display_partial_dialog(self, start, end, player_ends_dialog=False,clear_each_line=True):
        
        self.act.action("ShowDialog()")

        for x in range(start, end):
            self.act.action("SetDialog(" + self.text_list[x] + ")")

            if clear_each_line:
                self.pause_dialog()

        if not player_ends_dialog:
            self.act.action("HideDialog()")


        if end == len(self.text_list):
            self.completed = True

        return True

    def display_dialog(self,player_ends_dialog=False,clear_each_line=True):

        self.act.action("ShowDialog()")

        for x in range(0, len(self.text_list)):
            
            self.act.action("SetDialog(" + self.text_list[x] + ")")

            if x != (len(self.text_list) -1) and clear_each_line:
                self.pause_dialog()

        if not player_ends_dialog:
            self.act.action("ClearDialog()") 
            self.act.action("HideDialog()") 

        self.completed = True

        return True

    def pause_dialog(self):
        if self.pause_duration > 0:
            time.sleep(self.pause_duration)
            self.act.action("ClearDialog()")         
        return True


class Narration(InfoTools):

    def __init__(self, text_list, soundtrack ="",pause_duration=0):
        super().__init__(text_list,soundtrack)
        self.pause_duration = pause_duration

    def display_narration(self):

        self.play_soundtrack()

        self.act.action("ShowNarration()")

        for ind, val in enumerate(self.text_list):
            self.act.action("SetNarration(" + val + ")")
            self.pause_narration()

        self.act.action('HideNarration()')
        self.act.action("StopSound()")

        return True

    def pause_narration(self):
        print(self.pause_duration)
        if self.pause_duration > 0:
            time.sleep(self.pause_duration)
        return True

class Hint(Narration):

    def __init__(self, text_list, soundtrack, pause_duration):
        super().__init__(text_list, soundtrack, pause_duration)
        self.display_narration()

    def display_narration(self):
        self.play_soundtrack()
        self.act.action("ShowNarration()")

        for ind, val in enumerate(self.text_list):
            self.act.action("SetNarration(" + val + ")")
            self.pause_narration()

        self.act.action('HideNarration()')

        return True

    def get_hint(self,player_location):
        
        return

if __name__ == "__main__":
    h = Hint(["Hi", "No"], "", 4)
    # h.display_narration()
   
    text_list = [

            "Mirabel: Dad! What's wrong? You seem quite worried",
            "Hamlin: Oh honey! The king will have my head on a pike for this! Yes he will! What shall I do?",
            "Mirabel: What happened?",
            "Hamlin: Oh the most unspeakable happened! I lost a cherished gift from the king that he gave me many seasons back and a very confidential letter he gave me the other day.",
            "Mirabel: The King sends you letters and gifts?",
            "Hamlin: Yes. Yes! he's an old friend. An old friend who is going to execute me if I cannot find them again.",
            "Mirabel: What does it look like? May be I can help you look for it?",
            "Hamlin: The gift is a regular-looking gold coin! But it has the insignia of House Covingtomb engraved on one side.",
            "Mirabel: House Covingtomb insignia. The raven perched on a tombstone?",
            "Hamlin: Yes. Yes. The letter has the insignia too. Hard to miss it. Now hurry my dear and help me find it.",
            "[EndDialog|Exit]"
    ]

    # hamlin_conversation = Dialog(text_list, left_char="Hamlin", right_char="Mirabel",pause_duration=3)
    # hamlin_conversation.display_dialog()


