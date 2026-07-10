# Calculate the area of a rectangle using a function

def rectangel_area(length, width):
    return length * width

length = float(input("Enter length: "))
width = float(input("Enter width: "))

print("Area =",rectangel_area(length,width))