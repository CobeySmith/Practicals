"""Quick picks"""

from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBER_OF_LINES = 6


def main():
    try:
        number_of_quick_picks = int(input("How many quick picks: "))
    except ValueError:
        number_of_quick_picks = randint(1, 10)
        print(f"Must be an integer so here's one i prepared earlier: {number_of_quick_picks}")
    while number_of_quick_picks <= 0:
        print("Can't have zero, try again")
        number_of_quick_picks = int(input("How many quick picks: "))

    generate_quick_picks(number_of_quick_picks)


def generate_quick_picks(number_of_quick_picks):
    """Generate the quick picks."""
    for i in range(number_of_quick_picks):
        numbers = []
        for j in range(NUMBER_OF_LINES):
            number = randint(MIN_NUMBER, MAX_NUMBER)
            while number in numbers:
                number = randint(MIN_NUMBER, MAX_NUMBER)
            numbers.append(number)
        numbers.sort()
        print(" ".join(f"{number:2}" for number in numbers))


main()
