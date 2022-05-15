#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO  # Import the GPIO library.
import time  # Import time library
from hc_sr04 import HCSR04


class PWM_LED:

    def __init__(self, dc, pin):
        self._dc = dc
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        self._pwm = GPIO.PWM(pin, 100)
        self._usensor = HCSR04(18, 24)

    def start(self):
        self._pwm.start(self._dc)  # Start PWM with 0% duty cycle
        sleep_time = 0
        dc = self._usensor.distance()
        try:
            while True: 
                self._pwm.ChangeDutyCycle(abs(dc - 100))
                time.sleep(0.05)
                sleep_time += 0.05
                if round(sleep_time, 1) == 1.0:
                    sleep_time = 0
                    dc = self._usensor.distance()
                    print('Measured Distance = %.1f cm' % dc)
        except KeyboardInterrupt:
            print('Ctl C pressed - ending program')

        pwm.stop()  # stop PWM
        GPIO.cleanup()  # resets GPIO ports used back to input mode
