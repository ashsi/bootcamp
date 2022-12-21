""" Determine whether a word is a palindrome. """

# Get word from user.
print("This is a palindrome checker.")
word = input("Please enter a word: ")

# Check and print whether word is a palindrome
# Checks first half of word is equal to second half reversed, excluding any middle letter
midpoint = len(word) // 2
if len(word) % 2 == 0:
    reversed_half = word[:midpoint-1:-1]
else:
    reversed_half = word[:midpoint:-1]
if word[:midpoint] == reversed_half:
    print("Your word is a palindrome.")
else:
    print("Your word is not a palindrome.")

