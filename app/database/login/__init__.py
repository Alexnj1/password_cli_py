from database.schemas.User import User
from database import Session, engine
import bcrypt

session = Session(bind = engine)

def login(credentials):
  users = session.query(User).filter_by(username = credentials["username"])
  
  
  return bcrypt.checkpw(credentials["password"].encode("utf-8"), users[0].password.encode("utf-8"))


  # print(users[0].password)
  # for user in users:
  #   print(user.username)
  #   print(user.password)