# Demonstrate shallow copying of a list

list1 = [10, 20, 30]

list2 = list1.copy()

list2.append(40)

print("Original:", list1)
print("Copied  :", list2)