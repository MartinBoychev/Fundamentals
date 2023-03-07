# You will be receiving key-value pairs on separate lines
# separated by ": " until you receive the command "statistics".
# Sometimes you may receive a product more than once. In that case,
# you have to add the new quantity to the existing one.
# When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"


products = {}
command = input()

while command != "statistics":
    tokens = command.split(": ")
    product = tokens[0]
    quantity = int(tokens[1])
    if product not in products:
        products[product] = 0
    products[product] += quantity

    command = input()

print("Products in stock:")
for (product, quantity) in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
