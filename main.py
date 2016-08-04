from valid import *


def setup():
  print("Please enter in the following information: ")


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