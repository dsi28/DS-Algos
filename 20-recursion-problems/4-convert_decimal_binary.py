# convert a decimal number to binary

def dToB(num, bin=""):
    if num <= 0:
        return bin[::-1]
    bin += str(num % 2)
    return dToB(num//2,bin)

result = dToB(100)
print(result)