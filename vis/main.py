from visitor import Student
from visitor import Professor
from visitor import Session
from visitor import Vacation


def main():
    student = Student("Агафонова Ю.Д.")
    professor = Professor("Степанов А.Н.")
    session = Session()
    vacation = Vacation()
    print(student.accept(session))
    print(professor.accept(session))
    print(student.accept(vacation))
    print(professor.accept(vacation))


if __name__ == "__main__":
    main()
