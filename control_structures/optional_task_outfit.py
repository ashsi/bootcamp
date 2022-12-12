""" Help user decide what to wear based on weather and whether it is the weekend. """


# Declare 3 bool conditions that effect decision of what to wear.
is_temp_over_20 = False
is_weekend = False
is_sunny = False

# Prepare user for yes/no questions to set bools.
print("Please enter yes or no when answering the following questions to decide your outfit.")

# Set is_temp_over_20
temp = input("Is the temperature over 20 degrees? ").strip(".").lower()
if temp == "yes":
    is_temp_over_20 = True

# Set is_weekend
weekend = input("Is it the weekend? ").strip(".").lower()
if weekend == "yes":
    is_weekend = True

# Set is_sunny
sunny = input("Is it sunny? ").strip(".").lower()
if sunny == "yes":
    is_sunny = True

# Decide shirt.
if is_temp_over_20:
    shirt = "short-sleeved"
else:
    shirt = "long-sleeved"

# Decide trousers.
if is_weekend:
    trous = "shorts"
else:
    trous = "jeans"

# Decide accessory.
if is_sunny:
    acc = "cap"
else:
    acc = "raincoat"

# Tell the user what to wear.
print(f"Then, today you should wear a {shirt} shirt, {trous}, and a {acc}.")
