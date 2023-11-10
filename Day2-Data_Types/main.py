# ** -> Power
# // -> Rounded Division

print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total of the bill? $"))
tip_percentage = float(input("What percentage of tip would you like to give? "))
split = int(input("How many people will split the bill? "))

tip = tip_percentage / 100 + 1

total_per_person = round(total_bill * tip / split, 2)

print(f"Each person should pay: ${total_per_person}")