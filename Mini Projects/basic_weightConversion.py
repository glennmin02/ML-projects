weight = float(input("Enter weight: "))
unit = input("Is this weight in kg or pounds? (Enter 'kg' or 'pounds'): ").lower()

if unit == "kg":
    converted_weight = round(weight * 2.25,3)
    unit = "pounds"
    print(f"Your weight is {converted_weight} {unit}.")
elif unit == "pounds":
    converted_weight = round(weight / 2.25,3)
    unit = "kg"
    print(f"Your weight is {converted_weight} {unit}.")
else:
    print(f"{unit} was not valid.")

