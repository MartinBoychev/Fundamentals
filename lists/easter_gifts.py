# Create a program that helps you plan the gifts for your friends and family.
# First, you are going to receive the gifts you plan on buying on a single line,
# separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# "OutOfStock {gift}"
# Find the gifts with this name in your collection, if any, and change their values to "None".
# "Required {gift} {index}"
# If the index is valid, replace the gift on the given index with the given gift.
# "JustInCase {gift}"
# Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None",
# separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"
# Input / Constraints
# On the 1st line,  you will receive the names of the gifts, separated by a single space.
# On the following lines, until the "No Money" command is received, you will be receiving commands.
# The input will always be valid.
# Output
# Print the gifts in the format described above.


gifts = input().split()

while True:
    command = input().split()
    if command[0] == "No" and command[1] == "Money":
        break
    if command[0] == "OutOfStock":
        gift = command[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = None
    elif command[0] == "Required":
        gift = command[1]
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift
    elif command[0] == "JustInCase":
        gift = command[1]
        gifts[-1] = gift

gifts = [gift for gift in gifts if gift is not None]
print(" ".join(gifts))
