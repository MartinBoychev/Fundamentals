# Write a program that receives strings on different lines and extracts only the numbers.
# Print all extracted numbers on a single line, separated by a single space.

import re


numbers_pattern = re.compile(r"\d+")

digits = []

while True:
    sequences = input()
    if not sequences:
        break
    matches = re.findall(numbers_pattern, sequences)
    digits.extend(matches)

print(*digits)
