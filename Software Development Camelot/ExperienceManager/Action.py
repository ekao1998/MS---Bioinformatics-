class Action:
    def __init__(self):
        pass

    def action(self, command, wait=True):

        print('start '+command)

        if wait == True:
            return self.check_for_success(command)
        else:
            return True


    def check_for_success(self, command):
        while True:
            received = input()

            if received == 'succeeded '+ command:
                return True

            elif received.startswith('failed '+command):
                return False

class Motion (Action):

    def __init__(self):  
       pass
                
    def move_to(self, character, location):
        self.act.action("WalkTo(" +character + ","+ location +")")
        return True

    def move_away(self, location):
        self.act.action("MoveAway("+ location +")")
        return True
