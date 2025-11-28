from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean, ForeignKey, BigInteger
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime, timezone

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    name = Column(String(100))
    username = Column(String(100))
    active = Column(Boolean, default=False)
    created_on = Column(DateTime, default=datetime.now)
    created_by = Column(String(100), default='telegram-bot')
    updated_on = Column(DateTime, nullable=True)
    updated_by = Column(String(100), nullable=True)

    expenses = relationship('Expense', back_populates='user')

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    description = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_on = Column(DateTime, default=datetime.now)
    created_by = Column(String(100), default='telegram-bot')
    updated_on = Column(DateTime, nullable=True)
    updated_by = Column(String(100), nullable=True)

    user = relationship('User', back_populates='expenses')
