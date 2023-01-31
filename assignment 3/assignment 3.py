"""This program converts in this program and determine your body mass index.
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
import sys
def get_user_name():
    """Gets user's name.

    Args: None

    Returns:
        str: user's name
    """
    print("Please enter your name:")
    name = input()
    return name

def convert_height_user(height_feet, height_inches):
    """convert height in feet and inches to total inches.

    Args:
        height_feet (int): height in feet
        height_inches (int): height in inches
        height (float): user's height
    Returns:
         int: Total height in inches.
    extis:
        ValueError: "Height must be given in whole numbers of feet and inches."
        ValueError: "Height cannot be negative."

    """
    height_feet = int(input("Please enter your height in feet: "))
    height_inches = int(input("Please enter your height in inches: "))
    height =  float()
    if not isinstance(height_feet, int) or not isinstance(height_inches, int):
        raise ValueError("Height must be given in whole numbers of feet and inches.")
    if height_feet < 0 or height_inches < 0:
        raise ValueError("Height cannot be negative.")
    height_feet = 1
    height_inches = 12
    height = (height_feet * 12) + height_inches
    return height

def calculate_bmi(weight_pounds, height_user):
    """Calculate BMI using weight in pounds and height in inches.
    Parameters:
        weight_pounds (int): Weight in pounds.
        height_user (int): Height in inches.

    Returns:
        int: BMI rounded to one decimal place.
    Raises:
        ValueError: If weight_pounds or height_inches are not positive numbers. 
        ValueError: If bmi is not a positive number.

    """
    weight_pounds = int(input("please enter your weight in pounds:"))
    height_user= int()
    weight_pounds = int()
    if not isinstance(weight_pounds, int, float) or not isinstance(height_user, int):
        raise ValueError("Weight must be given in pounds as height must be given in feet and inches.")
    if weight_pounds <= 0 or height_user <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    weight_pounds = 0.45359237
    weight_pounds = (weight_pounds / (height_user ** 2)) * 703
    return weight_pounds

def display_results(name, bmi):
    """Display BMI and Classification for a given name.

    Args:
        name (str): Name of person.
        bmi (float): BMI value.
        classification (str): Classification of BMI.
    Returns:
        None
    Raises:
        AssertionError: Height must be given in whole numbers of feet and inches.
        AssertionError: Weight must be given in pounds as height must be given in feet and inches.
        AssertionError: Height must be given in whole numbers of feet and inches
    """
    name = input("Please enter your name: ")
    bmi = float(input("Please enter your weight in lbs: "))
    if bmi < 18.5:
        print(name + " is Underweight (bmi= " + str(bmi) + ")")
    elif bmi >= 18.5 and bmi < 25:
        print(name + " is Healthy (bmi= " + str(bmi) + ")")
    elif bmi >= 25 and bmi < 30:
        print(name + " is Overweight (bmi= " + str(bmi) + ")")
    else:
        print (name + " is obese (bmi= " + str(bmi) + ")")
    bmi = round(bmi, 1)
    assert isinstance(name, int) or isinstance(bmi, int), \
        "Height must be given in whole numbers of feet and inches. Received {type(Classification)}" 
    assert isinstance(weight_user= int) , \
        "Weight must be given in pounds as height must be given in feet and inches. Received {type(height_user)}"
    print(f"{name}'s BMI is {bmi}.")
    
def main():
    """Runs the main program logic.
    """
try:
    name = get_user_name()
    height = convert_height_user(height_feet=any, height_inches=any)
    weight_pounds = calculate_bmi(weight_pounds=any, height_user=any)
    display_results(name=any,bmi=any, classification=any)
except:
    
    print("Unexpected error.")
    print("Error:")
    print("File: ") 
    print("Line: ")


main()
