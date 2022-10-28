"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""


def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = get_valid_denominator()
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    # except ZeroDivisionError:
    #     print("Cannot divide by zero!")
    print("Finished.")


def get_valid_denominator():
    """Get a denominator that is not zero."""
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0")
        denominator = int(input("Enter the denominator: "))
    return denominator


main()

"""
1. If anything other than an integer is entered after numerator and denominator inputs.
2. If a zero is entered as the denominator.
3. You could add an error-checking loop to make sure denominator != 0
"""
