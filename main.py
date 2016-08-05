from valid import *
from human import Human


def setup():
  print("\033c")
  print("Please enter in the following information: ")
  name = input("What is your name: ")
  age = int(input("What is your age: "))
  while not validSetup(age):
    age = int(input("What is your age: "))
  gender = input("what is your gender: ")
  person = Human(name, age, gender)
  person.test()

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
    print("3. Wait! Who mad this???")
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
