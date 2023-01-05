# Write a program that reads an integer n. Then, for all numbers in the range [1, n],
# prints the number and if it is special or not (True / False).
# A number is special when the sum of its digits is 5, 7, or 11.

n = int(input())

for i in range(1, n + 1):
    sum_digits = 0
    digit = i
    while digit > 0:
        sum_digits += digit % 10
        digit = int(digit / 10)
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")

