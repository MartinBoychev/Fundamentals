def sort_into_groups(numbers):
    # Convert the string of numbers into a list of integers
    numbers_list = [int(num) for num in numbers.split(", ")]

    # Initialize variables
    groups = []
    group_boundary = 10

    # Loop until the list of numbers is empty
    while numbers_list:
        # Filter the numbers that belong to the current group
        current_group = [num for num in numbers_list if num <= group_boundary]

        # Remove the current group from the list of numbers
        for num in current_group:
            numbers_list.remove(num)

        # If there are numbers in the current group, add it to the list of groups
        if current_group:
            groups.append(current_group)

        # Increase the group boundary by 10
        group_boundary += 10

    # Print the groups of numbers in the desired format
    for i, group in enumerate(groups):
        print(f"Group of {10 * (i + 1)}'s: {group}")


sort_into_groups(input())