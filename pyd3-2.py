import itertools

def find_combinations(digits):
    if len(digits) != 3:
        return "Please enter exactly 3 digits."

    combinations = list(itertools.permutations(digits, 3))

    return combinations

# Example usage:
digits = input("Enter 3 digits separated by spaces: ").split()
combinations = find_combinations(digits)
print("Possible combinations:", combinations)
