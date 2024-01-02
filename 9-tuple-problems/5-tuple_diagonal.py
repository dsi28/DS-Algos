# Diagonal
# Create a function that takes a tuple of tuples and 
# returns a tuple containing the diagonal elements of the input.
# Example
#     input_tuple = (
#         (1, 2, 3),
#         (4, 5, 6),
#         (7, 8, 9)
#     )
#     output_tuple = get_diagonal(input_tuple)
#     print(output_tuple)  # Expected output: (1, 5, 9)

def get_diagonal(tup):
    # temp = []
    # for i in range(0, len(tup)):
    #     for j in range(i, len(tup)):
    #         if j == i:
    #             temp.append(tup[i][j])
    # return tuple(temp)
    temp = []
    temp = (tup[i][i] for i in range(len(tup)))
    return tuple(temp)


input_tuple = ((1, 2, 3),(4, 5, 6),(7, 8, 9))
result = get_diagonal(input_tuple)
print(result)