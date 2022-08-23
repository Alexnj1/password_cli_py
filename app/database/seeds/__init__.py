from random import randint
from app.database import Session, engine
from app.database.schemas.User import User

# Create an instance of a new session and bind it to the database
session = Session(bind = engine)

# test
new_user = User(id = randint(1,1000000), username = "passwordtest", email = f"password{randint(1,1000000)}@alex.com", password = "password1234")

# Add and commit
def add_test():
  session.add(new_user)
  session.commit()

