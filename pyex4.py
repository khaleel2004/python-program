def is_palindrome(x):
    # Convert the integer to a string
    x_str = str(x)
    
    # Check if the string is equal to its reverse
    return x_str == x_str[::-1]

# Example usage:
number = int(input("Enter an integer: "))
print("Is the number a palindrome?", is_palindrome(number))
