""" String manipulation. """

# Get sentence from user.
str_manip = input("Please enter a sentence:\n")

# Output length.
length = len(str_manip)
print(length)

# Replace every occurrence of last letter with "@".
print(str_manip.replace(str_manip[-1], "@"))

# Last 3 characters backwards.
print(str_manip[-1:-4:-1])

# Create a 5 letter word, from first 3 chars and last 2 chars.
print(str_manip[:3] + str_manip[-1:-3:-1])

# Display each word on a new line.
print(str_manip.replace(" ", "\n"))
