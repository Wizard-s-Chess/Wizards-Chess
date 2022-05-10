from serial import Serial
import time

def move_motors(moves):
    ser = Serial('COM4', 9600)
    for move in moves:
        ser.write(bytes(str(move), 'ascii'))
        time.sleep(0.5)
    ser.close()