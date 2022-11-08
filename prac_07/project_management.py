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
    menu_choice = input("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
                        "- (A)dd new project\n- (U)pdate project\n- (Q)uit\n>>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = get_valid_string("Filename: ")
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
            add_new_project(projects)
        elif menu_choice == "U":
            update_project(projects)
        else:
            print("Incorrect menu choice")
        menu_choice = input("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
                            "- (A)dd new project\n- (U)pdate project\n- (Q)uit\n>>> ").upper()
    print("Thanks for coming")


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    print(f"{projects[project_choice]}")
    new_percentage = get_valid_integer("New percentage: ", 0, 100)
    projects[project_choice].completion = new_percentage
    new_priority = get_valid_integer("New priority: ", 1, 10)
    projects[project_choice].priority = new_priority


# def get_valid_index(prompt):


# TODO
def get_valid_value(prompt, projects, project_choice, is_percentage):
    try:
        value = int(input(prompt))
        if is_percentage:
            projects[project_choice].completion = value
        else:
            projects[project_choice].priority = value
    except ValueError:
        pass


def add_new_project(projects):
    print("Let's add a new project")
    name = get_valid_string("Name: ").title()
    start_date = get_valid_date()
    priority = get_valid_integer("Priority: ", 1, 10)
    cost_estimate = get_valid_cost("Cost estimate: $ ")
    percent_complete = get_valid_integer("Percent complete: ", 0, 100)
    new_project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(new_project)


def get_valid_integer(prompt, min_value, max_value):
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(prompt))
            if number < min_value or number > max_value:
                print(f"Must be between {min_value} and {max_value}")
            else:
                is_valid_input = True
        except ValueError:
            print("Must be a float")
    return number


def get_valid_cost(prompt):
    is_valid_input = False
    while not is_valid_input:
        try:
            cost = float(input(prompt))
            if cost < 0:
                print(f"Must be > 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Must be an integer")
    return cost


def get_valid_string(prompt):
    value = input(prompt)
    while value == "":
        print("Cannot be empty")
        value = input(prompt)
    return value


def filter_projects(projects):
    user_date = get_valid_date()
    for project in projects:
        project.start_date = convert_str_to_date(project.start_date)
    sorted_projects = [project for project in projects if project.start_date >= user_date]
    return sorted(sorted_projects, key=attrgetter("start_date"))


def convert_date_to_str(project):
    return f"{project.start_date.day}/{project.start_date.month}/{project.start_date.year}"


def convert_str_to_date(date_string):
    return datetime.datetime.strptime(date_string, "%d/%m/%Y").date()


def get_valid_date():
    is_valid_input = False
    while not is_valid_input:
        date_string = input("Date (dd/mm/yyyy): ")
        try:
            date_value = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            is_valid_input = True
        except ValueError:
            print("Not in correct date format")
    return date_value


def load_title(filename):
    with open(filename, "r") as in_file:
        title = in_file.readline().strip().split("\t")
    return title


def save_data(projects, title):
    out_file = get_valid_string("Save file name: ")
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
        print(f"\t{project}")
    print("Completed Projects: ")
    for project in completed_projects:
        print(f"\t{project}")


main()
