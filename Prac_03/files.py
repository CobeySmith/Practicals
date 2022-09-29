"""Files"""


def main():
    # Question 1
    name = input("Name: ")
    with open("name.txt", "w") as outfile:
        outfile.write(name)

    # Question 2
    with open("name.txt", "r") as infile:
        name = infile.read().strip()
    print(f"Your name is {name}")

    # Question 3
    with open("numbers.txt", "r") as infile:
        first_number = get_valid_number(infile)
        second_number = get_valid_number(infile)
    total = first_number + second_number
    print(f"The total is: {total}")

    # Question 4
    with open("numbers.txt", "r") as infile:
        error_line_numbers = []
        total = 0
        for line_number, line in enumerate(infile, 1):
            try:
                number = float(line)
                total += number
            except ValueError:
                error_line_numbers.append(line_number)
    error_line_numbers = ", ".join([str(number) for number in error_line_numbers])
    print(f"These lines have errors: {error_line_numbers}")
    print(f"The total is: {total}")


def get_valid_number(infile):
    """Gets a valid number."""
    try:
        number = float(infile.readline())
        return number
    except ValueError:
        return 0


main()
