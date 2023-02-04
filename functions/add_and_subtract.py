# You will receive three integer numbers. Write functions named: sum_numbers() that returns the sum of the first two
# integers subtract() that returns the difference between the returned result of the first function and the third
# integer Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as
# parameters. Print the result of the subtract() function on the console.

def sum_numbers(a, b):
    return first_num + sec_num


def subtract(a, b):
    return a - b


first_num = int(input())
sec_num = int(input())
third_num = int(input())

sum_total = sum_numbers(first_num, sec_num)
result = subtract(sum_total, third_num)
print(result)