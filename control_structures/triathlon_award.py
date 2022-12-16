""" Determine Triathlon Award """

# Read in time in minutes for each event
swimming_mins = float(input("Enter the time in minutes for completing the swimming event: "))
cycling_mins = float(input("Enter the time in minutes for completing the cycling event: "))
running_mins = float(input("Enter the time in minutes for completing the running event: "))

# Calculate and display total time
total_mins = swimming_mins + cycling_mins + running_mins
print(f"\nTotal time taken to complete the triathlon: {total_mins}")

# Decide and display award given for this total time
QUALIFYING_TIME = 100
print("Award received: ", end="")
if total_mins <= QUALIFYING_TIME:
    print("Provincial Colours")
elif total_mins <= QUALIFYING_TIME + 5:
    print("Provincial Half Colours")
elif total_mins <= QUALIFYING_TIME + 10:
    print("Provincial Scroll")
else:
    print("No award")
