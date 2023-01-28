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
import os 
import sys

height_inches = 12
height_feet = 1
LBS_TO_KGS = 0.453592

def get_name ():
    """
    Get user's name
    
    Args: None
    Returns:
        float: user's name
    """ 
    print ("Please enter your name: ") 
    name = float (input ()) 
    return name 
def convert_height_user(height_feet, height_inches):
    """convert height in feet and inches to total inches.
    
    Args:
        height_feet (int): height in feet
        height_inches (int): height in inches

    Returns: 
            int: total height in inches. 
    Exits:
        ValueError: If height_feet or height_inches are not 
positive integers.
    """
    try:
        print("please enter your feet:")
        print("please enter your inches:")
        height_inches= input()
        height_feet= float()
        height_user= float(height_feet * 12) + height_inches
        if not isinstance(height_feet, int) or not isinstance(height_inches, int):
            print("Height must be given in whole numbers of feet and inches.")
            os._exit(1)   
        return height_user
    except ValueError:
        if height_feet < 0 or height_inches < 0:
            print("Height cannot be negative.")
        os._exit(2)

def calculate_bmi(weight_pounds, height_user):
    """Calculate BMI using weight in pounds and height in inches.

    Args:
        weight_pound (float): weight in pounds.
        height_user (int): height in inches and feet
    return:
        float: BMI rounded to decimal place 

    Raises:
        ValueError: If weight_pounds or height_inches are 
not positive numbers.
    """               
    try:
        bmi = float()
        height_user= float()
        weight_pounds= float()
    except ValueError:
        
        if not isinstance(weight_pounds, (int, float)) or not isinstance(convert_height_user, int):
            raise ValueError("Weight must be given in pounds and height must be given in inches.")
    
    except:
        raise
    
        if weight_pounds <= 0 or height_inches <= 0:
          raise ValueError("Weight and height must be positive numbers.")
    bmi = (weight_pounds / (height_inches ** 2)) * 703
    return bmi

def display_results(bmi, weight_pounds):
    """Classify BMI as underweight, healthy, or overweight.

    Args:
        bmi (float): BMI value.
        weight_pounds (float): weight in pounds
    Returns:
        str: Classification of BMI.

    Raises:
        ValueError: If bmi is not a positive number.
    """
    assert isinstance(bmi, float) or isinstance(bmi, int), \
        "BMI must be a number.. Received {type(bmi)}" 
    assert isinstance(weight_pounds, float) or isinstance(weight_pounds, int), \
        "BMI must be a positive number. Received {type(weight_pound)}"
    print(f"{bmi}.<= 0 bmi is {weight_pounds}.<= 0 weight_pounds")

def main():
    """Runs the main program logic."""
    try:
        get_name = input()
        weight_pounds = float()
        convert_height_use = int()
        height_inches = int(input("Enter any additional inches: "))
        height_inches = convert_height_use(height_feet, height_inches)
    except:
        print("Please enter your name:")
        print("Please enter your weight in lbs: ")
        print("Enter your height in feet: ", sys.exc_info()[2].tb_frame.f_code.co_filename) 
        print("Enter any additional inches: ", sys.exc_info()[2].tb_lineno)
main()
