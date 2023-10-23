import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

def setservo(deg):
    currentSpeed = 7.25 + deg / 90 * 4.75
    servo.ChangeDutyCycle(currentSpeed)
    time.sleep(1.0)

print("Test code")

print("90 degrees")
setservo(90)

print("-90 degrees")
setservo(-90)

print("0 degrees")
setservo(0)

print("45 degrees")
setservo(45)

print("-45 degrees")
setservo(-45)
