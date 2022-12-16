""" Calculate the area that the foundation of a building covers. """
from math import pi

# Ask user to choose shape of the building foundation.
shape = input("Please give the shape of the building foundation.\nEnter 0 for square, 1 for rectangular,"
              " or 2 for round: ")

# Prepare user for inputting the dimensions appropriate to the shape.
print("You will now be asked to enter the dimensions of the building's foundation, in the unit measurement of choice.")

# Case 0: Square
if shape == "0":
    # Get dimensions.
    length = float(input("Please enter the length of the square: "))
    # Calculate and display the area.
    print(f"The area is {length ** 2:.4f} units squared (to 4d.p.).")

# Case 1: Rectangle
elif shape == "1":
    # Get dimensions.
    length = float(input("Please enter the length of the rectangle: "))
    width = float(input("Please enter the width of the rectangle: "))
    # Calculate and display the area.
    print(f"The area is {length * width:.4f} units squared (to 4d.p.).")

# Case 2: Circle
elif shape == "2":
    # Get dimensions.
    radius = float(input("Please enter the radiu"
                         "s of the circle: "))
    # Calculate and display the area.
    print(f"The area is {pi * radius ** 2:.4f} units squared (to 4d.p.).")

# Error in initial user input.
else:
    print("Error: You didn't enter 0, 1, or 2.")
