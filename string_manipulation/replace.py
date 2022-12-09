"""Using string.replace()"""


# Original sentence
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

# Update sentence without exclamation marks. Print sentence.
sentence = sentence.replace("!", " ").replace(" .", ".")
print(sentence)

# Print sentence in capital letters.
print(sentence.upper())

# Print sentence reversed.
print(sentence[::-1])
