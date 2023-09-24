import random

namesString = input("Enter the names: ")
names = namesString.split(", ")

# randNum = random.randint(0, len(names) - 1)

# print(f"{names[randNum]} will pay the bill")


print(f"{random.choice(names)} will pay the bill")

# IndexError - access out of bound index
