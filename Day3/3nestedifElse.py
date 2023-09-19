height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    if age > 18:
        print("You have to pay $12\n")
    if age > 12:
        print("You have to pay $7\n")
    else:
        print("You have to pay $5\n")
else:
    print("You cant ride, your height is below 120cm.!\n")
