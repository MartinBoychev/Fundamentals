n = int(input())
total_money = 0

for _ in range(n):
    price_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    total_price = price_capsule * days * capsules_per_day
    if 0.01 <= price_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        print(f"The price for the coffee is: ${total_price:.2f}")
        total_money += total_price
print(f"Total: ${total_money:.2f}")
