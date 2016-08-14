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

### Validation for priusDrive file 
def driveOne(choice):
  if choice == 1 or choice == 2:
    return True 
  else: 
    return False

### Validation for street function
def streetValid(choice):
  if choice == 1 or choice == 2 or choice == 3 or choice == 4:
    return True
  else:
    return False
