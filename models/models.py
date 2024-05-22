# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, text, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


Base = declarative_base()
metadata = Base.metadata

class Subject(Base):
  __tablename__ = 'subjects'
  id = Column(Integer, primary_key=True)
  subject_name = Column(String(255), nullable=False)
  description = Column(String(1024), nullable=False)


class Student(Base):
  __tablename__ = 'students'
  id = Column(Integer, primary_key=True)
  student_name = Column(String(80), nullable=False)
  contact = Column(String(20), nullable=False)
  class_name = Column(String(50))
  school = Column(String(80))
  doj = Column(Date)
