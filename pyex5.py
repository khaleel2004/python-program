# Price of a loaf of bread
regular_price = 185

# Discount percentage for day-old bread
discount_percentage = 60

# Read the number of loaves of day-old bread from the user
num_loaves = int(input("Enter the number of loaves of day-old bread: "))

# Calculate the regular price, discount, and total price
regular_total = num_loaves * regular_price
discount_amount = regular_total * (discount_percentage / 100)
total_price = regular_total - discount_amount

# Display the results with two decimal places aligned properly
print("Regular Price:   {:10.2f} rupees".format(regular_total))
print("Discount:        {:10.2f} rupees".format(discount_amount))
print("Total Price:     {:10.2f} rupees".format(total_price))
