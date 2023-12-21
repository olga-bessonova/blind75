class Vehicle:

  # Class variable
  vehicle_count = 0

  # Constructor or initializer method
  def __init__(self, make, model, year):
    # Instance variables
    self.make = make
    self.model = model
    self.year = year
    self.is_running = False

    # Incrementing the class variable
    Vehicle.vehicle_count += 1

  # Instance method to start the vehicle
  def start(self):
    if not self.is_running:
      self.is_running = True
      return "{self.year} {self.make} {self.model} has been started."
    else:
      return "{self.year} {self.make} {self.model} is already running."
    
  # Class method to get the count of vehicles
  @classmethod
  def get_vehicle_count(cls):
    return cls.vehicle_count


# Create an instance of the class Vehicle:
c1 = Vehicle('Toyota','Corolla',2023)
c2 = Vehicle('Porche','911',1975)

print(c1.make)
print(c1.is_running)
c1.start()
print(c1.is_running)
print(Vehicle.get_vehicle_count())


  