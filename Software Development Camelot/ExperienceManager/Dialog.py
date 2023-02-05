import Action
import time

act_on = Action()

class Dialog:

    def __init__(self, left_char, right_char,dialog_text):  
        self.left_char = left_char
        self.right_char = right_char
        self.dialog_text = dialog_text

    def partial_dialog(narration_text, start, end, left="", right="", soundtrack=""):

        if not isinstance(narration_text, list):
            return "TypeError: Narration text must be a list of dialog lines"

        act_on.action("ShowDialog()")
        if left!="":
            act_on.action("SetLeft("+left+")")

        if right!="":
            act_on.action("SetRight("+right+")")

        for x in range(start, end):
            act_on.action("SetDialog(" + narration_text[x] + ")")
            time.sleep(3)

        act_on.action("HideDialog()")

        return True