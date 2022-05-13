import socket

# import typing as tp

from logo import LOGO

HOST, PORT = "localhost", 9999


def make_request(data: str) -> str:
    if not data.endswith("\n"):
        data += "\n"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(data.encode(encoding="utf-8"))
    response_bytes = s.recv(10240)
    return response_bytes.decode(encoding="utf-8")


# def dummy_handler():
#     print("Whoopsie")


# HANDLERS: tp.List[tp.Callable] = [
#     dummy_handler,
#     dummy_handler,
#     dummy_handler,
# ]


if __name__ == "__main__":
    print(LOGO)
    print("Welcome to the SmartLocks!")

    while True:
        # print("What do you want to do?")
        # print("  1. Find empty locker")
        # print("  2. Lock the locker and set passcode")
        # print("  3. Unlock the locker with passcode")
        # print("  4. Exit")

        # choice = int(input("1-4 > "))
        # if not 1 <= choice <= 4:
        #     print("Please enter number 1, 2, 3, or 4")
        #     continue

        # if choice == 4:
        #     print("Thank you for using SmartLocks!")
        #     break

        # HANDLERS[choice - 1]()

        # -----
        # DEBUG VERSION
        # -----
        print("\n\n### THIS IS DEBUG PANEL, REMOVE IN PRODUCTION ###")
        print(
            "Enter command to send to the server,",
            "or 'exit' to exit the panel\n",
            sep="\n",
        )
        command = input()

        if command != "exit":
            print(f"REQUEST: '{command}'")
            response = make_request(command)
            print(f"RESPONSE: '{response.strip()}'")
        else:
            break
