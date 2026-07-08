# BMI Calculator

weight = float(input("Enter weight(in Kg): "))
height = float(input("Enter height(in meter): "))

BMI = weight / pow(height, 2) # formula requires height in meters, not cm

if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal")
elif BMI >= 25 and BMI <= 29.9:
    print("Overweight")
else:
    print("Obese")
