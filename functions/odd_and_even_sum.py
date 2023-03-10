# You will receive a single number. You should write a function that returns the sum of all even and all odd digits
# in a given number. The result should be returned as a single string in the format: "Odd sum = {sum_of_odd_digits},
# Even sum = {sum_of_even_digits}" Print the result of the function on the console.


def sum_of_digits(number):
    odd_sum = 0
    even_sum = 0
    for i in range(len(number)):
        if int(number[i]) % 2 == 0:
            even_sum += int(number[i])
        else:
            odd_sum += int(number[i])
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


num = input()
sum_of_digits(num)
