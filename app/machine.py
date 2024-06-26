import requests
from lcd import lcd_string, LCD_LINE_1, LCD_LINE_2
import time


API_URL = "https://gtu-vend-web-server.onrender.com/api/v1"
# API_URL = "http://192.168.61.189:4000/api/v1"


class Machine:
    def __init__(self, username, password, id):
        self.username = username
        self.name = username
        self.password = password
        self.id = id
        self.token = None

    def __str__(self):
        return f"Machine({self.id}, {self.username}, {self.token})"

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
        }

    def approve_transaction(self, code):
        print("code: ", code)
        print("id: ", self.id)
        response = requests.put(
            f"{API_URL}/transactions/approve",
            json={"code": code, "vendingMachineId": self.id},
            headers=self.get_headers(),
        )

        return response.json()

    def login(self):
        response = requests.post(
            f"{API_URL}/login",
            json={"username": self.username, "password": self.password},
        )

        return response.json()

    def setup(self):
        # login
        response = self.login()

        print(response)

        # if response is not, print error to display
        if "user" not in response:
            # lcd_string("Login failed", LCD_LINE_1)
            # lcd_string("Check credentials", LCD_LINE_2)
            while True:
                lcd_string("Login failed", LCD_LINE_1)
                lcd_string("Check credentials", LCD_LINE_2)
        else:
            # set machine id and token
            # self.id = response["user"]["id"]
            self.token = response["user"]["token"]
            # show success message for 3 seconds
            lcd_string("Login successful", LCD_LINE_1)
            lcd_string("Welcome", LCD_LINE_2)
            time.sleep(3)
            lcd_string("", LCD_LINE_1)
            lcd_string("", LCD_LINE_2)
