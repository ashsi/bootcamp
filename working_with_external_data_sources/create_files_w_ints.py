""" Create files with sorted integers. """


# Define a function that creates a file containing ints.
def create_file(filename: str, a: list[int]):
    with open(filename, "w") as f:
        f.write(" ".join([str(item) for item in a]))


# Create the first text file.
ints1 = sorted([3, 4, 1, 8, 4, 9, 10, 2, 33, 1])
create_file("numbers1.txt", ints1)

# Create the second text file.
ints2 = sorted([4, 104, 22, 9, 6, 111, 77])
create_file("numbers2.txt", ints2)

# Create a file containing all the integers in ascending order.
all_ints = sorted(ints1 + ints2)
create_file("all_numbers.txt", all_ints)
