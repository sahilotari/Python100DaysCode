height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kgs: "))

# BMI Calculation

bmi = round(weight / (height * height), 2)
bmi_as_int = int(bmi)
print("Your BMI is " + str(bmi) + "\n")
