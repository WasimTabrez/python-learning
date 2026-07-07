name = "Python"
print(id(name)) # 4333755040

name += " Programming"
print(id(name)) # 4334208624

"""
Why did the ID change?
  Because strings are immutable — Python cannot modify the original string object in memory. Instead it creates a brand new string object.
"""