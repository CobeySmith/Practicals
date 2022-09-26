"""Covert Temperatures"""

input_file = "temps_input.txt"


# def main():
#     fahrenheit_values = open(input_file, "r")
#     fahrenheit_values.read())
#     save_results_to_file("temps_output.txt", fahrenheit_values)
#
#
# def get_fahrenheit_values():
#     input_file = open(input_file, "r")
#     fahrenheit_values.read())

def save_results_to_file(file_name, fahrenheit_values):
    """Save scores and their results to a file"""
    output_file = open(file_name, "w")
    for fahrenheit_value in fahrenheit_values:
        celsius_value = convert_to_celsius(fahrenheit_value)
        output_file.write(f"{celsius_value}\n")
    output_file.close()


def convert_to_fahrenheit(celsius):
    """covert celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32


def convert_to_celsius(fahrenheit_values):
    """convert fahrenheit to celsius"""
    return 5 / 9 * (fahrenheit_values - 32)


main()
