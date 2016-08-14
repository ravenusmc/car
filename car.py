class Car():

  def __init__(self, make, model, year):
    self.make = make 
    self.model = model
    self.year = year
    self.fuel = 20
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

  def drive(self):
    if self.start == False:
      print("You have to turn the car on!")

  def carCrash(self):
    print("The car has crashed!")

  def carTurn(self):
    print("You swerve away from the object!!")
    self.fuel -= 3

  def carForward(self):
    self.fuel -= 3
    print("You hit the gas to move forward!")

  def showStats(self):
    print("Here are the stats on your car: ")
    print("Your fuel level is: " + str(self.fuel))
    if self.fuel <= 9:
      print("You are starting to run low on gas. May want to get some next time the gas station comes up!")

class Electric(Car):

  def __init__(self, make, model, year):
    self.make = make 
    self.model = model
    self.year = year
    self.speed = 0
    self.batteryCharge = 0
    self.start = False 

  def electricTurn(self):
    print("You swerve away from the object!!")
    self.batteryCharge -= 3

  def electricForward(self):
    self.batteryCharge -= 3
    print("You hit the gas to move forward!")

  def showStatsElectric(self):
    print("Here are the stats on your car: ")
    print("Your charge level is: " + str(self.batteryCharge))
    if self.batteryCharge <= 9:
      print("You are starting to run low on battery power. You may want to get some next time the gas station comes up!")

