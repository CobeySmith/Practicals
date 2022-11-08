"""
Prac 07 - Project Management
Estimate: 45 mins
Actual:
"""

from project import Project
import datetime
from operator import attrgetter

FILENAME = "projects.txt"


def main():
    title = load_title(FILENAME)
    projects = load_data(FILENAME)
    # for project in projects:
    #     print(project)
    menu_choice = input("Menu Choice: ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = input("Filename: ")
            projects = load_data(filename)
        elif menu_choice == "S":
            save_data(projects, title)
        elif menu_choice == "D":
            display_sorted_projects(projects)
        elif menu_choice == "F":
            filtered_projects = filter_projects(projects)
            for project in filtered_projects:
                project.start_date = convert_date_to_str(project)
                print(project)
        elif menu_choice == "A":
            print("Let's add a new project")
            name = input("Name: ").title()
            start_date = input("Start date (dd/mm/yyyy): ")
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: $"))
            percent_complete = int(input("Percent complete: "))
            new_project = Project(name, start_date, priority, cost_estimate, percent_complete)
            projects.append(new_project)
        elif menu_choice == "U":
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project_choice = int(input("Project choice: "))
            print(f"{projects[project_choice]}")
            try:
                new_percentage = int(input("New percentage: "))
                projects[project_choice].completion = new_percentage
            except ValueError:
                pass
            try:
                new_priority = int(input("New priority: "))
                projects[project_choice].priority = new_priority
            except ValueError:
                pass
        else:
            print("Incorrect menu choice")
        menu_choice = input("Menu Choice: ").upper()
    print("Thanks for coming")


def filter_projects(projects):
    date_string = input("Date (dd/mm/yyyy): ")
    user_date = convert_str_to_date(date_string)
    for project in projects:
        project.start_date = convert_str_to_date(project.start_date)
    sorted_projects = [project for project in projects if project.start_date >= user_date]
    return sorted(sorted_projects, key=attrgetter("start_date"))


def convert_date_to_str(project):
    return f"{project.start_date.day}/{project.start_date.month}/{project.start_date.year}"


def convert_str_to_date(date_string):
    return datetime.datetime.strptime(date_string, "%d/%m/%Y").date()


def load_title(filename):
    with open(filename, "r") as in_file:
        title = in_file.readline().strip().split("\t")
    return title


def save_data(projects, title):
    out_file = input("Save file name: ")
    with open(out_file, "w") as out_file:
        print("\t".join(title), file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}"
                  f"\t{project.priority}\t{project.estimate}\t{project.completion}",
                  file=out_file, end="\n")


def load_data(filename):
    """Get movie data from file."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def display_sorted_projects(projects):
    completed_projects = [project for project in sorted(projects) if project.is_complete()]
    incomplete_projects = [project for project in sorted(projects) if not project.is_complete()]
    print("Incomplete Projects: ")
    for project in incomplete_projects:
        # project.start_date = convert_date_to_str(project)
        print(f"\t{project}")
    print("Completed Projects: ")
    for project in completed_projects:
        # project.start_date = convert_date_to_str(project)
        print(f"\t{project}")


main()
