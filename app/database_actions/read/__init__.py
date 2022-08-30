from database.schemas import Password, User
from database import Session, engine
from helpers import user_profile
from prettytable import PrettyTable
from sqlalchemy import MetaData

# def view_user():

session = Session(bind = engine)


def view_user_passwords():
  passwords = session.query(Password).filter_by(belongs_to = user_profile["id"])
  # password = passwords[0]
  # print(passwords[0], passwords[1])
  
  my_table = PrettyTable()
  my_table.field_names = ["Password", "Matches", "Created_At", "Updated_At"]

  for index in passwords:
    my_table.add_row([index.password, index.matches, index.created_at, index.updated_at])

  print("""
                  ***************************

                        SAVED PASSWORDS
                  
                  ***************************
  """)
  print(my_table)

