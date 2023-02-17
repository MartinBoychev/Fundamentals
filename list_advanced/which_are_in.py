# You will be given two sequences of strings, separated by ", ".
# Print a new list containing only the strings from the first input line,
# which are substrings of any string in the second input line.
#

first_input = input().split(", ")
second_input = input().split(", ")

result = [string for string in first_input
          if any(string in s for s in second_input)]

print(result)