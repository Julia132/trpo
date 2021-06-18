from visitor import Student
from visitor import Professor
from visitor import Session
from visitor import Vacation


def main():
    student = Student("Юляша")
    professor = Professor("Степанов")
    session = Session()
    vacation = Vacation()
    student.accept(session)
    professor.accept(session)
    student.accept(vacation)
    professor.accept(vacation)


if __name__ == "__main__":
    main()
