import RPi.GPIO as GPIO

# Keypad configuration
ROWS = [7, 11, 13, 15]
COLS = [16, 18, 22]

KEYMAP = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]


def setup_keypad():
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


def destroy():
    GPIO.cleanup()
