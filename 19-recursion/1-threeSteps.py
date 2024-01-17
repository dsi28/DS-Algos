#  write a recursive method for calculating factorial of a given integer

def fact(n):
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        return n * fact(n - 1)
    print('n must be a positive integer')

result = fact(-1)
print(result)