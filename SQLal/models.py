from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from sqlalchemy.sql.expression import null

from sqlalchemy.sql.schema import CheckConstraint, ForeignKey
from myengine import Base, engine

class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer(), primary_key=True)
    product_id = Column(Integer(), ForeignKey("product.id"))
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
    item_name = Column(String(225), nullable=False, unique=True)
    id_family = Column(Integer(), ForeignKey("expense_family.id"))
    cost= Column(Integer())    


class AssignedExpenseItems(Base):
    __tablename__ = "assigned_expense_items"

    id = Column(Integer(), primary_key=True)
    items_id = Column(Integer(), ForeignKey("expense_items.id"))
    state = Column(String(224))
    created_at = Column(DateTime(), default=datetime.now())

 
