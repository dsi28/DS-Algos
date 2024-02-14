# implement insertion sort
    # 9,8,7,6,5,4
    # key=8, i=1
    # 9,9,7,6,5,4
    # 8,9,7,6,5,4
    # key=7,i=2
    # 8,9,9,6,5,4
    # 8,8,9,6,5,4
    # 7,8,9,6,5,4

def insertionSort(some_list):
    list_len = len(some_list)
    # first loop. from second element to last element in list
        # set key = to value at i. the goal of this is to get key at the
            # correct index from 0..i
        # set j = i-1. since we are going to compare key with values at 
            # indexes before i only. 
    for i in range(1, list_len):
        key = some_list[i]
        j = i-1
        # second loop. while j>-1 and value at j is greater than key
            # if value at j is less than key we found the correct index for key
            # if j<0 then there were no elements smaller than key would be set 
                # at the first index of the list
        while j >= 0 and some_list[j] > key:
            some_list[j+1] = some_list[j]
            j-=1
        # after second loop. set index of key. since j will be either -1 or
            # the value at index j will be less than key you set index of 
            # j+1 = key
        some_list[j+1] = key

test = [10,111,12,8,3,1,2,14]
insertionSort(test)
print(test)