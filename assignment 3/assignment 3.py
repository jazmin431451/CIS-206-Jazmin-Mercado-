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
    Args: 
        None
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

def calculate_weight(weight_pounds, height_user):
    """Calculate BMI using weight in pounds and height in inches.
    Parameters:
        weight_pounds str(int): Weight in pounds.
        height_user str(int): Height in inches.

    Returns:
        int: BMI rounded to one decimal place.
    Raises:
        ValueError: If weight_pounds or height_inches are not positive numbers. 
        ValueError: If bmi is not a positive number.
    """
    weight_pounds = int(input("please enter your weight in pounds: "))
    height_user= int()
    weight_pounds = (weight_pounds / (height_user ** 2)) * 703
    weight_pounds = 0.45359237 
    if not isinstance(weight_pounds, int, float) or not isinstance(height_user, int):
        raise ValueError("If weight_pounds or height_inches are not positive numbers.")
    if weight_pounds <= 0 or weight_pounds <=0:
        raise ValueError("Weight and height must be positive numbers.")    
    return weight_pounds
def table_BMI(bmi):
    """table BMI as underweight, healthy, or overweight.

    Parameters:
        bmi (float): BMI value.

    Returns:
        str: Classification of BMI.

    Raises:
        ValueError: If bmi is not a positive number.
    """
    if not isinstance(bmi, float):
        raise ValueError("BMI must be a number.")
    if bmi <= 0:
        raise ValueError("BMI must be a positive number.")

    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "healthy"
    else:
        return "overweight"
    
def display_results(name, bmi):
    """Display BMI and Classification for a given name.

    Args:
        name (str): Name to person.
        bmi (float): BMI value.
        c
    Returns:
        None
    Raises:
        AssertionError: Height must be given in whole numbers to feet and inches.
        AssertionError: Weight must be given in pounds as height must be given in feet and inches.
        AssertionError: Height must be given in whole numbers to feet and inches
    """
    name = input("Please enter your name: ")
    bmi = float(input("Please enter your weight in lbs: "))
    assert isinstance(name, int) or isinstance(bmi, int), \
        "Height must be given in whole numbers to feet and inches. Received {type(Classification)}" 
    assert isinstance(weight_user= int) , \
        "Weight must be given in pounds as height must be given in inches. Received {type(height_user)}"
    print(f"{name}'s BMI is {bmi}.")
    
def main():
    """Runs the main program logic.
    """
try:

    name = get_user_name()
    height = convert_height_user(height_feet=any, height_inches=any)
    weight_pounds = calculate_weight(weight_pounds=any, height_user=any)
    bmi = table_BMI(bmi=any)
    display_results(name=any,bmi=any, classification=any)
    while True:
        choice = input("Do you want to calculate another BMI? (Y/N) ")
        if choice.upper() == "Y":
            weight_pounds = float(input("Please enter your weight in lbs: "))
            height_feet = int(input("Enter your height in feet: "))
            height_inches = int(input("Enter any additional inches: "))
            height_inches = convert_height_user(height_feet, height_inches)
            bmi = calculate_weight(weight_pounds, height_inches)
            display_results(name, bmi)
        elif choice.upper() == "N":
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
except:
    print(f"Error: {convert_height_user}")
    print(f"An unknown error occurred: {calculate_weight}")
     
     
main()
