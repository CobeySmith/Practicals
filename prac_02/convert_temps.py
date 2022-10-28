"""Covert Temperatures"""


def main():
    infile = open("temps_input.txt", "r")
    outfile = open("results.txt", "w")
    for line in infile:
        fahrenheit_value = float(line.strip())
        celsius_value = convert_to_celsius(fahrenheit_value)
        outfile.write(f"{celsius_value}\n")
    infile.close()
    outfile.close()


def convert_to_celsius(fahrenheit_value):
    """Convert from fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit_value - 32)


main()
