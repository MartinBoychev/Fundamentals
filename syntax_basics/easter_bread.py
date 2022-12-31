budget = float(input())
price_floor = float(input())

eggs_price = price_floor * 0.75
milk_price = (price_floor * 1.25) * 0.25
money_per_bread = price_floor + eggs_price + milk_price
money_left = budget - money_per_bread
current_bread_count = 0
colored_eggs = 0

while money_left > 0:
    money_left -= money_per_bread
    current_bread_count += 1
    colored_eggs += 3
    if current_bread_count % 3 == 0:
        colored_eggs = colored_eggs - (current_bread_count - 2)
    continue

final_money = budget - (current_bread_count * money_per_bread)

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {final_money:.2f}BGN left.")

