# implment bucket sort
import math

def bucketSort(some_list):
    list_len = len(some_list)
    list_len = round(math.sqrt(list_len))
    buckets = []
    # create empty list of buckets
    for _ in some_list:
        buckets.append([])

    # insert items from og list into calculated bucket
    max_val = max(some_list)
    for item in some_list:
        insert_index = math.ceil((item * list_len) / max_val)
        insert_index = max(0, min(insert_index, list_len-1))
        print(insert_index)
        buckets[insert_index].append(item)
    
    # sort all buckets
    for bucket in buckets:
        # use algo of choice
        insertionSort(bucket)
    
    # put sorted buckets together back into original list
    i = 0
    for bucket in buckets:
        for item in bucket:
            some_list[i] = item
            i+=1

def insertionSort(s_list):
    list_len = len(s_list)
    for i in range(1, list_len):
        key = s_list[i]
        j = i-1
        while j > -1 and s_list[j] > key:
            s_list[j+1] = s_list[j]
            j-=1
        s_list[j+1] = key
    # return s_list

def bubbleSort(s_list):
    len_s = len(s_list)
    for i in range (0, len_s):
        for j in range(0, len_s-i-1): #-1 to since we do not want to compare index at len with len + 1
            if s_list[j] > s_list[j+1]:
                s_list[j],s_list[j+1] = s_list[j+1],s_list[j]

def selectionSort(s_list):
    s_len = len(s_list)
    for i in range(0, s_len):
        temp_min = i
        for j in range(1+i,s_len):
            if s_list[j]<s_list[temp_min]:
                temp_min = j
        s_list[i],s_list[temp_min]=s_list[temp_min],s_list[i]


test = [10,111,12,8,3,1,2,14]
print(test)
bucketSort(test)
print(test)