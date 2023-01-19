print("please enter your name")
name = input()
print("Please Enter height in feet and inches")
height = int(input())
print("also please enter your weight in lbs")
weight = int(input())
bmi = float(weight) / (height * 2) * 703
if bmi < 16:
    print(name + " is severely underweight (bmi= " + str(bmi) + ")")
else:
    if bmi >= 16 and bmi < 18.5:
        print(name + " is  underweight (bmi= " + str(bmi) + ")")
    else:
        if bmi >= 18.5 and bmi < 25:
            print(name + " is healthy (bmi= " + str(bmi) + ")")
        else:
            if bmi >= 25 and bmi < 30:
                print(name + " is overweightt (bmi= " + str(bmi) + ")")
            else:
                if bmi >= 30:
                    print(name + " is obese (bmi= " + str(bmi) + ")")
