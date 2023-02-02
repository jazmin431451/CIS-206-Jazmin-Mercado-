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

weight = 105
def get_height():
    """convert height in feet and inches to total inches.
    Args:
        none
    Returns:
         int: height in feet and inches.
    exit:
        ValueError: "Height must be given in whole numbers of feet and inches."
        ValueError: "Height cannot be negative."
    """
    try:
        print("Please enter your height in feet: ")
        height_feet = input()
        height_feet = float()
        print("Please enter your height in inches: ")
        height_inches = input()
        height_inches = float()
        if (height_inches * 12) + height_inches:
            print("Height must be given in whole numbers of feet and inches.")
            print(f"ValueError: {height_inches}is invalid")
            os._exit(1)
        return height_inches
    except ValueError:
        print("Height cannot be negative.")
        print(f"ValueError: {height_inches} is invalid")
        os._exit(2)

def calculate_bmi(weight):
    """Calculate BMI using weight in lbs and height in feet and inches.
    Args:
        bmi (float): Weight in lbs.
    Returns:
        float: BMI rounded to one decimal place.
    Raises:
        ValueError: If weight must be given in whole numbers of bmi. 
        ValueError: If weight cannot be negative.
    """
    try:
        print("please enter your bmi in weight:" )
        bmi= input()
        bmi = float()
    except:   
        if bmi < 18.5:
            raise ValueError (f" bmi must be 'underweight', 'healthy', or 'overweight. Received '{bmi}'") 
    height_feet= 1.82
    height_inches = 1.6616
    height = (height_feet * 12) + height_inches
    bmi = round(weight/(height**2),1)   
    return bmi


def display_results(bmi, height, weight):
    """Display BMI and Classification for a given name.
    Args:
        height (float): Name to person.
        bmi (float): BMI value.
    Returns:
        None
    Raises:
         AssertionError: If height is not a valid float.
         AssertionError: If weight is not a valid float.
    """ 
    assert isinstance(height, float) or isinstance(height, int), \
        "If height is not a valid float. Received {typr(height)}" 
    assert isinstance(weight, float) or isinstance(weight, int), \
        "If weight is not a valid float. Received {type(weight)}"
    assert isinstance(bmi, float) or isinstance(bmi, int), \
        "If bmi is not a valid float. Received {type(bmi)}"
    print(f"{height} bmi is {weight} weight is {bmi}")
    

def main():
    """Runs the main program logic."""
    try:
        height = get_height()
        bmi = calculate_bmi(weight)
        display_results(bmi ,height, weight)
    except:
        print("Unexpected error.")
        print("Error:", sys.exc_info()[1])
        print("File: ", sys.exc_info()[2].tb_frame.f_code.co_filename) 
        print("Line: ", sys.exc_info()[2].tb_lineno)

main()
