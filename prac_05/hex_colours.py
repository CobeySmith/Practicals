"""
Hex Colours
Prac 5 Exercise
"""

COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Amethyst": "#9966cc", "Aqua": "#00ffff", "Aureolin": "#fdee00",
                  "Patriarch": "#800080", "Portland Orange": "#ff5a36", "Tropical Rainforest": "#00755e",
                  "Up Maroon": "#7b1113", "Wheat": "#f5deb3", "White Smoke": "#f5f5f5"}


def main():
    max_code_length = max(len(pair) for pair in COLOUR_TO_CODE.values())
    max_name_length = max(len(pair) for pair in COLOUR_TO_CODE.keys())

    colour_name = input("Colour Name: ").title()
    while colour_name != "":
        try:
            print(f"{colour_name:{max_code_length}} is {COLOUR_TO_CODE[colour_name]:{max_name_length}}")
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Colour Name: ").title()


main()
