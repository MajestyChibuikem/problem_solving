import functions
"""
base@ base of the triangle
height@ height of the triangle
result = 0.5 * base * height

"""

base = input("Enter the base: ")
base = functions.int_check(base)

height = input("Enter the height: ")
height = functions.int_check(height)

result = functions.area(base,height)
print(result)