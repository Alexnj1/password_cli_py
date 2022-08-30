from InquirerPy import inquirer

def validates_email(email):
  if "@" in email:
    # Doesn't currently work, might need to be handled elsewhere
    # if len(email) <= 80 & len(email) > 0:
      return True
  return False

def validates_length(string, length):
  if len(string) > 0 & len(string) <= length:
    return True
  return False

def new_user():
  username = inquirer.text(
    message = "What is your new username?",
    validate = lambda result: validates_length(result, 50),
    invalid_message = "Username must be 50 characters or less"
  ).execute()

  email = inquirer.text(
    message = "What is your email?",
    validate = lambda result: validates_email(result),
    invalid_message= "Email must be in the proper format and 80 characters or less"
  ).execute()

  password = inquirer.text(
    message = "What is your new password?",
    validate = lambda result: validates_length(result, 100),
    invalid_message= "Password must be 100 characters or less"
  ).execute()

  choices = {
    "username": username,
    "email": email,
    "password": password
  }


  return choices

