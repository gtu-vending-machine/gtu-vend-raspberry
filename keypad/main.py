import RPi.GPIO as GPIO
import time

# Updated GPIO pin numbers
ROWS = [7, 13, 15, 29]
COLS = [16, 18, 22]

# Updated keymap
KEYMAP = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ROWS, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(COLS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def get_key():
    key = None
    for i in range(len(ROWS)):
        GPIO.output(ROWS[i], GPIO.LOW)
        for j in range(len(COLS)):
            if GPIO.input(COLS[j]) == GPIO.LOW:
                key = KEYMAP[i][j]
                while GPIO.input(COLS[j]) == GPIO.LOW:
                    pass
        GPIO.output(ROWS[i], GPIO.HIGH)
    return key

def loop():
    while True:
        key = get_key()
        if key:
            print(key)
        time.sleep(0.1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
