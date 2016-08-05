class Car():

  def __init__(self, make, model, year):
    self.make = make 
    self.model = model
    self.year = year
    self.fuel = 0
    self.speed = 0
    self.batteryCharge = 0

  def description(self):
    print("Car Information: ")
    print("Make: " + self.make)
    print("Model: " + self.model)
    print("Year: " + str(self.year))

class Electric(Car):

  def __init__(self, make, model, year):
    self.make = make 
    self.model = model
    self.year = year
    self.speed = 0
    self.batteryCharge = 0

