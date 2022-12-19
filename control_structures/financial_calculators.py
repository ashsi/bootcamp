""" Investment Calculator and Home Loan Repayment Calculator"""
import math

# User chooses which calculator to use.
print("investment\t- to calculate the amount of interest you'll earn on your investment")
print("bond\t\t- to calculate the amount you'll have to pay on a home loan")
calculator = input("Enter either \'investment\' or \'bond\' from the menu above to proceed: ").lower()

# ----------------------
# Investment calculator.
# ----------------------

# Output: the amount after investment that the user will get back after the given period.
# User inputs variable values.
if calculator == "investment":
    deposit = float(input("Enter the amount of money you are depositing: "))
    rate = float(input("Enter the interest rate as a percentage: ")) / 100
    years = int(input("Enter the number of whole years you are planning on investing: "))
    interest = input("Is the interest \'simple\' or \'compound\'? ").lower()

    # Calculate and display investment.

    # Simple interest investment.
    if interest == "simple":
        total = deposit * (1 + rate * years)
        print(f"Total amount after interest: {total:.2f}")
    # Compound interest investment.
    elif interest == "compound":
        total = deposit * math.pow(1 + rate, years)
        print(f"Total amount after interest: {total:.2f}")
    else:
        print("Error: invalid interest type selected.")

# ----------------
# Bond calculator.
# ----------------

# Output: the amount that will have to be repaid on a home loan each month.
# User inputs variable values.
elif calculator == "bond":
    present_house_value = float(input("Enter the present value of the house: "))
    rate = float(input("Enter the annual interest rate as a percentage: ")) / 100
    months = float(input("Enter the number of months you plan to take to repay the bond: "))

    # Calculate and display how much the user will have to repay each month.
    repayment = (rate * present_house_value) / (1 - (1 + rate / 12) ** (-months))
    print(f"Amount you will have to repay each month: {repayment:.2f}")

# ---------------------------
# Calculator selection error.
# ---------------------------

else:
    print("Error: calculator name entered is invalid.")
