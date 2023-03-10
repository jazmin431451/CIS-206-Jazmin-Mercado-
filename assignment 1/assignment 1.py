"""BMI is convert in this program and determine your body mass index. 

input:
    your name, weight, and height
    
output:
    your weight in lbs
    your height in feet 
    additional inches
    one decimal place
example:
    enter your weight and height:
    130 and 5'3 ft
    resulting from mass in kilograms and height in metres is healthy bmi= 23.025951121189216
Todo:
    * ask there weight in lbs and their height in feet and inches 
    * calculate and display their BMI and also include the display the value range for underweight, normal and overweight.
    *also make sure the sorce in BMI is in range recommendations.
References:
    *https://www.w3schools.com/python/default.asp
    *https://en.wikipedia.org/wiki/Body_mass_index
    *https://www.mathsisfun.com/metric-imperial-conversion-charts.html
 """

print("Please Enter your name")
name = input()

# Ask the user for their weight in pounds
weight_pounds = float(input("Please enter your weight in lbs: "))

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

# Classify the user's BMI
if bmi < 18.5:
    print(name + " is Underweight (bmi= " + str(bmi) + ")")
elif bmi < 25:
    print(name + " is Healthy (bmi= " + str(bmi) + ")")
else:
    print(name + " is Overweight (bmi= " + str(bmi) + ")")
