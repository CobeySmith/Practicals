"""
Prac 07 - Project Management
Estimate: 45 mins
Actual: 4 hours
"""

from project import Project
import datetime
from operator import attrgetter

FILENAME = "projects.txt"


def main():
    title = load_title_from_file(FILENAME)
    projects = load_data(FILENAME)
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
            display_filtered_projects(projects)
        elif menu_choice == "A":
            add_new_project(projects)
        elif menu_choice == "U":
            update_project(projects)
        else:
            print("Incorrect menu choice")
        menu_choice = input("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
                            "- (A)dd new project\n- (U)pdate project\n- (Q)uit\n>>> ").upper()
    print("Thanks for coming")


def load_title_from_file(filename):
    """Load title line from file."""
    with open(filename, "r") as in_file:
        title = in_file.readline().strip().split("\t")
    return title


def load_data(filename):
    """Load movie data from file."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def save_data(projects, title):
    """Save data to file."""
    out_file = get_valid_string("Save file name: ")
    with open(out_file, "w") as out_file:
        print("\t".join(title), file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}"
                  f"\t{project.priority}\t{project.estimate}\t{project.completion}",
                  file=out_file, end="\n")


def display_sorted_projects(projects):
    """Display completed and uncompleted projects sorted by priority."""
    completed_projects = [project for project in sorted(projects) if project.is_complete()]
    incomplete_projects = [project for project in sorted(projects) if not project.is_complete()]
    print("Incomplete Projects: ")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Completed Projects: ")
    for project in completed_projects:
        print(f"\t{project}")


def filter_projects(projects):
    """Filter projects to sort by date."""
    user_date = get_valid_date()
    for project in projects:
        project.start_date = convert_str_to_date(project.start_date)
    sorted_projects = [project for project in projects if project.start_date >= user_date]
    return sorted(sorted_projects, key=attrgetter("start_date"))


def display_filtered_projects(projects):
    """Display filtered projects."""
    filtered_projects = filter_projects(projects)
    for project in filtered_projects:
        project.start_date = convert_date_to_str(project)
        print(project)


def add_new_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project")
    name = get_valid_string("Name: ").title()
    start_date = get_valid_date()
    priority = get_valid_integer("Priority: ", 1, 10)
    cost_estimate = get_valid_cost("Cost estimate: $")
    percent_complete = get_valid_integer("Percent complete: ", 0, 100)
    new_project = Project(name, start_date, priority, cost_estimate, percent_complete)
    new_project.start_date = convert_date_to_str(new_project)
    projects.append(new_project)


def update_project(projects):
    """Update the priority and completion percentage of a project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = get_valid_integer("Project choice: ", 0, len(projects) - 1)
    print(f"{projects[project_choice]}")
    get_valid_new_value("New percentage: ", projects, project_choice, True, 0, 100)
    get_valid_new_value("New priority: ", projects, project_choice, False, 1, 10)


def get_valid_new_value(prompt, projects, project_choice, is_percentage, min_value, max_value):
    """Get a valid value to update completion percentage or priority."""
    try:
        value = int(input(prompt))
        if value < min_value or value > max_value:
            print(f"Must be between {min_value} and {max_value}")
        else:
            if is_percentage:
                projects[project_choice].completion = value
            else:
                projects[project_choice].priority = value
    except ValueError:
        pass


def get_valid_string(prompt):
    """Get a non-empty string."""
    value = input(prompt)
    while value == "":
        print("Cannot be empty")
        value = input(prompt)
    return value


def get_valid_integer(prompt, min_value, max_value):
    """Get a valid integer from the user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(prompt))
            if number < min_value or number > max_value:
                print(f"Must be between {min_value} and {max_value}")
            else:
                is_valid_input = True
        except ValueError:
            print("Must be an integer")
    return number


def get_valid_cost(prompt):
    """Get a valid cost from the user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            cost = float(input(prompt))
            if cost < 0:
                print(f"Must be >= 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Must be a float")
    return cost


def convert_date_to_str(project):
    """Convert a date object into a string."""
    return f"{project.start_date.day}/{project.start_date.month}/{project.start_date.year}"


def convert_str_to_date(date_string):
    """Convert a date string into a date object."""
    return datetime.datetime.strptime(date_string, "%d/%m/%Y").date()


def get_valid_date():
    """Get a valid date input from the user."""
    is_valid_input = False
    while not is_valid_input:
        date_string = input("Date (dd/mm/yyyy): ")
        try:
            date_value = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            is_valid_input = True
        except ValueError:
            print("Not in correct date format")
    return date_value


main()
