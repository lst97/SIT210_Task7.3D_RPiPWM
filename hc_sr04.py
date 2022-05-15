
import RPi.GPIO as GPIO
import time

class HCSR04:

    def __init__(self, GPIO_TRIGGER, GPIO_ECHO):
        GPIO.setmode(GPIO.BOARD)
        self.GPIO_TRIGGER = GPIO_TRIGGER
        self.GPIO_ECHO = GPIO_ECHO

        # set GPIO direction (IN / OUT)

        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)

        # for simlulation

        self._dist = 0
        self._direction = 'far'

    def distance(self):

        # set Trigger to HIGH
        # GPIO.output(GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        # time.sleep(0.00001)
        # GPIO.output(GPIO_TRIGGER, False)

        # StartTime = time.time()
        # StopTime = time.time()

        # save StartTime
        # while GPIO.input(GPIO_ECHO) == 0:
        # ....StartTime = time.time()

        # save time of arrival
        # while GPIO.input(GPIO_ECHO) == 1:
        # ....StopTime = time.time()

        # time difference between start and arrival
        # TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        # distance = (TimeElapsed * 34300) / 2

        # because the sensor was damaged. I will return a continues value between
        # 0 - 34300

        if self._direction == 'far':
            self._dist += 5000
            if self._dist >= 17150:
                self._dist = 17150
                self._direction = 'close'
        else:
            self._dist -= 5000
            if self._dist <= 0:
                self._dist = 0
                self._direction = 'far'

        # convert distance to presentage.

        return (self._dist / 17150) * 100
