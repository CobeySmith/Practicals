"""Password Stars"""

MINIMUM_LENGTH = 8


def main():
    user_password = get_valid_password()
    print_asterisks(user_password)


def get_valid_password():
    """Get a valid password length"""
    user_password = input("Password: ")
    while len(user_password) < MINIMUM_LENGTH:
        print("Error")
        user_password = input("Password: ")
    return user_password


def print_asterisks(user_password):
    """Print asterisks to length of password"""
    print("*" * len(user_password))


main()
