print("Welcome to tip calculator!")
totalBill = float(input("What was the total bill? $"))
tipPercentage = float(input("What percentage of tip would you give? "))
people = int(input("How many people to split the bill? "))

amount = round((totalBill + totalBill * tipPercentage / 100) / people, 2)

print(f"Each person should pay: ${amount}")
