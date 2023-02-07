file = open('./text.txt')
# Reading all the file
#print(file.read())

# Reading line per line of the file
#print('per line ====>> ' ,file.readline())

# Reading file with for
for line in file:
  print(line)
  
# Closing the file
file.close()

# Another way to read a file, in this manner the file is closed automatically whitout using the method .close()
with open('./text.txt', 'r', encoding="UTF-8") as file2:
  for line in file2:
    print(line)