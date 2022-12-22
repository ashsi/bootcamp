""" Tell the user what they already know because they just told you. """


# Get user's favourite restaurant.
fav_rest = input("Please enter the name of your favourite restaurant:\n")
print("")

# Get user's favourite number.
int_fav = input("Please enter your favourite whole number: ")
print("")

# Print these
print(f"Your favourite restaurant is {fav_rest}.")
print(f"Your favourite number is {int_fav}.")


## Try to cast fav_rest to an int
"""
Error thrown when casting fav_rest to an integer:
    ValueError: invalid literal for int() with base 10: 'Wagamamas'
Explanation:
    string.int() only casts strings that contain only numerals to ints
    this restaurant name contains non-numeral chars, so it cannot be an int.
"""
# int(fav_rest)

