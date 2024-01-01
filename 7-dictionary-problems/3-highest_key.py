# Key with the Highest Value
# Define a function which takes a dictionary as a parameter and 
# returns the key with the highest value in a dictionary.
# Example:
#     my_dict = {'a': 5, 'b': 9, 'c': 2}
#     max_value_key(my_dict)
# Output:
# b 

# tc: O(n)
# sc: O(1)
def max_value_key(my_dict):
    # temp = -1
    # temp_key = -1
    # for key,value in my_dict.items():
    #     if value > temp:
    #         temp = value
    #         temp_key = key
    # return temp_key
    return max(my_dict, key=my_dict.get)

my_dict = {'a': 5, 'b': 9, 'c': 2}
result = max_value_key(my_dict)
print(result)