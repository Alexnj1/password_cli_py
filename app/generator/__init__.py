from random import randint
import string

def password_generator(length, upper, lower):
  letters = string.ascii_letters
  letters_lower = string.ascii_lowercase
  letters_upper = string.ascii_uppercase
  password_string = ''

  if upper == True & lower == True:
    for x in letters:
      password_string += letters[randint(0,51)]
  if upper == True:
    for x in letters_upper:
      password_string += letters_upper[randint(0,25)]
  if lower == True:
    for x in letters_lower:
      password_string += letters_lower[randint(0,25)]
  else: return False

  password_string = password_string[0:length]

  return password_string