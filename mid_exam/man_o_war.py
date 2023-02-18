# Create a program that tracks the battle and either chooses a winner or prints a stalemate.
# On the first line, you will receive the status of the pirate ship,
# which is a string representing integer sections separated by ">".
# On the second line, you will receive the same type of status, but for the warship:
# "{section1}>{section2}>{section3}… {sectionn}"
# On the third line, you will receive the maximum health capacity a section of the ship can reach.
# The following lines represent commands until "Retire":
# "Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section.
# Check if the index is valid and if not, skip the command. If the section breaks (health <= 0) the warship sinks,
# print the following and stop the program: "You won! The enemy ship has sunken."
# "Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship with the given damage at that range.
# Check if both indexes are valid and if not, skip the command. If the section breaks the pirate ship sinks,
# print the following and stop the program:
# "You lost! The pirate ship has sunken."
# "Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health.
# Check if the index is valid and if not, skip the command.
# The health of the section cannot exceed the maximum health capacity.
# "Status" - prints the count of all sections of the pirate ship that need repair soon,
# which are all sections that are lower than 20% of the maximum health capacity. Print the following:
# "{count} sections need repair."
# In the end, if a stalemate occurs, print the status of both ships,
# which is the sum of their individual sections, in the following format:
# "Pirate ship status: {pirateShipSum}
# Warship status: {warshipSum}"
# Input
# On the 1st line, you are going to receive the status of the pirate ship (integers separated by '>')
# On the 2nd line, you are going to receive the status of the warship
# On the 3rd line, you will receive the maximum health a section of a ship can reach.
# On the following lines, until "Retire", you will be receiving commands.
# Output
# Print the output in the format described above.


pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_health = int(input())

while True:
    command = input()
    if command == "Retire":
        break

    tokens = command.split()
    action = tokens[0]

    if action == "Fire":
        index = int(tokens[1])
        damage = int(tokens[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit(0)
    elif action == "Defend":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        damage = int(tokens[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit(0)
    elif action == "Repair":
        index = int(tokens[1])
        health = int(tokens[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] = min(pirate_ship[index] + health, max_health)
    elif action == "Status":
        count = len([x for x in pirate_ship if x < max_health * 0.2])
        print(f"{count} sections need repair.")

pirate_ship_sum = sum(pirate_ship)
warship_sum = sum(warship)
if pirate_ship_sum > warship_sum:
    print(f"Pirate ship status: {pirate_ship_sum}\nWarship status: {warship_sum}")
else:
    print(f"Pirate ship status: {pirate_ship_sum}\nWarship status: {warship_sum}")

