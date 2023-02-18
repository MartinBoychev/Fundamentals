# Write a program that receives a sequence of numbers (a string containing integers separated by ", ")
# and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# The numbers 2, 8, 4, and 10 fall into the group of 10's.
# The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.


numbers = [int(i) for i in input().split(", ")]
groups = 0

while numbers:
    groups += 10
    print_list = [num for num in numbers if num <= groups]
    numbers = [num for num in numbers if num > groups]
    print(f"Group of {groups}'s: {print_list}")
