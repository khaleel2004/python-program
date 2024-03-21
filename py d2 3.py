def max_words_in_sentence(sentences):
    max_words = 0
    
    for sentence in sentences:
        words = sentence.split()  # Split the sentence into words
        max_words = max(max_words, len(words))  # Update max_words if necessary
    
    return max_words

# Example usage:
sentences = ["This is a sample sentence", "Another sentence with more words", "Short sentence"]
print("Maximum number of words in a single sentence:", max_words_in_sentence(sentences))
