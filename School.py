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
        print(f'{self.name} has classrooms')
        for key, value in self.classrooms.items():
            print(key, value)
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

    def __str__(self) -> str:
        return f'{self.name}_jhakanaka_{len(self.students)}'
    
    # TODO: sort students by grade
    def get_top_students(self):
        pass

