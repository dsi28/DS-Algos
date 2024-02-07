def heapify(some_list, len_list, parent_index):
    min_index = parent_index
    child_left = parent_index * 2 + 1
    child_right = parent_index * 2 + 2
    
    if child_left < len_list and some_list[child_left] < some_list[min_index]:
        min_index = child_left
    
    if child_right < len_list and some_list[child_right] < some_list[min_index]:
        min_index = child_right

    if min_index != parent_index:
        # swap value at min with value at parent
        some_list[min_index], some_list[parent_index] = some_list[parent_index], some_list[min_index]
        # call heapify for new child sub tree. min index is the index of the child that was less than the parent at the start of this function 
        heapify(some_list, len_list, min_index)



# Initial Heap Property:
    # Initially, the input list is transformed into a max-heap, 
        # where the maximum element is at the root (index 0), and the elements below it satisfy the heap property (parent nodes are greater than or equal to their children).
# Swapping:
    # In each iteration of the sorting phase, we swap the root (maximum element) 
        # with the last element in the unsorted portion of the list (index i). 
        # This effectively moves the maximum element to the end of the list, but it's not yet in its correct sorted position.
# Heap Property Violation:
    # After the swap, the heap property is violated at the root because the 
        # maximum element is no longer at its original position.
# Re-Heapification:
    # To restore the heap property, we need to heapify the heap again. 
        # This involves "sinking down" the root element to its correct 
        # position within the heap, ensuring that the largest element remains at the root.
# Sorted Order:
    # After each iteration of swapping and re-heapification, 
        # the largest element in the unsorted portion of the list 
        # (which was originally the root) is placed at the end of the list. 
        # As we repeat this process, the sorted portion of the list grows from 
        # the end towards the beginning.
# Completion:
    # Once all iterations are complete, the entire list is sorted in ascending order.

def heapSort(some_list):
    list_len = len(some_list)
    #  this loop heapifs the list
    for i in range(int(list_len/2)-1, -1, -1):
        heapify(some_list, list_len, i)
    

    for i in range(list_len-1, 0, -1):
        some_list[i],some_list[0] = some_list[0], some_list[i]
        heapify(some_list, i, 0)


some_list = [9,8,2,10,3,4,5,7,1,6]
heapSort(some_list)
print(some_list)