class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passengers = []

  def add_passenger(self, name):
    if not self.open_sets():
      return False
    self.passengers.append(name)
    return True

  def open_sets(self):
    return self.capacity - len(self.passengers)

flight = Flight(3)

print("check out")

people=["harry","ron","hermino","ginny"]

for person in people:
  if flight.add_passenger(person):
    print(f"add {person} to flight successfully")
  else:
    print(f"no available seats for {person}")