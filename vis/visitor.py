
class Person(object):

    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        raise NotImplementedError()


class Student(Person):

    def __init__(self, name):
        super().__init__(name)

    def accept(self, visitor):
        return visitor.visit_student(self)


class Professor(Person):

    def __init__(self, name):
        super().__init__(name)

    def accept(self, visitor):
        return visitor.visit_professor(self)


class Visitor(object):

    def visit_student(self, student):
        raise NotImplementedError()

    def visit_professor(self, professor):
        raise NotImplementedError()


class Session(Visitor):

    def visit_student(self, student):
        return "{} сдаёт сессию".format(student.name)

    def visit_professor(self, professor):
        return "{} принимает экзамен".format(professor.name)


class Vacation(Visitor):

    def visit_student(self, student):
        return "{} отдыхает".format(student.name)

    def visit_professor(self, professor):
        return "{} в отпуске".format(professor.name)
