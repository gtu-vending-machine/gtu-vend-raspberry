from lcd import lcd_init, lcd_string, lcd_byte, LCD_LINE_1, LCD_LINE_2, LCD_CMD
from keypad import setup_keypad, get_key, destroy
from machine import Machine
import time


machine = Machine("machine", "machine")

def main():

    # Initialize LCD display
    lcd_init()

       # Setup machine
    machine.setup()

    # Initialize keypad
    setup_keypad()

    # Display buffer
    code = ""

    try:
        while True:
            key = get_key()
            if key:
                if key == '*':
                    code = ""
                    lcd_string("Cleared", LCD_LINE_1)
                    lcd_string("", LCD_LINE_2)
                    time.sleep(1)
                    lcd_string("Welcome", LCD_LINE_1)
                    lcd_string("Input code", LCD_LINE_2)
                elif key == '#':
                    lcd_string("Input:", LCD_LINE_1)
                    lcd_string(code, LCD_LINE_2)
                    response = machine.approve_transaction(code)
                    print(response)
                    # if "message" in response:
                    #     lcd_string(response["message"], LCD_LINE_1)
                    #     lcd_string("", LCD_LINE_2)
                    #     time.sleep(3)
                    #     lcd_string("", LCD_LINE_1)
                    #     lcd_string("", LCD_LINE_2)
                    # else:
                    #     lcd_string("Error", LCD_LINE_1)
                    #     lcd_string("Try again", LCD_LINE_2)
                    #     time.sleep(3)
                    #     lcd_string("", LCD_LINE_1)
                    #     lcd_string("", LCD_LINE_2)
                    # result: {'id': 13, 'hasConfirmed': True, 'userId': 1, 'slot': {'stock': 20, 'id': 1, 'index': 0}, 'product': {'price': 20}}
                    if response["hasConfirmed"]:
                        lcd_string("Transaction", LCD_LINE_1)
                        lcd_string("Approved", LCD_LINE_2)
                        time.sleep(3)
                        lcd_string("", LCD_LINE_1)
                        lcd_string("", LCD_LINE_2)
                    else:
                        lcd_string("Transaction", LCD_LINE_1)
                        lcd_string("Failed", LCD_LINE_2)
                        time.sleep(3)
                        lcd_string("", LCD_LINE_1)
                        lcd_string("", LCD_LINE_2)
                    code = ""

                else:
                    if len(code) < 16:
                        code += key
                    lcd_string("Input:", LCD_LINE_1)
                    lcd_string(code, LCD_LINE_2)
            time.sleep(0.1)
    except KeyboardInterrupt:
        destroy()
        lcd_byte(0x01, LCD_CMD)

if __name__ == '__main__':
    main()
