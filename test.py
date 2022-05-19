from buttons import buttons_init
from screen import lcd_init
from choose_options import *

if __name__ == "__main__":
    lcd_init()
    buttons_init()
    options = [["Choose your level", "Level " + str(i + 1)] for i in range(10)]
    choose_between(options)
