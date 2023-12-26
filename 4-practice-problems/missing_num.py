# Missing Number
# Write a function to find the missing number in a given integer array of 1 to 100. 
# The function takes to parameter the array and the number of elements 
# that needs to be in array. 
# For example if we want to find missing number from 1 to 6 
# the second parameter will be 6.

# Example:missing_number([1, 2, 3, 4, 6], 6) # 5

# tc: O(n)
# sc: O(1)
def missing_number(arr, n):
    current = arr[0]
    for num in arr:
        if num == current:
            current += 1
        else:
            return current
    return current # since 1 is the starter

missing_num = missing_number([1,2,3,4,5], 6)
print(missing_num)

# tc: ~O(n)
# sc: O(1)
def missing_number_2(arr, n):
    sum_n = 0
    for i in range(1,n+1):
        sum_n += i
    sum_missing = 0
    for i in arr:
        sum_missing+=i
    return sum_n - sum_missing

missing_num_2 = missing_number_2([1,2,3,5,6], 6)
print(missing_num_2)
