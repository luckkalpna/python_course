'''
program to read any file

'''

# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

#-----------Problem_01------------
f = open("poem.txt")
content = f.read()
if("twinkle" in content):
  print("The word twinkle is present in the content")

else:
  print("The word twinkle is not present in the content")
f.close()