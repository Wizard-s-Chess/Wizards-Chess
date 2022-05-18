from shutil import move
from play import *
import logging
from serial import Serial


if __name__ == "__main__":
    ser = Serial('COM5', 9600)
    logging.basicConfig(filename='chess.log', encoding='utf-8', level=logging.INFO)
    launch_game(ser)
    ser.close()
    