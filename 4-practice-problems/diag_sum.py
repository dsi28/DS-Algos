# 2D Lists
# Given 2D list calculate the sum of diagonal elements.
# Example
#     myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
#     diagonal_sum(myList2D) # 15


# tc: O(n)
# sc: O(1)
def diagonal_sum(matrix):
    i = 0
    sum_matrix = 0
    while i < len(matrix):
        sum_matrix += matrix[i][i]
        i += 1
    return sum_matrix

myList2D= [[1,73,22],[88,5,32],[78,10,52]] 
result = diagonal_sum(myList2D) 
print(result)