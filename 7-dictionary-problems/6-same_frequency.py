# Same Frequency
# Define a function which takes two lists as parameters and 
# check if two given lists have the same frequency of elements.
# Example:
#     list1 = [1, 2, 3, 2, 1]
#     list2 = [3, 1, 2, 1, 3]
#     check_same_frequency(list1, list2)
# Output: False 

# tc: O(n+m)
# sc: O(n+m)
def check_same_frequency(list1, list2):
    merged_1 = {}
    merged_2 = {}
    for item in list1:
        merged_1[item] = merged_1.get(item, 0) + 1
    for item in list2:
        merged_2[item] = merged_2.get(item, 0) + 1
    if merged_2 == merged_1:
        return True
    return False

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
result = check_same_frequency(list1, list2)
print(result)