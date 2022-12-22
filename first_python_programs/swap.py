# Optional Task
# Swapping two numbers from the user.

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

print("\nBefore the swap.")
print(f"num1: {num1}, num2: {num2}\n")

temp = num1
num1 = num2
num2 = temp

print("After the swap.")
print(f"num1: {num1}, num2: {num2}")


# Alternative solution without declaring a temporary variable. 
# Change is in line 27, replacing lines 10-12.

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

print("\nBefore the swap.")
print(f"num1: {num1}, num2: {num2}\n")

num1, num2 = num2, num1

print("After the swap.")
print(f"num1: {num1}, num2: {num2}")
