decor_qty = int(input())
day = int(input())

days_till_xmas = day
total_buying = 0
points = 0
while days_till_xmas > 1:
    days_till_xmas -= 1
    if days_till_xmas % 2 == 0:
        total_buying += decor_qty * 2
        points += 5
    if days_till_xmas % 3 == 0:
        total_buying += decor_qty * 5 + decor_qty * 3
        points += 13
    if days_till_xmas % 5 == 0:
        total_buying += decor_qty * 15
        points += 17
    if days_till_xmas % 10 == 0:
        points -= 20
        total_buying += decor_qty * 2 + decor_qty * 5 + decor_qty * 3 + decor_qty * 15
    if days_till_xmas % 11 == 0:
        decor_qty += 2
    if days_till_xmas == 10:
        points -= 30
print(f"Total cost: {total_buying}")
print(f"Total spirit {points}")







