"""
Prac 07 - Guitars
"""

from prac_06.guitar import Guitar


def main():
    guitars = []
    with open("guitars.csv") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
