# You are given an array with integers. Write a program to modify the elements after receiving the following
# commands: "swap {index1} {index2}" takes two elements and swap their places. "multiply {index1} {index2}" takes
# element at the 1st index and multiply it with the element at 2nd index. Save the product at the 1st index.
# "decrease" decreases all elements in the array with 1. Input On the first input line, you will be given the initial
# array values separated by a single space. On the next lines you will receive commands until you receive the command
# "end". The commands are as follow: "swap {index1} {index2}" "multiply {index1} {index2}" "decrease" Output The
# output should be printed on the console and consist of elements of the modified array – separated by a comma and a
# single space ", ".

data = [int(x) for x in input().split()]

while True:
    line = input()
    if line == "end":
        break
    elif line == "decrease":
        for i in range(len(data)):
            data[i] -= 1
    else:
        command, idx1, idx2 = line.split()
        index1 = int(idx1)
        index2 = int(idx2)
        if command == "swap":
            data[index1], data[index2] = data[index2], data[index1]
        elif command == "multiply":
            data[index1] *= data[index2]

data = [str(x) for x in data]
print(", ".join(data))
