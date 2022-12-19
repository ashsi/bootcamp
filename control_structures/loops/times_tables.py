""" Display A Times Table """

# User picks number for times table
print("This program prints the times table for the number you choose.")
num = int(input("Please enter a number: "))

# Print times table
for mult in range(1, 13):
    print(f"{num} x {mult}\t= {num * mult}")
