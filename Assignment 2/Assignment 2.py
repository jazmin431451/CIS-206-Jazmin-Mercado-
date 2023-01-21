# Constants for height and weight conversions
FEET_TO_INCHES = 12
LBS_TO_KGS = 0.453592

def get_name():
    """
    Get user's name
    """
    name = input("Please enter your name: ")
    return name

def get_height():
    """
    Get user's height in feet and inches
    """
    feet = int(input("Please enter your height in feet: "))
    inches = int(input("Please enter your height in inches: "))
    return feet * FEET_TO_INCHES + inches

def get_weight():
    """
    Get user's weight in pounds
    """
    weight = int(input("Please enter your weight in pounds: "))
    return weight

def calculate_bmi(height, weight):
    """
    Calculate user's BMI
    """
    return weight / (height ** 2) * 703

def display_bmi(name, bmi):
    """
    Display user's name and BMI status
    """
    if bmi < 16:
        print(name + " is severely underweight (bmi= " + str(bmi) + ")")
    elif bmi >= 16 and bmi < 18.5:
        print(name + " is underweight (bmi= " + str(bmi) + ")")
    elif bmi >= 18.5 and bmi < 25:
        print(name + " is healthy (bmi= " + str(bmi) + ")")
    elif bmi >= 25 and bmi < 30:
        print(name + " is overweight (bmi= " + str(bmi) + ")")
    else:
        print(name + " is obese (bmi= " + str(bmi) + ")")

def main():
    """
    Main function that calls other functions to get input,
    perform calculations, and display output
    """
    name = get_name()
    height = get_height()
    weight = get_weight()
    bmi = calculate_bmi(height, weight)
    display_bmi(name, bmi)

if __name__ == "__main__":
    main()
