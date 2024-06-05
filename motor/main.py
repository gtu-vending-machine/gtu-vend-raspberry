from gpiozero import Servo
from time import sleep

# Raspberry Pi'nin 33 numaralı pinini kullanarak Servo nesnesi oluştur
servo = Servo(33)

try:
    while True:
        # Servo motoru minimum konuma (-1) hareket ettir
        servo.min()
        print("Servo minimum konumda")
        sleep(1)  # 1 saniye bekle
        
        # Servo motoru orta konuma (0) hareket ettir
        servo.mid()
        print("Servo orta konumda")
        sleep(1)  # 1 saniye bekle
        
        # Servo motoru maksimum konuma (+1) hareket ettir
        servo.max()
        print("Servo maksimum konumda")
        sleep(1)  # 1 saniye bekle

except KeyboardInterrupt:
    # CTRL+C basılınca döngüyü durdur
    print("Program sonlandırıldı")
