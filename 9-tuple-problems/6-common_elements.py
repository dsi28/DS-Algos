# Common Elements
# Write a function that takes two tuples and returns a 
# tuple containing the common elements of the input tuples.
# Example
#     tuple1 = (1, 2, 3, 4, 5)
#     tuple2 = (4, 5, 6, 7, 8)
#     output_tuple = common_elements(tuple1, tuple2)
#     print(output_tuple)  # Expected output: (4, 5)

# tc: O(n*m)
# sc: O(n)
def common_elements(tuple1, tuple2):
    # return tuple(a for a,b in zip(tuple1,tuple2) if a==b)
    temp = []
    found_b = []
    found_a = []
    for a in range(len(tuple1)):
        for b in range(len(tuple2)):
            if tuple2[b] == tuple1[a] and (b not in found_b) and (a not in found_a):
                temp.append(tuple2[b])
                found_b.append(b)
                found_a.append(a)
    return tuple(temp)

tuple1 = (1, 2, 3, 4, 5,1, 2, 4,5)
tuple2 = (4, 5, 6, 7, 8,4)
result = common_elements(tuple1, tuple2)
print(result)  # Expected output: (4, 5)
