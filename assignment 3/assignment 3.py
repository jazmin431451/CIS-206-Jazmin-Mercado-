import sys

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
    if not isinstance(height_feet, int) or not isinstance(height_inches, int):
        raise ValueError("Height must be given in whole numbers of feet and inches.")
    if height_feet < 0 or height_inches < 0:
        raise ValueError("Height cannot be negative.")

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
    if not isinstance(weight_pounds, (int, float)) or not isinstance(height_inches, int):
        raise ValueError("Weight must be given in pounds and height must be given in inches.")
    if weight_pounds <= 0 or height_inches <= 0:
        raise ValueError("Weight and height must be positive numbers.")

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


def display_bmi(name, bmi, classification):
    """Display BMI and classification for a given name.

    Parameters:
        name (str): Name of person.
        bmi (float): BMI value.
        classification (str): Classification of BMI.

    Raises:
        ValueError: If name is not a string, bmi is not a positive number, or classification is not a string.
    """
    if not isinstance(name, str) or not isinstance(bmi, float) or not isinstance(classification, str):
        raise ValueError("Name must be a string, BMI must be a positive number, and classification must be a string.")
    if bmi <= 0:
raise ValueError("BMI must be a positive number.")
if classification not in ["underweight", "healthy", "overweight"]:
raise ValueError("Classification must be 'underweight', 'healthy', or 'overweight'.")

print(f"{name}'s BMI is {bmi} and they are classified as {classification}.")

def display_bmi_table():
"""Display a table of BMI values for various weight and height combinations.
"""
print("BMI Table:")
print("Weight (lbs) | Height (in) | BMI")
for weight in range(100, 251, 10):
for height in range(58, 77, 2):
bmi = calculate_bmi(weight, height)
classification = classify_bmi(bmi)
print(f"{weight} | {height} | {bmi} ({classification})")

def main():
try:
name = input("Please enter your name: ")
weight_pounds = float(input("Please enter your weight in lbs: "))
height_feet = int(input("Enter your height in feet: "))
height_inches = int(input("Enter any additional inches: "))
height_inches = convert_height_inches(height_feet, height_inches)
b
mi = calculate_bmi(weight_pounds, height_inches)
classification = classify_bmi(bmi)
display_bmi(name, bmi, classification)
    while True:
        choice = input("Do you want to calculate another BMI? (Y/N) ")
        if choice.upper() == "Y":
            weight_pounds = float(input("Please enter your weight in lbs: "))
            height_feet = int(input("Enter your height in feet: "))
            height_inches = int(input("Enter any additional inches: "))

            height_inches = convert_height_inches(height_feet, height_inches)
            bmi = calculate_bmi(weight_pounds, height_inches)
            classification = classify_bmi(bmi)
            display_bmi(name, bmi, classification)
        elif choice.upper() == "N":
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    display_bmi_table()

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unknown error occurred: {e}")
if name == "main":
main()
