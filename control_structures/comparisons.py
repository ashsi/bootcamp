""" Comparisons on 3 numbers. """

# Instantiate 3 number variables.
num1, num2, num3 = 10, 33, 56

# Display the larger value of {num1, num2}.
if num1 > num2:
    print(f"num1 {num1} is larger than num2 {num2}.")
elif num2 > num1:
    print(f"num2 {num2} is larger than num1 {num1}.")
else:
    print(f"num1 and num2 have the same value: {num1}")

# Display whether num1 is odd or even.
print("Is num1 odd or even?")
if num1 % 2 == 0:
    print("even")
else:
    print("odd")

# Display the three numbers from largest to smallest.
print("Numbers from largest to smallest:")
if num3 >= num2:
    if num2 >= num1:
        print(f"{num3}, {num2}, {num1}")
    elif num3 >= num1:
        print(f"{num3}, {num1}, {num2}")
    else:
        print(f"{num1}, {num3}, {num2}")
else:
    # num2 > num3
    if num1 >= num2:
        print(f"{num1}, {num2}, {num3}")
    elif num1 >= num3:
        print(f"{num2}, {num1}, {num3}")
    else:
        print(f"{num2}, {num3}, {num1}")
