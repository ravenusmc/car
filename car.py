class Car():

  def __init__(self, make, model, year):
    self.make = make 
    self.model = model
    self.year = year
    self.fuel = 0
    self.speed = 0
    self.batteryCharge = 0
    self.start = False 
    self.direction = forward

  def description(self):
    print("Car Information: ")
    print("Make: " + self.make)
    print("Model: " + self.model)
    print("Year: " + str(self.year))

  def startCar(self):
    self.start == True
    print("You turned the key. The car started")

  def carDirection(self):
    print("Which way do you want to go:")
    print("1. Forward")
    print("2. Reverse")
    choice = int(input("What is your option?"))
    if choice == 1:
      self.direction == forward
    elif choice == 2:
      self.direction == reverse

  def drive(self):
    if self.start == False:
      print("You have to turn the car on!")


class Electric(Car):

  def __init__(self, make, model, year):
    self.make = make 
    self.model = model
    self.year = year
    self.speed = 0
    self.batteryCharge = 0

