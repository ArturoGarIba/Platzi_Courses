# print(0/0) 
# print(result)

suma = lambda x, y : x + y
assert suma(2,2) == 4

print('Hola 2')

# We can create own exceptios
age = 10
if age < 18:
  raise Exception('No minors allowed')