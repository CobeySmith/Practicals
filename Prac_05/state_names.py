"""
CP1404/CP5632 Practical
State names in a dictionary
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

max_code_length = max(list(len(pair) for pair in CODE_TO_NAME.keys()))
max_name_length = max(list(len(pair) for pair in CODE_TO_NAME.values()))

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code:{max_code_length}} is {CODE_TO_NAME[state_code]:{max_name_length}}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

for state_code, name in CODE_TO_NAME.items():
    print(f"{state_code:{max_code_length}} is {CODE_TO_NAME[state_code]:{max_name_length}}")
