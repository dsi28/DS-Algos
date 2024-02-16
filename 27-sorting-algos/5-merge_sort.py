#  implement merge sort

def mergeSort(some_list):
    list_len = len(some_list)

    # BASE case.
    if list_len <= 1:
        return some_list
    
    # split list into two
    mid_index = list_len // 2
    left_l = some_list[0:mid_index]
    right_l = some_list[mid_index:]

    # call mergeSort for each side. recursive call
    sorted_l = mergeSort(left_l)
    sorted_r = mergeSort(right_l)

    # merge both sides
    merged_list = merge(sorted_l,sorted_r)

    return merged_list

def merge(left_l,right_l):
    l_i = 0
    r_i = 0
    l_len = len(left_l)
    r_len = len(right_l) 

    m_list = []

    # merge and sort both lists until one is done.
    while l_i < l_len and r_i < r_len:
        if left_l[l_i] < right_l[r_i]:
            m_list.append(left_l[l_i])
            l_i += 1
        else:
            m_list.append(right_l[r_i])
            r_i += 1
    
    # add any left over items in left list
    while l_i< l_len:
        m_list.append(left_l[l_i])
        l_i += 1
    
    # add any left over items in right list
    while r_i < r_len:
        m_list.append(right_l[r_i])
        r_i += 1

    return m_list


test = [10,111,12,8,3,1,2,14]
print(test)
test = mergeSort(test)
print(test)
