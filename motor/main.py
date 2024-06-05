import time

import RPi.GPIO as GPIO

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Set the pin number
servo_pin = 37

# Set the PWM frequency and duty cycle
frequency = 50
duty_cycle = 7.5

# Configure the pin as PWM
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, frequency)

# Start the PWM
pwm.start(duty_cycle)

# Rotate the servo motor to a specific angle
def rotate(angle):
    duty_cycle = (angle / 18) + 2.5
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)

# Rotate the servo motor to 0 degrees
rotate(0)

# Rotate the servo motor to 90 degrees
rotate(90)

# Rotate the servo motor to 180 degrees
rotate(180)

# Cleanup
pwm.stop()
GPIO.cleanup()