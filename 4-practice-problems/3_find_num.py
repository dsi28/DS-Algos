# check if a numpy array contains a number
import numpy as np


# tc: O(n)
# sp: O(1)
def find_num(arr, num):
    # if num in arr:
    #     return True
    # return False
    i = 0
    j = len(arr)-1
    while i<=j:
        if arr[i] == num:
            print('found i')
            return i
        if arr[j] == num:
            print('found j') 
            return j
        i+=1
        j-=1
arr = np.array([1,2,34,51,6,78,57,9,5,334])
result = find_num(arr, 78)
print(result)