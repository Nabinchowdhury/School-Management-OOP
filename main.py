from School import School, Classroom, Subject
from Person import Student, Teacher

def main():
    admaji_school = School('adam_ji', 'uttara')
    class_8 = Classroom('class_8')
    admaji_school.add_classroom(class_8)
    class_9 = Classroom('class_9')
    admaji_school.add_classroom(class_9)
    class_10 = Classroom('class_10')
    admaji_school.add_classroom(class_10)
    
    stu_nabin = Student('Nabin')
    # print(f'before admission {stu_nabin}')

    School.student_admission(admaji_school, stu_nabin, class_10)
    print(f'after admission {stu_nabin}')

    chem_teacher = Teacher('purnima')
    chemistry = Subject('chemistry', chem_teacher)
    class_10.add_subject(chemistry)
    # print(class_10.subjects)
    chemistry.exam(class_10.students)
    print(admaji_school)
if __name__ == '__main__':
    main()