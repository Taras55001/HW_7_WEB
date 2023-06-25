import random
from datetime import datetime

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from database.db import session
from database.models import Grade,Subject, Student


fake = Faker('uk-UA')


def insert_grades():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for student in students:
        for _ in range(20):
            grade = Grade(
                grade_value=random.choice(list(range(1, 13))),
                subject_id=random.choice(subjects).id,
                student_id=student.id,
                time_of=fake.date_between(start_date=datetime(2022, 9, 1).date(),end_date=datetime(2023, 6, 30).date())
            )
            session.add(grade)





if __name__ == '__main__':
    try:
        insert_grades()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
