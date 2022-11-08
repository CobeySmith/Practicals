"""
Gopher Population Simulator
Every year, a random number of gophers is born, between 10% of the current population, and 20%.
Also, each year a random number of gophers die, between 5% and 25%.
"""

from random import randint

STARTING_POPULATION = 1000
NUMBER_OF_YEARS = 10


def main():
    count = 1
    population = STARTING_POPULATION
    print(f"Welcome to the Gopher Population Simulator!\nThe Starting Population: {STARTING_POPULATION}\n")
    for i in range(NUMBER_OF_YEARS):
        print(f"Year {count}")
        number_of_births = simulate_births(population)
        number_of_deaths = simulate_deaths(population)
        print(f"{number_of_births} were born. {number_of_deaths} died.")
        population = calculate_population(population, number_of_births, number_of_deaths)
        if population <= 0:
            print("Everyone has died :(")
            break
        else:
            print(f"Population: {population}\n")
            count += 1


def calculate_population(population, number_of_births, number_of_deaths):
    """Calculate population after total deaths and births."""
    population += number_of_births
    population -= number_of_deaths
    return population


def simulate_births(population):
    """Simulate a random number of births."""
    return randint(int(population * 0.1), int(population * 0.2))


def simulate_deaths(population):
    """Simulate a random number of deaths."""
    plague_chance = randint(1, 100)
    if plague_chance >= 95:
        print("Plague")
        return randint(int(population * 0.5), int(population * 0.9))
    return randint(int(population * 0.05), int(population * 0.25))


main()
