# Write a program to read a sequence of integers and find and print the top 5 numbers
# greater than the average value in the sequence, sorted in descending order.
# Input
# Read from the console a single line holding space-separated integers.
# Output
# Print the above-described numbers on a single line, space-separated.
# If less than 5 numbers hold the property mentioned above, print less than 5 numbers.
# Print "No" if no numbers hold the above property.

numbers = [int(x) for x in input().split()]

average = sum(numbers) / len(numbers)
greater_than_average = [x for x in numbers if x > average]
top_five = sorted(greater_than_average, reverse=True)[:5]

if top_five:
    print(*top_five)
else:
    print("No")
