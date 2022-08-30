user_profile = {
  "id" : None,
  "username": None,
  "email": None,
  "date_created": None
}

def current_user_profile(profile):
  user_profile["id"] = profile[0].id
  user_profile["username"] = profile[0].username
  user_profile["email"] = profile[0].email
  user_profile["date_created"] = profile[0].date_created