from lcd import lcd_init, lcd_string, lcd_byte, LCD_LINE_1, LCD_LINE_2, LCD_CMD
from keypad import setup_keypad, get_key, destroy
from machine import Machine
import time


machine = Machine("machine", "machine")

def welcome():
    lcd_string("Welcome", LCD_LINE_1)
    lcd_string("Input the code", LCD_LINE_2)

def main():

    # Initialize LCD display
    lcd_init()

       # Setup machine
    machine.setup()

    # Initialize keypad
    setup_keypad()

    # Display buffer
    code = ""

    welcome()

    try:
        while True:
            key = get_key()
            if key:
                if key == '*':
                    code = ""
                    lcd_string("Cleared", LCD_LINE_1)
                    lcd_string("", LCD_LINE_2)
                    time.sleep(1)
                    welcome()
                elif key == '#':
                    lcd_string("Processing...", LCD_LINE_1)
                    lcd_string(code, LCD_LINE_2)
                    response = machine.approve_transaction(code)
                    # if there is not response, print error to display
                    if "hasConfirmed" in response:
                        lcd_string("Transaction", LCD_LINE_1)
                        lcd_string("Approved", LCD_LINE_2)
                        time.sleep(3)
                        welcome()
                    else:
                        lcd_string("Transaction", LCD_LINE_1)
                        lcd_string("Failed", LCD_LINE_2)
                        time.sleep(3)
                        welcome()
                    code = ""
                else:
                    if len(code) < 8:
                        code += key
                    lcd_string("Input:", LCD_LINE_1)
                    lcd_string(code, LCD_LINE_2)
            time.sleep(0.1)
    except KeyboardInterrupt:
        destroy()
        lcd_byte(0x01, LCD_CMD)

if __name__ == '__main__':
    main()
