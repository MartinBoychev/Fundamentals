# Write a program that receives strings on different lines and extracts only the numbers.
# Print all extracted numbers on a single line, separated by a single space.


import re

sequences = input()
numbers_pattern = re.compile(r"(?P<numbers>\d+)")

digits = []

while sequences:
    current_digits = numbers_pattern.finditer(sequences)
    for digit in current_digits:
        digits.append(digit['numbers'])
    sequences = input()

print(*digits)