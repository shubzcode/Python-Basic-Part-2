# Perform Trigonometric Calculations (Sine, Cosine, Tangent)

import math

angle_degrees = float(input("Enter an angle in degrees: "))
angle_radians = math.radians(angle_degrees)

sine_value = math.sin(angle_radians)
cosine_value = math.cos(angle_radians)
tangent_value = math.tan(angle_radians)

print("Sine:", sine_value)
print("Cosine:", cosine_value)
print("Tangent:", tangent_value)