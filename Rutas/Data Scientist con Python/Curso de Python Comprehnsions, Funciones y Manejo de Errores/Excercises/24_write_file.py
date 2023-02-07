# Using the r+ we can edit the file adding more information
with open('./text.txt', "r+", encoding="UTF-8") as file:
  for line in file:
    print(line)
  file.write('nueva linea')

# Using the w+ we can edit the file, but the old information will be deleted, so the file will be overwritten with the new information added
with open('./text.txt', "w+", encoding="UTF-8") as file:
  for line in file:
    print(line)
  file.write('nueva linea')