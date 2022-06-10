import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin1 = 23
led_pin2 = 24

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

pwm1 = GPIO.PWM(led_pin1, 1000.0)
pwm1.start(0.0)
pwm2 = GPIO.PWM(led_pin2, 1000.0)
pwm2.start(0.0)

try:
    while True:
        for i in range(101):
            pwm1.ChangeDutyCycle(i)
            pwm2.ChangeDutyCycle(i)
            time.sleep(0.01)

        for i in range(100, -1, -1):
            pwm1.ChangeDutyCycle(i)
            pwm2.ChangeDutyCycle(i)
            time.sleep(0.01)

except KeyboardInterrupt:
    pass

pwm1.stop()
pwm2.stop()

GPIO.cleanup()
