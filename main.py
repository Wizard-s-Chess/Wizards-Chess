from play import *
from serial import Serial
from screen import lcd_init
from buttons import buttons_init


if __name__ == "__main__":
    lcd_init()
    buttons_init()
    ser = Serial('COM5', 9600)
    launch_game(ser)
    ser.close()
    