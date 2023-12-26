# Best Score
# Given a list, write a function to get first, second best scores from the list.
# List may contain duplicates.
#     myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
#     first_second(myList) # 90 87

# tc: O(n)
# sc: O(1)
def first_second(my_list):
    if my_list[0] >= my_list[1]:
        first = my_list[0]
        second = my_list[1]
    else: 
        first = my_list[1]
        second = my_list[0]
        
    for num in my_list[2:]:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
        
    return first, second

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0,100,100]
result = first_second(myList)
print(result)