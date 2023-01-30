""" This program converts this program and determines your body mass index.
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
    resulting from mass in kilograms and 
height in meters is healthy (bmi= 23.025951121189216)
Todo:
    * ask there weight in lbs and their height in feet and inches 
    * calculate and display their BMI and also include the display of the value
range for underweight,normal and overweight.
    * also make sure the source in BMI is in range recommendations.
References:
    * https://www.w3schools.com/python/default.asp
    * https://en.wikipedia.org/wiki/Body_mass_index
    * https://www.mathsisfun.com/metric-imperial-conversion-charts.html
"""
import sys

LBS_TO_KGS = 0.453592
def get_user_name(user_name):
    """Get the user's name
    Args: user_name (input): user's name
    Return: user_name (input): user's name
    Exits: none
    """
    print("Please enter your name:")
    user_name = float(input())
    return user_name

def height_inches(height_feet, height_inches, name):
    """Convert height in feet and inches to total inches.

    Args:
        height_feet(float): user's height in feet
         height_inches(float): user's height in inches
    Returns:
        float: feet and inches
    Exits:
        ValueError: If height must be given in whole number of feet and inches.
        ValueError: If height cannot be negative.
    """
    try:
        print("Please enter your height in feet: ")
        feet = float (input ()) 
        print(" Please enter your height in inches:")
        inches = float(input())
        if height_feet <0 or height_inches < 0:
            print("Height must be given in whole numbers of feet and inches.")
            print(name + "ValueError: {height_feet, height_inches} is invalid.")
            sys._exit(1)   
        return height_feet, height_inches
    except ValueError:
        print("Height cannot be negative.")
        print(name + "ValueError: {height_feet, height_inches} is invalid.")
        sys._exit(2)
    
        height_inches = feet * FEET_TO_INCHES + inches
        FEET_TO_INCHES = 12
        return FEET_TO_INCHES

def calculate_bmi(name):
    """Calculate BMI using weight in pounds and height in feet and inches.

    Args:
         weight_pounds (float): weight in pounds.
         height_user (int): height in feet and inches.
    Returns:
        float: BMI rounded to one decimal place.
    Raise:
        ValueError: If weight must be given in pounds.
        ValueError: If weight and height must be a numbers.
    """
    try:
        print("Please enter your weight in pounds: ")
        weight_pounds = float (input ()) 
        height_user = int(input())
        if weight_pounds <0 or height_user < 0:
            print("weight must be given in pounds.")
            print(name + "ValueError: {weight_pounds} is invalid.")
            sys._exit(1)   
        return weight_pounds
    except ValueError:
        print("Weight and height must be positive numbers.")
        print(name + "ValueError: {weight_pounds} is invalid.")
        sys._exit(2)
        bmi = (weight_pounds / (height_user ** 2)) * 703
        weight_pounds = 0.453592
    return round(bmi, 1)

def bmi_to_weight(name):
    """ Display user's name and BMI status.
    Args:
        BMI (float): user's name and BMI status
    Returns:
        None
    Raises:
        ValueError: If BMI is not a valid float.
        ValueError: If BMI is below 16.
        ValueError: IF BMI is Greater than 16 and BMI Less than 18.5
        ValueError: If BMI is Greater than 18.5 and BMI less then 25
        ValueError: If BMI is Greater than 25 and BMI less than 30
    """
    try:
        bmi = float(bmi)
    except ValueError:
        raise ValueError(name +"BMI must be a weight. Received '{bmi}'")
    except:
        raise
    if bmi < 0:
        raise ValueError(name + "BMI must be a positive number (bmi= " + str(bmi) + ")")
    if bmi < 16:
        raise ValueError(name + " is severely underweight (bmi= " + str(bmi) + ")")
    if bmi >= 16 and bmi < 18.5:
        raise ValueError(name + " is underweight (bmi= " + str(bmi) + ")")
    if bmi >= 18.5 and bmi < 25:
        raise ValueError(name + " is healthy (bmi= " + str(bmi) + ")")
    if bmi >= 25 and bmi < 30:
        raise ValueError(name + " is overweight (bmi= " + str(bmi) + ")")


def display_results(name, bmi, classification):
    """Display BMI and classification for a given name.

    Args:
        name (str): name of person.
        bmi (float): BMI value.
        classification (str): classification of BMI.
        
    Returns:
        None

    Raises:
        AssertionError: If name is not a string, bmi.
        AssertionError: If bmi is not a positive number.
        AssertionError: If classification is not a string.

    """
    assert isinstance(bmi, float) or isinstance(name, str) or isinstance(classification, str), \
        "Name must be a string, BMI must be a positive number, and classification must be a string. Received {type(classification)}" 
    assert isinstance(bmi, float) or isinstance(name, int) or isinstance(classification, str), \
        "BMI must be a positive number. Received {type(classification)}"
    print(name + "{bmi}.the user name is (bmi = " + str(classification) + ")")

def display_bmi(name, bmi, classification)
    """Runs the main program logic."""
    try:
        name = input("Please enter your name: ")
        weight_pounds = float(input("Please enter your weight in lbs: "))
        height_feet = int(input("Enter your height in feet: "))
        height_inches = int(input("Enter any additional inches: "))
        height_user = height_user(height_feet, height_inches)
        bmi = bmi(weight_pounds, height_inches)
        bmi = calculate_bmi(bmi)
        display_bmi(name, bmi, classification)
    except:
    while True:
        choice = input("Do you want to calculate another BMI? (Y/N) ")
    if choice.upper() == "Y":
        display_bmi(name, bmi, classification)
    elif choice.upper() == "N":
    break
    else:
         print("Invalid input. Please enter 'Y' or 'N'.")
         
def main():
    """Runs the main program logic."""
    try:
        name = get_user_name(user_name=any)
        height_inches = height_inches()
        bmi_to_weight = calculate_bmi()
        bmi = bmi_to_weight(bmi)
        display_results(name, bmi, classification=any)
    except:
        print("Unexpected error.")
        print("Error:", sys.exc_info()[1])
        print("File: ", sys.exc_info()[2].tb_frame.f_code.co_filename) 
        print("Line: ", sys.exc_info()[2].tb_lineno)

main()