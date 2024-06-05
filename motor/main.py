import RPi.GPIO as GPIO
import time

# Pin Definitions
servo_pin = 13  # GPIO 13 (PWM1)

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
GPIO.setup(servo_pin, GPIO.OUT)  # Set GPIO pin as an output

# Set up PWM (Pulse Width Modulation)
pwm_frequency = 50  # Frequency in Hz (50 Hz is common for servos)
pwm = GPIO.PWM(servo_pin, pwm_frequency)
pwm.start(0)  # Initialization with 0% duty cycle

def set_servo_angle(angle):
    """Set the servo angle.
    
    Args:
        angle (int): Angle in degrees, typically between 0 and 180.
    """
    duty_cycle = (angle / 18.0) + 2.5  # Convert angle to duty cycle
    pwm.ChangeDutyCycle(duty_cycle)  # Change the duty cycle
    time.sleep(1)  # Wait 1 second for the servo to reach the position

try:
    # Set servo to 90 degrees
    set_servo_angle(90)
    print("Servo moved to 90 degrees.")
except KeyboardInterrupt:
    print("Program exited by user.")
finally:
    pwm.stop()  # Stop PWM
    GPIO.cleanup()  # Clean up GPIO to reset pins
