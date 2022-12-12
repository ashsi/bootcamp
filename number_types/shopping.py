""" Calculate the total and average price of 3 user-given products."""

# Ask for product names.
products = []
print("You will be asked to enter the name of 3 products, one by one.")
for i in range(0, 3):
    products.append(input("Enter a product name: "))
print("Thank you for your product names!\n")

# Ask for product prices.
prices = []
print("You will be asked to enter the prices of each product you named.")
for i in range(0, 3):
    prices.append(float(input(f"Enter the price of {products[i]}: £")))
print("Thank you for entering the prices!\n")

# Calculate the total price.
total = sum(prices)

# Calculate the average price.
avg = round(total/3, 2)

# Print calculations to the user.
print(f"The total of {products[0]}, {products[1]}, {products[2]} is £{total} and the average price of the items is "
      f"£{avg}.")
