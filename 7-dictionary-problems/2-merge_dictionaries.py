# Common Keys
# Define a function with takes two dictionaries as parameters 
# and merge them and sum the values of common keys.
# Example:
#     dict1 = {'a': 1, 'b': 2, 'c': 3}
#     dict2 = {'b': 3, 'c': 4, 'd': 5}
#     merge_dicts(dict1, dict2)
# Output:
#     {'a': 1, 'b': 5, 'c': 7, 'd': 5}

# tc: O(n)
# sc: O(1)
def merge_dicts(dict1, dict2):
    for key, value in dict1.items():
        dict2[key] = dict2.get(key,0) + value
    return dict2

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
result = merge_dicts(dict1, dict2)
print(result)