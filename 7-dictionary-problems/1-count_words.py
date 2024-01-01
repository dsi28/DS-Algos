# Count Word Frequency
# Define a function to count the frequency of words in a given list of words.
# Example:
#     words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
#     count_word_frequency(words) 
# Output:
#      {'apple': 3, 'orange': 2, 'banana': 1}

# TC: O(n)
# SC: O(n)
def count_word_frequency(words):
    output_words = {}
    for word in words:
        # if word not in output_words:
        #     output_words['word'] = 1
        # else:
        #     output_words['word'] += 1
        output_words[word] = output_words.get(word, 0) + 1
    return output_words

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
result = count_word_frequency(words)     
print(result)