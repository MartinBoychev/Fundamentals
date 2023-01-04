n = int(input())

for i in range(1, n + 1):
    if i == 5 or i == 7 or i == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")