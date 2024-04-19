class Student:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name


class Teacher:
    def __init__(self, name, subject, class_taught):
        self.name = name
        self.subject = subject
        self.class_taught = class_taught


class ClassTutor:
    def __init__(self, name, class_managed):
        self.name = name
        self.class_managed = class_managed


students = []
teachers = []
class_tutors = []


def create_student():
    name = input('Podaj imie i nazwisko ucznia: ')
    class_name = input('Podaj nazwe klasy: ')
    student = Student(name, class_name)
    students.append(student)
    return student


def create_teacher():
    name = input('Podaj imie i nazwisko nauczyciela: ')
    subject = input('Podaj nazwe przedmiotu: ')
    class_taught = input('Podaj, ktora klase uczy: ')
    teacher = Teacher(name, subject, class_taught)
    teachers.append(teacher)
    return teacher


def create_class_tutor():
    name = input('Podaj imie i nazwisko wychowawcy: ')
    class_managed = input('Podaj klase, ktorej jest wychowawca: ')
    class_tutor = ClassTutor(name, class_managed)
    class_tutors.append(class_tutor)
    return class_tutor


def manage_class():
    class_name = input('Podaj nazwe klasy, ktora chcesz wyswietlic: ')
    print(f'Uczniowie klasy {class_name}: ')
    for student in students:
        if student.class_name == class_name:
            print(student.name)
    print(f'Wychowawca klasy {class_name} jest: ')
    for class_tutor in class_tutors:
        if class_tutor.class_managed == class_name:
            print(class_tutor.name)


def manage_student():
    student_name = input('Podaj imie i nazwisko ucznia, ktorego chcesz wyswietlic: ')
    for student in students:
        if student.name == student_name:
            print(f'Lekcje ucznia {student.name}: ')
            for teacher in teachers:
                if teacher.class_taught == student.class_name:
                    print(f'{teacher.subject} - {teacher.name}')


def manage_teacher():
    teacher_name = input('Podaj imie i nazwisko nauczyciela, ktorego chcesz wyswietlic: ')
    for teacher in teachers:
        if teacher.name == teacher_name:
            print(f'Klasy nauczyciela {teacher.name}: {teacher.class_taught}')


def manage_class_tutor():
    class_tutor_name = input('Podaj imie i nazwisko wychowawcy, ktorego chcesz wyswietlic: ')
    print(f'Uczniowie wychowawcy {class_tutor_name}: ')
    for class_tutor in class_tutors:
        if class_tutor.name == class_tutor_name:
            for student in students:
                if student.class_name == class_tutor.class_managed:
                    print(student.name)
