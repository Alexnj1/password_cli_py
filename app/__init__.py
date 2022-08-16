from __future__ import print_function, unicode_literals
from prompt import question_prompt
from generator import password_generator

# grabs the prompt answers packaged into an object from the prompt function
choices = question_prompt()

# creates password
new_password = password_generator(
  choices["password_length"], 
  choices["uppercase_letters"], 
  choices["lowercase_letters"],
  choices["special_characters"],
  choices["numbers"]
)

if new_password == False:
  print("Failed! Must select upper or lower case!")
else: print(new_password)
