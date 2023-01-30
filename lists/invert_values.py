# Write a program that receives a single string containing positive and
# negative numbers separated by a single space.
# Print a list containing the opposite of each number.

my_list = input().split()
opposite_list = []

for i in my_list:
    opposite_number = -int(i)
    opposite_list.append(opposite_number)

print(opposite_list)