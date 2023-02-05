import unittest
from Menu import Menu
from functions import MainGamePlay
from InfoTools import Hint



class TestMenu(unittest.TestCase):
    menu_options = ["Show Hint"]
    menu_actions = ["ShowHint"]
    # M = MainGamePlay()
    # H=Hint()    
    menu = Menu(menu_options,menu_actions)

    def test_menu_data_type(self):
        self.assertIsInstance(self.menu.get_menu(),list)


    def test_menu_data(self):        
        self.assertEqual(self.menu.get_menu(),[('Show Hint', 'ShowHint')])


    def test_menu_show(self):
        self.assertEqual(self.menu.show_menu(),['[ShowHint|Show Hint]'])


    def test_map_fxn(self):
        self.assertEqual(self.menu.map_options_functions(),{"ShowHint":"ShowHint"})

    def test_map_fxn_mm(self):
        self.assertEqual(self.menu.map_options_functions(),{"ShowHint":"ShowHint"})

    # def test_get_text(self):
        
    #     dialog_texts = Menu()
    #     dialog_texts.set_text("new_text","en",["New text row 1"])     
    #     self.assertEqual(dialog_texts.get_text("new_text","en",["New text row 1"]), ["New text row 1"])


if __name__=="__main__":
    unittest.main()