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
