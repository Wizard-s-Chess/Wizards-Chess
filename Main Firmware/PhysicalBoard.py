from serial import Serial
import time

class PhysicalBoard:
    def __init__(self):
        self.serial_port = Serial('COM5', 9600)

    def move_motors(self, moves, active_magnet):
        time.sleep(3)
        if active_magnet:
            self.serial_port.write(bytes('m', 'ascii'))

        self.serial_port.write(bytes(moves, 'ascii'))
        self.serial_port.write(bytes('n', 'ascii'))
        #wait for confirmation from arduino that move was performed

