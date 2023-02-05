import unittest
from DialogTexts import DialogTexts
from functions import MainGamePlay
M = MainGamePlay

class TestDialogTexts(unittest.TestCase):

    def test_set_text(self):
        
        dialog_texts = DialogTexts(M)
        self.assertTrue(dialog_texts.set_text("new_text","en",["New text row 1"]), ["New text row 1"])


    def test_get_text(self):
        
        dialog_texts = DialogTexts(M)
        dialog_texts.set_text("new_text","en",["New text row 1"])     
        self.assertEqual(dialog_texts.get_text("new_text","en"), ["New text row 1"])

    def test_get_class(self):
        
        dialog_texts = DialogTexts(M)
        dialog_texts.set_text("new_text","en",["New text row 1"])   
        self.assertEqual(dialog_texts.get_specific_class(language="en",conversation_class="new"), [["New text row 1"]])


if __name__=="__main__":
    unittest.main()

    # Multi-Languages for hints
    # Multi-Lang for items
    # Menu presses E- change_appearance, change_language, show_hint
    # Slides - architecture, sprint impediments,
    # Tests
    # Start-to-end demo

