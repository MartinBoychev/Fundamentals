cards = input().split(", ")
rotation = int(input())

for card in range(rotation):
    command = input().split(", ")
    if command[0] == "Add":
        if command[1] in cards:
            print("Card is already in the deck")
        else:
            cards.append(command[1])
            print("Card successfully added")
    elif command[0] == "Remove":
        if command[1] in cards:
            card_to_remove = str(command[1])
            cards.remove(card_to_remove)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif command[0] == "Remove At":
        index = int(command[1])
        if index < len(cards):
            del cards[index]
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif command[0] == "Insert":
        index = int(command[1])
        card_to_insert = command[2]
        if card_to_insert in cards:
            print("Card is already in the deck")
        elif 0 <= index < len(cards):
            cards.insert(index, card_to_insert)
            print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(cards))