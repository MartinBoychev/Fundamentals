data = input().split(" | ")
notebook = {}

for word_def in data:
    word, definition = word_def.split(": ", 1)
    if word in notebook:
        notebook[word].append(definition)
    else:
        notebook[word] = [definition]

words_to_test = input().split(" | ")
command = input()

if command == "Test":
    for word in words_to_test:
        if word in notebook:
            print(f"{word}:")
            for definition in notebook[word]:
                print(f"-{definition}")
elif command == "Hand Over":
    print(" ".join(notebook.keys()))
