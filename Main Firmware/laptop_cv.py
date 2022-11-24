import serial
from ComputerVision2 import ComputerVision as CV

ser = serial.Serial("/dev/tty.raspberrypi", timeout=None, baudrate=9600)
ser.flushInput()
ser.flushOutput()

while True:
    out = ser.read(1).decode()
    print(out)
    if out == "d":
        changed_squares = CV.get_changed_squares()
        ser.write(bytes(changed_squares, "ascii"))
    if out == "p":
        CV.save_pre_movement_image()
        ser.write("o")
