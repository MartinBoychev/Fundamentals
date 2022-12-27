budget = int(input())
product = input()

total = 0

while budget >= total:
    if product == "End":
        print("You bought everything needed.")
        break
    total += int(product)
    if budget < total:
        print("You went in overdraft!")
        break
    product = input()