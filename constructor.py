class Employee:
  language = "Python"
  salary = 1500000

# Dunder method which is automatically called
# Not talking the class data we can set as our seprate data
  def __init__(self, name, language, salary):
    self.name = name
    self.language = language
    self.salary = salary
    print("I am creating an object")

# function inside the class and set self attribute
  def getInfo(self):
    print(f"The language is: {self.language}. The salry is: {self.salary}")

  @staticmethod # Use for not pass the self object
  def greet():
    print("Good Morning")

kalpna = Employee("Kalpna", "JavaScript", 2000000)
print(kalpna.name, kalpna.language, kalpna.salary)
