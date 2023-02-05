import time
from Action import Action
from Menu import Menu
from functions import MainGamePlay
from Transition import Transition
from Sequences import Sequences
from DialogTexts import DialogTexts
from HintTexts import HintTexts


menu_options = ["Show Hint", "Change Appearance", "Change Language"]
menu_actions = ["MenuShowHint", "MenuChangeAppearance", "MenuChangeLanguage"]

M = MainGamePlay()
H = HintTexts(M)
D = DialogTexts(M)
T = Transition(M)
S = Sequences(M,D)
MM = Menu(menu_options,menu_actions,M,H)
TalkToHamlin=False
Act = Action()



def Wait():
    while (True):
        received=input()

        if received=="input Selected Start":
            Act.action('HideMenu()')
            # S.startNarration()
            # M.PlayerAppearanceChoice()
            break

        elif received=="input Selected Credits":
            show_credit()
        
        elif received=="input Selected Quit":
            Act.action("Quit()") 

def showMenu():
    Act.action("ShowMenu()")
    Wait()
    # Act.action("HideMenu()")
    Act.action("EnableInput()")

def credit_close():
    while (True):
        rec=input()
        if rec=="input Close Credits":
            break 

def show_credit():
        Act.action("SetCredits('MyExperienceManager')")
        Act.action("ShowCredits")
        credit_close()
        Act.action("HideCredits")   

def main():
    
    # initialization()
    showMenu()

    while (True):
        
        received=input()

        try:
            # Menu interaction inputs
            if received=="input Selected Start":
                Act.action('HideMenu()')
                S.startNarration()
                
            elif received=="input TalkToNicholaus Nicholaus": #Talk to Nicholaus
                S.TalkToNicholaus()    

            elif received == "input arrived Mirabel position Nicholaus": #Nicholaus turning face to Mirabel
                Act.action("Face(Nicholaus,Mirabel)")

            elif received=="input Selected Resume":
                Act.action("HideMenu()")
                Act.action("EnableInput()")


            elif received=="input Selected Credits":
                show_credit()
            
            elif received=="input Selected Quit":
                Act.action("Quit()")          
            
            elif received=="input Key Pause":
                Act.action("ShowMenu()")

            elif received=="input Selected changetoBandit":
                MM.ChangeCharacterClothing("Bandit")

            elif received=="input Selected changetopeasant":
                MM.ChangeCharacterClothing("Peasant")

            elif received=="input Selected changetonobel":
                MM.ChangeCharacterClothing("Noble")
                
            # General story interaction inputs
            elif received=="input Close Narration":
                Act.action("HideNarration()")
                Act.action("EnableInput()")
            
            elif received=="input TalkToHamlin Hamlin":
                S.TalkToHamlinSequence()
            
            elif received=="input MeetHamlin Hamlin":
                if not TalkToHamlin:
                    M.KingAnnouncment()
                else:
                    M.KingSpokesPersonAnnouncement()    


            elif received=="input TalkToDorothy Dorothy":
                Act.action("ClearDialog()")
                S.TalkToDorothy()

            elif received=="input TalkToNicholaus2 Nicholaus":
                S.TalkToNicholaus2()

            elif received=='input Close List': #Close inventory List
                Act.action("HideList()")

            elif received=="input Selected EndDialog":
                Act.action("HideDialog()")

            # Place interaction inputs
            elif received=="input LeaveHome Home.Door":
                M.character_Mirabel.exit_from_to("Home.Door","Sedonia.BlueHouseDoor")

            elif received=="input LeaveCityLibrary CityLibrary.Door":
                M.character_Mirabel.exit_from_to("CityLibrary.Door","Sedonia.BrownHouseDoor")

            elif received=="input LeaveBar Bar.Door":
                M.character_Mirabel.exit_from_to("Bar.Door","Sedonia.RedHouseDoor")

            elif received=="input LeaveStorage Storage.Door":
                M.character_Mirabel.exit_from_to("Storage.Door","Sedonia.GreenHouseDoor")
            
            elif received=="input EnterHome Sedonia.BlueHouseDoor":
                M.character_Mirabel.exit_from_to("Sedonia.BlueHouseDoor","Home")

            elif received=="input EnterBar Sedonia.RedHouseDoor":
                M.character_Mirabel.exit_from_to("Sedonia.RedHouseDoor","Bar.Door")

            elif received=="input EnterCityLibrary Sedonia.BrownHouseDoor":
                M.character_Mirabel.exit_from_to("Sedonia.BrownHouseDoor","CityLibrary.Door")
            
            elif received=="input EnterStorage Sedonia.GreenHouseDoor":
                M.character_Mirabel.exit_from_to("Sedonia.GreenHouseDoor","Storage.Door")

            # Transitions between Sedonia and Elmwood Forest
            elif received == "input arrived Mirabel position Sedonia.NorthEnd":
                #S.WarnPlayer()
                Act.action("SetCameraMode(follow)")
                T.TransitionSedoniaToElmwood()
                # M.character_Mirabel.exit_from_to("Sedonia.NorthEnd","Elmwood.WestEnd")

            elif received == "input arrived Mirabel position D":
                M.character_Mirabel.exit_from_to("")

            elif received == "input arrived Mirabel position Elmwood.WestEnd":
                M.character_Mirabel.exit_from_to("Elmwood.WestEnd","Sedonia.NorthEnd")
                M.ReturnToSedonia()
                
            elif received=="input Selected save Nicholaus":
                Act.action("HideDialog")
                M.SaveNicholaus()
                TalkToHamlin=False

            elif received=="input Selected find father":
                Act.action("HideDialog")
                M.LetNickolausDie()
                TalkToHamlin=True

            elif received=="input AttackSoldierToSaveNicholaus knight3":
                M.AttackSoldierToSaveNicholaus()

            elif received=="input arrived Mirabel position deadknight":
                M.TakeSword()

            # Transitions between Elmwood and Elmwood2 Forest
            elif received == "input arrived Mirabel position Elmwood.EastEnd":                            
                T.TransitionElmwood1ToElmwood2()
                #T.TransitionSedoniaToElmwood()
                
            # Bandits attack Mirabel
            elif received == "input arrived Mirabel position Bandit1":
                M.BanditAttackMirabel()

            elif received == "input arrived Mirabel position Elmwood2.WestEnd":
                T.ElmwoodWestEndToElmwoodEastEnd()
                            
            #Transition from Elmwood2 to SpookyPath
            elif received == "input arrived Mirabel position Elmwood2.Plant":
                T.TransitionElmwoodToSpookyPath()
                S.BanditsEavesdropSequence()

            #Transition from SpookyPath to Elmwood2
            elif received == "input arrived Mirabel position SpookyPath.WestEnd":
                Act.action("StopSound()")
                T.SpookyPathWestEndToElmwood2Plant()     

            #Transition from SpookyPath to Ginezin
            elif received == "input arrived Mirabel position SpookyPath.EastEnd":
                T.SpookyPathEastEndToGinezinNorthEnd()  

            elif received=="input Selected Take Nicholaus help": #Take Nicholaus help
                S.TakeNicholausHelp()

            # transition elmwood2 / City of Ginezin
            elif received == "input arrived Mirabel position Elmwood2.EastEnd": 
                M.arrived_city_ginezin()
                M.create_castle_sorrounding()
                M.G_Library_letter()

            elif received == "input arrived Mirabel position Ginezin.WestEnd": 
                T.GinezinWestEndToElmwood2EastEnd()

            # Items interaction inputs
            elif received =="input ReadScroll HamlinNote":
                S.ReadRollSequence()

            elif received =='input PickUpMagnifyingGlass MagnifyingGlass':
                M.PickupMagnifyingGlass()

            elif received=="input PickUpSedoniaSword SedoniaSword":
                M.PickupSedoniaSword()

            elif received=="input Key Inventory":
                Act.action("ShowList(Mirabel)")

            elif received =='input StashMagnifyingGlass MagnifyingGlass':
                M.StashMagnifyingGlass()            

            elif received == 'input StashCoin MagnifyingGlass':
                M.StashCoin()

            elif received == 'input InspectCoin GinezinCoin':
                S.InspectCoin()

            elif received =='input PickUpCoin GinezinCoin':   # Pickup Coin 
                M.PickupCoin()            
                
            elif received == 'input Selected Insults':
                Act.action("ClearDialog()")
                S.InsultsDorothy()

            elif received == 'input Selected Praises':
                Act.action("ClearDialog()")
                S.PraisesDorothy()

            elif received == "input arrived Mirabel position CastleCrossroads.Gate":
                S.castle_warning()
            
            elif received == 'input Selected Listen to the guard':
                Act.action("HideDialog()")

            elif received == "input Selected Ignore the guard":
                Act.action("HideDialog()")
                T.transition_to_dungeon()

            elif received=='input Selected Do not take nicholaus help':
                Act.action("HideDialog()")

            elif received =="input arrived Mirabel position Ginezin.EastEnd":
                T.transition_to_castlecrossroads()

            elif received == "input arrived Mirabel position Ginezin.Fountain":
                M.trasition_to_G_library()

            elif received == 'input arrived Mirabel position CastleCrossroads.WestEnd':
                T.transition_castlecrossroads_to_G()
            
            elif received == "input arrived Mirabel position G_Library.SpellBook":
                S.SecretPassageWaySequence()

            elif received == "input Selected HailWitch":
                Act.action("HideDialog()")
                S.WitchDialogSequence()

            elif received == "input Selected DontHailWitch":
                Act.action("HideDialog()")

            elif received == "input Selected AgreeRiddle":
                S.WitchAgreeRiddle()

            elif received == "input Selected RefuseRiddle":
                S.WitchRefuseRiddle()

            elif received == "input Selected SolveRiddle":
                S.WitchSolveRiddle()

            elif received == "input Selected FailRiddle":
                S.WitchFailRiddle()

            elif received == "input arrived Mirabel position Ginezin.Fountain":
                M.trasition_to_G_library()

            elif received == "input ReadLetter Letter":
                S.G_Letter_content()
            
            elif received == 'input Selected Close the letter':
                Act.action("HideDialog()")

            elif received == "input arrived Mirabel position HallWay.Door":
                T.transition_from_Hallway_to_Library()

            elif received== "input arrived Mirabel position G_Library.Door":
                T.transition_from_Library_to_Hallway()
                M.Hallwaysequence()

            elif received == 'input Selected Listen_to_the_guard1':
                Act.action("HideDialog()")
                M.transition_to_dungeon()

            elif received == "input Selected Ignore_the_guard1":
                Act.action("HideDialog()")
                M.MirabelFight()
                
            elif received == "input Selected EavesdropDialog":
                Act.action("HideDialog()")
                S.BanditEavesdropDialog()

            elif received == "input Selected LeaveBanditsDialog":
                Act.action("HideDialog()")

            elif received == "input Key Interact":
                MM.open_menu()

            elif received[0:19] == "input Selected Menu":
                # menu_options = M.MM.map_options_functions()
                menu_input = received[14:]
                eval("MM."+menu_input+"()")

            elif received == "input Selected changetoEnglish":
                MM.ChangeLanguage(game_language="en")

            elif received == "input Selected changetoSwahili":
                MM.ChangeLanguage(game_language="sw")

        except AttributeError as err:
            print("Attribute error: {0}".format(err))
            raise       
        except OSError as err:
            print("OS error: {0}".format(err))
            raise
        except ValueError:
            print("Could not convert data to an integer.")
            raise
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise
            

###################################
#Main Function Starts here    
if __name__ == "__main__":
    main()
