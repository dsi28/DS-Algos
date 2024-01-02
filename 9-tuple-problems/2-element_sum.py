# Elementwise Sum
# Create a function that takes two tuples and 
# returns a tuple containing the element-wise sum of the input tuples.
# Example
#     tuple1 = (1, 2, 3)
#     tuple2 = (4, 5, 6)
#     output_tuple = tuple_elementwise_sum(tuple1, tuple2)
#     print(output_tuple)  # Expected output: (5, 7, 9)

# tc: O(n)
# sp: O(n)
def tuple_elementwise_sum(tuple1, tuple2):
    # in case the lengths are the same use zip()
    # return tuple(map(sum, zip(tuple1, tuple2)))

    # in case the lengths can be different use
    tuple_a = None
    tuple_b = None
    if len(tuple1) >= len(tuple2):
        tuple_a = tuple1
        tuple_b = tuple2
    else:
        tuple_a = tuple2
        tuple_b = tuple1
    sum_list = []
    for i in range(0, len(tuple_b)):
        sum_list.append(tuple_b[i] + tuple_a[i])
    if len(tuple_a) > len(tuple_b):
        for i in tuple_a[len(tuple_b) - 1:len(tuple_a)]:
            sum_list.append(i)
    return tuple(sum_list)