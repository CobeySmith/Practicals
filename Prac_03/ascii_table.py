"""ASCII Table"""

from random import randint

LOWER = 33
UPPER = 127
MIN_COLUMNS = 2
MAX_COLUMNS = 10
INVALID_MESSAGE = "Invalid"
ASCII_TABLE_REQUIRED = True


def main():
    string_character = input("Enter a character: ")
    while len(string_character) != 1:
        print(INVALID_MESSAGE)
        string_character = input("Enter a character: ")
    print(f"The ASCII code for {string_character} is {ord(string_character)}")
    number = get_valid_number()
    print(f"The character for {number} is: {chr(number)}")
    if ASCII_TABLE_REQUIRED:
        number_of_columns = get_valid_number_of_columns("How many columns? ")
        while number_of_columns < MIN_COLUMNS or number_of_columns > MAX_COLUMNS:
            print(INVALID_MESSAGE)
            number_of_columns = get_valid_number_of_columns("How many columns? ")
        number_of_values = (UPPER - LOWER) + 1
        number_of_rows = number_of_values // number_of_columns
        value = LOWER
        for i in range(number_of_rows):
            for j in range(number_of_columns):
                print(f"{value:3} {chr(value)}", end=" ")
                value += 1
            print()
        leftover_value = number_of_values % number_of_columns
        if leftover_value > 0:
            for i in range(UPPER - leftover_value, UPPER - 1):
                print(f"{value:3} {chr(value)}", end=" ")
                value += 1


def get_valid_number_of_columns(prompt):
    """Get a valid number of columns."""
    try:
        value = int(input(prompt))
    except ValueError:
        print(INVALID_MESSAGE)
        value = randint(MIN_COLUMNS, MAX_COLUMNS)
    return value


def get_valid_number():
    """Get a valid number."""
    try:
        number = int(input("Enter a number between 33 and 127: "))
    except ValueError:
        print(INVALID_MESSAGE)
        number = randint(LOWER, UPPER)
    if number < LOWER or number > UPPER:
        print(INVALID_MESSAGE)
        number = randint(LOWER, UPPER)
    return number


main()
