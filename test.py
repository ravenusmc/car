## Test file for my ideas

import random

def obstacle():
  value = random.randint(1,5)
  if value == 1:
    print("There is a box in the middle of the road")
  elif value == 2:
    print("A person is walking across the road from your right")
  elif value == 3:
    print("A dog ran out across from the road from your left")
  elif value == 4:
    print("You see a gas station, will you stop there?")
  elif value == 5:
    print("You see a gas station, will you stop there?")

  return value

def street():
  print("\033c")
  print("You are driving on the street!")
  while True:
    print('\n')
    value = obstacle()
    print(value)
    print("1. Drive")
    print("2. Turn Right")
    print("3. Turn Left")
    print("4. Stop at Gas station")
    choice = int(input("What do you want to do: "))
    #Not sure why but using the or statement below for choices was causing issues. 
    #So I had to fully break out the if/else statements.
    if value == 1 and choice == 1:
      print("You crashed!!!")
      break 
    elif value == 2 and choice == 2:
      print("You crashed!!!")
      break 
    elif value == 3 and choice == 3:
      print("You crashed!!!")
      break 
    elif value == 1 and choice == 2:
      print("You swerve away from the object!!")
    elif value == 1 and choice == 3:
      print("You swerve away from the object!!")
    elif value == 2 and choice == 1:
      print("You swerve away from the object!!")
    elif value == 2 and choice == 3:
      print("You swerve away from the object!!")
    elif value == 3 and choice == 1:
      print("You swerve away from the object!!")
    elif value == 3 and choice == 2:
      print("You swerve away from the object!!")
    elif value == 4 and choice == 4:
      print("You stop at the gas station and fill up your car with gas")
    elif value == 5 and choice == 4:
      print("You stop at the gas station and fill up your car with gas")


    # elif value == 2 and choice == 1 or choice == 3:
    #   print("You crashed")
    #   break
    # elif value == 2 and choice == 2:
    #   print("You swerve away from the object!!")
    # elif value == 3 and choice == 1 or choice == 3:
    #   print("You crashed")
    #   break
    # elif value == 3 and choice == 3:
    #   print("You crashed")
    #   break 
    # elif value == 3 and choice == 2:
    #   print("You swerve away from the object!!")

street()