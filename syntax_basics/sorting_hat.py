name = input()

while True:
    if len(name) < 5 and name != "Voldemort" and name != "Welcome!":
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5 and name != "Voldemort" and name != "Welcome!":
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6 and name != "Voldemort" and name != "Welcome!":
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6 and name != "Voldemort" and name != "Welcome!":
        print(f"{name} goes to Hufflepuff.")

    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    elif name == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    name = input()