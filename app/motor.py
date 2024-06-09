from gpiozero import DigitalOutputDevice
from time import sleep


class Motor:
    def __init__(self, in1, in2):
        self.in1 = DigitalOutputDevice(in1)
        self.in2 = DigitalOutputDevice(in2)

    def forward(self, duration):
        self.in1.on()
        self.in2.off()
        print("Motor running forward")
        sleep(duration)
        self.stop()

    def backward(self, duration):
        self.in1.off()
        self.in2.on()
        print("Motor running backward")
        sleep(duration)
        self.stop()

    def stop(self):
        self.in1.off()
        self.in2.off()
        print("Motor stopped")

    def close(self):
        self.in1.close()
        self.in2.close()
