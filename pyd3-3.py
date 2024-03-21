def num_identical_pairs(nums):
    num_counts = {}
    good_pairs = 0

    # Count the occurrences of each number
    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    # Calculate the number of good pairs for each number
    for count in num_counts.values():
        good_pairs += (count * (count - 1)) // 2

    return good_pairs

# Example usage:
nums = [1, 2, 3, 1, 1, 3]
print(num_identical_pairs(nums))  # Output: 4
