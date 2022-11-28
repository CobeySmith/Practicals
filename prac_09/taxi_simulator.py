"""
Taxi Simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

INPUT_STRING = "q)uit, c)hoose taxi, d)rive\n>>> "


def main():
    taxis = [Taxi(name="Prius", fuel=100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    print("Let's drive!")
    user_input = input(INPUT_STRING).upper()
    current_taxi = None
    total_cost = 0
    while user_input != "Q":
        if user_input == "C":
            display_taxis(taxis)
            taxi_choice = get_valid_number("Choose taxi: ")
            current_taxi = taxis[taxi_choice]
        elif user_input == "D":
            if not current_taxi:
                print("You need to choose a taxi before you can drive")
            else:
                drive_cost = determine_taxi_cost(current_taxi)
                total_cost += drive_cost
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_cost}")
        user_input = input(INPUT_STRING).upper()
    print(f"Total trip cost: ${total_cost}")
    print("Taxis are now:")
    display_taxis(taxis)


def determine_taxi_cost(current_taxi):
    """Determine the cost of a trip after drive a certain distance."""
    drive_distance = get_valid_number("Drive how far? ")
    current_taxi.drive(drive_distance)
    drive_cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${drive_cost}")
    return drive_cost


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_number(prompt):
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(prompt))
            if number < 0:
                print("Number must be >= 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid (not an integer)")
    return number


main()


