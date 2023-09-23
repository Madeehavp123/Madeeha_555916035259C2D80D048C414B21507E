class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students_by_cgpa(student_list):
    return sorted(student_list, key=lambda student: student.cgpa, reverse=True)

students = []

while True:
    name = input("Enter student's name (or 'exit' to finish): ")
    if name.lower() == 'exit':
        break
    roll_number = input("Enter roll number: ")
    cgpa = float(input("Enter CGPA: "))
    students.append(Student(name, roll_number, cgpa))

sorted_students = sort_students_by_cgpa(students)

print("Students sorted by CGPA (highest to lowest):")
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
