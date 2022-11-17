class Project:
    def __init__(self, name="", start_date="", priority=0, money_estimate=0, completion_percentage=0):
        """Initializes a project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = money_estimate
        self.completion = completion_percentage

    def __repr__(self):
        """Represents a project as a string."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate}," \
               f" completion: {self.completion}%"

    def is_complete(self):
        """Evaluates if a project is complete (returns bool)."""
        return self.completion == 100

    def __lt__(self, other):
        """Sorts projects by priority."""
        return self.priority < other.priority
