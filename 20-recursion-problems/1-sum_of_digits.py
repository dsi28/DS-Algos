# find sum of digits of a positive number using recursion

def sum_of_digits(num):
    assert int(num) >= 0, "num must be a positive number" 
    num_str = str(num)
    if len(num_str) == 1 or len(num_str) == 0:
        return int(num_str)
    return sum_of_digits(num_str[0]) + sum_of_digits(num_str[1:])

def sum_of_digits_nums(num):
    assert num >= 0, "must be a positive number"  
    if num < 10:
        return num
    mod = num % 10
    next = int(num/10)
    return sum_of_digits_nums(mod) + sum_of_digits_nums(next)

result = sum_of_digits_nums(101010)
print(result)