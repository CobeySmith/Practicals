from taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, fanciness: float, **kwargs):
        price_per_km = 1.23
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km = price_per_km * self.fanciness
        self.flagfall = 4.50

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super(SilverServiceTaxi, self).get_fare() + self.flagfall

    def __str__(self):
        return f"{super().__str__()} plus flagfall of %{self.flagfall}"
