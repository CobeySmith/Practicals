"""Score"""


def main():
    score = get_valid_score()
    result = determine_result(score)
    print(f"Your result is: {result} ")


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


main()
