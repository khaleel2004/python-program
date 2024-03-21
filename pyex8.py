def is_valid_number(s):
    # Function to check if a string represents an integer
    def is_integer(s):
        if not s:
            return False
        if s[0] in ['+', '-']:
            s = s[1:]
        return s.isdigit()

    # Function to check if a string represents a decimal number
    def is_decimal(s):
        if not s or s == '.':
            return False
        if s[0] in ['+', '-']:
            s = s[1:]
        parts = s.split('.')
        if len(parts) > 2:
            return False
        return (parts[0].isdigit() or parts[0] == '') and (len(parts) == 1 or parts[1].isdigit())

    # Skip leading and trailing whitespaces
    s = s.strip()

    # Check for empty string
    if not s:
        return False

    # Check for optional sign character
    if s[0] in ['+', '-']:
        s = s[1:]

    # Check for decimal number or integer
    if '.' in s:
        parts = s.split('e')
        if len(parts) > 2:
            return False
        if len(parts) == 1:
            return is_decimal(parts[0])
        else:
            return is_decimal(parts[0]) and is_integer(parts[1])
    else:
        parts = s.split('e')
        if len(parts) > 2:
            return False
        return is_integer(parts[0]) and (len(parts) == 1 or is_integer(parts[1]))

# Example usage:
test_cases = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

for test_case in test_cases:
    print(f'"{test_case}" is valid:', is_valid_number(test_case))
