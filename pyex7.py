def count_sorted_vowel_strings(n):
    # Define a dictionary to store the count of strings ending with each vowel
    counts = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

    # Iterate from the second position to the nth position
    for _ in range(2, n + 1):
        # Update the count for each vowel based on the counts of previous positions
        counts['a'] += counts['e'] + counts['i'] + counts['o'] + counts['u']
        counts['e'] += counts['i'] + counts['o'] + counts['u']
        counts['i'] += counts['o'] + counts['u']
        counts['o'] += counts['u']

    # Sum up the counts for all vowels to get the total count
    total_count = sum(counts.values())

    return total_count

# Example usage:
n = int(input("Enter the length of strings: "))
print("Number of lexicographically sorted vowel strings of length", n, ":", count_sorted_vowel_strings(n))
