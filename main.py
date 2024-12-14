from app.curd_operation import (
    add_student, view_students, get_teachers, delete_student, update_student,
)


def main():
    add_student("Dilli", "d@d.com", "password567")
    view_students()
    update_student(3, name="John Wick", email="jk@jk.com")
    delete_student(2)
    get_teachers(3)


if __name__ == "__main__":
    main()

