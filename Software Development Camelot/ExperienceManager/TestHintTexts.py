import unittest
from HintTexts import HintTexts
from functions import MainGamePlay
M = MainGamePlay

class TestHintTexts(unittest.TestCase):

    def test_set_text(self):
        
        hint_texts = HintTexts(M)
        self.assertTrue(hint_texts.set_text("new_text","en",["New text row 1"]), ["New text row 1"])


    def test_get_text(self):
        
        hint_texts = HintTexts(M)
        hint_texts.set_text("new_text","en",["New text row 1"])     
        self.assertEqual(hint_texts.get_text("new_text","en"), ["New text row 1"])

    def test_get_class(self):
        
        hint_texts = HintTexts(M)
        hint_texts.set_text("new_text","en",["New text row 1"])   
        self.assertEqual(hint_texts.get_specific_class(language="en",hint_class="new"), [["New text row 1"]])


if __name__=="__main__":
    unittest.main()