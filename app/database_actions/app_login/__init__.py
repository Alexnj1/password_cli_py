from database.schemas.User import User
from database import Session, engine
from helpers import current_user_profile
import bcrypt

session = Session(bind=engine)


def login(credentials):
    users = session.query(User).filter_by(username=credentials["username"])

    # User table columns
        # ID, USERNAME, EMAIL, PASSWORD, DATE_CREATED

    current_user_profile(users)

    # print(users[0])

    try:
      auth = bcrypt.checkpw(
        credentials["password"].encode("utf-8"),
        users[0].password.encode("utf-8")
      )
    except:
        return False

    # print(auth)
    return auth
