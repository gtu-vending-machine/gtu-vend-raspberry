import smbus
import time
import RPi.GPIO as GPIO

# LCD Display configuration
I2C_ADDR = 0x27  # I2C device address
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1  # Mode - Sending data
LCD_CMD = 0  # Mode - Sending command

LCD_LINE_1 = 0x80  # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  # LCD RAM address for the 2nd line

LCD_BACKLIGHT = 0x08  # On
ENABLE = 0b00000100  # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

# Open I2C interface
bus = smbus.SMBus(1)

def lcd_init():
    # Initialise display
    lcd_byte(0x33, LCD_CMD)  # 110011 Initialise
    lcd_byte(0x32, LCD_CMD)  # 110010 Initialise
    lcd_byte(0x06, LCD_CMD)  # 000110 Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # 001100 Display On,Cursor Off, Blink Off
    lcd_byte(0x28, LCD_CMD)  # 101000 Data length, number of lines, font size
    lcd_byte(0x01, LCD_CMD)  # 000001 Clear display
    time.sleep(E_DELAY)

def lcd_byte(bits, mode):
    # Send byte to data pins
    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT

    # High bits
    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)

    # Low bits
    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    # Toggle enable
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
    time.sleep(E_DELAY)

def lcd_string(message, line):
    # Send string to display
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, LCD_CMD)
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

# Keypad configuration
ROWS = [7, 13, 15, 29]
COLS = [16, 18, 22]

KEYMAP = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

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

def main():
    # Initialize LCD display
    lcd_init()

    # Initialize keypad
    setup_keypad()

    # Display buffer
    display_buffer = ""

    try:
        while True:
            key = get_key()
            if key:
                # Clear display if '*' is pressed
                if key == '*':
                    display_buffer = ""
                    lcd_string("Cleared", LCD_LINE_1)
                    lcd_string("", LCD_LINE_2)
                # Confirm display if '#' is pressed
                elif key == '#':
                    lcd_string("Input:", LCD_LINE_1)
                    lcd_string(display_buffer, LCD_LINE_2)
                else:
                    if len(display_buffer) < 16:  # Ensure it fits on one line
                        display_buffer += key
                    lcd_string("Input:", LCD_LINE_1)
                    lcd_string(display_buffer, LCD_LINE_2)
            time.sleep(0.1)
    except KeyboardInterrupt:
        destroy()
        lcd_byte(0x01, LCD_CMD)  # Clear display

if __name__ == '__main__':
    main()
