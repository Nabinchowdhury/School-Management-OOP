import random
from School import Classroom
class Person:
    def __init__(self, name) -> None:
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject
    
    def teach(self):
        pass

    def take_exams(self, subject, students):
        for student in students:
            marks = random.randint(0, 100)
            # TODO: set marks for the subject for each student

class Student(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.__id = None
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

st = Student('nabin')
# print(st.name)

classroom = Classroom('class 10')
classroom.add_student(st)
for stu in classroom.students:
    print(stu.name)
    print('id', stu.id)
print('private id', st._Student__id)
print('private id from class', st.id)