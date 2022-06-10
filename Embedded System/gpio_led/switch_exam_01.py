import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

button_pin = 18

GPIO.setup(button_pin, GPIO.IN)

try:
    while True:
        buttonInput = GPIO.input(button_pin)
        print(buttonInput)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
