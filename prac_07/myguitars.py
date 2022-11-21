"""
Prac 07 - Guitars
"""

from prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read file, add user guitars, display sorted list, save to file."""
    guitars = load_guitars()
    get_new_guitars(guitars)
    guitars.sort()
    display_guitars(guitars)
    save_guitars(guitars)


def save_guitars(guitars):
    """Save guitars to file."""
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def display_guitars(guitars):
    """Display formatted guitars."""
    print("\nGuitars:")
    for guitar in guitars:
        print(guitar)


def get_new_guitars(guitars):
    """Add new user guitars to guitars list."""
    name = input("Name: ")
    while name != "":
        year = get_valid_number("Year: ", int)
        cost = get_valid_number("Cost: ", float)
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print("-----")
        name = input("Name: ")


def load_guitars():
    """Load guitars from file."""
    guitars = []
    with open(FILENAME) as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def get_valid_number(prompt, value_type):
    """Get a valid number from user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = value_type(input(prompt))
            if number <= 0:
                print("Must be > 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Must be a number")
    return number


main()
