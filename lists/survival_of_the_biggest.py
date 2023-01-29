# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list.
# You should remove the smallest ones, and then, you should
# print all the numbers that are left in the list, separated by a comma and a space ", ".

my_list = input().split()
count_of_removals = int(input())
my_list_as_digits = []
final_list = []

for element in my_list:
    my_list_as_digits.append(int(element))
for _ in range(count_of_removals):
    my_list_as_digits.remove(min(my_list_as_digits))
for el in my_list_as_digits:
    final_list.append(str(el))

print(", ".join(final_list))
