# On the first line, you will receive a single number n. On the following n lines, you will receive integers. After
# that, you will be given one of the following commands: ⦁	even ⦁	odd ⦁	negative ⦁	positive Filter all the
# numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

n = int(input())
even = []
odd = []
negative = []
positive = []

for _ in range(n):
    current_num = int(input())
    if current_num >= 0:
        positive.append(current_num)
    else:
        negative.append(current_num)

    if current_num % 2 == 0:
        even.append(current_num)
    else:
        odd.append(current_num)

type_of_num = input()

if type_of_num == "even":
    print(even)
elif type_of_num == "odd":
    print(odd)
elif type_of_num == "negative":
    print(negative)
elif type_of_num == "positive":
    print(positive)
