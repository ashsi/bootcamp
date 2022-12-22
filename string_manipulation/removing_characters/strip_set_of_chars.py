""" Strip a set of characters from a string. """

# Ask user to input string
s = input("Please enter a string: ")

# Ask user which characters to remove from string. No separators between characters.
chars = input("Enter the characters you would like to make disappear: ")

# Print sentence with removed chars
for ch in chars:
    s = s.replace(ch, "")
print(s)
