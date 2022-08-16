from InquirerPy import inquirer
from InquirerPy.validator import NumberValidator

def valid_length(number):
  if number >= 8 | number <= 100:
    return True
  return False

def question_prompt():
  password_length = inquirer.text(
    message="What should the length of your password be?",
    validate= lambda result: valid_length(int(result)),
    invalid_message= "Length must be a number from 8 to 100"
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

  choices = {
    "password_length": password_length,
    "uppercase_letters": uppercase,
    "lowercase_letters": lowercase
  }

  return choices