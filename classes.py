class Student:
    id = 1

    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.grades = []
        self.id = Student.id
        self.teachers = []
        Student.id += 1

    def __repr__(self):
        return f"<Student({self.name}, {self.course})>"

    def __str__(self):
        return f"Id: {self.id} - {self.name}"

    @property
    def details(self):
        return f"""Student \n
        id: {self.id}
        Name: {self.name}
        Course: {self.course}
        Grades: {self.grades}
        Teachers: {[teacher.__str__() for teacher in self.teachers]}
        """

    def add_grade(self, grade):
        if not isinstance(grade, int) and not isinstance(grade, float):
            raise ValueError('Grade must be a number!')
        self.grades.append(grade)

    def add_teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError('Tried to add a `{teacher.__class__.__name__}` to student, but you can only add `Teacher` object. ')
        if teacher in self.teachers:
            return print('<<<<<  Teacher already exists  >>>>>')
        self.teachers.append(teacher)
        teacher.students.append(self)
        print(f'Teacher added! to {self.name}.')




class Working_student(Student):

    def __init__(self, name, course, job, pay):
        super().__init__(name, course)
        self.job = job
        self.pay = pay

    def __repr__(self):
        return f"<Working_student({self.name}, {self.course}, {self.job}, {self.pay})>"

    def __str__(self):
        return f"Id: {self.id} - {self.name} (Working)"

    @property
    def details(self):
        return f"""Working student \n
        id: {self.id}
        Name: {self.name} 
        Course: {self.course}
        Grades: {self.grades}
        Teachers: {[teacher.__str__() for teacher in self.teachers]}
        Job: {self.job}
        Pay(Yearly): {self.pay}
        """



class Teacher:
    id = 1

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = []
        self.id = Teacher.id

        Teacher.id += 1

    def __repr__(self):
        return f'<Teacher: {self.name} {self.subject}>'

    def __str__(self):
        return f"Id: {self.id} - {self.name}"

    @property
    def details(self):
        return f"""Teacher \n
        id: {self.id}
        Name: {self.name} 
        Subject: {self.subject}
        Students: {[student.__str__() for student in self.students]}
        """
