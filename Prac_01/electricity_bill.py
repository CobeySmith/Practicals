"""Electricity Bill Calculator"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff_choice = input("Which Tariff? 11 or 13: ")
while tariff_choice != "11" and tariff_choice != "13":
    print("Invalid choice")
    tariff_choice = input("Which Tariff? 11 or 13: ")

if tariff_choice == "11":
    tariff = TARIFF_11
else:
    tariff = TARIFF_31

daily_use = float(input("Daily use in kWh: "))
billing_days = int(input("Number of billing days: "))
estimated_bill = (tariff * daily_use * billing_days)
print(f"Estimated Bill is: ${estimated_bill:.2f}")
