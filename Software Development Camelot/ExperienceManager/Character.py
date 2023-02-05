from Action import Action
from Icon import Icon

class Character:

    char_icons = []

    def __init__(self,character_name,body_type,expression,cloth_type,start_location,skin_color,eye_color,hair_color,hairstyle,soundtrack="",current_location=""):
        self.character_name=character_name
        self.body_type=body_type
        self.expression=expression
        self.cloth_type=cloth_type
        self.start_location=start_location
        self.skin_color=skin_color
        self.eye_color=eye_color
        self.hair_color=hair_color
        self.hairstyle=hairstyle
        self.soundtrack=soundtrack
        self.current_location=start_location

        self.act = Action()
        
        self.create_character()
        self.set_dress()
        self.set_expression()
        self.set_hair_style()
        self.initialize_location()
        self.play_soundtrack()

        pass
    
    def create_character(self):
        self.act.action("CreateCharacter("+self.character_name+","+self.body_type+")")
        return True
    
    def set_camera_focus(self,mode):
        self.act.action("SetCameraFocus("+self.character_name+")")
        self.act.action("SetCameraMode("+mode+")")
        return True

    def set_dress(self):
        self.act.action("SetClothing("+self.character_name+","+self.cloth_type+")")
        return True

    def set_hair_style(self):
        self.act.action("SetHairStyle("+self.character_name+","+self.hairstyle+")")
        self.act.action("SetHairColor("+self.character_name+","+self.hair_color+")")
        return True

    def set_expression(self, expression=""):
        if expression != "":
            self.expression = expression
        if self.expression != "":
            self.act.action("SetExpression("+self.character_name+","+self.expression+")")
        return True


    def initialize_location(self):
        self.act.action("SetPosition("+self.character_name+","+self.start_location+")")
        self.current_location = self.start_location
        return True

    def play_soundtrack(self):
        
        if self.soundtrack != "":
            self.act.action("PlaySound("+self.soundtrack + "," + self.character_name + ",true)")
            
        return True

    def enable_char_icon(self, icon_details):

        char_icon = Icon(icon_details["name"], icon_details["target"], icon_details["icon_type"], icon_details["description"], icon_details["default"])

        # char_icon = Icon()

        self.char_icons.append(icon_details)    

        return True

    def exit_from_to(self,current_location,target_location):
        self.act.action("FadeOut()")
        self.act.action("Exit("+self.character_name+","+current_location+", true)")
        self.act.action("SetPosition("+self.character_name+", "+target_location+")")
        self.act.action("FadeIn()")
        self.current_location = target_location
        return True

 
    def teleport(self,target_location,effect="", fade_out=True, fade_in=True):
        if effect !="":
            self.act.action("CreateEffect("+self.character_name+","+effect+")")
        if fade_out:
            self.act.action("FadeOut()")
        self.act.action("SetPosition("+self.character_name+", "+target_location+")")
        if fade_in:
           self.act.action("FadeIn()")
        self.current_location = target_location
        return True

