import time

import RPi.GPIO as GPIO

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin for the servo motor
servo_pin = 13

# Set the frequency for the servo motor
frequency = 50

# Initialize the GPIO pin for the servo motor
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM object for the servo motor
pwm = GPIO.PWM(servo_pin, frequency)

# Start the PWM signal with a duty cycle of 0 (servo motor at 0 degrees)
pwm.start(0)

# Function to set the angle of the servo motor
def set_angle(angle):
    duty_cycle = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

# Example usage: set the servo motor to 90 degrees
set_angle(90)

# Cleanup GPIO
pwm.stop()
GPIO.cleanup()