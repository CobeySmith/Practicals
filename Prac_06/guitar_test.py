"""
Testing Guitar Class
"""

from guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2020, 3.50)
    print(f"Expected 100, got: {gibson.get_age()}")
    print(f"Expected 2, got: {another_guitar.get_age()}")
    print(f"Expected False, got: {another_guitar.is_vintage()}")
    print(f"Expected True, got: {gibson.is_vintage()}")


main()
