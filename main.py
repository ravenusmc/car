from valid import *
from car import *
from priusDrive import *
from teslaDrive import *
from human import Human


def main():
  print("\033c")
  while True:
    print("******************")
    print("Welcome to Car!!!!")
    print("******************")
    print("Would you like to play? ")
    print("1. Yes")
    print("2. No")
    print("3. Wait! Who made this???")
    option = int(input("What is your choice: "))
    while not validMain(option):
      option = int(input("What is your choice: "))
    if option == 1:
      setup()
      exit()
    elif option == 2:
      print("Thank you for trying the program!")
      print("I hope you come by again!")
      input("PRESS ENTER TO EXIT.")
      exit()
    elif option == 3:
      credits()

def credits():
  print("CREDITS:")
  print("-------------------------")
  print("Creator: github user, ravenusmc")
  print("Contributors: github user, jessep13 (who made the credits and edited the 'main' function). ")
  print("-------------------------")

def setup():
  print("\033c")
  print("Please enter in the following information: ")
  name = input("What is your name: ")
  age = int(input("What is your age: "))
  while not validSetup(age):
    age = int(input("What is your age: "))
  gender = input("what is your gender: ")
  person = Human(name, age, gender)
  print("Now we got you set up, time to choose your car!!!")
  carInfo(person)

def carInfo(person):
  print("\033c")
  carOne = Car("Toyota", "Prius", 2008)
  carTwo = Electric("Tesla", "Model S", 2016)
  print("There are two cars two choose from: ")
  print("1. Car One")
  print("2. Car Two")
  print("3. Skip Section")
  choice = int(input("Which one do you want to look at?(3 to exit loop) "))
  while True:
    if choice == 1:
      carOne.description()
    elif choice == 2:
      carTwo.description()
    elif choice == 3:
      break 
    choice = int(input("Which one do you want to look at? "))
  print('\n')
  print("1. Car One")
  print("2. Car Two")
  selection = int(input("Please enter the number of the car you want: "))
  if selection == 1 and person.age >= 16:
    print("You choose the Toyota Prius")
    print("It also has a full tank of gas!")
    driveOne(person, carOne )
  elif selection == 2 and person.age >= 16:
    print("You choose the Tesla Model S")
    print("The battery is fully charged as well!")
    carTwo.batteryCharge = 20
    driveTwo(person, carTwo)
  elif person.age < 16:
    print("You are too young to drive! Even in this virtual world!")



main()
