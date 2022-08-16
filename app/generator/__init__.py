import random
from random import randint
import string

def password_generator(length, upper, lower, special, numbers):
  letters = string.ascii_letters
  letters_lower = string.ascii_lowercase
  letters_upper = string.ascii_uppercase
  special_chars = '!@#$%^&*()!@#$%^&*()'
  number_chars = '12345678901234567890'
  password_string = ''

  if upper == True & lower == True:
    for x in letters:
      password_string += letters[randint(0,51)]
  elif upper == True:
    for x in letters_upper:
      password_string += letters_upper[randint(0,25)]
  elif lower == True:
    for x in letters_lower:
      password_string += letters_lower[randint(0,25)]
  else: return False

  if special == True & numbers == True: 
    for x in special_chars:
      password_string += special_chars[randint(0,8)]
    for x in number_chars:
      password_string += number_chars[randint(0,8)]
  elif special == True:
    for x in special_chars:
      password_string += special_chars[randint(0,8)]
  elif numbers == True:
    for x in number_chars:
      password_string += number_chars[randint(0,8)]
  # password_string = password_string[0:length]
  password_string = random.sample(password_string, length)
  return "".join(password_string)