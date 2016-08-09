### All of the functions for the Prius will be in this file. 
from car import Car
from valid import * 

def driveOne(person, carOne):
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
      driving(person, carOne)
    elif option == 2:
      carOne.drive()
  elif choice == 2:
    print("Sorry you are bored!!")

def house(person, carOne):
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

def street(person, carOne):
  print("You are out on the street!")
  print("What do you want to do: ")
  



