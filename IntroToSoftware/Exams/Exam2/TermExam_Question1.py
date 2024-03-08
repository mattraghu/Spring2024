def median_fun(nums = None):
    if not nums:
        nums = input("Enter the numbers for median (seperate by commas): ")
        nums = nums.split(",")
    nums = [int(i) for i in nums]
    nums.sort()
    mid = len(nums) // 2
    if len(nums) % 2 == 0:
        median = (nums[mid] + nums[mid - 1]) / 2
    else:
        median = nums[mid]
    return median

def mean_fun(nums=None):
    if not nums: 
        nums = input("Enter the numbers for mean (seperate by commas): ")
        nums = nums.split(",")
        nums = [int(i) for i in nums]
    n = len(nums)
    total = 0
    for num in nums:
        total += num
    return total / n

def standardDerviation_fun(nums = None):
    if not nums:
        nums = input("Enter the numbers for standard dev (seperate by commas): ")
        nums = nums.split(",")
    nums = [int(i) for i in nums]

    mean = mean_fun(nums)
    n = len(nums)

    sum_of_squares = 0
    for num in nums:
        sum_of_squares += (num - mean) ** 2

    return (sum_of_squares / (n - 1)) ** 0.5

print(median_fun())
print(mean_fun())
print(standardDerviation_fun())





