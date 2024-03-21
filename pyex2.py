def sumsquare(l):
    odd_sum = 0
    even_sum = 0

    for num in l:
        if num % 2 == 0:  # Even number
            even_sum += num ** 2
        else:  # Odd number
            odd_sum += num ** 2

    return [odd_sum, even_sum]

# Example usage:
num_elements = int(input("Enter the number of elements: "))
input_list = []

for i in range(num_elements):
    num = int(input("Enter the element: "))
    input_list.append(num)

result = sumsquare(input_list)
print("Sum of squares of odd numbers:", result[0])
print("Sum of squares of even numbers:", result[1])
