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
        lcd_string("Loading..." if loading else "Enter the code:", LCD_LINE_1)
        time.sleep(0.1)

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

    
    # start the first line thread
    threading.Thread(target=print_prompt, daemon=True).start()
    # start the second line thread
    threading.Thread(target=print_code, daemon=True).start()

    # take code from the user and approve the transaction
    try:
        while True:
            key = get_key()
            if key == "#":
                # if the user presses #, approve the transaction
                loading = True
                response = machine.approve_transaction(code)
                loading = False
                code = ""
                lcd_string(response["message"], LCD_LINE_1)
                time.sleep(3)
            elif key == "*":
                # if the user presses *, clear the code
                code = ""
            else:
                # add the key to the code
                code += key
    except KeyboardInterrupt:
        destroy()
        print("Exiting...")
        exit(0)


   


if __name__ == '__main__':
    main()
