"""
Tests for unreliable taxi class.
"""

from unreliable_car import UnreliableCar


def main():
    c1 = UnreliableCar("Boom", 100, 10)
    print(c1)
    c1.drive(40)
    print(c1)
    c2 = UnreliableCar("c2", 50, 50)
    print(c2)


main()