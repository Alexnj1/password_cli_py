from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

# Table class for User with column definitions
class User(Base):
    __tablename__ = "User_2"
    id = Column(Integer(), primary_key = True)
    username = Column(String(50), nullable= False, unique = True)
    email = Column(String(80), unique = True, nullable = False)
    password = Column(String(100), nullable = False)
    date_created = Column(DateTime(), default = datetime.utcnow())

    def __repr__(self):
        # Returns string representation of User class
        return f"<User username ={self.username} email={self.email}"

# new_user = User(id = 3, username = "msater1003", email = "alex@alex.com")
# print(new_user.__tablename__)