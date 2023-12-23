import array 

# empty array
# space(memory) complexity is O(1) 
# time complexity is O(1) since the time for allocating it is minimal
my_array = array.array('i') 
print(my_array)

# array with elements
# space(memory) complexity is O(N) memory needed to store elements increases based on n 
# time complexity is O(1) since the time for creating increases depending on n
my_array = array.array('i',[1,2,3,4,4,5,6])
print(my_array)

import numpy  as np

# empty array
# space(memory) complexity is O(1) 
# time complexity is O(1) since the time for allocating it is minimal
np_array = np.array([], dtype=int)
print(np_array)

# array with elements
# space(memory) complexity is O(N) memory needed to store elements increases based on n 
# time complexity is O(1) since the time for creating increases depending on n
np_array = np.array([1,2,2,33,3,4,5,6,7])
print(np_array)


# Insert
# time complexity is O(n) becuase worst case it will move every element if inserted at 0 index
# space complexity is O(1) becuase only a constant number will be added to memeory
my_array.insert(2,77)
print(my_array)


# traverse array
# space complexity is O(n)
def traverseArray(ar):
    # time complexity is O(n) becuase time will increase while number of elements increases
    # space complexity is O(n) do not need extra memory location to perform this
    for i in ar:
        # time complexity is O(1) becuase only one item printed. does not matter
        print(i)

traverseArray(my_array)


# accessing an element in an array
# time complexity is O(1)
# space complexity is O(1)
def accessEle(ar, index):
    if index < len(ar):
        print(ar, index)
    else: 
        print('not a valid index')

accessEle(my_array, 2)
accessEle(my_array,22)



def linear_search(arr, target):
    for i in range(len(arr)):  # time commplexity O(n), space complexity is O(1)
        if arr[i] == target: # O(1)
            return i
    return -1

print("linear_search", my_array)
print(linear_search(my_array, 5))