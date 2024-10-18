import random

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
        self.classroom = None
        self.grade = None
        self.subjects = []
        self.marks = {}
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

    def __repr__(self):
        return f'Student {self.name}, id {self.id}, classroom {self.classroom}, grade {self.grade}, subjects {self.subjects}, marks {self.marks}'
