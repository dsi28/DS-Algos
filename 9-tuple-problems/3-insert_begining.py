# Insert at the Beginning
# Write a function that takes a tuple and a value, 
# and returns a new tuple with the value inserted at the beginning of the original tuple.
# Example
#     input_tuple = (2, 3, 4)
#     value_to_insert = 1
#     output_tuple = insert_value_front(input_tuple, value_to_insert)
#     print(output_tuple)  # Expected output: (1, 2, 3, 4)

# tc: O(n)
# sc: O(n)
def insert_value_front(input_tuple, value_to_insert):
    # temp = list(input_tuple)
    # temp.insert(0,value_to_insert)
    # return tuple(temp)
    return (value_to_insert,) + input_tuple

input_tuple = (2, 3, 4)
value_to_insert = 1
result = insert_value_front(input_tuple, value_to_insert)
print(result)