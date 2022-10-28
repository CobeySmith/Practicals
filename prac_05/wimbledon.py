"""
Wimbledon - Prac 5
The champions and how many times they have won.
The countries of the champions in alphabetical order
Estimate: 40 mins
Actual: 46 mins
"""

FILENAME = "wimbeldon.txt"


def main():
    data = get_data_from_file()
    champions = extract_values_from_data(data, 2)
    countries = set(extract_values_from_data(data, 3))
    champion_to_wins = covert_list_to_dictionary(champions)
    print_champions(champion_to_wins)
    print(f"\nThese {len(countries)} countries have won Wimbledon:\n{', '.join(countries)}")


def get_data_from_file():
    """Get data from file."""
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip().split(",")
            data.append(line)
    return data


def extract_values_from_data(data, index):
    """Extract values from a list of data."""
    values = []
    for element in data:
        values.append(element[index])
    return values


def covert_list_to_dictionary(champions):
    """Convert a list to a dictionary."""
    champion_to_wins = {}
    for champion in champions:
        try:
            champion_to_wins[champion] += 1
        except KeyError:
            champion_to_wins[champion] = 1
    champion_to_wins = {champion: champion_to_wins[champion] for champion in sorted(champion_to_wins)}
    return champion_to_wins


def print_champions(champion_to_wins):
    """Print the champion and the corresponding wins from a dictionary."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion}: {wins}")


main()
