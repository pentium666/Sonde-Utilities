import RPi.GPIO as GPIO
import time

GPS = 40

GPIO.setmode(GPIO.board)
GPIO.setup(GPS, GPIO.OUT)

# Set output to high
GPIO.output(GPS, 1)
time.sleep(1)
GPIO.output(GPS, 0)
time.sleep(1)
GPIO.outpu(GPS, 1)
