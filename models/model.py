# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, text, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Administrator(Base):
    __tablename__ = 'Administrator'

    ID = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    user_id = Column(ForeignKey('User.ID'), index=True)

    user = relationship('User')


class Quiz(Base):
    __tablename__ = 'Quiz'

    ID = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    subject = Column(String(255))
    created_by = Column(ForeignKey('User.ID'), index=True)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    User = relationship('User')


class QuizAnswer(Base):
    __tablename__ = 'QuizAnswer'

    ID = Column(Integer, primary_key=True)
    question_id = Column(ForeignKey('QuizQuestion.ID'), index=True)
    answer = Column(Text)
    is_correct = Column(Integer)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    question = relationship('QuizQuestion')


class QuizQuestion(Base):
    __tablename__ = 'QuizQuestion'

    ID = Column(Integer, primary_key=True)
    quiz_id = Column(ForeignKey('Quiz.ID'), index=True)
    question = Column(Text)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    quiz = relationship('Quiz')


class StudyMaterial(Base):
    __tablename__ = 'StudyMaterial'

    ID = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    subject = Column(String(255))
    content = Column(Text)
    created_by = Column(ForeignKey('User.ID'), index=True)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    User = relationship('User')

class User(Base):
    __tablename__ = 'User'
    ID = Column(Integer, primary_key=True)
    student_name = Column(String(255), nullable=False)
    contact = Column(String(255), nullable=False)
    class_name = Column(String(255), nullable=False)
    school = Column(String(255), nullable=False)
    doj = Column(Date)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class UserAnswer(Base):
    __tablename__ = 'UserAnswer'

    ID = Column(Integer, primary_key=True)
    user_question_id = Column(ForeignKey('UserQuestion.ID'), index=True)
    answer = Column(Text)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    user_question = relationship('UserQuestion')


class UserQuestion(Base):
    __tablename__ = 'UserQuestion'

    ID = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('User.ID'), index=True)
    question = Column(Text)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    user = relationship('User')


class UserQuizResult(Base):
    __tablename__ = 'UserQuizResult'

    ID = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('User.ID'), index=True)
    quiz_id = Column(ForeignKey('Quiz.ID'), index=True)
    score = Column(Integer)
    total_questions = Column(Integer)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    quiz = relationship('Quiz')
    user = relationship('User')


class UserStudyMaterial(Base):
    __tablename__ = 'UserStudyMaterial'

    ID = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('User.ID'), index=True)
    study_material_id = Column(ForeignKey('StudyMaterial.ID'), index=True)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    study_material = relationship('StudyMaterial')
    user = relationship('User')
