import RPi.GPIO as GPIO
import time

def button_callback():
    print("Button was pushed!")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    v = GPIO.input(22)
    if v == 0:
        button_callback()
        time.sleep(1)