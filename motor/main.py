import RPi.GPIO as GPIO
import time

# Pin Definitions
servo_pin = 13  # GPIO 13 (PWM1)

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
GPIO.setup(servo_pin, GPIO.OUT)  # Set GPIO pin as an output

# Set up PWM (Pulse Width Modulation)
pwm_frequency = 50  # Frekans Hz cinsinden (servolar için genellikle 50 Hz)
pwm = GPIO.PWM(servo_pin, pwm_frequency)
pwm.start(0)  # 0% duty cycle ile başlatma

def set_servo_angle(angle):
    duty_cycle = (angle / 18.0) + 2.5  # Açıyı duty cycle'a çevir
    pwm.ChangeDutyCycle(duty_cycle)  # Duty cycle'ı değiştir
    time.sleep(1)  # Servonun pozisyon alması için bekle

try:
    set_servo_angle(90)  # Servoyu 90 dereceye ayarla
    print("Servo 90 dereceye ayarlandı.")
finally:
    pwm.stop()  # PWM durdur
    GPIO.cleanup()  # GPIO ayarlarını temizle
