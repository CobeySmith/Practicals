
from unreliable_car import UnreliableCar


def main():
    c1 = UnreliableCar("Boom", 100, 10)
    print(c1)
    c1.drive(40)
    print(c1)


main()