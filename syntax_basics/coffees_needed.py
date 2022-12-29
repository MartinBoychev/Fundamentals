action = input()
coffees = 0

while action != "END":
    if action == "CODING" or action == "DOG" or action == "MOVIE" or action == "CAT":
        coffees += 2
    elif action == "coding" or action == "dog" or action == "movie" or action == "cat":
        coffees += 1
    action = input()
if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)