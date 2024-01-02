# Sum and Product
# Write a function that calculates the sum and product 
# of all elements in a tuple of numbers.
# Example
#     input_tuple = (1, 2, 3, 4)
#     sum_result, product_result = sum_product(input_tuple)
#     print(sum_result, product_result)  # Expected output: 10, 24

# tc: O(n)
# sc: O(1)
def sum_product(input_tuple):
    #{sum(i) for i in input_tuple}
    temp = 1
    sum_t = 0
    for i in input_tuple:
        temp *= i
        sum_t += i
    return sum_t,temp

input_tuple = (1, 2, 3, 4)
result = sum_product(input_tuple)
print(result)  