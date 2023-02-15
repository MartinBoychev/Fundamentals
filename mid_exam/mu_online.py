# You have initial health 100 and initial bitcoins 0. You will be given a string representing the dungeon's rooms.
# Each room is separated with '|' (vertical bar): "room1|room2|room3…"
# Each room contains a command and a number, separated by space. The command can be:
# "potion"
# You are healed with the number in the second part. But your health cannot exceed your initial health (100).
# First print: "You healed for {amount} hp."
# After that, print your current health: "Current health: {health} hp."
# "chest"
# You've found some bitcoins, the number in the second part.
# Print: "You found {amount} bitcoins."
# In any other case, you are facing a monster, which you will fight.
# The second part of the room contains the attack of the monster.
# You should remove the monster's attack from your health.
# If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
# If you've died, print "You died! Killed by {monster}." and your quest is over.
# Print the best room you've manage to reach: "Best room: {room}"
# If you managed to go through all the rooms in the dungeon, print on the following three lines:
# "You've made it!"
# "Bitcoins: {bitcoins}"
# "Health: {health}"
# Input / Constraints
# You receive a string representing the dungeon's rooms, separated with '|' (vertical bar): "room1|room2|room3…".
# Output:
# Print the corresponding messages described above.


rooms = input().split("|")

MAX_HEALTH = 100
health = MAX_HEALTH
bitcoins = 0

room_number = 0

for room in rooms:
    room_number += 1
    command, amount = room.split()
    amount = int(amount)

    if command == "potion":
        if health + amount > MAX_HEALTH:
            print(f"You healed for {MAX_HEALTH - health} hp.")
            health = MAX_HEALTH
        else:
            print(f"You healed for {amount} hp.")
            health += amount
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += amount
        print(f"You found {amount} bitcoins.")
    else:
        health -= amount
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_number}")
            exit(0)

print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")