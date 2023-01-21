# This program calculates a person's Body Mass Index (BMI) based on their weight in pounds and height in feet and inches.

UNDERWEIGHT_BMI = 18.5
NORMAL_BMI = 24.9
OVERWEIGHT_BMI = 29.9


print("Please Enter your name")
name = input()

# Ask the user for their weight in pounds
weight_pounds = float(input("Enter your weight in pounds: "))

# Ask the user for their height in feet and inches
height_feet = int(input("Enter your height in feet: "))
height_inches = int(input("Enter any additional inches: "))

# Convert the height to inches
height_inches = (height_feet * 12) + height_inches

# Calculate the user's BMI
bmi = (weight_pounds / (height_inches * height_inches)) * 703

# Round the BMI to one decimal place
bmi = round(bmi, 1)

# Print the user's BMI
print("Your BMI is:", bmi)

# the user's BMI
if bmi < UNDERWEIGHT_BMI:
    print("You are underweight.")
elif bmi <= NORMAL_BMI:
    print("You have a normal weight.")
else:
    print("You are overweight.")
    
# Print the legend
print("BMI Ranges:")
print("Underweight: less than", UNDERWEIGHT_BMI)
print("Normal:", UNDERWEIGHT_BMI, "to", NORMAL_BMI)
print("Overweight:", NORMAL_BMI, "or greater")
