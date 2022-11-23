import RPi.GPIO as GPIO
import time

ssr1 = 14
ssr2 = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ssr1, GPIO.OUT)
GPIO.setup(ssr2, GPIO.OUT)

GPIO.output(ssr1, GPIO.HIGH)
GPIO.output(ssr2, GPIO.HIGH)
time.sleep(3600)
GPIO.output(ssr1, GPIO.LOW)
GPIO.output(ssr2, GPIO.LOW)

GPIO.cleanup()

