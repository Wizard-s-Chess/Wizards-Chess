from serial import Serial
import time

def move_motors(moves, active_magnet):
    ser = Serial('COM4', 9600)
    for move in moves:
        ser.write(bytes(str(move), 'ascii'))
        time.sleep(0.5)
    if active_magnet:
        ser.write(b'm', 'ascii')
    else:
        ser.write(b'n', 'ascii')
    ser.close()

