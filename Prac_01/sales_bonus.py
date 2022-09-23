"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

MINIMUM_BONUS = 0.1
MAXIMUM_BONUS = 0.15
BONUS_THRESHOLD = 1000

sales = float(input("Enter sales: $"))
while sales > 0:
    if sales < BONUS_THRESHOLD:
        bonus = sales * MINIMUM_BONUS
    else:
        bonus = sales * MAXIMUM_BONUS
    print(f"Your bonus for ${sales:.2f} sales is ${bonus:.2f}")
    sales = float(input("Enter sales: $"))
print("Thanks for coming")
