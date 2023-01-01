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