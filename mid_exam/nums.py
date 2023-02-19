nums = input().split()
command = input()

while command != "Finish":
    command_line = command.split()
    if command_line[0] == "Add":
        number = command_line[1]
        if number in nums:
            nums.append(number)
    elif command_line[0] == "Remove":
        number = command_line[1]
        if number in nums:
            nums.remove(number)
    elif command_line[0] == "Replace":
        old_num = command_line[1]
        new_new = command_line[2]
        if old_num in nums:
            index = nums.index(old_num)
            nums[index] = new_new
    elif command_line[0] == "Collapse":
        number = command_line[1]
        for el in nums:
            if el < number:
                nums.remove(el)
    command = input()

print("".join(nums))
