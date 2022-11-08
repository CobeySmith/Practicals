"""
Prac 07 - Project Management
Estimate: 45 mins
Actual:
"""

from project import Project
import datetime

FILENAME = "projects.txt"


def main():
    projects = load_data(FILENAME)
    menu_choice = input("Menu Choice: ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            print(projects)
            filename = input("Filename: ")
            projects = load_data(filename)
        elif menu_choice == "S":
            save_data(projects)
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            print("Filter")
        elif menu_choice == "A":
            print("Add")
        elif menu_choice == "U":
            print("Update")
        else:
            print("Incorrect menu choice")
        menu_choice = input("Menu Choice: ").upper()
    print("Thanks for coming")


def save_data(projects):
    out_file = input("Save file name: ")
    with open(out_file, "w") as out_file:
        for project in projects:
            print(f"{project}", file=out_file, end="\n")


def load_data(filename):
    """Get movie data from file."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            date_string = parts[1]
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            project = Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def display_projects(projects):
    completed_projects = [project for project in projects if project.is_complete()]
    incomplete_projects = [project for project in projects if not project.is_complete()]
    print("Incomplete Projects: ")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Completed Projects: ")
    for project in completed_projects:
        print(f"\t{project}")


main()
