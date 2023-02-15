# Create a program that manages the state of the treasure chest along the way.
# On the first line, you will receive the initial loot of the treasure chest,
# which is a string of items separated by a "|".
# "{loot1}|{loot2}|{loot3} … {lootn}"
# The following lines represent commands until "Yohoho!" which ends the treasure hunt:
# "Loot {item1} {item2}…{itemn}":
# Pick up treasure loot along the way. Insert the items at the beginning of the chest.
# If an item is already contained, don't insert it.
# "Drop {index}":
# Remove the loot at the given position and add it at the end of the treasure chest.
# If the index is invalid, skip the command.
# "Steal {count}":
# Someone steals the last count loot items. If there are fewer items than the given count, remove as much as there are.
# Print the stolen items separated by ", ":
# "{item1}, {item2}, {item3} … {itemn}"
# In the end, output the average treasure gain, which is the sum of all treasure items length divided by
# the count of all items inside the chest formatted to the second decimal point:
# "Average treasure gain: {averageGain} pirate credits."
# If the chest is empty, print the following message:
# "Failed treasure hunt."
# Input
# On the 1st line, you are going to receive the initial treasure chest (loot separated by "|")
# On the following lines, until "Yohoho!", you will be receiving commands.
# Output
# Print the output in the format described above.
# Constraints
# The loot items will be strings containing any ASCII code.
# The indexes will be integers in the range [-200…200]
# The count will be an integer in the range [1….100]


loot = input().split("|")
command = input()

while command != "Yohoho!":
    tokens = command.split()
    action = tokens[0]

    if action == "Loot":
        items = tokens[1:]
        for item in items:
            if item not in loot:
                loot.insert(0, item)

    elif action == "Drop":
        index = int(tokens[1])
        if 0 <= index < len(loot):
            loot.append(loot.pop(index))

    elif action == "Steal":
        count = int(tokens[1])
        stolen_items = loot[-count:]
        loot = loot[:-count]
        print(", ".join(stolen_items))

    command = input()

if not loot:
    print("Failed treasure hunt.")
else:
    total_gain = sum(len(item) for item in loot)
    average_gain = total_gain / len(loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
