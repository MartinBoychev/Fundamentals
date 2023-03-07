# After you have completed your first task, your boss decides to give you another one right away. Now not only you
# have to keep track of the stock, but also you should answer customers if you have some products in stock or not. You
# will be given key-value pairs of products and quantities (on a single line separated by space). On the following
# line, you will be given products to search for. Check for each product. You have 2 possibilities: ⦁	If you have
# the product, print "We have {quantity} of {product} left". ⦁	Otherwise, print "Sorry, we don't have {product}".

elements = input().split(" ")
bakery = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)

searched_products = input().split(" ")

for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")