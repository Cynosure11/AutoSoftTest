# x, y = 5, 11 # tuple. brackets - () is not necessary

t = 5, 11
x, y = t
print(x, y)

student_attendance= {"Rolf": 96, "Bob": 80, "Anne": 100}
print(list(student_attendance.items()))

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


people = [
    ("Bob", 42, "Mechanic"),
    ("James", 24, "Artist"),
    ("Harry", 32, "Lecture")
]

for name, age, profession in people:
    print(f"{name}, {age} years old and works as {profession}")

for person in people:
    print(f"Name: {person[0]}, years old: {person[1]}, profession {person[2]}")


person = ("Bob", 42, "Mechanic")
name, _, job_title = person
print(name, job_title)


# *tail - will collect variables example: [2,3,4,5]
# *head - will collect variables in the end: [1,2,3,4]
head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)


