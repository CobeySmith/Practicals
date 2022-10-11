"""
Name: Cobey Smith
Date started: 11.10.2022
GitHub URL: https://github.com/CobeySmith/Practicals

Users can choose to see the list of movies, which should be sorted by year then by title.
Users can add new movies and mark movies as watched.
Users cannot change movies from watched to unwatched.
"""


def main():
    """..."""
    print("Movies To Watch 1.0 - by Cobey Smith")
    menu_choice = input("(D)isplay, (A)dd, (W)atch, (Q)uit: ").upper()
    while menu_choice != "Q":
        if menu_choice == "D":
            print("Display choice")
        elif menu_choice == "A":
            print("Add choice")
        elif menu_choice == "W":
            print("Watch choice")
        menu_choice = input("(D)isplay, (A)dd, (W)atch, (Q)uit: ").upper()
    print("Thanks for coming")


if __name__ == '__main__':
    main()
