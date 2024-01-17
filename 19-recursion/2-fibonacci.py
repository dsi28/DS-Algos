


def fibo(n):
    assert n >= 0 and int(n) == n , "n must be posititive integer"
    if n == 0 or n == 1:
        return n
    return fibo(n-1) + fibo(n-2)

result = fibo(1)
print(result)