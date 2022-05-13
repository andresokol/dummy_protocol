import typing as tp

from logo import LOGO


def dummy_handler():
    print("Whoopsie")


HANDLERS: tp.List[tp.Callable] = [
    dummy_handler,
    dummy_handler,
    dummy_handler,
]


if __name__ == "__main__":
    print(LOGO)
    print("Welcome to the SmartLocks!")

    while True:
        print("What do you want to do?")
        print("  1. Find empty locker")
        print("  2. Lock the locker and set passcode")
        print("  3. Unlock the locker with passcode")
        print("  4. Exit")

        choice = int(input("1-4 > "))
        if not 1 <= choice <= 4:
            print("Please enter number 1, 2, 3, or 4")
            continue

        if choice == 4:
            print("Thank you for using SmartLocks!")
            break

        HANDLERS[choice]()
