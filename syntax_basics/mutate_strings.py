word = input()
second_word = input()
new_string = ""

for i in range(1, len(word) + 1):
    new_string = second_word[:i] + word[i:]
    if word[i - 1] != second_word[i - 1]:
        print(new_string)