import requests
import threading
import time

API_URL = "https://gtu-vend-web-server.onrender.com/api/v1"
# API_URL = "http://localhost:4000/api/v1"


class Machine:
    def __init__(self, username, password):
        self.username = username
        self.name = username
        self.password = password
        self.id = None
        self.token = None
    
    def __str__(self):
        return f"Machine({self.id}, {self.username}, {self.token})"

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

machine = Machine("machine", "machine")

def approve_transaction(code):
    response = requests.put(f"{API_URL}/transactions/approve", json={"code": code}, headers=machine.get_headers())

    return response.json()

def login():
    response = requests.post(f"{API_URL}/login", json={"username": machine.username, "password": machine.password})

    return response.json()

def print_prompt():
    while True:
        print("Enter the code: ")
        time.sleep(3)


def main():
    # login
    response = login()

    print(response)

    # set machine id and token
    machine.id = response["user"]["id"]
    machine.token = response["user"]["token"]

    threading.Thread(target=print_prompt, daemon=True).start()

    # take code from the user and approve the transaction
    while True:
        code = input()
        response = approve_transaction(code)
        print(response)


if __name__ == "__main__":
    main()