from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine


engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/exel')
Base = declarative_base()








 




















"""from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/enginetest')
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.username
    
Session = sessionmaker(engine)
session = Session()


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    user1 = User(username="User1", email="user1@example.com")
    user2 = User(username="User2", email="user2@example.com")
    user3 = User(username="User3", email="user3@example.com")

    session.add(user1)
    session.add(user2)
    session.add(user3)

    session.commit()
    
    #SELECT * FROM users;
    #users = session.query(User).all()

    #SELECT email, created_at FROM users WHERE id >= 2 AND username = 'User3' 
    #(Clases) -> instancias de la clase
    #(Argumentos) -> tuplas(solo poseemos los valores que preguntamos)
    #users = session.query(User.email, User.created_at).filter(
    #    User.id >= 2
    #).filter(
    #    User.username == "User3"
    #)
    
    #for user in users:
    #    print(user.created_at)

    
    #para obtener un objeto no iterable se use one or first(la diferencia es que one retorna uyn error y first none)
    #users = session.query(User).filter(
    #    User.id == 1
    #).first()
    

    #modificacion de datos de a uno
    #user = session.query(User).first()
    #user.email = "holamundo.com"
    #session.add(user)
    #session.commit()

    #de a varios
    #session.query(User).filter(
    #    User.id == 1
    #
    #).update(
    #    {
    #        User.email: "catastrofe.com"
    #    }
    #) 
    #session.commit()

    #eliminar valores
    session.query(User).delete()
    session.commit()
    """