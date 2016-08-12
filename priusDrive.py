### All of the functions for the Prius will be in this file. 
from car import Car
from valid import * 
import random

def driveOne(person, carOne):
  print("\033c")
  print("You now have your car!")
  print("1. Cruise the roads!")
  print("2. Exit Program")
  choice = int(input("What do you want to do? "))
  if choice == 1:
    print("You enter your car. What do you want to do: ")
    print("1. Start the car")
    print("2. Drive the car")
    option = int(input("What is your choice: "))
    if option == 1:
      carOne.startCar()
      street(person, carOne)
    elif option == 2:
      carOne.drive()
  elif choice == 2:
    print("Sorry you are bored!!")

def house(person, carOne):
  print("\033c")
  print("You car is in the garage with the door behind you.")
  print("What do you want to do? ")
  print("1. Go Into Reverse")
  print("2. Go forward")
  direction = int(input("What is your choice: "))
  if direction == 1:
    carOne.carReverse()
    print("You roll out onto the street")
    street(person, carOne)
  elif direction == 2:
    carOne.carForward()
    print("You crash!!")

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

def street(person, carOne):
  print("\033c")
  print("You are driving on the street!")
  while True:
    print('\n')
    value = obstacle()
    print("1. Drive")
    print("2. Turn Right")
    print("3. Turn Left")
    print("4. Stop at Gas station")
    choice = int(input("What do you want to do: "))
    #Not sure why but using the or statement below for choices was causing issues. 
    #So I had to fully break out the if/else statements. It is ugly...I know!!!
    if value == 1 and choice == 1:
      carOne.carCrash()
      break 
    elif value == 2 and choice == 2:
      carOne.carCrash()
      break 
    elif value == 3 and choice == 3:
      carOne.carCrash()
      break 
    elif value == 1 and choice == 2:
      carOne.carTurn()
    elif value == 1 and choice == 3:
      carOne.carTurn()
    elif value == 2 and choice == 1:
      carOne.carForward()
    elif value == 2 and choice == 3:
      carOne.carTurn()
    elif value == 3 and choice == 1:
      carOne.carForward()
    elif value == 3 and choice == 2:
      carOne.carTurn()
    elif value == 4 and choice == 4:
      carOne.fillUp()
    elif value == 5 and choice == 4:
      carOne.fillUp()
    carOne.showStats()
  



