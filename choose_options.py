from buttons import button_pressed
from screen import display
import time

def choose_between(options):
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
    print(options[i][0], options[i][1])
