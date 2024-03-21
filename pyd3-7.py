def permute_unique(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])  # Append a copy of the current permutation
            return
        used = set()  # Track used numbers in this level of recursion
        for i in range(start, len(nums)):
            if nums[i] in used:
                continue  # Skip duplicate numbers
            nums[start], nums[i] = nums[i], nums[start]  # Swap
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # Backtrack (swap back)
            used.add(nums[i])  # Mark the number as used

    result = []
    nums.sort()  # Sort the numbers to handle duplicates
    backtrack(0)
    return result

# Example usage:
nums = [1, 1, 2]
print(permute_unique(nums))
