
import os
import sys

height_feet = 1
height_inches = 12

def get_height():
    """convert height in feet and inches to total inches.
    Args:
        height_feet (int): height in feet
        height_inches (int): height in inches
        height (float): user's height
    Returns:
         int: Total height in inches.
    exit:
        ValueError: "Height must be given in whole numbers of feet and inches."
        ValueError: "Height cannot be negative."
    """
    try:

        height_feet = int(input("Please enter your height in feet: "))
        height_inches = int(input("Please enter your height in inches: "))
        height = float(height)
        if height_feet  <= (float) or height_inches <= (float):
            print("Height must be given in whole numbers of feet and inches.")
            print(f"ValueError: {height}is invalid")
            os._exit(1)
        return height
    except ValueError:
        print("Height cannot be negative.")
        print(f"ValueError: {height} is invalid")
        os._exit(2)



def calculate_BMI(weigth):
    """Calculate BMI using weight in pounds and height in inches.
    Args:
        weight_pounds str(int): Weight in pounds.
        height_user str(int): Height in inches.
    Returns:
        int: BMI rounded to one decimal place.
    Raises:
        ValueError: If weight_pounds or height_inches are not positive numbers. 
        ValueError: If bmi is not a positive number.
    """
    try:
        weigth = float("please enter your weight in pounds:" )
        bmi = float(weight)
    except ValueError:
        raise ValueError(f"If weight_pounds or height_inches are not positive numbers. Received '{weigth}'")
    except:
        raise
    weight = 0.45359237
    height_inches = (height_feet * 12) + height_inches 
    weight= (weight / (height_feet** 2)) * 703
    
    if weight <= 0.45359237:
        raise ValueError(f"Weight and height must be positive numbers. Received '{weigth}'")
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "healthy"
    else:
        return "overweight"
    


def display_results(height, weight):
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
    
    assert isinstance(height, float) or isinstance(height, int), \
        "Height must be given in whole numbers to feet and inches. Received {type(height)}" 
    assert isinstance(weight, float) or isinstance(weight, int), \
        "Weight must be given in pounds as height must be given in inches. Received {type(weight)}"
    print(f"{height}'s BMI is {weight}.")
    

def main():
    """Runs the main program logic."""

   try:
        height = get_height(height)
        weight = calculate_BMI(weight)
        display_results(height, weight)
   
import os
import sys

height_feet = 1
height_inches = 12

def get_height():
    """convert height in feet and inches to total inches.
    Args:
        height_feet (int): height in feet
        height_inches (int): height in inches
        height (float): user's height
    Returns:
         int: Total height in inches.
    exit:
        ValueError: "Height must be given in whole numbers of feet and inches."
        ValueError: "Height cannot be negative."
    """
    try:

        height_feet = int(input("Please enter your height in feet: "))
        height_inches = int(input("Please enter your height in inches: "))
        height = float(height)
        if height_feet  <= (float) or height_inches <= (float):
            print("Height must be given in whole numbers of feet and inches.")
            print(f"ValueError: {height}is invalid")
            os._exit(1)
        return height
    except ValueError:
        print("Height cannot be negative.")
        print(f"ValueError: {height} is invalid")
        os._exit(2)



def calculate_BMI(weigth):
    """Calculate BMI using weight in pounds and height in inches.
    Args:
        weight_pounds str(int): Weight in pounds.
        height_user str(int): Height in inches.
    Returns:
        int: BMI rounded to one decimal place.
    Raises:
        ValueError: If weight_pounds or height_inches are not positive numbers. 
        ValueError: If bmi is not a positive number.
    """
    try:
        weigth = float("please enter your weight in pounds:" )
        bmi = float(weight)
    except ValueError:
        raise ValueError(f"If weight_pounds or height_inches are not positive numbers. Received '{weigth}'")
    except:
        raise
    weight = 0.45359237
    height_inches = (height_feet * 12) + height_inches 
    weight= (weight / (height_feet** 2)) * 703
    
    if weight <= 0.45359237:
        raise ValueError(f"Weight and height must be positive numbers. Received '{weigth}'")
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "healthy"
    else:
        return "overweight"
    


def display_results(height, weight):
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
    
    assert isinstance(height, float) or isinstance(height, int), \
        "Height must be given in whole numbers to feet and inches. Received {type(height)}" 
    assert isinstance(weight, float) or isinstance(weight, int), \
        "Weight must be given in pounds as height must be given in inches. Received {type(weight)}"
    print(f"{height}'s BMI is {weight}.")
    

def main():
    """Runs the main program logic."""

    height = get_height(height)
    weight = calculate_BMI(weight)
    display_results(height, weight)

import os
import sys

height_feet = 1
height_inches = 12

def get_height():
    """convert height in feet and inches to total inches.
    Args:
        height_feet (int): height in feet
        height_inches (int): height in inches
        height (float): user's height
    Returns:
         int: Total height in inches.
    exit:
        ValueError: "Height must be given in whole numbers of feet and inches."
        ValueError: "Height cannot be negative."
    """
    try:

        height_feet = int(input("Please enter your height in feet: "))
        height_inches = int(input("Please enter your height in inches: "))
        height = float(height)
        if height_feet  <= (float) or height_inches <= (float):
            print("Height must be given in whole numbers of feet and inches.")
            print(f"ValueError: {height}is invalid")
            os._exit(1)
        return height
    except ValueError:
        print("Height cannot be negative.")
        print(f"ValueError: {height} is invalid")
        os._exit(2)



def calculate_BMI(weigth):
    """Calculate BMI using weight in pounds and height in inches.
    Args:
        weight_pounds str(int): Weight in pounds.
        height_user str(int): Height in inches.
    Returns:
        int: BMI rounded to one decimal place.
    Raises:
        ValueError: If weight_pounds or height_inches are not positive numbers. 
        ValueError: If bmi is not a positive number.
    """
    try:
        weigth = float("please enter your weight in pounds:" )
        bmi = float(weight)
    except ValueError:
        raise ValueError(f"If weight_pounds or height_inches are not positive numbers. Received '{weigth}'")
    except:
        raise
    weight = 0.45359237
    height_inches = (height_feet * 12) + height_inches 
    weight= (weight / (height_feet** 2)) * 703
    
    if weight <= 0.45359237:
        raise ValueError(f"Weight and height must be positive numbers. Received '{weigth}'")
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "healthy"
    else:
        return "overweight"
    


def display_results(height, weight):
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
    
    assert isinstance(height, float) or isinstance(height, int), \
        "Height must be given in whole numbers to feet and inches. Received {type(height)}" 
    assert isinstance(weight, float) or isinstance(weight, int), \
        "Weight must be given in pounds as height must be given in inches. Received {type(weight)}"
    print(f"{height}'s BMI is {weight}.")
    

def main():
    """Runs the main program logic."""
 try:
     height = get_height(height)
     weight = calculate_BMI(weight)
     display_results(height, weight)
 except:
       print("Unexpected error.")
       print("Error:", sys.exc_info()[1])
       print("File: ", sys.exc_info()[2].tb_frame.f_code.co_filename) 
       print("Line: ", sys.exc_info()[2].tb_lineno)
   

main()
