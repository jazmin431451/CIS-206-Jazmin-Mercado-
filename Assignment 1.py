print("Please Enter height in feet and inches")
height = int(input())
print("also please enter your weight in lbs")
weight = int(input())
bmi = float(weight) / (height * 2) * 703
if bmi < 16:
    print("severely underweight")
else:
    if bmi >= 16 and bmi < 18.5:
        print("underweight")
    else:
        if bmi >= 18.5 and bmi < 25:
            print("healthy")
        else:
            if bmi >= 25 and bmi < 30:
                print("overweight")
            else:
                if bmi >= 30:
                    print("obese")
print("your bmi is" + str(bmi) + "and you are" + str(bmi))
