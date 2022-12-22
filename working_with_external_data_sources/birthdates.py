""" Print names and DOBs from a text file. """

# Read data from DOB.txt text file and store in two lists.
names = []
birthdates = []
with open("DOB.txt", "r") as f:
    for line in f:
        line_list = line.split()
        names.append(" ".join(line_list[:2]))
        birthdates.append(" ".join(line_list[2:]))

# Print data in two sections with required formatting.
print("\033[1m" + "Name" + "\033[0m")
for name in names:
    print(name)
print()
print("\033[1m" + "Birthdate" + "\033[0m")
for bd in birthdates:
    print(bd)
