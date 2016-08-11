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
  value = random.randint(1,3)
  if value == 1:
    print("There is a box in the middle of the road")
  if value == 2:
    print("A person is walking across the road from your right")
  if value == 3:
    print("A dog ran out across from the road")

def street(person, carOne):
  print("\033c")
  print("You are out on the street!")
  while True:
    obstacle()
    print("1. Drive")
    print("2. Brake")
    print("3. Turn Right")
    print("4. Turn Left")
    choice = int(input("What do you want to do: "))
    if value == 1 and choice == 1:
      carOne.carCrash()
      break 
    elif value == 1 and choice == 2 or choice == 3 or choice == 4:
      print("You swerved away from the object!!")
    if value == 2 and choice == 1:
      carOne.carCrash()
      break
  



