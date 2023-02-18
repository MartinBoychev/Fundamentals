# You are at the shooting gallery again, and you need a program that helps you keep track of moving targets. On the
# first line, you will receive a sequence of targets with their integer values, split by a single space. Then,
# you will start receiving commands for manipulating the targets until the "End" command. The commands are the
# following: "Shoot {index} {power}" Shoot the target at the index if it exists by reducing its value by the given
# power (integer value). Remove the target if it is shot. A target is considered shot when its value reaches 0. "Add {
# index} {value}" Insert a target with the received value at the received index if it exists. If not, print: "Invalid
# placement!" "Strike {index} {radius}" Remove the target at the given index and the ones before and after it
# depending on the radius. If any of the indices in the range is invalid, print: "Strike missed!" and skip this
# command. Example:  "Strike 2 2" {radius}	{radius}	{strikeIndex}	{radius}	{radius}
#
# "End"
# Print the sequence with targets in the following format and end the program:
# "{target1}|{target2}…|{targetn}"


targets = input().split()
targets = [int(t) for t in targets]

while True:
    command = input().split()
    if command[0] == "End":
        break

    if command[0] == "Shoot":
        index = int(command[1])
        power = int(command[2])
        if index < 0 or index >= len(targets):
            continue
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)

    elif command[0] == "Add":
        index = int(command[1])
        value = int(command[2])
        if index < 0 or index > len(targets):
            print("Invalid placement!")
            continue
        targets.insert(index, value)

    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])
        start_index = index - radius
        end_index = index + radius
        if start_index < 0 or end_index >= len(targets):
            print("Strike missed!")
            continue
        targets = targets[:start_index] + targets[end_index + 1:]

print("|".join(str(t) for t in targets))
