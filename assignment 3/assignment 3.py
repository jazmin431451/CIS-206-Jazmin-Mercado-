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


def get_pounds():
    """Gets weight in pounds.

    Args:
        None

    Returns:
        float: pounds

    Exits:
        ValueError: If weight is not a valid float.
        ValueError: If weight is not in range > 0 and < 1000.

    """
    try:
        print("Enter weight in pounds:")
        pounds = input()
        pounds = float(pounds)
        if pounds <= 0:
            print("pounds must be a positive value.")
            print(f"ValueError: {pounds} is invalid.")
            os._exit(1)
        elif pounds >= 1000:
            print("pounds must be less than 1000.")
            print(f"ValueError: {pounds} is invalid.")
            os._exit(2)
        return pounds
    except ValueError:
        print("pounds must be a floating point value.")
        print(f"ValueError: {pounds} is invalid.")
        os._exit(3)


def get_feet():
    """Gets height in feet.

    Args:
        None

    Returns:
        int: feet

    Exits:
        ValueError: If feet is not a valid float.
        ValueError: If feet is not in range > 0 and < 10.

    """
    try:
        print("Enter height in feet:")
        feet = input()
        feet = int(feet)
        if feet <= 0:
            print("feet must be a positive value.")
            print(f"ValueError: {feet} is invalid.")
            os._exit(4)
        elif feet >= 10:
            print("feet must be less than 10.")
            print(f"ValueError: {feet} is invalid.")
            os._exit(5)
        return feet
    except ValueError:
        print("feet must be an integer value.")
        print(f"ValueError: {feet} is invalid.")
        os._exit(6)


def get_inches():
    """Gets height in inches.

    Args:
        None

    Returns:
        int: inches

    Exits:
        ValueError: If inches is not a valid float.
        ValueError: If inches is not in range >= 0 and < 12.

    """
    try:
        print("Enter height in inches:")
        inches = input()
        inches = int(inches)
        if inches < 0:
            print("inches must be a positive value.")
            print(f"ValueError: {inches} is invalid.")
            os._exit(7)
        elif inches >= 12:
            print("inches must be less than 12.")
            print(f"ValueError: {inches} is invalid.")
            os._exit(8)
        return inches
    except ValueError:
        print("inches must be an integer value.")
        print(f"ValueError: {inches} is invalid.")
        os._exit(9)


def convert_height_inches(height_feet, height_inches):
    """Convert height in feet and inches to total inches.

    Parameters:
        height_feet (int): Height in feet.
        height_inches (int): Additional inches.

    Returns:
        int: Total height in inches.

    Raises:
        ValueError: If height_feet or height_inches are not positive integers.
    """
    assert isinstance(height_feet, int) and \
        isinstance(height_inches, int), \
        "Height must be given in whole numbers of feet and inches."
    assert height_feet > 0 and height_inches >= 0, \
        "Height cannot be negative."

    return (height_feet * 12) + height_inches


def calculate_bmi(weight_pounds, height_inches):
    """Calculate BMI using weight in pounds and height in inches.

    Parameters:
        weight_pounds (float): Weight in pounds.
        height_inches (int): Height in inches.

    Returns:
        float: BMI rounded to one decimal place.

    Raises:
        ValueError: If weight_pounds or height_inches are not positive numbers.
    """
    assert isinstance(weight_pounds, (int, float)) and \
        isinstance(height_inches, int), \
        "Weight must be given in pounds and height must be given in inches."
    assert weight_pounds > 0 and height_inches > 0, \
        "Weight and height must be positive numbers."

    bmi = (weight_pounds / (height_inches ** 2)) * 703
    return round(bmi, 1)


def classify_bmi(bmi):
    """Classify BMI as underweight, healthy, or overweight.

    Parameters:
        bmi (float): BMI value.

    Returns:
        str: Classification of BMI.

    Raises:
        ValueError: If bmi is not a positive number.
    """
    assert isinstance(bmi, float), "BMI must be a number."
    assert bmi > 0, "BMI must be a positive number."

    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "healthy"
    else:
        return "overweight"


def display_bmi(bmi, classification):
    """Display BMI and classification for a given name.

    Parameters:
        name (str): Name of person.
        bmi (float): BMI value.
        classification (str): Classification of BMI.

    Raises:
        ValueError: If name is not a string,
            bmi is not a positive number,
            or classification is not a string.
    """
    assert isinstance(bmi, float) and isinstance(classification, str), \
        "BMI must be a positive number, and classification must be a string."
    assert bmi > 0, "BMI must be a positive number."
    assert classification in ["underweight", "healthy", "overweight"], \
        "Classification must be 'underweight', 'healthy', or 'overweight'."

    print(f"BMI is {bmi} and they are classified as {classification}.")


def main():
    try:
        weight_pounds = get_pounds()
        height_feet = get_feet()
        height_inches = get_inches()
        height_inches = convert_height_inches(height_feet, height_inches)
        bmi = calculate_bmi(weight_pounds, height_inches)
        classification = classify_bmi(bmi)
        display_bmi(bmi, classification)

    except:
        print("Unexpected error.")
        print("Error:", sys.exc_info()[1])
        print("File: ", sys.exc_info()[2].tb_frame.f_code.co_filename)
        print("Line: ", sys.exc_info()[2].tb_lineno)


main()
