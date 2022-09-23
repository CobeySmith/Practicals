"""
More scores

Ask the user for a number of scores
Generate that many random numbers (scores) between 0 and 100 inclusive
For each of those scores, write the "result" to a file called results.txt as below:
"""

from random import randint

scores = []


def main():
    number_of_scores = get_valid_number("Number of scores: ")
    generate_scores(number_of_scores)
    save_results_to_file("results.txt")


def get_valid_number(prompt):
    """Get a valid number"""
    number = int(input(prompt))
    while number <= 0:
        print("Invalid number")
        number = int(input(prompt))
    return number


def generate_scores(number_of_scores):
    """Generate a list of scores"""
    for i in range(number_of_scores):
        score = randint(0, 100)
        scores.append(score)


def save_results_to_file(file_name):
    """Save scores and their results to a file"""
    save_file = open(file_name, "w")
    for score in scores:
        result = determine_result(score)
        save_file.write(f"{score} is {result}\n")
    save_file.close()


def determine_result(score):
    """Determine the user's result"""
    if score < 50:
        return "Bad"
    elif score >= 90:
        return "Excellent"
    return "Passable"


main()
