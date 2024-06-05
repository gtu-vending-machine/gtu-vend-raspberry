import time

import RPi.GPIO as GPIO

# Set GPIO mode and pin number
GPIO.setmode(GPIO.BCM)
servo_pin = 37

# Set servo motor properties
GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50)  # 50 Hz frequency

# Start servo motor
servo.start(0)

try:
    while True:
        # Rotate servo motor to 0 degrees
        servo.ChangeDutyCycle(2.5)
        time.sleep(1)

        # Rotate servo motor to 90 degrees
        servo.ChangeDutyCycle(7.5)
        time.sleep(1)

        # Rotate servo motor to 180 degrees
        servo.ChangeDutyCycle(12.5)
        time.sleep(1)

except KeyboardInterrupt:
    # Stop servo motor and clean up GPIO
    servo.stop()
    GPIO.cleanup()