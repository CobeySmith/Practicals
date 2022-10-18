"""
Emails - Prac 5
Estimate: 30 mins
Actual: 42 mins
"""


def main():
    name_to_email = {}
    email = input("Email: ")
    while email != "":
        if '@' not in email:
            print("Incorrect structure")
        else:
            name = extract_name(email)
            menu_choice = input(f"Is your name {name}? Y/n: ").upper()
            if menu_choice == "N":
                name = input("Name: ").title()
            name_to_email[name] = email
        email = input("Email: ")
    print_name_and_emails(name_to_email)


def print_name_and_emails(name_to_email):
    """Print the name and the corresponding email from a dictionary."""
    print("----------")
    for name, email in name_to_email.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from user email."""
    name = email.split('@')[0].title()
    return name


main()
