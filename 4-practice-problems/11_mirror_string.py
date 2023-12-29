# Check if two strings are a mirror of each other
# ex) loop and pool 

# tc: O(n)
# sc: O(1)
def mirror_check(str_1, str_2):
    if len(str_1) == len(str_2):
        i = 0
        j = len(str_1)-1
        while i < len(str_1):
            if str_1[i] != str_2[j]:
                return False
            i += 1
            j -= 1
        return True
    else:
        return False
    
result = mirror_check('loop','pool')
print(result)
