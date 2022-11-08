"""Shop Calculator"""

total_price = 0
FIXED_DISCOUNT = 0.1

number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    item_price = float(input(f"Price of item {i + 1}: $"))
    total_price += item_price

if total_price > 100:
    discount_total = total_price * FIXED_DISCOUNT
    total_price -= discount_total

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
