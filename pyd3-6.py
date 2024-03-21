def is_mirror_number(number):
    reverse_number = number[::-1]  # Reverse the number
    return number == reverse_number

# Example usage:
number = input("Enter a number: ")
if is_mirror_number(number):
    print("The number is already a mirror number.")
else:
    print("The number is not a mirror number.")
