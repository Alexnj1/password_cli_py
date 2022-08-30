from __future__ import print_function, unicode_literals
from app.database_actions import login
from prompt import question_prompt, new_user
from generator import password_generator
from database_actions.create import add_user_db, add_password_db
# from helpers import user_profile
from InquirerPy import inquirer

# from app.database.schemas.User import User
# from app.database.seeds import add_test


def length_validator(string):
  if len(string) == 0:
    return False
  return True

def app(): 
  # will act as a pivot point for the application
  # will first allow the user to log into the app or exit

  choice = inquirer.select(
    message= "Would you like to log in, create a new user, or exit?",
    choices=["Login","Create a New User", "Exit"],
    default= None
  ).execute()

  if choice == "Login" :
    # Authenticate the user and run the app
    username = inquirer.text(
      message= "username?",
      validate= lambda string: length_validator(string),
      invalid_message= "You must enter a username"
    ).execute()

    password = inquirer.text(
      message= "password?",
      validate= lambda string: length_validator(string),
      invalid_message= "You must enter a password"
    ).execute()


    credentials = {"username": username, "password" : password}
    # login(credentials)
    authenticated = login(credentials)

    if authenticated:
    # once user is logged in, ask if they would like to create a new password
    # or view current passwords, this needs a new schema for passwords connected to user
      print(
        """
        *********************************************

              WELCOME TO YOUR PASSWORD MANAGER!
        
        *********************************************
        """
      )

      def app_choice():
        choice = inquirer.select(
        message= "Would you like to create a new password, or view your current passwords?",
        choices=["Create New Password", "View Saved Passwords", "Exit Menu"],
        default= None
        ).execute()

        if choice == "Create New Password":
          password_choices = question_prompt()

          # creates password
          new_password = password_generator(
            password_choices["password_length"], 
            password_choices["uppercase_letters"], 
            password_choices["lowercase_letters"],
            password_choices["special_characters"],
            password_choices["numbers"]
          )

          print(f"""
                ***************************************

                          Your new password:

                {new_password}

                ***************************************
                """)

          save = inquirer.select(
            message="Would you like to save this new password?",
            choices=["Yes", "No"],
            default=None
          ).execute()
          
          if save == "Yes":
            # save password function, the re call the app

            add_password_db(new_password, password_choices["password_matches"])
            
            app_choice()

          else: app_choice()
        elif choice == "View Saved Passwords":
          # saved database passwords function
          print("Saved passwords...")
          app_choice()
      
      app_choice()
      
    else: 
      print(  """
      ****************************
      
          Incorect Credentials!
      
      ****************************
      
      """)
      app()

  elif choice == "Create a New User":
    print(
      """
      *************************

          Create a New User
      
      *************************
      """
    )
    new_user_profile = new_user()
    add_user_db(new_user_profile)

  else: return


app()