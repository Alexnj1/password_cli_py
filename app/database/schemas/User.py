from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import validates
import bcrypt
from app.database import Base, engine

# Table class for User with column definitions
class User(Base):
    __tablename__ = "Users_1"
    # extend_existing = True
    id = Column(Integer(), primary_key = True, auto_increment = True)
    username = Column(String(50), nullable= False, unique = True)
    email = Column(String(80), unique = True, nullable = False)
    password = Column(String(100), nullable = False)
    date_created = Column(DateTime(), default = datetime.utcnow())

    @validates('password')
    def validate_password(self, key, password):
        assert len(password) >= 8
        password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(10))
        return password
    
    @validates("email")
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError("failed simple email validation")
        return address

    def __repr__(self):
        # Returns string representation of User class
        # Used for class testing purposes
        return f"<User username ={self.username} email={self.email}"

Base.metadata.create_all(engine)

# new_user = User(id = 3, username = "msater1003", email = "alex@alex.com")
# print(new_user.__tablename__)