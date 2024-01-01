# Reverse Key-Value Pairs
# Define a function which takes as a parameter dictionary 
# and returns a dictionary in which everse the key-value pairs are reversed.
# Example:
#     my_dict = {'a': 1, 'b': 2, 'c': 3}
#     reverse_dict(my_dict)
# Output:
#     {1: 'a', 2: 'b', 3: 'c'}

# tc: O(n)
# sc: O(n)
def reverse_dict(my_dict):
    # reverse_1 = {}
    # for key, value in my_dict.items():
    #     reverse_1[value] = key
    return {value:key for key, value in my_dict.items()}
    # return reverse_1
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)
result = reverse_dict(my_dict)
print(result)