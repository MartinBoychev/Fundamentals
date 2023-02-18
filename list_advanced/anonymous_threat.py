# Anonymous has created a hyper cyber virus, which steals data from the CIA. The virus is known for its innovative
# and unbelievably clever merging and dividing data into partitions. As the lead security developer in the CIA,
# you have been tasked to analyze the software of the virus and observe its actions on the data. You will receive a
# single input line containing strings, separated by spaces. The strings may contain any ASCII character except
# whitespace. Then you will begin receiving commands in one of the following formats: merge {startIndex} {endIndex}
# divide {index} {partitions} Every time you receive the merge command, you must merge all elements from the
# startIndex to the endIndex. In other words, you should concatenate them. Example: {abc, def, ghi} -> merge 0 1 -> {
# abcdef, ghi} If any of the given indexes is out of the array, you must take only the range that is inside the array
# and merge it. Every time you receive the divide command, you must divide the element at the given index into
# several small substrings with equal length. The count of the substrings should be equal to the given partitions.
# Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl} If the string cannot be exactly divided into
# the given partitions, make all partitions except the last with equal lengths and make the last one - the longest.
# Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl} The input ends when you receive the command
# "3:1". At that point, you must print the resulting elements, joined by a space. Input The first input line will
# contain the array of data. On the next several input lines, you will receive commands in the format specified
# above. The input ends when you receive the command "3:1". Output As output, you must print a single line containing
# the elements of the array, joined by a space.


message = input().split()
receiving_command = input()

while receiving_command != "3:1":
    command_list = receiving_command.split()
    command = command_list[0]
    starting_index = int(command_list[1])
    end_index = int(command_list[2])

    if command == "merge":
        if starting_index < 0:
            starting_index = 0
        if end_index > len(message) - 1:
            end_index = len(message) - 1

        diff_indices = end_index - starting_index
        if end_index == len(message):
            diff_indices -= 1
        new_message = message[starting_index:end_index + 1]
        message_to_add = "".join(new_message)
        for _ in range(diff_indices + 1):
            if len(message) > 0:
                message.pop(starting_index)
            else:
                continue
        message.insert(starting_index, message_to_add)
        receiving_command = input()
    elif command == "divide":
        new_message = message[starting_index]
        message.pop(starting_index)
        substring_len = len(new_message) // end_index
        remainder = len(new_message) % end_index
        substrings_added = 0
        start_part = 0
        end_part = substring_len
        while substrings_added < end_index:
            message.insert(starting_index, new_message[start_part:end_part])
            starting_index += 1
            substrings_added += 1
            if substrings_added + 1 == end_index:
                start_part += substring_len
                end_part += substring_len + remainder
            else:
                start_part += substring_len
                end_part += substring_len
        receiving_command = input()
print(" ".join(message))