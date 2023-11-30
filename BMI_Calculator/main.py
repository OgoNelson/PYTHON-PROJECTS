#A welcome statement
print("I'm your BMI calculator")

#Taking inputs from the user
height = float(input("Enter your height in meters\n"))
weight = int(input("Enter your weight in kilogram\n"))

#calculating the BMI
bmi = weight / (height * height)

#conditions that help to classify their BMI
if bmi < 18.5:
    print(f"Your BMI is {round(bmi, 2)}, you are underweight.")
elif bmi >= 18.5 and bmi <= 24.9:
    print(f"Your BMI is {round(bmi, 2)}, you have a normal weight.")
elif bmi > 24.9 and bmi <= 29.9:
    print(f"Your BMI is {round(bmi, 2)}, you are overweight.")
elif bmi > 29.9 and bmi <= 34.9:
    print(f"Your BMI is {round(bmi, 2)}, you are obese I.")
elif bmi > 34.9 and bmi <= 39.9:
    print(f"Your BMI is {round(bmi, 2)}, you are obese II.")
else:
    print(f"Your BMI is {round(bmi, 2)}, you are morbidly obese1.")