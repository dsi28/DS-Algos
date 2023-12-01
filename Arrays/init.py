import array 
# empty array
# space(memory) complexity is O(1) 
# time complexity is O(1) since the time for allocating it is minimal
my_array = array.array('i') 
print(my_array)
# array with elements
# space(memory) complexity is O(N) memory needed to store elements increases based on n 
# time complexity is O(1) since the time for creating increases depending on n
my_array = array.array('i',[1,2,3,4,5,6])
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
np_array = np.array([1,2,3,4,5,6,7])
print(np_array)