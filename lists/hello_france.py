command = input().split("|")
budget = float(input())
money_spend = []
new_prices = []
total_profit = 0
for i in command:
    split_item_from_price = i.split("->")
    item = split_item_from_price[0]
    price = float(split_item_from_price[1])

    if item == "Clothes" and price > 50.00:
        continue
    if item == "Shoes" and price > 35.00:
        continue
    if item == "Accessories" and (price > 20.50):
        continue
    if budget < price:
        continue

    budget -= price
    money_spend.append(price)
    new_price = price * 1.4
    new_prices.append(new_price)
    profit = new_price - price
    total_profit += profit

new_budget = budget + sum(new_prices)
formated_new_prices = [float("%.02f" % x) for x in new_prices]

print(*formated_new_prices, sep=" ")
print(f"Profit: {total_profit:.2f}")

if new_budget > 150:
    print("Hello, France!")
else:
    print("Not enough money.")
