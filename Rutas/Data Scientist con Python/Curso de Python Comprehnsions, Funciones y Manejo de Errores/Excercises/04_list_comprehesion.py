list_num = []
# 1st way to create a list
for element in range(1,11):
  if(element % 2 == 0):
    list_num.append(element * 2)
print(list_num)

# 2nd way (better)
list_comprehesion = [element * 2 for element in range(1,11) if element % 2 == 0]
print(list_comprehesion)
