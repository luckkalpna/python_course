class Employee:
  language = "Python"
  salary = 1500000

# function inside the class and set self attribute
  def getInfo(self):
    print(f"The language is: {self.language}. The salry is: {self.salary}")

  @staticmethod # Use for not pass the self object
  def greet():
    print("Good Morning")

kalpna = Employee()
kalpna.getInfo()
kalpna.greet()
