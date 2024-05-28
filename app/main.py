from lcd import lcd_init, lcd_string, lcd_byte, LCD_LINE_1, LCD_LINE_2, LCD_CMD
from keypad import setup_keypad, get_key, destroy
from machine import Machine, machine_setup
import time


machine = Machine("machine", "machine")


def main():

    # Initialize LCD display
    lcd_init()

       # Setup machine
    machine_setup(machine)

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
