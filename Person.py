import random

class Person:
    def __init__(self, name) -> None:
        self.name = name

class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def teach(self):
        pass

    def evaluate_exam(self):
        marks = random.randint(0, 100)
        return marks

    def __repr__(self):
        return f'Teacher {self.name}'

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
