# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order. Use sorted().

def sorted_nums(nums):
    nums = sorted(map(int, nums.split()))
    print(nums)


numbers = input()
sorted_nums(numbers)