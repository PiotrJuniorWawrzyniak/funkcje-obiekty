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
