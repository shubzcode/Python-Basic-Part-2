import math

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Roots:", root1, root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("Root:", root)
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print("Complex Roots:", real_part, "+", imaginary_part, "i and", real_part, "-", imaginary_part, "i")
