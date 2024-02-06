string = input().strip()

while True:
    command = input().strip()

    if command == "Done":
        break

    command = command.split()

    if command[0] == "Change":
        character = command[1]
        replacement = command[2]
        string = string.replace(character, replacement)
        print(string)

    elif command[0] == "Includes":
        substring = command[1]
        if substring in string:
            print("True")
        else:
            print("False")

    elif command[0] == "End":
        substring = command[1]
        if string.endswith(substring):
            print("True")
        else:
            print("False")

    elif command[0] == "Uppercase":
        string = string.upper()
        print(string)

    elif command[0] == "FindIndex":
        character = command[1]
        if character in string:
            index = string.index(character)
            print(index)
        else:
            print("-1")

    elif command[0] == "Cut":
        start_index = int(command[1])
        count = int(command[2])
        cut_string = string[start_index:start_index+count]
        print(cut_string)

