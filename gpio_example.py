# !/usr/bin/python
import RPi.GPIO as GPIO
import time

version = GPIO.VERSION
print version

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(17)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)

