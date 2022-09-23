"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

name = input("Name: ")
menu_choice = input("(H)ello / (G)oodbye , (Q)uit: ").upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print(f"Hello {name}")
    elif menu_choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid Option")
    menu_choice = input("(H)ello / (G)oodbye , (Q)uit: ").upper()
print("Finished")
