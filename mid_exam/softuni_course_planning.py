# Help plan the next Programming Fundamentals course by keeping track of the lessons that
# will be included in the course and all the exercises for the lessons. Before the course starts,
# there are some changes to be made.
# On the first input line, you will receive the initial schedule of lessons and exercises that
# will be part of the next course, separated by a comma and a space ", ".
# Until you receive the "course start" command, you will be given some commands to modify the course schedule.
# The possible commands are:
# "Add:{lessonTitle}" - add the lesson to the end of the schedule if it does not exist.
# "Insert:{lessonTitle}:{index}" - insert the lesson to the given index, if it does not exist.
# "Remove:{lessonTitle}" - remove the lesson, if it exists.
# "Swap:{lessonTitle}:{lessonTitle}" - swap the position of the two lessons if they exist.
# "Exercise:{lessonTitle}" - add Exercise in the schedule right after the lesson index,
# if the lesson exists and there is no exercise already, in the following format "{lessonTitle}-Exercise".
# If the lesson doesn't exist, add the lesson at the end of the course schedule, followed by the Exercise.
# Note: Each time you Swap or Remove a lesson, you should do the same with the Exercises,
# if there are any following the lessons.
# Input / Constraints
# On the first line - the initial schedule lessons - strings, separated by comma and space ", ".
# Until "course start" you will receive commands in the format described above.
# Output
# Print the whole course schedule, each lesson on a new line with its number (index) in the schedule:
# "{lesson index}.{lessonTitle}".


subject_list = input().split(", ")
next_command = input()

while next_command != "course start":
    next_command_list = next_command.split(":")
    command = next_command_list[0]
    title = next_command_list[1]
    exercise = title + "-Exercise"
    if command == "Add":
        if title not in subject_list:
            subject_list.append(title)
    elif command == "Insert":
        index = int(next_command_list[2])
        if index < len(subject_list):
            if title not in subject_list:
                subject_list.insert(index, title)
    elif command == "Remove":
        if title in subject_list:
            subject_list.remove(title)
            if exercise in subject_list:
                subject_list.remove(exercise)
    elif command == "Swap":
        title_1 = next_command_list[1]
        title_2 = next_command_list[2]
        exercise_two = title_2 + "-Exercise"
        if title_1 and title_2 in subject_list:
            index_1 = subject_list.index(title_1)
            index_2 = subject_list.index(title_2)
            if exercise in subject_list and exercise_two in subject_list:
                subject_list[index_1], subject_list[index_2] = \
                    subject_list[index_2], subject_list[index_1]
                subject_list.remove(exercise)
                subject_list.remove(exercise_two)
                subject_list.insert(index_2 + 1, exercise)
                subject_list.insert(index_1 + 1, exercise_two)
            elif exercise in subject_list:
                subject_list[index_1], subject_list[index_2], = subject_list[index_2], subject_list[index_1]
                subject_list.remove(exercise)
                subject_list.insert(index_2 + 1, exercise)
            elif exercise_two in subject_list:
                subject_list[index_1], subject_list[index_2] = subject_list[index_2], subject_list[index_1]
                subject_list.remove(exercise_two)
                subject_list.insert(index_1 + 1, exercise_two)
            else:
                subject_list[index_1], subject_list[index_2] = subject_list[index_2], subject_list[index_1]
    elif command == "Exercise":
        if title not in subject_list:
            if exercise not in subject_list:
                subject_list.append(title)
                subject_list.append(exercise)
        else:
            if exercise not in subject_list:
                index_1 = subject_list.index(title)
                subject_list.insert(index_1 + 1, exercise)
    next_command = input()
for n in range(len(subject_list)):
    print(f"{n + 1}.{subject_list[n]}")
