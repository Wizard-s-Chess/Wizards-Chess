from serial import Serial
import time

def move_motors(ser, moves, active_magnet):
    time.sleep(3)
    if active_magnet:
        ser.write(bytes('m', 'ascii'))

    ser.write(bytes(moves, 'ascii'))
    ser.write(bytes('n', 'ascii'))

