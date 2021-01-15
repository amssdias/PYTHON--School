from classes import Student, Working_student, Teacher

students = []
teachers = []

def main():

    menu = '''
What would you like to do?

Add student - (a)
Add Grade to student - (ag)
List all students - (ls)
List all teachers - (lt)
Search for specific student - (s)
Add teacher to a student - (at)
Create dummy data - (d)
quit - (q)

'''

    selected = {
        'a': create_student,
        'ag': add_grade,
        'ls': list_students,
        'lt': list_teachers,
        's': search_student,
        'at': add_student_teacher,
        'd': dummy_data
    }

    selection = input(menu).lower()

    while selection != 'q':

        try:
            selected_option = selected[selection]
            selected_option()
        except KeyError:
            print('Input not available!')

        selection = input(menu).lower()
        print()


    print('''
    Deleting all data...
    Goodbye!
    ''')


def create_student():
    """
    Function to create a student
    """
    name = input('Name of new student: \n').title()
    course = input('Which course is taking: \n').title()
    working = input('Is this student working? (y/n) \n').lower()

    if working == 'y':
        job = input("What's his job: \n")
        try:
            pay = int(input("Yearly Payment: \n"))
            working_st = Working_student(name, course, job, pay)
            students.append(working_st)
            return print(f'Student added!')
        except ValueError:
            return print('Must Type a number')


    new_student = Student(name, course)
    students.append(new_student)
    return print(f'Student added!')


def display_students():
    if len(students) == 0:
        return print('No students \n')
    for student in students:
        print(student, '\n')


def add_grade():
    display_students()
    name = input('Name of student: \n').title()
    try:
        grade = int(input('Grade valuation: \n'))
    except ValueError:
        print('Must type a number!\nGoing back to menu..')
        return None
    
    for student in students:
        if student.name == name:
            student.add_grade(grade)
            print('\nGrade added!')
            break
    else:
        print('\nStudent not found! Try again.\nGoing back to menu..')


def list_students():
    if len(students) == 0:
        return print('No students \n')
    for student in students:
        print(student.details)
        print()


def list_teachers():
    if len(teachers) == 0:
        return print('No teachers')
    for teacher in teachers:
        print(teacher.details)
        print()


def search_student():
    if len(students) == 0:
        return print('No students \n')

    name = input("What's the student name? \n").title()
    for student in students:
        if student.name == name:
            print('Found student! Printing details...')
            return print(student.details)
            
    else:
        print('Student not found.\nGoing back to menu..')


def add_student_teacher():
    if len(students) == 0:
        return print('No students in database! Add new one first')
    if len(teachers) == 0:
        return print('No teachers in database! Add new one first')

    for student in students:
        print(student, '\n')
    
    try:
        student_id = int(input('\nWhich student id you want to add a teacher?\n'))
        student = students[student_id - 1]
        print()
        for teacher in teachers:
            print(teacher, '\n\n')
        teacher_id = int(input('Which teacher id you want to add?\n'))
        teacher = teachers[teacher_id - 1]
        student.add_teacher(teacher)
        print(f"{teacher.name} was added to {student.name}!")

    except ValueError:
        return print('Must type a number! \nGoing back to menu..')
    except IndexError:
        return print('ID not in database.')

def dummy_data():
    student_1 = Student('Student 1', 'Economics')
    student_2 = Student('Student 2', 'Sports')
    working_student_1 = Working_student('Working Student 1', 'Web Dev', 'Full stack developer', 25000)
    working_student_2 = Working_student('Working Student 2', 'Web Dev', 'Junior Python Developer', 17000)
    student_1.add_grade(80)
    student_1.add_grade(70)
    student_1.add_grade(86)
    student_2.add_grade(90)
    student_2.add_grade(93)
    student_2.add_grade(91)
    working_student_1.add_grade(65)
    working_student_1.add_grade(70)

    students.extend([student_1, student_2, working_student_1, working_student_2])

    teacher_1 = Teacher('Corey Schaufer', 'Python')
    teacher_2 = Teacher('Pretty Printed', 'Django')
    teacher_1.add_student(student_1)
    teacher_1.add_student(working_student_2)
    teacher_2.add_student(working_student_2)

    teachers.extend([teacher_1, teacher_2])

    print('Dummy data created sucessfully! \n')


main()