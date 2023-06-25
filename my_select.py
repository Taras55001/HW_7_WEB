from sqlalchemy import func, desc

from database.db import session
from database.models import Student, Teacher, Grade, Group, Subject

def select_1():
    print('Знайти 5 студентів із найбільшим середнім балом з усіх предметів.')
    data = session.query(Student.fullname, func.round(func.avg(Grade.grade_value), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    print(data)
        

def select_2():
    print('Знайти студента із найвищим середнім балом з певного предмета.')
    data=session.query(Student.fullname, func.round(func.avg(Grade.grade_value), 2).label('avg_grade'))\
    .join(Grade).join(Subject)\
    .filter(Subject.id == '2')\
    .group_by(Student.id)\
    .order_by(func.avg(Grade.grade_value).desc())\
    .first()
    print(data)
    

def select_3():
    print('Знайти середній бал у групах з певного предмета.')
    data=session.query(Group.group_name, func.round(func.avg(Grade.grade_value), 2).label('avg_grade'))\
    .join(Student, Group.id == Student.group_id)\
    .join(Grade, Student.id == Grade.student_id)\
    .join(Subject, Grade.subject_id == Subject.id)\
    .filter(Subject.id == '2')\
    .group_by(Group.group_name, Subject.subject_name)\
    .all()
    print(data)
    


def select_4():
    print('Знайти середній бал на потоці (по всій таблиці оцінок).')
    print({session.query(func.round(func.avg(Grade.grade_value), 2).label('avg_grade')).scalar()})


def select_5():
    print('Знайти, які курси читає певний викладач.')
    data = session.query(Subject.subject_name).join(Teacher).filter(Teacher.id == '1').all()
    print(data)


def select_6():
    print('Знайти список студентів у певній групі.')
    
    print(session.query(Student.fullname).join(Group).filter(Group.id == '2').all()
    )

def select_7():
    print('Знайти оцінки студентів в окремій групі з певного предмета.')
    data =session.query(Student.fullname, Grade.grade_value)\
    .join(Group)\
    .join(Grade, Student.id == Grade.student_id)\
    .join(Subject, Subject.id == Grade.subject_id)\
    .filter(Student.group_id == '1', Subject.id == '2')\
    .all()
    print(data)

def select_8():
    print('Знайти середній бал, який ставить певний викладач зі своїх предметів.')
    data =session.query(Subject.subject_name, func.round(func.avg(Grade.grade_value), 2))\
    .join(Teacher, Teacher.id == Subject.teacher_id)\
    .join(Grade, Grade.subject_id == Subject.id)\
    .filter(Teacher.id == '1')\
    .group_by(Subject)\
    .all()
    print(data)

def select_9():
    print('Знайти список курсів, які відвідує певний студент.')
    data =session.query(Subject.subject_name)\
    .join(Grade, Subject.id == Grade.subject_id)\
    .join(Student, Student.id == Grade.student_id)\
    .filter(Student.id == '2')\
    .group_by(Subject)\
    .all()
    print(data)

def select_10():
    print('Список курсів, які певному студенту читає певний викладач.')
    data =session.query(Subject.subject_name)\
    .join(Teacher, Teacher.id == Subject.teacher_id)\
    .join(Grade, Grade.subject_id == Subject.id)\
    .join(Student, Student.id == Grade.student_id)\
    .filter(Teacher.id == '1', Student.id == '2')\
    .group_by(Subject.subject_name)\
    .all()
    print(data)

if __name__ == '__main__':
    select_1()
    select_2()
    select_3()
    select_4()
    select_5()
    select_6()
    select_7()
    select_8()
    select_9()
    select_10()
    
    