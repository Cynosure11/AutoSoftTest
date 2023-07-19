friend_ages = {
    "Rolf": 24,
    "Adam": 30,
    "Anne": 27
}
print(friend_ages["Rolf"])


friends =[
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
]
print(friends[1]["name"])


student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for student, attendance in student_attendance.items():
    print(f"{student}: {student_attendance[student]}%")

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print(f"Bob is not a student in this class")

attendance_values = student_attendance.values()
print(attendance_values)
print(sum(attendance_values) / len(attendance_values))
print(f"brun, len{attendance_values}")
besties_scores = {"Aial": 99, "Kostya": 60, "Karyna": 20}
besties_scores_average = besties_scores.values()
print(sum(besties_scores_average) / len(besties_scores.values()))
for bestie, score in besties_scores.items():
    print(f"{bestie}: {score}. \n")