"""
Prac 06 - Guitars prac
"""

from guitar import Guitar


def main():
    guitars = []
    name = input("Name: ")
    while name != "":
        year = get_valid_number("Year: ", int)
        cost = get_valid_number("Cost: ", float)
        guitars.append(Guitar(name, year, cost))
        print("-----")
        name = input("Name: ")
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


def get_valid_number(prompt, value_type):
    try:
        number = value_type(input(prompt))
        while number <= 0:
            print("Must be > 0")
    except ValueError:
        print("Must be a number")
    return number


main()
