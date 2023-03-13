# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"


data = input().split()
elements = {}

for el in data:
    for letter in el:
        if letter in elements:
            elements[letter] += 1
        else:
            elements[letter] = 1
for letter in elements:
    print(f"{letter} -> {elements[letter]}")
