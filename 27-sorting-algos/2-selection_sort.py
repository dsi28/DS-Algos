#  implement selection sort

def selectionSort(some_list):
    list_len = len(some_list)
    # first loop goes from 0 to second last index in list
        # set min = i
    for i in range(0, list_len-1):
        temp_min = i
        # second loop goes from i.next to last element in list.
            # since i is the temp min no need to go through i
            # if the value at j is less than value at min, then update min = j
        for j in range(i+1, list_len):
            if some_list[j] < some_list[temp_min]:
                temp_min = j
        # swap value at i with value at min. this moves the lowest unsorted value to the front
        some_list[i],some_list[temp_min]=some_list[temp_min],some_list[i]

test = [10,111,12,8,3,1,2,14]
selectionSort(test)
print(test)