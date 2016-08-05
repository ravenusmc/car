from valid import *
from human import Human
from car import Car

def car(person):
  carOne = Car("Toyota", "Prius", 2008)
  carTwo = Car("Tesla", "Model S", 2016)
  print("There are two cars two choose from: ")
  print("1. Car One")
  print("2. Car Two")
  choice = int(input("Which one do you want to look at?"))
  if choice == 1:
    carOne.description()
  elif choice == 2:
    carTwo.description()

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
  car(person)

def credits():
  print("CREDITS:")
  print("-------------------------")
  print("Creator: github user, ravenusmc")
  print("Contributors: github user, jessep13 (who made the credits and edited the 'main' function). ")
  print("-------------------------")

def main():
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

main()
