# You will be given two strings. Transform the first string into the second one,
# letter by letter, starting from the first one. After each interaction,
# print the resulting string only if it is unique.
# Note: the strings will have the same length.

word = input()
second_word = input()
new_string = ""

for i in range(1, len(word) + 1):
    new_string = second_word[:i] + word[i:]
    if word[i - 1] != second_word[i - 1]:
        print(new_string)