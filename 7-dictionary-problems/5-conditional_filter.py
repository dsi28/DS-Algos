# Conditional Filter
# Define a function that takes a dictionary as a parameter and returns 
# a dictionary with elements based on a condition.
# Example:
#     my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
#     filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0) 
# Output:
#     {'b': 2, 'd': 4}

# TC: O(n)
# SC: O(n)
def filter_dict(my_dict, condition):
    return {key:value for key,value in my_dict.items() if condition(key,value)}

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
result = filter_dict(my_dict, lambda k, v: v % 2 == 0)
print(result)