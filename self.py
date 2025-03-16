class Employee:
  language = "Python"
  salary = 1500000

# function inside the class and set self attribute
  def getInfo(self):
    print(f"The language is: {self.language}. The salry is: {self.salary}")

kalpna = Employee()
kalpna.getInfo()
