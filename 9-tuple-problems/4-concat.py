# Concatenate
# Write a function that takes a tuple of strings and 
# concatenates them, separating each string with a space.
# Example
#     input_tuple = ('Hello', 'World', 'from', 'Python')
#     output_string = concatenate_strings(input_tuple)
#     print(output_string)  # Expected output: 'Hello World from Python'


# tc: O(n)
# sc: O(n)
def concatenate_strings(input_tuple):
    # temp = ''
    # for i in range(0, len(input_tuple)):
    #     temp += input_tuple[i]
    #     if i != len(input_tuple) - 1:
    #         temp += ' '
    # return temp
    return ' '.join(input_tuple)

input_tuple = ('Hello', 'World', 'from', 'Python')
result = concatenate_strings(input_tuple)
print(result) 