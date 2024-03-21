def calculate(s):
    stack = []
    num = 0
    sign = '+'
    
    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)
        if (not char.isdigit() and char != ' ') or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] *= num
            elif sign == '/':
                stack[-1] = int(stack[-1] / num)
            sign = char
            num = 0

    return sum(stack)

# Example usage:
s = "3 + 2 * 2"
print("Result:", calculate(s))  # Output: 7
