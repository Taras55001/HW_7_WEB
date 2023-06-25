import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from database.db import session
from database.models import Group


fake = Faker('uk-UA')


def insert_group():
    
    groups = ["ФФ-11", "GoIt-12", "ЕМ-10"]
    for g in groups:
        session.add(Group(group_name=g))







if __name__ == '__main__':
    try:
        insert_group()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
