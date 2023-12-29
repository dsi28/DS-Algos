# check if two lists are a permutation of each other
# ex: [1,2,3] , [1,3,2], [2,1,3], [2,3,1], ..

# tc: O(n)
# sc: O(1)
def permutation_check(list_1, list_2):
    if len(list_1) != len(list_2):
        return False
    for item in list_1:
        try:
            list_2.remove(item)
        except:
            return False
    return True    

result = permutation_check([3,1,99,3,3], [3,2,1,3,3])
print(result)

print('xxxxxxxxx')

def permutation_check_2(list_1, list_2):
    if len(list_1) != len(list_2):
        return False
    dict_perm = {} # every key should have a value of 2
    i = 0
    while i < len(list_1):
        if list_1[i] != list_2[i]:
            if list_1[i] not in dict_perm.keys():
                dict_perm[list_1[i]] = 1
            else: 
                dict_perm[list_1[i]] += 1
            if list_2[i] not in dict_perm.keys():
                dict_perm[list_2[i]] = 1
            else: 
                dict_perm[list_2[i]] += 1
        i += 1
    for item in dict_perm.values():
        if item % 2 != 0:
            return False
    return True

result = permutation_check_2([3,1,2,1], [1,1,1,1])
print(result)