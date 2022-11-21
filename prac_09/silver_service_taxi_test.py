"""
Test code for Silver Service Taxi class.
"""


from silver_service_taxi import SilverServiceTaxi


def main():
    t1 = SilverServiceTaxi(name="Hummer", fuel=200, fanciness=2.0)
    print(t1)
    t1.drive(18)
    print(t1.get_fare())


main()
