def is_happy(n):
    seen = set()

    while n != 1:
        n_str = str(n)
        n = sum(int(digit)**2 for digit in n_str)
        
        if n in seen:
            return False
        seen.add(n)

    return True

# Example usage:
number = int(input("Enter a number: "))
print("Is the number happy?", is_happy(number))
