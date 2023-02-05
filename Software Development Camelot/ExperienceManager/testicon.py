import unittest
from Icon import Icon

class TestIcon(unittest.TestCase):

    def test_set_icon_name(self):
        
        icon = Icon("hamilin_talk","hamilin","talk","talk to hamilin", True)
        self.assertTrue(icon.set_icon_name("talk_icon")) 

    def test_set_icon_target(self):
        
        icon = Icon("hamilin_talk","hamilin","talk","talk to hamilin", True)
        self.assertTrue(icon.set_icon_target("Hamilin"))

    def test_get_icon_name(self):
        icon = Icon("hamilin_talk","hamilin","talk","talk to hamilin", True)
        icon.set_icon_name("mirabel_talk")
        self.assertEqual(icon.get_icon_name(), "mirabel_talk")

    def test_get_icon_target(self):
        icon = Icon("hamilin_talk","hamilin","talk","talk to hamilin", True)
        icon.set_icon_target("mirabel")
        self.assertEqual(icon.get_icon_target(), "mirabel")

      

if __name__=="__main__":
    unittest.main()