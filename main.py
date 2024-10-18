from School import School, Classroom
from Person import Student

def main():
    admaji_school = School('adam_ji', 'uttara')
    class_8 = Classroom('class_8')
    admaji_school.add_classroom(class_8)
    class_9 = Classroom('class_9')
    admaji_school.add_classroom(class_9)
    class_10 = Classroom('class_10')
    admaji_school.add_classroom(class_10)
    print(admaji_school)
    
    stu_nabin = Student('Nabin')
    print(f'before admission {stu_nabin}')

    School.student_admission(admaji_school, stu_nabin, class_10)
    print(f'after admission {stu_nabin}')
if __name__ == '__main__':
    main()