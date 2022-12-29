import RPi.GPIO as GPIO
import time

ssr1 = 14
ssr2 = 15
led = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(ssr1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ssr2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

try:
    print("set GIOP high")
    GPIO.output(ssr1, GPIO.HIGH)
    GPIO.output(ssr2, GPIO.HIGH)
    GPIO.output(led, GPIO.HIGH)
    print("sleeping")
    time.sleep(3600)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print("Keyboard interrupt")

except:
    print("some error")

finally:
    print("clean up")
    GPIO.cleanup() # cleanup all GPIO
