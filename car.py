class Car():

  def __init__(self, make, model, year):
    self.make = make 
    self.model = model
    self.year = year
    self.fuel = 0
    self.speed = 0
    self.batteryCharge = 0
    self.start = False 

  def description(self):
    print("Car Information: ")
    print("Make: " + self.make)
    print("Model: " + self.model)
    print("Year: " + str(self.year))

  def startCar(self):
    self.start == True
    print("You turned the key. The car started")

  def carReverse(self):
    print("The car rolls backwards!")

  def carForward(self):
    self.fuel -= 3
    print("The car moves forward!")


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

