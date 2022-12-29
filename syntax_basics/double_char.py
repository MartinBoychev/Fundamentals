string = input()

while string != "End":
    if string == "SoftUni":
        string = input()
    else:
        print('S'.join(c + c for c in string))
        string = input()