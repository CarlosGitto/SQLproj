from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from sqlalchemy.sql.schema import ForeignKey
from myengine import Base, engine

class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer(), primary_key=True)
    product_id = Column(Integer(), ForeignKey("product.id"))
    expense_family_id = Column(Integer, ForeignKey("expense_family.id"))
    expense_items_id = Column(Integer, ForeignKey("expense_items.id"))
    assigned_expense_items_id = Column(Integer, ForeignKey("assigned_expense_items.id"))
    created_at = Column(DateTime(), default=datetime.now())



class Product(Base):
    __tablename__ = "product"

    id = Column(Integer(), primary_key=True)
    price = Column(Integer(),nullable=False, unique=False)
    cost = Column(Integer(), nullable=False, unique=False)
    stock = Column(Integer(), nullable=False, unique=False)


class ExpenseFamily(Base):
    __tablename__ = "expense_family"

    id = Column(Integer(), primary_key=True)
    service_name = Column(String(225), nullable=False, unique=False)
    



class ExpenseItems(Base):
    __tablename__ = "expense_items"

    id = Column(Integer(), primary_key=True)
    


class AssignedExpenseItems(Base):
    __tablename__ = "assigned_expense_items"

    id = Column(Integer(), primary_key=True)
 
