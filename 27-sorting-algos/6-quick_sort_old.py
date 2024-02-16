
def pivot(some_list, pivot_index, end_index):
    # set swap index
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        # if cur element is less than pivot
        if some_list[i] < some_list[pivot_index]:
            # increment swap. swap is the last lesser element than the pivot or the pivot
            swap_index += 1
            # swap cur element with pivot.next (which is greater than pivot)
            some_list[i], some_list[swap_index] = some_list[swap_index], some_list[i]
    some_list[pivot_index],some_list[swap_index] = some_list[swap_index],some_list[pivot_index]
    return swap_index


def quickSort(some_list, left, right):
    if left < right:
        pivot_index = pivot(some_list, left, right)
        quickSort(some_list, left, pivot_index-1)
        quickSort(some_list, pivot_index+1, right)
    return some_list

some_list = [9,8,2,10,3,4,5,7,1,6]
pivot(some_list, 0, len(some_list) - 1)
print(some_list)

some_list = [9,8,2,10,3,4,5,7,1,6]
quickSort(some_list, 0, len(some_list)-1)
print(some_list)