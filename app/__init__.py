from __future__ import print_function, unicode_literals
from app.database.login import login
from prompt import question_prompt
from generator import password_generator

# from app.database.schemas.User import User
# from app.database.seeds import add_test

from InquirerPy import inquirer


# grabs the prompt answers packaged into an object from the prompt function
# choices = question_prompt()

# creates password
# new_password = password_generator(
#   choices["password_length"], 
#   choices["uppercase_letters"], 
#   choices["lowercase_letters"],
#   choices["special_characters"],
#   choices["numbers"]
# )

# if new_password == False:
#   print("Failed! Must select upper or lower case!")
# else: print(new_password)

# new_user = User(id = 3, username = "alexnj1", email = "alex@alex.com", password = "password1234")


def login_test():
  choice = inquirer.select(
    message= "Would you like to log in or exit?",
    choices=["Login", "Exit"],
    default= None
  ).execute()

  if choice == "Login" :
    username = inquirer.text(
      message= "username?"
    ).execute()

    password = inquirer.text(
      message= "password?"
    ).execute()


    credentials = {"username": username, "password" : password}
    # login(credentials)
    authenticated = login(credentials)

    if authenticated:
      return "WELCOME!"
    return "Incorect Credentials"

  else: return

  

# addTest()
print(login_test())

# def app(): 
  # will act as a pivot point for the application
  # will first allow the user to log into the app or exit
