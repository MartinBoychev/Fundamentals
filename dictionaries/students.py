# You will be receiving names of students, their ID, and a course of programming they have taken in the format
# "{name}:{ID}:{course}". On the last line, you will receive a name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course in the format:
# "{name} - {ID}" on separate lines.
# Note: each student's ID will always be unique


data = input()
courses = {}

while ":" in data:
    student_name, id_student, course_taken = data.split(":")
    if course_taken not in courses:
        courses[course_taken] = {id_student: student_name}
    else:
        courses[course_taken][id_student] = student_name

    data = input()
course_taken = data.replace("_", " ")
students = courses[course_taken]

for id_student, name in students.items():
    print(f"{name} - {id_student}")


