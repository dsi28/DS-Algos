# implement quick sort.

def quickSort(some_list, left, right):
    if left < right:
        # call pivot
        pivot_index = pivot(some_list, left, right)

        # call quick sort recursively for both sides around pivot. since pivot is sorted
        quickSort(some_list,left, pivot_index-1)
        quickSort(some_list,pivot_index+1,right)



def pivot(some_list, pivot_index, end_index):
    swap_index = pivot_index
    # do not include pivot index and include end_index
    for i in range(pivot_index+1, end_index+1):
        if some_list[i] < some_list[pivot_index]:
            # increase swap index so swap index is set to the first element greater than pivot
            swap_index += 1
            # swap current with new swap index
            some_list[i],some_list[swap_index] = some_list[swap_index],some_list[i]
    # place pivot in correct place so its sorted. swap pivot with last item lesser than pivot
    some_list[pivot_index],some_list[swap_index] = some_list[swap_index],some_list[pivot_index]
    return swap_index



test = [10,111,12,8,3,1,2,14]
quickSort(test, 0, len(test)-1)
print(test)