# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print the min and max values of the given numbers and the sum of all the numbers in the list.
# Use min(), max() and sum().

def min_max_sum(nums):
    nums = list(map(int, nums.split()))
    print(f"The minimum number is {min(nums)}")
    print(f"The maximum number is {max(nums)}")
    print(f"The sum number is: {sum(nums)}")


numbers = input()
min_max_sum(numbers)