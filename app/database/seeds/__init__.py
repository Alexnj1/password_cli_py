from app.database import Session, engine
from app.database.schemas import User

# Create an instance of a new session and bind it to the database
session = Session(bind = engine)

# test
new_user = User(id = 3, username = "alexnj1", email = "alex@alex.com", password = "password1234")

# Add and commit
session.add(new_user)

session.commit()