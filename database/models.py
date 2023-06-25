from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func, event, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property


Base = declarative_base()


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column("cell_phone", String(120))
    address = Column(String(120))
    start_work = Column(Date, nullable=False)
    students = relationship(
        "Student", secondary="teachers_to_students", back_populates="teachers"
    )
    subject = relationship("Subject", backref="teachers")

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class Student(Base):
    __tablename__ = "students"
    id = Column("id", Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column("cell_phone", String(120))
    address = Column(String(120))
    teachers = relationship(
        "Teacher", secondary="teachers_to_students", back_populates="students"
    )
    group_id = Column(
        Integer, ForeignKey("groups.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    grade = relationship("Grade", backref="students")
    group = relationship("Group", backref="students")

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class Contact(Base):
    __tablename__ = "contacts"
    id = Column("id", Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column("cell_phone", String(120))
    address = Column(String(120))
    student_id = Column('student_id', ForeignKey("students.id", ondelete="CASCADE", onupdate="CASCADE"))
    student = relationship("Student", backref="contacts")

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class TeacherStudent(Base):
    __tablename__ = "teachers_to_students"
    id = Column("id", Integer, primary_key=True)
    teacher_id = Column(
        Integer, ForeignKey("teachers.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    student_id = Column(
        Integer, ForeignKey("students.id", ondelete="CASCADE", onupdate="CASCADE")
    )

class Group(Base):
    __tablename__ = "groups"
    id = Column("id", Integer, primary_key=True)
    group_name = Column(String(16))
    


class Grade(Base):
    __tablename__ = "grades"
    id = Column("id", Integer, primary_key=True)
    grade_value = Column(Integer)
    time_of = Column("date",DateTime())

    subject_id = Column(
        Integer, ForeignKey("subject.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    student_id = Column(
        Integer, ForeignKey("students.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    subject = relationship("Subject", backref="grade")

class Subject(Base):
    __tablename__ = "subject"
    id = Column("id", Integer, primary_key=True)
    subject_name = Column(String(120))
    teacher_id = Column(
        Integer, ForeignKey("teachers.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    
