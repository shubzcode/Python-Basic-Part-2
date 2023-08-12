import math
# Calculate the Area and Circumference of a Circle Given the Radius:
radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius**2
circumference = 2 * math.pi * radius

print("Area:", area)
print("Circumference:", circumference)