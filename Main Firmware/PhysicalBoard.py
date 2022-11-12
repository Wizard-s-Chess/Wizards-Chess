if not (__debug__):
    from serial import Serial
import time


class PhysicalBoard:
    def __init__(self):
        print("init serial")
        if not (__debug__):
            self.serial_port = Serial("/dev/ttyUSB0", 9600, timeout=None)

    def move_motors(self, moves, active_magnet):
        if __debug__:
            return
        if active_magnet:
            self.serial_port.write(bytes("m", "ascii"))
        else:
            self.serial_port.write(bytes("n", "ascii"))
        self.serial_port.write(bytes(moves, "ascii"))
        self.serial_port.write(bytes("f", "ascii"))
        # wait for confirmation from arduino that move was performed
        serialString = self.serial_port.read(1)

    def reset_motors(self):
        if __debug__:
            return
        self.serial_port.write(bytes("r", "ascii"))
