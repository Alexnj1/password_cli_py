from InquirerPy import inquirer

def valid_length(number):
  if number.isnumeric():
    if int(number) >= 25 | int(number) <= 100:
      return True
  return False

def question_prompt():
  password_length = inquirer.text(
    message="What should the length of your password be?",
    validate= lambda result: valid_length(result),
    invalid_message= "Length must be a number from 25 to 100"
  ).execute()
  if password_length:
    password_length = int(password_length)

  uppercase = inquirer.select(
    message="Would you like uppercase letters?",
    choices=["Yes", "No"],
    default= None
  ).execute()
  if uppercase == "Yes":
    uppercase = True
  else:
    uppercase = False

  lowercase = inquirer.select(
    message="Would you like lowercase letters?",
    choices=["Yes", "No"],
    default= None
  ).execute()
  if lowercase == "Yes":
    lowercase = True
  else:
    lowercase = False
  
  special = inquirer.select(
    message="Would you like special characters?",
    choices=["Yes", "No"],
    default= None
  ).execute()
  if special == "Yes":
    special = True
  else:
    special = False

  numbers = inquirer.select(
    message= "Would you like numbers?",
    choices= ["Yes", "No"],
    default= None
  ).execute()
  if numbers == "Yes":
    numbers = True
  else:
    numbers = False

  choices = {
    "password_length": password_length,
    "uppercase_letters": uppercase,
    "lowercase_letters": lowercase,
    "special_characters": special,
    "numbers": numbers
  }

  return choices