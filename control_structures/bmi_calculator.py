""" Calculate user's BMI. """

# Take weight and height from user.
weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in m: "))

# Calculate BMI.
bmi = weight/(height*height)

# Decide category of BMI.
if bmi >= 30.0:
    cat = "obese"
elif bmi >= 25.0:
    cat = "overweight"
elif bmi >= 18.5:
    cat = "normal"
else:
    cat = "underweight"

# Display user's BMI and category.
print(f"Your BMI is {bmi:.2f}.\nBased on your BMI, you are {cat}.")
