

# tc: O(n)
# sc: O(n)
def twoSum(nums, target):
    possible_solutions = []
    count = 0
    while count < len(nums):
        temp = target - nums[count]
        if nums[count] in possible_solutions:
            if nums[count] != temp:
                return [count,nums.index(temp)]
            else:
                return [count, nums[0:count].index(temp)]
        possible_solutions.append(temp)
        count+=1

solution = twoSum([2,7,11,15],9)
print(solution)
           