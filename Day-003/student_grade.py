# Student grade

name = input("Enter Name: ")

marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))
marks4 = int(input("Enter marks for subject 4: "))
marks5 = int(input("Enter marks for subject 5: "))

total = marks1 + marks2 + marks3 + marks4 + marks5
average = total / 5

# chedcked highest-first: a 92 average also satisfies >= 75 and >= 60,
# so order determines which grade wins
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'F'

print()
print("Studen Report Card")
print("------------------- ")
print(f"Name    : {name}")
print(f"Total   : {total}")
print(f"Average : {average:.1f}")
print(f"Grade   : {grade}")
