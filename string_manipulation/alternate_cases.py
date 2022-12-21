""" Alternate lowercase and uppercase in a user-given string. """

# Read in string1 from user.
string1 = input("Enter a sentence: ")

# Print string with alternate lowercase and uppercase CHARACTERS
string1_alt_builder = ""
for i in range(0, len(string1)):
    if i % 2 == 0:
        string1_alt_builder += string1[i].upper()
    else:
        string1_alt_builder += string1[i].lower()
print(string1_alt_builder)

# Print string with alternate lowercase and uppercase WORDS
# Use the same string from string1 or set string2 on line 17.
string2 = string1
string2_list = string2.split()
for i in range(0, len(string2_list)):
    if i % 2 == 0:
        string2_list[i] = string2_list[i].lower()
    else:
        string2_list[i] = string2_list[i].upper()
print(" ".join(string2_list))
