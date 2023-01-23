# Write a program that receives two numbers (factor and count).
# It should create a list with a length of the given count that contains only integer numbers,
# which are multiples of the given factor. The numbers should be only positive,
# and they should be arranged in ascending order, starting from the value of the factor.

num1 = int(input())
num2 = int(input())
my_list = []

for i in range(1, num2 + 1):
    b = int(i * num1)
    my_list.append(b)

print(my_list)
