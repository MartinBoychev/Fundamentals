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
