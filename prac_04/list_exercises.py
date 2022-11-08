"""List Exercises"""

from random import randint

NUMBER_OF_NUMBERS = 5


def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    numbers = get_numbers()
    print_numbers_information(numbers)
    username = input("Username: ")
    if username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


def get_numbers():
    """Get a list of numbers."""
    numbers = []
    for i in range(NUMBER_OF_NUMBERS):
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Not an integer")
            number = randint(1, 100)
            print(f"Number = {number}")
        numbers.append(number)
    return numbers


def print_numbers_information(numbers):
    """Print information about a list of numbers."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    total = 0
    for number in numbers:
        total += number
    print(f"The average is {total / len(numbers)}")


main()
