from classes import Student, Working_student, Teacher

students = []
teachers = []

no_students = '|!< No students in database! Add new one first. >!|'
no_teachers = '|!< No teachers in database! Add new one first. >!|'
value_error_message = '|!< Must type a number!\nGoing back to menu... >!|'

def main():

    menu = '''
What would you like to do?

Create student - (a)
Add Grade to a student - (ag)
Update details of a student - (ua)
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
        'ua': update_student_details,
        'ls': list_students,
        'lt': list_teachers,
        's': search_student,
        'at': add_teacher_to_student,
        'd': dummy_data
    }

    selection = input(menu).lower()
    print()

    while selection != 'q':

        try:
            selected_option = selected[selection]
            selected_option()
        except KeyError:
            print('Input not available!')

        print('\n------------------------------------------\n------------------------------------------\n')
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
            return print(f'\nStudent added!')
        except ValueError:
            return print(value_error_message)


    new_student = Student(name, course)
    students.append(new_student)
    return print(f'\nStudent added!')


def add_grade():
    """
    Function do add a grade to a student
    """
    if len(students) == 0:
        return print(no_students)
    for student in students:
        print(student)

    name = input('Name of student: \n').title()
    try:
        grade = int(input('Grade valuation: \n'))
    except ValueError:
        print(value_error_message)
        return None
    
    for student in students:
        if student.name == name:
            student.add_grade(grade)
            print('\nGrade added!')
            break
    else:
        print('\nStudent not found! Try again.\nGoing back to menu..')


def update_student_details():
    if len(students) == 0:
        return print(no_students)
    for student in students:
        print(student)
    try:
        student_id = int(input('\nType student ID to update: '))
        student_id = students[student_id - 1]
        print(student_id.details)
        name = input('Name of student: ').title()
        course = input('Course: ')
        if isinstance(student_id, Working_student):
            job = input('Job: ')
            pay = int(input('Yearly pay: '))
            student_id.job = job
            student_id.pay = pay
        student_id.name = name
        student_id.course = course
        return print('\nStudent Updated!')

    except ValueError:
        return print(value_error_message)


def list_students():
    if len(students) == 0:
        return print(no_students)
    for student in students:
        print(student.details)
        print()


def list_teachers():
    if len(teachers) == 0:
        return print(no_teachers)
    for teacher in teachers:
        print(teacher.details)
        print()


def search_student():
    """
    Function to search for a specific student
    """
    if len(students) == 0:
        return print(no_students)

    name = input("What's the student name? \n").title()
    for student in students:
        if student.name == name:
            print('\nFound student! Printing details...')
            return print(student.details)
            
    else:
        print('\nStudent not found.\nGoing back to menu..')


def add_teacher_to_student():
    """
    Function adds teacher to a student
    """
    if len(students) == 0:
        return print(no_students)
    if len(teachers) == 0:
        return print(no_teachers)

    for student in students:
        print(student)
    
    try:
        student_id = int(input('\nWhich student id you want to add a teacher?\n'))
        student = students[student_id - 1]
        print()
        for teacher in teachers:
            print(teacher)
        teacher_id = int(input('\nWhich teacher id you want to add?\n'))
        teacher = teachers[teacher_id - 1]
        student.add_teacher(teacher)

    except ValueError:
        return print(value_error_message)
    except IndexError:
        return print('\nID not in database.')


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
    teacher_3 = Teacher('The Net Ninja', 'Javascript')

    teachers.extend([teacher_1, teacher_2, teacher_3])

    print('Dummy data created sucessfully! \n')


main()