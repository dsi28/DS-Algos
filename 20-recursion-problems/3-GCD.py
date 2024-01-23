# find the greatest common denominator using recursion

def GCD(a,b,x=-1):
    if (x != -1 and a/x == a//x and b/x == b//x) or x ==1:
        return x
    elif x == -1:
        x = b + 1
    return GCD(a, b, x-1)

def euGCD(a,b):
    if a % b == 0:
        return b
    return euGCD(b, a % b) 

result = euGCD(64,16)
print(result)