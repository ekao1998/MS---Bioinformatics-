from Action import Action

class Items:

    def __init__(self,name,item_type,current_location,description):
        self.name = name
        self.item_type = item_type
        self.current_location=current_location
        self.description = description

        self.act = Action()
        self.create()
        self.set_position()
        #pass

    owner=""
    description = ""
    player_owned = False
    sheathed = False
    icon_enabled = False
    total_icons = 0
    hand_held = "right"

    def create(self):
        print(self.item_type)
        self.act.action("CreateItem("+self.name+","+self.item_type+")")
        return True

    def set_position(self):
        # instantiate places class here, call place.create() fxn, if place doesn't already exist, create it
        self.act.action("SetPosition(" + self.name + "," + self.current_location + ")")
        return True

    def add_to_list(self):
        self.act.action("AddToList(" + self.name + ',' + self.description +")")
        return True

    def pick_up(self, character_name):

        if self.current_location == "":

            self.act.action("Pickup(" + character_name + "," + self.name + ")")

            if character_name == "Mirabel":
                self.player_owned = True

        else:
            self.act.action("Pickup(" + character_name + "," + self.name + ","+self.current_location+")")

            if character_name == "Mirabel":
                self.player_owned = True
            self.current_location = ""

        return True

    def remove_from_list(self):
        self.act.action("RemoveFromList(" + self.name + ")")
        self.player_owned = False
        self.sheathed = False
        return True

    def place_at(self, character, target,effect=""):
        self.act.action("Put(" +character+","+self.name+ "," + target+ ")")
        if effect != "":
            self.act.action("CreateEffect("+target+","+effect+")")
        return True

    def throw_away(self,character):
        self.act.action("Put(" +character+ "," +self.name+")")
        return True
    
    def give_to(self,character,target):
        self.act.action("Give(" +character+ "," +self.name+ ","+target+")")
        return True

    def take_from(self,character,target=""):
        if target != "":
            self.act.action("Take(" +character+ "," +self.name+ "," +target+")")
        else:
            self.act.action("Take(" +character+ "," +self.name+")")
        return True

    
    def pocket(self,character):
        '''
        Character places item held in left hand or right hand into pocket.
        '''

        if self.hand_held == "right":
            self.act.action("Sheathe(" + character + "," + self.name + ")")
            self.hand_held = None

        else:
            self.act.action("Pocket("+ character+ "," + self.name +")")
            self.hand_held = None

        return True
                

class Weapon(Items):
    def __init__(self, name, item_type, current_location, description):
        super().__init__(name, item_type, current_location, description)
        self.pocket(self.current_location)
    
    def weapon_attack(self, character, target, hit = "false"):
        self.weapon_draw(character)
        self.act.action("Attack(" +character+ "," +target+","+hit+")")
        return True
    
    def weapon_draw(self, character):
        self.act.action("Draw(" + character + "," + self.name + ")")
        self.sheathed = False
        return True

    def weapon_sheathe(self, character):
        '''
        Character places item held in right hand into pocket/sheathe etc.
        '''
        self.act.action("Sheathe(" + character + ","+ self.name +")")
        self.sheathed = True
        return True


class Potion(Items):
    def __init__(self, name, item_type, current_location, description, color, effect, vfx):
        super().__init__(name, item_type, current_location, description)
        self.color = color
        self.effect = effect
        self.vfx = vfx

    def drink(self, character):
        self.act.action("Drink(" +character + ")")
        return True

    def place_at(self, character, target,effect=""):
        self.act.action("Put(" +character+","+self.name+ "," + target+ ")")
        if effect == "" and self.vfx != "":
            self.set_effect(target,self.vfx)
        elif effect != "":
            self.set_effect(target,effect)
        return True

    def throw_away(self,character):
        self.act.action("Put(" +character+ "," +self.name+")")
        return True

    def set_effect(self, target, effect):
        self.act.action("CreateEffect(" + target+", "+effect+")")
        return True



    
    



# class potions: inherits all Items attributes and fxns, additionally has color, effect (e.g. resurrects, kills) 
# and vfx(e.g. explode) as attributes, additional methods: drink, throw_at, create_effect



# if __name__ == "__main__":
    # I = Items("")
