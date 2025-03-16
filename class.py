class Employee:
  # name = "Kalpna"
  language = "Python" # This is the class attribute
  salary = 1500000

kalpna = Employee()
kalpna.name = "Kalpna" # This is the object attribute
print(kalpna.name, kalpna.language, kalpna.salary)


riya = Employee()
riya.name = "Riya" # This is the object attribute   
print(riya.name, kalpna.salary, kalpna.language)

# Here name is object attribute and salary and language are class attributes as they are directly belong to the class