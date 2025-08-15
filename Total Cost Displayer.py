no_of_item = float(input(f"Please enter the amount of your item: "))
price = float(input(f"Please enter the price of the item: "))

total_cost = no_of_item * price

print(f"The total cost is Rs.{total_cost: >10,.2f}.")
#format specifiers = {value : flags}
#format specifiers are used to format a value output based on the flags