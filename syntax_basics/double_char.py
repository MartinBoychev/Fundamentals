string = input()

while string != "End":
    if string == "SoftUni":
        string = input()
    else:
        print(''.join(c + c for c in string))
        string = input()