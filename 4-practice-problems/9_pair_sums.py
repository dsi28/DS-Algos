# Pairs
# Write a function to find all pairs of an integer array whose sum
# is equal to a given number. Do not consider commutative pairs.
# Example
#     pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
#     Output : ['2+5', '4+3', '3+4', '-2+9']
# Note:
# 4+3 comes from second and third elements from the main list.
# 3+4 comes from third and seventh elements from the main list.

# tc: O(n^2)
# sc: O(n)
def pair_sum(myList, sum_num):
    possible_solutions = []
    solutions_list = []
    for num in myList: # O(n)
        temp = sum_num - num
        if temp in possible_solutions: #O(n)
            solutions_list.append(f'{temp}+{num}')
        if num not in possible_solutions: # not needed tbh
            possible_solutions.append(num)
    print(solutions_list)
    return solutions_list

pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
