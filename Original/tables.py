from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from myengine import Base, engine

class Luz(Base):
    __tablename__ = "luz"

    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=False)
    cost = Column(Integer(), nullable=False, unique=False)
    email = Column(String(50), nullable=False, unique=False)
    receipt = Column(String(50), nullable=True)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.username

class Internet(Base):
    __tablename__ = "internet"

    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=False)
    cost = Column(Integer(), nullable=False, unique=False)
    email = Column(String(50), nullable=False, unique=False)
    receipt = Column(String(50), nullable=True)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.username

class Gas(Base):
    __tablename__ = "gas"

    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=False)
    cost = Column(Integer(), nullable=False, unique=False)
    email = Column(String(50), nullable=False, unique=False)
    receipt = Column(String(50), nullable=True)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.username

class Agua(Base):
    __tablename__ = "agua"

    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=False)
    cost = Column(Integer(), nullable=False, unique=False)
    email = Column(String(50), nullable=False, unique=False)
    receipt = Column(String(50), nullable=True)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.username
