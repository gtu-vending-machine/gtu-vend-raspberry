import RPi.GPIO as GPIO
import time

# Define the rows and columns for the keypad
ROWS = [4, 17, 27, 22]  # Adjust GPIO pins accordingly
COLS = [18, 23, 24]     # Adjust GPIO pins accordingly

# Keypad button layout
KEYPAD = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

def setup():
    GPIO.setmode(GPIO.BCM)

    # Setup row pins as outputs
    for row in ROWS:
        GPIO.setup(row, GPIO.OUT)
        GPIO.output(row, GPIO.LOW)

    # Setup column pins as inputs with pull-up resistors
    for col in COLS:
        GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def read_keypad():
    pressed_key = None
    for row_index, row in enumerate(ROWS):
        GPIO.output(row, GPIO.HIGH)
        for col_index, col in enumerate(COLS):
            if GPIO.input(col) == GPIO.LOW:
                pressed_key = KEYPAD[row_index][col_index]
                while GPIO.input(col) == GPIO.LOW:
                    pass  # Wait for the button to be released
        GPIO.output(row, GPIO.LOW)
    return pressed_key

def main():
    setup()
    try:
        while True:
            key = read_keypad()
            if key:
                print(f"Key pressed: {key}")
            time.sleep(0.1)  # Polling interval
    except KeyboardInterrupt:
        print("Program stopped by user")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
