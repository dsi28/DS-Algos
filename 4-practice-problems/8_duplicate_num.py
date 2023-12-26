# Duplicate Number
# Write a function to remove the duplicate numbers on given integer array/list.
# Example
#     remove_duplicates([1, 1, 2, 2, 3, 4, 5])
#     Output : [1, 2, 3, 4, 5]

# tc: O(n)
# sc: O(n), becuase clean_arr could be as or almost as long as arr
def remove_duplicates(arr):
    clean_arr = []
    for item in arr:
        if item not in clean_arr:
            clean_arr.append(item)
    return clean_arr

result = remove_duplicates([1, 1, 2, 2, 3, 4, 6,7,5,5])
print(result)