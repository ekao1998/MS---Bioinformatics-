from Action import Action

class Icon:
    def __init__(self,name,target,icon_type, description,default) -> None:
        self.name = name
        self.target = target
        self.icon_type = icon_type
        self.description = description
        self.default = default

        self.act = Action()

    def set_icon_name(self,name):
        self.name=name
        return True

    def get_icon_name(self):
        return self.name

    def set_icon_target(self,target):
        self.target=target
        return True

    def get_icon_target(self):
        return self.target

    def create_icon(self):
        self.act.action('EnableIcon("'+self.name +'", '+self.icon_type+','+self.target+',"'+self.description+'","'+self.default+'")')
        return True

    def remove_icon(self):
        self.act.action('DisableIcon("'+self.name+'",'+self.target+')')
        return True