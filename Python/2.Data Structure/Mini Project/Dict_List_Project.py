students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")

    math = float(input("Enter Math marks: "))
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))

    students[name] = [math, physics, chemistry]

search_name = input("Enter a name: ")

marks = students[search_name]
average = sum(marks) / len(marks)

print("Average percentage mark:", average)