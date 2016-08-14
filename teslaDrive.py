### All of the functions for the Prius will be in this file. 
from car import *
from valid import * 
from gas import GasStation
import random

def driveTwo(person, carTwo):
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
      carTwo.startCar()
      house(person, carTwo)
    elif option == 2:
      carTwo.drive()
  elif choice == 2:
    print("Sorry you are bored!!")

def house(person, carTwo):
  print("\033c")
  print("You car is in the garage with the door behind you.")
  print("What do you want to do? ")
  print("1. Go Into Reverse")
  print("2. Go forward")
  direction = int(input("What is your choice: "))
  if direction == 1:
    carTwo.carReverse()
    print("You roll out onto the street")
    street(person, carTwo)
  elif direction == 2:
    carTwo.carForward()
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

def street(person, carTwo):
  print("\033c")
  print("You are driving on the street!")
  station = GasStation()
  while True:
    print('\n')
    value = obstacle()
    print("1. Drive")
    print("2. Turn Right")
    print("3. Turn Left")
    print("4. Stop at Gas station")
    choice = int(input("What do you want to do: "))
    while not streetValid(choice):
      choice = int(input("What do you want to do: "))
    #Not sure why but using the or statement below for choices was causing issues. 
    #So I had to fully break out the if/else statements. It is ugly...I know!!!
    if value == 1 and choice == 1:
      carTwo.carCrash()
      break 
    elif value == 2 and choice == 2:
      carTwo.carCrash()
      break 
    elif value == 3 and choice == 3:
      carTwo.carCrash()
      break 
    elif value == 1 and choice == 2:
      carTwo.electricTurn()
    elif value == 1 and choice == 3:
      carTwo.electricTurn()
    elif value == 2 and choice == 1:
      carTwo.electricForward()
    elif value == 2 and choice == 3:
      carTwo.electricTurn()
    elif value == 3 and choice == 1:
      carTwo.electricForward()
    elif value == 3 and choice == 2:
      carTwo.electricTurn()
    elif value == 4 and choice == 4:
      station.charge(carTwo)
    elif value == 5 and choice == 4:
      station.charge(carTwo)
    carTwo.showStatsElectric()
  



