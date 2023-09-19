height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kgs: "))

# BMI Calculation

bmi = round(weight / (height * height), 2)

print("Your BMI is " + str(bmi) + "\n")

if bmi < 18.5:
    print("You are underweight!")
elif bmi < 25:
    print("You have normal weight!")
elif bmi < 30:
    print("You are overweight!")
elif bmi < 35:
    print("You are obese!")
else:
    print("You are clinically obese!")
