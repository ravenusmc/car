class Human():

  def __init__(self, name, age, gender):
    self.name = name 
    self.age = age 
    self.gender = gender

  def test(self):
    print(self.name + " is alive!")