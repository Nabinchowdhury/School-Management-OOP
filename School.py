#School, name, address , add classroom, student admission, Classroom, add student

class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        #compositions
        self.classrooms = {} #dictionary
    
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
    
    def student_admission(self, student, classroom_name):
        if classroom_name in self.classrooms:
            self.classrooms[classroom_name].add_student(student)
        else: 
            print(f'No class is available for {classroom_name} currently')

class Classroom:
    def __init__(self, class_name) -> None:
        self.classroom_name = class_name
        #compositions
        self.students = []
    
    def add_student(self, student):
        serial_id = f'{self.name}_{len(self.students)+1}'
        self.students.append(student)

    def __str__(self) -> str:
        return f'{self.name}_{len(self.students)}'
    
    # TODO: sort students by grade
    def get_top_students(self):
        pass