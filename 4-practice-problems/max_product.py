# Max Product of Two Integers
# Find the maximum product of two integers in 
# an array where all elements are positive.
# Example)
#     arr = [1, 7, 3, 4, 9, 5] 
#     max_product(arr) # Output: 63 (9*7)


# tc: O(n)
# sc: O(1)
def max_product(arr): 
    # arr.sort(reverse=True)
    # return arr[0]*arr[1]
    if arr[0] >= arr[1]:
        max_1 = arr[0]
        max_2 = arr[1]
    else:
        max_1 = arr[1]
        max_2 = arr[0]
    
    for num in arr[2:len(arr)]:
        if num >= max_1:
            max_2 = max_1
            max_1 = num
        elif num>max_2:
            max_2=num
    return max_1*max_2

arr = [1, 7, 3, 4, 9, 10] 
result = max_product(arr)
print(result)