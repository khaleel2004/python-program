def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0

    if arr[0] == 0:
        return -1

    max_reach = arr[0]
    max_index = arr[0]
    jumps = 1

    for i in range(1, n):
        if i > max_reach:
            return -1

        if i > max_index:
            jumps += 1
            max_index = max_reach

        max_reach = max(max_reach, i + arr[i])

    return jumps

# Example usage:
arr = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
print(min_jumps(arr))  # Output: 4
