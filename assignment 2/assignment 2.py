UNDERWEIGHT_BMI = 18.5
NORMAL_BMI = 24.9
OVERWEIGHT_BMI = 29.9


print("Please Enter your name")
name = input()

weight_pounds = float(input("Enter your weight in pounds: "))

height_feet = int(input("Enter your height in feet: "))
height_inches = int(input("Enter any additional inches: "))

height_inches = (height_feet * 12) + height_inches

bmi = (weight_pounds / (height_inches * height_inches)) * 703


bmi = round(bmi, 1)

print("Your BMI is:", bmi)

if bmi < UNDERWEIGHT_BMI:
    print("You are underweight.")
elif bmi <= NORMAL_BMI:
    print("You have a normal weight.")
else:
    print("You are overweight.")
    
print("BMI Classification Ranges:")
print("Underweight: less than", UNDERWEIGHT_BMI)
print("Normal:", UNDERWEIGHT_BMI, "to", NORMAL_BMI)
print("Overweight:", NORMAL_BMI, "or greater")
