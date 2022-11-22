import serial
from ComputerVision2 import ComputerVision as CV

ser = serial.Serial("/dev/tty.raspberrypi", timeout=1, baudrate=9600)
serial.flushInput()
serial.flushOutput()

while True:
    out = serial.read(1).decode()
    if out == "d":
        changed_squares = CV.get_changed_squares()
        serial.write(bytes(changed_squares, "ascii"))
    if out == "p":
        CV.save_pre_movement_image()
        serial.write("o")
