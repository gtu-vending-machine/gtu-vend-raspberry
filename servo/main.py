from gpiozero import DigitalOutputDevice
from time import sleep

# Setup the GPIO pins for IN1 and IN2 on the L298N
in1 = DigitalOutputDevice(5)
in2 = DigitalOutputDevice(6)

in3 = DigitalOutputDevice(16)
in4 = DigitalOutputDevice(26)


def motor_forward(duration, in1, in2):
    in1.on()
    in2.off()
    print("Motor running forward")
    sleep(duration)
    motor_stop()


def motor_backward(duration, in1, in2):
    in1.off()
    in2.on()
    print("Motor running backward")
    sleep(duration)
    motor_stop()


def motor_stop():
    in1.off()
    in2.off()
    print("Motor stopped")


# Example usage:
# motor_forward(5)  # Run motor forward for 5 seconds
# motor_backward(5)  # Run motor backward for 5 seconds

motor_forward(5, in1, in2)
motor_backward(5, in1, in2)

motor_forward(5, in3, in4)
motor_backward(5, in3, in4)

# Cleanup the GPIO pins
in1.close()
in2.close()

in3.close()
in4.close()
