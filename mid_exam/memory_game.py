# Write a program that recreates the Memory game.
# On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin.
# Until the player receives "end" from the console, you will receive strings with two integers separated by a space,
# representing the indexes of elements in the sequence.
# If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence,
# you should add two matching elements at the middle of the sequence in the following format:
# "-{number of moves until now}a"
# Then print this message on the console:
# "Invalid input! Adding additional elements to the board"
# Input
# On the first line, you will receive a sequence of elements
# On the following lines, you will receive integers until the command "end"
# Output
# Every time the player hit two matching elements,
# you should remove them from the sequence and print on the console the following message:
# "Congrats! You have found matching elements - ${element}!"
# If the player hit two different elements, you should print on the console the following message:
# "Try again!"
# If the player hit all matching elements before he receives "end" from the console,
# you should print on the console the following message:
# "You have won in {number of moves until now} turns!"
# If the player receives "end" before he hits all matching elements,
# you should print on the console the following message:
# "Sorry you lose :(
# {the current sequence's state}"
# Constraints
# All elements in the sequence will always have a matching element.


def is_index_in_range(index, cards_count):
    if 0 <= index < cards_count:
        return True
    return False


def check_indexes_are_valid(index1, index2, count_cards):
    if (
            is_index_in_range(index1, count_cards)
            and is_index_in_range(index2, count_cards)
            and index1 != index2
    ):
        return True
    return False


cards = input().split()

command = input()
n_moves = 0

while command != "end":
    n_moves += 1
    index1, index2 = [int(el) for el in command.split()]
    if check_indexes_are_valid(index1, index2, len(cards)):
        if cards[index1] == cards[index2]:
            element = cards[index1]
            cards.pop(index1)
            # Elements are reordered after pop, so we need to use the.remove, 
            # because the index is no longer accurate
            cards.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        else:
            print("Try again!")
    else:
        # punish the player
        element_to_add = f"-{n_moves}a"
        index = len(cards) // 2
        cards.insert(index, element_to_add)
        cards.insert(index, element_to_add)
        print("Invalid input! Adding additional elements to the board")

    if not cards:
        print(f"You have won in {n_moves} turns!")
        exit(0)

    command = input()

print(f"Sorry you lose :(")
print(*cards, sep=' ')