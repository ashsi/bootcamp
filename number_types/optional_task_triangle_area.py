""" Calculate area of a triangle given 3 side lengths. """
from math import sqrt

# Start up message.
print("I will calculate the area of a triangle for you.")

# Ask user to enter 3 lengths (for the sides of the triangle).
sides = []
print("Please enter the length of each side of the triangle.")
for i in range(0, 3):
    sides.append(float(input("Enter a length: ")))

# Calculate area.
s = sum(sides)/2
area = sqrt(s * (s-sides[0]) * (s-sides[1]) * (s-sides[2]))

# Print area.
print(f"The area of the triangle is {area} units squared.")
