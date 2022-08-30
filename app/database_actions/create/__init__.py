from database.schemas import User, Password
from database import Session, engine
from random import randint
from helpers import user_profile

session = Session(bind = engine)
id = randint(1,1000000)

def add_user_db(profile):
  new_user = User(id = id, username = profile["username"], email = profile["email"], password = profile["password"])
  
  try: 
    session.add(new_user)
    session.commit()
    print("""
    **********************

        NEW USER ADDED!

    **********************
    """)
  except:
    print("""
    
    ********** There was a problem **********
    
    """)

def add_password_db(new_password, password_matches):
  # user = session.query(User).filter_by(id = user_profile["id"])
  new_password = Password(id = id, password = new_password, matches = password_matches, belongs_to = user_profile["id"])

  # try: 
  session.add(new_password)
  session.commit()
    # print("""
    # ***************************

    #     NEW PASSWORD ADDED!

    # ***************************
    # """)
  # except:
  #   print("""
    
  #   ********** There was a problem **********
    
  #   """)