from database.schemas.User import User
from database import Session, engine
import bcrypt

session = Session(bind=engine)


def login(credentials):
    users = session.query(User).filter_by(username=credentials["username"])

    print(users)
    # if "username_1" in users[0]:

    try:
      auth = bcrypt.checkpw(
        credentials["password"].encode("utf-8"),
        users[0].password.encode("utf-8")
      )
    except:
        return False

    return auth
    # else:
    #     return False

    # for user in users:
    #   print(user.username)
    #   print(user.password)
