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
 
def FEET_TO_INCHES (height):
    """ Get user's height in feet and inches
    Args:
        feet(float): user's height in feet
         inches(float): user's height in inches
    Returns:
        float: feet and inches
    """
    print ("Please enter your height in feet: ") 
    feet = float (input ()) 
     
    print(" Please enter your height in inches:")
    inches = float(input())
    
    height = feet * FEET_TO_INCHES + inches
    FEET_TO_INCHES = 12
    LBS_TO_KGS = 0.453592
    return FEET_TO_INCHES


def display_results(weight):
    """ Displays user 's weight in pounds.

    Args:
        weight (float): user' s weight in pounds 
 
    Returns:
        float:in weight 
 
"" "
    print(" Please enter your weight in pounds:")
    weight = float(input())
    return weight
def  calculate_bmi(height, weight):
    " "" Converts Calculate user 's BMI.

    Args:
        BMI (float): Calculate user' s BMI 
 
    Returns:
        float:height, weight 
 
    "" "
    BMI = weight / (height ** 2) * 703
    return height, weight
    
def display_bmi(name, bmi):
    "" " Display user's name and BMI status.

    Args:
        BMI (float): user's name and BMI status

    Returns:
        None

    Raises:
        ValueError: If BMI is not a valid float.
        ValueError: If BMI is below 16.
        ValueError: IF BMI is Greater than 16 and BMI Less than 18.5
        ValueError: If BMI is Greater than 18.5 and BMI less then 25
        ValueError: If BMI is Greater than 25 and BMI less thean 30
    """
    try:
        bmi = float(bmi)
        name = float()
    except ValueError:
        raise ValueError("BMI must be a weight. Received '{name}'")
    except:
        raise
    if bmi < 16:
        raise ValueError(name + " is severely underweight (bmi= " + str(bmi) + ")")
    if bmi >= 16 and bmi < 18.5:
        raise ValueError(name + " is underweight (bmi= " + str(bmi) + ")")
    if bmi >= 18.5 and bmi < 25:
        raise ValueError(name + " is healthy (bmi= " + str(bmi) + ")")
    if bmi >= 25 and bmi < 30:
        raise ValueError(name + " is overweight (bmi= " + str(bmi) + ")")
    else:
        raise ValueError(name + " is obese (bmi= " + str(bmi) + ")")

def main():
    """ Main function that calls other functions to get input, perform calculations, and display output"""

    name = get_name()
    height = FEET_TO_INCHES (height)
    weight = display_results(weight)
    bmi = calculate_bmi(height, weight)
    display_bmi(name, bmi)

if __name__ == "__main__":
    main()
