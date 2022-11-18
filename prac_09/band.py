
from musician import Musician


class Band:
    def __init__(self, name: str):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} ({', '.join([str(musician) for musician in self.musicians])})"

    def play(self):
        for musician in self.musicians:
            musician.play()
