# Store student marks and calculate total and average

marks = []

subjects = int(input("Enter number of subjects: "))

for i in range(subjects):
    mark = float(input(f"Enter marks for Subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

print("\nMarks  :", marks)
print("Total    :", total)
print("Average  :", average)