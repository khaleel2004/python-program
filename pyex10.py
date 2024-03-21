def modify_string(S):
    # Function to calculate circular distance from 'a'
    def circular_distance(char, freq):
        return chr(((ord(char) - ord('a') + freq) % 26) + ord('a'))

    # Count the frequency of each character
    freq_map = {}
    for char in S:
        freq_map[char] = freq_map.get(char, 0) + 1

    # Replace each character with the modified character
    modified_string = ''
    for char in S:
        modified_string += circular_distance(char, freq_map[char])

    return modified_string

# Example usage:
S = "hello"
print("Modified string:", modify_string(S))
