"""Score Menu"""


def main():
    score = get_valid_score()
    menu_choice = input("(R)esult / (S)tars / (Q)uit: ").upper()
    while menu_choice != "Q":
        if menu_choice == "R":
            result = determine_result(score)
            print(f"Your result is : {result}")
        elif menu_choice == "S":
            print_stars(score)
        else:
            print("Invalid Option")
        menu_choice = input("(R)esult / (S)tars / (Q)uit: ").upper()
    print("Thanks for coming")


def get_valid_score():
    """Get a valid score"""
    score = float(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = float(input("Score: "))
    return score


def determine_result(score):
    """Determine the user's result"""
    if score < 50:
        return "Bad"
    elif score >= 90:
        return "Excellent"
    return "Passable"


def print_stars(score):
    """Print stars"""
    print("*" * int(score))


main()
