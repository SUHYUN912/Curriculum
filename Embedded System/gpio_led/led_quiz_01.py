import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led1 = 23
led2 = 24

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

try:
    while True:
        for i in range(11):
            cnt=0
            while True:
                GPIO.output(led1, True)
                GPIO.output(led2, True)
                time.sleep(i*0.001)

                GPIO.output(led1, False)
                GPIO.output(led2, False)
                time.sleep((10-i)*0.001)

                cnt=cnt+1
                if cnt==10: break;

        for j in range(10, -1, -1):
            cnt=0
            while True:
                GPIO.output(led1, True)
                GPIO.output(led2, True)
                time.sleep(i*0.001)

                GPIO.output(led1, False)
                GPIO.output(led2, False)
                time.sleep((10-i)*0.001)

                cnt=cnt+1
                if cnt==10: break;

except KeyboardInterrupt:
    pass

GPIO.cleanup()
