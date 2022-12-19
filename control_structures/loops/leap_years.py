""" Check for leap years. """

# User inputs parameters: start year, # years to check
start = int(input("What year do you want to start with?\t"))
total_years = int(input("How many years do you want to check?\t"))

# Determine and display whether each year is a leap year
end = start + total_years
for year in range(start, end):
    if year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} isn't a leap year")
