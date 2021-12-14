


from sqlalchemy.orm import sessionmaker
from myengine import engine,Base
from tables import *


Session = sessionmaker(engine)
session = Session()





def new_pay(service,user,cost,email):
    new_pay = service(username= user, cost= cost, email= email, receipt="pagado")
    session.add(new_pay)
    session.commit()

def delete_pay(service,id):
    session.query(table_name).filter(
        table_name.id == id
    ).delete()
    session.commit()

def edit_pay(service,id,command):
    if command == "costo":
        session.query(service).filter(
            service.id == id
            ).update(
                {
                    service.cost: input("ingrese el valor correcto: ")
                }
            )
    if command == "datos":
        session.query(service).filter(
            service.id == id
            ).update(
                {
                    service.email: input("ingrese el valor correcto(email): "),
                    service.username: input("ingrese el valor correcto(nombre): ")
                }
            )
    if command == "recibo":
        session.query(service).filter(
            service.id == id
            ).update(
                {
                    service.cost: input("ingrese el valor correcto(recibo): ")
                }
            )
    session.commit()

def select(tb_name):
    s = session.query(tb_name.id,tb_name.cost,tb_name.receipt,tb_name.created_at).all()
    return(s)
    



    


