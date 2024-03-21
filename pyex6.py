def max_area(height):
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        # Calculate the area between the two lines
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)

        # Move the pointer of the shorter line towards the center
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example usage:
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("Maximum area of water that can be contained:", max_area(heights))
