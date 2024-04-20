OPTIONS = ['utworz', 'zarzadzaj', 'koniec']
CREATE_OPTIONS = ['uczen', 'nauczyciel', 'wychowawca', 'koniec']
MANAGE_OPTIONS = ['klasa', 'uczen', 'nauczyciel', 'wychowawca', 'koniec']


class Student:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name


class Teacher:
    def __init__(self, name, subject, classes_taught):
        self.name = name
        self.subject = subject
        self.classes_taught = classes_taught

    def __str__(self):
        return f'Nauczyciel: {self.name}\nPrzedmiot: {self.subject}\nKlasa: {self.classes_taught}'


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
    student = Student(name=name, class_name=class_name)
    students.append(student)
    return student


def create_teacher():
    name = input('Podaj imie i nazwisko nauczyciela: ')
    subject = input('Podaj nazwe przedmiotu: ')
    classes_taught = []
    while True:
        class_name = input('Podaj nazwe klasy: ')
        if not class_name:
            break
        classes_taught.append(class_name)

    teacher = Teacher(name=name, subject=subject, classes_taught=classes_taught)
    teachers.append(teacher)
    return teacher


def create_class_tutor():
    name = input('Podaj imie i nazwisko wychowawcy: ')
    class_managed = input('Podaj klase, ktorej jest wychowawca: ')
    class_tutor = ClassTutor(name=name, class_managed=class_managed)
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
            print(f'Lekcje ucznia {student.name} z klasy {student.class_name}: ')
            for teacher in teachers:
                for class_taught in teacher.classes_taught:
                    if class_taught == student.class_name:
                        print(teacher)


def manage_teacher():
    teacher_name = input('Podaj imie i nazwisko nauczyciela, ktorego chcesz wyswietlic: ')
    for teacher in teachers:
        if teacher.name == teacher_name:
            print(f'Klasy nauczyciela {teacher.name} [przedmiot {teacher.subject}]: {teacher.classes_taught}')


def manage_class_tutor():
    class_tutor_name = input('Podaj imie i nazwisko wychowawcy, ktorego chcesz wyswietlic: ')
    print(f'Uczniowie wychowawcy {class_tutor_name}: ')
    for class_tutor in class_tutors:
        if class_tutor.name == class_tutor_name:
            for student in students:
                if student.class_name == class_tutor.class_managed:
                    print(student.name)


def main():
    while True:
        print(f'Dostepne opcje: {OPTIONS}')
        user_choice = input('Wybierz opcje: ')

        if user_choice == 'utworz':
            while True:
                create_choice = input(f'Kogo chcesz dodac? {CREATE_OPTIONS}: ')
                if create_choice == 'uczen':
                    create_student()
                elif create_choice == 'nauczyciel':
                    create_teacher()
                elif create_choice == 'wychowawca':
                    create_class_tutor()
                elif create_choice == 'koniec':
                    break
                else:
                    print('Niepoprawna opcja, wybierz jeszcze raz.')

        elif user_choice == 'zarzadzaj':
            while True:
                manage_choice = input(f'Co chcesz wyswietlic? {MANAGE_OPTIONS}: ')
                if manage_choice == 'klasa':
                    manage_class()
                elif manage_choice == 'uczen':
                    manage_student()
                elif manage_choice == 'nauczyciel':
                    manage_teacher()
                elif manage_choice == 'wychowawca':
                    manage_class_tutor()
                elif manage_choice == 'koniec':
                    break
                else:
                    print('Niepoprawna opcja, wybierz jeszcze raz.')

        elif user_choice == 'koniec':
            break

        else:
            print('Niepoprawna opcja, wybierz jeszcze raz.')


if __name__ == '__main__':
    main()
