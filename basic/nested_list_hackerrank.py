import sys

N = int(input())
students = []  # declare a variable called 'students' and initialize it as an empty list

# read in the names and grades for all the students
for i in range(N):
    student = []
    name = input()
    student.append(name)
    grade = float(input())
    student.append(grade)
    students.append(student)

# find the lowest and second lowest grades
lowest = students[0][1]
second_lowest = students[0][1]
for i in range(1, N):
    if students[i][1] <= lowest:
        second_lowest = lowest
        lowest = students[i][1]
    else:
        if students[i][1] < second_lowest:
            second_lowest = students[i][1]

students.sort()

for i in range(N):
    if students[i][1] == second_lowest:
        print(students[i][0])