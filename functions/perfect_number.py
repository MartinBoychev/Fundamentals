# A perfect number is a positive integer that is equal to the sum of its proper positive divisors. That is the sum of
# its positive divisors, excluding the number itself (also known as its aliquot sum). Write a function that receives
# an integer number and returns one of the following messages: "We have a perfect number!" - if the number is
# perfect. "It's not so perfect." - if the number is NOT perfect. Print the result on the console.


def is_perfect_number(num):
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    if divisors_sum == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
result = is_perfect_number(num)
print(result)