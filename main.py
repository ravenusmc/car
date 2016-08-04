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



def main():
  print("******************")
  print("Welcome to Car!!!!")
  print("******************")
  print("Would you like to play: ")
  print("1. Yes")
  print("2. No")
  option = int(input("What is your choice? "))
  while not validMain(option):
    option = int(input("What is your choice? "))
  if option == 1:
    setup()
  elif option == 2:
    print("Thank you for trying the program!")
    print("I hope you come by again!")

main()