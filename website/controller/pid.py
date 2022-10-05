import PID
import time
import numpy as np
from scipy.interpolate import BSpline, make_interp_spline #  Switched to BSpline
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
HEATER = 17
GPIO.setup(HEATER,GPIO.OUT)

P = 0.2
I = 0.0
D = 0.0
L = 0
sampletime = 2.0

def measure_Temp:
    temp = 20.0
    return temp

while True:
    pid = PID.PID(P, I, D)
    pid.SetPoint=25.0
    pid.setSampleTime(sampletime)
    END = L
    feedback = measure_Temp()
    pid.update(feedback)
    output = pid.output
    GPIO.output(HEATER, False)
    time.sleep(output)
    GPIO.output(HEATER, True)
