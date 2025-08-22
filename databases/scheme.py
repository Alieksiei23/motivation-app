from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, DateTime, String

class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True)


class Users(Base):
    __tablename__ = 'users'

    username = Column(String)
    password = Column(String)
    email = Column(String)
    date_start = Column(DateTime)


class Letters(Base):
    __tablename__ = 'letters'

    letter = Column(String)
