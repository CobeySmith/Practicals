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
    if guitars:
        print("\nThese are my guitars:")
        # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
        # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
        for i, guitar in enumerate(guitars, 1):
            vintage_string = "(Vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
    else:
        print("No guitars :(")


def get_valid_number(prompt, value_type):
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
