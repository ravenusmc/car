def validMain(option):
  if option == 1 or option == 2 or option == 3:
    return True 
  else:
    return False

def validSetup(age):
  if age < 0 or age > 125:
    return False
  else:
    return True 
