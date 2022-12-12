"""Simple calculations on n=3 user-inputted integers."""

# Number of integers.
n = 3

# Store integers given by user in a list.
ints = []
print(f"You will be asked to enter {n} integers.")
for i in range(0, n):
    ints.append(int(input("Enter an integer: ")))
print("Thank you for your integers!\n")

# Print sum.
print("Sum:")
ints_sum = sum(ints)
print(ints_sum)

# Print first number minus second number.
print("First int - Second int:")
print(ints[0]-ints[1])

# Print third number * first number.
print("Third int * First int:")
print(ints[2]*ints[0])

# Sum of all numbers divided by the third number.
print(f"Sum of all {n} ints divided by the third int:")
print(ints_sum/ints[2])
