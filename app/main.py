from lcd import lcd_init, lcd_string, lcd_byte, LCD_LINE_1, LCD_LINE_2, LCD_CMD
from keypad import setup_keypad, get_key, destroy
from machine import Machine
import threading
import time


machine = Machine("machine", "machine")

loading = False

# code being entered by the user
code = ""
        
# first line thread
def print_prompt():
    # if loading is true, otherwise, print "enter the code"
    while True:
        if loading:
            lcd_string("Loading...", LCD_LINE_1)
            lcd_string("", LCD_LINE_2)
        else:
            lcd_string("Enter the code:", LCD_LINE_1)
            lcd_string("", LCD_LINE_2)
        time.sleep(0.5)

# second line thread
def print_code():
    # print the code being entered by the user
    while True:
        lcd_string(code, LCD_LINE_2)
        time.sleep(0.1)


def main():

    # Initialize LCD display
    lcd_init()

       # Setup machine
    machine.setup()

    # Initialize keypad
    setup_keypad()

    
    # try:
    #     while True:
    #         key = get_key()
    #         if key:
    #             # Clear display if '*' is pressed
    #             if key == '*':
    #                 code = ""
    #                 lcd_string("Cleared", LCD_LINE_1)
    #                 lcd_string("", LCD_LINE_2)
    #             # Confirm display if '#' is pressed
    #             elif key == '#':
    #                 lcd_string("Input:", LCD_LINE_1)
    #                 lcd_string(code, LCD_LINE_2)
    #             else:
    #                 if len(code) < 16:  # Ensure it fits on one line
    #                     code += key
    #                 lcd_string("Input:", LCD_LINE_1)
    #                 lcd_string(code, LCD_LINE_2)
    #         time.sleep(0.1)
    # except KeyboardInterrupt:
    #     destroy()
    #     lcd_byte(0x01, LCD_CMD)  # Clear display

    # start the first line thread
    threading.Thread(target=print_prompt, daemon=True).start()
    # start the second line thread
    threading.Thread(target=print_code, daemon=True).start()

    try:
        while True:
            key = get_key()
            if key:
                # Clear display if '*' is pressed
                if key == '*':
                    code = ""
                    lcd_string("Cleared", LCD_LINE_1)
                    lcd_string("", LCD_LINE_2)
                # Confirm display if '#' is pressed
                elif key == '#':
                    loading = True
                    machine.approve_transaction(code)
                    loading = False
                    code = ""
                    lcd_string("Transaction", LCD_LINE_1)
                    lcd_string("Approved", LCD_LINE_2)
                    time.sleep(3)
                else:
                    if len(code) < 16:  # Ensure it fits on one line
                        code += key
                    lcd_string("Input:", LCD_LINE_1)
                    lcd_string(code, LCD_LINE_2)
            time.sleep(0.1)
    except KeyboardInterrupt:
        destroy()
        lcd_byte(0x01, LCD_CMD)
        # Clear display
        lcd_string("Goodbye", LCD_LINE_1)
        time.sleep(2)
        lcd_byte(0x01, LCD_CMD)
        # Clear display
        lcd_string("", LCD_LINE_1)
        lcd_string("", LCD_LINE_2)
        exit(0)

if __name__ == '__main__':
    main()
