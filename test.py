## Test file for my ideas

import random

def obstacle():
  value = random.randint(1,3)
  if value == 1:
    print("There is a box in the middle of the road")
  elif value == 2:
    print("A person is walking across the road from your right")
  elif value == 3:
    print("A dog ran out across from the road from your left")
  return value

def street():
  print("\033c")
  print("You are out on the street!")
  while True:
    print("\033c")
    value = obstacle()
    print("1. Drive")
    print("2. Turn Right")
    print("3. Turn Left")
    choice = int(input("What do you want to do: "))
    if value == 1 and choice == 1:
      print("You crashed!!!")
      break 
    elif value == 1 and choice == 2 or choice == 3:
      print("You swerved away from the object!!")
    elif value == 2 and choice == 1 or choice == 3:
      print("You crashed")
      break
    # elif value == 2 and choice == 3:
    #   print("You swerve to the left and avoid the person")
    # elif value == 3 and choice == 1 or choice == 3:
    #   print("You crashed")
    #   break
    # elif value == 3 and choice == 2:
    #   print("You swerve to the right!")


street()