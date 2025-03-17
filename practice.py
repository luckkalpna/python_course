# Problem  number 01
class Programmer:
  company = "Mocrosoft"
  def __init__(self, name, salary, pin):
    self.name = name
    self.salary = salary
    self.pin = pin

p = Programmer("Kalpna", 1200000, 201001)
print(p.name, p.salary, p.pin)


s = Programmer("Shreya", 200000, 201005)
print(s.name, s.salary, s.pin)