import unittest

from unittest import TestCase

from visitor import Student
from visitor import Professor
from visitor import Session
from visitor import Vacation


class TestStudent(TestCase):

    def test_accept(self):
        student = Student("Агафонова Ю.Д.")
        session = Session()
        vacation = Vacation()
        accept_session = student.accept(session)
        accept_vacation = student.accept(vacation)
        self.assertEqual(accept_session, "Агафонова Ю.Д. сдаёт сессию")
        self.assertEqual(accept_vacation, "Агафонова Ю.Д. отдыхает")


class TestProfessor(TestCase):

    def test_accept(self):
        professor = Professor("Степанов А.Н.")
        session = Session()
        vacation = Vacation()
        accept_session = professor.accept(session)
        accept_vacation = professor.accept(vacation)
        self.assertEqual(accept_session, "Степанов А.Н. принимает экзамен")
        self.assertEqual(accept_vacation, "Степанов А.Н. в отпуске")


class TestSession(TestCase):

    def test_visit_student(self):
        student = Student("Агафонова Ю.Д.")
        session = Session()
        visit_student = session.visit_student(student)
        self.assertEqual(visit_student, "Агафонова Ю.Д. сдаёт сессию")

    def test_visit_professor(self):
        professor = Professor("Степанов А.Н.")
        session = Session()
        visit_professor = session.visit_professor(professor)
        self.assertEqual(visit_professor, "Степанов А.Н. принимает экзамен")


class TestVacation(TestCase):

    def test_visit_student(self):
        student = Student("Агафонова Ю.Д.")
        vacation = Vacation()
        visit_student = vacation.visit_student(student)
        self.assertEqual(visit_student, "Агафонова Ю.Д. отдыхает")

    def test_visit_professor(self):
        professor = Professor("Степанов А.Н.")
        vacation = Vacation()
        visit_professor = vacation.visit_professor(professor)
        self.assertEqual(visit_professor, "Степанов А.Н. в отпуске")


if __name__ == "__main__":
    unittest.main()
