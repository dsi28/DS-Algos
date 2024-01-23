# calculate power of a number using recursion

def powerOfNum(num, power):
    if power == 1:
        return num
    elif power == 0:
        return 1
    return powerOfNum(num,power - 1) * num

result = powerOfNum(3, 3)
print(result)