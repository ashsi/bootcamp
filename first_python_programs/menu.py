# Take the user's order.
# Use string.format() method.

print("You will be asked to enter your 3 favourite foods to order.")
item1 = input("Please enter your first food: ")
item2 = input("Please enter your second food: ")
item3 = input("Please enter your third food: ")

print("Order confirmation!")
print("You have ordered: \n{},\n{},\nand {}.".format(item1, item2, item3))
