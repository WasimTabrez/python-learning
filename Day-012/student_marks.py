# Student Marks Validation

try:

    marks = float(input("Enter Marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks should be between 0 and 100.")

    print("Marks =", marks)

    if marks >= 35:
        print("Result : Pass")
    else:
        print("Result : Fail")

except ValueError as error:
    print(error)
