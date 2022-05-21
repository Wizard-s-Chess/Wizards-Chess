from serial import Serial
import time

class PhysicalBoard:
    def __init__(self):
        print("init serial")
        self.serial_port = Serial("COM4", 9600,timeout=None)

    def move_motors(self, moves, active_magnet):
        time.sleep(3)
        if active_magnet:
            self.serial_port.write(bytes('m', 'ascii'))
        self.serial_port.write(bytes(moves, 'ascii'))
        self.serial_port.write(bytes('n', 'ascii'))
        self.serial_port.write(bytes('f', 'ascii'))
        #wait for confirmation from arduino that move was performed
        serialString = self.serial_port.read(1)
        

