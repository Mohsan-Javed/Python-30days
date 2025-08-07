weight = float(input(f"Enter your weight: "))
unit = input(f"Enter the unit (K for Kilograms or L for Pounds): ")

unit = unit.lower()

if unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight, 2)} {unit}")
elif unit == "l":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is {round(weight, 2)} {unit}")
else:
    print(f"{unit} is not a valid unit")
# lower() function is to lower the string input
# float() function works same as int()