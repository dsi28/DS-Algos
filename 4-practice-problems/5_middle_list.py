# Middle Function
# Write a function called middle that takes a list and 
# returns a new list that contains all but the first and last elements.
#     myList = [1, 2, 3, 4]
#     middle(myList)  # [2,3]

# tc: O(n)
# sc: O(n)
def middle_function(lst):
    return lst[1:len(lst)-1]

myList = [1, 2, 3,8,99,13,172,5,3, 4]
result = middle_function(myList)
print(result)