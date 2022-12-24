# BMI Calculator

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight/(height**2))
if bmi < 18.5:
    print(f"Your bmi is {bmi}, You are Underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your bmi is {bmi}, You have normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"Your bmi is {bmi}, You are overweight.")
elif bmi > 30 and bmi < 35:
    print(f"Your bmi is {bmi}, You are obese.")
else:
    print(f"Your bmi is {bmi}, You are clinic obese.")
