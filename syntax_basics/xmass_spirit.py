# It is time to get in a Christmas mood. You need to decorate the house in time for the big event, but you have
# limited days to do so. Write a program that calculates how much money you will need to spend on Christmas
# decorations and how much your Christmas spirit will improve. On the first line, you will receive the quantity of
# decorations you should buy each time you go shopping. On the second line, you will receive the days left until
# Christmas. There are 4 types of decorations, and each piece costs a certain price. Also, each time you go shopping
# for a concrete type of decoration, your Christmas spirit is improved by some points: Decoration	Price/Piece
# Points/Shopping Ornament Set	2$	5 Tree Skirt	5$	3 Tree Garland	3$	10 Tree Lights	15$	17 Until Christmas,
# you go shopping for a certain decoration as follows: Every second day you buy Ornament Sets. Every third day you
# buy Tree Skirts and Tree Garlands. Every fifth day you buy Tree Lights. If you have bought Tree Skirts and Tree
# Garlands on the same day, you additionally increase your spirit by 30. That's not all! You have a cat at home that
# really likes to mess around with the decoration: Every tenth day your cat ruins all tree decorations, and you lose
# 20 points of the spirit: Because of that, you go shopping (for a second time during the day) to buy one piece of
# tree skirt, garlands, and lights, but you do NOT earn additional spirit points for them. Also, because of the cat -
# at the beginning of every eleventh day, you are forced to increase the quantity of decorations needed to be bought
# each time you go shopping by 2. If the last day is a tenth day, the cat demolishes even more and ruins the
# Christmas turkey, and you lose an additional 30 points of spirit. In the end, you must print the total cost and the
# gained spirit.

decor_qty = int(input())
day = int(input())

total_buying = 0
points = 0
count_days = 0

while day > 0:
    count_days += 1
    day -= 1
    if count_days % 11 == 0:
        decor_qty += 2
    if count_days % 2 == 0:
        total_buying += decor_qty * 2
        points += 5
    if count_days % 3 == 0:
        total_buying += decor_qty * 5 + decor_qty * 3
        points += 13
    if count_days % 5 == 0:
        total_buying += decor_qty * 15
        points += 17
    if count_days % 15 == 0:
        points += 30
    if count_days % 10 == 0:
        total_buying += 23
        points -= 20
    if count_days % 10 == 0 and day == 0:
        points -= 30

print(f"Total cost: {total_buying}")
print(f"Total spirit: {points}")
