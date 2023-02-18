import math

students = int(input())
lectures = int(input())
initial_bonus = int(input())
attendance_list = []

if lectures == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
else:
    for i in range(1, students + 1):
        attendances = int(input())
        attendance_list.append(attendances)

    print(f'Max Bonus: {math.ceil((max(attendance_list) / lectures) * (5 + initial_bonus))}.')
    print(f'The student has attended {max(attendance_list)} lectures.')