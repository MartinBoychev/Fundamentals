# Write a program that keeps track of every won battle against an enemy. You will receive initial energy. Afterward,
# you will start receiving the distance you need to reach an enemy until the "End of battle" command is given,
# or you run out of energy. The energy you need for reaching an enemy is equal to the distance you receive. Each time
# you reach an enemy, you win a battle, and your energy is reduced. Otherwise, if you don't have enough energy to
# reach an enemy, end the program and print: "Not enough energy! Game ends with {count} won battles and {energy}
# energy". Every third won battle increases your energy with the value of your current count of won battles. Upon
# receiving the "End of battle" command, print the count of won battles in the following format: "Won battles: {
# count}. Energy left: {energy}"


initial_energy = int(input())
battles_won = 0

while True:
    distance = input()
    if distance == 'End of battle':
        print(f"Won battles: {battles_won}. Energy left: {initial_energy}")
        break
    else:
        distance = int(distance)

    if initial_energy >= distance:
        initial_energy -= distance
        battles_won += 1
        if battles_won % 3 == 0:
            initial_energy += battles_won

    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy")
        break
