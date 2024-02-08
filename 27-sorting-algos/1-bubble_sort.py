# implment bubble sort

def bubbleSort(some_list):
    list_len = len(some_list)
    # outer loop 0 - last index of list
    for i in range(0, list_len):
        # inner loop 0 - last index-i-1. 
            # -i: because after every iteration you move the largest element 
                # to the end so there is no need to compare last/sorted element(s) again
            # -1: becuase when i=0, j+1 can be out of range
        # after every iteration the largest element is moved to end of list
        for j in range(0, list_len-i-1):
            if some_list[j] > some_list[j+1]:
                some_list[j],some_list[j+1] = some_list[j+1],some_list[j]

test = [10,111,12,8,3,1,2,14]
bubbleSort(test)
print(test)