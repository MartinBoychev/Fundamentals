# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().

def even_numbers(num):
    num = list(map(int, num.split()))
    even_nums = list(filter(lambda x: x % 2 == 0, num))
    return even_nums


numbers = input()
print(even_numbers(numbers))
