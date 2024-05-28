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
def first_line():
    global loading
    while True:
        if not loading:
            lcd_string("Input:", LCD_LINE_1)
            time.sleep(0.1)
        else:
            lcd_string("Loading...", LCD_LINE_1)
            time.sleep(0.1)

# second line thread
def second_line():
    global code
    while True:
        lcd_string(code, LCD_LINE_2)
        time.sleep(0.1)

# main function
def main():

    # Initialize LCD display
    lcd_init()

       # Setup machine
    machine.setup()

    # Initialize keypad
    setup_keypad()

    # Start first line thread
    t1 = threading.Thread(target=first_line)
    t1.start()

    # Start second line thread
    t2 = threading.Thread(target=second_line)
    t2.start()

    try:
        while True:
            key = get_key()
            if key == "#":
                global loading
                loading = True
                machine.run(code)
                loading = False
                code = ""
            elif key == "*":
                code = ""
            elif key != None:
                code += key
            time.sleep(0.1)
    except KeyboardInterrupt:
        destroy()
        machine.cleanup()
        t1.join()
        t2.join()


if __name__ == '__main__':
    main()
