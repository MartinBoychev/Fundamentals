n = int(input())

for _ in range(n):
    new_num = int(input())
    if new_num % 2 == 1:
        print(f"{new_num} is odd!")
        break
else:
    print("All numbers are even.")
