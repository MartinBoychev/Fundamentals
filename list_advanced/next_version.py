# You are fed up with changing the version of your software manually. Instead, you will create a little script that
# will make it for you. You will be given a string representing the version of your software in the format: "{n1}.{
# n2}.{n3}". Your task is to print the next version. For example, if the current version is "1.3.4", the next version
# will be "1.3.5". The only rule is that the numbers cannot be greater than 9. If it happens, set the current number
# to 0 and increase the previous number. For more clarification, see the examples below. Note: there will be no case
# in which the first number will become greater than 9.


nums = input()

nums_list = [int(n) for n in nums.split(".")]

nums_list[2] += 1
if nums_list[2] == 10:
    nums_list[2] = 0
    nums_list[1] += 1
    if nums_list[1] == 10:
        nums_list[1] = 0
        nums_list[0] += 1
version_string = ".".join(str(num) for num in nums_list)
print(version_string)
