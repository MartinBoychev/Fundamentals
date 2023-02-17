# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ",
# and prints all the positive, negative, even, and odd numbers on separate lines as shown below.

nums_as_list = input().split(", ")

positive_nums = [int(num) for num in nums_as_list if int(num) > -1]
negative_nums = [int(num) for num in nums_as_list if int(num) <= -1]
even_nums = [int(num) for num in nums_as_list if int(num) % 2 == 0]
odd_nums = [int(num) for num in nums_as_list if int(num) % 2 != 0]

print(f"Positive: {', '.join(str(num) for num in positive_nums)}")
print(f"Negative: {', '.join(str(num) for num in negative_nums)}")
print(f"Even: {', '.join(str(num) for num in even_nums)}")
print(f"Odd: {', '.join(str(num) for num in odd_nums)}")


