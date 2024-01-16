height = float(input("What is your height in meters? "))
weight = int(input("What is your weight in Kg? "))

BMI = (weight / height ** 2)

# It should tell them the clinical interpretation of their BMI based on the clinical BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese.

if BMI < 18.5:
    print(f"Your BMI is {round(BMI, 2)}, you are underweight.")
elif BMI < 25.0:
    print(f"Your BMI is {round(BMI, 2)}, you have a normal weight.")
elif BMI == 25.0:
    print(f"Your BMI is {round(BMI, 2)}, you are slightly overweight.")
elif BMI < 30:
    print(f"Your BMI is {round(BMI, 2)}, you are obese.")
else:
    print(f"Your BMI is {round(BMI, 2)}, you are obese.")