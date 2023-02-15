# You will receive a single integer number between 0 and 100 (inclusive)
# divisible by 10 without remainder (, 10, 20, 30...).
# Your task is to create a function that returns a loading bar depending on the number you have received
# in the input. Print the result on the console. For more clarification, see the examples below.

def loading_bar(num):
    num_bars = num // 10
    num_spaces = 10 - num_bars
    loading = "{}% [{}{}]".format(num, "%" * num_bars, "." * num_spaces)
    if num < 100:
        loading += "\nStill loading..."
    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
        exit()
    return loading


num = int(input())
result = loading_bar(num)
print(result)