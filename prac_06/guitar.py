"""
Prac 06 - Guitars Prac
Estimate: 30 mins
Actual: 28 mins
"""


class Guitar:
    """Define a guitar"""

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}): ${self.cost:.2f}"

    def __repr__(self):
        return f"{self.name}, {self.year}, {self.cost:.2f}"

    def get_age(self):
        return 2022 - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self, other):
        return self.year < other.year
