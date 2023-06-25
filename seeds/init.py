import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from database.db import session
from database.models import Teacher, Student, TeacherStudent, Group
from seeds.groups import insert_group
from seeds.grades import insert_grades
from seeds.subjects import insert_subject


fake = Faker('uk-UA')


def insert_students():
    groups = session.query(Group).all()
    for _ in range(50):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            group_id=random.choice(groups).id
        )
        session.add(student)


def insert_teachers():
    for _ in range(5):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            start_work=fake.date_between(start_date='-7y')
        )
        session.add(teacher)


def insert_rel():
    students = session.query(Student).all()
    teachers = session.query(Teacher).all()

    for student in students:
        rel = TeacherStudent(teacher_id=random.choice(teachers).id, student_id=student.id)
        session.add(rel)


if __name__ == '__main__':
    try:
        insert_group()
        insert_students()
        insert_teachers()
        session.commit()
        insert_rel()
        session.commit()
        insert_subject()
        session.commit()
        insert_grades()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
