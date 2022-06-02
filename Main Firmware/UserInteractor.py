from Screen import *
from Buttons import *
import time


#A class that prompts the user with messages on the screen and gets input from them
class UserInteractor:
    def __init__(self):
        lcd_init()
        buttons_init()

    def get_game_mode(self):
        options = [("Choose mode",">Watch      Play"),("Choose mode"," Watch     >Play")]
        res = self.choose_between(options)
        return res == 1

    def choose_ai_level(self):
        options = [["Pick level: 1-20", "Level " + str(i + 1)] for i in range(20)]
        return self.choose_between(options)
    
    def get_player_starts(self):
        options = [("Choose color",">White     Black"),("Choose color"," White    >Black")]
        res = self.choose_between(options)
        return res == 1
    
    def wait_for_player_confirmation(self):
        options = [["Your turn: ", ">Play      Reset"], ["Your turn: ", "Play      >Reset"]]
        choice = self.choose_between(options)
        reset = False
        if choice == 1:
            display("Put pieces to", "initial position")
            reset = True
            pass
        else:
            display("Great! Please", "wait for the AI")
            time.sleep(0.5)
            display("","")
        return reset
    
    def display_try_again(self):
        display("Move not legal","choose other move")
        time.sleep(2)
        display("","")
    
    def choose_between(self,options):
        i = 0
        display(options[i][0], options[i][1])
        finished = False
        while not finished:
            pressed = button_pressed()
            if pressed[0]:
                i += 1
                i = i % len(options)
                display(options[i][0], options[i][1])
                time.sleep(0.5)
            elif pressed[1]:
                finished = True
                display("Wait please ...", "")
        return i
    
    def display_result(self,result):
        if result:
            display("You won!","Well played :)")
        else:
            display("You lost!",":(")

