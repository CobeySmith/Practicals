"""Sequences"""

x_input = int(input("X input: "))
y_input = int(input("Y input: "))
while y_input < x_input:
    print("X must be lower than Y")
    y_input = int(input("Y input: "))

menu_choice = input("(E)ven / (O)dd / (S)quares / (Q)uit: ").upper()
while menu_choice != "Q":
    if menu_choice == "E":
        if x_input % 2 == 0:
            for i in range(x_input, y_input + 1, 2):
                print(i, end=" ")
            print()
        else:
            for i in range(x_input + 1, y_input + 1, 2):
                print(i, end=" ")
            print()
    elif menu_choice == "O":
        if x_input % 2 == 0:
            for i in range(x_input + 1, y_input + 1, 2):
                print(i, end=" ")
            print()
        else:
            for i in range(x_input, y_input + 1, 2):
                print(i, end=" ")
            print()
    elif menu_choice == "S":
        for i in range(x_input, y_input + 1):
            print(i * i, end=" ")
        print()
    else:
        print("Invalid option")
    menu_choice = input("(E)ven / (O)dd / (S)quares / (Q)uit: ").upper()
print("Bye Bye")
