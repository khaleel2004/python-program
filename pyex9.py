def max_guests_present_within_T_hours(entering, leaving, T):
    # Create a list to store the changes in the number of guests present at each hour
    changes = []

    # Iterate through the entering and leaving arrays and record the changes
    for i in range(len(entering)):
        changes.append((entering[i], 1))
        changes.append((leaving[i], -1))

    # Sort the changes based on the hour
    changes.sort()

    max_guests = 0
    current_guests = 0

    # Iterate through the changes to calculate the maximum number of guests present
    for hour, change in changes:
        current_guests += change
        max_guests = max(max_guests, current_guests)

    return max_guests

# Example usage:
entering = [1, 2, 3, 4, 5]
leaving = [2, 3, 4, 5, 6]
T = 5
print("Maximum number of guests present within T hours:", max_guests_present_within_T_hours(entering, leaving, T))
