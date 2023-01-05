n = int(input())

for i in range(1, n + 1):
    sum = 0
    for digit in str(i):
        sum += int(digit)
    if sum == 5 or sum == 7 or sum == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")