# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))

# average = (a+b+c)/2
# print(average)

# ----------function defination------------
# def avg():
#   a = int(input("Enter your number: "))
#   b = int(input("Enter your number: "))
#   c = int(input("Enter your number: "))

#   average = (a+b+c)/2
#   print(average)

# avg() # function call


# ------------Functions with arguments---------

# def goodDay(name):
#   print("Good Day, " + name)

# goodDay("Kalpana")
# goodDay("Anaya")
# goodDay("Bhargavi")

def goodDay(name, ending):
  print("Good Day, " + name)
  print(ending)
  return "Done"

a = goodDay("Kalpana", "Thank You")
print(a)