def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    mapping = {}
    mapped_chars = set()

    for char_s, char_t in zip(s, t):
        if char_s not in mapping:
            if char_t in mapped_chars:
                return False
            mapping[char_s] = char_t
            mapped_chars.add(char_t)
        else:
            if mapping[char_s] != char_t:
                return False

    return True

# Example usage:
s1 = "egg"
t1 = "add"
print(is_isomorphic(s1, t1))  # Output: True

s2 = "foo"
t2 = "bar"
print(is_isomorphic(s2, t2))  # Output: False
