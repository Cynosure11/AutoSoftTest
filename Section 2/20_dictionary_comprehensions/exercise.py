student = {'name': 'Jose', 'school': 'Computing',
           'grades': (66, 77, 88)}


def average_grade(data):
    grades = len(data['grades'])
    return sum(grades) / len(grades)



# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])

    return total / count

