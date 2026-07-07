a = [10, 20, 30]
b = a

print(id(a))  # 4363942272
print(id(b))  # 4363942272

b.append(40)

print(a)  # [10, 20, 30, 40]
print(b)  # [10, 20, 30, 40]

"""
Why did both lists change?
  Because b = a does not copy the list — it just makes b point to the same object as a.
"""