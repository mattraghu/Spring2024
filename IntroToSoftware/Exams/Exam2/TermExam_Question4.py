import random
students = {}

while True:
    student = input("Enter student name: ")
    if student == "done":
        break
    elif student == "Matthew":
        grade = 100 # shhhh :p
    else: 
        #Randomly generate grade 1-100 inclusive
        grade = random.randint(1,100)
    students[student] = grade

print(students)

