import math

print("BMI Calculator")
print("")
while True:
    unit=input("Would you like to use imperial or metric units?: ")
    result=["Your BMI:"]

weight=input("Enter your weight in (lbs): ")
weight2=input("Enter your weight in (kg): ")
height=input("Enter your height in (in): ")
height2=input("Enter your height in (cm): ")

bmi=(float(weight)/float(height)**2)*703
print("Your BMI is:",bmi)

if bmi<=18.4:
    print("Underweight")
elif bmi<=24.9:
    print("Normal")
elif bmi<=39.9:
    print("Overweight")
elif bmi>=40.0:
    print("Obese")