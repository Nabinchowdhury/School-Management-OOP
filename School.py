#School, name, address , add classroom, student admission, Classroom, add student

class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        #compositions
        self.classrooms = {} #dictionary
        self.teachers = {} #dictionary

    
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, teacher):
        self.teachers[teacher.subject] = teacher
    
    def student_admission(self, student, classroom):
        if classroom.name in self.classrooms:
            self.classrooms[classroom.name].add_student(student)
        else: 
            print(f'No class is available for {classroom.name} currently')

    def __repr__(self) -> str:
        print(f'------------{self.name} has classrooms-------------')
        for key, value in self.classrooms.items():
            print(key)

        print(f'---------students---------')
        for student in self.classrooms['class_10'].students:
            print(student)

        print(f'---------subjects---------')
        for subject in self.classrooms['class_10'].subjects:
            print(subject.name)
        return ''
    
class Classroom:
    def __init__(self, name) -> None:
        self.name = name
        #compositions
        self.students = []
        self.subjects = []
    
    def add_student(self, student):
        serial_id = f'{self.name}_{len(self.students)+1}'
        student.id = serial_id
        student.classroom = self.name
        self.students.append(student)
    
    def add_subject(self, subject):
        self.subjects.append(subject)

    def __str__(self) -> str:
        return f'{self.name}_jhakanaka_{len(self.students)}'
    
    
    # TODO: sort students by grade
    def get_top_students(self):
        pass

class Subject:
    def __init__(self, name, teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.max_mark = 100
        self.pass_mark = 33

    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark