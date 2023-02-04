def func_1(num_1, num_2, num_3):
    if num_1 < num_2 and num_1 < num_3:
        print(num_1)
    elif num_2 < num_3:
        print(num_2)
    else:
        print(num_3)
    return


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
func_1(num_1, num_2, num_3)
