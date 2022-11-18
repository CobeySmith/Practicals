from car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability: float):
        """Initialise an unreliable car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        drive_chance = randint(0, 100)
        if drive_chance >= self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            print("Didn't start, try again next time")
            return 0
