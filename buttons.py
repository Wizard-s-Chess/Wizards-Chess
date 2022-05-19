import RPi.GPIO as GPIO
import time

def buttons_init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_pressed():
    v1 = GPIO.input(22)
    v2 = GPIO.input(27)
    return [v1 == 0, v2 == 0]