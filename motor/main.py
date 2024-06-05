import RPi.GPIO as GPIO
import time

# GPIO pin numarasını Broadcom SOC kanalına göre ayarla
GPIO.setmode(GPIO.BCM)

# Servo motorun bağlı olduğu pin numarası
servo_pin = 33

# GPIO pinini çıkış olarak ayarla
GPIO.setup(servo_pin, GPIO.OUT)

# PWM nesnesi oluştur ve 50Hz ile başlat (Servo motorlar genellikle 50Hz ile çalışır)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

def set_servo_angle(angle):
    # Açıyı duty cycle'a dönüştür
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

try:
    # Servo motoru belirli bir açıya ayarla
    set_servo_angle(90)  # Örnek olarak 90 dereceye ayarla
finally:
    # PWM'i durdur
    pwm.stop()
    # GPIO ayarlarını temizle
    GPIO.cleanup()
