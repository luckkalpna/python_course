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

# def goodDay(name, ending):
#   print("Good Day, " + name)
#   print(ending)
#   return "Done"

# a = goodDay("Kalpana", "Thank You")
# print(a)

#----------Problems---------

def greatest(a, b, c):
  if(a>b and a>c):
    return a
  elif(b>c and b>a):
    return b
  elif(c>a and c>a):
    return c
  
a = 1324
b = 11234
c = 34

print(greatest(a, b, c))