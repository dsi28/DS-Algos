# implment bubble sort
import math


# tc: O(n^2), sc: O(1)
def bubbleSort(in_list):
    for i in range(len(in_list) - 1):
        if i == 9:
            print(i)
        for j in range(len(in_list) - i - 1):
            if i == 9 or j == 9:
                print(i, j)
            if in_list[j] > in_list[j + 1]:
                in_list[j], in_list[j + 1] = in_list[j + 1], in_list[j]
    print('bubble sort: ',in_list)

# tc: O(n^2), sc: O(1)
def selectionSort(in_list):
    for i in range(0, len(in_list)):
        temp_min = i
        for j in range(i + 1, len(in_list)):
            if in_list[j] < in_list[temp_min]:
                temp_min = j
        in_list[i], in_list[temp_min] = in_list[temp_min], in_list[i]
    print('selection sort: ', in_list)

# tc: O(n^2), sc: O(1)
def inserstionSort(in_list, is_solo):
    for i in range(1, len(in_list)):
        key = in_list[i]
        j = i - 1
        while j >= 0 and key < in_list[j]:
            in_list[j + 1] = in_list[j]
            j -= 1
        in_list[j + 1] = key
    if is_solo:
        print('insersion sort: ', in_list)
    return in_list

# tc: O(n^2), sc: O(n)
def bucketSort(in_list):
    num_buckets = round(math.sqrt(len(in_list)))
    temp_list = []
    max_value = max(in_list)

    # create buckets
    for _ in range(num_buckets):
        temp_list.append([])

    # insert items into buckets
    for item in in_list:
        insert_index = math.ceil((item * num_buckets) / max_value)
        temp_list[insert_index - 1].append(item)

    # sort buckets
    for sub_arr in temp_list:
        sub_arr = inserstionSort(sub_arr, False)

    # merge buckets
    i = 0
    for sub_arr in temp_list:
        for item in sub_arr:
            in_list[i] = item
            i += 1
    
    print('bucket sort: ', in_list)




some_list = [9,8,2,10,3,4,5,7,1,6]
bubbleSort(some_list)
some_list = [9,8,2,10,3,4,5,7,1,6]
selectionSort(some_list)
some_list = [9,8,2,10,3,4,5,7,1,6]
inserstionSort(some_list, True)
some_list = [9,8,2,10,3,4,5,7,1,6]
bucketSort(some_list)